# NI_LABVIEW_PROGRAMMING_REFERENCE

<!--SYSTEM_CORPUS id=NI_LABVIEW_PROGRAMMING_REFERENCE format=markdown generated=2026-07-14T12:02:18+00:00 -->
- title: LabVIEW Programming Reference Manual
- source: https://docs-be.ni.com/bundle/labview-api-ref/preprocessedpdf/enus
- source_sha256: 7a54c389b4f3d78e2215f55c9f156124d3668ce61d0d5018094e356004d895ac
- versions: 2024 Q1|2024 Q3|2025 Q1|2025 Q3|2026 Q1
- fidelity: full-text-records

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9001 ordinal=9001 -->
## Property and Method Reference

Property and Method Reference


 Property     Description

 Automatic    Sets or returns if the polymorphic VI automatically selects the instance.

 Polymorphic              Returns a reference to the Polymorphic VI that the subVI references. VI

 Selected      Specifies the polymorphic VI instance to select. Writing to this property removes
 Type        automatic selection.

 Selector      Returns a reference to the polymorphic VI selector for a polymorphic VI.

 Selector              Sets or returns if the polymorphic VI selector is visible. Visible

AutomaticAutomatic
AutomaticAutomatic

Sets or returns if the polymorphic VI automatically selects the instance.

If TRUE, the polymorphic VI automatically selects the instance. If FALSE, the property
manually selects the current instance.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                 No

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                                    Yes


                                                    © National Instruments 9001

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9001 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9002 ordinal=9002 -->
## Property and Method Reference

Property and Method Reference


       Remote access allowed                                                  Yes

   PolymorphicPolymorphic VIVI
   PolymorphicPolymorphic VIVI

       Returns a reference to the Polymorphic VI that the subVI references.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                                         Yes

       Need to authenticate before use                                 No

        Loads the block diagram into memory                                      Yes

       Remote access allowed                                                   Yes

   SelectedSelected TypeType
    SelectedSelected TypeType

       Specifies the polymorphic VI instance to select. Writing to this property removes
      automatic selection.


9002   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9002 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9003 ordinal=9003 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                 No

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                                    Yes

 Remote access allowed                                                  Yes

SelectorSelector
SelectorSelector

Returns a reference to the polymorphic VI selector for a polymorphic VI.

If the polymorphic VI selector is not visible, this property returns NotAReference.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

                                                    © National Instruments 9003

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9003 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9004 ordinal=9004 -->
## Property and Method Reference

Property and Method Reference


        Loads the front panel into memory                                         Yes

       Need to authenticate before use                                 No

        Loads the block diagram into memory                                      Yes

       Remote access allowed                                                   Yes

   SelectorSelector VisibleVisible
    SelectorSelector VisibleVisible

       Sets or returns if the polymorphic VI selector is visible.

           If TRUE, the polymorphic VI selector is visible.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                 No

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                                    Yes

       Remote access allowed                                                  Yes

   ConfNodeConfNode


9004   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9004 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9005 ordinal=9005 -->
## Property and Method Reference

Property and Method Reference

AbstractDynamicDispatchAbstractDynamicDispatch
DynamicDispatchSubVIDynamicDispatchSubVI
DynamicDispatchSubVIDynamicDispatchSubVI
CallParentNodeCallParentNode
CallParentNodeCallParentNode
GenericSubVIGenericSubVI
CallByRefCallByRef

CallByRef Methods

CallByRef Properties
CallByRefCallByRef MethodsMethods


 Method                         Description

                                Converts the referenced node into a standard Call By Reference
 Convert:Call By Reference
                               node.

                                Converts the referenced node into a Start Asynchronous Call
 Convert:Start Asynchronous Call
                               node.

 Convert:Wait On Asynchronous   Converts the referenced node into a Wait On Asynchronous Call
 Call                           node.


                                                    © National Instruments 9005

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9005 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9006 ordinal=9006 -->
## Property and Method Reference

Property and Method Reference

   Convert:CallConvert:Call ByBy ReferenceReference
    Convert:CallConvert:Call ByBy ReferenceReference

       Converts the referenced node into a standard Call By Reference node.

      Use this method to convert a Start Asynchronous Call node or a Wait On Asynchronous
        Call node into a Call By Reference node programmatically. To programmatically
      determine the node style of an instance of the Call By Reference class, use the Call By
       Ref Node Style property.

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

   Convert:StartConvert:Start AsynchronousAsynchronous CallCall
    Convert:StartConvert:Start AsynchronousAsynchronous CallCall

       Converts the referenced node into a Start Asynchronous Call node.

      Use this method to convert a standard Call By Reference node or a Wait On
      Asynchronous Call node into a Start Asynchronous Call node programmatically. To

9006   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9006 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9007 ordinal=9007 -->
## Property and Method Reference

Property and Method Reference

programmatically determine the node style of an instance of the Call By Reference
class, use the Call By Ref Node Style property.

This method provides the only programmatic way to create a Start Asynchronous Call
node with VI Scripting.

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                              No

 Available in Real-Time Operating System                      No

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

Convert:WaitConvert:Wait OnOn AsynchronousAsynchronous CallCall
Convert:WaitConvert:Wait OnOn AsynchronousAsynchronous CallCall

Converts the referenced node into a Wait On Asynchronous Call node.

Use this method to convert a Call By Reference node or a Start Asynchronous Call node
into a Wait On Asynchronous Call node programmatically. To programmatically
determine the node style of an instance of the Call By Reference class, use the Call By
Ref Node Style property.

This method provides the only way to create a Wait On Asynchronous Call node using
VI Scripting.


                                                    © National Instruments 9007

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9007 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9008 ordinal=9008 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

    CallByRefCallByRef PropertiesProperties


        Property   Description

          Call By Ref  Returns the style of an instance of the Call By Reference class. The possible values
       Node Style  include Call By Reference, Start Asynchronous Call, and Wait On Asynchronous Call.

    CallCall ByBy RefRef NodeNode StyleStyle
    CallCall ByBy RefRef NodeNode StyleStyle

       Returns the style of an instance of the Call By Reference class. The possible values
       include Call By Reference, Start Asynchronous Call, and Wait On Asynchronous Call.

      Use the following methods to change the style of a particular instance of the Call By
       Reference class:

            • Convert:Call By Reference
            • Convert:Start Asynchronous Call


9008   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9008 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9009 ordinal=9009 -->
## Property and Method Reference

Property and Method Reference

  • Convert:Wait On Asynchronous Call

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

UnitCastUnitCast

UnitCast Properties
UnitCastUnitCast PropertiesProperties


 Property                                 Description

 Unit                                      Unit string.

UnitUnit
UnitUnit

Unit string.

                                                    © National Instruments 9009

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9009 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9010 ordinal=9010 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    StructureStructure

       Structure Methods

       Structure Properties
    StructureStructure MethodsMethods


       Method         Description

        Auto Size       Automatically resizes the structure to fit its contents.

                    Removes the structure from the block diagram. LabVIEW merges the contents of
       Remove
                        the visible frame of the structure with the block diagram. However, LabVIEW
         Structure
                      removes the contents of the hidden frames of the structure.

        Shared
                           Directs LabVIEW to use the Allocate As Needed allocation option for reentrant VIs
         Clones:Allocate
                         within the structure.
        as Needed

        Shared          Directs LabVIEW to use the Preallocate allocation option for reentrant VIs within


9010   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9010 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9011 ordinal=9011 -->
## Property and Method Reference

Property and Method Reference


 Method         Description

 Clones:Pre-                the structure. Allocate

AutoAuto SizeSize
AutoAuto SizeSize

Automatically resizes the structure to fit its contents.

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                              No

 Available in Real-Time Operating System                      No

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

RemoveRemove StructureStructure
RemoveRemove StructureStructure

Removes the structure from the block diagram. LabVIEW merges the contents of the
visible frame of the structure with the block diagram. However, LabVIEW removes the
contents of the hidden frames of the structure.


                                                    © National Instruments 9011

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9011 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9012 ordinal=9012 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

   SharedShared Clones:AllocateClones:Allocate asas NeededNeeded
   SharedShared Clones:AllocateClones:Allocate asas NeededNeeded

       Directs LabVIEW to use the Allocate As Needed allocation option for reentrant VIs
       within the structure.

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No


9012   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9012 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9013 ordinal=9013 -->
## Property and Method Reference

Property and Method Reference


 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

SharedShared Clones:Pre-AllocateClones:Pre-Allocate
SharedShared Clones:Pre-AllocateClones:Pre-Allocate

Directs LabVIEW to use the Preallocate allocation option for reentrant VIs within the
structure.

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                             Yes

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

StructureStructure PropertiesProperties


 Property             Description

 AutoSize To Fit        Sets or returns whether the structure automatically resizes to fit its
 Contents?             contents.

 Content Rect         Returns the size of the visible portion of the subdiagram of a structure.

 Diagrams[]           Returns all subdiagrams of the structure.

                                                    © National Instruments 9013

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9013 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9014 ordinal=9014 -->
## Property and Method Reference

Property and Method Reference


        Property             Description

                              Excludes the contents of the structure when you clean up the block diagram
          Fix Contents                 if you set this property to TRUE; otherwise, includes the contents of the
                                structure in the clean up operation.

       Frame Size           Gets or sets the height and width of the structure.

        Shared
        Clones:Automatic     Indicates whether LabVIEW uses the Automatic allocation option for
         Allocation Strategy    reentrant VIs within the structure.
        Enabled

        Shared Clones:Pre-    Indicates whether LabVIEW uses the Preallocate allocation option for
         Allocate               reentrant VIs within the structure.

        Subdiagram Label                               Sets the visibility of the subdiagram label.
          Visible

         Tunnels[]            Returns an array of references to the tunnels of the loop.

   AutoSizeAutoSize ToTo FitFit Contents?Contents?
    AutoSizeAutoSize ToTo FitFit Contents?Contents?

       Sets or returns whether the structure automatically resizes to fit its contents.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                 No

        Loads the front panel into memory                              No

       Need to authenticate before use                                No


9014   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9014 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9015 ordinal=9015 -->
## Property and Method Reference

Property and Method Reference


 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

ContentContent RectRect
ContentContent RectRect

Returns the size of the visible portion of the subdiagram of a structure.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

Diagrams[]Diagrams[]
Diagrams[]Diagrams[]

Returns all subdiagrams of the structure.


                                                    © National Instruments 9015

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9015 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9016 ordinal=9016 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                                   Yes

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

   FixFix ContentsContents
    FixFix ContentsContents

       Excludes the contents of the structure when you clean up the block diagram if you set
        this property to TRUE; otherwise, includes the contents of the structure in the clean up
       operation.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                 No

9016   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9016 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9017 ordinal=9017 -->
## Property and Method Reference

Property and Method Reference


 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

FrameFrame SizeSize
FrameFrame SizeSize

Gets or sets the height and width of the structure.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes


                                                    © National Instruments 9017

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9017 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9018 ordinal=9018 -->
## Property and Method Reference

Property and Method Reference

   SharedShared Clones:AutomaticClones:Automatic AllocationAllocation
   StrategyStrategy EnabledEnabled
   SharedShared Clones:AutomaticClones:Automatic AllocationAllocation StrategyStrategy
   EnabledEnabled

       Indicates whether LabVIEW uses the Automatic allocation option for reentrant VIs
       within the structure.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                 No

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   SharedShared Clones:Pre-AllocateClones:Pre-Allocate
   SharedShared Clones:Pre-AllocateClones:Pre-Allocate

       Indicates whether LabVIEW uses the Preallocate allocation option for reentrant VIs
       within the structure.

9018   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9018 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9019 ordinal=9019 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

SubdiagramSubdiagram LabelLabel VisibleVisible
SubdiagramSubdiagram LabelLabel VisibleVisible

Sets the visibility of the subdiagram label.

This property is similar to the Visible Items»Subdiagram Label item on the shortcut
menu of a structure. This property is also similar to the Subdiagram label visible
option on the Appearance page of the Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No


                                                    © National Instruments 9019

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9019 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9020 ordinal=9020 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                          No

         Settable when the VI is running                                 No

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   Tunnels[]Tunnels[]
    Tunnels[]Tunnels[]

       Returns an array of references to the tunnels of the loop.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

   LoopLoop

      Loop Methods

9020   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9020 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9021 ordinal=9021 -->
## Property and Method Reference

Property and Method Reference

Loop Properties
LoopLoop MethodsMethods
LoopLoop MethodsMethods


 Method       Description

 Add Shift     Adds a shift register at the specified location on the frame of the loop. The position
 Register         is relative to the frame.

AddAdd ShiftShift RegisterRegister
AddAdd ShiftShift RegisterRegister

Adds a shift register at the specified location on the frame of the loop. The position is
relative to the frame.

Parameters

         Data Name           Required  Description         type

 Y                             Specifies the position relative to the frame of the loop at which to
                  Yes
 Position                 add the shift register.


Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                         No


                                                    © National Instruments 9021

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9021 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9022 ordinal=9022 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                                 No

         Settable when the VI is running                                        No

        Loads the front panel into memory                                     No

       Need to authenticate before use                                       No

        Loads the block diagram into memory                                   No

       Remote access allowed                                                           Yes

   LoopLoop PropertiesProperties
   LoopLoop PropertiesProperties


        Property            Description

        Diagram            Returns a reference to the diagram of the loop.

       Loop Counter       Returns a reference to the loop counter.

          Shift Registers[]     Returns an array of references to the shift registers of the loop.

   DiagramDiagram
   DiagramDiagram

       Returns a reference to the diagram of the loop.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                   No


9022   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9022 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9023 ordinal=9023 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

LoopLoop CounterCounter
LoopLoop CounterCounter

Returns a reference to the loop counter.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes


                                                    © National Instruments 9023

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9023 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9024 ordinal=9024 -->
## Property and Method Reference

Property and Method Reference

    ShiftShift Registers[]Registers[]
    ShiftShift Registers[]Registers[]

       Returns an array of references to the shift registers of the loop.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

   ForLoopForLoop
   ForLoopForLoop

      ForLoop Properties
   ForLoopForLoop PropertiesProperties
   ForLoopForLoop PropertiesProperties


9024   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9024 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9025 ordinal=9025 -->
## Property and Method Reference

Property and Method Reference


Property    Description

Chunk Size            Returns a reference to the chunk size (C) terminal of the For Loop.Tunnel

Dynamic
Parallel     Returns a reference to the tunnel for the dynamic number of parallel instances of the
Instances    For Loop.
Tunnel

             Creates the conditional terminal if you set this property TRUE. If the conditional
Has         terminal already exists, this property does nothing and does not return an error. If you
Conditional  set this property to FALSE, this property removes the conditional terminal, possibly
Terminal?   leaving broken wires. If the conditional terminal does not already exist, this property
           does nothing and does not return an error.

Is                    If TRUE, allows debugging inside the For Loop by setting the loop iterations to runDebugging              sequentially. If FALSE, debugging is not allowed in the For Loop.
Allowed

                    If TRUE, this property enables parallel loop iterations. If parallel loop iterations
Is           already are enabled, this property does nothing, and LabVIEW does not return an
Parallelism   error. If FALSE, this property disables parallel loop iterations, which might break wires.
Enabled?      If parallel loop iterations already are disabled, this property does nothing, and
           LabVIEW does not return an error.

Iteration            Hides the iteration terminal if you set this property TRUE. Returns an error if you try toTerminal
            hide the iteration terminal when it is wired.Hidden?

Loop Count  Returns a reference to the loop count.

Loop End            Returns a reference to the end terminal of the For Loop.Ref

Number of
Static
             Specifies the number of loop instances LabVIEW uses to run parallel loop iterations.
Parallel
Instances

Parallel
             Sets the parallel loop iteration schedule of the For Loop when you enable parallelism.
Schedule

Stop If
             Specifies whether the For Loop stops if you wire TRUE to the end terminal of the loop.
True?


                                                    © National Instruments 9025

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9025 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9026 ordinal=9026 -->
## Property and Method Reference

Property and Method Reference

   ChunkChunk SizeSize TunnelTunnel
   ChunkChunk SizeSize TunnelTunnel

       Returns a reference to the chunk size (C) terminal of the For Loop.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                                         Yes

       Need to authenticate before use                                 No

        Loads the block diagram into memory                                      Yes

       Remote access allowed                                                   Yes

   DynamicDynamic ParallelParallel InstancesInstances TunnelTunnel
   DynamicDynamic ParallelParallel InstancesInstances TunnelTunnel

       Returns a reference to the tunnel for the dynamic number of parallel instances of the
       For Loop.

     Remarks

      The following table lists the characteristics of this property.


9026   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9026 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9027 ordinal=9027 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                                         Yes

 Need to authenticate before use                                 No

 Loads the block diagram into memory                                      Yes

 Remote access allowed                                                   Yes

HasHas ConditionalConditional Terminal?Terminal?
HasHas ConditionalConditional Terminal?Terminal?

Creates the conditional terminal if you set this property TRUE. If the conditional
terminal already exists, this property does nothing and does not return an error. If you
set this property to FALSE, this property removes the conditional terminal, possibly
leaving broken wires. If the conditional terminal does not already exist, this property
does nothing and does not return an error.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                 No

 Loads the front panel into memory                                       Yes


                                                    © National Instruments 9027

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9027 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9028 ordinal=9028 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                                No

        Loads the block diagram into memory                                    Yes

       Remote access allowed                                                  Yes

    IsIs DebuggingDebugging AllowedAllowed
     IsIs DebuggingDebugging AllowedAllowed

           If TRUE, allows debugging inside the For Loop by setting the loop iterations to run
       sequentially. If FALSE, debugging is not allowed in the For Loop.

       This property applies only to For Loops with parallel loop iterations enabled.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                 No

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                                    Yes

       Remote access allowed                                                  Yes


9028   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9028 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9029 ordinal=9029 -->
## Property and Method Reference

Property and Method Reference

IsIs ParallelismParallelism Enabled?Enabled?
IsIs ParallelismParallelism Enabled?Enabled?

If TRUE, this property enables parallel loop iterations. If parallel loop iterations already
are enabled, this property does nothing, and LabVIEW does not return an error. If
FALSE, this property disables parallel loop iterations, which might break wires. If
parallel loop iterations already are disabled, this property does nothing, and LabVIEW
does not return an error.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                 No

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                                    Yes

 Remote access allowed                                                  Yes

IterationIteration TerminalTerminal Hidden?Hidden?
IterationIteration TerminalTerminal Hidden?Hidden?

Hides the iteration terminal if you set this property TRUE. Returns an error if you try to
hide the iteration terminal when it is wired.


                                                    © National Instruments 9029

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9029 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9030 ordinal=9030 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                 No

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                                    Yes

       Remote access allowed                                                  Yes

   LoopLoop CountCount
   LoopLoop CountCount

       Returns a reference to the loop count.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No


9030   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9030 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9031 ordinal=9031 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

LoopLoop EndEnd RefRef
LoopLoop EndEnd RefRef

Returns a reference to the end terminal of the For Loop.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

NumberNumber ofof StaticStatic ParallelParallel InstancesInstances
NumberNumber ofof StaticStatic ParallelParallel InstancesInstances

Specifies the number of loop instances LabVIEW uses to run parallel loop iterations.


                                                    © National Instruments 9031

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9031 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9032 ordinal=9032 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                 No

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                                    Yes

       Remote access allowed                                                  Yes

    ParallelParallel ScheduleSchedule
    ParallelParallel ScheduleSchedule

       Sets the parallel loop iteration schedule of the For Loop when you enable parallelism.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                 No

        Loads the front panel into memory                                       Yes


9032   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9032 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9033 ordinal=9033 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                                No

 Loads the block diagram into memory                                    Yes

 Remote access allowed                                                  Yes

StopStop IfIf True?True?
StopStop IfIf True?True?

Specifies whether the For Loop stops if you wire TRUE to the end terminal of the loop.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                 No

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

WhileLoopWhileLoop
WhileLoopWhileLoop

WhileLoop Methods


                                                    © National Instruments 9033

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9033 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9034 ordinal=9034 -->
## Property and Method Reference

Property and Method Reference

      WhileLoop Properties
   WhileLoopWhileLoop MethodsMethods
   WhileLoopWhileLoop MethodsMethods


       Method                           Description

        Replace With TimeLoop            Replaces a While Loop with a Timed Loop.

   ReplaceReplace WithWith TimeLoopTimeLoop
   ReplaceReplace WithWith TimeLoopTimeLoop

       Replaces a While Loop with a Timed Loop.

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes


9034   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9034 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9035 ordinal=9035 -->
## Property and Method Reference

Property and Method Reference

WhileLoopWhileLoop PropertiesProperties
WhileLoopWhileLoop PropertiesProperties


 Property        Description

 Iteration                 Hides the iteration terminal if you set this property TRUE. Returns an error if you Terminal                    try to hide the iteration terminal when it is wired. Hidden?

 Loop End Ref    Returns a reference to the end terminal of the While Loop.

                   Specifies whether the While Loop stops if you wire TRUE to the end terminal of Stop If True?                 the loop.

IterationIteration TerminalTerminal Hidden?Hidden?
IterationIteration TerminalTerminal Hidden?Hidden?

Hides the iteration terminal if you set this property TRUE. Returns an error if you try to
hide the iteration terminal when it is wired.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                 No

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No


                                                    © National Instruments 9035

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9035 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9036 ordinal=9036 -->
## Property and Method Reference

Property and Method Reference


        Loads the block diagram into memory                                    Yes

       Remote access allowed                                                  Yes

   LoopLoop EndEnd RefRef
   LoopLoop EndEnd RefRef

       Returns a reference to the end terminal of the While Loop.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

   StopStop IfIf True?True?
   StopStop IfIf True?True?

       Specifies whether the While Loop stops if you wire TRUE to the end terminal of the
       loop.


9036   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9036 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9037 ordinal=9037 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                 No

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

TimedLoopTimedLoop
TimedLoopTimedLoop

TimedLoop Methods
TimedLoopTimedLoop MethodsMethods
TimedLoopTimedLoop MethodsMethods


 Method             Description

 Replace With        Replaces a Timed Loop with a Timed Sequence structure and returns a
 TimedSequence     reference of the Timed Sequence structure.

 Replace With        Replaces a Timed Loop with a While Loop and returns a reference to the While
 WhileLoop          Loop.


                                                    © National Instruments 9037

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9037 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9038 ordinal=9038 -->
## Property and Method Reference

Property and Method Reference

   ReplaceReplace WithWith TimedSequenceTimedSequence
   ReplaceReplace WithWith TimedSequenceTimedSequence

       Replaces a Timed Loop with a Timed Sequence structure and returns a reference of the
      Timed Sequence structure.

     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                                      Yes

         Available in Real-Time Operating System                                            Yes

         Settable when the VI is running                                        No

        Loads the front panel into memory                                     No

       Need to authenticate before use                                       No

        Loads the block diagram into memory                                   No

       Remote access allowed                                                           Yes

   ReplaceReplace WithWith WhileLoopWhileLoop
   ReplaceReplace WithWith WhileLoopWhileLoop

       Replaces a Timed Loop with a While Loop and returns a reference to the While Loop.

     Remarks

      The following table lists the characteristics of this method.


        Data type


9038   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9038 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9039 ordinal=9039 -->
## Property and Method Reference

Property and Method Reference


 Available in Run-Time Engine                                                      Yes

 Available in Real-Time Operating System                                            Yes

 Settable when the VI is running                                        No

 Loads the front panel into memory                                     No

 Need to authenticate before use                                       No

 Loads the block diagram into memory                                   No

 Remote access allowed                                                           Yes

MultiFrameStructureMultiFrameStructure

MultiFrameStructure Methods

MultiFrameStructure Properties
MultiFrameStructureMultiFrameStructure MethodsMethods
MultiFrameStructureMultiFrameStructure MethodsMethods


 Method            Description

                 Adds a new frame before or after the frame whose index you specify and Add Frame                     returns a reference to the new frame.

 Duplicate Frame    Duplicates the frame you specify and returns a reference to the new frame.

                   Rearranges the frames of the structure according to the order you specify in
 Rearrange Frames
                 Frame References.

 Rearrange Frames  Rearranges the frames of the structure according to the order you specify in
 By Index           Index Array.

                 Removes the frame you specify. LabVIEW also removes the contents of the
 Remove Frame
                    frame.


                                                    © National Instruments 9039

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9039 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9040 ordinal=9040 -->
## Property and Method Reference

Property and Method Reference

   AddAdd FrameFrame
   AddAdd FrameFrame

      Adds a new frame before or after the frame whose index you specify and returns a
       reference to the new frame.

     Parameters

                  Data      Name           Required  Description                   type

         Reference
                                        Specifies the index of the frame beside which you want to add the       Frame         No                            new frame.         Index


                                                           If TRUE (default), LabVIEW adds the frame after Reference Frame
          After? (T)       No        Index. If FALSE, LabVIEW adds the frame before Reference Frame
                                     Index.


     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                         No

         Available in Real-Time Operating System                                 No

         Settable when the VI is running                                        No

        Loads the front panel into memory                                     No

       Need to authenticate before use                                       No

        Loads the block diagram into memory                                   No

       Remote access allowed                                                           Yes


9040   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9040 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9041 ordinal=9041 -->
## Property and Method Reference

Property and Method Reference

DuplicateDuplicate FrameFrame
DuplicateDuplicate FrameFrame

Duplicates the frame you specify and returns a reference to the new frame.

Parameters

 Name            Data type      Required      Description

 Frame Index                       Yes             Specifies the index of the frame.


Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                         No

 Available in Real-Time Operating System                                 No

 Settable when the VI is running                                        No

 Loads the front panel into memory                                     No

 Need to authenticate before use                                       No

 Loads the block diagram into memory                                   No

 Remote access allowed                                                           Yes

RearrangeRearrange FramesFrames
RearrangeRearrange FramesFrames

Rearranges the frames of the structure according to the order you specify in Frame

                                                    © National Instruments 9041

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9041 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9042 ordinal=9042 -->
## Property and Method Reference

Property and Method Reference

       References.

     Parameters

      Name              Data type   Required    Description

       Frame References                  Yes          Specifies the desired order of the frames.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

   RearrangeRearrange FramesFrames ByBy IndexIndex
   RearrangeRearrange FramesFrames ByBy IndexIndex

       Rearranges the frames of the structure according to the order you specify in Index
       Array.


9042   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9042 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9043 ordinal=9043 -->
## Property and Method Reference

Property and Method Reference

Parameters

 Name         Data type    Required     Description

 Index Array                   Yes           Specifies the desired order of the frames.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                             Yes

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

RemoveRemove FrameFrame
RemoveRemove FrameFrame

Removes the frame you specify. LabVIEW also removes the contents of the frame.

Parameters

 Name            Data type      Required      Description

 Frame Index                       Yes             Specifies the index of the frame.


                                                    © National Instruments 9043

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9043 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9044 ordinal=9044 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

   MultiFrameStructureMultiFrameStructure PropertiesProperties
    MultiFrameStructureMultiFrameStructure PropertiesProperties


        Property           Description

       Frame Count        Returns the number of frames in the structure.

       Frame Selector                            Returns the bounds of the selector label of the structure.         Rect

         Frames[]           Returns an array of references to the frames of the structure.

                            Returns the index to the visible frame of the structure, where 0 is the first
          Visible Frame
                            frame.

   FrameFrame CountCount
   FrameFrame CountCount

       Returns the number of frames in the structure.

9044   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9044 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9045 ordinal=9045 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

FrameFrame SelectorSelector RectRect
FrameFrame SelectorSelector RectRect

Returns the bounds of the selector label of the structure.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No


                                                    © National Instruments 9045

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9045 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9046 ordinal=9046 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

   Frames[]Frames[]
    Frames[]Frames[]

       Returns an array of references to the frames of the structure.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

    VisibleVisible FrameFrame
    VisibleVisible FrameFrame

       Returns the index to the visible frame of the structure, where 0 is the first frame.


9046   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9046 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9047 ordinal=9047 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

SequenceSequence
SequenceSequence

Sequence Methods

Sequence Properties
SequenceSequence MethodsMethods
SequenceSequence MethodsMethods


 Method   Description

 Convert   Converts a Stacked Sequence structure into a Flat Sequence structure and returns a
 To Flat     reference to the Flat Sequence structure. This method automatically closes the
 Sequence  reference to the Stacked Sequence structure.


                                                    © National Instruments 9047

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9047 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9048 ordinal=9048 -->
## Property and Method Reference

Property and Method Reference

   ConvertConvert ToTo FlatFlat SequenceSequence
   ConvertConvert ToTo FlatFlat SequenceSequence

       Converts a Stacked Sequence structure into a Flat Sequence structure and returns a
       reference to the Flat Sequence structure. This method automatically closes the
       reference to the Stacked Sequence structure.

     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                                      Yes

         Available in Real-Time Operating System                                            Yes

         Settable when the VI is running                                        No

        Loads the front panel into memory                                     No

       Need to authenticate before use                                       No

        Loads the block diagram into memory                                   No

       Remote access allowed                                                           Yes

   SequenceSequence PropertiesProperties
   SequenceSequence PropertiesProperties


        Property       Description

        Sequence      Returns an array of references to the sequence local terminals of the Stacked
          Locals[]       Sequence structure.


9048   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9048 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9049 ordinal=9049 -->
## Property and Method Reference

Property and Method Reference

SequenceSequence Locals[]Locals[]
SequenceSequence Locals[]Locals[]

Returns an array of references to the sequence local terminals of the Stacked
Sequence structure.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

ExternalNodeExternalNode
ExternalNodeExternalNode
CaseStructureCaseStructure
CaseStructureCaseStructure


                                                    © National Instruments 9049

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9049 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9050 ordinal=9050 -->
## Property and Method Reference

Property and Method Reference

       CaseStructure Methods

       CaseStructure Properties
   CaseStructureCaseStructure MethodsMethods
    CaseStructureCaseStructure MethodsMethods


       Method          Description

                         Returns the index of the Case structure subdiagram whose Frame Name matches        Get Frame Index                         the string you specify.

       Remove Default  Removes the default case from the Case structure.

       Remove Empty                     Removes the empty frames of the Case structure.        Cases

         Set Default Case  Sets the default case of the Case structure.

   GetGet FrameFrame IndexIndex
   GetGet FrameFrame IndexIndex

       Returns the index of the Case structure subdiagram whose Frame Name matches the
        string you specify.

     Parameters

                 Data
      Name            Required  Description
                  type

       Frame                         Specifies the name of the subdiagram for which you want LabVIEW
                            Yes
      Name                         to return the index.


9050   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9050 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9051 ordinal=9051 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                                      Yes

 Available in Real-Time Operating System                                            Yes

 Settable when the VI is running                                        No

 Loads the front panel into memory                                     No

 Need to authenticate before use                                       No

 Loads the block diagram into memory                                   No

 Remote access allowed                                                           Yes

RemoveRemove DefaultDefault
RemoveRemove DefaultDefault

Removes the default case from the Case structure.

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                              No

 Available in Real-Time Operating System                      No

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No


                                                    © National Instruments 9051

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9051 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9052 ordinal=9052 -->
## Property and Method Reference

Property and Method Reference


       Remote access allowed                                             Yes

   RemoveRemove EmptyEmpty CasesCases
   RemoveRemove EmptyEmpty CasesCases

      Removes the empty frames of the Case structure.

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

   SetSet DefaultDefault CaseCase
    SetSet DefaultDefault CaseCase

       Sets the default case of the Case structure.


9052   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9052 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9053 ordinal=9053 -->
## Property and Method Reference

Property and Method Reference

Parameters

 Name       Data type   Required   Description

 Case Index            No         Index of the case you want to specify as the default.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                              No

 Available in Real-Time Operating System                      No

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

CaseStructureCaseStructure PropertiesProperties
CaseStructureCaseStructure PropertiesProperties


 Property          Description

 Case Insensitive    Specifies whether this Case structure performs case insensitive matching when
 Match           comparing strings.

 Default Case       Specifies the default case of the Case structure.

 Frame Names     Gets or sets the name of the frame of the Case structure.

 Selector          Returns a reference to the case selector of the Case structure.


                                                    © National Instruments 9053

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9053 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9054 ordinal=9054 -->
## Property and Method Reference

Property and Method Reference

   CaseCase InsensitiveInsensitive MatchMatch
   CaseCase InsensitiveInsensitive MatchMatch

       Specifies whether this Case structure performs case insensitive matching when
      comparing strings.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                 No

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                                    Yes

       Remote access allowed                                                  Yes

   DefaultDefault CaseCase
    DefaultDefault CaseCase

       Specifies the default case of the Case structure.

     Remarks

      The following table lists the characteristics of this property.


9054   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9054 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9055 ordinal=9055 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

FrameFrame NamesNames
FrameFrame NamesNames

Gets or sets the name of the frame of the Case structure.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes


                                                    © National Instruments 9055

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9055 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9056 ordinal=9056 -->
## Property and Method Reference

Property and Method Reference

   SelectorSelector
    SelectorSelector

       Returns a reference to the case selector of the Case structure.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

   EventStructureEventStructure
    EventStructureEventStructure

       EventStructure Methods

       EventStructure Properties


9056   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9056 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9057 ordinal=9057 -->
## Property and Method Reference

Property and Method Reference

EventStructureEventStructure MethodsMethods
EventStructureEventStructure MethodsMethods


 Method    Description

 Get Event           Gets a reference to the Event Data Node on the Event structure at the given event case Data            index. Node

 Get Event
           Gets a reference to the Event Filter Node on the Event structure at the given event case Filter            index. If the event case handles a notify event, this property returns a NULL reference. Node

 Get
           Gets all events configured for a given frame, or event case, to handle. This method Handled            returns the events in separate outputs grouped by registration type and refnum class. Events

 Set
 Handled   Sets all events configured for the given the frame, or event case, to handle.
 Events

GetGet EventEvent DataData NodeNode
GetGet EventEvent DataData NodeNode

Gets a reference to the Event Data Node on the Event structure at the given event case
index.

The Event Data Node identifies the data LabVIEW returns when an event occurs.

Parameters

          Data
 Name            Required  Description
          type

 Frame
              No        Specifies the index for the frame, or event case, that contains the
 Index

                                                    © National Instruments 9057

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9057 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9058 ordinal=9058 -->
## Property and Method Reference

Property and Method Reference


                 Data      Name            Required  Description
                 type

                               node you want to return.


     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                         No

         Available in Real-Time Operating System                                 No

         Settable when the VI is running                                        No

        Loads the front panel into memory                                                 Yes

       Need to authenticate before use                                       No

        Loads the block diagram into memory                                              Yes

       Remote access allowed                                                           Yes

   GetGet EventEvent FilterFilter NodeNode
   GetGet EventEvent FilterFilter NodeNode

       Gets a reference to the Event Filter Node on the Event structure at the given event case
       index. If the event case handles a notify event, this property returns a NULL reference.

      The Event Filter Node identifies the event data you can modify before the user
        interface can process that data.


9058   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9058 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9059 ordinal=9059 -->
## Property and Method Reference

Property and Method Reference

Parameters

         Data Name          Required  Description
         type

 Frame                       Specifies the index for the frame, or event case, that contains the             No Index                     Event Filter Node you want to return.


Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                         No

 Available in Real-Time Operating System                                 No

 Settable when the VI is running                                        No

 Loads the front panel into memory                                                 Yes

 Need to authenticate before use                                       No

 Loads the block diagram into memory                                              Yes

 Remote access allowed                                                           Yes

GetGet HandledHandled EventsEvents
GetGet HandledHandled EventsEvents

Gets all events configured for a given frame, or event case, to handle. This method
returns the events in separate outputs grouped by registration type and refnum class.


                                                    © National Instruments 9059

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9059 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9060 ordinal=9060 -->
## Property and Method Reference

Property and Method Reference

     Parameters

                 Data      Name         Required  Description
                 type

       Frame                      Specifies the index for the frame, or event case, that contains the                        Yes         Index                     configured events you want to return.


          Static                    Returns an array of clusters containing the application or VI event type
        App/VI         Yes        for events statically handled by the given event case, the lossy queue
        Events                         limit, and whether the front panel locks until the event case completes.


                                  Returns an array of clusters containing each statically handled control          Static                                   or pane event type, the GObject refnum of the associated control, the
         Control         Yes                                     lossy event limit count for the event type, and whether the front panel        Events                                    locks until the event case completes.


       Dynamic                 Returns an array of clusters containing the dynamic event type and the                        Yes        Events                   order that dynamic events are registered.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

         Settable when the VI is running                             No

        Loads the front panel into memory                                  Yes

       Need to authenticate before use                            No

        Loads the block diagram into memory                               Yes

       Remote access allowed                                             Yes

9060   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9060 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9061 ordinal=9061 -->
## Property and Method Reference

Property and Method Reference

SetSet HandledHandled EventsEvents
SetSet HandledHandled EventsEvents

Sets all events configured for the given the frame, or event case, to handle.

Parameters

         Data Name         Required  Description          type

 Frame                      Specifies the index for the frame, or event case, that contains the
                Yes Index                     configured events you want to set.


 Static                      Specifies an array of clusters containing the application or VI event type
 App/VI       No         for events statically handled by the given event case, the lossy queue
 Events                         limit, and whether the front panel locks until the event case completes.


                             Specifies an array of clusters containing each statically handled control
 Static                           or pane event type, the GObject refnum of the associated control, the Control       No
                            lossy event limit count for the event type, and whether the front panel Events                            locks until the event case completes.


 Dynamic                   Specifies an array of clusters containing the dynamic event type and
            No
 Events                   the order that dynamic events are registered.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                              No


                                                    © National Instruments 9061

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9061 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9062 ordinal=9062 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                      No

         Settable when the VI is running                             No

        Loads the front panel into memory                                  Yes

       Need to authenticate before use                            No

        Loads the block diagram into memory                               Yes

       Remote access allowed                                             Yes

   EventStructureEventStructure PropertiesProperties
    EventStructureEventStructure PropertiesProperties


        Property                Description

                                Gets a reference to the dynamic terminal on the left side of the Event
       Dynamic Terminal (Left)                                     structure.

       Dynamic Terminal       Gets a reference to the dynamic terminal on the right side of the Event
          (Right)                    structure.

       Dynamic Terminals
                                  Sets whether the Event structure dynamic terminals are visible.          Visible?

        Event Selectors          Gets the human-readable names of the Event structure cases.

                                Gets the number of subdiagrams, or event cases, owned by the Event       Number of Event Frames                                     structure.

        Timeout Terminal        Gets a reference to the Timeout terminal of the Event structure.

   DynamicDynamic TerminalTerminal (Left)(Left)
   DynamicDynamic TerminalTerminal (Left)(Left)

       Gets a reference to the dynamic terminal on the left side of the Event structure.


9062   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9062 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9063 ordinal=9063 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                                         Yes

 Need to authenticate before use                                 No

 Loads the block diagram into memory                                      Yes

 Remote access allowed                                                   Yes

DynamicDynamic TerminalTerminal (Right)(Right)
DynamicDynamic TerminalTerminal (Right)(Right)

Gets a reference to the dynamic terminal on the right side of the Event structure.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                                         Yes


                                                    © National Instruments 9063

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9063 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9064 ordinal=9064 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                                 No

        Loads the block diagram into memory                                      Yes

       Remote access allowed                                                   Yes

   DynamicDynamic TerminalsTerminals Visible?Visible?
   DynamicDynamic TerminalsTerminals Visible?Visible?

       Sets whether the Event structure dynamic terminals are visible.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                 No

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                                    Yes

       Remote access allowed                                                  Yes

   EventEvent SelectorsSelectors
   EventEvent SelectorsSelectors

       Gets the human-readable names of the Event structure cases.


9064   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9064 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9065 ordinal=9065 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                                         Yes

 Need to authenticate before use                                 No

 Loads the block diagram into memory                                      Yes

 Remote access allowed                                                   Yes

NumberNumber ofof EventEvent FramesFrames
NumberNumber ofof EventEvent FramesFrames

Gets the number of subdiagrams, or event cases, owned by the Event structure.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                                         Yes


                                                    © National Instruments 9065

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9065 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9066 ordinal=9066 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                                 No

        Loads the block diagram into memory                                      Yes

       Remote access allowed                                                   Yes

   TimeoutTimeout TerminalTerminal
   TimeoutTimeout TerminalTerminal

       Gets a reference to the Timeout terminal of the Event structure.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                                         Yes

       Need to authenticate before use                                 No

        Loads the block diagram into memory                                      Yes

       Remote access allowed                                                   Yes

   DisableStructureDisableStructure
    DisableStructureDisableStructure

       DisableStructure Methods


9066   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9066 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9067 ordinal=9067 -->
## Property and Method Reference

Property and Method Reference

DisableStructure Properties
DisableStructureDisableStructure MethodsMethods
DisableStructureDisableStructure MethodsMethods


 Method        Description

 Change       Changes the disable structure to a Diagram Disable structure, a Conditional Disable
 Disable Style   structure, or a Type Specialization structure.

 Get Frame     Returns the index of the Conditional Disable structure subdiagram whose
 Index         Condition matches the string you specify.

 Remove      Removes any empty subdiagrams from the Conditional Disable structure you
 Empty Frames  specify.

ChangeChange DisableDisable StyleStyle
ChangeChange DisableDisable StyleStyle

Changes the disable structure to a Diagram Disable structure, a Conditional Disable
structure, or a Type Specialization structure.

Parameters

        Data
 Name        Required  Description
         type

                         Disable Style—Specifies the type of structure to which you want to
                           convert.
 Disable
               Yes
 Style                            Conditional Disable Style—Changes a Diagram Disable structure or
                        0
                          a Type Specialization structure to a Conditional Disable structure.


                                                    © National Instruments 9067

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9067 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9068 ordinal=9068 -->
## Property and Method Reference

Property and Method Reference


                Data      Name        Required  Description
                type


                                Diagram Disable Style—Changes a Conditional Disable structure or                               1                                 a Type Specialization structure to a Diagram Disable structure.

                                Type Specialization Style—Changes a Conditional Disable structure                               2
                                     or a Diagram Disable structure to a Type Specialization structure.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                      No

         Settable when the VI is running                             No

        Loads the front panel into memory                                  Yes

       Need to authenticate before use                            No

        Loads the block diagram into memory                               Yes

       Remote access allowed                                             Yes

   GetGet FrameFrame IndexIndex
   GetGet FrameFrame IndexIndex

       Returns the index of the Conditional Disable structure subdiagram whose Condition
      matches the string you specify.


9068   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9068 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9069 ordinal=9069 -->
## Property and Method Reference

Property and Method Reference

Parameters

 Name     Data type  Required  Description

 Condition             Yes        Specifies the condition whose subdiagram you want to return.


Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                                      Yes

 Available in Real-Time Operating System                                 No

 Settable when the VI is running                                        No

 Loads the front panel into memory                                                 Yes

 Need to authenticate before use                                       No

 Loads the block diagram into memory                                              Yes

 Remote access allowed                                                           Yes

RemoveRemove EmptyEmpty FramesFrames
RemoveRemove EmptyEmpty FramesFrames

Removes any empty subdiagrams from the Conditional Disable structure you specify.

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

                                                    © National Instruments 9069

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9069 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9070 ordinal=9070 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                      No

         Settable when the VI is running                             No

        Loads the front panel into memory                                  Yes

       Need to authenticate before use                            No

        Loads the block diagram into memory                               Yes

       Remote access allowed                                             Yes

   DisableStructureDisableStructure PropertiesProperties
    DisableStructureDisableStructure PropertiesProperties


        Property   Description

         Active      Returns the index of the Conditional Disable structure subdiagram that is currently
       Frame       active, or the subdiagram whose conditions the block diagram code meets.

                    Gets or sets an array of the strings that define the condition for each Conditional
         Conditions                     Disable structure subdiagram.

         Default
                    Gets or sets the index of the default subdiagram of a Conditional Disable structure.       Frame

                  Reads whether this structure is a Diagram Disable structure, a Conditional Disable
         Disable                       structure, or a Type Specialization structure. This property is read-only. To change the         Style                    type of structure, use the Change Disable Style method.

   ActiveActive FrameFrame
    ActiveActive FrameFrame

       Returns the index of the Conditional Disable structure subdiagram that is currently
        active, or the subdiagram whose conditions the block diagram code meets.


9070   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9070 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9071 ordinal=9071 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                                    Yes

 Remote access allowed                                                  Yes

ConditionsConditions
ConditionsConditions

Gets or sets an array of the strings that define the condition for each Conditional
Disable structure subdiagram.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes


                                                    © National Instruments 9071

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9071 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9072 ordinal=9072 -->
## Property and Method Reference

Property and Method Reference


        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                                    Yes

       Remote access allowed                                                  Yes

   DefaultDefault FrameFrame
    DefaultDefault FrameFrame

       Gets or sets the index of the default subdiagram of a Conditional Disable structure.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                                    Yes

       Remote access allowed                                                  Yes

   DisableDisable StyleStyle
    DisableDisable StyleStyle

      Reads whether this structure is a Diagram Disable structure, a Conditional Disable

9072   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9072 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9073 ordinal=9073 -->
## Property and Method Reference

Property and Method Reference

structure, or a Type Specialization structure. This property is read-only. To change the
type of structure, use the Change Disable Style method.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                                         Yes

 Need to authenticate before use                                 No

 Loads the block diagram into memory                                      Yes

 Remote access allowed                                                   Yes

RaceStructureNodeRaceStructureNode
RaceStructureNodeRaceStructureNode
SimulationNodeSimulationNode

SimulationNode Properties
SimulationNodeSimulationNode PropertiesProperties
SimulationNodeSimulationNode PropertiesProperties


                                                    © National Instruments 9073

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9073 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9074 ordinal=9074 -->
## Property and Method Reference

Property and Method Reference


        Property          Description

        SIMConfigNode   Returns a reference to the input node for the Control & Simulation Loop.

        SIMOutputNode   Returns a reference to the output node for the Control & Simulation Loop.

   SIMConfigNodeSIMConfigNode
   SIMConfigNodeSIMConfigNode

       Returns a reference to the input node for the Control & Simulation Loop.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                                   Yes

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

   SIMOutputNodeSIMOutputNode
   SIMOutputNodeSIMOutputNode

       Returns a reference to the output node for the Control & Simulation Loop.


9074   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9074 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9075 ordinal=9075 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

SynchronousDataFlowNodeSynchronousDataFlowNode

SynchronousDataFlowNode Properties
SynchronousDataFlowNodeSynchronousDataFlowNode PropertiesProperties
SynchronousDataFlowNodeSynchronousDataFlowNode PropertiesProperties


 Property        Description

 Sdf Config       Returns a reference to the left configuration node of a synchronous data flow
 Node           node.


                                                    © National Instruments 9075

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9075 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9076 ordinal=9076 -->
## Property and Method Reference

Property and Method Reference

   SdfSdf ConfigConfig NodeNode
   SdfSdf ConfigConfig NodeNode

       Returns a reference to the left configuration node of a synchronous data flow node.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                                   Yes

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

   TimedSequenceTimedSequence

      TimedSequence Methods

      TimedSequence Properties
   TimedSequenceTimedSequence MethodsMethods
   TimedSequenceTimedSequence MethodsMethods


9076   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9076 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9077 ordinal=9077 -->
## Property and Method Reference

Property and Method Reference


 Method         Description

 Convert To      Converts a Timed Sequence structure to a Flat Sequence structure and returns a
 FlatSequence    reference to the Flat Sequence structure.

 Convert To      Converts a Timed Sequence structure to a Timed Loop and returns a reference to
 TimedLoop      the Timed Loop.

ConvertConvert ToTo FlatSequenceFlatSequence
ConvertConvert ToTo FlatSequenceFlatSequence

Converts a Timed Sequence structure to a Flat Sequence structure and returns a
reference to the Flat Sequence structure.

This method automatically closes the reference to the Timed Sequence structure.

Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                                      Yes

 Available in Real-Time Operating System                                            Yes

 Settable when the VI is running                                        No

 Loads the front panel into memory                                     No

 Need to authenticate before use                                       No

 Loads the block diagram into memory                                   No

 Remote access allowed                                                           Yes


                                                    © National Instruments 9077

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9077 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9078 ordinal=9078 -->
## Property and Method Reference

Property and Method Reference

   ConvertConvert ToTo TimedLoopTimedLoop
   ConvertConvert ToTo TimedLoopTimedLoop

       Converts a Timed Sequence structure to a Timed Loop and returns a reference to the
      Timed Loop.

       This property automatically closes the reference to the Timed Sequence structure.

     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                                      Yes

         Available in Real-Time Operating System                                            Yes

         Settable when the VI is running                                        No

        Loads the front panel into memory                                     No

       Need to authenticate before use                                       No

        Loads the block diagram into memory                                   No

       Remote access allowed                                                           Yes

   TimedSequenceTimedSequence PropertiesProperties
   TimedSequenceTimedSequence PropertiesProperties


        Property                        Description

       Embedded Flat Sequence        Returns a reference to the Flat Sequence structure.


9078   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9078 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9079 ordinal=9079 -->
## Property and Method Reference

Property and Method Reference

EmbeddedEmbedded FlatFlat SequenceSequence
EmbeddedEmbedded FlatFlat SequenceSequence

Returns a reference to the Flat Sequence structure.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                               Read Only

 Available in Run-Time Engine                                        Yes (Read Only)

 Available in Real-Time Operating System                             Yes

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

StatechartStructureNodeStatechartStructureNode
JoinNodeJoinNode
JoinNodeJoinNode


                                                    © National Instruments 9079

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9079 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9080 ordinal=9080 -->
## Property and Method Reference

Property and Method Reference

   ForkNodeForkNode
   ForkNodeForkNode
   StateNodeStateNode
   StateNodeStateNode
   JunctionNodeJunctionNode
   JunctionNodeJunctionNode
   RegionNodeRegionNode
   RegionNodeRegionNode
    InPlaceElementStructureInPlaceElementStructure

       InPlaceElementStructure Methods

       InPlaceElementStructure Properties
   InPlaceElementStructureInPlaceElementStructure MethodsMethods
    InPlaceElementStructureInPlaceElementStructure MethodsMethods


       Method         Description

       Add In Place    Adds a pair of border nodes at the specified Y Position on an In Place Element

9080   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9080 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9081 ordinal=9081 -->
## Property and Method Reference

Property and Method Reference


 Method         Description

 Pair             Structure.

AddAdd InIn PlacePlace PairPair
AddAdd InIn PlacePlace PairPair

Adds a pair of border nodes at the specified Y Position on an In Place Element
Structure.

Parameters

         Data Name           Required  Description         type

 Y                             Specifies the position relative to the structure border at which to add                  Yes Position                    the border nodes.


                               Specifies the def proc ID of the border nodes you want to add to the
 DPID             Yes                                structure.


Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                         No

 Available in Real-Time Operating System                                 No

 Settable when the VI is running                                        No

 Loads the front panel into memory                                     No

 Need to authenticate before use                                       No


                                                    © National Instruments 9081

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9081 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9082 ordinal=9082 -->
## Property and Method Reference

Property and Method Reference


        Loads the block diagram into memory                                   No

       Remote access allowed                                                           Yes

   InPlaceElementStructureInPlaceElementStructure PropertiesProperties
    InPlaceElementStructureInPlaceElementStructure PropertiesProperties


        Property         Description

                          Returns an array of references to any of the following border nodes on the In
                           Place Element structure: Array Index Elements, Array Split Subarrays, Unbundle
         DecomposerList[]                          Elements, Waveform Unbundle Elements, Variant To Element, In Place In
                          Element, Data Value Reference Read Element.

                          Returns an array of references to any of the following border nodes on the In
        Recomposer      Place Element structure: Array Replace Elements, Array Replace Subarrays,
           List[]            Bundle Elements, Waveform Bundle Elements, Variant From Element, In Place
                       Out Element, Data Value Reference Write Element.

   DecomposerList[]DecomposerList[]
   DecomposerList[]DecomposerList[]

       Returns an array of references to any of the following border nodes on the In Place
      Element structure: Array Index Elements, Array Split Subarrays, Unbundle Elements,
      Waveform Unbundle Elements, Variant To Element, In Place In Element, Data Value
       Reference Read Element.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only


9082   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9082 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9083 ordinal=9083 -->
## Property and Method Reference

Property and Method Reference


 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

RecomposerRecomposer List[]List[]
RecomposerRecomposer List[]List[]

Returns an array of references to any of the following border nodes on the In Place
Element structure: Array Replace Elements, Array Replace Subarrays, Bundle
Elements, Waveform Bundle Elements, Variant From Element, In Place Out Element,
Data Value Reference Write Element.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes


                                                    © National Instruments 9083

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9083 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9084 ordinal=9084 -->
## Property and Method Reference

Property and Method Reference

   TargetStructureNodeTargetStructureNode
   ClosureStructureNodeClosureStructureNode
   FormulaFormula

      Formula Methods

      Formula Properties
   FormulaFormula MethodsMethods


       Method         Description

       Add Input      Adds an input to a Formula Node at the position you specify.

       Add Output     Adds an output to a Formula Node at the position you specify.

   AddAdd InputInput
   AddAdd InputInput

      Adds an input to a Formula Node at the position you specify.

     Parameters

                Data
      Name            Required  Description
                 type

                                         Specifies the position of the input relative to the frame of the
         Position           Yes
                                  Formula Node.


9084   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9084 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9085 ordinal=9085 -->
## Property and Method Reference

Property and Method Reference


         Data Name            Required  Description
         type

 Name             Yes        Specifies the name of the input you want to add.


Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                         No

 Available in Real-Time Operating System                                 No

 Settable when the VI is running                                        No

 Loads the front panel into memory                                     No

 Need to authenticate before use                                       No

 Loads the block diagram into memory                                   No

 Remote access allowed                                                           Yes

AddAdd OutputOutput
AddAdd OutputOutput

Adds an output to a Formula Node at the position you specify.

Parameters

         Data
 Name            Required  Description
         type

                                Specifies the position of the output relative to the frame of the
 Position           Yes
                           Formula Node.


                                                    © National Instruments 9085

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9085 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9086 ordinal=9086 -->
## Property and Method Reference

Property and Method Reference


                Data      Name            Required  Description
                 type

      Name             Yes        Specifies the name of the output you want to add.


     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                         No

         Available in Real-Time Operating System                                 No

         Settable when the VI is running                                        No

        Loads the front panel into memory                                     No

       Need to authenticate before use                                       No

        Loads the block diagram into memory                                   No

       Remote access allowed                                                           Yes

   FormulaFormula PropertiesProperties


        Property                   Description

        Formula Expression          Specifies an expression for the Formula Node.

        Formula Parameters[]        Specifies the inputs and outputs of the Formula Node.

         Scrollbar Visible?             Specifies whether the vertical scroll bar is visible.


9086   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9086 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9087 ordinal=9087 -->
## Property and Method Reference

Property and Method Reference

FormulaFormula ExpressionExpression
FormulaFormula ExpressionExpression

Specifies an expression for the Formula Node.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                 No

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

FormulaFormula Parameters[]Parameters[]
FormulaFormula Parameters[]Parameters[]

Specifies the inputs and outputs of the Formula Node.

Remarks

The following table lists the characteristics of this property.


 Data type

                                                    © National Instruments 9087

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9087 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9088 ordinal=9088 -->
## Property and Method Reference

Property and Method Reference


         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                                   Yes

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

   ScrollbarScrollbar Visible?Visible?
    ScrollbarScrollbar Visible?Visible?

       Specifies whether the vertical scroll bar is visible.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                 No

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes


9088   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9088 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9089 ordinal=9089 -->
## Property and Method Reference

Property and Method Reference

ScriptNodeScriptNode
MathScriptNodeMathScriptNode

MathScriptNode Methods
MathScriptNodeMathScriptNode MethodsMethods
MathScriptNodeMathScriptNode MethodsMethods


 Method          Description

 Set MathScript    Sets a breakpoint on a line of the MathScript Node with the Status you specify.
 Node Line        This method also returns the number of the line on which LabVIEW sets the
 Breakpoint       breakpoint.

SetSet MathScriptMathScript NodeNode LineLine BreakpointBreakpoint
SetSet MathScriptMathScript NodeNode LineLine BreakpointBreakpoint

Sets a breakpoint on a line of the MathScript Node with the Status you specify. This
method also returns the number of the line on which LabVIEW sets the breakpoint.

Parameters

           Data
 Name           Required  Description
            type

                               Specifies the number of the line on which you want to set the
 Line              Yes
                             breakpoint. Line numbers in MathScript Nodes are one-based.


                                                    © National Instruments 9089

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9089 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9090 ordinal=9090 -->
## Property and Method Reference

Property and Method Reference


                   Data      Name           Required  Description
                   type

                                        Specifies the status of the breakpoint you want to set.

        Breakpoint                 0        Cleared Break                           Yes         Status                                  1       Enabled Break

                                  2        Disabled Break


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                                      Yes

        Loads the front panel into memory                                  Yes

       Need to authenticate before use                            No

        Loads the block diagram into memory                               Yes

       Remote access allowed                                             Yes

   InlineCNodeInlineCNode
   GrowableFunctionGrowableFunction

      GrowableFunction Methods

      GrowableFunction Properties


9090   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9090 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9091 ordinal=9091 -->
## Property and Method Reference

Property and Method Reference

GrowableFunctionGrowableFunction MethodsMethods


 Method            Description

                  Adds one or more chunks of terminals to the top or bottom of this growable
 Resize:Add Chunk                   node.

 Resize:Remove     Removes one or more chunks of terminals from the top or bottom of this
 Chunk            growable node.

Resize:AddResize:Add ChunkChunk
Resize:AddResize:Add ChunkChunk

Adds one or more chunks of terminals to the top or bottom of this growable node.

Parameters

           Data Name            Required  Description           type

 Chunks
                    Yes        Specifies the number of terminals to add to the node. To Add


                                Specifies whether to add the chunk of terminals to the top or the
                          bottom of the growable node.
 Where To
               No
 Add                        0            Bottom

                            1            Top


Remarks

The following table lists the characteristics of this method.


                                                    © National Instruments 9091

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9091 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9092 ordinal=9092 -->
## Property and Method Reference

Property and Method Reference


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                               Yes

       Remote access allowed                                             Yes

   Resize:RemoveResize:Remove ChunkChunk
   Resize:RemoveResize:Remove ChunkChunk

      Removes one or more chunks of terminals from the top or bottom of this growable
      node.

     Parameters

                   Data      Name             Required  Description                    type

        Chunks To                             Yes        Specifies the number of terminals to remove from the node.
       Remove


                                          Specifies whether to remove the chunk of terminals from the top
                                       or the bottom of the growable node.
       Where To
                      No
       Remove                     0            Bottom

                                    1            Top


9092   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9092 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9093 ordinal=9093 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                              No

 Available in Real-Time Operating System                      No

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                               Yes

 Remote access allowed                                             Yes

GrowableFunctionGrowableFunction PropertiesProperties


 Property         Description

 Terminal Height  Returns the height, in pixels, of each growable terminal on a growable node.

TerminalTerminal HeightHeight
TerminalTerminal HeightHeight

Returns the height, in pixels, of each growable terminal on a growable node.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only


                                                    © National Instruments 9093

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9093 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9094 ordinal=9094 -->
## Property and Method Reference

Property and Method Reference


         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                                   Yes

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

    BuildClusterArrayBuildClusterArray
   CompoundArithmeticCompoundArithmetic

      CompoundArithmetic Properties
   CompoundArithmeticCompoundArithmetic PropertiesProperties
   CompoundArithmeticCompoundArithmetic PropertiesProperties


        Property      Description

          Invert
                       Returns an array of Boolean values that indicate whether the inputs are inverted.
          Inputs?[]

                       Gets or sets whether the output terminal on a Compound Arithmetic Function is
          Invert Output
                         inverted.

       Mode          Specifies the mode.


9094   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9094 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9095 ordinal=9095 -->
## Property and Method Reference

Property and Method Reference

InvertInvert Inputs?[]Inputs?[]
InvertInvert Inputs?[]Inputs?[]

Returns an array of Boolean values that indicate whether the inputs are inverted.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                 No

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

InvertInvert OutputOutput
InvertInvert OutputOutput

Gets or sets whether the output terminal on a Compound Arithmetic Function is
inverted.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 9095

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9095 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9096 ordinal=9096 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                 No

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   ModeMode
   ModeMode

       Specifies the mode.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                 No

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes


9096   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9096 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9097 ordinal=9097 -->
## Property and Method Reference

Property and Method Reference

IndexArrayIndexArray

IndexArray Properties
IndexArrayIndexArray PropertiesProperties
IndexArrayIndexArray PropertiesProperties


 Property     Description

 Array Input              Returns a reference to the array input. Terminal

              Gets or sets the number of indexes. On a set, this property expands the node to Index Count            accommodate the number of indexes you specify.

 Index              Returns an array of references to the index terminals. Terminals[][]

 Output              Returns an array of references to the index array output terminals. Terminals[]

ArrayArray InputInput TerminalTerminal
ArrayArray InputInput TerminalTerminal

Returns a reference to the array input.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

                                                    © National Instruments 9097

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9097 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9098 ordinal=9098 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                                   Yes

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

   IndexIndex CountCount
   IndexIndex CountCount

       Gets or sets the number of indexes. On a set, this property expands the node to
      accommodate the number of indexes you specify.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes


9098   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9098 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9099 ordinal=9099 -->
## Property and Method Reference

Property and Method Reference

IndexIndex Terminals[][]Terminals[][]
IndexIndex Terminals[][]Terminals[][]

Returns an array of references to the index terminals.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

OutputOutput Terminals[]Terminals[]
OutputOutput Terminals[]Terminals[]

Returns an array of references to the index array output terminals.

Remarks

The following table lists the characteristics of this property.


 Data type

                                                    © National Instruments 9099

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9099 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9100 ordinal=9100 -->
## Property and Method Reference

Property and Method Reference


         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                                   Yes

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

   CINCIN

      CIN Methods

      CIN Properties
   CINCIN MethodsMethods
   CINCIN MethodsMethods


       Method         Description

       Add Parameter  Adds a new parameter after the item you specify in Index and returns a reference
          After            to the new pair of terminals.

         Create C File     Creates a C file for the Code Interface Node at the path you specify.

        Load Code                      Loads a code resource from a code resource (.lsb) file.        Resource

        Purge Code
                         Deletes the code associated with the Code Interface Node.
        Resource

       Remove
                    Removes the parameter at the index you specify.
        Parameter


9100   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9100 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9101 ordinal=9101 -->
## Property and Method Reference

Property and Method Reference

AddAdd ParameterParameter AfterAfter
AddAdd ParameterParameter AfterAfter

Adds a new parameter after the item you specify in Index and returns a reference to
the new pair of terminals.

Parameters

       Data Name       Required  Description       type

                          Specifies the index of the item after which to add the new item. To add the
 Index        Yes                       item to the beginning of the node, specify –1 for Index.


Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                                      Yes

 Available in Real-Time Operating System                                            Yes

 Settable when the VI is running                                        No

 Loads the front panel into memory                                     No

 Need to authenticate before use                                       No

 Loads the block diagram into memory                                   No

 Remote access allowed                                                           Yes


                                                    © National Instruments 9101

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9101 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9102 ordinal=9102 -->
## Property and Method Reference

Property and Method Reference

   CreateCreate CC FileFile
    CreateCreate CC FileFile

       Creates a C file for the Code Interface Node at the path you specify.

     Parameters

      Name Data type  Required  Description

        Path              Yes        Specifies the path to the directory where you want to save the C file.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

   LoadLoad CodeCode ResourceResource
   LoadLoad CodeCode ResourceResource

      Loads a code resource from a code resource (.lsb) file.

9102   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9102 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9103 ordinal=9103 -->
## Property and Method Reference

Property and Method Reference

Parameters

 Name    Data type     Required     Description

 Path                    Yes            Specifies the path to the code resource file.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                              No

 Available in Real-Time Operating System                      No

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

PurgePurge CodeCode ResourceResource
PurgePurge CodeCode ResourceResource

Deletes the code associated with the Code Interface Node.

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

                                                    © National Instruments 9103

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9103 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9104 ordinal=9104 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

   RemoveRemove ParameterParameter
   RemoveRemove ParameterParameter

      Removes the parameter at the index you specify.

     Parameters

      Name    Data type     Required     Description

         Index                   Yes          Index of the parameter you want to remove.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No


9104   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9104 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9105 ordinal=9105 -->
## Property and Method Reference

Property and Method Reference


 Remote access allowed                                             Yes

CINCIN PropertiesProperties
CINCIN PropertiesProperties


 Property              Description

 Code Resource Path    Specifies the path to the code resource (.lsb) file.

 Input Terminals[]      Returns a 1D array of references to the input parameter terminals.

 Output Terminals[]     Returns a 1D array of references to the output parameter terminals.

 ParameterCount       Gets or sets the number of parameters.

CodeCode ResourceResource PathPath
CodeCode ResourceResource PathPath

Specifies the path to the code resource (.lsb) file.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No


                                                    © National Instruments 9105

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9105 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9106 ordinal=9106 -->
## Property and Method Reference

Property and Method Reference


        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

   InputInput Terminals[]Terminals[]
    InputInput Terminals[]Terminals[]

       Returns a 1D array of references to the input parameter terminals.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                                   Yes

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

   OutputOutput Terminals[]Terminals[]
   OutputOutput Terminals[]Terminals[]

       Returns a 1D array of references to the output parameter terminals.


9106   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9106 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9107 ordinal=9107 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

ParameterCountParameterCount
ParameterCountParameterCount

Gets or sets the number of parameters.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No


                                                    © National Instruments 9107

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9107 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9108 ordinal=9108 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    CallLibraryCallLibrary

       CallLibrary Methods

       CallLibrary Properties
   CallLibraryCallLibrary MethodsMethods
    CallLibraryCallLibrary MethodsMethods


       Method        Description

         Create C File    Creates a C file for the Call Library Function Node at the specified path.

         Prototype      Returns the C prototype string for the currently configured function.

   CreateCreate CC FileFile
    CreateCreate CC FileFile

       Creates a C file for the Call Library Function Node at the specified path.

     Parameters

      Name Data type  Required  Description

        Path              Yes        Specifies the path to the directory where you want to save the C file.


9108   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9108 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9109 ordinal=9109 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                             Yes

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

PrototypePrototype
PrototypePrototype

Returns the C prototype string for the currently configured function.

Parameters

 Name             Data type  Required  Description

 Prototype                      Yes        Returns the C prototype string.


 Typedefs                       Yes        Returns the type definitions for Prototype.


 Include Typedefs?              Yes             If TRUE, the type definitions for Prototype appear.


                                                    © National Instruments 9109

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9109 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9110 ordinal=9110 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

   CallLibraryCallLibrary PropertiesProperties
    CallLibraryCallLibrary PropertiesProperties


        Property    Description

        Abort                     Sets or returns the name of the abort callback function that LabVIEW calls.
         Callback

        Any                      Indicates whether the function is reentrant.
        Thread?

          Calling
                   Uses the calling conventions to call libraries.
        Convention

                     Sets the Call Library Function Node, in write mode, to execute with the library path
       Dynamic
                  you specify. In read mode, this property returns whether LabVIEW configures the Call
         Library?
                      Library Function Node to load the library dynamically.

         Error
        Checking    Sets or returns the error level for the Call Library Function Node.
         Level

         Function    Sets or returns the name of the function you configure the Call Library Function Node


9110   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9110 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9111 ordinal=9111 -->
## Property and Method Reference

Property and Method Reference


 Property    Description

 Name       to call.

 Input             Returns a 1D array of references to the input parameters. Terminals[]

 Library              Specifies the path to the DLL or shared library the Call Library Function Node calls.
 Path

 Output
 Terminals   Returns a 1D array of references to the output parameters.
 []

 Parameter             Sets or returns an array of clusters with information for the parameters of a function. Info

 Reserve             Sets or returns the name of the reserve callback function that LabVIEW calls.
 Callback

 Unreserve             Sets or returns the name of the unreserve callback function that LabVIEW calls.
 Callback

AbortAbort CallbackCallback
AbortAbort CallbackCallback

Sets or returns the name of the abort callback function that LabVIEW calls.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                 No

 Loads the front panel into memory                              No


                                                    © National Instruments 9111

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9111 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9112 ordinal=9112 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   AnyAny Thread?Thread?
   AnyAny Thread?Thread?

       Indicates whether the function is reentrant.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                 No

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   CallingCalling ConventionConvention
    CallingCalling ConventionConvention

      Uses the calling conventions to call libraries.


9112   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9112 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9113 ordinal=9113 -->
## Property and Method Reference

Property and Method Reference

Valid values include 0 (C Call) and 1 (stdcall (WINAPI)).

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                 No

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

DynamicDynamic Library?Library?
DynamicDynamic Library?Library?

Sets the Call Library Function Node, in write mode, to execute with the library path you
specify. In read mode, this property returns whether LabVIEW configures the Call
Library Function Node to load the library dynamically.

With the dynamic library property set in write mode, the library loads when LabVIEW
executes the node. When you wire a different path, the Call Library Function Node
unloads the previous library and loads the new library. When you wire a NULL path,
the Call Library Function Node unloads the previous library and loads the NULL path in
the same way.

Remarks

The following table lists the characteristics of this property.

                                                    © National Instruments 9113

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9113 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9114 ordinal=9114 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                 No

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   ErrorError CheckingChecking LevelLevel
    ErrorError CheckingChecking LevelLevel

       Sets or returns the error level for the Call Library Function Node.

       Valid values include 0 (maximum), 1 (default), and 2 (disabled).

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                 No

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

9114   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9114 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9115 ordinal=9115 -->
## Property and Method Reference

Property and Method Reference


 Remote access allowed                                                  Yes

FunctionFunction NameName
FunctionFunction NameName

Sets or returns the name of the function you configure the Call Library Function Node
to call.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                 No

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

InputInput Terminals[]Terminals[]
InputInput Terminals[]Terminals[]

Returns a 1D array of references to the input parameters.


                                                    © National Instruments 9115

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9115 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9116 ordinal=9116 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                                   Yes

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

   LibraryLibrary PathPath
    LibraryLibrary PathPath

       Specifies the path to the DLL or shared library the Call Library Function Node calls.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                 No

        Loads the front panel into memory                              No


9116   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9116 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9117 ordinal=9117 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

OutputOutput TerminalsTerminals [][]
OutputOutput TerminalsTerminals [][]

Returns a 1D array of references to the output parameters.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

ParameterParameter InfoInfo
ParameterParameter InfoInfo

Sets or returns an array of clusters with information for the parameters of a function.


                                                    © National Instruments 9117

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9117 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9118 ordinal=9118 -->
## Property and Method Reference

Property and Method Reference

      Each cluster in the array represents a parameter of the function, starting with the
       return value. The property only returns the fields relevant to the parameter type. For
      example, if the parameter type is a numeric, the property returns a value to the Param
       Passing element but not to the Array Passing element.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                 No

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   ReserveReserve CallbackCallback
   ReserveReserve CallbackCallback

       Sets or returns the name of the reserve callback function that LabVIEW calls.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

9118   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9118 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9119 ordinal=9119 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                          No

 Settable when the VI is running                                 No

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

UnreserveUnreserve CallbackCallback
UnreserveUnreserve CallbackCallback

Sets or returns the name of the unreserve callback function that LabVIEW calls.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                 No

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

FormatScanStringFormatScanString

FormatScanString Properties

                                                    © National Instruments 9119

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9119 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9120 ordinal=9120 -->
## Property and Method Reference

Property and Method Reference

   FormatScanStringFormatScanString PropertiesProperties
   FormatScanStringFormatScanString PropertiesProperties


        Property                   Description

        Format String                Specifies a string to scan or format.

   FormatFormat StringString
   FormatFormat StringString

       Specifies a string to scan or format.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                 No

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   ObjectFunctionObjectFunction


9120   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9120 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9121 ordinal=9121 -->
## Property and Method Reference

Property and Method Reference

ObjectFunction Properties
ObjectFunctionObjectFunction PropertiesProperties
ObjectFunctionObjectFunction PropertiesProperties


 Property   Description

 Class       Returns the name of the class that evokes a function.

 Name       Sets or returns the name format. Valid values include 0 (no names), 1 (short names),
 Format    and 2 (long names).

ClassClass
ClassClass

Returns the name of the class that evokes a function.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes


                                                    © National Instruments 9121

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9121 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9122 ordinal=9122 -->
## Property and Method Reference

Property and Method Reference

  NameName FormatFormat
   NameName FormatFormat

       Sets or returns the name format. Valid values include 0 (no names), 1 (short names),
      and 2 (long names).

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                 No

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   PropertyProperty
    PropertyProperty

       Property Methods

       Property Properties


9122   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9122 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9123 ordinal=9123 -->
## Property and Method Reference

Property and Method Reference

PropertyProperty MethodsMethods
PropertyProperty MethodsMethods


 Method     Description

 Add            Adds a new property item after the item you specify in Index and returns a reference Property              to the new property item. Item After

 Disconnect
 From        Disconnects the property node from a control.
 Control

 Get
 Property    Returns a reference to the property item you specify with index.
 Item

              Links the property node to the control you specify. The link to the control is available Link To             only when you do not wire data to the Reference input. If you wire data to the
 Control             Reference input, LabVIEW returns an error.

 Remove
 Property    Removes the property item at the index you specify.
 Item

 Set              Sets the properties for this Property Node. Properties[]

AddAdd PropertyProperty ItemItem AfterAfter
AddAdd PropertyProperty ItemItem AfterAfter

Adds a new property item after the item you specify in Index and returns a reference to
the new property item.


                                                    © National Instruments 9123

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9123 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9124 ordinal=9124 -->
## Property and Method Reference

Property and Method Reference

     Parameters

              Data      Name       Required  Description
               type

                                   Specifies the index of the item after which to add the new item. To add the
         Index        Yes                               item to the beginning of the node, specify –1 for Index.


     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                                      Yes

         Available in Real-Time Operating System                                            Yes

         Settable when the VI is running                                        No

        Loads the front panel into memory                                     No

       Need to authenticate before use                                       No

        Loads the block diagram into memory                                   No

       Remote access allowed                                                           Yes

   DisconnectDisconnect FromFrom ControlControl
   DisconnectDisconnect FromFrom ControlControl

       Disconnects the property node from a control.

     Remarks

      The following table lists the characteristics of this method.


9124   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9124 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9125 ordinal=9125 -->
## Property and Method Reference

Property and Method Reference


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                             Yes

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

GetGet PropertyProperty ItemItem
GetGet PropertyProperty ItemItem

Returns a reference to the property item you specify with index.

Parameters

 Name    Data type      Required      Description

 Index                     Yes             Specifies where to return a reference.


Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                         No

 Available in Real-Time Operating System                                 No

 Settable when the VI is running                                        No

 Loads the front panel into memory                                     No

                                                    © National Instruments 9125

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9125 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9126 ordinal=9126 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                                       No

        Loads the block diagram into memory                                   No

       Remote access allowed                                                           Yes

   LinkLink ToTo ControlControl
    LinkLink ToTo ControlControl

       Links the property node to the control you specify. The link to the control is available
       only when you do not wire data to the Reference input. If you wire data to the
      Reference input, LabVIEW returns an error.

     Parameters

      Name     Data type  Required  Description

         Reference             Yes        Specifies a control from the VI that owns the property node.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes


9126   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9126 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9127 ordinal=9127 -->
## Property and Method Reference

Property and Method Reference

RemoveRemove PropertyProperty ItemItem
RemoveRemove PropertyProperty ItemItem

Removes the property item at the index you specify.

Parameters

 Name    Data type     Required     Description

 Index                   Yes            Specifies the index of the item to remove.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                             Yes

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

SetSet Properties[]Properties[]
SetSet Properties[]Properties[]

Sets the properties for this Property Node.

                                                    © National Instruments 9127

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9127 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9128 ordinal=9128 -->
## Property and Method Reference

Property and Method Reference

     Parameters

                 Data      Name          Required  Description
                 type

                                      Specifies the Unique ID string of the properties you want to set. Use
                                  the All Supported Properties property to determine the Unique ID
         ID                          string of the properties you want to set. Set Allow Alternative Names?                         Yes
          Strings[]                   to TRUE if you want to match the ID Strings[] to any of the following
                                   values of a property: Unique ID string, Data name, Short name
                                        (localized), or Long name (localized).


                                      Specifies whether you can set the property or method using the
        Allow                              Unique ID string, Data name, Short name (localized), or Long name         Alternate                   No        (localized) of the property or method. The default is FALSE, which
       Names?                            means you must specify the Unique ID string of the property or           (F)                             method in ID String.


     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                         No

         Available in Real-Time Operating System                                 No

         Settable when the VI is running                                        No

        Loads the front panel into memory                                                 Yes

       Need to authenticate before use                                       No

        Loads the block diagram into memory                                              Yes

       Remote access allowed                                                           Yes


9128   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9128 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9129 ordinal=9129 -->
## Property and Method Reference

Property and Method Reference

PropertyProperty PropertiesProperties
PropertyProperty PropertiesProperties


 Property    Description

 All
 Supported   Lists all properties supported for the current class.
 Properties

 Flags:Has
             Returns TRUE if Ignore Errors inside Node is set for the Property Node. You can set a Ignore             Property Node to ignore errors by right-clicking the Property Node and selecting Errors             Ignore Errors inside Node from the shortcut menu or by setting the Ignore Error Inside
              Inside Node property. Node

 Ignore
 Errors              Sets or gets the option to ignore individual property errors. Inside
 Node?

 Linked
             Returns a reference to a front panel control if the property node links to the control. Control

 Properties[] Gets information about the properties selected in this node.

 Property              Sets or gets the number of properties in the property node. Count

 Property             Returns references to individual items of the property node. Items[]

 Property
 Node Class  Sets or gets the class name for the property node.
 Name

AllAll SupportedSupported PropertiesProperties
AllAll SupportedSupported PropertiesProperties

Lists all properties supported for the current class.

                                                    © National Instruments 9129

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9129 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9130 ordinal=9130 -->
## Property and Method Reference

Property and Method Reference

     Some properties have a Unique ID string. The Unique ID string is consistent across all
       versions and locales of LabVIEW. Properties without a Unique ID string return an
      empty string. All properties return Data name, Short name (localized), and Long
     name (localized), which contain the strings shown to the user in this version and
       locale of LabVIEW; however, strings can vary across versions, locales, and even
       individual launches of LabVIEW.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                                         Yes

       Need to authenticate before use                                 No

        Loads the block diagram into memory                                      Yes

       Remote access allowed                                                   Yes

   Flags:HasFlags:Has IgnoreIgnore ErrorsErrors InsideInside NodeNode
    Flags:HasFlags:Has IgnoreIgnore ErrorsErrors InsideInside NodeNode

       Returns TRUE if Ignore Errors inside Node is set for the Property Node. You can set a
       Property Node to ignore errors by right-clicking the Property Node and selecting
       Ignore Errors inside Node from the shortcut menu or by setting the Ignore Error Inside
     Node property.

     Remarks

      The following table lists the characteristics of this property.

9130   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9130 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9131 ordinal=9131 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                                         Yes

 Need to authenticate before use                                 No

 Loads the block diagram into memory                                      Yes

 Remote access allowed                                                   Yes

IgnoreIgnore ErrorsErrors InsideInside Node?Node?
IgnoreIgnore ErrorsErrors InsideInside Node?Node?

Sets or gets the option to ignore individual property errors.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                 No

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes


                                                    © National Instruments 9131

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9131 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9132 ordinal=9132 -->
## Property and Method Reference

Property and Method Reference

   LinkedLinked ControlControl
   LinkedLinked ControlControl

       Returns a reference to a front panel control if the property node links to the control.

       This property returns a NULL reference and an error if the property node does not link
       to a front panel control.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                                   Yes

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

    Properties[]Properties[]
    Properties[]Properties[]

       Gets information about the properties selected in this node.

     Some properties have a Unique ID string. The Unique ID string is consistent across all
       versions and locales of LabVIEW. Properties without a Unique ID string return an


9132   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9132 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9133 ordinal=9133 -->
## Property and Method Reference

Property and Method Reference

empty string. If this node has an invalid property selected, this property returns empty
strings for Unique ID string, Data name, Short name, and Long name. This property is
read only. Use the Set Properties method to change the currently selected properties.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                                         Yes

 Need to authenticate before use                                 No

 Loads the block diagram into memory                                      Yes

 Remote access allowed                                                   Yes

PropertyProperty CountCount
PropertyProperty CountCount

Sets or gets the number of properties in the property node.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No


                                                    © National Instruments 9133

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9133 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9134 ordinal=9134 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                          No

         Settable when the VI is running                                 No

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   PropertyProperty Items[]Items[]
    PropertyProperty Items[]Items[]

       Returns references to individual items of the property node.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes


9134   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9134 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9135 ordinal=9135 -->
## Property and Method Reference

Property and Method Reference

PropertyProperty NodeNode ClassClass NameName
PropertyProperty NodeNode ClassClass NameName

Sets or gets the class name for the property node.

If you set the class name, include the full names for the server class and the node
class, separated by a colon. VI Server:Generic is an example of a class name.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                 No

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

InvokeInvoke
InvokeInvoke

Invoke Methods

Invoke Properties


                                                    © National Instruments 9135

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9135 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9136 ordinal=9136 -->
## Property and Method Reference

Property and Method Reference

   InvokeInvoke MethodsMethods
   InvokeInvoke MethodsMethods


       Method     Description

        Disconnect
       From       Disconnects the invoke node from a control.
         Control

                     Links the invoke node to the control you specify. The link to the control is available
         Link To                    only when you do not wire data to the Reference input. If you wire data to the         Control                   Reference input, LabVIEW returns an error.

         Set
                     Sets the method of the invoke node.       Method

   DisconnectDisconnect FromFrom ControlControl
   DisconnectDisconnect FromFrom ControlControl

       Disconnects the invoke node from a control.

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

9136   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9136 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9137 ordinal=9137 -->
## Property and Method Reference

Property and Method Reference


 Remote access allowed                                             Yes

LinkLink ToTo ControlControl
LinkLink ToTo ControlControl

Links the invoke node to the control you specify. The link to the control is available
only when you do not wire data to the Reference input. If you wire data to the
Reference input, LabVIEW returns an error.

Parameters

 Name     Data type  Required  Description

 Reference              Yes         Specifies a control from the VI that owns the invoke node.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                             Yes

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes


                                                    © National Instruments 9137

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9137 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9138 ordinal=9138 -->
## Property and Method Reference

Property and Method Reference

   SetSet MethodMethod
    SetSet MethodMethod

       Sets the method of the invoke node.

     Parameters

                 Data      Name          Required  Description                 type

                                      Specifies the Unique ID string of the method you want to set. Use the
                                             All Supported Methods property to determine the Unique ID string of
                                  the method you want to set. Set Allow Alternative Names? to TRUE if
         ID String        Yes                              you want to match the ID String to any of the following values of the
                               method: Unique ID string, Data name, Short name (localized), or Long
                          name (localized).


                                      Specifies whether you can set the property or method using the        Allow
                              Unique ID string, Data name, Short name (localized), or Long name         Alternate                   No        (localized) of the property or method. The default is FALSE, which       Names?
                            means you must specify the Unique ID string of the property or           (F)                             method in ID String.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

         Settable when the VI is running                             No

        Loads the front panel into memory                                  Yes


9138   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9138 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9139 ordinal=9139 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                            No

 Loads the block diagram into memory                               Yes

 Remote access allowed                                             Yes

InvokeInvoke PropertiesProperties
InvokeInvoke PropertiesProperties


 Property              Description

 All Supported                            Lists all methods supported for the current class. Methods

 Input Terminals []      Returns references to the input parameters.

 Invoke Node Class
                        Sets or gets the class name for the invoke node. Name

                       Returns a reference to a front panel control if the invoke node links to the
 Linked Control                          control.

 Method               Gets information about the methods selected in this node.

 Output Terminals []    Returns references to the output parameters.

AllAll SupportedSupported MethodsMethods
AllAll SupportedSupported MethodsMethods

Lists all methods supported for the current class.

Some methods have a Unique ID string. The Unique ID string is consistent across all
versions and locales of LabVIEW. Methods without a Unique ID string return an empty
string. All methods return Data name, Short name (localized), and Long name
(localized), which contain the strings shown to the user in this version and locale of
LabVIEW; however, strings can vary across versions, locales, and even individual
launches of LabVIEW.

                                                    © National Instruments 9139

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9139 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9140 ordinal=9140 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                                         Yes

       Need to authenticate before use                                 No

        Loads the block diagram into memory                                      Yes

       Remote access allowed                                                   Yes

   InputInput TerminalsTerminals [][]
    InputInput TerminalsTerminals [][]

       Returns references to the input parameters.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                                   Yes

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No


9140   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9140 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9141 ordinal=9141 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

InvokeInvoke NodeNode ClassClass NameName
InvokeInvoke NodeNode ClassClass NameName

Sets or gets the class name for the invoke node.

If you set the class name, include the full names for the server class and the node
class, separated by a colon. VI Server:Generic is an example of a class name.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                 No

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes


                                                    © National Instruments 9141

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9141 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9142 ordinal=9142 -->
## Property and Method Reference

Property and Method Reference

   LinkedLinked ControlControl
   LinkedLinked ControlControl

       Returns a reference to a front panel control if the invoke node links to the control.

       This property returns a NULL reference and an error if the invoke node does not link to
      a front panel control.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                                   Yes

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

   MethodMethod
   MethodMethod

       Gets information about the methods selected in this node.

     Some methods have a Unique ID string. The Unique ID string is consistent across all
       versions and locales of LabVIEW. Methods without a Unique ID string return an empty


9142   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9142 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9143 ordinal=9143 -->
## Property and Method Reference

Property and Method Reference

string. If this node has an invalid method selected, this property returns empty strings
for Data name, Short name, and Long name. This property is read only. Use the Set
Method method to change the currently selected method.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                                         Yes

 Need to authenticate before use                                 No

 Loads the block diagram into memory                                      Yes

 Remote access allowed                                                   Yes

OutputOutput TerminalsTerminals [][]
OutputOutput TerminalsTerminals [][]

Returns references to the output parameters.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes


                                                    © National Instruments 9143

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9143 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9144 ordinal=9144 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                                   Yes

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

   ConstructorConstructor
    ConstructorConstructor

       Constructor Properties
   ConstructorConstructor PropertiesProperties
    ConstructorConstructor PropertiesProperties


        Property           Description

         Constructor Node   Gets or sets the class name for the constructor node. This property is similar to
         Class Name        the MethClassName for the Invoke Node.

         Input Terminals []   Returns an array of references to the input parameter terminals.

        Output Terminals
                           Returns an array of references to the output parameter terminals.
             []

   ConstructorConstructor NodeNode ClassClass NameName
    ConstructorConstructor NodeNode ClassClass NameName

       Gets or sets the class name for the constructor node. This property is similar to the


9144   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9144 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9145 ordinal=9145 -->
## Property and Method Reference

Property and Method Reference

MethClassName for the Invoke Node.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                      No

InputInput TerminalsTerminals [][]
InputInput TerminalsTerminals [][]

Returns an array of references to the input parameter terminals.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

                                                    © National Instruments 9145

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9145 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9146 ordinal=9146 -->
## Property and Method Reference

Property and Method Reference


        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

   OutputOutput TerminalsTerminals [][]
   OutputOutput TerminalsTerminals [][]

       Returns an array of references to the output parameter terminals.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

   BundlerBundler

      Bundler Methods

      Bundler Properties


9146   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9146 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9147 ordinal=9147 -->
## Property and Method Reference

Property and Method Reference

BundlerBundler MethodsMethods
BundlerBundler MethodsMethods


 Method       Description

             Adds a new input terminal after the item specified by Index and returns a reference AddInputAfter                to the new terminal.

 RemoveInput  Removes the input terminal at the Index you specify.

AddInputAfterAddInputAfter
AddInputAfterAddInputAfter

Adds a new input terminal after the item specified by Index and returns a reference to
the new terminal.

Parameters

       Data Name       Required  Description       type

                          Specifies the index of the item after which to add the new item. To add the
 Index        Yes                       item to the beginning of the node, specify –1 for Index.


Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                         No

 Available in Real-Time Operating System                                 No

                                                    © National Instruments 9147

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9147 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9148 ordinal=9148 -->
## Property and Method Reference

Property and Method Reference


         Settable when the VI is running                                        No

        Loads the front panel into memory                                     No

       Need to authenticate before use                                       No

        Loads the block diagram into memory                                   No

       Remote access allowed                                                           Yes

   RemoveInputRemoveInput
   RemoveInputRemoveInput

      Removes the input terminal at the Index you specify.

     Parameters

      Name    Data type     Required     Description

         Index                   Yes            Specifies the index of the item to remove.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes


9148   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9148 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9149 ordinal=9149 -->
## Property and Method Reference

Property and Method Reference

BundlerBundler PropertiesProperties
BundlerBundler PropertiesProperties


 Property           Description

 Input Count        Gets or sets the number of input terminals on a node.

 Input Terminals     Returns an array of references to the input terminals on a node.

InputInput CountCount
InputInput CountCount

Gets or sets the number of input terminals on a node.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes


                                                    © National Instruments 9149

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9149 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9150 ordinal=9150 -->
## Property and Method Reference

Property and Method Reference

   InputInput TerminalsTerminals
    InputInput TerminalsTerminals

       Returns an array of references to the input terminals on a node.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

   BuildArrayBuildArray
    BuildArrayBuildArray

       BuildArray Properties
   BuildArrayBuildArray PropertiesProperties
    BuildArrayBuildArray PropertiesProperties


9150   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9150 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9151 ordinal=9151 -->
## Property and Method Reference

Property and Method Reference


 Property     Description

 Concatenate  Gets or sets whether a Build Array function is configured to concatenate inputs. If
 Inputs       TRUE, the function concatenates inputs.

ConcatenateConcatenate InputsInputs
ConcatenateConcatenate InputsInputs

Gets or sets whether a Build Array function is configured to concatenate inputs. If
TRUE, the function concatenates inputs.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

NamedBundlerNamedBundler
NamedBundlerNamedBundler

NamedBundler Properties

                                                    © National Instruments 9151

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9151 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9152 ordinal=9152 -->
## Property and Method Reference

Property and Method Reference

   NamedBundlerNamedBundler PropertiesProperties
   NamedBundlerNamedBundler PropertiesProperties


        Property        Description

         Available                        Returns an array of the names of available elements in the bundler.         Elements[]

        Element                        Gets or sets the names of the elements in the bundler.        Names[]

          Full Element    Gets or sets the complete names of elements in the bundler, including the name
        Names[]         at each level of the hierarchy.

          Full Names
                        Gets or sets whether to display the full names of elements.          Visible?

   AvailableAvailable Elements[]Elements[]
    AvailableAvailable Elements[]Elements[]

       Returns an array of the names of available elements in the bundler.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No


9152   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9152 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9153 ordinal=9153 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

ElementElement Names[]Names[]
ElementElement Names[]Names[]

Gets or sets the names of the elements in the bundler.

This property returns names at each level of the hierarchy delimited by periods (.). You
cannot set hierarchical element names. The Full Element Names[] property provides
more support for hierarchical names.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                 No

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes


                                                    © National Instruments 9153

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9153 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9154 ordinal=9154 -->
## Property and Method Reference

Property and Method Reference

    FullFull ElementElement Names[]Names[]
    FullFull ElementElement Names[]Names[]

       Gets or sets the complete names of elements in the bundler, including the name at
      each level of the hierarchy.

      Element names are formatted as a cluster that contains an array of strings that
       represent the hierarchical name.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                 No

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    FullFull NamesNames Visible?Visible?
    FullFull NamesNames Visible?Visible?

       Gets or sets whether to display the full names of elements.


9154   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9154 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9155 ordinal=9155 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                 No

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

UnbundlerUnbundler

Unbundler Methods

Unbundler Properties
UnbundlerUnbundler MethodsMethods
UnbundlerUnbundler MethodsMethods


 Method      Description

 Add Output  Adds a new output terminal after the item whose Index you specify and returns a
 After         reference to the new terminal.

 Remove
            Removes the output terminal at the Index you specify.
 Output


                                                    © National Instruments 9155

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9155 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9156 ordinal=9156 -->
## Property and Method Reference

Property and Method Reference

   AddAdd OutputOutput AfterAfter
   AddAdd OutputOutput AfterAfter

      Adds a new output terminal after the item whose Index you specify and returns a
       reference to the new terminal.

     Parameters

              Data      Name       Required  Description               type

                                   Specifies the index of the item after which to add the new item. To add the
         Index        Yes                               item to the beginning of the node, specify –1 for Index.


     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                         No

         Available in Real-Time Operating System                                 No

         Settable when the VI is running                                        No

        Loads the front panel into memory                                     No

       Need to authenticate before use                                       No

        Loads the block diagram into memory                                   No

       Remote access allowed                                                           Yes


9156   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9156 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9157 ordinal=9157 -->
## Property and Method Reference

Property and Method Reference

RemoveRemove OutputOutput
RemoveRemove OutputOutput

Removes the output terminal at the Index you specify.

Parameters

 Name    Data type     Required     Description

 Index                   Yes            Specifies the index of the item to remove.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                              No

 Available in Real-Time Operating System                      No

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

UnbundlerUnbundler PropertiesProperties
UnbundlerUnbundler PropertiesProperties


                                                    © National Instruments 9157

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9157 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9158 ordinal=9158 -->
## Property and Method Reference

Property and Method Reference


        Property             Description

        Output Count         Gets or sets the number of output terminals on the node.

        Output Terminals[]    Returns an array of references to the output terminals on the node.

   OutputOutput CountCount
   OutputOutput CountCount

       Gets or sets the number of output terminals on the node.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   OutputOutput Terminals[]Terminals[]
   OutputOutput Terminals[]Terminals[]

       Returns an array of references to the output terminals on the node.


9158   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9158 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9159 ordinal=9159 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

NamedUnbundlerNamedUnbundler
NamedUnbundlerNamedUnbundler

NamedUnbundler Properties
NamedUnbundlerNamedUnbundler PropertiesProperties
NamedUnbundlerNamedUnbundler PropertiesProperties


 Property       Description

 Available
                Returns an array of the names of available elements in the unbundler.
 Elements[]

 Element
                Gets or sets the names of the elements in the unbundler.
 Names[]

 Full Element    Gets or sets the complete names of elements in the unbundler, including the name

                                                    © National Instruments 9159

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9159 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9160 ordinal=9160 -->
## Property and Method Reference

Property and Method Reference


        Property       Description

        Names[]         at each level of the hierarchy.

          Full Names                        Gets or sets whether to display the full names of elements.          Visible?

   AvailableAvailable Elements[]Elements[]
    AvailableAvailable Elements[]Elements[]

       Returns an array of the names of available elements in the unbundler.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

   ElementElement Names[]Names[]
   ElementElement Names[]Names[]

       Gets or sets the names of the elements in the unbundler.

9160   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9160 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9161 ordinal=9161 -->
## Property and Method Reference

Property and Method Reference

This property returns names at each level of the hierarchy delimited by periods (.). You
cannot set hierarchical element names. The Full Element Names[] property provides
more support for hierarchical names.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                 No

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

FullFull ElementElement Names[]Names[]
FullFull ElementElement Names[]Names[]

Gets or sets the complete names of elements in the unbundler, including the name at
each level of the hierarchy.

Element names are formatted as a cluster that contains an array of strings that
represent the hierarchical name.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 9161

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9161 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9162 ordinal=9162 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                 No

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    FullFull NamesNames Visible?Visible?
    FullFull NamesNames Visible?Visible?

       Gets or sets whether to display the full names of elements.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                 No

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes


9162   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9162 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9163 ordinal=9163 -->
## Property and Method Reference

Property and Method Reference

RegisterForEventsRegisterForEvents

RegisterForEvents Properties
RegisterForEventsRegisterForEvents PropertiesProperties
RegisterForEventsRegisterForEvents PropertiesProperties


 Property  Description

 Event     Gets or sets an array of Booleans where each element gets or sets whether an event item
 Locks    on the referenced Register For Events function locks the front panel when generated.
 Panel    LabVIEW ignores this property for non-UI events.

 Event     Gets or sets an array of event types. You can get or set one event type for each event item
 Types    on the referenced Register For Events function.

EventEvent LocksLocks PanelPanel
EventEvent LocksLocks PanelPanel

Gets or sets an array of Booleans where each element gets or sets whether an event
item on the referenced Register For Events function locks the front panel when
generated. LabVIEW ignores this property for non-UI events.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


                                                    © National Instruments 9163

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9163 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9164 ordinal=9164 -->
## Property and Method Reference

Property and Method Reference


         Settable when the VI is running                                 No

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   EventEvent TypesTypes
   EventEvent TypesTypes

       Gets or sets an array of event types. You can get or set one event type for each event
      item on the referenced Register For Events function.

       For detailed on help on a specific user event, refer to the help topic of the same name
       as the event.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                 No

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes


9164   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9164 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9165 ordinal=9165 -->
## Property and Method Reference

Property and Method Reference

BuildSetNodeBuildSetNode
BuildMapNodeBuildMapNode
AssertStructuralTypeMismatchNodeAssertStructuralTypeMismatchNode
ControlReferenceConstantControlReferenceConstant

ControlReferenceConstant Properties
ControlReferenceConstantControlReferenceConstant PropertiesProperties


 Property    Description

 Control      Gets or sets the data type to which the control reference constant is linked. The
 Reference    reference can be a VI reference, an application reference, a control reference, or a
 Linked To    variable object reference.

ControlControl ReferenceReference LinkedLinked ToTo
ControlControl ReferenceReference LinkedLinked ToTo

Gets or sets the data type to which the control reference constant is linked. The
reference can be a VI reference, an application reference, a control reference, or a
variable object reference.

Remarks

The following table lists the characteristics of this property.


 Data type


                                                    © National Instruments 9165

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9165 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9166 ordinal=9166 -->
## Property and Method Reference

Property and Method Reference


         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                 No

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    StaticVIReferenceStaticVIReference

       StaticVIReference Properties
    StaticVIReferenceStaticVIReference PropertiesProperties


        Property  Description

           Is Strict    Sets or returns the strict value for the Static VI Reference function.

          VI Name   Sets or returns the name of the VI that the Static VI Reference function references.

          VI Path    Sets or returns the path to the VI that the Static VI Reference function references.

    IsIs StrictStrict
     IsIs StrictStrict

       Sets or returns the strict value for the Static VI Reference function.

     Remarks

      The following table lists the characteristics of this property.


9166   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9166 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9167 ordinal=9167 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                 No

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

VIVI NameName
VIVI NameName

Sets or returns the name of the VI that the Static VI Reference function references.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                 No

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes


                                                    © National Instruments 9167

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9167 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9168 ordinal=9168 -->
## Property and Method Reference

Property and Method Reference

   VIVI PathPath
    VIVI PathPath

       Sets or returns the path to the VI that the Static VI Reference function references.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                 No

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   XNodeXNode
   XDataNodeXDataNode

      XDataNode Properties
   XDataNodeXDataNode PropertiesProperties
   XDataNodeXDataNode PropertiesProperties

9168   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9168 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9169 ordinal=9169 -->
## Property and Method Reference

Property and Method Reference


 Property                   Description

 Is XNode Hidden            Gets or sets whether the XNode is hidden.

IsIs XNodeXNode HiddenHidden
IsIs XNodeXNode HiddenHidden

Gets or sets whether the XNode is hidden.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                 No

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

SharedVariableNodeSharedVariableNode

SharedVariableNode Methods

SharedVariableNode Properties
SharedVariableNodeSharedVariableNode MethodsMethods

                                                    © National Instruments 9169

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9169 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9170 ordinal=9170 -->
## Property and Method Reference

Property and Method Reference


       Method    Description

       Change                 Changes the shared variable node to a constant and returns a reference to the constant.         to                 LabVIEW automatically closes the reference to the shared variable node.        Constant

       Change                 Changes the shared variable node to a control and returns a reference to the control.
         to                 LabVIEW automatically closes the reference to the shared variable node.         Control

       Change                 Changes the shared variable node to an indicator and returns a reference to the         to                      indicator. LabVIEW automatically closes the reference to the shared variable node.
         Indicator

   ChangeChange toto ConstantConstant
   ChangeChange toto ConstantConstant

      Changes the shared variable node to a constant and returns a reference to the
       constant. LabVIEW automatically closes the reference to the shared variable node.

     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                         No

         Available in Real-Time Operating System                                 No

         Settable when the VI is running                                        No

        Loads the front panel into memory                                     No

       Need to authenticate before use                                       No

        Loads the block diagram into memory                                              Yes

       Remote access allowed                                                           Yes


9170   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9170 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9171 ordinal=9171 -->
## Property and Method Reference

Property and Method Reference

ChangeChange toto ControlControl
ChangeChange toto ControlControl

Changes the shared variable node to a control and returns a reference to the control.
LabVIEW automatically closes the reference to the shared variable node.

Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                         No

 Available in Real-Time Operating System                                 No

 Settable when the VI is running                                        No

 Loads the front panel into memory                                                 Yes

 Need to authenticate before use                                       No

 Loads the block diagram into memory                                              Yes

 Remote access allowed                                                           Yes

ChangeChange toto IndicatorIndicator
ChangeChange toto IndicatorIndicator

Changes the shared variable node to an indicator and returns a reference to the
indicator. LabVIEW automatically closes the reference to the shared variable node.

Remarks

The following table lists the characteristics of this method.


                                                    © National Instruments 9171

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9171 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9172 ordinal=9172 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Available in Run-Time Engine                                         No

         Available in Real-Time Operating System                                 No

         Settable when the VI is running                                        No

        Loads the front panel into memory                                                 Yes

       Need to authenticate before use                                       No

        Loads the block diagram into memory                                              Yes

       Remote access allowed                                                           Yes

   SharedVariableNodeSharedVariableNode PropertiesProperties


        Property             Description

                             Returns whether you can set the Shared Variable node to an absolute        Allow Absolute?
                            connection with the variable.

        Allow Direct?         Returns whether you can set the Shared Variable node to use direct access.

                             Returns whether you can read data from variable bound to the Shared        Allow Read?                               Variable node.

                             Returns whether you can set the Shared Variable node to a target-relative        Allow Relative?                            connection with the variable.

                             Returns whether you can set the Shared Variable node to use scanned        Allow Scanned?                                access.

                             Returns whether you can write data to the variable bound to the Shared
        Allow Write?
                               Variable node.

        IOVLocalAccessMode Gets or sets the access mode of the Shared Variable node.

                             Gets or sets whether the connection between a shared variable and a Shared
         Relative Mode
                               Variable node is absolute, target-relative, or the default mode.

                             Gets or sets a reference to the shared variable in the LabVIEW Project that is
        Shared Variable      associated with a Shared Variable node. If the VI with the Shared Variable
         Project Item        node is not part of a project, or if the shared variable is located in a different
                                project than the VI, LabVIEW returns an error.

       Show Timeout?      Gets or sets whether LabVIEW shows the ms timeout input and timed out?

9172   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9172 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9173 ordinal=9173 -->
## Property and Method Reference

Property and Method Reference


 Property             Description

                    output on a Shared Variable node.

                     Gets or sets whether LabVIEW shows the timestamp terminal on a Shared Show Timestamp?                       Variable node.

 Timeout Allowed?    Returns whether a Shared Variable node supports a timeout period.

                     Returns whether LabVIEW can display a timestamp for a Shared Variable Timestamp Allowed?                    node.

                     Gets or sets whether a Shared Variable node is configured to read or write
 Write?                data. TRUE corresponds to writing data, and FALSE corresponds to reading
                       data.

AllowAllow Absolute?Absolute?
AllowAllow Absolute?Absolute?

Returns whether you can set the Shared Variable node to an absolute connection with
the variable.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes


                                                    © National Instruments 9173

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9173 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9174 ordinal=9174 -->
## Property and Method Reference

Property and Method Reference

   AllowAllow Direct?Direct?
   AllowAllow Direct?Direct?

       Returns whether you can set the Shared Variable node to use direct access.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

   AllowAllow Read?Read?
   AllowAllow Read?Read?

       Returns whether you can read data from variable bound to the Shared Variable node.

     Remarks

      The following table lists the characteristics of this property.


        Data type

9174   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9174 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9175 ordinal=9175 -->
## Property and Method Reference

Property and Method Reference


 Permissions                                                     Read Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

AllowAllow Relative?Relative?
AllowAllow Relative?Relative?

Returns whether you can set the Shared Variable node to a target-relative connection
with the variable.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                       No


                                                    © National Instruments 9175

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9175 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9176 ordinal=9176 -->
## Property and Method Reference

Property and Method Reference

   AllowAllow Scanned?Scanned?
   AllowAllow Scanned?Scanned?

       Returns whether you can set the Shared Variable node to use scanned access.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

   AllowAllow Write?Write?
   AllowAllow Write?Write?

       Returns whether you can write data to the variable bound to the Shared Variable node.

     Remarks

      The following table lists the characteristics of this property.


        Data type

9176   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9176 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9177 ordinal=9177 -->
## Property and Method Reference

Property and Method Reference


 Permissions                                                     Read Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

IOVLocalAccessModeIOVLocalAccessMode
IOVLocalAccessModeIOVLocalAccessMode

Gets or sets the access mode of the Shared Variable node.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                 No

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes


                                                    © National Instruments 9177

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9177 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9178 ordinal=9178 -->
## Property and Method Reference

Property and Method Reference

    RelativeRelative ModeMode
    RelativeRelative ModeMode

       Gets or sets whether the connection between a shared variable and a Shared Variable
      node is absolute, target-relative, or the default mode.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                 No

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   SharedShared VariableVariable ProjectProject ItemItem
   SharedShared VariableVariable ProjectProject ItemItem

       Gets or sets a reference to the shared variable in the LabVIEW Project that is associated
       with a Shared Variable node. If the VI with the Shared Variable node is not part of a
        project, or if the shared variable is located in a different project than the VI, LabVIEW
       returns an error.


9178   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9178 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9179 ordinal=9179 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                 No

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

ShowShow Timeout?Timeout?
ShowShow Timeout?Timeout?

Gets or sets whether LabVIEW shows the ms timeout input and timed out? output on a
Shared Variable node.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                 No


                                                    © National Instruments 9179

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9179 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9180 ordinal=9180 -->
## Property and Method Reference

Property and Method Reference


        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   ShowShow Timestamp?Timestamp?
   ShowShow Timestamp?Timestamp?

       Gets or sets whether LabVIEW shows the timestamp terminal on a Shared Variable
      node.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                 No

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes


9180   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9180 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9181 ordinal=9181 -->
## Property and Method Reference

Property and Method Reference

TimeoutTimeout Allowed?Allowed?
TimeoutTimeout Allowed?Allowed?

Returns whether a Shared Variable node supports a timeout period.

You only can enable a timeout period for Shared Variable nodes configured to read
data. You cannot enable a timeout period for nodes that access I/O variables locally.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

TimestampTimestamp Allowed?Allowed?
TimestampTimestamp Allowed?Allowed?

Returns whether LabVIEW can display a timestamp for a Shared Variable node.

Timestamps are supported only by Shared Variable nodes that are configured to read
data.


                                                    © National Instruments 9181

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9181 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9182 ordinal=9182 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

   Write?Write?
    Write?Write?

       Gets or sets whether a Shared Variable node is configured to read or write data. TRUE
      corresponds to writing data, and FALSE corresponds to reading data.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                 No


9182   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9182 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9183 ordinal=9183 -->
## Property and Method Reference

Property and Method Reference


 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

InPlaceBorderNodeInPlaceBorderNode

InPlaceBorderNode Properties
InPlaceBorderNodeInPlaceBorderNode PropertiesProperties


 Property  Description

 Partner    Returns the partner of the specified border node on the In Place Element structure.

PartnerPartner
PartnerPartner

Returns the partner of the specified border node on the In Place Element structure.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

 Settable when the VI is running                                  No


                                                    © National Instruments 9183

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9183 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9184 ordinal=9184 -->
## Property and Method Reference

Property and Method Reference


        Loads the front panel into memory                                         Yes

       Need to authenticate before use                                 No

        Loads the block diagram into memory                                      Yes

       Remote access allowed                                                   Yes

   InPlaceElementNodeInPlaceElementNode
   InPlaceVariantNodeInPlaceVariantNode
   InPlaceArrayNodeInPlaceArrayNode

       InPlaceArrayNode Methods

       InPlaceArrayNode Properties
   InPlaceArrayNodeInPlaceArrayNode MethodsMethods
   InPlaceArrayNodeInPlaceArrayNode MethodsMethods


       Method  Description

                  Resizes the expandable Array Index / Replace Elements border node to the height you
         Resize
                    specify.

   ResizeResize
    ResizeResize

       Resizes the expandable Array Index / Replace Elements border node to the height you
        specify.


9184   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9184 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9185 ordinal=9185 -->
## Property and Method Reference

Property and Method Reference

Parameters

        Data Name           Required  Description
        type

                               Specifies the height, in pixels, to which you want to resize the border Height           Yes                           node.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                              No

 Available in Real-Time Operating System                      No

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

InPlaceArrayNodeInPlaceArrayNode PropertiesProperties
InPlaceArrayNodeInPlaceArrayNode PropertiesProperties


 Property      Description

 Array Input    Returns a reference to the array input on an Array Index / Replace Elements border
 Terminal     node.

              Gets or sets the number of index inputs an Array Index / Replace Elements border
 Index Count  node contains. When writing the number of inputs, this property grows the border
            node to accommodate the number of indexes you specify.


                                                    © National Instruments 9185

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9185 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9186 ordinal=9186 -->
## Property and Method Reference

Property and Method Reference


        Property      Description

         Index         Returns an array of references to the index terminals of an Array Index / Replace
          Terminalsl[][] Elements border node.

        Output       Returns an array of references to the outputs on an Array Index / Replace Elements
         Terminals[]   border node.

        Terminal      Returns the height, in pixels, of each terminal of an expandable border node on the
        Height         In Place Element Structure.

   ArrayArray InputInput TerminalTerminal
    ArrayArray InputInput TerminalTerminal

       Returns a reference to the array input on an Array Index / Replace Elements border
      node.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes


9186   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9186 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9187 ordinal=9187 -->
## Property and Method Reference

Property and Method Reference

IndexIndex CountCount
IndexIndex CountCount

Gets or sets the number of index inputs an Array Index / Replace Elements border node
contains. When writing the number of inputs, this property grows the border node to
accommodate the number of indexes you specify.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

IndexIndex Terminalsl[][]Terminalsl[][]
IndexIndex Terminalsl[][]Terminalsl[][]

Returns an array of references to the index terminals of an Array Index / Replace
Elements border node.


                                                    © National Instruments 9187

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9187 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9188 ordinal=9188 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

   OutputOutput Terminals[]Terminals[]
   OutputOutput Terminals[]Terminals[]

       Returns an array of references to the outputs on an Array Index / Replace Elements
      border node.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No


9188   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9188 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9189 ordinal=9189 -->
## Property and Method Reference

Property and Method Reference


 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

TerminalTerminal HeightHeight
TerminalTerminal HeightHeight

Returns the height, in pixels, of each terminal of an expandable border node on the In
Place Element Structure.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

InPlaceClusterNodeInPlaceClusterNode

InPlaceClusterNode Methods


                                                    © National Instruments 9189

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9189 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9190 ordinal=9190 -->
## Property and Method Reference

Property and Method Reference

       InPlaceClusterNode Properties
   InPlaceClusterNodeInPlaceClusterNode MethodsMethods
   InPlaceClusterNodeInPlaceClusterNode MethodsMethods


       Method       Description

       Add Output   Adds a new output after the item whose Index you specify and returns a reference to
          After          the new terminal.

       Remove                   Removes the output terminal at the Index you specify.        Output

                        Resizes the expandable Unbundle / Bundle Element border node to the height you         Resize                          specify.

   AddAdd OutputOutput AfterAfter
   AddAdd OutputOutput AfterAfter

      Adds a new output after the item whose Index you specify and returns a reference to
       the new terminal.

     Parameters

              Data
      Name       Required  Description
               type

                                   Specifies the index of the item after which to add the new item. To add the
         Index        Yes                               item to the beginning of the node, specify –1 for Index.


     Remarks

      The following table lists the characteristics of this method.

9190   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9190 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9191 ordinal=9191 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Available in Run-Time Engine                                         No

 Available in Real-Time Operating System                                 No

 Settable when the VI is running                                        No

 Loads the front panel into memory                                     No

 Need to authenticate before use                                       No

 Loads the block diagram into memory                                   No

 Remote access allowed                                                           Yes

RemoveRemove OutputOutput
RemoveRemove OutputOutput

Removes the output terminal at the Index you specify.

Parameters

 Name    Data type     Required     Description

 Index                   Yes            Specifies the index of the item to remove.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                              No

 Available in Real-Time Operating System                      No

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

                                                    © National Instruments 9191

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9191 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9192 ordinal=9192 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

   ResizeResize
    ResizeResize

       Resizes the expandable Unbundle / Bundle Element border node to the height you
        specify.

     Parameters

               Data      Name           Required  Description
               type

                                        Specifies the height, in pixels, to which you want to resize the border        Height           Yes
                                  node.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

9192   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9192 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9193 ordinal=9193 -->
## Property and Method Reference

Property and Method Reference

InPlaceClusterNodeInPlaceClusterNode PropertiesProperties
InPlaceClusterNodeInPlaceClusterNode PropertiesProperties


 Property    Description

 Available            Returns an array of the labels of the named elements in the cluster. Elements[]

 Element            Gets or sets the names of the elements in the cluster. Names[]

 Full        Gets or sets an array of the full, hierarchical names of the elements in the cluster.
 Element    Element names are formatted as a cluster that contains an array of strings that
 Names[]    represent the hierarchical name.

 Full Names            Gets or sets whether LabVIEW displays the full names of elements in the cluster. Visible?

 Output     Gets or sets the number of output terminals on the expandable Unbundle / Bundle
 Count      Elements border node.

 Output     Returns an array of references to the output terminals on an Unbundle / Bundle
 Terminals[] Elements border node.

 Terminal    Resizes the expandable Unbundle / Bundle Elements border node to the height in
 Height       pixels you specify.

AvailableAvailable Elements[]Elements[]
AvailableAvailable Elements[]Elements[]

Returns an array of the labels of the named elements in the cluster.

Remarks

The following table lists the characteristics of this property.


 Data type

                                                    © National Instruments 9193

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9193 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9194 ordinal=9194 -->
## Property and Method Reference

Property and Method Reference


         Permissions                                                     Read Only

         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

   ElementElement Names[]Names[]
   ElementElement Names[]Names[]

       Gets or sets the names of the elements in the cluster.

       This property returns names at each level of the hierarchy delimited by periods (.). You
      cannot set hierarchical element names. The Full Element Names[] property provides
      more support for hierarchical names.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                 No

        Loads the front panel into memory                              No

       Need to authenticate before use                                No


9194   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9194 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9195 ordinal=9195 -->
## Property and Method Reference

Property and Method Reference


 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

FullFull ElementElement Names[]Names[]
FullFull ElementElement Names[]Names[]

Gets or sets an array of the full, hierarchical names of the elements in the cluster.
Element names are formatted as a cluster that contains an array of strings that
represent the hierarchical name.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                 No

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

FullFull NamesNames Visible?Visible?
FullFull NamesNames Visible?Visible?

Gets or sets whether LabVIEW displays the full names of elements in the cluster.


                                                    © National Instruments 9195

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9195 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9196 ordinal=9196 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                 No

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   OutputOutput CountCount
   OutputOutput CountCount

       Gets or sets the number of output terminals on the expandable Unbundle / Bundle
      Elements border node.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes


9196   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9196 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9197 ordinal=9197 -->
## Property and Method Reference

Property and Method Reference


 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

OutputOutput Terminals[]Terminals[]
OutputOutput Terminals[]Terminals[]

Returns an array of references to the output terminals on an Unbundle / Bundle
Elements border node.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes


                                                    © National Instruments 9197

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9197 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9198 ordinal=9198 -->
## Property and Method Reference

Property and Method Reference

   TerminalTerminal HeightHeight
   TerminalTerminal HeightHeight

       Resizes the expandable Unbundle / Bundle Elements border node to the height in
        pixels you specify.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

   InPlaceDataValRefNodeInPlaceDataValRefNode

       InPlaceDataValRefNode Properties
   InPlaceDataValRefNodeInPlaceDataValRefNode PropertiesProperties
   InPlaceDataValRefNodeInPlaceDataValRefNode PropertiesProperties


9198   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9198 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9199 ordinal=9199 -->
## Property and Method Reference

Property and Method Reference


 Property      Description

 Allow Parallel When set to true, allows a Data Value Reference Write node to be left unwired
 Read Only     without breaking the VI. It allows multiple readers to be looking at the contents of
 Access        the DVR simultaneously.

AllowAllow ParallelParallel ReadRead OnlyOnly AccessAccess
AllowAllow ParallelParallel ReadRead OnlyOnly AccessAccess

When set to true, allows a Data Value Reference Write node to be left unwired without
breaking the VI. It allows multiple readers to be looking at the contents of the DVR
simultaneously.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                 No

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                                    Yes

 Remote access allowed                                      No

InPlaceArraySplitNodeInPlaceArraySplitNode

InPlaceArraySplitNode Properties


                                                    © National Instruments 9199

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9199 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9200 ordinal=9200 -->
## Property and Method Reference

Property and Method Reference

   InPlaceArraySplitNodeInPlaceArraySplitNode PropertiesProperties
    InPlaceArraySplitNodeInPlaceArraySplitNode PropertiesProperties


        Property   Description

         Array      Returns a reference to the array terminal of an Array Split / Replace Subarrays border
        Terminal   node.

        Length     Returns an array of references to the split length terminals of an Array Split / Replace
         Terminals  Subarrays border node.

          Split       Gets or sets the number of times the Array Split / Replace Subarrays border node splits
        Count      the input array.

                    Gets or sets the dimension along which LabVIEW splits the input array to an Array Split
          Split         / Replace Subarrays border node. For example, if you select 1 for a two-dimensional
        Dimension  array, LabVIEW creates the subarrays from columns of the original array. If you select 0,
                  LabVIEW creates the subarrays from rows of the original array.

          Split       Returns an array of references to the subarray terminals of an Array Split / Replace
         Terminals  Subarrays border node.

        Terminal   Returns the height, in pixels, of a split length terminal on an Array Split / Replace
        Height     Subarrays border node.

   ArrayArray TerminalTerminal
    ArrayArray TerminalTerminal

       Returns a reference to the array terminal of an Array Split / Replace Subarrays border
      node.

     Remarks

      The following table lists the characteristics of this property.


        Data type


9200   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9200 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9201 ordinal=9201 -->
## Property and Method Reference

Property and Method Reference


 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

LengthLength TerminalsTerminals
LengthLength TerminalsTerminals

Returns an array of references to the split length terminals of an Array Split / Replace
Subarrays border node.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                 No

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes


                                                    © National Instruments 9201

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9201 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9202 ordinal=9202 -->
## Property and Method Reference

Property and Method Reference

    SplitSplit CountCount
    SplitSplit CountCount

       Gets or sets the number of times the Array Split / Replace Subarrays border node splits
       the input array.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    SplitSplit DimensionDimension
    SplitSplit DimensionDimension

       Gets or sets the dimension along which LabVIEW splits the input array to an Array Split
         / Replace Subarrays border node. For example, if you select 1 for a two-dimensional
        array, LabVIEW creates the subarrays from columns of the original array. If you select 0,
      LabVIEW creates the subarrays from rows of the original array.

       Using this property in write mode is similar to right-clicking an Array Split / Replace

9202   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9202 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9203 ordinal=9203 -->
## Property and Method Reference

Property and Method Reference

Subarrays border node and selecting Split Dimension to specify in which dimension to
split the array.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

SplitSplit TerminalsTerminals
SplitSplit TerminalsTerminals

Returns an array of references to the subarray terminals of an Array Split / Replace
Subarrays border node.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes


                                                    © National Instruments 9203

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9203 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9204 ordinal=9204 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                                   Yes

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

   TerminalTerminal HeightHeight
   TerminalTerminal HeightHeight

       Returns the height, in pixels, of a split length terminal on an Array Split / Replace
       Subarrays border node.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                                   Yes

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

    InPlaceVariantAttributeNodeInPlaceVariantAttributeNode


9204   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9204 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9205 ordinal=9205 -->
## Property and Method Reference

Property and Method Reference

InPlaceVariantAttributeNode Methods

InPlaceVariantAttributeNode Properties
InPlaceVariantAttributeNodeInPlaceVariantAttributeNode MethodsMethods
InPlaceVariantAttributeNodeInPlaceVariantAttributeNode MethodsMethods


 Method     Description

 Resize       Set the height in pixels of the Inplace Variant Attribute Node.

ResizeResize
ResizeResize

Set the height in pixels of the Inplace Variant Attribute Node.

Parameters

 Name          Data type              Required               Description

 height                                   Yes

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                              No

 Available in Real-Time Operating System                      No

 Settable when the VI is running                             No

 Loads the front panel into memory                                  Yes

                                                    © National Instruments 9205

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9205 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9206 ordinal=9206 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                            No

        Loads the block diagram into memory                               Yes

       Remote access allowed                                             Yes

   InPlaceVariantAttributeNodeInPlaceVariantAttributeNode PropertiesProperties
    InPlaceVariantAttributeNodeInPlaceVariantAttributeNode PropertiesProperties


        Property   Description

                Number of variant attribute terminals. Also the number of name terminals. There will          Attribute                   always at least be one. When written, this property will add or delete name and
        Count                      attribute pairs to both paired nodes.

          Attribute
        Terminal   Height in pixels of variant name and attribute terminals.
        Height

          Attribute                    Array of attribute input or output terminals.         Terminals

       Found                    Array of Boolean found? terminals.         Terminals

        Header    Height in pixels of the Variant input/output terminal. This is the fixed-size top section of
        Height     the node.

      Name
                    Array of name input or output terminals.         Terminals

         Variant
                 The Variant input or output terminal.
         Input

   AttributeAttribute CountCount
    AttributeAttribute CountCount

     Number of variant attribute terminals. Also the number of name terminals. There will


9206   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9206 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9207 ordinal=9207 -->
## Property and Method Reference

Property and Method Reference

always at least be one. When written, this property will add or delete name and
attribute pairs to both paired nodes.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                 No

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                                    Yes

 Remote access allowed                                                  Yes

AttributeAttribute TerminalTerminal HeightHeight
AttributeAttribute TerminalTerminal HeightHeight

Height in pixels of variant name and attribute terminals.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No


                                                    © National Instruments 9207

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9207 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9208 ordinal=9208 -->
## Property and Method Reference

Property and Method Reference


         Settable when the VI is running                                  No

        Loads the front panel into memory                                         Yes

       Need to authenticate before use                                 No

        Loads the block diagram into memory                                      Yes

       Remote access allowed                                                   Yes

   AttributeAttribute TerminalsTerminals
    AttributeAttribute TerminalsTerminals

       Array of attribute input or output terminals.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                                         Yes

       Need to authenticate before use                                 No

        Loads the block diagram into memory                                      Yes

       Remote access allowed                                                   Yes


9208   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9208 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9209 ordinal=9209 -->
## Property and Method Reference

Property and Method Reference

FoundFound TerminalsTerminals
FoundFound TerminalsTerminals

Array of Boolean found? terminals.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                                         Yes

 Need to authenticate before use                                 No

 Loads the block diagram into memory                                      Yes

 Remote access allowed                                                   Yes

HeaderHeader HeightHeight
HeaderHeader HeightHeight

Height in pixels of the Variant input/output terminal. This is the fixed-size top section
of the node.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 9209

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9209 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9210 ordinal=9210 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                                         Yes

       Need to authenticate before use                                 No

        Loads the block diagram into memory                                      Yes

       Remote access allowed                                                   Yes

  NameName TerminalsTerminals
   NameName TerminalsTerminals

       Array of name input or output terminals.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                                         Yes

       Need to authenticate before use                                 No

        Loads the block diagram into memory                                      Yes

       Remote access allowed                                                   Yes


9210   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9210 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9211 ordinal=9211 -->
## Property and Method Reference

Property and Method Reference

VariantVariant InputInput
VariantVariant InputInput

The Variant input or output terminal.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                                         Yes

 Need to authenticate before use                                 No

 Loads the block diagram into memory                                      Yes

 Remote access allowed                                                   Yes

InPlaceMapNodeInPlaceMapNode

InPlaceMapNode Methods

InPlaceMapNode Properties
InPlaceMapNodeInPlaceMapNode MethodsMethods
InPlaceMapNodeInPlaceMapNode MethodsMethods


                                                    © National Instruments 9211

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9211 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9212 ordinal=9212 -->
## Property and Method Reference

Property and Method Reference


       Method                                     Description

         Set number of Key/Value Pairs                Set the number of key/value pairs.

   SetSet numbernumber ofof Key/ValueKey/Value PairsPairs
    SetSet numbernumber ofof Key/ValueKey/Value PairsPairs

       Set the number of key/value pairs.

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

   InPlaceMapNodeInPlaceMapNode PropertiesProperties
   InPlaceMapNodeInPlaceMapNode PropertiesProperties


        Property              Description

                                Array of action terminals on the ReplaceMapValueNode. Returns an error
         Action Terminals
                          on the GetMapValueNode.


9212   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9212 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9213 ordinal=9213 -->
## Property and Method Reference

Property and Method Reference


 Property              Description

                        Array of default value terminals from the GetMapValueNode. Returns an DefaultValueTerminals                         error on the ReplaceMapValueNode.

 Found Terminals       Array of found terminals.

 Key Height            Height of key and default value terminals in pixels.

 Key Terminals          Array of key in or out terminals.

 KeyCount           Number of keys.

 Map                The map in or out terminal.

 Map Height           Height of map terminal in pixels.

 Value Terminals        Array of value in or out terminals.

ActionAction TerminalsTerminals
ActionAction TerminalsTerminals

Array of action terminals on the ReplaceMapValueNode. Returns an error on the
GetMapValueNode.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No


                                                    © National Instruments 9213

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9213 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9214 ordinal=9214 -->
## Property and Method Reference

Property and Method Reference


       Remote access allowed                                                   Yes

   DefaultValueTerminalsDefaultValueTerminals
    DefaultValueTerminalsDefaultValueTerminals

       Array of default value terminals from the GetMapValueNode. Returns an error on the
      ReplaceMapValueNode.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

   FoundFound TerminalsTerminals
   FoundFound TerminalsTerminals

       Array of found terminals.


9214   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9214 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9215 ordinal=9215 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

KeyKey HeightHeight
KeyKey HeightHeight

Height of key and default value terminals in pixels.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No


                                                    © National Instruments 9215

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9215 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9216 ordinal=9216 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

   KeyKey TerminalsTerminals
   KeyKey TerminalsTerminals

       Array of key in or out terminals.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

   KeyCountKeyCount
   KeyCountKeyCount

     Number of keys.


9216   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9216 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9217 ordinal=9217 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                 No

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

MapMap
MapMap

The map in or out terminal.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No


                                                    © National Instruments 9217

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9217 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9218 ordinal=9218 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

  MapMap HeightHeight
   MapMap HeightHeight

       Height of map terminal in pixels.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

   ValueValue TerminalsTerminals
   ValueValue TerminalsTerminals

       Array of value in or out terminals.


9218   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9218 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9219 ordinal=9219 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

FeedbackNodeFeedbackNode

FeedbackNode Methods

FeedbackNode Properties
FeedbackNodeFeedbackNode MethodsMethods


 Method       Description

 Highlight      Scrolls to and highlights the initializer of the Feedback Node. To perform the same
 Initializer      action with the rest of the Feedback Node, use the Object Highlight method.

 Replace With  Changes a Feedback Node inside a loop into a shift register. LabVIEW returns an
 Shift Register  error if the Feedback Node is not within a loop.


                                                    © National Instruments 9219

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9219 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9220 ordinal=9220 -->
## Property and Method Reference

Property and Method Reference

   HighlightHighlight InitializerInitializer
    HighlightHighlight InitializerInitializer

        Scrolls to and highlights the initializer of the Feedback Node. To perform the same
       action with the rest of the Feedback Node, use the Object Highlight method.

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

         Settable when the VI is running                             No

        Loads the front panel into memory                                  Yes

       Need to authenticate before use                            No

        Loads the block diagram into memory                               Yes

       Remote access allowed                                             Yes

   ReplaceReplace WithWith ShiftShift RegisterRegister
   ReplaceReplace WithWith ShiftShift RegisterRegister

      Changes a Feedback Node inside a loop into a shift register. LabVIEW returns an error if
       the Feedback Node is not within a loop.

           If the Feedback Node initializer terminal is on a loop, LabVIEW adds the shift register to
       that loop. If the initializer terminal is not on a loop, LabVIEW adds the shift register to
       the innermost loop that contains the Feedback Node.


9220   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9220 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9221 ordinal=9221 -->
## Property and Method Reference

Property and Method Reference

      Note After this method executes, the reference to the Feedback Node is no
        longer valid.

Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                         No

 Available in Real-Time Operating System                                 No

 Settable when the VI is running                                        No

 Loads the front panel into memory                                     No

 Need to authenticate before use                                       No

 Loads the block diagram into memory                                   No

 Remote access allowed                                                           Yes

FeedbackNodeFeedbackNode PropertiesProperties


 Property     Description

             Gets or sets the value of the Feedback Node delay. If the delay is less than 1, LabVIEW Delay              returns an error.

 Direction     Gets and sets the direction the Feedback Node faces.

 Enable
 Terminal     Gets or sets whether the enable terminal of the Feedback Node is shown.
 Shown

 Header
             Gets or sets the cosmetic appearance of the Feedback Node.
 Appearance

             Gets or sets whether this Feedback Node initializes if the FPGA VI resets. If TRUE, this
 Ignore FPGA
            node does not initialize if the FPGA VI resets. This node initializes the next time you
 Reset
            download the FPGA VI to the FPGA target. This property applies only when the
 Method
            Feedback Node is deployed on an FPGA target. This property can have a value of


                                                    © National Instruments 9221

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9221 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9222 ordinal=9222 -->
## Property and Method Reference

Property and Method Reference


        Property     Description

                 TRUE only when the initialization style of the Feedback Node is to initialize on
                    compile or load.

                      Controls where the initialization multiplexer is relative to the core feedback register           Initialization                 when the containing VI is targeted to FPGA. The multiplexer can only be before the       Mux
                         register if a constant is wired in to the initialization terminal. This option only applies         Location                                    if the feedback node is globally initialized.

                      Places the initializer terminal on the innermost loop. When you first call this method,           Initialization                      or when LabVIEW compiles or loads the VI that contains the loop, LabVIEW places the        Type
                      terminal on the node and sets the initialization mode appropriately.

                     Returns TRUE if the initializer terminal of the Feedback Node is on a loop and not           Initializer Is                        globally initialized on the first call of the VI in an execution or when the VI it belongs      On Loop
                       to compiles or loads.

           Initializer                     Returns a reference to the initializer terminal of the Feedback Node.
        Terminal

           Initializer's   Gets or sets a reference to the loop to which the initializer is currently attached, or an
       Loop         invalid reference if the initializer is not on a loop and will be globally initialized.

         Input        Returns a reference to the input terminal of the Feedback Node. The input terminal of
        Terminal    a Feedback Node provides the output value for the node the next time the VI runs.

        Output
                     Returns a reference to the output terminal of the Feedback Node.        Terminal

   DelayDelay
   DelayDelay

       Gets or sets the value of the Feedback Node delay. If the delay is less than 1, LabVIEW
       returns an error.

     Remarks

      The following table lists the characteristics of this property.


        Data type


9222   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9222 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9223 ordinal=9223 -->
## Property and Method Reference

Property and Method Reference


 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                 No

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

DirectionDirection
DirectionDirection

Gets and sets the direction the Feedback Node faces.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                 No

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes


                                                    © National Instruments 9223

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9223 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9224 ordinal=9224 -->
## Property and Method Reference

Property and Method Reference

   EnableEnable TerminalTerminal ShownShown
   EnableEnable TerminalTerminal ShownShown

       Gets or sets whether the enable terminal of the Feedback Node is shown.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                 No

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   HeaderHeader AppearanceAppearance
   HeaderHeader AppearanceAppearance

       Gets or sets the cosmetic appearance of the Feedback Node.

       Using this property to set the appearance is similar to right-clicking a Feedback Node
      and enabling or disabling the Z-Transform View item in the shortcut menu.


9224   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9224 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9225 ordinal=9225 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                 No

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

IgnoreIgnore FPGAFPGA ResetReset MethodMethod
IgnoreIgnore FPGAFPGA ResetReset MethodMethod

Gets or sets whether this Feedback Node initializes if the FPGA VI resets. If TRUE, this
node does not initialize if the FPGA VI resets. This node initializes the next time you
download the FPGA VI to the FPGA target. This property applies only when the
Feedback Node is deployed on an FPGA target. This property can have a value of TRUE
only when the initialization style of the Feedback Node is to initialize on compile or
load.

If you write a value of TRUE, ensure the application does not depend on the value this
Feedback Node returns on the first call after resetting the FPGA VI.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 9225

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9225 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9226 ordinal=9226 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                 No

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    InitializationInitialization MuxMux LocationLocation
    InitializationInitialization MuxMux LocationLocation

       Controls where the initialization multiplexer is relative to the core feedback register
     when the containing VI is targeted to FPGA. The multiplexer can only be before the
        register if a constant is wired in to the initialization terminal. This option only applies if
       the feedback node is globally initialized.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                 No

        Loads the front panel into memory                              No

       Need to authenticate before use                                No


9226   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9226 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9227 ordinal=9227 -->
## Property and Method Reference

Property and Method Reference


 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

InitializationInitialization TypeType
InitializationInitialization TypeType

Places the initializer terminal on the innermost loop. When you first call this method,
or when LabVIEW compiles or loads the VI that contains the loop, LabVIEW places the
terminal on the node and sets the initialization mode appropriately.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                 No

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

InitializerInitializer IsIs OnOn LoopLoop
InitializerInitializer IsIs OnOn LoopLoop

Returns TRUE if the initializer terminal of the Feedback Node is on a loop and not


                                                    © National Instruments 9227

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9227 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9228 ordinal=9228 -->
## Property and Method Reference

Property and Method Reference

       globally initialized on the first call of the VI in an execution or when the VI it belongs to
      compiles or loads.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

    InitializerInitializer TerminalTerminal
     InitializerInitializer TerminalTerminal

       Returns a reference to the initializer terminal of the Feedback Node.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No


9228   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9228 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9229 ordinal=9229 -->
## Property and Method Reference

Property and Method Reference


 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

Initializer'sInitializer's LoopLoop
Initializer'sInitializer's LoopLoop

Gets or sets a reference to the loop to which the initializer is currently attached, or an
invalid reference if the initializer is not on a loop and will be globally initialized.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                 No

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes


                                                    © National Instruments 9229

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9229 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9230 ordinal=9230 -->
## Property and Method Reference

Property and Method Reference

   InputInput TerminalTerminal
    InputInput TerminalTerminal

       Returns a reference to the input terminal of the Feedback Node. The input terminal of
      a Feedback Node provides the output value for the node the next time the VI runs.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

   OutputOutput TerminalTerminal
   OutputOutput TerminalTerminal

       Returns a reference to the output terminal of the Feedback Node.

     Remarks

      The following table lists the characteristics of this property.


9230   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9230 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9231 ordinal=9231 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

MathScriptCallByRefMathScriptCallByRef
SharedVariableDynamicOpenSharedVariableDynamicOpen
SharedVariableDynamicReadSharedVariableDynamicRead
SharedVariableDynamicWriteSharedVariableDynamicWrite
TextBaseNodeTextBaseNode

TextBaseNode Properties
TextBaseNodeTextBaseNode PropertiesProperties


 Property   Description

 Contained Returns the text contained in the Text Base Node reference you specify. You can inspect
 Text       or modify the text contained within the node using this output string.


                                                    © National Instruments 9231

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9231 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9232 ordinal=9232 -->
## Property and Method Reference

Property and Method Reference

   ContainedContained TextText
   ContainedContained TextText

       Returns the text contained in the Text Base Node reference you specify. You can inspect
       or modify the text contained within the node using this output string.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                 No

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                                    Yes

       Remote access allowed                                                  Yes

   ExpressionNodeExpressionNode
   WireWire

       Wire Methods

       Wire Properties
   WireWire MethodsMethods

9232   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9232 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9233 ordinal=9233 -->
## Property and Method Reference

Property and Method Reference


 Method          Description

 Attach Probe      Attaches a probe to the wire and returns a VI reference to the probe.

                  Cleans up the wire so that it has no loose ends, no hidden wire, and few bends Clean Up Wire               and branches.

 Copy Probes To                 Copies the probes from the simulation diagram to the companion diagram.
 Companion

 Delete Joint     Removes the joint closest to Point.

 Disconnect                  Disconnects a terminal from the wire without removing the loose end. Terminal

                    Inserts a new node into the wire and returns a reference to the node. Use only Insert Node                   Style or Path to specify the new node, not both.

 Remove Loose               Removes the loose ends of a wire.
 Ends

 Remove Probe   Removes any probe attached to the wire.

AttachAttach ProbeProbe

Attaches a probe to the wire and returns a VI reference to the probe.

Parameters

 Name         Data type  Required  Description

 Smart Probe VI          No         Specifies the path to the probe VI.


 Open FP?              No         Specifies whether to open the front panel of the probe VI.

 VIClone               No

Remarks

The following table lists the characteristics of this method.


                                                    © National Instruments 9233

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9233 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9234 ordinal=9234 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Available in Run-Time Engine                                         No

         Available in Real-Time Operating System                                 No

         Settable when the VI is running                                                    Yes

        Loads the front panel into memory                                                 Yes

       Need to authenticate before use                                       No

        Loads the block diagram into memory                                              Yes

       Remote access allowed                                                           Yes

   CleanClean UpUp WireWire

       Cleans up the wire so that it has no loose ends, no hidden wire, and few bends and
       branches.

      The wire you clean up maintains connections to all other terminals.

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes


9234   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9234 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9235 ordinal=9235 -->
## Property and Method Reference

Property and Method Reference

CopyCopy ProbesProbes ToTo CompanionCompanion

Copies the probes from the simulation diagram to the companion diagram.

This method only works if the companion diagram has been scripted.

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                             Yes

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

DeleteDelete JointJoint

Removes the joint closest to Point.

Parameters

 Name       Data type  Required  Description

 Point                   Yes        Specifies the Horizontal and Vertical integers of the point.


 Aggressive?          No         Specifies how close the joint must be to Point.


                                                    © National Instruments 9235

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9235 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9236 ordinal=9236 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

   DisconnectDisconnect TerminalTerminal

       Disconnects a terminal from the wire without removing the loose end.

     Parameters

      Name              Data type             Required             Description

        Terminal                                    Yes

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

         Settable when the VI is running                             No

        Loads the front panel into memory                          No


9236   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9236 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9237 ordinal=9237 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

InsertInsert NodeNode

Inserts a new node into the wire and returns a reference to the node. Use only Style or
Path to specify the new node, not both.

Parameters

          Data Name         Required  Description          type

 Style         No        Specifies to insert a built-in function.


 Path         No        Specifies the path to a subVI.

                             Specifies the name of the object on the palettes.

                          Note The Palette String of an object on the palettes differs Palette
             No              between the English version of LabVIEW and each localized String
                                     version of LabVIEW. Also, the Palette String might change
                               between different versions of LabVIEW.


 Insertion               A cluster of horizontal and vertical pairs that indicate the wire
             No
 Point                      coordinates.


Remarks

The following table lists the characteristics of this method.


                                                    © National Instruments 9237

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9237 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9238 ordinal=9238 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Available in Run-Time Engine                                         No

         Available in Real-Time Operating System                                 No

         Settable when the VI is running                                        No

        Loads the front panel into memory                                     No

       Need to authenticate before use                                       No

        Loads the block diagram into memory                                   No

       Remote access allowed                                                           Yes

   RemoveRemove LooseLoose EndsEnds

      Removes the loose ends of a wire.

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

   RemoveRemove ProbeProbe

      Removes any probe attached to the wire.


9238   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9238 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9239 ordinal=9239 -->
## Property and Method Reference

Property and Method Reference

Parameters

 Name            Data type             Required              Description

 VIClone                           No

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                              No

 Available in Real-Time Operating System                      No

 Settable when the VI is running                                      Yes

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

WireWire PropertiesProperties


 Property        Description

 Breakpoint
               Reads or writes the status of a breakpoint on a wire.
 Status

 Description      Sets or returns a description of the wire.

 Is Broken?      Returns TRUE if the wire is broken or in a bad state.

                Returns an array of all joints of the wire, which includes intersections, bends, and
 Joints[]
              end points.

 Label           Returns a reference to the label associated with this wire.

 Probe          References the probe associated with this wire.

 Terminals[]      References the terminals connected by this wire.


                                                    © National Instruments 9239

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9239 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9240 ordinal=9240 -->
## Property and Method Reference

Property and Method Reference


        Property        Description

        Wire Width      Returns the width of the wire in pixels.

   BreakpointBreakpoint StatusStatus

      Reads or writes the status of a breakpoint on a wire.

       Select from Cleared Break, Enabled Break, and Disabled Break.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                          Yes

        Loads the block diagram into memory                                    Yes

       Remote access allowed                                                  Yes

    DescriptionDescription

       Sets or returns a description of the wire.

     Remarks

      The following table lists the characteristics of this property.


9240   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9240 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9241 ordinal=9241 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

IsIs Broken?Broken?

Returns TRUE if the wire is broken or in a bad state.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes


                                                    © National Instruments 9241

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9241 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9242 ordinal=9242 -->
## Property and Method Reference

Property and Method Reference

    Joints[]Joints[]

       Returns an array of all joints of the wire, which includes intersections, bends, and end
       points.

      The output of this property is an array of clusters, and each cluster represents one joint
       of the wire. The following table lists descriptions for the output of each cluster.

     Elements

      Name    Description

         Position  Identifies the X,Y position of the joint on the block diagram.

                    Indicates whether the joint has a loose end, an endpoint, a bend in the wire, a fork of the        Type                    wire, or a connection to a terminal.

      Up
         Joint     Identifies the next index of the array above the joint.
        Index

      Down
         Joint     Identifies the next index of the array below the joint.
        Index

          Left
         Joint     Identifies the next index of the array to the left of the joint.
        Index

         Right
         Joint     Identifies the next index of the array to the right of the joint.
        Index

                    Indicates the action of the joint:

                              • 0x1—The joint connects to one of the terminals of the signal.
                              • 0x2—The joint optimizes the redrawing of signals. Do not modify.
                              • 0x4—The joint optimizes the redrawing of signals. Do not modify.
         Flags          • 0x8—The joint is currently selected on the block diagram. Any edge LabVIEW selects
                       to be connected to the joint is set.
                              • 0x10—LabVIEW selects the right edge of the joint.
                              • 0x20—LabVIEW selects the lower edge of the joint.
                              • 0x40—LabVIEW uses the joint to optimize routing. Do not modify.


9242   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9242 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9243 ordinal=9243 -->
## Property and Method Reference

Property and Method Reference


 Name    Description

                  • 0x8—LabVIEW uses the joint to optimize routing. Do not modify.
                  • 0x100—The joint is loose and it is not between two joints that are connected to
                terminals. Do not modify.
                  • 0x200—The joint is on the path. LabVIEW uses this joint during path and split
               algorithms. Do not modify.
                  • 0x400—LabVIEW does not use the joint.
                  • 0x800—LabVIEW does not use the joint.
                  • 0x1000—LabVIEW shifted the joint horizontally during the most recent edit
               operation. The joint clears when the wire table rebuilds at the end of every edit
               operation.
                  • 0x2000—LabVIEW shifted the joint vertically during the most recent edit operation.


Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

LabelLabel

Returns a reference to the label associated with this wire.


                                                    © National Instruments 9243

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9243 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9244 ordinal=9244 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

   ProbeProbe

       References the probe associated with this wire.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No


9244   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9244 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9245 ordinal=9245 -->
## Property and Method Reference

Property and Method Reference


 Remote access allowed                                                   Yes

Terminals[]Terminals[]

References the terminals connected by this wire.

The first reference is the source if a source exists. The other references on the list are in
no particular order. If there is more than one source on the list, the wire is broken and
the extra sources are not necessarily at the start of the list.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

WireWire WidthWidth

Returns the width of the wire in pixels.

The width measures only the colored portion of the wire and does not include the
extra pixel of white border that appears on each side when the wire crosses another
wire.


                                                    © National Instruments 9245

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9245 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9246 ordinal=9246 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                                   Yes

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

   PropertyItemPropertyItem

       PropertyItem Methods

       PropertyItem Properties
   PropertyItemPropertyItem MethodsMethods


       Method              Description

         Set Property          Sets the selected property of the PropertyItem.

    SetSet PropertyProperty

       Sets the selected property of the PropertyItem.


9246   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9246 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9247 ordinal=9247 -->
## Property and Method Reference

Property and Method Reference

Parameters

          Data Name          Required  Description
          type

                             Specifies the Unique ID string of the property you want to set. Use the
                                   All Supported Properties property to determine the Unique ID string of
                          the property you want to set. Set Allow Alternative Names? to TRUE if ID String        Yes
                        you want to match the ID String to any of the following values of the
                            property: Unique ID string, Data name, Short name (localized), or
                       Long name (localized).


                             Specifies whether you can set the property or method using the
 Allow                       Unique ID string, Data name, Short name (localized), or Long name Alternate             No        (localized) of the property or method. The default is FALSE, which
 Names?                      means you must specify the Unique ID string of the property or (F)                      method in ID String.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                             Yes

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

PropertyItemPropertyItem PropertiesProperties


                                                    © National Instruments 9247

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9247 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9248 ordinal=9248 -->
## Property and Method Reference

Property and Method Reference


        Property    Description

           Is Write      Sets or returns whether a property is a write or read property item.

         Property    Gets information about the property selected on this PropertyItem.

        Terminal     Sets or returns a reference to the terminal.

     IsIs WriteWrite

       Sets or returns whether a property is a write or read property item.

           If TRUE, the property is a write item. If FALSE, the property is a read item.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                 No

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    PropertyProperty

       Gets information about the property selected on this PropertyItem.

     Some properties have a Unique ID string. The Unique ID string is consistent across all
       versions and locales of LabVIEW. Properties without a Unique ID string return an

9248   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9248 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9249 ordinal=9249 -->
## Property and Method Reference

Property and Method Reference

empty string. If this property item has an invalid property selected, this property
returns empty strings for Unique ID string, Data name, Short name, and Long name.
This property is read only. Use the Set Property method to change the currently
selected property.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                                         Yes

 Need to authenticate before use                                 No

 Loads the block diagram into memory                                      Yes

 Remote access allowed                                                   Yes

TerminalTerminal

Sets or returns a reference to the terminal.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


                                                    © National Instruments 9249

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9249 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9250 ordinal=9250 -->
## Property and Method Reference

Property and Method Reference


         Settable when the VI is running                                 No

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   FlatSequenceFlatSequence

      FlatSequence Methods

      FlatSequence Properties
   FlatSequenceFlatSequence MethodsMethods


       Method     Description

                  Adds a new frame before or after the frame whose index you specify and returns a
       Add Frame                      reference to the new frame.

        Auto Size    Automatically resizes the Flat Sequence structure to fit contents.

        Convert To                     Converts the Flat Sequence structure to a Timed Sequence structure and returns a       Timed
                      reference to the new structure.        Sequence

       Remove
                  Removes the Flat Sequence structure from the diagram. The contents of the structure
          Flat
                  merge with the rest of the contents of the diagram.
        Sequence

                  Removes the frame you specify. LabVIEW also removes the contents of the frame. You
       Remove
                    cannot use this method to remove the only frame of a sequence structure. Use the
       Frame
                     Delete method instead.

   AddAdd FrameFrame

      Adds a new frame before or after the frame whose index you specify and returns a
       reference to the new frame.

9250   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9250 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9251 ordinal=9251 -->
## Property and Method Reference

Property and Method Reference

Parameters

           Data Name           Required  Description
            type

 Reference                               Specifies the index of the frame beside which you want to add the Frame         No                      new frame. Index


                                              If TRUE (default), LabVIEW adds the frame after Reference Frame
 After? (T)       No        Index. If FALSE, LabVIEW adds the frame before Reference Frame
                             Index.


Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                                      Yes

 Available in Real-Time Operating System                                            Yes

 Settable when the VI is running                                        No

 Loads the front panel into memory                                     No

 Need to authenticate before use                                       No

 Loads the block diagram into memory                                   No

 Remote access allowed                                                           Yes

AutoAuto SizeSize

Automatically resizes the Flat Sequence structure to fit contents.

Remarks

The following table lists the characteristics of this method.

                                                    © National Instruments 9251

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9251 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9252 ordinal=9252 -->
## Property and Method Reference

Property and Method Reference


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

   ConvertConvert ToTo TimedTimed SequenceSequence

       Converts the Flat Sequence structure to a Timed Sequence structure and returns a
       reference to the new structure.

       This method automatically closes the reference to the original Flat Sequence
        structure.

     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                                      Yes

         Available in Real-Time Operating System                                            Yes

         Settable when the VI is running                                        No

        Loads the front panel into memory                                     No

       Need to authenticate before use                                       No

        Loads the block diagram into memory                                   No

       Remote access allowed                                                           Yes


9252   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9252 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9253 ordinal=9253 -->
## Property and Method Reference

Property and Method Reference

RemoveRemove FlatFlat SequenceSequence

Removes the Flat Sequence structure from the diagram. The contents of the structure
merge with the rest of the contents of the diagram.

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                             Yes

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

RemoveRemove FrameFrame

Removes the frame you specify. LabVIEW also removes the contents of the frame. You
cannot use this method to remove the only frame of a sequence structure. Use the
Delete method instead.

Parameters

                     Data
 Name                         Required  Description
                      type

 Reference Frame                              Specifies the index of the frame you want to
                                  Yes
 Index                                   remove.


                                                    © National Instruments 9253

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9253 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9254 ordinal=9254 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

   FlatSequenceFlatSequence PropertiesProperties


        Property             Description

         AutoSize To Fit        Sets or returns whether the Flat Sequence structure automatically resizes to
        Contents?                  fit its contents.

        Breakpoint Status     Sets or returns the status of a breakpoint on a Flat Sequence structure.

         Description           Sets or returns the description string for the Flat Sequence structure.

         Frames[]             Returns an array of references to the frames of the Flat Sequence structure.

         Label                References the label of the Flat Sequence structure.

        Subdiagram Label
                              Sets the visibility of the subdiagram label.
          Visible

                             Returns an array of references to the terminals of the Flat Sequence
         Terminals[]
                                 structure.

    AutoSizeAutoSize ToTo FitFit Contents?Contents?

       Sets or returns whether the Flat Sequence structure automatically resizes to fit its

9254   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9254 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9255 ordinal=9255 -->
## Property and Method Reference

Property and Method Reference

contents.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                 No

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

BreakpointBreakpoint StatusStatus

Sets or returns the status of a breakpoint on a Flat Sequence structure.

Valid values include Cleared Break, Enabled Break, and Disabled Break.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes


                                                    © National Instruments 9255

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9255 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9256 ordinal=9256 -->
## Property and Method Reference

Property and Method Reference


        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                          Yes

        Loads the block diagram into memory                                    Yes

       Remote access allowed                                                  Yes

    DescriptionDescription

       Sets or returns the description string for the Flat Sequence structure.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    Frames[]Frames[]

       Returns an array of references to the frames of the Flat Sequence structure.

     Remarks

      The following table lists the characteristics of this property.


9256   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9256 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9257 ordinal=9257 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

LabelLabel

References the label of the Flat Sequence structure.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes


                                                    © National Instruments 9257

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9257 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9258 ordinal=9258 -->
## Property and Method Reference

Property and Method Reference

   SubdiagramSubdiagram LabelLabel VisibleVisible

       Sets the visibility of the subdiagram label.

       This property is similar to the Visible Items»Subdiagram Label item on the shortcut
     menu of a structure. This property is also similar to the Subdiagram label visible
       option on the Appearance page of the Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                 No

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    Terminals[]Terminals[]

       Returns an array of references to the terminals of the Flat Sequence structure.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

9258   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9258 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9259 ordinal=9259 -->
## Property and Method Reference

Property and Method Reference


 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

TimeFlatSequenceTimeFlatSequence
SimulationDCOSimulationDCO
FlatSequenceInnerTunnelFlatSequenceInnerTunnel

FlatSequenceInnerTunnel Properties
FlatSequenceInnerTunnelFlatSequenceInnerTunnel PropertiesProperties


 Property      Description

 Left Frame    Returns a reference to the left frame of an inner tunnel on a Flat Sequence structure.

               Returns a reference to the left terminal of an inner tunnel on a Flat Sequence
 Left Terminal
                 structure.

               Returns a reference to the right frame of an inner tunnel on a Flat Sequence
 Right Frame
                 structure.

 Right         Returns a reference to the right terminal of an inner tunnel on a Flat Sequence
 Terminal       structure.


                                                    © National Instruments 9259

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9259 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9260 ordinal=9260 -->
## Property and Method Reference

Property and Method Reference

    LeftLeft FrameFrame

       Returns a reference to the left frame of an inner tunnel on a Flat Sequence structure.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                                   Yes

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

    LeftLeft TerminalTerminal

       Returns a reference to the left terminal of an inner tunnel on a Flat Sequence structure.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                                   Yes

         Settable when the VI is running                                  No

9260   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9260 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9261 ordinal=9261 -->
## Property and Method Reference

Property and Method Reference


 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

RightRight FrameFrame

Returns a reference to the right frame of an inner tunnel on a Flat Sequence structure.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

RightRight TerminalTerminal

Returns a reference to the right terminal of an inner tunnel on a Flat Sequence
structure.

Remarks

The following table lists the characteristics of this property.

                                                    © National Instruments 9261

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9261 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9262 ordinal=9262 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                                   Yes

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

   FlatSequenceOuterTunnelFlatSequenceOuterTunnel

      FlatSequenceOuterTunnel Properties
   FlatSequenceOuterTunnelFlatSequenceOuterTunnel PropertiesProperties


        Property      Description

                       Returns a reference to a Flat Sequence structure frame that contains an outer       Frame                         tunnel.

         Inner         Returns a reference to the inner terminal of an outer tunnel on a Flat Sequence
        Terminal       structure.

        Outer         Returns a reference to the outer terminal of an outer tunnel on a Flat Sequence
        Terminal       structure.

   FrameFrame

       Returns a reference to a Flat Sequence structure frame that contains an outer tunnel.


9262   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9262 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9263 ordinal=9263 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

InnerInner TerminalTerminal

Returns a reference to the inner terminal of an outer tunnel on a Flat Sequence
structure.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No


                                                    © National Instruments 9263

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9263 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9264 ordinal=9264 -->
## Property and Method Reference

Property and Method Reference


        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

   OuterOuter TerminalTerminal

       Returns a reference to the outer terminal of an outer tunnel on a Flat Sequence
        structure.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                                   Yes

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

    PolymorphicVISelectorPolymorphicVISelector

       PolymorphicVISelector Properties
    PolymorphicVISelectorPolymorphicVISelector PropertiesProperties


        Property         Description

         Instance Text     Returns the text displayed in the selector of a polymorphic VI.

9264   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9264 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9265 ordinal=9265 -->
## Property and Method Reference

Property and Method Reference

InstanceInstance TextText

Returns the text displayed in the selector of a polymorphic VI.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                                         Yes

 Need to authenticate before use                                 No

 Loads the block diagram into memory                                      Yes

 Remote access allowed                                                   Yes

SynchronousDataFlowDCOSynchronousDataFlowDCO
TimedStructDCOTimedStructDCO

PlotPlot

Plot Properties
PlotPlot PropertiesProperties


                                                    © National Instruments 9265

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9265 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9266 ordinal=9266 -->
## Property and Method Reference

Property and Method Reference


        Property     Description

         Anti-aliased   Enables anti-aliasing for the referenced plot.

        Bar Plot                      Gets or sets the bar plot style.         Style

                       Sets whether LabVIEW uses a thin or thick line in the plot to distinguish high or low
          Digital Line   values or to offset a particular plot line. Applies to digital plots only. Valid values
         Style         include 0 (do not distinguish high or low values), 1 (distinguish low values), 2
                         (distinguish high values), 3 (thicken entire line).

          Digital        Sets whether to display high to low transitions at the previous point, in between
         Transition     points, or at the new point on the x-axis. The default displays high to low transitions
         Location      at the new point on the x-axis. Applies to digital plots only.

          Digital                       Sets how LabVIEW distinguishes differing values in the plot. This affects only plots
         Transition                      with more than one bit. Applies to digital plots only.        Type

                                Fill baseline: -1 None, -2 Zero, -3 Negative Infinity, -4 Infinity. Otherwise, the number             Fill To                        of the plot being filled.

          Fill/Point                      Color of the point and fills.         Color

         Label                      Gets or sets the format of the text label on a digital plot.        Format

         Line Style     Line style (0-4) as shown on the shortcut menu from top-left to bottom-right.

         Line Width    Width of the plot (0-5).

         Plot Color     Color of the plot.

         Plot           Interpolation of plot: 0-None, 1-Stepwise, 2-Linear, 3-Stepwise horizontal,
         Interpolation  4-Stepwise horizontally centered, 5-Stepwise vertically centered.

                Name of the plot. If the Ignore Attributes property is FALSE, you cannot set the plot
         Plot Name
                   name.

         Point Style    Point Style (0-16) as shown on the shortcut menu from top-left to bottom-right.

          Visible      Shows the plot.

        X Scale Index The index of X-scale with which this plot is associated.

        Y Scale Index The index of Y-scale with which this plot is associated.


9266   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9266 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9267 ordinal=9267 -->
## Property and Method Reference

Property and Method Reference

Anti-aliasedAnti-aliased

Enables anti-aliasing for the referenced plot.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

BarBar PlotPlot StyleStyle

Gets or sets the bar plot style.

This property is similar to the Bar Plots item on the shortcut menu of a plot.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes


                                                    © National Instruments 9267

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9267 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9268 ordinal=9268 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    DigitalDigital LineLine StyleStyle

       Sets whether LabVIEW uses a thin or thick line in the plot to distinguish high or low
       values or to offset a particular plot line. Applies to digital plots only. Valid values
       include 0 (do not distinguish high or low values), 1 (distinguish low values), 2
        (distinguish high values), 3 (thicken entire line).

       This property is similar to the Line Style item on the shortcut menu of a digital
      waveform graph plot legend.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes


9268   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9268 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9269 ordinal=9269 -->
## Property and Method Reference

Property and Method Reference

DigitalDigital TransitionTransition LocationLocation

Sets whether to display high to low transitions at the previous point, in between
points, or at the new point on the x-axis. The default displays high to low transitions at
the new point on the x-axis. Applies to digital plots only.

This property is similar to the Transition Location item on the shortcut menu of a plot.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

DigitalDigital TransitionTransition TypeType

Sets how LabVIEW distinguishes differing values in the plot. This affects only plots with
more than one bit. Applies to digital plots only.

This property is similar to the Transition Type item on the shortcut menu of a plot.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 9269

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9269 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9270 ordinal=9270 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

     FillFill ToTo

          Fill baseline: -1 None, -2 Zero, -3 Negative Infinity, -4 Infinity. Otherwise, the number of
       the plot being filled.

       This property is similar to the Fill Base Line item on the shortcut menu of a plot and
       the Fill to option on the Plots page of the Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No


9270   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9270 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9271 ordinal=9271 -->
## Property and Method Reference

Property and Method Reference


 Remote access allowed                                                  Yes

Fill/PointFill/Point ColorColor

Color of the point and fills.

You can set the color of the front panel object by wiring a hexadecimal number with
the form RRGGBB or by wiring the color box constant to the property.

This property is similar to the Point/fill color option on the Plots page of the
Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

LabelLabel FormatFormat

Gets or sets the format of the text label on a digital plot.

This property is similar to the Label Format item on the shortcut menu of the plot
legend of a mixed signal or digital waveform graph.

                                                    © National Instruments 9271

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9271 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9272 ordinal=9272 -->
## Property and Method Reference

Property and Method Reference

       This property is similar to the Format option on the Plots page of the Digital Graph
       Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    LineLine StyleStyle

       Line style (0-4) as shown on the shortcut menu from top-left to bottom-right.

       This property is similar to the Line Style item on the shortcut menu of a plot and the
       Line Style option on the Plots page of the Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

9272   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9272 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9273 ordinal=9273 -->
## Property and Method Reference

Property and Method Reference


 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

LineLine WidthWidth

Width of the plot (0-5).

This property is similar to the Line Width item on the shortcut menu of a plot and the
Line Width option on the Plots page of the Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

PlotPlot ColorColor

Color of the plot.


                                                    © National Instruments 9273

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9273 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9274 ordinal=9274 -->
## Property and Method Reference

Property and Method Reference

      You can set the color of the front panel object by wiring a hexadecimal number with
       the form RRGGBB or by wiring the color box constant to the property.

       This property is similar to the Color item on the shortcut menu of a plot and the Line
       color option on the Plots page of the Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    PlotPlot InterpolationInterpolation

       Interpolation of plot: 0-None, 1-Stepwise, 2-Linear, 3-Stepwise horizontal, 4-Stepwise
       horizontally centered, 5-Stepwise vertically centered.

       This property is similar to the Interpolation item on the shortcut menu of a plot and
       the Plot Interpolation option on the Plots page of the Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type


9274   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9274 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9275 ordinal=9275 -->
## Property and Method Reference

Property and Method Reference


 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

PlotPlot NameName

Name of the plot. If the Ignore Attributes property is FALSE, you cannot set the plot
name.

This property is similar to the Name option on the Plots page of the Properties dialog
box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes


                                                    © National Instruments 9275

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9275 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9276 ordinal=9276 -->
## Property and Method Reference

Property and Method Reference

    PointPoint StyleStyle

       Point Style (0-16) as shown on the shortcut menu from top-left to bottom-right.

       This property is similar to the Point Style item on the shortcut menu of a plot and
       Point Style option on the Plots page of the Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    VisibleVisible

      Shows the plot.

       This property is similar to the Plot Visible option in the shortcut menu of a glyph in the
       plot legend of a graph or chart.

     Remarks

      The following table lists the characteristics of this property.


9276   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9276 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9277 ordinal=9277 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

XX ScaleScale IndexIndex

The index of X-scale with which this plot is associated.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes


                                                    © National Instruments 9277

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9277 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9278 ordinal=9278 -->
## Property and Method Reference

Property and Method Reference

   YY ScaleScale IndexIndex

      The index of Y-scale with which this plot is associated.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

      CursorCursor

       Cursor Properties
   CursorCursor PropertiesProperties


        Property       Description

        Allow Drag          If TRUE, allows you to drag the cursor.

         Cursor Color    The color of the cursor, including its point, arrow, and name.

                         Array index of point to which the cursor is snapped. This property can have a value
         Cursor Index
                     between 0 and the number of data points minus 1.

                           Specifies the way in which the cursor snaps to the plots in the plot area. Valid
         Cursor Mode
                         values include 0 (Free), 1 (Single-plot), and 2 (Multi-plot).

9278   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9278 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9279 ordinal=9279 -->
## Property and Method Reference

Property and Method Reference


Property       Description

Cursor Name    Text displayed in the plot area that is associated with the cursor.

Cursor Name                          If TRUE, displays the cursor name in the plot area.Visible

                 Plot with which the cursor is associated. If Plot is –1, the cursor snaps to all plots in
Cursor Plot     the plot area. You can move the cursor to the nearest data point along any plot in
               the plot area.

              The symbol that, in combination with Style, is drawn at the focal point of theCursor Point                  cursor. Valid values are 0-16, as shown on the shortcut menu of the plot legendStyle
              from top-left to bottom-right.

Cursor Position  Position of cursor in terms of X-Y coordinates.

Cursor              The X coordinate of the cursor in the plot area. Position:X is in the coordinate
Position:Cursor               system of the X Scale value that is associated with the cursor or plot.X

Cursor              The Y coordinate of the cursor in the plot area. Position:Y is in the coordinatePosition:Cursor               system of the Y Scale value that is associated with the cursor or plot.
Y

Cursor
                Color of the cursor row selected in the cursor legend.Selection Color

              The symbol that, in combination with Point Style, is drawn at the focal point of the
                  cursor. Valid values are 0-8, from top-left to bottom-right, as shown when youCursor Style                   right-click a cursor in the cursor legend and select Attributes»Cursor Style from
               the shortcut menu.

                 Specifies the line style of the active cursor. Valid values are 0–4, as shown on the
Line Style       shortcut menu of the plot legend and on the Cursors page of the Properties dialog
              box ordered from top to bottom.

                 Specifies the width of the line used to display the active cursor. Valid values are
Line Width      0–4, as shown on the shortcut menu of the plot legend and on the Cursors page of
               the Properties dialog box ordered from top to bottom.

              The plot area with which the cursor is associated. This property applies only to
Plot Area
               Mixed Signal graphs.

Visible        Shows the cursor.

                          If TRUE, the cursor watches all plots in the plot area. If FALSE, the cursor watches
Watch All Plots  only the plots specified by the Watch Plots property. This property is valid only for
                cursors that are associated with multiple plots.


                                                    © National Instruments 9279

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9279 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9280 ordinal=9280 -->
## Property and Method Reference

Property and Method Reference


        Property       Description

                         Array that contains the indexes of the plots that the cursor is watching when the
        Watch Plots    Watch All Plots property is set to FALSE. This property is valid only for cursors that
                         are associated with multiple plots.

                         Sets the x-scale of the cursor. This property is valid only for free cursors. When the        X Scale
                         cursor is associated with a plot, this property might be overwritten by the plot.

                         Sets the y-scale of the cursor. This property is valid only for free cursors. When the        Y Scale                         cursor is associated with a plot, this property might be overwritten by the plot.

   AllowAllow DragDrag

           If TRUE, allows you to drag the cursor.

       This property is similar to the Attributes»Allow Drag item on the shortcut menu on the
       cursor legend of a graph and the Allow Dragging option on the Cursors page of the
       Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes


9280   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9280 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9281 ordinal=9281 -->
## Property and Method Reference

Property and Method Reference

CursorCursor ColorColor

The color of the cursor, including its point, arrow, and name.

You can set the color of the front panel object by wiring a hexadecimal number with
the form RRGGBB or by wiring the color box constant to the property.

This property is similar to the Color item on the shortcut menu of the cursor legend of
a graph and the Cursor color option on the Cursors page of the Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

CursorCursor IndexIndex

Array index of point to which the cursor is snapped. This property can have a value
between 0 and the number of data points minus 1.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 9281

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9281 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9282 ordinal=9282 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   CursorCursor ModeMode

       Specifies the way in which the cursor snaps to the plots in the plot area. Valid values
       include 0 (Free), 1 (Single-plot), and 2 (Multi-plot).

       This property is similar to the Create Cursor items in the shortcut menu of the cursor
      legend of a graph.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No


9282   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9282 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9283 ordinal=9283 -->
## Property and Method Reference

Property and Method Reference


 Remote access allowed                                                  Yes

CursorCursor NameName

Text displayed in the plot area that is associated with the cursor.

This property is similar to the name text box in the cursor legend of a graph and the
Name option on the Cursors page of the Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

CursorCursor NameName VisibleVisible

If TRUE, displays the cursor name in the plot area.

This property is similar to the Show Name item of the shortcut menu of the cursor
legend of a graph and the Show name option on the Cursors page of the Properties
dialog box.


                                                    © National Instruments 9283

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9283 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9284 ordinal=9284 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   CursorCursor PlotPlot

       Plot with which the cursor is associated. If Plot is –1, the cursor snaps to all plots in the
       plot area. You can move the cursor to the nearest data point along any plot in the plot
       area.

       This property is similar to the cursor plot items of the shortcut menu of the cursor
      legend of a graph and the Cursor plot option on the Cursors page of the Properties
       dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

9284   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9284 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9285 ordinal=9285 -->
## Property and Method Reference

Property and Method Reference


 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

CursorCursor PointPoint StyleStyle

The symbol that, in combination with Style, is drawn at the focal point of the cursor.
Valid values are 0-16, as shown on the shortcut menu of the plot legend from top-left
to bottom-right.

This property is similar to the Point Style item of the shortcut menu of the cursor
legend of a graph and the Point Style option on the Cursors page of the Properties
dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes


                                                    © National Instruments 9285

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9285 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9286 ordinal=9286 -->
## Property and Method Reference

Property and Method Reference

   CursorCursor PositionPosition

       Position of cursor in terms of X-Y coordinates.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   CursorCursor Position:CursorPosition:Cursor XX

      The X coordinate of the cursor in the plot area. Position:X is in the coordinate system of
       the X Scale value that is associated with the cursor or plot.

       This property is an element of the Cursor Position property.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write


9286   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9286 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9287 ordinal=9287 -->
## Property and Method Reference

Property and Method Reference


 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

CursorCursor Position:CursorPosition:Cursor YY

The Y coordinate of the cursor in the plot area. Position:Y is in the coordinate system of
the Y Scale value that is associated with the cursor or plot.

This property is an element of the Cursor Position property.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes


                                                    © National Instruments 9287

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9287 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9288 ordinal=9288 -->
## Property and Method Reference

Property and Method Reference

   CursorCursor SelectionSelection ColorColor

       Color of the cursor row selected in the cursor legend.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   CursorCursor StyleStyle

      The symbol that, in combination with Point Style, is drawn at the focal point of the
        cursor. Valid values are 0-8, from top-left to bottom-right, as shown when you right-
        click a cursor in the cursor legend and select Attributes»Cursor Style from the shortcut
      menu.

       This property is similar to the Cursor Style item of the shortcut menu of the cursor
      legend of a graph and the Cursor Style option on the Cursors page of the Properties
       dialog box.

     Remarks

      The following table lists the characteristics of this property.


9288   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9288 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9289 ordinal=9289 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

LineLine StyleStyle

Specifies the line style of the active cursor. Valid values are 0–4, as shown on the
shortcut menu of the plot legend and on the Cursors page of the Properties dialog box
ordered from top to bottom.

This property is similar to the Line Style item of the shortcut menu of the cursor legend
of a graph and the Line style option on the Cursors page of the Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No


                                                    © National Instruments 9289

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9289 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9290 ordinal=9290 -->
## Property and Method Reference

Property and Method Reference


        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    LineLine WidthWidth

       Specifies the width of the line used to display the active cursor. Valid values are 0–4, as
      shown on the shortcut menu of the plot legend and on the Cursors page of the
       Properties dialog box ordered from top to bottom.

       Assigning a value of 0 results in a line width of exactly one pixel. Assigning values 1–4
        will result in a line width of increasing thickness based upon the resolution of the
       monitor.

       This property is similar to the Line Width item of the shortcut menu of the cursor
      legend of a graph and the Line width option on the Cursors page of the Properties
       dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes


9290   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9290 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9291 ordinal=9291 -->
## Property and Method Reference

Property and Method Reference

PlotPlot AreaArea

The plot area with which the cursor is associated. This property applies only to Mixed
Signal graphs.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

VisibleVisible

Shows the cursor.

This property is similar to the Show cursor option on the Cursors page of the
Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

                                                    © National Instruments 9291

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9291 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9292 ordinal=9292 -->
## Property and Method Reference

Property and Method Reference


         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   WatchWatch AllAll PlotsPlots

           If TRUE, the cursor watches all plots in the plot area. If FALSE, the cursor watches only
       the plots specified by the Watch Plots property. This property is valid only for cursors
       that are associated with multiple plots.

       This property is similar to the Watch»All Plots item on the shortcut menu of the cursor
      legend of a mixed signal graph.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes


9292   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9292 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9293 ordinal=9293 -->
## Property and Method Reference

Property and Method Reference

WatchWatch PlotsPlots

Array that contains the indexes of the plots that the cursor is watching when the Watch
All Plots property is set to FALSE. This property is valid only for cursors that are
associated with multiple plots.

This property is similar to the Watch items on the shortcut menu of the cursor legend
of a mixed signal graph.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

XX ScaleScale

Sets the x-scale of the cursor. This property is valid only for free cursors. When the
cursor is associated with a plot, this property might be overwritten by the plot.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 9293

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9293 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9294 ordinal=9294 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   YY ScaleScale

       Sets the y-scale of the cursor. This property is valid only for free cursors. When the
       cursor is associated with a plot, this property might be overwritten by the plot.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

      PagePage

9294   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9294 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9295 ordinal=9295 -->
## Property and Method Reference

Property and Method Reference

Page Methods

Page Properties
PagePage MethodsMethods


 Method             Description

 Import Image       Imports the image from the clipboard to the page.

 Rearrange Tabbing   Reorders the controls on the page according to the order of the input array of
 Order               control references.

 Remove Image     Removes the image from the page.

ImportImport ImageImage

Imports the image from the clipboard to the page.

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                             Yes

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes


                                                    © National Instruments 9295

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9295 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9296 ordinal=9296 -->
## Property and Method Reference

Property and Method Reference

   RearrangeRearrange TabbingTabbing OrderOrder

       Reorders the controls on the page according to the order of the input array of control
       references.

     Parameters

      Name             Data type  Required  Description

         Control References              Yes          List of control references that you want to reorder.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                                      Yes

        Loads the front panel into memory                                  Yes

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

   RemoveRemove ImageImage

      Removes the image from the page.

     Remarks

      The following table lists the characteristics of this method.


9296   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9296 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9297 ordinal=9297 -->
## Property and Method Reference

Property and Method Reference


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                             Yes

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

PagePage PropertiesProperties


 Property            Description

 Colors              Gets or sets the foreground and background colors of a tab control page.

 Colors:BG Color     Gets or sets the background color of the tab control page.

 Colors:FG Color     Gets or sets the foreground color of the tab control page.

 Description         Gets or sets the description of a tab control page.

 Independent Label  Makes the tab control page caption independent of the page label.

 Page Enabled State  Gets or sets the state of a tab control page.

 Page Label          Gets the label of a tab control page.

 Page Visible       Shows or hides individual pages of a tab control.

 Tab Caption         Gets or sets the text of a caption on a tab control page.

                    Returns an array of references to the controls and indicators on a page. The
                    order in which you place the objects on the page determines the index of the
 Tabbing Order       object in the array. For example, if the first object you place on the page is a
                   numeric control, the index of the numeric control in the array returned by this
                    property is 0.

                    Gets or sets the tip strip of a tab control page. A tip strip is the brief
 Tip Strip
                      description of the object that appears when you move the cursor over the


                                                    © National Instruments 9297

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9297 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9298 ordinal=9298 -->
## Property and Method Reference

Property and Method Reference


        Property            Description

                               object.

                           Other products refer to tip strips as tooltips.

         Z-Order:All          Gets an array of references to all controls, indicators, and decorations on a
         Objects[]           page.

          Z-
                            Gets an array of references to all decorations on a tab control page.         Order:Decorations[]

    ColorsColors

       Gets or sets the foreground and background colors of a tab control page.

      You can set the color of the front panel object by wiring a hexadecimal number with
       the form RRGGBB or by wiring the color box constant to the property.

      To set the colors, you must set the Allow Multiple Colors property to TRUE or right-click
       the tabs of the tab control and select Advanced»Allow Multiple Colors from the
       shortcut menu.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

9298   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9298 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9299 ordinal=9299 -->
## Property and Method Reference

Property and Method Reference


 Remote access allowed                                                  Yes

Colors:BGColors:BG ColorColor

Gets or sets the background color of the tab control page.

You can set the color of the front panel object by wiring a hexadecimal number with
the form RRGGBB or by wiring the color box constant to the property.

This property is an element of the Colors property.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Colors:FGColors:FG ColorColor

Gets or sets the foreground color of the tab control page.

You can set the color of the front panel object by wiring a hexadecimal number with
the form RRGGBB or by wiring the color box constant to the property.


                                                    © National Instruments 9299

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9299 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9300 ordinal=9300 -->
## Property and Method Reference

Property and Method Reference

       This property is an element of the Colors property.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    DescriptionDescription

       Gets or sets the description of a tab control page.

       This property is similar to the Description and Tip item on the shortcut menu of a page
      on a tab control.

           If you set the description, it appears in the Context Help window for that page and in
      any custom documentation you generate for the VI. You can format the text in the
       description to appear bold in the Context Help window.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

9300   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9300 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9301 ordinal=9301 -->
## Property and Method Reference

Property and Method Reference


 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

IndependentIndependent LabelLabel

Makes the tab control page caption independent of the page label.

After you set this property to TRUE, you can use the Tab Caption property to change
the page caption.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes


                                                    © National Instruments 9301

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9301 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9302 ordinal=9302 -->
## Property and Method Reference

Property and Method Reference

   PagePage EnabledEnabled StateState

       Gets or sets the state of a tab control page.

       This property is similar to the Advanced»Page Enabled State item on the shortcut
     menu of a tab control.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   PagePage LabelLabel

       Gets the label of a tab control page.

      Page labels correspond to the values of the enumerated type control on the block
       diagram.

     Remarks

      The following table lists the characteristics of this property.


9302   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9302 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9303 ordinal=9303 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                     Read/Write

 Available in Run-Time Engine                                        Yes (Read Only)

 Available in Real-Time Operating System                             Yes

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

PagePage VisibleVisible

Shows or hides individual pages of a tab control.

If you hide the default page, the next page becomes the default page. If the only visible
page is the default page, you cannot hide the default page.

This property is similar to the Hide Page and Show Hidden Pages items on the shortcut
menu of a tab control.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

                                                    © National Instruments 9303

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9303 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9304 ordinal=9304 -->
## Property and Method Reference

Property and Method Reference


        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   TabTab CaptionCaption

       Gets or sets the text of a caption on a tab control page.

      To set the caption, you must set the Independent Label property to TRUE or right-click
       the tabs of the tab control and remove the checkmark next to Advanced»Make Page
      Caption Match Label on the shortcut menu.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   TabbingTabbing OrderOrder

       Returns an array of references to the controls and indicators on a page. The order in
      which you place the objects on the page determines the index of the object in the
        array. For example, if the first object you place on the page is a numeric control, the
       index of the numeric control in the array returned by this property is 0.


9304   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9304 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9305 ordinal=9305 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                               Read Only

 Available in Run-Time Engine                                        Yes (Read Only)

 Available in Real-Time Operating System                             Yes

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

TipTip StripStrip

Gets or sets the tip strip of a tab control page. A tip strip is the brief description of the
object that appears when you move the cursor over the object.

Other products refer to tip strips as tooltips.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No


                                                    © National Instruments 9305

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9305 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9306 ordinal=9306 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    Z-Order:AllZ-Order:All Objects[]Objects[]

       Gets an array of references to all controls, indicators, and decorations on a page.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                               Read Only

         Available in Run-Time Engine                                        Yes (Read Only)

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

    Z-Order:Decorations[]Z-Order:Decorations[]

       Gets an array of references to all decorations on a tab control page.

     Remarks

      The following table lists the characteristics of this property.


        Data type

9306   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9306 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9307 ordinal=9307 -->
## Property and Method Reference

Property and Method Reference


 Permissions                                               Read Only

 Available in Run-Time Engine                                        Yes (Read Only)

 Available in Real-Time Operating System                             Yes

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

ConnectorPaneConnectorPane

ConnectorPane Methods

ConnectorPane Properties
ConnectorPaneConnectorPane MethodsMethods


 Method                   Description

 Assign Control To Terminal  Assigns a front panel control to a connector pane terminal of the VI.

 Disconnect All Terminals    Disconnects all connector pane terminals from controls and indicators.

 Disconnect Terminal       Disconnects a connector pane terminal from a control or an indicator.

 Flip Horizontal               Flips the connector pane horizontally.

 Flip Vertical                  Flips the connector pane vertically.

 Rotate By 90               Rotates the connector pane counter-clockwise by 90 degrees.

 Wiring Rule:Get            Gets the wiring properties of a connector pane terminal.

 Wiring Rule:Set            Sets the wiring properties of a connector pane terminal.


                                                    © National Instruments 9307

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9307 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9308 ordinal=9308 -->
## Property and Method Reference

Property and Method Reference

    AssignAssign ControlControl ToTo TerminalTerminal

       Assigns a front panel control to a connector pane terminal of the VI.

      You can use this method to configure the connector panes of a target VI using VI
        Scripting.

     Parameters

                 Data      Name         Required  Description
                 type

         Control         Yes        Specifies the control to assign to a connector pane terminal.


                                     Specifies the index of the connector pane terminal to which to assign
        Terminal                 the control. Display additional VI Scripting information in the Context
                        Yes         Index                   Help window to identify the terminal index of the connector pane
                                   terminal to which you want to assign the control.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

         Settable when the VI is running                             No

        Loads the front panel into memory                                  Yes

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes


9308   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9308 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9309 ordinal=9309 -->
## Property and Method Reference

Property and Method Reference

DisconnectDisconnect AllAll TerminalsTerminals

Disconnects all connector pane terminals from controls and indicators.

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                              No

 Available in Real-Time Operating System                      No

 Settable when the VI is running                             No

 Loads the front panel into memory                                  Yes

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

DisconnectDisconnect TerminalTerminal

Disconnects a connector pane terminal from a control or an indicator.

Parameters

          Data
 Name         Required  Description
          type

                             Specifies the index of the connector pane terminal to which to assign
 Terminal                 the control. Display additional VI Scripting information in the Context
                Yes
 Index                   Help window to identify the terminal index of the connector pane
                           terminal to which you want to assign the control.


                                                    © National Instruments 9309

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9309 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9310 ordinal=9310 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

         Settable when the VI is running                             No

        Loads the front panel into memory                                  Yes

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

    FlipFlip HorizontalHorizontal

        Flips the connector pane horizontally.

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

         Settable when the VI is running                             No

        Loads the front panel into memory                                  Yes

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes


9310   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9310 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9311 ordinal=9311 -->
## Property and Method Reference

Property and Method Reference

FlipFlip VerticalVertical

Flips the connector pane vertically.

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                              No

 Available in Real-Time Operating System                      No

 Settable when the VI is running                             No

 Loads the front panel into memory                                  Yes

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

RotateRotate ByBy 9090

Rotates the connector pane counter-clockwise by 90 degrees.

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                              No

 Available in Real-Time Operating System                      No

 Settable when the VI is running                             No

 Loads the front panel into memory                                  Yes

 Need to authenticate before use                            No

                                                    © National Instruments 9311

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9311 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9312 ordinal=9312 -->
## Property and Method Reference

Property and Method Reference


        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

    WiringWiring Rule:GetRule:Get

       Gets the wiring properties of a connector pane terminal.

       Possible values include Invalid Wire Rule, Required, Recommended,
     Optional, and Dynamic Dispatch.

     Parameters

                 Data      Name         Required  Description
                 type

                                     Specifies the index of the connector pane terminal to which to assign
        Terminal                 the control. Display additional VI Scripting information in the Context
                        Yes         Index                   Help window to identify the terminal index of the connector pane
                                   terminal to which you want to assign the control.


     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                         No

         Available in Real-Time Operating System                                 No

         Settable when the VI is running                                        No

        Loads the front panel into memory                                                 Yes

       Need to authenticate before use                                       No

        Loads the block diagram into memory                                   No

       Remote access allowed                                                           Yes


9312   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9312 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9313 ordinal=9313 -->
## Property and Method Reference

Property and Method Reference

WiringWiring Rule:SetRule:Set

Sets the wiring properties of a connector pane terminal.

Parameters

          Data Name         Required  Description          type

                             Specifies the index of the connector pane terminal to which to assign
 Terminal                 the control. Display additional VI Scripting information in the Context                Yes Index                   Help window to identify the terminal index of the connector pane
                           terminal to which you want to assign the control.


                             Specifies the rules for the wiring properties.

                         0        Invalid Wire Rule

                         1       Required
 Rule            Yes
                         2      Recommended

                         3       Optional

                         4      Dynamic Dispatch


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                              No

 Available in Real-Time Operating System                      No

 Settable when the VI is running                             No

 Loads the front panel into memory                                  Yes


                                                    © National Instruments 9313

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9313 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9314 ordinal=9314 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

   ConnectorPaneConnectorPane PropertiesProperties


        Property     Description

         Controls[]     Gets the controls hooked to the connector.

         Icon Visible   Makes the icon or the connector pane visible.

       Number of
        Connection   Returns the number of connection terminals in the connector pane
         Terminals

         Pattern       Assigns or gets the connector pane pattern for a VI. Valid values are 4800 to 4835.

                      Returns an array of terminal bounds for the referenced connector pane. The bounds        Terminal                          for each terminal are represented as a cluster of integers that indicate the position of        Bounds[]
                    each edge of the terminal rectangle.

         WiringRules[]  Sets or returns an array of the wiring rules for each terminal on a connector pane.

    Controls[]Controls[]

       Gets the controls hooked to the connector.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                               Read Only

         Available in Run-Time Engine                                        Yes (Read Only)

         Available in Real-Time Operating System                             Yes


9314   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9314 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9315 ordinal=9315 -->
## Property and Method Reference

Property and Method Reference


 Settable when the VI is running                             No

 Loads the front panel into memory                                  Yes

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

IconIcon VisibleVisible

Makes the icon or the connector pane visible.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read/Write

 Available in Run-Time Engine                                        Yes (Read Only)

 Available in Real-Time Operating System                             Yes

 Settable when the VI is running                                      Yes

 Loads the front panel into memory                                  Yes

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

NumberNumber ofof ConnectionConnection TerminalsTerminals

Returns the number of connection terminals in the connector pane

Remarks

The following table lists the characteristics of this property.

                                                    © National Instruments 9315

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9315 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9316 ordinal=9316 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                                   Yes

         Settable when the VI is running                                  No

        Loads the front panel into memory                                         Yes

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

    PatternPattern

       Assigns or gets the connector pane pattern for a VI. Valid values are 4800 to 4835.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                 No

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes


9316   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9316 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9317 ordinal=9317 -->
## Property and Method Reference

Property and Method Reference

TerminalTerminal Bounds[]Bounds[]

Returns an array of terminal bounds for the referenced connector pane. The bounds
for each terminal are represented as a cluster of integers that indicate the position of
each edge of the terminal rectangle.

The array elements are in terminal order as defined in the Connector Pane Pattern
Reference VI for each connector pane pattern.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                               Read Only

 Available in Run-Time Engine                                        Yes (Read Only)

 Available in Real-Time Operating System                             Yes

 Settable when the VI is running                             No

 Loads the front panel into memory                                  Yes

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Application Control\VI Scripting\
   Connector Pane\Connector Pane Pattern Reference.vi


                                                    © National Instruments 9317

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9317 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9318 ordinal=9318 -->
## Property and Method Reference

Property and Method Reference

    WiringRules[]WiringRules[]

       Sets or returns an array of the wiring rules for each terminal on a connector pane.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                 No

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

     BusBus

      Bus Properties
   BusBus PropertiesProperties


        Property     Description

        Bar Plot
                      Gets or sets the bar plot style.
         Style

          Digital Line   Sets whether LabVIEW uses a thin or thick line in the plot to distinguish high or low
         Style         values or to offset a particular plot line. Applies to digital plots only.

          Digital        Sets whether to display high to low transitions at the previous point, in between
         Transition     points, or at the new point on the x-axis. The default displays high to low transitions


9318   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9318 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9319 ordinal=9319 -->
## Property and Method Reference

Property and Method Reference


Property     Description

Location      at the new point on the x-axis. Applies to digital plots only.

Digital              Sets how LabVIEW distinguishes differing values in the plot. This affects only plotsTransition             with more than one bit. Applies to digital plots only.Type

                    Fill baseline: -1 None, -2 Zero, -3 Negative Infinity, -4 Infinity. Otherwise, the numberFill To               of the plot being filled.

Fill/Point             Get or set the color of the point and fills.Color

Fixed Point   Sets the number of digits of precision shown in the digital bus label when you select
Digits of      the Fixed Point label format. You can use the Label Format property to set the label
Precision     format programmatically.

             Gets or sets a cluster of settings that indicate or control the fixed-point
Fixed Point    representation of a digital bus. You can use this property only if you set the bus to
Settings      Fixed Point label format. You can use the Label Format property to set the label
             format programmatically.

             Gets or sets the formatting style of the digital bus label that LabVIEW displays whenFixed Point            you select the Fixed Point label format. You can use the Label Format property to set
Style             the label format programmatically.

Label        Gets or sets the format of the text label on a digital bus. LabVIEW displays the plot
Format        label only if there is enough room in the digital graph plot.

             Get or set the line style (0-4) as shown on the shortcut menu from top-left to bottom-
Line Style                 right.

Line Width    Get or set the width of the plot (0-5).

Plot Color    Get or set the color of the plot.

Plot
             Get or set the interpolation of the plot.
Interpolation

             Get or set the name of the plot. If the Ignore Attributes property is FALSE, you cannot
Plot Name
               set the plot name.

             Get or set the point style (0-16) as shown on the shortcut menu from top-left to
Point Style
              bottom-right.

Visible      Shows the plot.

X Scale Index  Gets the index of X-scale with which this plot is associated.

Y Scale Index  Gets the index of Y-scale with which this plot is associated.

                                                    © National Instruments 9319

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9319 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9320 ordinal=9320 -->
## Property and Method Reference

Property and Method Reference

   BarBar PlotPlot StyleStyle

       Gets or sets the bar plot style.

       This property is similar to the Bar Plots item on the shortcut menu of a plot.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    DigitalDigital LineLine StyleStyle

       Sets whether LabVIEW uses a thin or thick line in the plot to distinguish high or low
       values or to offset a particular plot line. Applies to digital plots only.

       This property is similar to the Line Style item on the shortcut menu of a digital
      waveform graph plot legend.

     Remarks

      The following table lists the characteristics of this property.


9320   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9320 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9321 ordinal=9321 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

DigitalDigital TransitionTransition LocationLocation

Sets whether to display high to low transitions at the previous point, in between
points, or at the new point on the x-axis. The default displays high to low transitions at
the new point on the x-axis. Applies to digital plots only.

This property is similar to the Transition Location item on the shortcut menu of a plot.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No


                                                    © National Instruments 9321

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9321 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9322 ordinal=9322 -->
## Property and Method Reference

Property and Method Reference


       Remote access allowed                                                  Yes

    DigitalDigital TransitionTransition TypeType

       Sets how LabVIEW distinguishes differing values in the plot. This affects only plots with
      more than one bit. Applies to digital plots only.

       This property is similar to the Transition Type item on the shortcut menu of a plot.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

     FillFill ToTo

          Fill baseline: -1 None, -2 Zero, -3 Negative Infinity, -4 Infinity. Otherwise, the number of
       the plot being filled.

       This property is similar to the Fill Base Line item on the shortcut menu of a plot and
       the Fill to option on the Plots page of the Properties dialog box.


9322   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9322 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9323 ordinal=9323 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Fill/PointFill/Point ColorColor

Get or set the color of the point and fills.

You can set the color of the front panel object by wiring a hexadecimal number with
the form RRGGBB or by wiring the color box constant to the property.

This property is similar to the Point/fill color option on the Plots page of the
Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

                                                    © National Instruments 9323

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9323 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9324 ordinal=9324 -->
## Property and Method Reference

Property and Method Reference


         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    FixedFixed PointPoint DigitsDigits ofof PrecisionPrecision

       Sets the number of digits of precision shown in the digital bus label when you select
       the Fixed Point label format. You can use the Label Format property to set the label
       format programmatically.

       This property is similar to the Digits of Precision option on the Configure Fixed Point
       dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes


9324   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9324 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9325 ordinal=9325 -->
## Property and Method Reference

Property and Method Reference

FixedFixed PointPoint SettingsSettings

Gets or sets a cluster of settings that indicate or control the fixed-point representation
of a digital bus. You can use this property only if you set the bus to Fixed Point label
format. You can use the Label Format property to set the label format
programmatically.

The cluster that this property gets or sets includes the following components:

  • Signed—Boolean that specifies whether the fixed-point data is signed or unsigned.
  • Word Length—Long unsigned integer that specifies the total number of bits in the
    bit string that LabVIEW uses to represent all possible values of the fixed-point data.
   LabVIEW accepts a maximum word length of 64 bits.
  • Integer Word Length—Long signed integer that specifies the number of bits in the
    bit string that LabVIEW uses to represent the integer portion of the value of the
    fixed-point data. The integer word length can be larger than the word length, and
   can be positive or negative.

This property is similar to the Encoding options on the Configure Fixed Point dialog
box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

                                                    © National Instruments 9325

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9325 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9326 ordinal=9326 -->
## Property and Method Reference

Property and Method Reference

    FixedFixed PointPoint StyleStyle

       Gets or sets the formatting style of the digital bus label that LabVIEW displays when
      you select the Fixed Point label format. You can use the Label Format property to set
       the label format programmatically.

       This property is similar to the Style option on the Configure Fixed Point dialog box.

      Values

        0             Normal

        1                 Scientific

        2               Engineering

        3                 SI notation

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes


9326   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9326 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9327 ordinal=9327 -->
## Property and Method Reference

Property and Method Reference

LabelLabel FormatFormat

Gets or sets the format of the text label on a digital bus. LabVIEW displays the plot label
only if there is enough room in the digital graph plot.

This property is similar to the Label Format item on the shortcut menu of the plot
legend of a mixed signal or digital waveform graph.

This property is similar to the Format option on the Plots page of the Digital Graph
Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

LineLine StyleStyle

Get or set the line style (0-4) as shown on the shortcut menu from top-left to bottom-
right.

This property is similar to the Line Style item on the shortcut menu of a plot and the
Line Style option on the Plots page of the Properties dialog box.


                                                    © National Instruments 9327

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9327 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9328 ordinal=9328 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    LineLine WidthWidth

      Get or set the width of the plot (0-5).

       This property is similar to the Line Width item on the shortcut menu of a plot and the
       Line Width option on the Plots page of the Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No


9328   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9328 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9329 ordinal=9329 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

PlotPlot ColorColor

Get or set the color of the plot.

You can set the color of the front panel object by wiring a hexadecimal number with
the form RRGGBB or by wiring the color box constant to the property.

This property is similar to the Color item on the shortcut menu of a plot and the Line
color option on the Plots page of the Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

PlotPlot InterpolationInterpolation

Get or set the interpolation of the plot.


                                                    © National Instruments 9329

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9329 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9330 ordinal=9330 -->
## Property and Method Reference

Property and Method Reference

       This property is similar to the Interpolation item on the shortcut menu of a plot and
       the Plot Interpolation option on the Plots page of the Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    PlotPlot NameName

      Get or set the name of the plot. If the Ignore Attributes property is FALSE, you cannot
       set the plot name.

       This property is similar to the Name option on the Plots page of the Properties dialog
       box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes


9330   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9330 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9331 ordinal=9331 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

PointPoint StyleStyle

Get or set the point style (0-16) as shown on the shortcut menu from top-left to
bottom-right.

This property is similar to the Point Style item on the shortcut menu of a plot and
Point Style option on the Plots page of the Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes


                                                    © National Instruments 9331

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9331 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9332 ordinal=9332 -->
## Property and Method Reference

Property and Method Reference

    VisibleVisible

      Shows the plot.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   XX ScaleScale IndexIndex

       Gets the index of X-scale with which this plot is associated.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

9332   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9332 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9333 ordinal=9333 -->
## Property and Method Reference

Property and Method Reference


 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

YY ScaleScale IndexIndex

Gets the index of Y-scale with which this plot is associated.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

ProbeProbe

Probe Properties
ProbeProbe PropertiesProperties


                                                    © National Instruments 9333

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9333 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9334 ordinal=9334 -->
## Property and Method Reference

Property and Method Reference


        Property          Description

        Wire              Returns the wire that references the probe.

   WireWire

       Returns the wire that references the probe.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

      SubWizardSubWizard

      SubWizard Methods

      SubWizard Properties
   SubWizardSubWizard MethodsMethods


9334   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9334 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9335 ordinal=9335 -->
## Property and Method Reference

Property and Method Reference


 Method      Description

 Is Locked By              Returns a value of TRUE if the object is in the SubWizard list of locked objects. Me

 Lock Const   Adds a diagram constant to a SubWizard list of locked objects.

 Lock Object  Adds the specified object to the SubWizard list of locked objects.

 Unlock            Removes a diagram constant from a SubWizard list of locked objects Const

 Unlock      Unlocks panel objects. If the Objects parameter is not wired, the currently selected
 Object       objects are unlocked.

IsIs LockedLocked ByBy MeMe

Returns a value of TRUE if the object is in the SubWizard list of locked objects.

Parameters

 Name       Data type      Required      Description

 Obj Ref                     Yes           References the object.


 Locked?                     Yes           Queries whether the object is locked.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                             Yes

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

                                                    © National Instruments 9335

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9335 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9336 ordinal=9336 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

   LockLock ConstConst

      Adds a diagram constant to a SubWizard list of locked objects.

     Parameters

      Name                   Data type     Required     Description

        Const                                   Yes         The constant you want to lock.


        Allow Value Change                 No           Allows a change in value.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes


9336   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9336 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9337 ordinal=9337 -->
## Property and Method Reference

Property and Method Reference

LockLock ObjectObject

Adds the specified object to the SubWizard list of locked objects.

Parameters

 Name        Data type     Required     Description

 ObjectRef                    Yes           References the object you want to lock.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                             Yes

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

UnlockUnlock ConstConst

Removes a diagram constant from a SubWizard list of locked objects


                                                    © National Instruments 9337

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9337 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9338 ordinal=9338 -->
## Property and Method Reference

Property and Method Reference

     Parameters

      Name     Data type       Required       Description

        Const                      Yes           The constant you want to unlock.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

   UnlockUnlock ObjectObject

      Unlocks panel objects. If the Objects parameter is not wired, the currently selected
       objects are unlocked.

     Parameters

      Name        Data type    Required     Description

         Object Ref                   Yes          References the object you want to unlock.


9338   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9338 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9339 ordinal=9339 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                             Yes

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

SubWizardSubWizard PropertiesProperties


 Property           Description

 Locked Objects     Returns an array of references to all objects locked by the wizard.

LockedLocked ObjectsObjects

Returns an array of references to all objects locked by the wizard.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                           No


                                                    © National Instruments 9339

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9339 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9340 ordinal=9340 -->
## Property and Method Reference

Property and Method Reference


         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                       No

   StateDiagramWizardStateDiagramWizard

      StateDiagramWizard Methods
   StateDiagramWizardStateDiagramWizard MethodsMethods


       Method             Description

       Remove State      Removes the state at State Idx from the state diagram.

   RemoveRemove StateState

      Removes the state at State Idx from the state diagram.

     Parameters

      Name        Data type   Required   Description

         State Index                Yes        The state index of the state you want to remove.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value


9340   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9340 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9341 ordinal=9341 -->
## Property and Method Reference

Property and Method Reference


 Available in Run-Time Engine                              No

 Available in Real-Time Operating System                      No

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

CodeWizardCodeWizard

CodeWizard Properties
CodeWizardCodeWizard PropertiesProperties


 Property      Description

 Name         Gets or sets the name of the code wizard.

 Path          Gets or sets the VI path of the code wizard, or callback VI.

NameName

Gets or sets the name of the code wizard.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes


                                                    © National Instruments 9341

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9341 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9342 ordinal=9342 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   PathPath

       Gets or sets the VI path of the code wizard, or callback VI.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    ExternalEditorWizardExternalEditorWizard

       ExternalEditorWizard Methods

       ExternalEditorWizard Properties


9342   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9342 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9343 ordinal=9343 -->
## Property and Method Reference

Property and Method Reference

ExternalEditorWizardExternalEditorWizard MethodsMethods


 Method                 Description

 LaunchEditor          Launch the external editor for this wizard.

LaunchEditorLaunchEditor

Launch the external editor for this wizard.

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                              No

 Available in Real-Time Operating System                      No

 Settable when the VI is running                                      Yes

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

ExternalEditorWizardExternalEditorWizard PropertiesProperties


 Property        Description

                   Gets/sets reference to the master container structure within which all locked
 MasterContainer
                  objects for this external editor wizard reside.

                   Gets/sets reference to the master object from which all other necessary objects
 MasterObject
                    for this external editor wizard can be reached.


                                                    © National Instruments 9343

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9343 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9344 ordinal=9344 -->
## Property and Method Reference

Property and Method Reference

   MasterContainerMasterContainer

       Gets/sets reference to the master container structure within which all locked objects
        for this external editor wizard reside.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   MasterObjectMasterObject

       Gets/sets reference to the master object from which all other necessary objects for this
       external editor wizard can be reached.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No


9344   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9344 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9345 ordinal=9345 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

FlatSequenceFrameFlatSequenceFrame

FlatSequenceFrame Properties
FlatSequenceFrameFlatSequenceFrame PropertiesProperties


 Property             Description

                     Returns the size of the visible portion of a frame diagram on a Flat Sequence Content Rect                        structure.

 Diagram             Returns a reference to the diagram of the Flat Sequence structure.

 Frame Size           Gets or sets the height and width of a Flat Sequence structure frame.

 Left Side Inner        Returns an array of references to inner tunnels on the left side of a Flat
 Tunnels[]           Sequence structure.

 Outer Tunnels[]       Returns an array of references to outer tunnels on a Flat Sequence structure.

 Right Side Inner      Returns an array of references to inner tunnels on the right side of a Flat
 Tunnels[]           Sequence structure.

ContentContent RectRect

Returns the size of the visible portion of a frame diagram on a Flat Sequence structure.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 9345

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9345 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9346 ordinal=9346 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                                   Yes

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

   DiagramDiagram

       Returns a reference to the diagram of the Flat Sequence structure.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                                   Yes

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes


9346   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9346 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9347 ordinal=9347 -->
## Property and Method Reference

Property and Method Reference

FrameFrame SizeSize

Gets or sets the height and width of a Flat Sequence structure frame.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                 No

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

LeftLeft SideSide InnerInner Tunnels[]Tunnels[]

Returns an array of references to inner tunnels on the left side of a Flat Sequence
structure.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

                                                    © National Instruments 9347

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9347 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9348 ordinal=9348 -->
## Property and Method Reference

Property and Method Reference


         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

   OuterOuter Tunnels[]Tunnels[]

       Returns an array of references to outer tunnels on a Flat Sequence structure.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                                   Yes

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

    RightRight SideSide InnerInner Tunnels[]Tunnels[]

       Returns an array of references to inner tunnels on the right side of a Flat Sequence
        structure.


9348   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9348 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9349 ordinal=9349 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

TimeSequenceFrameTimeSequenceFrame

MasterWizardMasterWizard

ProjectProject

Project Methods

Project Properties

ProjectProject MethodsMethods


 Method        Description

 Browse         Displays a dialog box that allows you to browse for a variable and then returns a
 Variable Dialog  reference to the variable you select.

                Closes a LabVIEW project and all references to all items in the project. This method
 Close           also closes the Project Explorer window if it is open and closes any VIs that are
              open in any application instance owned by the project. You also can select


                                                    © National Instruments 9349

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9349 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9350 ordinal=9350 -->
## Property and Method Reference

Property and Method Reference


       Method        Description

                         File»Close All to close the project and the Project Explorer window.

         Close Window   Closes only the Project Explorer window. This method does not close VI windows.

        Deploy Items   Deploys an array of items in the LabVIEW project.

        Item From      Returns the refnum of the project item with the specified Item ID. Use this method
        Item ID          in conjunction with the Item ID property of the ProjectItem class.

         Local Project
         Settings:Delete  Deletes an item from the local project settings file.
        Item

         Local Project
         Settings:Delete  Deletes an entire section from the local project settings file.
         Section

         Local Project
         Settings:Get    Gets an item from the local project settings file.
        Item

         Local Project
         Settings:Has    Determines if an item exists in the local project settings file.
        Item

         Local Project
         Settings:Has    Determines if a section exists in the local project settings file.
         Section

         Local Project
         Settings:Set     Sets an item in the local project settings file.
        Item

       Open Window   Displays the Project Explorer window.

         Refresh Auto-
                        Force all auto-populated folders on this project to update their contents to match
         Populating
                        the disk.
         Folders

                       Saves the LabVIEW project to the path that the project was previously saved to or
        Save
                       loaded from or to a specified path.

                        Allows a LabVIEW project to be saved as a different name or to a different location.
                         This method also enables the save operation to copy all of the contents of the
        Save As         project to the new location. If you do not wire data to Items to copy, LabVIEW
                        copies everything to the new location. Otherwise, LabVIEW copies only the items
                     you specify.


9350   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9350 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9351 ordinal=9351 -->
## Property and Method Reference

Property and Method Reference


 Method        Description

               Saves a copy of the project to a new location on disk, where all referenced VIs are Save Copy                   in the same location.

               Saves a copy of the LabVIEW project that is readable by LabVIEW 8.0 and later. This Save For             method is similar to the LabVIEW Version selection in the Save for Previous Previous
                 Version dialog box.

 Undeploy               Undeploys an array of items and their dependencies. Items

BrowseBrowse VariableVariable DialogDialog

Displays a dialog box that allows you to browse for a variable and then returns a
reference to the variable you select.

Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                         No

 Available in Real-Time Operating System                                 No

 Settable when the VI is running                                        No

 Loads the front panel into memory                                     No

 Need to authenticate before use                                       No

 Loads the block diagram into memory                                   No

 Remote access allowed                                                           Yes

CloseClose

Closes a LabVIEW project and all references to all items in the project. This method
also closes the Project Explorer window if it is open and closes any VIs that are open in
any application instance owned by the project. You also can select File»Close All to

                                                    © National Instruments 9351

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9351 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9352 ordinal=9352 -->
## Property and Method Reference

Property and Method Reference

       close the project and the Project Explorer window.

           Note The LabVIEW Datalogging and Supervisory Control Module supports
                 this method in the Run-Time Engine.

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                      No

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

   CloseClose WindowWindow

       Closes only the Project Explorer window. This method does not close VI windows.

      You also can select File»Exit to close the Project Explorer window and any VIs that are
      open.

           Note The LabVIEW Datalogging and Supervisory Control Module supports
                 this method in the Run-Time Engine.

     Remarks

      The following table lists the characteristics of this method.


9352   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9352 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9353 ordinal=9353 -->
## Property and Method Reference

Property and Method Reference


 Data type                                            No return value

 Available in Run-Time Engine                              No

 Available in Real-Time Operating System                      No

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

DeployDeploy ItemsItems

Deploys an array of items in the LabVIEW project.

In the Project Explorer window, you also can open and run a VI under a target to deploy
files to the target.

      Note The LabVIEW Datalogging and Supervisory Control Module supports
         this method in the Run-Time Engine.

Parameters

          Data
 Name           Required  Description
          type

 Items             Yes        Specifies an array of references to items in the project.


                                               If TRUE, LabVIEW does not display any dialog boxes during the
 Silent            Yes
                           deploy operation. The default is FALSE.


 User
              No       User name that is required if the project library is password-
 Name


                                                    © National Instruments 9353

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9353 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9354 ordinal=9354 -->
## Property and Method Reference

Property and Method Reference


                 Data      Name           Required  Description
                  type

                                      protected.


                                        Specifies the password to use to unlock a password-protected        Password       No                                       project library.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

   ItemItem FromFrom ItemItem IDID

       Returns the refnum of the project item with the specified Item ID. Use this method in
       conjunction with the Item ID property of the ProjectItem class.

           Note The LabVIEW Datalogging and Supervisory Control Module supports
                 this method in the Run-Time Engine.


9354   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9354 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9355 ordinal=9355 -->
## Property and Method Reference

Property and Method Reference

Parameters

 Name            Data type              Required              Description

 Item ID                                    Yes

Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                         No

 Available in Real-Time Operating System                                 No

 Settable when the VI is running                                        No

 Loads the front panel into memory                                     No

 Need to authenticate before use                                       No

 Loads the block diagram into memory                                   No

 Remote access allowed                                                           Yes

LocalLocal ProjectProject Settings:DeleteSettings:Delete ItemItem

Deletes an item from the local project settings file.

Parameters

        Data
 Name        Required  Description
         type

                            Specifies the name of a collection of tag-value pairs that you want to
 Section        Yes
                         search for, set, get, or delete from a local project settings file.


 Tag           Yes        Specifies the name of the item you want to set, get, or delete from the


                                                    © National Instruments 9355

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9355 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9356 ordinal=9356 -->
## Property and Method Reference

Property and Method Reference


                Data      Name        Required  Description
                type

                                     section.


     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                         No

         Available in Real-Time Operating System                                 No

         Settable when the VI is running                                        No

        Loads the front panel into memory                                     No

       Need to authenticate before use                                       No

        Loads the block diagram into memory                                   No

       Remote access allowed                                                           Yes

    LocalLocal ProjectProject Settings:DeleteSettings:Delete SectionSection

       Deletes an entire section from the local project settings file.

     Parameters

                Data
      Name        Required  Description
                type

                                    Specifies the name of a collection of tag-value pairs that you want to
         Section        Yes
                                 search for, set, get, or delete from a local project settings file.


9356   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9356 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9357 ordinal=9357 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                         No

 Available in Real-Time Operating System                                 No

 Settable when the VI is running                                        No

 Loads the front panel into memory                                     No

 Need to authenticate before use                                       No

 Loads the block diagram into memory                                   No

 Remote access allowed                                                           Yes

LocalLocal ProjectProject Settings:GetSettings:Get ItemItem

Gets an item from the local project settings file.

Parameters

        Data Name        Required  Description         type

                            Specifies the name of a collection of tag-value pairs that you want to
 Section        Yes
                         search for, set, get, or delete from a local project settings file.


                            Specifies the name of the item you want to set, get, or delete from the
 Tag           Yes
                            section.

                            Specifies the value of the item. This input accepts the following data
                           types:
 Value         Yes
                                         •  String
                                         •  Integer


                                                    © National Instruments 9357

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9357 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9358 ordinal=9358 -->
## Property and Method Reference

Property and Method Reference


                Data      Name        Required  Description
                type

                                                     • Boolean
                                                     • Path


     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                                      Yes

         Available in Real-Time Operating System                                 No

         Settable when the VI is running                                        No

        Loads the front panel into memory                                     No

       Need to authenticate before use                                       No

        Loads the block diagram into memory                                   No

       Remote access allowed                                                           Yes

    LocalLocal ProjectProject Settings:HasSettings:Has ItemItem

      Determines if an item exists in the local project settings file.

     Parameters

                Data
      Name        Required  Description
                type

                                    Specifies the name of a collection of tag-value pairs that you want to
         Section        Yes
                                 search for, set, get, or delete from a local project settings file.


9358   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9358 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9359 ordinal=9359 -->
## Property and Method Reference

Property and Method Reference


        Data Name        Required  Description
         type

                            Specifies the name of the item you want to set, get, or delete from the Tag           Yes                            section.


Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                                      Yes

 Available in Real-Time Operating System                                 No

 Settable when the VI is running                                        No

 Loads the front panel into memory                                     No

 Need to authenticate before use                                       No

 Loads the block diagram into memory                                   No

 Remote access allowed                                                           Yes

LocalLocal ProjectProject Settings:HasSettings:Has SectionSection

Determines if a section exists in the local project settings file.

Parameters

        Data
 Name        Required  Description
         type

                            Specifies the name of a collection of tag-value pairs that you want to
 Section        Yes
                         search for, set, get, or delete from a local project settings file.


                                                    © National Instruments 9359

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9359 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9360 ordinal=9360 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                                      Yes

         Available in Real-Time Operating System                                 No

         Settable when the VI is running                                        No

        Loads the front panel into memory                                     No

       Need to authenticate before use                                       No

        Loads the block diagram into memory                                   No

       Remote access allowed                                                           Yes

    LocalLocal ProjectProject Settings:SetSettings:Set ItemItem

       Sets an item in the local project settings file.

     Parameters

                Data      Name        Required  Description                type

                                    Specifies the name of a collection of tag-value pairs that you want to
         Section        Yes
                                 search for, set, get, or delete from a local project settings file.


                                    Specifies the name of the item you want to set, get, or delete from the
        Tag           Yes
                                     section.

                                    Specifies the value of the item. This input accepts the following data
                                    types:
         Value         Yes
                                                     •  String
                                                     •  Integer


9360   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9360 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9361 ordinal=9361 -->
## Property and Method Reference

Property and Method Reference


        Data Name        Required  Description
         type

                                         • Boolean
                                         • Path


Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                         No

 Available in Real-Time Operating System                                 No

 Settable when the VI is running                                        No

 Loads the front panel into memory                                     No

 Need to authenticate before use                                       No

 Loads the block diagram into memory                                   No

 Remote access allowed                                                           Yes

OpenOpen WindowWindow

Displays the Project Explorer window.

You also can select File»Open Project to display the Project Explorer window.

      Note The LabVIEW Datalogging and Supervisory Control Module supports
         this method in the Run-Time Engine.

Remarks

The following table lists the characteristics of this method.


                                                    © National Instruments 9361

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9361 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9362 ordinal=9362 -->
## Property and Method Reference

Property and Method Reference


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Application Control\VI Server\
        Manipulating Projects\Add Files to Project.vi
    RefreshRefresh Auto-PopulatingAuto-Populating FoldersFolders

       Force all auto-populated folders on this project to update their contents to match the
        disk.

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                      No

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No


9362   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9362 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9363 ordinal=9363 -->
## Property and Method Reference

Property and Method Reference


 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

SaveSave

Saves the LabVIEW project to the path that the project was previously saved to or
loaded from or to a specified path.

If the project has not been saved and the value of the Path parameter is <Not A
Path> or Path is unwired, this method returns an error. You also can select File»Save
Project to save the project.

      Note The LabVIEW Datalogging and Supervisory Control Module supports
         this method in the Run-Time Engine.

Parameters

 Name        Data type           Required            Description

 Path                       No                 Path to the project.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                              No

 Available in Real-Time Operating System                      No

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No


                                                    © National Instruments 9363

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9363 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9364 ordinal=9364 -->
## Property and Method Reference

Property and Method Reference


        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

   SaveSave AsAs

       Allows a LabVIEW project to be saved as a different name or to a different location. This
      method also enables the save operation to copy all of the contents of the project to the
     new location. If you do not wire data to Items to copy, LabVIEW copies everything to
       the new location. Otherwise, LabVIEW copies only the items you specify.

     Parameters

                    Data      Name               Required  Description                    type

        Path                  Yes       Path to the project.


       Copy                              Specifies whether to copy all of the contents of the project to the                       No
         contents?                  new location.


        Items to                       No        Specifies the items to copy to the new location.        copy

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

         Settable when the VI is running                             No

        Loads the front panel into memory                          No


9364   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9364 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9365 ordinal=9365 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

SaveSave CopyCopy

Saves a copy of the project to a new location on disk, where all referenced VIs are in
the same location.

      Note The LabVIEW Datalogging and Supervisory Control Module supports
         this method in the Run-Time Engine.

Parameters

 Name   Data type   Required    Description

 Path                 Yes         Path to where you want to save a copy of the project.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                              No

 Available in Real-Time Operating System                      No

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes


                                                    © National Instruments 9365

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9365 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9366 ordinal=9366 -->
## Property and Method Reference

Property and Method Reference

   SaveSave ForFor PreviousPrevious

      Saves a copy of the LabVIEW project that is readable by LabVIEW 8.0 and later. This
      method is similar to the LabVIEW Version selection in the Save for Previous Version
       dialog box.

           Note The LabVIEW Datalogging and Supervisory Control Module supports
                 this method in the Run-Time Engine.

     Parameters

                Data
      Name        Required  Description                type

        Path          Yes       Path to the directory where you want to save the LabVIEW project.


                                  Version of LabVIEW for which you want to save. Wire the version number,
         Version      No       such as 8.6 or 9.0, to the Version input. The default is the immediately
                                 previous version.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No


9366   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9366 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9367 ordinal=9367 -->
## Property and Method Reference

Property and Method Reference


 Remote access allowed                                             Yes

UndeployUndeploy ItemsItems

Undeploys an array of items and their dependencies.

Parameters

 Name    Data type     Required     Description

 Items                   Yes            Specifies the items you want to undeploy.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                              No

 Available in Real-Time Operating System                      No

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

ProjectProject PropertiesProperties


 Property    Description

 Active           If the Project Explorer window has focus, returns an array of references to the selected
 Items In     project items in the Project Explorer window. If the Project Explorer window does not
 Tree       have focus, returns a reference to the project item associated with the VI window that


                                                    © National Instruments 9367

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9367 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9368 ordinal=9368 -->
## Property and Method Reference

Property and Method Reference


        Property    Description

                   has focus. You can use these references with the ProjectItem properties.

                    Returns the application reference for the My Computer target in the LabVIEW project.         Application                   You can use this reference with the Application properties.

                    Gets or sets the description of the LabVIEW project. You also can use the Project page         Description
                       of the Project Properties dialog box to set the project description.

        Items View                Show or hide the Items page in the Project Explorer window.         Active

       My         Returns a reference to My Computer in the Project Explorer window for the LabVIEW
       Computer   project. You can use this reference with the TargetItem properties.

                    Gets the name of the LabVIEW project. If the project has been saved, this property
                      returns the filename with the file extension. If the project has not been saved, this
      Name                     property returns untitled project x and you can write to this property to
                   change the name.

                    Gets the path to the saved LabVIEW project on disk. This path includes the filename of        Path
                    the project.

                    Returns a reference to the project root in the Project Explorer window. The project
        Root        root is the top item that represents the LabVIEW project in the Project Explorer
                   window. You can use this reference with the ProjectItem properties.

         Selected                    Returns an array of references to the project items currently selected in the Project        Items in
                      Explorer window. You can use these references with the ProjectItem properties.         Tree

                    Returns an array of references to all targets in the current LabVIEW project. You can
         Targets                   use these references with the TargetItem properties.

       Window
                    Returns the state of the Project Explorer window.
         State

    ActiveActive ItemsItems InIn TreeTree

           If the Project Explorer window has focus, returns an array of references to the selected
       project items in the Project Explorer window. If the Project Explorer window does not
      have focus, returns a reference to the project item associated with the VI window that
      has focus. You can use these references with the ProjectItem properties.


9368   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9368 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9369 ordinal=9369 -->
## Property and Method Reference

Property and Method Reference

      Note The LabVIEW Datalogging and Supervisory Control Module supports
         this property in the Run-Time Engine.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

ApplicationApplication

Returns the application reference for the My Computer target in the LabVIEW project.
You can use this reference with the Application properties.

If the project has multiple targets, each target is associated with a single application
instance.

      Note The LabVIEW Datalogging and Supervisory Control Module supports
         this property in the Run-Time Engine.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 9369

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9369 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9370 ordinal=9370 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

    DescriptionDescription

       Gets or sets the description of the LabVIEW project. You also can use the Project page
       of the Project Properties dialog box to set the project description.

           Note The LabVIEW Datalogging and Supervisory Control Module supports
                 this property in the Run-Time Engine.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read/Write

         Available in Run-Time Engine                                        Yes (Read Only)

         Available in Real-Time Operating System                      No

         Settable when the VI is running                                      Yes

        Loads the front panel into memory                          No

       Need to authenticate before use                            No


9370   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9370 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9371 ordinal=9371 -->
## Property and Method Reference

Property and Method Reference


 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

ItemsItems ViewView ActiveActive

Show or hide the Items page in the Project Explorer window.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                 No

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

MyMy ComputerComputer

Returns a reference to My Computer in the Project Explorer window for the LabVIEW
project. You can use this reference with the TargetItem properties.

      Note The LabVIEW Datalogging and Supervisory Control Module supports
         this property in the Run-Time Engine.


                                                    © National Instruments 9371

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9371 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9372 ordinal=9372 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

   NameName

       Gets the name of the LabVIEW project. If the project has been saved, this property
       returns the filename with the file extension. If the project has not been saved, this
       property returns untitled project x and you can write to this property to change
       the name.

           Note The LabVIEW Datalogging and Supervisory Control Module supports
                 this property in the Run-Time Engine.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read/Write

         Available in Run-Time Engine                                        Yes (Read Only)


9372   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9372 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9373 ordinal=9373 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                      No

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

PathPath

Gets the path to the saved LabVIEW project on disk. This path includes the filename of
the project.

      Note The LabVIEW Datalogging and Supervisory Control Module supports
         this property in the Run-Time Engine.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes


                                                    © National Instruments 9373

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9373 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9374 ordinal=9374 -->
## Property and Method Reference

Property and Method Reference

   RootRoot

       Returns a reference to the project root in the Project Explorer window. The project root
         is the top item that represents the LabVIEW project in the Project Explorer window. You
      can use this reference with the ProjectItem properties.

           Note The LabVIEW Datalogging and Supervisory Control Module supports
                 this property in the Run-Time Engine.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Application Control\VI Server\
        Manipulating Projects\Add Files to Project.vi


9374   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9374 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9375 ordinal=9375 -->
## Property and Method Reference

Property and Method Reference

SelectedSelected ItemsItems inin TreeTree

Returns an array of references to the project items currently selected in the Project
Explorer window. You can use these references with the ProjectItem properties.

      Note The LabVIEW Datalogging and Supervisory Control Module supports
         this property in the Run-Time Engine.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

TargetsTargets

Returns an array of references to all targets in the current LabVIEW project. You can use
these references with the TargetItem properties.

      Note The LabVIEW Datalogging and Supervisory Control Module supports
         this property in the Run-Time Engine.


                                                    © National Instruments 9375

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9375 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9376 ordinal=9376 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

   WindowWindow StateState

       Returns the state of the Project Explorer window.


          Invalid     0  If you read this property and an error occurs, the property returns this value.

        Standard   1 The Project Explorer window is open but is not minimized, maximized, or hidden.

        Closed     2 The Project Explorer window is not open.

                    The Project Explorer window is floating but is not visible because LabVIEW is not the
        Hidden    3
                         active application.

        Minimized  4 The Project Explorer window is minimized.

        Maximized 5 The Project Explorer window is maximized.

           Note The LabVIEW Datalogging and Supervisory Control Module supports
                 this property in the Run-Time Engine.


9376   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9376 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9377 ordinal=9377 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

ProjectItemProjectItem

ProjectItem Methods

ProjectItem Properties

ProjectItemProjectItem MethodsMethods


 Method      Description

            Adds a file at the specified path to the LabVIEW project with the referenced project
 Add File      item as the parent. You also can use the Project Explorer window to add a file to a
                project.

            Adds a new project item of the specified type to the LabVIEW project with the
 Add Item     referenced item as the parent. You also can use the Project Explorer window to add
            an item to a project.

 Add Item
            Adds an item that exists in memory to the LabVIEW project with the referenced
 From
               project item as the parent.
 Memory

 Collapse     Hides the contents of an expandable project item in the Project Explorer window.


                                                    © National Instruments 9377

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9377 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9378 ordinal=9378 -->
## Property and Method Reference

Property and Method Reference


       Method      Description

                    Expandable project items include folders, project libraries, LabVIEW classes, and
                       XControls.

        Convert to
         Auto-                    Connect this project item to a folder on disk.
         populating
         Folder

                  Removes the referenced project item from the LabVIEW project. If the item has
         Delete        children, the children also are deleted. You also can use the Project Explorer window
                       to remove items from the project.

                       Displays the contents of an expandable project item in the Project Explorer window.
        Expand      Expandable project items include folders, project libraries, LabVIEW classes, and
                       XControls.

                       Recursively returns project items that appear under the referenced item in the
        Get All        project tree. For example, if you call this method on project library A that contains an
        Descendents  inner project library B, the method returns items owned both by library A and library
                        B.

                     Replace a project item with a chosen file. The default value of "Allow If Missing?" is
        Replace      FALSE. The default value of "Save Option" is "Save All Without Prompts". The
        Item With    "Modified VIs" will return an array of references to the modified VIs. The "Modified
                         Libraries" will return an array of references to the modified Libraries.

        Stop Auto-
                      Disconnect this folder from a folder on disk.         populating

         Tag:Delete   Removes the named tag from the LabVIEW project item.

         Tag:Get                      Returns an array of tag names of all tags on the referenced project item.       Names

         Tag:Get Tag   Returns a tag value associated with the project item.

         Tag:Get XML
                      Returns the value in an XML tag.
        Tag

         Tag:Set Tag   Sets a tag value associated with the LabVIEW project.

         Tag:Set XML
                       Sets the value of an XML tag associated with the LabVIEW project.
        Tag


9378   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9378 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9379 ordinal=9379 -->
## Property and Method Reference

Property and Method Reference

AddAdd FileFile

Adds a file at the specified path to the LabVIEW project with the referenced project
item as the parent. You also can use the Project Explorer window to add a file to a
project.

      Note The LabVIEW Datalogging and Supervisory Control Module supports
         this method in the Run-Time Engine.

Parameters

 Name     Data type       Required        Description

 Path                        Yes             Path to the file you want to add.


Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                         No

 Available in Real-Time Operating System                                 No

 Settable when the VI is running                                        No

 Loads the front panel into memory                                     No

 Need to authenticate before use                                       No

 Loads the block diagram into memory                                   No

 Remote access allowed                                                           Yes

Examples

Refer to the following example files included with LabVIEW.


                                                    © National Instruments 9379

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9379 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9380 ordinal=9380 -->
## Property and Method Reference

Property and Method Reference

            • labview\examples\Application Control\VI Server\
        Manipulating Projects\Add Files to Project.vi
   AddAdd ItemItem

      Adds a new project item of the specified type to the LabVIEW project with the
       referenced item as the parent. You also can use the Project Explorer window to add an
      item to a project.

       This method returns an error if the specified type cannot be created under the current
       item. The method also returns an error when you try to add a shared variable to a
        library that is not opened in a project.

           Note The LabVIEW Datalogging and Supervisory Control Module supports
                 this method in the Run-Time Engine.

     Parameters

              Data      Name       Required  Description               type

      Name        Yes     Name of the project item you want to add.


        Path         Yes       Path to the project item you want to add.

                                   Specifies the project item type. The following values are the most
                       common Type values:

                                                  • VI
                                                  • Folder
        Type         Yes              • Library
                                                  • XControl
                                                  • EXE
                                                  • DLL
                                                  • Source Distribution


9380   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9380 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9381 ordinal=9381 -->
## Property and Method Reference

Property and Method Reference


       Data Name       Required  Description
       type

                                       • Installer
                                       • Zip File
                                       • Hyperlink

                  Some of the values listed above are supported only on certain LabVIEW
                     Development Systems. Refer to ni.com/labview for more information
                      about LabVIEW Development Systems.

                     To determine the value of Type for a project item that is not listed above,
                      use the Type String property to programmatically return the type of the
                         item.


Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                         No

 Available in Real-Time Operating System                                 No

 Settable when the VI is running                                        No

 Loads the front panel into memory                                     No

 Need to authenticate before use                                       No

 Loads the block diagram into memory                                   No

 Remote access allowed                                                           Yes

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Application Control\VI Server\
   Manipulating Projects\Add Files to Project.vi


                                                    © National Instruments 9381

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9381 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9382 ordinal=9382 -->
## Property and Method Reference

Property and Method Reference

   AddAdd ItemItem FromFrom MemoryMemory

      Adds an item that exists in memory to the LabVIEW project with the referenced project
      item as the parent.

           Note The LabVIEW Datalogging and Supervisory Control Module supports
                 this method in the Run-Time Engine.

     Parameters

              Data      Name          Required  Description
               type

                          Name that exists in memory, such as foo.vi, of the project item you      Name           Yes
                              want to add.


     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                         No

         Available in Real-Time Operating System                                 No

         Settable when the VI is running                                        No

        Loads the front panel into memory                                     No

       Need to authenticate before use                                       No

        Loads the block diagram into memory                                   No

       Remote access allowed                                                           Yes


9382   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9382 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9383 ordinal=9383 -->
## Property and Method Reference

Property and Method Reference

CollapseCollapse

Hides the contents of an expandable project item in the Project Explorer window.
Expandable project items include folders, project libraries, LabVIEW classes, and
XControls.

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                              No

 Available in Real-Time Operating System                      No

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

ConvertConvert toto Auto-populatingAuto-populating FolderFolder

Connect this project item to a folder on disk.

This property is similar to the Convert to Auto-populating Folder item on the shortcut
menu of a virtual folder in the project.

Parameters

 Name     Data type       Required        Description

 Path                        Yes             Path to the file you want to add.


                                                    © National Instruments 9383

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9383 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9384 ordinal=9384 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

    DeleteDelete

      Removes the referenced project item from the LabVIEW project. If the item has
       children, the children also are deleted. You also can use the Project Explorer window to
      remove items from the project.

           Note The LabVIEW Datalogging and Supervisory Control Module supports
                 this method in the Run-Time Engine.

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

9384   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9384 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9385 ordinal=9385 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

ExpandExpand

Displays the contents of an expandable project item in the Project Explorer window.
Expandable project items include folders, project libraries, LabVIEW classes, and
XControls.

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                              No

 Available in Real-Time Operating System                      No

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

GetGet AllAll DescendentsDescendents

Recursively returns project items that appear under the referenced item in the project
tree. For example, if you call this method on project library A that contains an inner
project library B, the method returns items owned both by library A and library B.

For this method, the term descendents does notrefer to children classes of the
referenced project item.


                                                    © National Instruments 9385

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9385 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9386 ordinal=9386 -->
## Property and Method Reference

Property and Method Reference

     Parameters

                            Data      Name                     Required  Description
                             type

                                                   Specifies which kind of project items this method returns.
                                        The following values are the most common Type values:

                                                                        • VI—Most VI types, such as ordinary VIs, polymorphic
                                                               VIs, control VIs, and global VIs
                                                                        • Library
                                                                        • LVLibp—Packed project libraries
                                                                        • LVClass—LabVIEW classes
                                                                        • Class Private Data—private data control of a
                                            LabVIEW class
                                                                        • XControl—XControl libraries
                                                                        • Ability VI—VI within an XControl
                                                                        • Folder

                                          To determine the value of Type for a project item that is
        Type                  No       not listed above, use the Type String property to
                                             programmatically return the type of the item.

                                                This method checks for exact matches to the Type you
                                                      specify. For example, if you specify a Type of Library,
                                                      this method returns only .lvlib project items, not
                                         LabVIEW classes or XControls. Furthermore, if you specify
                                          a Type of VI, the method does not return private data
                                                 controls or XControl VIs because these specialized VIs
                                          have their own type.

                                   Some of the values listed above are supported only on
                                                   certain LabVIEW Development Systems. Refer to ni.com/
                                             labview for more information about LabVIEW
                                         Development Systems.


                                                   Specifies whether to ignore items under the
                                   Dependencies folder if the referenced item is a project.
        ExcludeDependencies      No            If the referenced item is a target, this input specifies
                                          whether to exclude items under the target. If the
                                               referenced item is neither a project nor a target, this input


9386   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9386 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9387 ordinal=9387 -->
## Property and Method Reference

Property and Method Reference


                     Data Name                     Required  Description
                     type

                                    has no effect on the output of this method.


                                                               If TRUE, does not return Build Specifications or any items ExcludeBuilds           No                                   under Build Specifications. The default is FALSE.


                                                               If TRUE, does not return any targets or any items under ExcludeTargets           No
                                             targets. The default is FALSE.


Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                                      Yes

 Available in Real-Time Operating System                                 No

 Settable when the VI is running                                        No

 Loads the front panel into memory                                     No

 Need to authenticate before use                                       No

 Loads the block diagram into memory                                   No

 Remote access allowed                                                           Yes

ReplaceReplace ItemItem WithWith

Replace a project item with a chosen file. The default value of "Allow If Missing?" is
FALSE. The default value of "Save Option" is "Save All Without Prompts". The "Modified
VIs" will return an array of references to the modified VIs. The "Modified Libraries" will
return an array of references to the modified Libraries.


                                                    © National Instruments 9387

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9387 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9388 ordinal=9388 -->
## Property and Method Reference

Property and Method Reference

     Parameters

      Name                         Data type         Required          Description

        Replacement Path                                    Yes

        Allow If Missing?                            No

        Save Option                               No

         Modified VIs                               No

         Modified Libraries                           No

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

   StopStop Auto-populatingAuto-populating

       Disconnect this folder from a folder on disk.

       This property is similar to the Stop Auto-populating item on the shortcut menu of an
       auto-populating folder in the project.

     Remarks

      The following table lists the characteristics of this method.

9388   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9388 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9389 ordinal=9389 -->
## Property and Method Reference

Property and Method Reference


 Data type                                            No return value

 Available in Run-Time Engine                              No

 Available in Real-Time Operating System                      No

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

Tag:DeleteTag:Delete

Removes the named tag from the LabVIEW project item.

      Note The LabVIEW Datalogging and Supervisory Control Module supports
         this method in the Run-Time Engine.

Parameters

          Data Name             Required  Description
          type

 Tag                   Name of the tag. Use the Tag:Get Names method to retrieve the tag
                    Yes
 Name                     names.


Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                         No


                                                    © National Instruments 9389

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9389 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9390 ordinal=9390 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                                 No

         Settable when the VI is running                                        No

        Loads the front panel into memory                                     No

       Need to authenticate before use                                       No

        Loads the block diagram into memory                                   No

       Remote access allowed                                                           Yes

    Tag:GetTag:Get NamesNames

       Returns an array of tag names of all tags on the referenced project item.

           Note The LabVIEW Datalogging and Supervisory Control Module supports
                 this method in the Run-Time Engine.

     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                                      Yes

         Available in Real-Time Operating System                                 No

         Settable when the VI is running                                        No

        Loads the front panel into memory                                     No

       Need to authenticate before use                                       No

        Loads the block diagram into memory                                   No

       Remote access allowed                                                           Yes

    Tag:GetTag:Get TagTag

       Returns a tag value associated with the project item.

9390   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9390 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9391 ordinal=9391 -->
## Property and Method Reference

Property and Method Reference

      Note The LabVIEW Datalogging and Supervisory Control Module supports
         this method in the Run-Time Engine.

Parameters

          Data Name           Required  Description           type

                     Name of the tag. Use the Tag:Get Names method to retrieve the tag Tag Name        Yes
                         names.


 Value            Yes       Returns the tag value as a variant.


 Is                         Returns TRUE if LabVIEW saves the tag information when you save                  Yes Persistent                  the LabVIEW project. Returns FALSE otherwise.


Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                                      Yes

 Available in Real-Time Operating System                                 No

 Settable when the VI is running                                        No

 Loads the front panel into memory                                     No

 Need to authenticate before use                                       No

 Loads the block diagram into memory                                   No

 Remote access allowed                                                           Yes


                                                    © National Instruments 9391

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9391 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9392 ordinal=9392 -->
## Property and Method Reference

Property and Method Reference

    Tag:GetTag:Get XMLXML TagTag

       Returns the value in an XML tag.

      Use the Tag:Set XML Tag method to set the value in an XML tag.

           Note The LabVIEW Datalogging and Supervisory Control Module supports
                 this method in the Run-Time Engine.

     Parameters

                  Data
      Name           Required  Description                  type

                          Name of the tag. Use the Tag:Get Names method to retrieve the tag
        Tag Name        Yes                                names.


         Value            Yes       Returns the value of the XML tag as a string.


           Is                         Returns TRUE if LabVIEW saves the tag information when you save                          Yes         Persistent                  the LabVIEW project. Returns FALSE otherwise.


     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                                      Yes

         Available in Real-Time Operating System                                 No

         Settable when the VI is running                                        No

        Loads the front panel into memory                                     No


9392   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9392 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9393 ordinal=9393 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                                       No

 Loads the block diagram into memory                                   No

 Remote access allowed                                                           Yes

Tag:SetTag:Set TagTag

Sets a tag value associated with the LabVIEW project.

      Note The LabVIEW Datalogging and Supervisory Control Module supports
         this method in the Run-Time Engine.

Parameters

           Data
 Name            Required  Description           type

                     Name of the tag. Use the Tag:Get Names method to retrieve the tag
 Tag Name         Yes                          names.


 Value             Yes        Specifies the tag value as a variant.


 Is                                               If TRUE, LabVIEW saves the tag information when you save the
 Persistent       No
                         LabVIEW project. The default is FALSE.
 (T)

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                              No

 Available in Real-Time Operating System                      No

                                                    © National Instruments 9393

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9393 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9394 ordinal=9394 -->
## Property and Method Reference

Property and Method Reference


         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

    Tag:SetTag:Set XMLXML TagTag

       Sets the value of an XML tag associated with the LabVIEW project.

           Note The LabVIEW Datalogging and Supervisory Control Module supports
                 this method in the Run-Time Engine.

     Parameters

                  Data
      Name            Required  Description                  type

                           Name of the tag. Use the Tag:Get Names method to retrieve the tag
        Tag Name         Yes                                 names.


         Value             Yes        Specifies the value of the XML tag as a string.


           Is                                           If TRUE, LabVIEW saves the tag information when you save the
                    No
         Persistent                 LabVIEW project. The default is FALSE.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

9394   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9394 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9395 ordinal=9395 -->
## Property and Method Reference

Property and Method Reference


 Available in Run-Time Engine                              No

 Available in Real-Time Operating System                      No

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

ProjectItemProjectItem PropertiesProperties


 Property      Description

 Can Be        Private method to determine whether an item can be replaced by another item in
 Replaced      the project.

 Contains      Returns TRUE if this item or items beneath this item in the project tree are in
 Conflicts?      conflict.

               Gets as a string the name of the project item as the name appears in the Project Display Name                Explorer window.

               Applicable in IIO only. Tasks and program VIs can be set to Enabled, in which case Enabled               they will be deployed and run on the Controller.

               Returns an array of references to all project items that reference the project item Find:Callers             you select.

               Returns an array of references to all project items that are children of the project Find:Children
              item you select.

               Returns an array of references to all project items that are in conflict with the
 Find:Conflicts
                project item you select.

               Returns an array of references to all project items that are friends of the project item
 Find:Friends
             you select.

 Find:Items
 Incorrectly    Returns an array of references to all items within a project that are claimed by a
 Claimed by a   library but do not reciprocate the claim.
 Library

 Find:Items    Returns an array of references to all project items under the target that are not
 that make    under dependencies but cause this item to be under dependencies.

                                                    © National Instruments 9395

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9395 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9396 ordinal=9396 -->
## Property and Method Reference

Property and Method Reference


        Property      Description

          this a
        dependency

         Find:Items                      Returns an array of references to all top-level project items that call no other project        with No                        items.
          Callers

         Find:Missing                      Returns all project items that have a path but do not exist on disk.        Items

                      Returns an array of references to all project items that are subVIs of the item you         Find:SubVIs
                           select.

         Find:Variable  Returns an array of references to all project VIs that reference the shared variable
          Callers        project item you specify.

        Get Auto-
         populating    Returns the path on disk this auto-populating folder is connected to.
         Folder Path

        HyperLink                      Gets or sets the address of a hyperlink item.
        Address

                      Gets the icon of the project item in the Project Explorer window using the Icon
         Icon                           cluster, which limits size and color depth.

                      Returns TRUE if this item conflicts with another item with a different path under the
          In Conflict?                  same target.

           Is In Packed
                      Returns TRUE if a packed project library contains the project item.         Library

                      Gets the item ID of the referenced project item as a string. You can use this item ID to
        Item ID        uniquely identify the referenced item even if the path, name, or location in the
                        Project Explorer window changes.

                      Returns the type of the project item as it exists in the project library as a string. This
         Library Item
                       property returns an error if the project item is not part of a library. Use the Library
         Type:String
                      Item:Type property to return the type as a GUID.

                      Gets the type of the project item as it exists in the project library as a GUID string. If
         Library
                       the item is not part of a library, this property returns an error. Use the Library Item
        Item:Type
                        Type:String property to return the type as a human-readable string.

      Name         Gets the name of the referenced project item as it is saved in the file.

       Owned       Returns an array of references to the contents of the referenced project item. You
         Items[]       can use these references with the ProjectItem properties.

9396   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9396 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9397 ordinal=9397 -->
## Property and Method Reference

Property and Method Reference


 Property      Description

               Returns a reference to the project item that contains the referenced project item in
 Owner        the Project Explorer window. You can use this reference with the ProjectItem
                properties.

 Path          Gets the path of the referenced project item.

               Returns a reference to the LabVIEW project to which the referenced project item Project               belongs. You can use this reference with the Project properties.

               Returns a reference to the target that contains the referenced project item. You can Target              use this reference with the TargetItem properties.

               Gets the type of the project item as a GUID string. Use the Type String property to Type GUID                return the type as a string.

               Gets the type of the project item as a string. Use the Type GUID property to return Type String
               the type as a GUID.

                        If the project item refers to a VI, this property returns a reference to the VI.
 VI Reference   Otherwise, this property returns Not a Refnum. You can use this reference with
               the VI properties.

                        If the project item refers to a VI in memory, this property returns a reference to the
 VI Reference    VI. If the project item refers to a VI not in memory or to something that is not a VI,
 No Load        this property returns Not a Refnum. You can use this reference with the VI
                properties.

               Returns a reference to the variable the referenced project item references. If the
 Variable       referenced project item is not a variable item, this property returns Not a
 Reference    Refnum. You can use this reference with the Variable properties to configure shared
                variables programmatically.

                        If TRUE, indicates that the Project Explorer window is visible and ancestors of the Visible In
                project item are expanded in the Project Explorer window up to the root of the
 Tree
                project item.

CanCan BeBe ReplacedReplaced

Private method to determine whether an item can be replaced by another item in the
project.


                                                    © National Instruments 9397

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9397 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9398 ordinal=9398 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                                   Yes

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

   ContainsContains Conflicts?Conflicts?

       Returns TRUE if this item or items beneath this item in the project tree are in conflict.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No


9398   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9398 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9399 ordinal=9399 -->
## Property and Method Reference

Property and Method Reference


 Remote access allowed                                                   Yes

DisplayDisplay NameName

Gets as a string the name of the project item as the name appears in the Project
Explorer window.

      Note The LabVIEW Datalogging and Supervisory Control Module supports
         this property in the Run-Time Engine.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

EnabledEnabled

Applicable in IIO only. Tasks and program VIs can be set to Enabled, in which case they
will be deployed and run on the Controller.


                                                    © National Instruments 9399

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9399 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9400 ordinal=9400 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                 No

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    Find:CallersFind:Callers

       Returns an array of references to all project items that reference the project item you
        select.

       This property is similar to the Find»Callers item on the shortcut menu of a project
       item.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No


9400   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9400 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9401 ordinal=9401 -->
## Property and Method Reference

Property and Method Reference


 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

Find:ChildrenFind:Children

Returns an array of references to all project items that are children of the project item
you select.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

Find:ConflictsFind:Conflicts

Returns an array of references to all project items that are in conflict with the project
item you select.

This property is similar to the Find»Conflicts item on the shortcut menu of a project
item.

                                                    © National Instruments 9401

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9401 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9402 ordinal=9402 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

    Find:FriendsFind:Friends

       Returns an array of references to all project items that are friends of the project item
      you select.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No


9402   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9402 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9403 ordinal=9403 -->
## Property and Method Reference

Property and Method Reference


 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

Find:ItemsFind:Items IncorrectlyIncorrectly ClaimedClaimed byby aa LibraryLibrary

Returns an array of references to all items within a project that are claimed by a library
but do not reciprocate the claim.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

Find:ItemsFind:Items thatthat makemake thisthis aa dependencydependency

Returns an array of references to all project items under the target that are not under
dependencies but cause this item to be under dependencies.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 9403

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9403 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9404 ordinal=9404 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

    Find:ItemsFind:Items withwith NoNo CallersCallers

       Returns an array of references to all top-level project items that call no other project
       items.

       This property is similar to the Find»Items with No Callers item on the shortcut menu
       of a project item.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No


9404   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9404 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9405 ordinal=9405 -->
## Property and Method Reference

Property and Method Reference


 Remote access allowed                                                   Yes

Find:MissingFind:Missing ItemsItems

Returns all project items that have a path but do not exist on disk.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

Find:SubVIsFind:SubVIs

Returns an array of references to all project items that are subVIs of the item you
select.

This property is similar to the Find»SubVIs item on the shortcut menu of a project
item.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 9405

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9405 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9406 ordinal=9406 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

    Find:VariableFind:Variable CallersCallers

       Returns an array of references to all project VIs that reference the shared variable
       project item you specify.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes


9406   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9406 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9407 ordinal=9407 -->
## Property and Method Reference

Property and Method Reference

GetGet Auto-populatingAuto-populating FolderFolder PathPath

Returns the path on disk this auto-populating folder is connected to.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

HyperLinkHyperLink AddressAddress

Gets or sets the address of a hyperlink item.

This property is similar to the options available in the Hyperlink Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read/Write

 Available in Run-Time Engine                                        Yes (Read Only)


                                                    © National Instruments 9407

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9407 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9408 ordinal=9408 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                      No

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

    IconIcon

       Gets the icon of the project item in the Project Explorer window using the Icon cluster,
      which limits size and color depth.

           Note The LabVIEW Datalogging and Supervisory Control Module supports
                 this property in the Run-Time Engine.

     Elements

      Name     Description

        Image                  Reserved for future use.        Type

                     Specifies the color depth of the image, which is the number of bits to use to describe
        Image                   the color of each pixel in the image. Valid values include 1, 4, 8, and 24 bits per pixel.        Depth
                 Image Depth affects how LabVIEW interprets the values of Image and Colors.

                A 1-D array of bytes that describes the color of each pixel in the image in raster order.
                 The value of Image Depth determines how LabVIEW interprets the value of this input.

                               If Image Depth is 24, each pixel has three bytes to describe its color. The first byte for
        Image    each pixel describes the red value, the second byte describes the green value, and the
                      third byte describes the blue value.

                               If Image Depth is 8, each pixel has one byte to describe its color. The value of each bit
                  corresponds to an element in Colors, which stores 32-bit RGB values where the most-


9408   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9408 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9409 ordinal=9409 -->
## Property and Method Reference

Property and Method Reference


Name     Description

            significant byte is zero, followed in order by red, green, and blue values. Valid values
           include 0 through 255.

                 If Image Depth is 4, the behavior is similar to when Image Depth is 8 except valid values
            in image include 0 through 15.

                 If Image Depth is 1, any value of zero in Image corresponds to element 0 in Colors. All
           other values correspond to element 1 in Colors.

         An array of bytes in which each bit describes mask information for a pixel. The first byte
           describes the first eight pixels, the second byte describes the next eight pixels, and so
           on. If a bit is zero, LabVIEW draws the corresponding pixel as transparent. If the array isMask
          empty, LabVIEW draws all pixels without transparency. If the array does not contain a bit
            for each pixel in the image, LabVIEW draws any pixels missing from the array without
           transparency.

         An array of RGB color values that correspond to the values in image. The value of Image
          Depth determines how LabVIEW interprets the value of this input.

                 If Image Depth is 24, LabVIEW ignores this input.
Colors                 If Image Depth is 8, the array can have 256 elements.

                 If Image Depth is 4, the array can have 16 elements.

                 If Image Depth is 1, the array can have 2 elements.

         A cluster that contains coordinates that describe the bounding rectangle in which you
         want to draw the image. The VI clips the image to the width and height of the rectangle.
         The bottom and right edges of the rectangle bounds do not contain image pixels.
           Horizontal coordinates increase to the right, and vertical coordinates increase to the
          bottom.
Rectangle
                   • Left—The horizontal coordinate of the left edge of the rectangle.
                   • Top—The vertical coordinate of the top edge of the rectangle.
                   • Right—The horizontal coordinate of the right edge of the rectangle.
                   • Bottom—The vertical coordinate of the bottom edge of the rectangle.


                                                    © National Instruments 9409

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9409 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9410 ordinal=9410 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

    InIn Conflict?Conflict?

       Returns TRUE if this item conflicts with another item with a different path under the
     same target.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No


9410   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9410 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9411 ordinal=9411 -->
## Property and Method Reference

Property and Method Reference


 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

IsIs InIn PackedPacked LibraryLibrary

Returns TRUE if a packed project library contains the project item.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

ItemItem IDID

Gets the item ID of the referenced project item as a string. You can use this item ID to
uniquely identify the referenced item even if the path, name, or location in the Project
Explorer window changes.

      Note The LabVIEW Datalogging and Supervisory Control Module supports
         this property in the Run-Time Engine.


                                                    © National Instruments 9411

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9411 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9412 ordinal=9412 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

    LibraryLibrary ItemItem Type:StringType:String

       Returns the type of the project item as it exists in the project library as a string. This
       property returns an error if the project item is not part of a library. Use the Library
       Item:Type property to return the type as a GUID.

           Note The LabVIEW Datalogging and Supervisory Control Module supports
                 this property in the Run-Time Engine.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                           No

9412   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9412 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9413 ordinal=9413 -->
## Property and Method Reference

Property and Method Reference


 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

LibraryLibrary Item:TypeItem:Type

Gets the type of the project item as it exists in the project library as a GUID string. If the
item is not part of a library, this property returns an error. Use the Library Item
Type:String property to return the type as a human-readable string.

      Note The LabVIEW Datalogging and Supervisory Control Module supports
         this property in the Run-Time Engine.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes


                                                    © National Instruments 9413

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9413 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9414 ordinal=9414 -->
## Property and Method Reference

Property and Method Reference

   NameName

       Gets the name of the referenced project item as it is saved in the file.

      Use the Display Name property to get the name as it appears in the Project Explorer
      window.

           Note The LabVIEW Datalogging and Supervisory Control Module supports
                 this property in the Run-Time Engine.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

   OwnedOwned Items[]Items[]

       Returns an array of references to the contents of the referenced project item. You can
      use these references with the ProjectItem properties.

           Note The LabVIEW Datalogging and Supervisory Control Module supports


9414   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9414 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9415 ordinal=9415 -->
## Property and Method Reference

Property and Method Reference


         this property in the Run-Time Engine.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Application Control\VI Server\
   Manipulating Projects\Add Files to Project.vi
OwnerOwner

Returns a reference to the project item that contains the referenced project item in the
Project Explorer window. You can use this reference with the ProjectItem properties.

      Note The LabVIEW Datalogging and Supervisory Control Module supports
         this property in the Run-Time Engine.


                                                    © National Instruments 9415

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9415 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9416 ordinal=9416 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

   PathPath

       Gets the path of the referenced project item.

           Note The LabVIEW Datalogging and Supervisory Control Module supports
                 this property in the Run-Time Engine.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No


9416   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9416 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9417 ordinal=9417 -->
## Property and Method Reference

Property and Method Reference


 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

ProjectProject

Returns a reference to the LabVIEW project to which the referenced project item
belongs. You can use this reference with the Project properties.

      Note The LabVIEW Datalogging and Supervisory Control Module supports
         this property in the Run-Time Engine.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

TargetTarget

Returns a reference to the target that contains the referenced project item. You can use

                                                    © National Instruments 9417

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9417 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9418 ordinal=9418 -->
## Property and Method Reference

Property and Method Reference

        this reference with the TargetItem properties.

           Note The LabVIEW Datalogging and Supervisory Control Module supports
                 this property in the Run-Time Engine.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

   TypeType GUIDGUID

       Gets the type of the project item as a GUID string. Use the Type String property to
       return the type as a string.

           Note The LabVIEW Datalogging and Supervisory Control Module supports
                 this property in the Run-Time Engine.

     Remarks

      The following table lists the characteristics of this property.


9418   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9418 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9419 ordinal=9419 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

TypeType StringString

Gets the type of the project item as a string. Use the Type GUID property to return the
type as a GUID.

      Note The LabVIEW Datalogging and Supervisory Control Module supports
         this property in the Run-Time Engine.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No


                                                    © National Instruments 9419

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9419 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9420 ordinal=9420 -->
## Property and Method Reference

Property and Method Reference


        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

    VIVI ReferenceReference

           If the project item refers to a VI, this property returns a reference to the VI. Otherwise,
        this property returns Not a Refnum. You can use this reference with the VI
       properties.

           Note The VI Reference does not record changes to the VI. If you use this
               reference for editing the VI, you will not be prompted to save when the
               reference closes.

           Note The LabVIEW Datalogging and Supervisory Control Module supports
                 this property in the Run-Time Engine.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes


9420   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9420 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9421 ordinal=9421 -->
## Property and Method Reference

Property and Method Reference

VIVI ReferenceReference NoNo LoadLoad

If the project item refers to a VI in memory, this property returns a reference to the VI. If
the project item refers to a VI not in memory or to something that is not a VI, this
property returns Not a Refnum. You can use this reference with the VI properties.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

VariableVariable ReferenceReference

Returns a reference to the variable the referenced project item references. If the
referenced project item is not a variable item, this property returns Not a Refnum.
You can use this reference with the Variable properties to configure shared variables
programmatically.

      Note You can create, configure, and host shared variables only on Windows
        or RT targets with the LabVIEW Real Time Module. You can use the
       DataSocket VI and functions to read or write shared variables from other
        platforms.


                                                    © National Instruments 9421

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9421 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9422 ordinal=9422 -->
## Property and Method Reference

Property and Method Reference

           Note The LabVIEW Datalogging and Supervisory Control Module supports
                 this property in the Run-Time Engine.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

    VisibleVisible InIn TreeTree

           If TRUE, indicates that the Project Explorer window is visible and ancestors of the
       project item are expanded in the Project Explorer window up to the root of the project
       item.

           Note The LabVIEW Datalogging and Supervisory Control Module supports
                 this property in the Run-Time Engine.

     Remarks

      The following table lists the characteristics of this property.


        Data type

9422   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9422 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9423 ordinal=9423 -->
## Property and Method Reference

Property and Method Reference


 Permissions                                                     Read Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

LibraryLibrary

Library Methods

Library Properties
LibraryLibrary MethodsMethods

Use these methods to configure LabVIEW project libraries.


 Method         Description

                  Applies the icon for a library to the icons of all objects in the library. You can use
 Apply Icon To     this method to update the icons for objects in a library after you edit the library
 Existing VI        icon. This method loads member objects of the library into memory if they are
 Items           not already in memory. Callers might be prompted to provide VI passwords or to
                save the loaded VIs.

 Disconnect      Disconnects a LabVIEW project library that is a sublibrary of another project
 From Library     library from the owning project library.

 Disconnect
 Variables From   Disconnects variables in the library from type definitions.
 Typedefs

 Friends:Add
               Adds a friend to the list of friends of this library.
 Friend Library

 Friends:Add     Adds a friend to the list of friends of this library.

                                                    © National Instruments 9423

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9423 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9424 ordinal=9424 -->
## Property and Method Reference

Property and Method Reference


       Method         Description

         Friend VI

        Friends:Remove
        Friended VI or   Removes a friend from the list of friends of this library.
         Library

                     Shows this library in a project window. If the library is already in a project
                      window, this will show the project window and set focus to the library item in the
           Hilite In Project  project. If the library is already in a library-only project window for which it is the
       Window         root item, this will show the library-only project window. If the library is not in any
                           project window, this will open a library-only project window containing the
                               library.

         Icon:Get         Retrieves the icon associated with a LabVIEW project library.

         Icon:Set         Sets the icon for a project library from image data you specify.

         Library                          Deletes a tag from the LabVIEW project library.
         Tag:Delete

         Library Tag:Get   Retrieves a tag set on the LabVIEW project library.

         Library Tag:Get                          Retrieves a list of names for all tags set on the LabVIEW project library.       Names

         Library Tag:Set   Sets a tag on the LabVIEW project library.

                        Returns the lock state of the LabVIEW project library and indicates whether the
        Lock State:Get                      password for the project library is in the password cache.

                          Sets the level of editing permission for a LabVIEW project library, including the
        Lock State:Set                        password.

        Save:Copy      Saves a copy of the LabVIEW project library file.

                       Saves a copy of the project library and all items within the project library that is
         Save:For
                         readable by LabVIEW 8.0 and later. This method is similar to the LabVIEW Version
         Previous
                           selection on the Save for Previous Version dialog box.

                       Saves the LabVIEW project library file. You also can right-click the project library
         Save:Library      in the Project Explorer window and select Save As from the shortcut menu to
                        save the project library file.

        Source           Retrieves the access scope for an item that the LabVIEW project library owns,
        Scope:Get      such as public or private access.

        Source          Sets the access scope of an item that the LabVIEW project library owns, such as
        Scope:Set       public or private access.


9424   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9424 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9425 ordinal=9425 -->
## Property and Method Reference

Property and Method Reference


 Method         Description

 Source          Sets the access scope of an item that the LabVIEW project library owns, such as
 Scope:Set and   public or private access. If the item is a dynamic dispatch VI, LabVIEW also
 Propagate      changes the scope of other implementations.

ApplyApply IconIcon ToTo ExistingExisting VIVI ItemsItems

Applies the icon for a library to the icons of all objects in the library. You can use this
method to update the icons for objects in a library after you edit the library icon. This
method loads member objects of the library into memory if they are not already in
memory. Callers might be prompted to provide VI passwords or to save the loaded VIs.

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                              No

 Available in Real-Time Operating System                      No

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

DisconnectDisconnect FromFrom LibraryLibrary

Disconnects a LabVIEW project library that is a sublibrary of another project library
from the owning project library.

      Note The LabVIEW Datalogging and Supervisory Control Module supports


                                                    © National Instruments 9425

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9425 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9426 ordinal=9426 -->
## Property and Method Reference

Property and Method Reference


                 this method in the Run-Time Engine.

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

   DisconnectDisconnect VariablesVariables FromFrom TypedefsTypedefs

       Disconnects variables in the library from type definitions.

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No


9426   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9426 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9427 ordinal=9427 -->
## Property and Method Reference

Property and Method Reference


 Remote access allowed                                             Yes

Friends:AddFriends:Add FriendFriend LibraryLibrary

Adds a friend to the list of friends of this library.

Parameters

 Name            Data type    Required    Description

 Library To Add              No          Reference to the library you want to add.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                              No

 Available in Real-Time Operating System                      No

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

Friends:AddFriends:Add FriendFriend VIVI

Adds a friend to the list of friends of this library.


                                                    © National Instruments 9427

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9427 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9428 ordinal=9428 -->
## Property and Method Reference

Property and Method Reference

     Parameters

      Name        Data type      Required      Description

          VI To Add                     Yes           Reference to the VI you want to add.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

   Friends:RemoveFriends:Remove FriendedFriended VIVI oror LibraryLibrary

      Removes a friend from the list of friends of this library.

     Parameters

      Name            Data type   Required   Description

        Item To Remove                Yes         Qualified name of the item you want to remove.


9428   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9428 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9429 ordinal=9429 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                              No

 Available in Real-Time Operating System                      No

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

HiliteHilite InIn ProjectProject WindowWindow

Shows this library in a project window. If the library is already in a project window, this
will show the project window and set focus to the library item in the project. If the
library is already in a library-only project window for which it is the root item, this will
show the library-only project window. If the library is not in any project window, this
will open a library-only project window containing the library.

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                              No

 Available in Real-Time Operating System                      No

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No


                                                    © National Instruments 9429

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9429 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9430 ordinal=9430 -->
## Property and Method Reference

Property and Method Reference


        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

    Icon:GetIcon:Get

       Retrieves the icon associated with a LabVIEW project library.

           Note The LabVIEW Datalogging and Supervisory Control Module supports
                 this method in the Run-Time Engine.

     Parameters

                     Data      Name             Required  Description                     type

                                      Returns the 8-bit library icon. This icon appears as the 256 Colors
         Color               Yes       icon on the General Settings page of the Project Library Properties
                                        dialog box.


       Monochrome        Yes       Returns the 1-bit library icon.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                      No

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

9430   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9430 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9431 ordinal=9431 -->
## Property and Method Reference

Property and Method Reference


 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

Icon:SetIcon:Set

Sets the icon for a project library from image data you specify.

LabVIEW applies a library icon to the icon of all objects in the library. National
Instruments recommends creating only a banner for the library icon. The icon for each
object in the library then includes the banner, and you can modify the body of the icon
to provide information about the specific object.

This method is similar to the VI Icon Template section of the General Settings page of
the Project Library Properties dialog box.

      Note The LabVIEW Datalogging and Supervisory Control Module supports
         this method in the Run-Time Engine.

Parameters

             Data Name             Required  Description
              type

                                 Specifies image data to use as the 8-bit library icon. This icon
 Color               Yes       appears as the 256 Colors icon on the General Settings page of the
                                 Project Library Properties dialog box.


 Monochrome      No        Specifies image data to use as the 1-bit library icon.


Remarks

The following table lists the characteristics of this method.


                                                    © National Instruments 9431

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9431 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9432 ordinal=9432 -->
## Property and Method Reference

Property and Method Reference


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

    LibraryLibrary Tag:DeleteTag:Delete

       Deletes a tag from the LabVIEW project library.

           Note The LabVIEW Datalogging and Supervisory Control Module supports
                 this method in the Run-Time Engine.

     Parameters

      Name      Data type   Required   Description

        Tag Name                Yes          Specifies the name of the tag on the project library.


        Item Ref             No         Contains a reference to the project library.


     Remarks

      The following table lists the characteristics of this method.


        Data type


9432   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9432 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9433 ordinal=9433 -->
## Property and Method Reference

Property and Method Reference


 Available in Run-Time Engine                                         No

 Available in Real-Time Operating System                                 No

 Settable when the VI is running                                        No

 Loads the front panel into memory                                     No

 Need to authenticate before use                                       No

 Loads the block diagram into memory                                   No

 Remote access allowed                                                           Yes

LibraryLibrary Tag:GetTag:Get

Retrieves a tag set on the LabVIEW project library.

      Note The LabVIEW Datalogging and Supervisory Control Module supports
         this method in the Run-Time Engine.

Parameters

            Data Name                Required  Description            type

 Tag Name             Yes        Specifies the name of the tag on the project library.


 Value                 Yes       Returns the value of the tag.


 Is                              Returns TRUE if you save the tag when you save the project
                       Yes
 Persistent                             library.


 Item Ref           No       Contains a reference to the project library.


                                                    © National Instruments 9433

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9433 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9434 ordinal=9434 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                                      Yes

         Available in Real-Time Operating System                                 No

         Settable when the VI is running                                        No

        Loads the front panel into memory                                     No

       Need to authenticate before use                                       No

        Loads the block diagram into memory                                   No

       Remote access allowed                                                           Yes

    LibraryLibrary Tag:GetTag:Get NamesNames

       Retrieves a list of names for all tags set on the LabVIEW project library.

           Note The LabVIEW Datalogging and Supervisory Control Module supports
                 this method in the Run-Time Engine.

     Parameters

      Name      Data type     Required     Description

        Item Ref              No           Contains a reference to the project library.


     Remarks

      The following table lists the characteristics of this method.


        Data type

9434   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9434 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9435 ordinal=9435 -->
## Property and Method Reference

Property and Method Reference


 Available in Run-Time Engine                                                      Yes

 Available in Real-Time Operating System                                 No

 Settable when the VI is running                                        No

 Loads the front panel into memory                                     No

 Need to authenticate before use                                       No

 Loads the block diagram into memory                                   No

 Remote access allowed                                                           Yes

LibraryLibrary Tag:SetTag:Set

Sets a tag on the LabVIEW project library.

      Note The LabVIEW Datalogging and Supervisory Control Module supports
         this method in the Run-Time Engine.

Parameters

          Data Name             Required  Description           type

 Tag Name          Yes        Specifies the name of the tag on the project library.


 Value              Yes        Specifies the value of the tag.


 Is                              Specifies whether the tag is persistent. The default is FALSE, which
               No
 Persistent                            is not persistent.


 Item Ref         No       Contains a reference to the project library.


                                                    © National Instruments 9435

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9435 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9436 ordinal=9436 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

   LockLock State:GetState:Get

       Returns the lock state of the LabVIEW project library and indicates whether the
      password for the project library is in the password cache.

       This method is similar to the Protection page of the Project Library Properties dialog
       box.

           Note The LabVIEW Datalogging and Supervisory Control Module supports
                 this method in the Run-Time Engine.

     Parameters

      Name                    Data type           Required            Description

      pwd in cache                           No

     Remarks

      The following table lists the characteristics of this method.

9436   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9436 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9437 ordinal=9437 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Available in Run-Time Engine                                                      Yes

 Available in Real-Time Operating System                                 No

 Settable when the VI is running                                        No

 Loads the front panel into memory                                     No

 Need to authenticate before use                                       No

 Loads the block diagram into memory                                   No

 Remote access allowed                                                           Yes

LockLock State:SetState:Set

Sets the level of editing permission for a LabVIEW project library, including the
password.

This method is similar to the Protection page of the Project Library Properties dialog
box.

      Note The LabVIEW Datalogging and Supervisory Control Module supports
         this method in the Run-Time Engine.

Parameters

           Data
 Name           Required  Description
           type

                               Specifies the level of editing permission of the project library.

                          0  invalid lock state
 lock state         Yes
                            Not locked—Users can view public and private items that the
                          1  project library owns and can edit the project library and its
                                  properties.


                                                    © National Instruments 9437

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9437 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9438 ordinal=9438 -->
## Property and Method Reference

Property and Method Reference


                  Data      Name           Required  Description
                   type


                                   Locked (no password)—Users cannot add or remove items from
                                  2 the project library, edit project library properties, or view private
                                       items that the project library owns.

                                    Password-protected—Users cannot add or remove items from
                                       the project library, edit project library properties, or view private                                  3                                       items that the project library owns. Users must enter a password
                                         to edit the project library.


                                       Specifies the way in which you can use passwords with the project
                                            library. The default is FALSE, in which you can use a password to
                                  unlock a password-protected project library or to set the password of          interactive      No
                               an unprotected project library. If you set interactive to TRUE,
                                LabVIEW ignores the password and displays a dialog box that
                                prompts you to change the lock state.


                                       Specifies the password to set for a project library to which you want
        password      No        to add password protection, or the password to use to unlock a
                                   password-protected project library.


                                       Specifies whether you want to cache the password specified in
        put in                    No       password. The default is FALSE, which does not add the password to        cache                                    the LabVIEW password cache.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No


9438   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9438 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9439 ordinal=9439 -->
## Property and Method Reference

Property and Method Reference


 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

Save:CopySave:Copy

Saves a copy of the LabVIEW project library file.

      Note The LabVIEW Datalogging and Supervisory Control Module supports
         this method in the Run-Time Engine.

Parameters

                 Data
 Name                    Required  Description                  type

 Destination                             Specifies the destination directory for the copy of the
                            Yes Directory                               project library.


 New Name             No        Specifies the name of the copy of the project library.


 New Library Path         No       Returns the path to the copy of the project library.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value


                                                    © National Instruments 9439

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9439 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9440 ordinal=9440 -->
## Property and Method Reference

Property and Method Reference


         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

    Save:ForSave:For PreviousPrevious

      Saves a copy of the project library and all items within the project library that is
       readable by LabVIEW 8.0 and later. This method is similar to the LabVIEW Version
       selection on the Save for Previous Version dialog box.

           Note The LabVIEW Datalogging and Supervisory Control Module supports
                 this method in the Run-Time Engine.

     Parameters

                Data      Name        Required  Description
                type

        Path          Yes       Path to the directory where you want to save the project library.


                                  Version of LabVIEW for which you want to save. Wire the version number,
         Version      No       such as 8.6 or 9.0, to the Version input. The default is the immediately
                                 previous version.


     Remarks

      The following table lists the characteristics of this method.


9440   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9440 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9441 ordinal=9441 -->
## Property and Method Reference

Property and Method Reference


 Data type                                            No return value

 Available in Run-Time Engine                              No

 Available in Real-Time Operating System                      No

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

Save:LibrarySave:Library

Saves the LabVIEW project library file. You also can right-click the project library in the
Project Explorer window and select Save As from the shortcut menu to save the
project library file.

      Note The LabVIEW Datalogging and Supervisory Control Module supports
         this method in the Run-Time Engine.

Parameters

       Data Name       Required  Description       type

                       Path to the LabVIEW project library file. LabVIEW ignores this parameter if
 Path       No       you set Target to Clipboard. When you set Target to File, you must specify
                     a Path.


Remarks

The following table lists the characteristics of this method.


                                                    © National Instruments 9441

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9441 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9442 ordinal=9442 -->
## Property and Method Reference

Property and Method Reference


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

   SourceSource Scope:GetScope:Get

       Retrieves the access scope for an item that the LabVIEW project library owns, such as
       public or private access.

           Note The LabVIEW Datalogging and Supervisory Control Module supports
                 this method in the Run-Time Engine.

      The following table lists and describes the access scope enum values for the Source
      Scope:Get method:


        Scope       Description

         invalid     The item is an invalid value. The item is visible whenever the read function receives an
        scope        error and causes an error to occur if you pass the item to a write function.

                  The item is visible when users view the project library. Other VIs and applications can
         public
                          call public VIs.

                  The item does not appear visible when users view the project library or palettes if you
         private      lock the project library. Other VIs and applications that the project library does not
                own cannot call a private VI.

        protected   The item is visible to other VIs in the same class or a descendant class.

       community The item is visible when users view the project library.


9442   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9442 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9443 ordinal=9443 -->
## Property and Method Reference

Property and Method Reference

Parameters

          Data Name           Required  Description
          type

 source                     Contains a reference to the item in the project library for which you                  Yes ref                      want to set or retrieve access.


 inherited       No        Indicates whether the specified item is inherited.


Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                                      Yes

 Available in Real-Time Operating System                                 No

 Settable when the VI is running                                        No

 Loads the front panel into memory                                     No

 Need to authenticate before use                                       No

 Loads the block diagram into memory                                   No

 Remote access allowed                                                           Yes

SourceSource Scope:SetScope:Set

Sets the access scope of an item that the LabVIEW project library owns, such as public
or private access.

This method is similar to the Access Scope box on the Item Settings page of the Project
Library Properties dialog box.


                                                    © National Instruments 9443

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9443 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9444 ordinal=9444 -->
## Property and Method Reference

Property and Method Reference

           Note The LabVIEW Datalogging and Supervisory Control Module supports
                 this method in the Run-Time Engine.

     Parameters

               Data      Name       Required  Description               type

        source                 Contains a reference to the item in the project library for which you want                      Yes
          ref                      to set or retrieve access.

                                   Specifies the access setting for the item.

                                                   •  invalid scope—The item is an invalid value. The item is visible
                                whenever the read function receives an error and causes an error to
                                    occur if you pass this item to a write function.
                                                   • public—The item is visible when users view the project library. Other
                                         VIs and applications can call public VIs.
        scope        Yes              • private—The item does not appear visible when users view the
                                       project library or palettes if you lock the project library. Other VIs and
                                       applications that the project library does not own cannot call a
                                        private VI.
                                                   • protected—The item is visible to other VIs in the same class or a
                                  descendant class.
                                                   • community—The item is visible when users view the project library.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

         Settable when the VI is running                             No

        Loads the front panel into memory                          No


9444   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9444 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9445 ordinal=9445 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

SourceSource Scope:SetScope:Set andand PropagatePropagate

Sets the access scope of an item that the LabVIEW project library owns, such as public
or private access. If the item is a dynamic dispatch VI, LabVIEW also changes the scope
of other implementations.

Parameters

         Data Name         Required  Description         type

 source                   Contains a reference to the item in the project library for which you                Yes ref                    want to set or retrieve access.

                             Specifies the access setting for the item.

                                          •  invalid scope—The item is an invalid value. The item is visible
                           whenever the read function receives an error and causes an error
                                to occur if you pass this item to a write function.
                                          • public—The item is visible when users view the project library.
                             Other VIs and applications can call public VIs.
                                          • private—The item does not appear visible when users view the
 scope          Yes
                                project library or palettes if you lock the project library. Other VIs
                          and applications that the project library does not own cannot call a
                                 private VI.
                                          • protected—The item is visible to other VIs in the same class or a
                            descendant class.
                                          • community—The item is visible when users view the project
                                     library.


 skip                        Specifies whether to ask before applying the access scope setting to all
            No
 prompt?                  override VIs when the item is a dynamic dispatch VI. If skip prompt? is


                                                    © National Instruments 9445

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9445 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9446 ordinal=9446 -->
## Property and Method Reference

Property and Method Reference


                Data      Name         Required  Description
                 type

                               TRUE, this method applies the access scope setting to all override VIs
                                 without asking. If skip prompt? is FALSE or unwired, this method
                                throws a dialog box asking whether to apply the access scope setting to
                                              all override VIs.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

    LibraryLibrary PropertiesProperties

      Use these properties to configure LabVIEW project libraries.


        Property               Description

        AlarmsEvents:Database  Specifies the name of the computer where the alarms and events
       Computer             database resides.

        AlarmsEvents:Database  Specifies the name of the database where the Shared Variable Engine logs
      Name                 alarms and events.

        AlarmsEvents:Database  Specifies the file path to the database where the Shared Variable Engine
        Path                    logs alarms and events.

9446   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9446 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9447 ordinal=9447 -->
## Property and Method Reference

Property and Method Reference


Property               Description

AlarmsEvents:Enable    Enables alarms and events logging capability if set to TRUE.

                        Sets the alarms and events database to be the same as the database thatAlarmsEvents:Use                        logs data. If set to TRUE, LabVIEW ignores properties set on theDataLogging Database                      AlarmsEvents database.

Contains Compiled      Sets or returns whether LabVIEW stores the library in the compiled object
Code                   cache.

DataLogging:Database                         Specifies the name of the computer where the database resides.Computer

DataLogging:Database   Specifies the name of the database where the Shared Variable Engine logs
Name                   data.

DataLogging:Database   Specifies the file path to the database where the Shared Variable Engine
Path                    logs data.

DataLogging:Enable    Enables data logging capability if set to TRUE.

                        Sets the lifespan (in days) of the logged data in the database. If value is 0,
DataLogging:Lifespan   then data is always available, otherwise the database can destroy data
                           after the number of specified days.

                         Specifies the description of the LabVIEW project library for the Context
Description                     Help window.

                       Returns a list of strings which contain the qualified names of the friends of
Friends                           this library.

                      Path or symbolic path to an HTML file (.htm or .html) or compiled help
Help:Document Path
                                 file (.chm or .hlp) to which the LabVIEW project library is linked.

                       Index keyword or HTML filename for a topic in the compiled help file to
Help:Document Tag
                     which the LabVIEW project library is linked.

Is In Packed Library     Returns TRUE if a packed project library contains the library.

Localized Name       The localized name of the item.

                       Returns the name of the library. If the library has not been saved to disk,
Name
                    you can write to this property to change the name.

                       Returns a reference to the application instance that owns this library. Be
Owning Application
                       sure and close this reference afterward.

Process:Save State
                    The period (in minutes) the variable engine should save the process state.
Period


                                                    © National Instruments 9447

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9447 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9448 ordinal=9448 -->
## Property and Method Reference

Property and Method Reference


        Property               Description

         Qualified Name         Returns the qualified name of the library.

                               Returns an MD5 hash of the library. This value changes if the library         Signature                               changes.

         Version              The version number of the LabVIEW project library.

   AlarmsEvents:DatabaseAlarmsEvents:Database ComputerComputer

       Specifies the name of the computer where the alarms and events database resides.

           Note The LabVIEW Datalogging and Supervisory Control Module supports
                 this property in the Run-Time Engine.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   AlarmsEvents:DatabaseAlarmsEvents:Database NameName

       Specifies the name of the database where the Shared Variable Engine logs alarms and

9448   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9448 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9449 ordinal=9449 -->
## Property and Method Reference

Property and Method Reference

events.

      Note The LabVIEW Datalogging and Supervisory Control Module supports
         this property in the Run-Time Engine.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

AlarmsEvents:DatabaseAlarmsEvents:Database PathPath

Specifies the file path to the database where the Shared Variable Engine logs alarms
and events.

      Note The LabVIEW Datalogging and Supervisory Control Module supports
         this property in the Run-Time Engine.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 9449

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9449 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9450 ordinal=9450 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   AlarmsEvents:EnableAlarmsEvents:Enable

      Enables alarms and events logging capability if set to TRUE.

           Note The LabVIEW Datalogging and Supervisory Control Module supports
                 this property in the Run-Time Engine.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No


9450   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9450 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9451 ordinal=9451 -->
## Property and Method Reference

Property and Method Reference


 Remote access allowed                                                  Yes

AlarmsEvents:UseAlarmsEvents:Use DataLoggingDataLogging DatabaseDatabase

Sets the alarms and events database to be the same as the database that logs data. If
set to TRUE, LabVIEW ignores properties set on the AlarmsEvents database.

      Note The LabVIEW Datalogging and Supervisory Control Module supports
         this property in the Run-Time Engine.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

ContainsContains CompiledCompiled CodeCode

Sets or returns whether LabVIEW stores the library in the compiled object cache.

If TRUE, LabVIEW does notstore the library in the compiled object cache. In this case,
you must save the library every time you modify a member of the library or when you
migrate the library to a new version of LabVIEW. If FALSE, LabVIEW stores the library in

                                                    © National Instruments 9451

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9451 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9452 ordinal=9452 -->
## Property and Method Reference

Property and Method Reference

       the compiled object cache so you must save the library only when you change the
        library itself.

       This property is similar to the Separate compiled code from source file option on the
       General Settings page of the Project Library Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                 No

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   DataLogging:DatabaseDataLogging:Database ComputerComputer

       Specifies the name of the computer where the database resides.

           Note The LabVIEW Datalogging and Supervisory Control Module supports
                 this property in the Run-Time Engine.

     Remarks

      The following table lists the characteristics of this property.


        Data type


9452   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9452 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9453 ordinal=9453 -->
## Property and Method Reference

Property and Method Reference


 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

DataLogging:DatabaseDataLogging:Database NameName

Specifies the name of the database where the Shared Variable Engine logs data.

      Note The LabVIEW Datalogging and Supervisory Control Module supports
         this property in the Run-Time Engine.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes


                                                    © National Instruments 9453

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9453 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9454 ordinal=9454 -->
## Property and Method Reference

Property and Method Reference

   DataLogging:DatabaseDataLogging:Database PathPath

       Specifies the file path to the database where the Shared Variable Engine logs data.

           Note The LabVIEW Datalogging and Supervisory Control Module supports
                 this property in the Run-Time Engine.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   DataLogging:EnableDataLogging:Enable

      Enables data logging capability if set to TRUE.

           Note The LabVIEW Datalogging and Supervisory Control Module supports
                 this property in the Run-Time Engine.


9454   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9454 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9455 ordinal=9455 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

DataLogging:LifespanDataLogging:Lifespan

Sets the lifespan (in days) of the logged data in the database. If value is 0, then data is
always available, otherwise the database can destroy data after the number of
specified days.

The database only discards data if new data is logged. This property affects all data
from the library stored in the database, not just the most recent data. For example, if
you set this property to four days and you have three days of data, the database does
not destroy any data. However, if you set this same property to two days from four
days and you have three days of data, the database can destroy any data collected
more than two days ago.

      Note The LabVIEW Datalogging and Supervisory Control Module supports
         this property in the Run-Time Engine.


                                                    © National Instruments 9455

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9455 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9456 ordinal=9456 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    DescriptionDescription

       Specifies the description of the LabVIEW project library for the Context Help window.

           If you want to display a carriage return in the Context Help window, you must separate
      paragraphs with two carriage returns.

       This property is similar to the Description text box on the Documentation page of the
       Project Library Properties dialog box.

           Note The LabVIEW Datalogging and Supervisory Control Module supports
                 this property in the Run-Time Engine.

     Remarks

      The following table lists the characteristics of this property.


        Data type


9456   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9456 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9457 ordinal=9457 -->
## Property and Method Reference

Property and Method Reference


 Permissions                                                     Read/Write

 Available in Run-Time Engine                                        Yes (Read Only)

 Available in Real-Time Operating System                      No

 Settable when the VI is running                                      Yes

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

FriendsFriends

Returns a list of strings which contain the qualified names of the friends of this library.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes


                                                    © National Instruments 9457

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9457 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9458 ordinal=9458 -->
## Property and Method Reference

Property and Method Reference

   Help:DocumentHelp:Document PathPath

      Path or symbolic path to an HTML file (.htm or .html) or compiled help file (.chm or
      .hlp) to which the LabVIEW project library is linked.

           If the path is to a compiled help file, use the Help:Document Tag property to determine
       the specific topic in that help file.

       This property is similar to the Help path text box on the Documentation page of the
       Project Library Properties dialog box.

           Note The LabVIEW Datalogging and Supervisory Control Module supports
                 this property in the Run-Time Engine.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read/Write

         Available in Run-Time Engine                                        Yes (Read Only)

         Available in Real-Time Operating System                      No

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

   Help:DocumentHelp:Document TagTag

       Index keyword or HTML filename for a topic in the compiled help file to which the


9458   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9458 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9459 ordinal=9459 -->
## Property and Method Reference

Property and Method Reference

LabVIEW project library is linked.

Use this property only when Help:Document Path is a path to a compiled help file
(.chm or .hlp).

For .chm files, this property can be an HTML filename or index keyword. To link to a
bookmark within an HTML file, add # followed by the name of the bookmark to the
end of the filename. For .hlp files, this property can be an index keyword.

This property is similar to the Help tag text box on the Documentation page of the
Project Library Properties dialog box.

      Note The LabVIEW Datalogging and Supervisory Control Module supports
         this property in the Run-Time Engine.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read/Write

 Available in Run-Time Engine                                        Yes (Read Only)

 Available in Real-Time Operating System                      No

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

IsIs InIn PackedPacked LibraryLibrary

Returns TRUE if a packed project library contains the library.


                                                    © National Instruments 9459

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9459 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9460 ordinal=9460 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                                   Yes

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

    LocalizedLocalized NameName

      The localized name of the item.

       This property is similar to the Localized Name text box on the Documentation page of
       the Project Library Properties dialog box.

           Note The LabVIEW Datalogging and Supervisory Control Module supports
                 this property in the Run-Time Engine.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read/Write

         Available in Run-Time Engine                                        Yes (Read Only)


9460   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9460 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9461 ordinal=9461 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                      No

 Settable when the VI is running                                      Yes

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

NameName

Returns the name of the library. If the library has not been saved to disk, you can write
to this property to change the name.

      Note The LabVIEW Datalogging and Supervisory Control Module supports
         this property in the Run-Time Engine.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read/Write

 Available in Run-Time Engine                                        Yes (Read Only)

 Available in Real-Time Operating System                      No

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes


                                                    © National Instruments 9461

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9461 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9462 ordinal=9462 -->
## Property and Method Reference

Property and Method Reference

   OwningOwning ApplicationApplication

       Returns a reference to the application instance that owns this library. Be sure and close
        this reference afterward.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

    Process:SaveProcess:Save StateState PeriodPeriod

      The period (in minutes) the variable engine should save the process state.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

9462   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9462 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9463 ordinal=9463 -->
## Property and Method Reference

Property and Method Reference


 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

QualifiedQualified NameName

Returns the qualified name of the library.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                               Read Only

 Available in Run-Time Engine                                        Yes (Read Only)

 Available in Real-Time Operating System                      No

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

SignatureSignature

Returns an MD5 hash of the library. This value changes if the library changes.

Remarks

The following table lists the characteristics of this property.

                                                    © National Instruments 9463

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9463 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9464 ordinal=9464 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                                   Yes

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

    VersionVersion

      The version number of the LabVIEW project library.

       This property is similar to the Version Number component on the General Settings
      page of the Project Library Properties dialog box.

           Note The LabVIEW Datalogging and Supervisory Control Module supports
                 this property in the Run-Time Engine.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read/Write

         Available in Run-Time Engine                                        Yes (Read Only)

         Available in Real-Time Operating System                      No

         Settable when the VI is running                                      Yes

        Loads the front panel into memory                          No


9464   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9464 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9465 ordinal=9465 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

XInterfaceLibraryXInterfaceLibrary

XInterfaceLibrary Methods
XInterfaceLibraryXInterfaceLibrary MethodsMethods


 Method            Description

 Add Ability         Creates a new ability of the specified type.

 Add Method        Creates a new method.

 New Property      Creates a new property folder and returns a reference to it.

AddAdd AbilityAbility

Creates a new ability of the specified type.

      Note The LabVIEW Datalogging and Supervisory Control Module supports
         this method in the Run-Time Engine.

Parameters

       Data
 Name         Required  Description
        type

 Name          Yes     Name of the ability you want to create.


                                                    © National Instruments 9465

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9465 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9466 ordinal=9466 -->
## Property and Method Reference

Property and Method Reference


               Data      Name         Required  Description
               type

          VI                                       If VI Path is specified, an existing VI is used for the ability, if not, a new VI                  No        Path                             is created for the ability.


         Folder       No        Creates the ability in the specified folder.


     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                         No

         Available in Real-Time Operating System                                 No

         Settable when the VI is running                                        No

        Loads the front panel into memory                                     No

       Need to authenticate before use                                       No

        Loads the block diagram into memory                                   No

       Remote access allowed                                                           Yes

   AddAdd MethodMethod

       Creates a new method.

           Note The LabVIEW Datalogging and Supervisory Control Module supports
                 this method in the Run-Time Engine.


9466   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9466 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9467 ordinal=9467 -->
## Property and Method Reference

Property and Method Reference

Parameters

       Data Name         Required  Description
        type

 VI                                      If VI Path is specified, an existing VI is used for the method, if not, a new            No Path                         VI is created for the method.


 Folder       No        Creates the method in the specified folder.


Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                         No

 Available in Real-Time Operating System                                 No

 Settable when the VI is running                                        No

 Loads the front panel into memory                                     No

 Need to authenticate before use                                       No

 Loads the block diagram into memory                                   No

 Remote access allowed                                                           Yes

NewNew PropertyProperty

Creates a new property folder and returns a reference to it.

      Note The LabVIEW Datalogging and Supervisory Control Module supports
         this method in the Run-Time Engine.


                                                    © National Instruments 9467

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9467 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9468 ordinal=9468 -->
## Property and Method Reference

Property and Method Reference

     Parameters

      Name   Data type    Required    Description

      Name                 Yes       Name of the new property folder to create.


         Folder            No          Folder in which to create the new property folder.


     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                         No

         Available in Real-Time Operating System                                 No

         Settable when the VI is running                                        No

        Loads the front panel into memory                                     No

       Need to authenticate before use                                       No

        Loads the block diagram into memory                                   No

       Remote access allowed                                                           Yes

    XControlLibraryXControlLibrary
   XNodeLibraryXNodeLibrary
    LVClassLibraryLVClassLibrary

       LVClassLibrary Methods


9468   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9468 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9469 ordinal=9469 -->
## Property and Method Reference

Property and Method Reference

LVClassLibrary Properties
LVClassLibraryLVClassLibrary MethodsMethods


 Method          Description

 Add Parent                Makes the referenced interface a parent interface of the current class. Interface

 Descendants      Indicates whether the member VI specified by Dynamic Member VI requires
 Must Call Parent  each child class VI that overrides the member VI to call the member VI with the
 Item?:Get          Call Parent Class Method node.

 Descendants     Determines whether the member VI specified by Dynamic Member VI requires
 Must Call Parent  each child class VI that overrides the member VI to call the member VI with the
 Item?:Set          Call Parent Class Method node.

 Descendants
                   Indicates whether descendant classes must override the member VI specified by Must Override                  the Dynamic Member VI reference.
 Item?:Get

 Descendants                 Determines whether descendant classes must override the member VI specified
 Must Override                by Dynamic Member VI. Item?:Set

                  Returns TRUE if the class contains the specified VI. If the VI exists, this method
                   returns the qualified name and path of the VI. The path is <Not A Path> if the Has
                     VI has never been saved. If the class inherits multiple methods of the same name Implementation?
                from parent interfaces and does not provide its own override, this method
                   returns an error.

                 Given the qualified name of a current parent interface, this method removes that
 Remove Parent
                  parent from the current class. Taking in the qualified name allows for removal of
 Interface
                  missing parents. This method does not allow removal of parent classes.

 Write Parent      Writes the interfaces that the referenced class directly inherits from. Use this
 Interfaces       method to add or remove parents.

 Write Parent      Writes the libraries that the referenced class directly inherits from. Use this
 Library Paths    method to add or remove parent libraries.


                                                    © National Instruments 9469

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9469 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9470 ordinal=9470 -->
## Property and Method Reference

Property and Method Reference

   AddAdd ParentParent InterfaceInterface

      Makes the referenced interface a parent interface of the current class.

     Parameters

               Data      Name       Required  Description               type

      New                     Specifies the interface that you want the class to inherit from. If this input
                      Yes         Parent                        is a class instead of an interface, this method returns an error.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

   DescendantsDescendants MustMust CallCall ParentParent Item?:GetItem?:Get

       Indicates whether the member VI specified by Dynamic Member VI requires each child
       class VI that overrides the member VI to call the member VI with the Call Parent Class
      Method node.


9470   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9470 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9471 ordinal=9471 -->
## Property and Method Reference

Property and Method Reference

Parameters

              Data Name               Required  Description
              type

 Dynamic                          Specifies the member VI that you want to know whether                       Yes Member VI                     descendant classes must override.


Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                         No

 Available in Real-Time Operating System                                 No

 Settable when the VI is running                                                    Yes

 Loads the front panel into memory                                     No

 Need to authenticate before use                                       No

 Loads the block diagram into memory                                   No

 Remote access allowed                                                           Yes

DescendantsDescendants MustMust CallCall ParentParent Item?:SetItem?:Set

Determines whether the member VI specified by Dynamic Member VI requires each
child class VI that overrides the member VI to call the member VI with the Call Parent
Class Method node.

This method is similar to the Require overrides of this dynamic dispatch VI to always
invoke the Call Parent Class Method node checkbox on the Item Settings page of the
Class Properties dialog box.


                                                    © National Instruments 9471

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9471 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9472 ordinal=9472 -->
## Property and Method Reference

Property and Method Reference

     Parameters

                     Data      Name                Required  Description
                      type

       Dynamic                           Specifies the member VI that you want to specify whether each                                Yes       Member VI                         child class VI must call.


        Must Call                           Specifies whether the descendant VIs of the member VI must                                Yes         Parent?                                call the member VI.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

   DescendantsDescendants MustMust OverrideOverride Item?:GetItem?:Get

       Indicates whether descendant classes must override the member VI specified by the
      Dynamic Member VI reference.


9472   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9472 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9473 ordinal=9473 -->
## Property and Method Reference

Property and Method Reference

Parameters

              Data Name               Required  Description
              type

 Dynamic                          Specifies the member VI that you want to know whether                       Yes Member VI                     descendant classes must override.


Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                         No

 Available in Real-Time Operating System                                 No

 Settable when the VI is running                                                    Yes

 Loads the front panel into memory                                     No

 Need to authenticate before use                                       No

 Loads the block diagram into memory                                   No

 Remote access allowed                                                           Yes

DescendantsDescendants MustMust OverrideOverride Item?:SetItem?:Set

Determines whether descendant classes must override the member VI specified by
Dynamic Member VI.

This method is similar to the Require descendant classes to override this dynamic
dispatch VI checkbox of the Item Settings page of the Class Properties dialog box.


                                                    © National Instruments 9473

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9473 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9474 ordinal=9474 -->
## Property and Method Reference

Property and Method Reference

     Parameters

                     Data      Name               Required  Description
                      type

       Dynamic                          Specifies the member VI that you want to set whether                               Yes       Member VI                     descendant classes must override.


        Must                              Specifies whether the descendant VIs of the member VI must                               Yes         Override?                        override the member VI.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

   HasHas Implementation?Implementation?

       Returns TRUE if the class contains the specified VI. If the VI exists, this method returns
       the qualified name and path of the VI. The path is <Not A Path> if the VI has never
      been saved. If the class inherits multiple methods of the same name from parent
       interfaces and does not provide its own override, this method returns an error.


9474   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9474 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9475 ordinal=9475 -->
## Property and Method Reference

Property and Method Reference

Parameters

          Data Name          Required  Description
          type

 VI Name        Yes        Specifies the name of the VI you want to find.


                             Specifies whether you want to look for the VI within ancestors of the
 Consider                     class. If multiple ancestors contain a VI with the specified name,                 Yes Parents?                LabVIEW chooses the ancestor with the closest implementation.
                         Consider Parents? does not look within missing or corrupt ancestors.


                          Returns the path to the specified VI. If the class does not include the VI,
 VI Path       No                              VI Path returns <Not A Path>.


 VI                          Returns the qualified name of the VI. If the class does not include the Qualified      No
                                   VI, VI Qualified Name returns an empty string. Name

Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                         No

 Available in Real-Time Operating System                                 No

 Settable when the VI is running                                        No

 Loads the front panel into memory                                     No

 Need to authenticate before use                                       No

 Loads the block diagram into memory                                   No

 Remote access allowed                                                           Yes


                                                    © National Instruments 9475

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9475 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9476 ordinal=9476 -->
## Property and Method Reference

Property and Method Reference

   RemoveRemove ParentParent InterfaceInterface

      Given the qualified name of a current parent interface, this method removes that
       parent from the current class. Taking in the qualified name allows for removal of
       missing parents. This method does not allow removal of parent classes.

     Parameters

                               Data      Name                          Required  Description                                type

         Parent Interface Qualified                      Specifies the qualified name of the parent                                           Yes      Name                                            interface.


                                                         Specifies whether to prompt the user to save the       Prompt To Save?                  Yes
                                                   modified class.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes


9476   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9476 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9477 ordinal=9477 -->
## Property and Method Reference

Property and Method Reference

WriteWrite ParentParent InterfacesInterfaces

Writes the interfaces that the referenced class directly inherits from. Use this method
to add or remove parents.

Parameters

            Data Name              Required  Description            type

                                  Specifies the names of the interfaces to write. All references in the Interfaces           Yes                                 array must be interfaces.


 Prompt To                     Yes        Specifies whether to prompt the user to save the modified class. Save?

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                              No

 Available in Real-Time Operating System                      No

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

WriteWrite ParentParent LibraryLibrary PathsPaths

Writes the libraries that the referenced class directly inherits from. Use this method to

                                                    © National Instruments 9477

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9477 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9478 ordinal=9478 -->
## Property and Method Reference

Property and Method Reference

      add or remove parent libraries.

     Parameters

                Data      Name        Required  Description                type

                                    Specifies the paths to the parent libraries. If the parent library has never
         Parents        Yes      been saved, specify a relative path consisting of only the filename of the
                                 parent library. Otherwise, specify the absolute path of the parent library.

       Prompt
        To            Yes        Specifies whether to prompt the user to save the modified class.
        Save?

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                  No

    LVClassLibraryLVClassLibrary PropertiesProperties


        Property     Description

         Ancestor      Property indicates that an ancestor class controls the creation of data value
          Restricts      references to this class. Only the ancestors member VIs can create data value

9478   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9478 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9479 ordinal=9479 -->
## Property and Method Reference

Property and Method Reference


Property     Description

Reference               references.Creation

Child              Property indicates whether data value references to all of this class descendants canReferences            be created only in member VIs of this class.
Restricted

             Returns an array of references to all LabVIEW classes in memory that directly inheritChildren In            from the referenced class. This property does not return additional descendents ofMemory[]              the child classes.

             Returns a reference to the default probe for the LabVIEW class library. The default
DefaultProbe probe is the probe LabVIEW uses when you first create a probe from a wire of this
               class type.

             Returns an array of references to the member VIs of the referenced LabVIEW class
Dynamic      that contain a dynamic dispatch terminal. To obtain references to the methods of
Member VIs[]  the referenced class that do notcontain a dynamic dispatch terminal, use the Static
           Member VIs[] property.

             Returns TRUE if the referenced .lvclass file is an interface and returns FALSE ifIs Interface
              the file is a class.

             Gets or sets the LabVIEW class from which the referenced class directly inherits. ThisParent Class              property does not support interfaces.

            Reads the interfaces that the referenced class directly inherits from. Missing parentsParent              are not included. Use the Write Parent Interfaces method to assign parent interfacesInterfaces
              to a class.

Parent       Reads information about the parent libraries of this LabVIEW class library. Missing
Libraries      parents are included. Use the Write Parent Library Paths method to assign the array.

Private Data   Returns a reference to the control that contains the private data of this LabVIEW
Control        class.

Self
              Property indicates that data value references to this class can only be created/
References
              deleted by member VIs of this class.
Restricted

Simple       Returns the name of the class without prepending namespace information from
Name       owning classes.

             Returns an array of references to the members VIs of the referenced LabVIEW class
Static         that do notcontain a dynamic dispatch terminal. To obtain references to the
Member VIs[] methods of the referenced class that contain a dynamic dispatch terminal, use the
            Dynamic Member VIs[] property.

                                                    © National Instruments 9479

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9479 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9480 ordinal=9480 -->
## Property and Method Reference

Property and Method Reference


        Property     Description

                     Determines whether to allow the class to transfer all override requirements to any
                     descendant classes instead of overriding the dynamic dispatch VI itself.         Transfer
        Must                       This property is similar to the Transfer all Must Override requirements to
         Overrides?                    descendant classes checkbox of the Inheritance page of the Class Properties dialog
                       box.

        Wire Pens     Gets or sets the appearance of the wire associated with this LabVIEW class.

    AncestorAncestor RestrictsRestricts ReferenceReference CreationCreation

       Property indicates that an ancestor class controls the creation of data value references
       to this class. Only the ancestors member VIs can create data value references.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes


9480   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9480 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9481 ordinal=9481 -->
## Property and Method Reference

Property and Method Reference

ChildChild ReferencesReferences RestrictedRestricted

Property indicates whether data value references to all of this class descendants can
be created only in member VIs of this class.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                 No

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

ChildrenChildren InIn Memory[]Memory[]

Returns an array of references to all LabVIEW classes in memory that directly inherit
from the referenced class. This property does not return additional descendents of the
child classes.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only


                                                    © National Instruments 9481

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9481 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9482 ordinal=9482 -->
## Property and Method Reference

Property and Method Reference


         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

   DefaultProbeDefaultProbe

       Returns a reference to the default probe for the LabVIEW class library. The default
      probe is the probe LabVIEW uses when you first create a probe from a wire of this class
       type.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                 No

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes


9482   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9482 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9483 ordinal=9483 -->
## Property and Method Reference

Property and Method Reference

DynamicDynamic MemberMember VIs[]VIs[]

Returns an array of references to the member VIs of the referenced LabVIEW class that
contain a dynamic dispatch terminal. To obtain references to the methods of the
referenced class that do notcontain a dynamic dispatch terminal, use the Static
Member VIs[] property.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

IsIs InterfaceInterface

Returns TRUE if the referenced .lvclass file is an interface and returns FALSE if the
file is a class.

Remarks

The following table lists the characteristics of this property.


 Data type


                                                    © National Instruments 9483

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9483 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9484 ordinal=9484 -->
## Property and Method Reference

Property and Method Reference


         Permissions                                                     Read Only

         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

    ParentParent ClassClass

       Gets or sets the LabVIEW class from which the referenced class directly inherits. This
       property does not support interfaces.

           If the referenced class directly inherits from the LabVIEW Object class, this property
       returns Not a Refnum. To set the parent of the referenced class to be LabVIEW Object,
       wire a Not a Refnum constant to this property.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                 No

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

9484   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9484 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9485 ordinal=9485 -->
## Property and Method Reference

Property and Method Reference

ParentParent InterfacesInterfaces

Reads the interfaces that the referenced class directly inherits from. Missing parents
are not included. Use the Write Parent Interfaces method to assign parent interfaces to
a class.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

ParentParent LibrariesLibraries

Reads information about the parent libraries of this LabVIEW class library. Missing
parents are included. Use the Write Parent Library Paths method to assign the array.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only


                                                    © National Instruments 9485

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9485 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9486 ordinal=9486 -->
## Property and Method Reference

Property and Method Reference


         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                       No

    PrivatePrivate DataData ControlControl

       Returns a reference to the control that contains the private data of this LabVIEW class.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

    SelfSelf ReferencesReferences RestrictedRestricted

       Property indicates that data value references to this class can only be created/deleted
      by member VIs of this class.

9486   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9486 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9487 ordinal=9487 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                 No

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

SimpleSimple NameName

Returns the name of the class without prepending namespace information from
owning classes.

To change the name of the class, use the Save As method.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No


                                                    © National Instruments 9487

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9487 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9488 ordinal=9488 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

    StaticStatic MemberMember VIs[]VIs[]

       Returns an array of references to the members VIs of the referenced LabVIEW class that
      do notcontain a dynamic dispatch terminal. To obtain references to the methods of
       the referenced class that contain a dynamic dispatch terminal, use the Dynamic
     Member VIs[] property.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

    TransferTransfer MustMust Overrides?Overrides?

      Determines whether to allow the class to transfer all override requirements to any
      descendant classes instead of overriding the dynamic dispatch VI itself.

       This property is similar to the Transfer all Must Override requirements to descendant

9488   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9488 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9489 ordinal=9489 -->
## Property and Method Reference

Property and Method Reference

classes checkbox of the Inheritance page of the Class Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                 No

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

WireWire PensPens

Gets or sets the appearance of the wire associated with this LabVIEW class.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                 No

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

                                                    © National Instruments 9489

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9489 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9490 ordinal=9490 -->
## Property and Method Reference

Property and Method Reference


        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    StatechartLibraryStatechartLibrary

       StatechartLibrary Methods

       StatechartLibrary Properties
    StatechartLibraryStatechartLibrary MethodsMethods

      Use these methods to configure statecharts.


       Method         Description

                        Generates code for the statechart and optionally saves the statechart. The
        Generate Code  statechart is saved only if code generation occurs and the Save Statechart
                       parameter is TRUE.

                        Generates an XML file that contains information about all components, including        Generate                             states, pseudostates, connectors, regions, and transitions, of a statechart. You can
        Documentation                       view the XML file in a Web browser.

   GenerateGenerate CodeCode

       Generates code for the statechart and optionally saves the statechart. The statechart is
      saved only if code generation occurs and the Save Statechart parameter is TRUE.

     Parameters

                      Data
      Name                   Required  Description
                       type

        Save
                                  Yes        Specifies whether to save the statechart if code generation
         Statechart


9490   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9490 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9491 ordinal=9491 -->
## Property and Method Reference

Property and Method Reference


               Data Name                   Required  Description
                type

                                       occurs.


 Force                           Yes        Specifies whether to force code generation. Generation

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                              No

 Available in Real-Time Operating System                      No

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

GenerateGenerate DocumentationDocumentation

Generates an XML file that contains information about all components, including
states, pseudostates, connectors, regions, and transitions, of a statechart. You can
view the XML file in a Web browser.

This method also generates a folder of support files in the same location as the XML
file you generate. This support folder contains files that the XML file references,
including images of the statechart components, an EXtensible Stylesheet Language
Transformations (XSLT) file, and an XML Schema Definition (XSD) file.


                                                    © National Instruments 9491

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9491 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9492 ordinal=9492 -->
## Property and Method Reference

Property and Method Reference

           Note You may freely distribute your generated XML file and support folder
               containing the XSLT and XSD files. However, National Instruments claims all
               copyrights on NI_Statechart_Documentation_Tool.xslt and
           NI_Statechart_Documentation_Tool.xsd. Do not use or distribute
              these files except with the associated XML file and support folder generated
             by the LabVIEW Statechart Module Generate Documentation feature. You
           may modify NI_Statechart_Documentation_Tool.xslt, but the
                    file must retain the National Instruments copyright notice contained therein,
             which may not be modified or obscured. You also must add a prominent
               notice at the top of the file that states that you have modified the file. You
           may not modify NI_Statechart_Documentation_Tool.xsd.

       This method is similar to the Generate Documentation item on the shortcut menu of
      an .lvsc item, or statechart library, in a statechart project. This method also is
        similar to the File»Generate Documentation menu item in the Statechart Editor
      window.

     Parameters

              Data      Name       Required  Description               type

                                   Specifies the location to which LabVIEW saves the XML file and the folder
        Path         Yes        of support files. The path you specify must end in the .xml file extension.
                           The default value is the same location as the statechart you document.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

         Settable when the VI is running                             No


9492   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9492 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9493 ordinal=9493 -->
## Property and Method Reference

Property and Method Reference


 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

StatechartLibraryStatechartLibrary PropertiesProperties


 Property           Description

 Code Generation    Returns TRUE when the statechart has changes that require you to generate
 Needed           code for the statechart.

 Has Diagram Errors  Returns TRUE when the statechart diagram contains errors.

CodeCode GenerationGeneration NeededNeeded

Returns TRUE when the statechart has changes that require you to generate code for
the statechart.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

                                                    © National Instruments 9493

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9493 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9494 ordinal=9494 -->
## Property and Method Reference

Property and Method Reference

   HasHas DiagramDiagram ErrorsErrors

       Returns TRUE when the statechart diagram contains errors.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

      TargetItemTargetItem

       TargetItem Methods

       TargetItem Properties
    TargetItemTargetItem MethodsMethods


       Method       Description

         Refresh        Refreshes Dependencies under this target in the Project Explorer window. You also
        Dependencies can use the Project Explorer window to refresh Dependencies.


9494   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9494 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9495 ordinal=9495 -->
## Property and Method Reference

Property and Method Reference

RefreshRefresh DependenciesDependencies

Refreshes Dependencies under this target in the Project Explorer window. You also can
use the Project Explorer window to refresh Dependencies.

      Note The LabVIEW Datalogging and Supervisory Control Module supports
         this method in the Run-Time Engine.

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                              No

 Available in Real-Time Operating System                      No

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

TargetItemTargetItem PropertiesProperties


 Property      Description

 Application    The application instance opened by the target to edit and run VIs.

 Build          Returns a reference to Build Specifications under the current target in the Project
 Specifications  Explorer window. You can use this reference with the ProjectItem properties.

               Returns a reference to Dependencies under the current target in the Project
 Dependencies
               Explorer window. You can use this reference with the ProjectItem properties.


                                                    © National Instruments 9495

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9495 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9496 ordinal=9496 -->
## Property and Method Reference

Property and Method Reference

    ApplicationApplication

      The application instance opened by the target to edit and run VIs.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

    BuildBuild SpecificationsSpecifications

       Returns a reference to Build Specifications under the current target in the Project
       Explorer window. You can use this reference with the ProjectItem properties.

           Note The LabVIEW Datalogging and Supervisory Control Module supports
                 this property in the Run-Time Engine.

     Remarks

      The following table lists the characteristics of this property.


        Data type

9496   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9496 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9497 ordinal=9497 -->
## Property and Method Reference

Property and Method Reference


 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

DependenciesDependencies

Returns a reference to Dependencies under the current target in the Project Explorer
window. You can use this reference with the ProjectItem properties.

      Note The LabVIEW Datalogging and Supervisory Control Module supports
         this property in the Run-Time Engine.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

                                                    © National Instruments 9497

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9497 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9498 ordinal=9498 -->
## Property and Method Reference

Property and Method Reference

      PropertyFolderPropertyFolder

       PropertyFolder Methods
    PropertyFolderPropertyFolder MethodsMethods


       Method    Description

       Add                    Creates a new read or write property VI if you do not wire VI Path. If you wire VI Path,         Property                 LabVIEW uses an existing VI as a property VI.          VI

   AddAdd PropertyProperty VIVI

       Creates a new read or write property VI if you do not wire VI Path. If you wire VI Path,
      LabVIEW uses an existing VI as a property VI.

           Note The LabVIEW Datalogging and Supervisory Control Module supports
                 this method in the Run-Time Engine.

     Parameters

              Data      Name        Required  Description               type

        Read?                              If TRUE, creates a read property VI. If FALSE, creates a write property VI.
                 No
          (T)                   The default is TRUE.


          VI                     Path to the property VI. This parameter is optional. If you wire a path,
                 No
        Path                  LabVIEW uses an existing VI as a property VI.


9498   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9498 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9499 ordinal=9499 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                         No

 Available in Real-Time Operating System                                 No

 Settable when the VI is running                                        No

 Loads the front panel into memory                                     No

 Need to authenticate before use                                       No

 Loads the block diagram into memory                                   No

 Remote access allowed                                                           Yes

XPropertyFolderXPropertyFolder

XPropertyFolder Properties
XPropertyFolderXPropertyFolder PropertiesProperties


 Property         Description

 Description       Sets or gets the description of the property folder.

 Help Tag         Sets or gets the help tag of the property folder.

 Identifier         Sets or gets the property identifier of the property folder.

 Long Name       Sets or gets the long name of the property folder.

DescriptionDescription

Sets or gets the description of the property folder.


                                                    © National Instruments 9499

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9499 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9500 ordinal=9500 -->
## Property and Method Reference

Property and Method Reference

           Note The LabVIEW Datalogging and Supervisory Control Module supports
                 this property in the Run-Time Engine.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

         Settable when the VI is running                                 No

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   HelpHelp TagTag

       Sets or gets the help tag of the property folder.

           Note The LabVIEW Datalogging and Supervisory Control Module supports
                 this property in the Run-Time Engine.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write


9500   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:9500 -->

