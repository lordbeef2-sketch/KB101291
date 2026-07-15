# NI_LABVIEW_PROGRAMMING_REFERENCE

<!--SYSTEM_CORPUS id=NI_LABVIEW_PROGRAMMING_REFERENCE format=markdown generated=2026-07-14T12:02:18+00:00 -->
- title: LabVIEW Programming Reference Manual
- source: https://docs-be.ni.com/bundle/labview-api-ref/preprocessedpdf/enus
- source_sha256: 7a54c389b4f3d78e2215f55c9f156124d3668ce61d0d5018094e356004d895ac
- versions: 2024 Q1|2024 Q3|2025 Q1|2025 Q3|2026 Q1
- fidelity: full-text-records

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10001 ordinal=10001 -->
## Property and Method Reference

Property and Method Reference

MenuMenu Selection?Selection? (App)(App)

Generated when the user selects an application item from the LabVIEW menu, such as
Help»Show Context Help.

      Note If you have an event structure with a Menu Selection? (App) event,
       items chosen from the File»Recent Projects submenu return the item tag
      APP_RECENT_PROJECTS and items chosen from the File»Recent Files
      submenu return the item tag APP_RECENT_FILES.

Event Data Fields

 Name    Description

          Source of the event. LabVIEW UI refers to any built-in user interface event.

 Source
          0            LabVIEW UI


 Type     Type of event that occurred, such as Mouse Down, Value Change, Timeout, and so on.


 Time     Value of the millisecond timer when the event occurred.


 VIRef     Reference to the VI on which this event occurred.


 MenuRef  Reference to the LabVIEW menu from which an item was selected.


 ItemTag  Name of the menu item the user selected, such as APP_SHOW_HELP.


                                                    © National Instruments 10001

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10001 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10002 ordinal=10002 -->
## Property and Method Reference

Property and Method Reference


       Name    Description

                   Path of the LabVIEW menu item the user selected, such as
          ItemPath                APP_HELP:SHOW_APP_HELP. Components are separated by colons.

                    Allows you to prevent LabVIEW from processing the event, bypassing the behavior           Discard?                    normally triggered by that event. The default is FALSE.

   MouseMouse EnterEnter

        Generated when the cursor enters the bounds of the front panel.

       Event Data Fields

       Name   Description

                  Source of the event. LabVIEW UI refers to any built-in user interface event.

          Source
                  0            LabVIEW UI


         Type    Type of event that occurred, such as Mouse Down, Value Change, Timeout, and so on.


         Time    Value of the millisecond timer when the event occurred.


           VIRef    Reference to the VI on which this event occurred.

   MouseMouse LeaveLeave

        Generated when the cursor leaves the bounds of the front panel.


10002   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10002 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10003 ordinal=10003 -->
## Property and Method Reference

Property and Method Reference

Event Data Fields

 Name   Description

         Source of the event. LabVIEW UI refers to any built-in user interface event.

 Source
         0            LabVIEW UI


 Type    Type of event that occurred, such as Mouse Down, Value Change, Timeout, and so on.


 Time    Value of the millisecond timer when the event occurred.


 VIRef    Reference to the VI on which this event occurred.

PanelPanel CloseClose

Generated when the user tries to interactively close the front panel of a VI by selecting
the Close item in the File menu or by clicking the close glyph on the window border.

If a user closes the front panel of a VI that is not being called as a subVI and does not
have any open references, LabVIEW aborts the VI. To ensure a Panel Close event case
executes completely, be sure the application opens a reference to the VI before a user
can close the front panel.

      Caution Do not use the Panel Close notify event for important shutdown
       code unless you have taken steps to ensure that the VI does not abort when
       the panel closes. Alternatively, you can use the Panel Close? filter event,
       which occurs before the panel actually closes.

An event case configured to handle a notify event cannot affect if or how LabVIEW
processes a user interaction. If you want to modify how LabVIEW processes a user

                                                    © National Instruments 10003

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10003 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10004 ordinal=10004 -->
## Property and Method Reference

Property and Method Reference

         interaction, use the Panel Close? filter event.

            Note LabVIEW cannot generate a Panel Close event for a VI being viewed or
                controlled remotely. If you are viewing or controlling a VI remotely, LabVIEW
              can generate events only for controls, not for a VI or the entire application.

       Event Data Fields

       Name   Description

                  Source of the event. LabVIEW UI refers to any built-in user interface event.

          Source
                  0            LabVIEW UI


         Type    Type of event that occurred, such as Mouse Down, Value Change, Timeout, and so on.


         Time    Value of the millisecond timer when the event occurred.


           VIRef    Reference to the VI on which this event occurred.

    PanelPanel Close?Close?

        Generated when the user tries to interactively close the front panel on a VI by selecting
        the Close item in the File menu or by clicking the close glyph on the window border.

       LabVIEW ignores the Discard? event data field if you generate this event on a subpanel
         control.

            Note LabVIEW cannot generate a Panel Close event for a VI being viewed or
                controlled remotely. If you are viewing or controlling a VI remotely, LabVIEW


10004   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10004 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10005 ordinal=10005 -->
## Property and Method Reference

Property and Method Reference


       can generate events only for controls, not for a VI or the entire application.

An event case configured to handle a filter event informs you when a user interaction
takes place before LabVIEW processes the interaction. You then can modify if or how
LabVIEW processes the interaction. If you do not want LabVIEW to inform you before it
processes a user interaction, use the Panel Close notify event.

Event Data Fields

 Name    Description

          Source of the event. LabVIEW UI refers to any built-in user interface event.

 Source
          0            LabVIEW UI


 Type    Type of event that occurred, such as Mouse Down, Value Change, Timeout, and so on.


 Time     Value of the millisecond timer when the event occurred.


 VIRef     Reference to the VI on which this event occurred.

          Allows you to prevent LabVIEW from processing the event, bypassing the behavior Discard?
          normally triggered by that event. The default is FALSE.

PanelPanel ResizeResize

Generated when the user sizes the front panel by clicking and dragging the window
frame, minimizes or maximizes the front panel, or restores the front panel to its
original size from a maximized or minimized state.

Use this event when you want to perform computations necessary for resizing front
panel objects or when you want to reduce computation and conserve display memory

                                                    © National Instruments 10005

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10005 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10006 ordinal=10006 -->
## Property and Method Reference

Property and Method Reference

      when the user minimizes the front panel. You can use the OldBnds and NewBnds
        event data field values to determine how the user resized the front panel.

       Because LabVIEW may generate multiple Panel Resize events while you resize the
       window, LabVIEW generates a final event at the end of the resizing operation in which
       OldBnds and NewBnds return the same value. You can use the values to identify in the
       code when the sizing operation finishes.

       Event Data Fields

       Name     Description

                   Source of the event. LabVIEW UI refers to any built-in user interface event.

          Source
                    0            LabVIEW UI


         Type     Type of event that occurred, such as Mouse Down, Value Change, Timeout, and so on.


         Time      Value of the millisecond timer when the event occurred.


           VIRef      Reference to the VI on which this event occurred.


                    Returns a cluster of coordinates in pixels that specify the location of the front panel
         OldBnds  before the user resized the front panel. Coordinates refer to the upper left and lower
                        right position of the front panel.


                    Returns a cluster of coordinates in pixels that specify the location of the front panel after
        NewBnds  the user resized the front panel. Coordinates refer to the upper left and lower right
                      position of the front panel.


           Act       Returns the front panel action the user performed, such as Minimized, Maximized, or


10006   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10006 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10007 ordinal=10007 -->
## Property and Method Reference

Property and Method Reference


 Name     Description

            Resized.

           Returns the previous state of the front panel, such as Standard, Minimized, or
           Maximized.

                    • Standard—The front panel window is open but is not minimized, maximized, or
               hidden.
 PrevState                    • Minimized—The front panel window is minimized.
                    • Maximized—The front panel window is maximized.

         A state of Standard or Maximized indicates that the front panel window is visible to the
             user.

PolymorphicVIPolymorphicVI

PolymorphicVI Methods

PolymorphicVI Properties
PolymorphicVIPolymorphicVI MethodsMethods


 Method          Description

 GetPolyCHImage  Returns an image depicting how the context help looks for the polymorphic VI.

GetPolyCHImageGetPolyCHImage

Returns an image depicting how the context help looks for the polymorphic VI.


                                                    © National Instruments 10007

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10007 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10008 ordinal=10008 -->
## Property and Method Reference

Property and Method Reference

       Parameters

                  Data       Name         Required  Description
                  type

           Instance                  Instance Index specifies which instance VI to use for wire types. Use -1                          Yes          Index                     to use the help description and icon for the polymorphic VI.


      Remarks

       The following table lists the characteristics of this method.


          Data type

           Available in Run-Time Engine                                         No

           Available in Real-Time Operating System                                 No

           Settable when the VI is running                                                    Yes

         Loads the front panel into memory                                     No

        Need to authenticate before use                                       No

         Loads the block diagram into memory                                   No

         Remote access allowed                                             No

         Must wait until user interface is idle                                     No

           Available with control VIs                                            No

           Available with global VIs                                            No

           Available with strict type definitions                                    No

           Available with polymorphic VIs                                                     Yes

    PolymorphicVIPolymorphicVI PropertiesProperties


          Property        Description

         Adapt To Inputs  Selects the correct polymorphic instance based on the wired input data types.

10008   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10008 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10009 ordinal=10009 -->
## Property and Method Reference

Property and Method Reference


 Property        Description

 Draw Instance               Draws the instance icon if TRUE; otherwise, draws the polymorphic VI. Icon

                Returns an array of clusters where each cluster contains information about a InstanceInfo                polymorphic VI instance at the same index.

 Show Selector   Specifies whether the polymorphic VI selector is shown when an instance of this
 By Default      polymorphic VI is added to the block diagram.

AdaptAdapt ToTo InputsInputs

Selects the correct polymorphic instance based on the wired input data types.

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

 Must wait until user interface is idle                              No

 Available with control VIs                                     No

 Available with global VIs                                     No

 Available with strict type definitions                             No

 Available with polymorphic VIs                                           Yes


                                                    © National Instruments 10009

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10009 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10010 ordinal=10010 -->
## Property and Method Reference

Property and Method Reference

    DrawDraw InstanceInstance IconIcon

       Draws the instance icon if TRUE; otherwise, draws the polymorphic VI.

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

         Must wait until user interface is idle                              No

           Available with control VIs                                     No

           Available with global VIs                                     No

           Available with strict type definitions                             No

           Available with polymorphic VIs                                           Yes

    InstanceInfoInstanceInfo

        Returns an array of clusters where each cluster contains information about a
        polymorphic VI instance at the same index.

      Remarks

       The following table lists the characteristics of this property.

10010   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10010 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10011 ordinal=10011 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                 No

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                                    Yes

 Remote access allowed                                                  Yes

 Must wait until user interface is idle                              No

 Available with control VIs                                     No

 Available with global VIs                                     No

 Available with strict type definitions                             No

 Available with polymorphic VIs                                           Yes

ShowShow SelectorSelector ByBy DefaultDefault

Specifies whether the polymorphic VI selector is shown when an instance of this
polymorphic VI is added to the block diagram.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Settable when the VI is running                                 No


                                                    © National Instruments 10011

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10011 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10012 ordinal=10012 -->
## Property and Method Reference

Property and Method Reference


         Loads the front panel into memory                              No

        Need to authenticate before use                                No

         Loads the block diagram into memory                            No

         Remote access allowed                                                  Yes

         Must wait until user interface is idle                              No

           Available with control VIs                                     No

           Available with global VIs                                     No

           Available with strict type definitions                             No

           Available with polymorphic VIs                                           Yes

       FacadeVIFacadeVI

        FacadeVI Events
    FacadeVIFacadeVI EventsEvents


          Event     Description

                   Generated on the Facade VI when the value of the XControl changes as a result of writing          Data
                     to its terminal, local variable, or Value property. LabVIEW calls the Facade VI with the         Change                new value.

           Direction  Generated on the Facade VI when the direction of the XControl changes from control to
         Change   indicator or vice versa.

           Display
                   Generated on the Facade VI when the display state of the XControl changes because the
           State
                    user invoked a property or a method on the XControl.
         Change

          Exec
                   Generated on the Facade VI when the execution state of the VI that owns the XControl
           State
                   changes from idle to running or vice versa.
         Change


10012   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10012 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10013 ordinal=10013 -->
## Property and Method Reference

Property and Method Reference

DataData ChangeChange

Generated on the Facade VI when the value of the XControl changes as a result of
writing to its terminal, local variable, or Value property. LabVIEW calls the Facade VI
with the new value.

The Data Change event is not generated when the values of controls on the Facade VI
change. Add a Value Change event to the Facade VI for these controls.

      Note LabVIEW does not call the Facade VI on every write to the terminal or
        local variable. LabVIEW calls the Facade VI when the XControl requires an
       update. You cannot build an XControl that logs data written to its terminal
       because not every value is reported to the Facade VI. Use the Value
        (Signaling) property to write values if you want the Facade VI to update on
       every value written to the XControl.

Event Data Fields

 Name   Description

         Source of the event. LabVIEW UI refers to any built-in user interface event.

 Source
         0            LabVIEW UI


 Type    Type of event that occurred, such as Mouse Down, Value Change, Timeout, and so on.


 Time    Value of the millisecond timer when the event occurred.


 VIRef    Reference to the VI on which this event occurred.


                                                    © National Instruments 10013

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10013 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10014 ordinal=10014 -->
## Property and Method Reference

Property and Method Reference

     DirectionDirection ChangeChange

        Generated on the Facade VI when the direction of the XControl changes from control to
         indicator or vice versa.

       Event Data Fields

       Name   Description

                  Source of the event. LabVIEW UI refers to any built-in user interface event.

          Source
                  0            LabVIEW UI


         Type    Type of event that occurred, such as Mouse Down, Value Change, Timeout, and so on.


         Time    Value of the millisecond timer when the event occurred.


           VIRef    Reference to the VI on which this event occurred.

    DisplayDisplay StateState ChangeChange

        Generated on the Facade VI when the display state of the XControl changes because
        the user invoked a property or a method on the XControl.

       Event Data Fields

       Name   Description

          Source  Source of the event. LabVIEW UI refers to any built-in user interface event.


10014   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10014 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10015 ordinal=10015 -->
## Property and Method Reference

Property and Method Reference


 Name   Description


         0            LabVIEW UI


 Type    Type of event that occurred, such as Mouse Down, Value Change, Timeout, and so on.


 Time    Value of the millisecond timer when the event occurred.


 VIRef    Reference to the VI on which this event occurred.

ExecExec StateState ChangeChange

Generated on the Facade VI when the execution state of the VI that owns the XControl
changes from idle to running or vice versa.

Event Data Fields

 Name   Description

         Source of the event. LabVIEW UI refers to any built-in user interface event.

 Source
         0            LabVIEW UI


 Type    Type of event that occurred, such as Mouse Down, Value Change, Timeout, and so on.


 Time    Value of the millisecond timer when the event occurred.


                                                    © National Instruments 10015

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10015 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10016 ordinal=10016 -->
## Property and Method Reference

Property and Method Reference


       Name   Description

           VIRef    Reference to the VI on which this event occurred.


       MethodVIMethodVI

       SubsystemVISubsystemVI

     VISAVISA ResourceResource PropertiesProperties

        VISA resources have a variety of properties, or attributes, with values you can read or
          set.

       You can use the Property Node to read or set the values of VISA properties.

         After you place a Property Node on the block diagram, wire a VISA session to the
        reference input of the Property Node. After you wire a session to the reference input of
        the Property Node, LabVIEW sets the VISA Class to the class associated with that
         session.

       To optionally change the VISA class, right-click the Property Node and select Select
        Class»VISA»I/O Session from the shortcut menu. The default is Instr class, which
       encompasses all VISA properties for instruments. The other classes limit the properties
        displayed in the shortcut menu to those related to the selected class. In general,
        choosing a more specific instrument class is optional. Notice that for some classes, for
        example, Backplane and BoardInterface, properties and methods do not
        appear in the Instr class because there is no logical overlap. Therefore, for classes
        such as these, choosing the appropriate class is mandatory.

       The two basic types of VISA properties are global properties and local properties.
        Global properties are specific to a resource, and local properties are specific to a
         session. A global property has the same value for all the sessions that are open to a
         specific resource. A local property can have a different value for each session to a
         specific resource.

        Refer to the following class names for more information about the properties in each

10016   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10016 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10017 ordinal=10017 -->
## Property and Method Reference

Property and Method Reference

VISA class.

© 2005–2023 National Instruments Corporation. All rights reserved. Refer to the
<National Instruments>\_Legal Information directory for information
about NI copyright, patents, trademarks, warranties, product warnings, and export
compliance.

EventEvent ClassClass PropertiesProperties


 Property             Description

 Event                      Returns the unique logical identifier for the event type of the specified Information:Event
                       event. Type

 Version
 Information:Resource Returns the VXI manufacturer ID of the manufacturer that created the VISA
 Manufacturer         implementation.
 Identification

                      Returns the name of the manufacturer that created the implementation.
 Version               This is not related to the device manufacturer attributes. Note: Use the
 Information:Resource  value of this property for display purposes only and not for programmatic
 Manufacturer Name   decisions. The value can change between VISA implementations and/or
                         revisions.

                      Returns the version of a given implementation. This value is defined by the
 Version                individual manufacturer and increments with each new revision. The format
 Information:Version   of the value has the upper 12 bits as the major number of the version, the
 of Implementation    next lower 12 bits as the minor number of the version, and the lowest 8 bits
                      as the sub-minor number of the version.

                      Returns the value that uniquely identifies the version of the VISA
 Version                specification to which the implementation complies. The format of the
 Information:Version   value has the upper 12 bits as the major number of the version, the next
 of Specification       lower 12 bits as the minor number of the version, and the lowest 8 bits as
                      the sub-minor number of the version.

ClearClear EventEvent PropertiesProperties


                                                    © National Instruments 10017

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10017 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10018 ordinal=10018 -->
## Property and Method Reference

Property and Method Reference


          Property             Description

          Event                               Returns the unique logical identifier for the event type of the specified          Information:Event                                 event.         Type

           Version
          Information:Resource Returns the VXI manufacturer ID of the manufacturer that created the VISA
          Manufacturer         implementation.
            Identification

                               Returns the name of the manufacturer that created the implementation.
           Version               This is not related to the device manufacturer attributes. Note: Use the
          Information:Resource  value of this property for display purposes only and not for programmatic
          Manufacturer Name   decisions. The value can change between VISA implementations and/or
                                    revisions.

                               Returns the version of a given implementation. This value is defined by the
           Version                individual manufacturer and increments with each new revision. The format
           Information:Version   of the value has the upper 12 bits as the major number of the version, the
           of Implementation    next lower 12 bits as the minor number of the version, and the lowest 8 bits
                               as the sub-minor number of the version.

                               Returns the value that uniquely identifies the version of the VISA
           Version                specification to which the implementation complies. The format of the
           Information:Version   value has the upper 12 bits as the major number of the version, the next
           of Specification       lower 12 bits as the minor number of the version, and the lowest 8 bits as
                               the sub-minor number of the version.

    EventEvent Information:EventInformation:Event TypeType

        Returns the unique logical identifier for the event type of the specified event.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes


10018   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10018 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10019 ordinal=10019 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                                   Yes


 Service Request                                  1073684491

 Trigger                                          3221168138

 Clear                                           1073684493

 VXI Signal                                       1073684512

 VXI/VME Interrupt                                 3221168161

 VXI/VME Sysfail                                   1073684509

 VXI/VME Sysreset                                 1073684510

 GPIB CIC                                        1073684498

 GPIB Talk                                        1073684499

 GPIB Listen                                      1073684500

 PXI Interrupt                                     1073684514

 Serial Break                                      1073684515

 Serial TermChar                                  1073684516

 Serial CTS                                       1073684521

 Serial DSR                                       1073684522

 Serial DCD                                       1073684524

 Serial RI                                         1073684526

 Serial Character                                  1073684533

 USB Interrupt                                    1073684535

 All Enabled                                      1073709055

VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
IdentificationIdentification

Returns the VXI manufacturer ID of the manufacturer that created the VISA
implementation.

                                                    © National Instruments 10019

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10019 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10020 ordinal=10020 -->
## Property and Method Reference

Property and Method Reference

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
   NameName

        Returns the name of the manufacturer that created the implementation. This is not
         related to the device manufacturer attributes. Note: Use the value of this property for
         display purposes only and not for programmatic decisions. The value can change
       between VISA implementations and/or revisions.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    VersionVersion Information:VersionInformation:Version ofof
    ImplementationImplementation

        Returns the version of a given implementation. This value is defined by the individual

10020   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10020 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10021 ordinal=10021 -->
## Property and Method Reference

Property and Method Reference

manufacturer and increments with each new revision. The format of the value has the
upper 12 bits as the major number of the version, the next lower 12 bits as the minor
number of the version, and the lowest 8 bits as the sub-minor number of the version.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VersionVersion Information:VersionInformation:Version ofof SpecificationSpecification

Returns the value that uniquely identifies the version of the VISA specification to which
the implementation complies. The format of the value has the upper 12 bits as the
major number of the version, the next lower 12 bits as the minor number of the
version, and the lowest 8 bits as the sub-minor number of the version.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

GenericGeneric EventEvent PropertiesProperties


                                                    © National Instruments 10021

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10021 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10022 ordinal=10022 -->
## Property and Method Reference

Property and Method Reference


          Property             Description

          Event                               Returns the unique logical identifier for the event type of the specified          Information:Event                                 event.         Type

          Event                               Returns the 32-bit status/ID retrieved during the IACK cycle. This is valid
           Information:Interrupt                                only for the VXI/VME Interrupt event.           Status ID

          Event
           Information:PXI/PCI   Returns the first PXI/PCI register read in the successful interrupt detection
          Received Interrupt    sequence.
          Data

          Event
           Information:PXI/PCI   Returns the index of the interrupt sequence that detected the interrupt
          Received Interrupt     condition.
         Sequence

          Event                               Returns the CIC status of either gained (TRUE) or lost (FALSE). This is valid
          Information:Received                                only for the GPIB CIC event.          CIC State

          Event                               Returns the VXI interrupt level on which the interrupt was received. This is          Information:Received
                                    valid only for the VXI/VME Interrupt event.           Interrupt Level

          Event
                               Returns the triggering mechanism on which the specified trigger event was          Information:Received                                  received. This is valid only for the Trigger event.           Trigger ID

          Event                               Returns the 16-bit Status/ID value retrieved during the IACK cycle or from           Information:Signal
                               the Signal register. This is valid only for the VXI Signal event.
          Processor Status ID

          Event
                               Returns the VISA status code of the specified event.
           Information:Status

          Event
          Information:USB
                               Returns the number of bytes of USB interrupt data stored.
          Received Interrupt
           Size

           Version
          Information:Resource Returns the VXI manufacturer ID of the manufacturer that created the VISA
          Manufacturer         implementation.
            Identification

10022   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10022 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10023 ordinal=10023 -->
## Property and Method Reference

Property and Method Reference


 Property             Description

                      Returns the name of the manufacturer that created the implementation.
 Version               This is not related to the device manufacturer attributes. Note: Use the
 Information:Resource  value of this property for display purposes only and not for programmatic
 Manufacturer Name   decisions. The value can change between VISA implementations and/or
                         revisions.

                      Returns the version of a given implementation. This value is defined by the
 Version                individual manufacturer and increments with each new revision. The format
 Information:Version   of the value has the upper 12 bits as the major number of the version, the
 of Implementation    next lower 12 bits as the minor number of the version, and the lowest 8 bits
                      as the sub-minor number of the version.

                      Returns the value that uniquely identifies the version of the VISA
 Version                specification to which the implementation complies. The format of the
 Information:Version   value has the upper 12 bits as the major number of the version, the next
 of Specification       lower 12 bits as the minor number of the version, and the lowest 8 bits as
                      the sub-minor number of the version.

EventEvent Information:EventInformation:Event TypeType

Returns the unique logical identifier for the event type of the specified event.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


 Service Request                                  1073684491

 Trigger                                          3221168138

 Clear                                           1073684493

 VXI Signal                                       1073684512

                                                    © National Instruments 10023

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10023 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10024 ordinal=10024 -->
## Property and Method Reference

Property and Method Reference


         VXI/VME Interrupt                                 3221168161

         VXI/VME Sysfail                                   1073684509

         VXI/VME Sysreset                                 1073684510

         GPIB CIC                                        1073684498

         GPIB Talk                                        1073684499

         GPIB Listen                                      1073684500

          PXI Interrupt                                     1073684514

           Serial Break                                      1073684515

           Serial TermChar                                  1073684516

           Serial CTS                                       1073684521

           Serial DSR                                       1073684522

           Serial DCD                                       1073684524

           Serial RI                                         1073684526

           Serial Character                                  1073684533

        USB Interrupt                                    1073684535

             All Enabled                                      1073709055

    EventEvent Information:InterruptInformation:Interrupt StatusStatus IDID

        Returns the 32-bit status/ID retrieved during the IACK cycle. This is valid only for the
        VXI/VME Interrupt event.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

10024   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10024 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10025 ordinal=10025 -->
## Property and Method Reference

Property and Method Reference

EventEvent Information:PXI/PCIInformation:PXI/PCI ReceivedReceived InterruptInterrupt
DataData

Returns the first PXI/PCI register read in the successful interrupt detection sequence.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

EventEvent Information:PXI/PCIInformation:PXI/PCI ReceivedReceived InterruptInterrupt
SequenceSequence

Returns the index of the interrupt sequence that detected the interrupt condition.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


                                                    © National Instruments 10025

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10025 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10026 ordinal=10026 -->
## Property and Method Reference

Property and Method Reference

    EventEvent Information:ReceivedInformation:Received CICCIC StateState

        Returns the CIC status of either gained (TRUE) or lost (FALSE). This is valid only for the
       GPIB CIC event.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    EventEvent Information:ReceivedInformation:Received InterruptInterrupt LevelLevel

        Returns the VXI interrupt level on which the interrupt was received. This is valid only
         for the VXI/VME Interrupt event.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    EventEvent Information:ReceivedInformation:Received TriggerTrigger IDID

        Returns the triggering mechanism on which the specified trigger event was received.


10026   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10026 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10027 ordinal=10027 -->
## Property and Method Reference

Property and Method Reference

This is valid only for the Trigger event.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


 Software                                                             -1

 TTL0                                                     0

 TTL1                                                     1

 TTL2                                                     2

 TTL3                                                     3

 TTL4                                                     4

 TTL5                                                     5

 TTL6                                                     6

 TTL7                                                     7

 ECL0                                                     8

 ECL1                                                     9

EventEvent Information:SignalInformation:Signal ProcessorProcessor StatusStatus IDID

Returns the 16-bit Status/ID value retrieved during the IACK cycle or from the Signal
register. This is valid only for the VXI Signal event.

Remarks

The following table lists the characteristics of this property.

                                                    © National Instruments 10027

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10027 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10028 ordinal=10028 -->
## Property and Method Reference

Property and Method Reference


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    EventEvent Information:StatusInformation:Status

        Returns the VISA status code of the specified event.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    EventEvent Information:USBInformation:USB ReceivedReceived InterruptInterrupt
     SizeSize

        Returns the number of bytes of USB interrupt data stored.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes


10028   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10028 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10029 ordinal=10029 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                                   Yes

VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
IdentificationIdentification

Returns the VXI manufacturer ID of the manufacturer that created the VISA
implementation.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
NameName

Returns the name of the manufacturer that created the implementation. This is not
related to the device manufacturer attributes. Note: Use the value of this property for
display purposes only and not for programmatic decisions. The value can change
between VISA implementations and/or revisions.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

                                                    © National Instruments 10029

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10029 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10030 ordinal=10030 -->
## Property and Method Reference

Property and Method Reference


           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    VersionVersion Information:VersionInformation:Version ofof
    ImplementationImplementation

        Returns the version of a given implementation. This value is defined by the individual
        manufacturer and increments with each new revision. The format of the value has the
       upper 12 bits as the major number of the version, the next lower 12 bits as the minor
       number of the version, and the lowest 8 bits as the sub-minor number of the version.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    VersionVersion Information:VersionInformation:Version ofof SpecificationSpecification

        Returns the value that uniquely identifies the version of the VISA specification to which
        the implementation complies. The format of the value has the upper 12 bits as the
       major number of the version, the next lower 12 bits as the minor number of the
         version, and the lowest 8 bits as the sub-minor number of the version.

      Remarks

       The following table lists the characteristics of this property.


          Data type

10030   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10030 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10031 ordinal=10031 -->
## Property and Method Reference

Property and Method Reference


 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

GPIBGPIB CICCIC EventEvent PropertiesProperties


 Property             Description

 Event                      Returns the unique logical identifier for the event type of the specified Information:Event                       event. Type

 Event
                      Returns the CIC status of either gained (TRUE) or lost (FALSE). This is valid Information:Received                      only for the GPIB CIC Event. CIC State

 Version
 Information:Resource Returns the VXI manufacturer ID of the manufacturer that created the VISA
 Manufacturer         implementation.
 Identification

                      Returns the name of the manufacturer that created the implementation.
 Version               This is not related to the device manufacturer attributes. Note: Use the
 Information:Resource  value of this property for display purposes only and not for programmatic
 Manufacturer Name   decisions. The value can change between VISA implementations and/or
                         revisions.

                      Returns the version of a given implementation. This value is defined by the
 Version                individual manufacturer and increments with each new revision. The format
 Information:Version   of the value has the upper 12 bits as the major number of the version, the
 of Implementation    next lower 12 bits as the minor number of the version, and the lowest 8 bits
                      as the sub-minor number of the version.

                      Returns the value that uniquely identifies the version of the VISA
 Version                specification to which the implementation complies. The format of the
 Information:Version   value has the upper 12 bits as the major number of the version, the next
 of Specification       lower 12 bits as the minor number of the version, and the lowest 8 bits as
                      the sub-minor number of the version.


                                                    © National Instruments 10031

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10031 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10032 ordinal=10032 -->
## Property and Method Reference

Property and Method Reference

    EventEvent Information:EventInformation:Event TypeType

        Returns the unique logical identifier for the event type of the specified event.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


          Service Request                                  1073684491

           Trigger                                          3221168138

          Clear                                           1073684493

          VXI Signal                                       1073684512

         VXI/VME Interrupt                                 3221168161

         VXI/VME Sysfail                                   1073684509

         VXI/VME Sysreset                                 1073684510

         GPIB CIC                                        1073684498

         GPIB Talk                                        1073684499

         GPIB Listen                                      1073684500

          PXI Interrupt                                     1073684514

           Serial Break                                      1073684515

           Serial TermChar                                  1073684516

           Serial CTS                                       1073684521

           Serial DSR                                       1073684522

           Serial DCD                                       1073684524


10032   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10032 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10033 ordinal=10033 -->
## Property and Method Reference

Property and Method Reference


 Serial RI                                         1073684526

 Serial Character                                  1073684533

 USB Interrupt                                    1073684535

 All Enabled                                      1073709055

EventEvent Information:ReceivedInformation:Received CICCIC StateState

Returns the CIC status of either gained (TRUE) or lost (FALSE). This is valid only for the
GPIB CIC Event.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
IdentificationIdentification

Returns the VXI manufacturer ID of the manufacturer that created the VISA
implementation.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

                                                    © National Instruments 10033

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10033 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10034 ordinal=10034 -->
## Property and Method Reference

Property and Method Reference


           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
   NameName

        Returns the name of the manufacturer that created the implementation. This is not
         related to the device manufacturer attributes. Note: Use the value of this property for
         display purposes only and not for programmatic decisions. The value can change
       between VISA implementations and/or revisions.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    VersionVersion Information:VersionInformation:Version ofof
    ImplementationImplementation

        Returns the version of a given implementation. This value is defined by the individual
        manufacturer and increments with each new revision. The format of the value has the
       upper 12 bits as the major number of the version, the next lower 12 bits as the minor
       number of the version, and the lowest 8 bits as the sub-minor number of the version.

      Remarks

       The following table lists the characteristics of this property.

10034   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10034 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10035 ordinal=10035 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VersionVersion Information:VersionInformation:Version ofof SpecificationSpecification

Returns the value that uniquely identifies the version of the VISA specification to which
the implementation complies. The format of the value has the upper 12 bits as the
major number of the version, the next lower 12 bits as the minor number of the
version, and the lowest 8 bits as the sub-minor number of the version.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

GPIBGPIB ListenListen EventEvent PropertiesProperties


 Property             Description

 Event
                      Returns the unique logical identifier for the event type of the specified
 Information:Event
                       event.
 Type

 Version
 Information:Resource Returns the VXI manufacturer ID of the manufacturer that created the VISA
 Manufacturer         implementation.
 Identification

 Version              Returns the name of the manufacturer that created the implementation.


                                                    © National Instruments 10035

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10035 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10036 ordinal=10036 -->
## Property and Method Reference

Property and Method Reference


          Property             Description

                                 This is not related to the device manufacturer attributes. Note: Use the
          Information:Resource  value of this property for display purposes only and not for programmatic
          Manufacturer Name   decisions. The value can change between VISA implementations and/or
                                    revisions.

                               Returns the version of a given implementation. This value is defined by the
           Version                individual manufacturer and increments with each new revision. The format
           Information:Version   of the value has the upper 12 bits as the major number of the version, the
           of Implementation    next lower 12 bits as the minor number of the version, and the lowest 8 bits
                               as the sub-minor number of the version.

                               Returns the value that uniquely identifies the version of the VISA
           Version                specification to which the implementation complies. The format of the
           Information:Version   value has the upper 12 bits as the major number of the version, the next
           of Specification       lower 12 bits as the minor number of the version, and the lowest 8 bits as
                               the sub-minor number of the version.

    EventEvent Information:EventInformation:Event TypeType

        Returns the unique logical identifier for the event type of the specified event.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


          Service Request                                  1073684491

           Trigger                                          3221168138

          Clear                                           1073684493

          VXI Signal                                       1073684512


10036   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10036 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10037 ordinal=10037 -->
## Property and Method Reference

Property and Method Reference


 VXI/VME Interrupt                                 3221168161

 VXI/VME Sysfail                                   1073684509

 VXI/VME Sysreset                                 1073684510

 GPIB CIC                                        1073684498

 GPIB Talk                                        1073684499

 GPIB Listen                                      1073684500

 PXI Interrupt                                     1073684514

 Serial Break                                      1073684515

 Serial TermChar                                  1073684516

 Serial CTS                                       1073684521

 Serial DSR                                       1073684522

 Serial DCD                                       1073684524

 Serial RI                                         1073684526

 Serial Character                                  1073684533

 USB Interrupt                                    1073684535

 All Enabled                                      1073709055

VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
IdentificationIdentification

Returns the VXI manufacturer ID of the manufacturer that created the VISA
implementation.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only


                                                    © National Instruments 10037

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10037 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10038 ordinal=10038 -->
## Property and Method Reference

Property and Method Reference


           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
   NameName

        Returns the name of the manufacturer that created the implementation. This is not
         related to the device manufacturer attributes. Note: Use the value of this property for
         display purposes only and not for programmatic decisions. The value can change
       between VISA implementations and/or revisions.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    VersionVersion Information:VersionInformation:Version ofof
    ImplementationImplementation

        Returns the version of a given implementation. This value is defined by the individual
        manufacturer and increments with each new revision. The format of the value has the
       upper 12 bits as the major number of the version, the next lower 12 bits as the minor
       number of the version, and the lowest 8 bits as the sub-minor number of the version.

      Remarks

       The following table lists the characteristics of this property.

10038   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10038 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10039 ordinal=10039 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VersionVersion Information:VersionInformation:Version ofof SpecificationSpecification

Returns the value that uniquely identifies the version of the VISA specification to which
the implementation complies. The format of the value has the upper 12 bits as the
major number of the version, the next lower 12 bits as the minor number of the
version, and the lowest 8 bits as the sub-minor number of the version.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

GPIBGPIB TalkTalk EventEvent PropertiesProperties


 Property             Description

 Event
                      Returns the unique logical identifier for the event type of the specified
 Information:Event
                       event.
 Type

 Version
 Information:Resource Returns the VXI manufacturer ID of the manufacturer that created the VISA
 Manufacturer         implementation.
 Identification

 Version              Returns the name of the manufacturer that created the implementation.


                                                    © National Instruments 10039

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10039 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10040 ordinal=10040 -->
## Property and Method Reference

Property and Method Reference


          Property             Description

                                 This is not related to the device manufacturer attributes. Note: Use the
          Information:Resource  value of this property for display purposes only and not for programmatic
          Manufacturer Name   decisions. The value can change between VISA implementations and/or
                                    revisions.

                               Returns the version of a given implementation. This value is defined by the
           Version                individual manufacturer and increments with each new revision. The format
           Information:Version   of the value has the upper 12 bits as the major number of the version, the
           of Implementation    next lower 12 bits as the minor number of the version, and the lowest 8 bits
                               as the sub-minor number of the version.

                               Returns the value that uniquely identifies the version of the VISA
           Version                specification to which the implementation complies. The format of the
           Information:Version   value has the upper 12 bits as the major number of the version, the next
           of Specification       lower 12 bits as the minor number of the version, and the lowest 8 bits as
                               the sub-minor number of the version.

    EventEvent Information:EventInformation:Event TypeType

        Returns the unique logical identifier for the event type of the specified event.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


          Service Request                                  1073684491

           Trigger                                          3221168138

          Clear                                           1073684493

          VXI Signal                                       1073684512


10040   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10040 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10041 ordinal=10041 -->
## Property and Method Reference

Property and Method Reference


 VXI/VME Interrupt                                 3221168161

 VXI/VME Sysfail                                   1073684509

 VXI/VME Sysreset                                 1073684510

 GPIB CIC                                        1073684498

 GPIB Talk                                        1073684499

 GPIB Listen                                      1073684500

 PXI Interrupt                                     1073684514

 Serial Break                                      1073684515

 Serial TermChar                                  1073684516

 Serial CTS                                       1073684521

 Serial DSR                                       1073684522

 Serial DCD                                       1073684524

 Serial RI                                         1073684526

 Serial Character                                  1073684533

 USB Interrupt                                    1073684535

 All Enabled                                      1073709055

VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
IdentificationIdentification

Returns the VXI manufacturer ID of the manufacturer that created the VISA
implementation.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only


                                                    © National Instruments 10041

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10041 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10042 ordinal=10042 -->
## Property and Method Reference

Property and Method Reference


           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
   NameName

        Returns the name of the manufacturer that created the implementation. This is not
         related to the device manufacturer attributes. Note: Use the value of this property for
         display purposes only and not for programmatic decisions. The value can change
       between VISA implementations and/or revisions.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    VersionVersion Information:VersionInformation:Version ofof
    ImplementationImplementation

        Returns the version of a given implementation. This value is defined by the individual
        manufacturer and increments with each new revision. The format of the value has the
       upper 12 bits as the major number of the version, the next lower 12 bits as the minor
       number of the version, and the lowest 8 bits as the sub-minor number of the version.

      Remarks

       The following table lists the characteristics of this property.

10042   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10042 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10043 ordinal=10043 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VersionVersion Information:VersionInformation:Version ofof SpecificationSpecification

Returns the value that uniquely identifies the version of the VISA specification to which
the implementation complies. The format of the value has the upper 12 bits as the
major number of the version, the next lower 12 bits as the minor number of the
version, and the lowest 8 bits as the sub-minor number of the version.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

PXIPXI InterruptInterrupt EventEvent PropertiesProperties


 Property             Description

 Event
                      Returns the unique logical identifier for the event type of the specified
 Information:Event
                       event.
 Type

 Event
 Information:PXI/PCI   Returns the first PXI/PCI register read in the successful interrupt detection
 Received Interrupt    sequence.
 Data

 Event                Returns the index of the interrupt sequence that detected the interrupt


                                                    © National Instruments 10043

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10043 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10044 ordinal=10044 -->
## Property and Method Reference

Property and Method Reference


          Property             Description

           Information:PXI/PCI
          Received Interrupt     condition.
         Sequence

           Version
          Information:Resource Returns the VXI manufacturer ID of the manufacturer that created the VISA
          Manufacturer         implementation.
            Identification

                               Returns the name of the manufacturer that created the implementation.
           Version               This is not related to the device manufacturer attributes. Note: Use the
          Information:Resource  value of this property for display purposes only and not for programmatic
          Manufacturer Name   decisions. The value can change between VISA implementations and/or
                                    revisions.

                               Returns the version of a given implementation. This value is defined by the
           Version                individual manufacturer and increments with each new revision. The format
           Information:Version   of the value has the upper 12 bits as the major number of the version, the
           of Implementation    next lower 12 bits as the minor number of the version, and the lowest 8 bits
                               as the sub-minor number of the version.

                               Returns the value that uniquely identifies the version of the VISA
           Version                specification to which the implementation complies. The format of the
           Information:Version   value has the upper 12 bits as the major number of the version, the next
           of Specification       lower 12 bits as the minor number of the version, and the lowest 8 bits as
                               the sub-minor number of the version.

    EventEvent Information:EventInformation:Event TypeType

        Returns the unique logical identifier for the event type of the specified event.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes


10044   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10044 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10045 ordinal=10045 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                                   Yes


 Service Request                                  1073684491

 Trigger                                          3221168138

 Clear                                           1073684493

 VXI Signal                                       1073684512

 VXI/VME Interrupt                                 3221168161

 VXI/VME Sysfail                                   1073684509

 VXI/VME Sysreset                                 1073684510

 GPIB CIC                                        1073684498

 GPIB Talk                                        1073684499

 GPIB Listen                                      1073684500

 PXI Interrupt                                     1073684514

 Serial Break                                      1073684515

 Serial TermChar                                  1073684516

 Serial CTS                                       1073684521

 Serial DSR                                       1073684522

 Serial DCD                                       1073684524

 Serial RI                                         1073684526

 Serial Character                                  1073684533

 USB Interrupt                                    1073684535

 All Enabled                                      1073709055

EventEvent Information:PXI/PCIInformation:PXI/PCI ReceivedReceived InterruptInterrupt
DataData

Returns the first PXI/PCI register read in the successful interrupt detection sequence.


                                                    © National Instruments 10045

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10045 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10046 ordinal=10046 -->
## Property and Method Reference

Property and Method Reference

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    EventEvent Information:PXI/PCIInformation:PXI/PCI ReceivedReceived InterruptInterrupt
    SequenceSequence

        Returns the index of the interrupt sequence that detected the interrupt condition.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
     IdentificationIdentification

        Returns the VXI manufacturer ID of the manufacturer that created the VISA
        implementation.


10046   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10046 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10047 ordinal=10047 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
NameName

Returns the name of the manufacturer that created the implementation. This is not
related to the device manufacturer attributes. Note: Use the value of this property for
display purposes only and not for programmatic decisions. The value can change
between VISA implementations and/or revisions.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VersionVersion Information:VersionInformation:Version ofof
ImplementationImplementation

Returns the version of a given implementation. This value is defined by the individual

                                                    © National Instruments 10047

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10047 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10048 ordinal=10048 -->
## Property and Method Reference

Property and Method Reference

        manufacturer and increments with each new revision. The format of the value has the
       upper 12 bits as the major number of the version, the next lower 12 bits as the minor
       number of the version, and the lowest 8 bits as the sub-minor number of the version.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    VersionVersion Information:VersionInformation:Version ofof SpecificationSpecification

        Returns the value that uniquely identifies the version of the VISA specification to which
        the implementation complies. The format of the value has the upper 12 bits as the
       major number of the version, the next lower 12 bits as the minor number of the
         version, and the lowest 8 bits as the sub-minor number of the version.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

       ServiceService RequestRequest EventEvent PropertiesProperties


10048   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10048 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10049 ordinal=10049 -->
## Property and Method Reference

Property and Method Reference


 Property             Description

 Event                      Returns the unique logical identifier for the event type of the specified Information:Event                       event. Type

 Version
 Information:Resource Returns the VXI manufacturer ID of the manufacturer that created the VISA
 Manufacturer         implementation.
 Identification

                      Returns the name of the manufacturer that created the implementation.
 Version               This is not related to the device manufacturer attributes. Note: Use the
 Information:Resource  value of this property for display purposes only and not for programmatic
 Manufacturer Name   decisions. The value can change between VISA implementations and/or
                         revisions.

                      Returns the version of a given implementation. This value is defined by the
 Version                individual manufacturer and increments with each new revision. The format
 Information:Version   of the value has the upper 12 bits as the major number of the version, the
 of Implementation    next lower 12 bits as the minor number of the version, and the lowest 8 bits
                      as the sub-minor number of the version.

                      Returns the value that uniquely identifies the version of the VISA
 Version                specification to which the implementation complies. The format of the
 Information:Version   value has the upper 12 bits as the major number of the version, the next
 of Specification       lower 12 bits as the minor number of the version, and the lowest 8 bits as
                      the sub-minor number of the version.

EventEvent Information:EventInformation:Event TypeType

Returns the unique logical identifier for the event type of the specified event.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes


                                                    © National Instruments 10049

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10049 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10050 ordinal=10050 -->
## Property and Method Reference

Property and Method Reference


           Available in Real-Time Operating System                                   Yes


          Service Request                                  1073684491

           Trigger                                          3221168138

          Clear                                           1073684493

          VXI Signal                                       1073684512

         VXI/VME Interrupt                                 3221168161

         VXI/VME Sysfail                                   1073684509

         VXI/VME Sysreset                                 1073684510

         GPIB CIC                                        1073684498

         GPIB Talk                                        1073684499

         GPIB Listen                                      1073684500

          PXI Interrupt                                     1073684514

           Serial Break                                      1073684515

           Serial TermChar                                  1073684516

           Serial CTS                                       1073684521

           Serial DSR                                       1073684522

           Serial DCD                                       1073684524

           Serial RI                                         1073684526

           Serial Character                                  1073684533

        USB Interrupt                                    1073684535

             All Enabled                                      1073709055

    VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
     IdentificationIdentification

        Returns the VXI manufacturer ID of the manufacturer that created the VISA
        implementation.

10050   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10050 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10051 ordinal=10051 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
NameName

Returns the name of the manufacturer that created the implementation. This is not
related to the device manufacturer attributes. Note: Use the value of this property for
display purposes only and not for programmatic decisions. The value can change
between VISA implementations and/or revisions.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VersionVersion Information:VersionInformation:Version ofof
ImplementationImplementation

Returns the version of a given implementation. This value is defined by the individual

                                                    © National Instruments 10051

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10051 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10052 ordinal=10052 -->
## Property and Method Reference

Property and Method Reference

        manufacturer and increments with each new revision. The format of the value has the
       upper 12 bits as the major number of the version, the next lower 12 bits as the minor
       number of the version, and the lowest 8 bits as the sub-minor number of the version.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    VersionVersion Information:VersionInformation:Version ofof SpecificationSpecification

        Returns the value that uniquely identifies the version of the VISA specification to which
        the implementation complies. The format of the value has the upper 12 bits as the
       major number of the version, the next lower 12 bits as the minor number of the
         version, and the lowest 8 bits as the sub-minor number of the version.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

       TriggerTrigger EventEvent PropertiesProperties


10052   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10052 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10053 ordinal=10053 -->
## Property and Method Reference

Property and Method Reference


 Property             Description

 Event                      Returns the unique logical identifier for the event type of the specified Information:Event                       event. Type

 Event                      Returns the triggering mechanism on which the specified trigger event was
 Information:Received                        received. This is valid only for the Trigger event. Trigger ID

 Version
 Information:Resource Returns the VXI manufacturer ID of the manufacturer that created the VISA
 Manufacturer         implementation.
 Identification

                      Returns the name of the manufacturer that created the implementation.
 Version               This is not related to the device manufacturer attributes. Note: Use the
 Information:Resource  value of this property for display purposes only and not for programmatic
 Manufacturer Name   decisions. The value can change between VISA implementations and/or
                         revisions.

                      Returns the version of a given implementation. This value is defined by the
 Version                individual manufacturer and increments with each new revision. The format
 Information:Version   of the value has the upper 12 bits as the major number of the version, the
 of Implementation    next lower 12 bits as the minor number of the version, and the lowest 8 bits
                      as the sub-minor number of the version.

                      Returns the value that uniquely identifies the version of the VISA
 Version                specification to which the implementation complies. The format of the
 Information:Version   value has the upper 12 bits as the major number of the version, the next
 of Specification       lower 12 bits as the minor number of the version, and the lowest 8 bits as
                      the sub-minor number of the version.

EventEvent Information:EventInformation:Event TypeType

Returns the unique logical identifier for the event type of the specified event.

Remarks

The following table lists the characteristics of this property.


 Data type


                                                    © National Instruments 10053

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10053 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10054 ordinal=10054 -->
## Property and Method Reference

Property and Method Reference


          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


          Service Request                                  1073684491

           Trigger                                          3221168138

          Clear                                           1073684493

          VXI Signal                                       1073684512

         VXI/VME Interrupt                                 3221168161

         VXI/VME Sysfail                                   1073684509

         VXI/VME Sysreset                                 1073684510

         GPIB CIC                                        1073684498

         GPIB Talk                                        1073684499

         GPIB Listen                                      1073684500

          PXI Interrupt                                     1073684514

           Serial Break                                      1073684515

           Serial TermChar                                  1073684516

           Serial CTS                                       1073684521

           Serial DSR                                       1073684522

           Serial DCD                                       1073684524

           Serial RI                                         1073684526

           Serial Character                                  1073684533

        USB Interrupt                                    1073684535

             All Enabled                                      1073709055

    EventEvent Information:ReceivedInformation:Received TriggerTrigger IDID

        Returns the triggering mechanism on which the specified trigger event was received.


10054   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10054 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10055 ordinal=10055 -->
## Property and Method Reference

Property and Method Reference

This is valid only for the Trigger event.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


 Software                                                             -1

 TTL0                                                     0

 TTL1                                                     1

 TTL2                                                     2

 TTL3                                                     3

 TTL4                                                     4

 TTL5                                                     5

 TTL6                                                     6

 TTL7                                                     7

 ECL0                                                     8

 ECL1                                                     9

VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
IdentificationIdentification

Returns the VXI manufacturer ID of the manufacturer that created the VISA
implementation.


                                                    © National Instruments 10055

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10055 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10056 ordinal=10056 -->
## Property and Method Reference

Property and Method Reference

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
   NameName

        Returns the name of the manufacturer that created the implementation. This is not
         related to the device manufacturer attributes. Note: Use the value of this property for
         display purposes only and not for programmatic decisions. The value can change
       between VISA implementations and/or revisions.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    VersionVersion Information:VersionInformation:Version ofof
    ImplementationImplementation

        Returns the version of a given implementation. This value is defined by the individual

10056   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10056 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10057 ordinal=10057 -->
## Property and Method Reference

Property and Method Reference

manufacturer and increments with each new revision. The format of the value has the
upper 12 bits as the major number of the version, the next lower 12 bits as the minor
number of the version, and the lowest 8 bits as the sub-minor number of the version.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VersionVersion Information:VersionInformation:Version ofof SpecificationSpecification

Returns the value that uniquely identifies the version of the VISA specification to which
the implementation complies. The format of the value has the upper 12 bits as the
major number of the version, the next lower 12 bits as the minor number of the
version, and the lowest 8 bits as the sub-minor number of the version.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

USBUSB InterruptInterrupt EventEvent PropertiesProperties


                                                    © National Instruments 10057

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10057 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10058 ordinal=10058 -->
## Property and Method Reference

Property and Method Reference


          Property             Description

          Event                               Returns the unique logical identifier for the event type of the specified          Information:Event                                 event.         Type

          Event                               Returns the VISA status code of the specified event.
           Information:Status

          Event
          Information:USB                               Returns the number of bytes of USB interrupt data stored.          Received Interrupt
           Size

           Version
          Information:Resource Returns the VXI manufacturer ID of the manufacturer that created the VISA
          Manufacturer         implementation.
            Identification

                               Returns the name of the manufacturer that created the implementation.
           Version               This is not related to the device manufacturer attributes. Note: Use the
          Information:Resource  value of this property for display purposes only and not for programmatic
          Manufacturer Name   decisions. The value can change between VISA implementations and/or
                                    revisions.

                               Returns the version of a given implementation. This value is defined by the
           Version                individual manufacturer and increments with each new revision. The format
           Information:Version   of the value has the upper 12 bits as the major number of the version, the
           of Implementation    next lower 12 bits as the minor number of the version, and the lowest 8 bits
                               as the sub-minor number of the version.

                               Returns the value that uniquely identifies the version of the VISA
           Version                specification to which the implementation complies. The format of the
           Information:Version   value has the upper 12 bits as the major number of the version, the next
           of Specification       lower 12 bits as the minor number of the version, and the lowest 8 bits as
                               the sub-minor number of the version.

    EventEvent Information:EventInformation:Event TypeType

        Returns the unique logical identifier for the event type of the specified event.


10058   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10058 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10059 ordinal=10059 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


 Service Request                                  1073684491

 Trigger                                          3221168138

 Clear                                           1073684493

 VXI Signal                                       1073684512

 VXI/VME Interrupt                                 3221168161

 VXI/VME Sysfail                                   1073684509

 VXI/VME Sysreset                                 1073684510

 GPIB CIC                                        1073684498

 GPIB Talk                                        1073684499

 GPIB Listen                                      1073684500

 PXI Interrupt                                     1073684514

 Serial Break                                      1073684515

 Serial TermChar                                  1073684516

 Serial CTS                                       1073684521

 Serial DSR                                       1073684522

 Serial DCD                                       1073684524

 Serial RI                                         1073684526

 Serial Character                                  1073684533

 USB Interrupt                                    1073684535

 All Enabled                                      1073709055

                                                    © National Instruments 10059

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10059 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10060 ordinal=10060 -->
## Property and Method Reference

Property and Method Reference

    EventEvent Information:StatusInformation:Status

        Returns the VISA status code of the specified event.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    EventEvent Information:USBInformation:USB ReceivedReceived InterruptInterrupt
     SizeSize

        Returns the number of bytes of USB interrupt data stored.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


10060   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10060 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10061 ordinal=10061 -->
## Property and Method Reference

Property and Method Reference

VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
IdentificationIdentification

Returns the VXI manufacturer ID of the manufacturer that created the VISA
implementation.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
NameName

Returns the name of the manufacturer that created the implementation. This is not
related to the device manufacturer attributes. Note: Use the value of this property for
display purposes only and not for programmatic decisions. The value can change
between VISA implementations and/or revisions.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes


                                                    © National Instruments 10061

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10061 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10062 ordinal=10062 -->
## Property and Method Reference

Property and Method Reference


           Available in Real-Time Operating System                                   Yes

    VersionVersion Information:VersionInformation:Version ofof
    ImplementationImplementation

        Returns the version of a given implementation. This value is defined by the individual
        manufacturer and increments with each new revision. The format of the value has the
       upper 12 bits as the major number of the version, the next lower 12 bits as the minor
       number of the version, and the lowest 8 bits as the sub-minor number of the version.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    VersionVersion Information:VersionInformation:Version ofof SpecificationSpecification

        Returns the value that uniquely identifies the version of the VISA specification to which
        the implementation complies. The format of the value has the upper 12 bits as the
       major number of the version, the next lower 12 bits as the minor number of the
         version, and the lowest 8 bits as the sub-minor number of the version.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

10062   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10062 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10063 ordinal=10063 -->
## Property and Method Reference

Property and Method Reference


 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VXIVXI SignalSignal EventEvent PropertiesProperties


 Property             Description

 Event                      Returns the unique logical identifier for the event type of the specified Information:Event                       event. Type

 Event
                      Returns the 16-bit Status/ID value retrieved during the IACK cycle or from Information:Signal                      the Signal register. This is valid only for the VXI Signal Event. Processor Status ID

 Version
 Information:Resource Returns the VXI manufacturer ID of the manufacturer that created the VISA
 Manufacturer         implementation.
 Identification

                      Returns the name of the manufacturer that created the implementation.
 Version               This is not related to the device manufacturer attributes. Note: Use the
 Information:Resource  value of this property for display purposes only and not for programmatic
 Manufacturer Name   decisions. The value can change between VISA implementations and/or
                         revisions.

                      Returns the version of a given implementation. This value is defined by the
 Version                individual manufacturer and increments with each new revision. The format
 Information:Version   of the value has the upper 12 bits as the major number of the version, the
 of Implementation    next lower 12 bits as the minor number of the version, and the lowest 8 bits
                      as the sub-minor number of the version.

                      Returns the value that uniquely identifies the version of the VISA
 Version                specification to which the implementation complies. The format of the
 Information:Version   value has the upper 12 bits as the major number of the version, the next
 of Specification       lower 12 bits as the minor number of the version, and the lowest 8 bits as
                      the sub-minor number of the version.

EventEvent Information:EventInformation:Event TypeType

Returns the unique logical identifier for the event type of the specified event.


                                                    © National Instruments 10063

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10063 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10064 ordinal=10064 -->
## Property and Method Reference

Property and Method Reference

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


          Service Request                                  1073684491

           Trigger                                          3221168138

          Clear                                           1073684493

          VXI Signal                                       1073684512

         VXI/VME Interrupt                                 3221168161

         VXI/VME Sysfail                                   1073684509

         VXI/VME Sysreset                                 1073684510

         GPIB CIC                                        1073684498

         GPIB Talk                                        1073684499

         GPIB Listen                                      1073684500

          PXI Interrupt                                     1073684514

           Serial Break                                      1073684515

           Serial TermChar                                  1073684516

           Serial CTS                                       1073684521

           Serial DSR                                       1073684522

           Serial DCD                                       1073684524

           Serial RI                                         1073684526

           Serial Character                                  1073684533

        USB Interrupt                                    1073684535

             All Enabled                                      1073709055

10064   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10064 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10065 ordinal=10065 -->
## Property and Method Reference

Property and Method Reference

EventEvent Information:SignalInformation:Signal ProcessorProcessor StatusStatus IDID

Returns the 16-bit Status/ID value retrieved during the IACK cycle or from the Signal
register. This is valid only for the VXI Signal Event.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
IdentificationIdentification

Returns the VXI manufacturer ID of the manufacturer that created the VISA
implementation.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


                                                    © National Instruments 10065

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10065 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10066 ordinal=10066 -->
## Property and Method Reference

Property and Method Reference

    VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
   NameName

        Returns the name of the manufacturer that created the implementation. This is not
         related to the device manufacturer attributes. Note: Use the value of this property for
         display purposes only and not for programmatic decisions. The value can change
       between VISA implementations and/or revisions.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    VersionVersion Information:VersionInformation:Version ofof
    ImplementationImplementation

        Returns the version of a given implementation. This value is defined by the individual
        manufacturer and increments with each new revision. The format of the value has the
       upper 12 bits as the major number of the version, the next lower 12 bits as the minor
       number of the version, and the lowest 8 bits as the sub-minor number of the version.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only


10066   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10066 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10067 ordinal=10067 -->
## Property and Method Reference

Property and Method Reference


 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VersionVersion Information:VersionInformation:Version ofof SpecificationSpecification

Returns the value that uniquely identifies the version of the VISA specification to which
the implementation complies. The format of the value has the upper 12 bits as the
major number of the version, the next lower 12 bits as the minor number of the
version, and the lowest 8 bits as the sub-minor number of the version.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VXI/VMEVXI/VME InterruptInterrupt EventEvent PropertiesProperties


 Property             Description

 Event
                      Returns the unique logical identifier for the event type of the specified
 Information:Event
                       event.
 Type

 Event
                      Returns the 32-bit status/ID retrieved during the IACK cycle. This is valid
 Information:Interrupt
                      only for the VXI/VME Interrupt event.
 Status ID

 Event
                      Returns the VXI interrupt level on which the interrupt was received. This is
 Information:Received
                         valid only for the VXI/VME Interrupt event.
 Interrupt Level

 Version              Returns the VXI manufacturer ID of the manufacturer that created the VISA
 Information:Resource implementation.

                                                    © National Instruments 10067

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10067 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10068 ordinal=10068 -->
## Property and Method Reference

Property and Method Reference


          Property             Description

          Manufacturer
            Identification

                               Returns the name of the manufacturer that created the implementation.
           Version               This is not related to the device manufacturer attributes. Note: Use the
          Information:Resource  value of this property for display purposes only and not for programmatic
          Manufacturer Name   decisions. The value can change between VISA implementations and/or
                                    revisions.

                               Returns the version of a given implementation. This value is defined by the
           Version                individual manufacturer and increments with each new revision. The format
           Information:Version   of the value has the upper 12 bits as the major number of the version, the
           of Implementation    next lower 12 bits as the minor number of the version, and the lowest 8 bits
                               as the sub-minor number of the version.

                               Returns the value that uniquely identifies the version of the VISA
           Version                specification to which the implementation complies. The format of the
           Information:Version   value has the upper 12 bits as the major number of the version, the next
           of Specification       lower 12 bits as the minor number of the version, and the lowest 8 bits as
                               the sub-minor number of the version.

    EventEvent Information:EventInformation:Event TypeType

        Returns the unique logical identifier for the event type of the specified event.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


          Service Request                                  1073684491

           Trigger                                          3221168138


10068   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10068 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10069 ordinal=10069 -->
## Property and Method Reference

Property and Method Reference


 Clear                                           1073684493

 VXI Signal                                       1073684512

 VXI/VME Interrupt                                 3221168161

 VXI/VME Sysfail                                   1073684509

 VXI/VME Sysreset                                 1073684510

 GPIB CIC                                        1073684498

 GPIB Talk                                        1073684499

 GPIB Listen                                      1073684500

 PXI Interrupt                                     1073684514

 Serial Break                                      1073684515

 Serial TermChar                                  1073684516

 Serial CTS                                       1073684521

 Serial DSR                                       1073684522

 Serial DCD                                       1073684524

 Serial RI                                         1073684526

 Serial Character                                  1073684533

 USB Interrupt                                    1073684535

 All Enabled                                      1073709055

EventEvent Information:InterruptInformation:Interrupt StatusStatus IDID

Returns the 32-bit status/ID retrieved during the IACK cycle. This is valid only for the
VXI/VME Interrupt event.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

                                                    © National Instruments 10069

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10069 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10070 ordinal=10070 -->
## Property and Method Reference

Property and Method Reference


           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    EventEvent Information:ReceivedInformation:Received InterruptInterrupt LevelLevel

        Returns the VXI interrupt level on which the interrupt was received. This is valid only
         for the VXI/VME Interrupt event.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
     IdentificationIdentification

        Returns the VXI manufacturer ID of the manufacturer that created the VISA
        implementation.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

10070   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10070 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10071 ordinal=10071 -->
## Property and Method Reference

Property and Method Reference

VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
NameName

Returns the name of the manufacturer that created the implementation. This is not
related to the device manufacturer attributes. Note: Use the value of this property for
display purposes only and not for programmatic decisions. The value can change
between VISA implementations and/or revisions.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VersionVersion Information:VersionInformation:Version ofof
ImplementationImplementation

Returns the version of a given implementation. This value is defined by the individual
manufacturer and increments with each new revision. The format of the value has the
upper 12 bits as the major number of the version, the next lower 12 bits as the minor
number of the version, and the lowest 8 bits as the sub-minor number of the version.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only


                                                    © National Instruments 10071

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10071 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10072 ordinal=10072 -->
## Property and Method Reference

Property and Method Reference


           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    VersionVersion Information:VersionInformation:Version ofof SpecificationSpecification

        Returns the value that uniquely identifies the version of the VISA specification to which
        the implementation complies. The format of the value has the upper 12 bits as the
       major number of the version, the next lower 12 bits as the minor number of the
         version, and the lowest 8 bits as the sub-minor number of the version.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

      VXI/VMEVXI/VME SysfailSysfail EventEvent PropertiesProperties


          Property             Description

          Event
                               Returns the unique logical identifier for the event type of the specified
          Information:Event
                                 event.
         Type

           Version
          Information:Resource Returns the VXI manufacturer ID of the manufacturer that created the VISA
          Manufacturer         implementation.
            Identification

                               Returns the name of the manufacturer that created the implementation.
           Version               This is not related to the device manufacturer attributes. Note: Use the
          Information:Resource  value of this property for display purposes only and not for programmatic
          Manufacturer Name   decisions. The value can change between VISA implementations and/or
                                    revisions.

10072   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10072 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10073 ordinal=10073 -->
## Property and Method Reference

Property and Method Reference


 Property             Description

                      Returns the version of a given implementation. This value is defined by the
 Version                individual manufacturer and increments with each new revision. The format
 Information:Version   of the value has the upper 12 bits as the major number of the version, the
 of Implementation    next lower 12 bits as the minor number of the version, and the lowest 8 bits
                      as the sub-minor number of the version.

                      Returns the value that uniquely identifies the version of the VISA
 Version                specification to which the implementation complies. The format of the
 Information:Version   value has the upper 12 bits as the major number of the version, the next
 of Specification       lower 12 bits as the minor number of the version, and the lowest 8 bits as
                      the sub-minor number of the version.

EventEvent Information:EventInformation:Event TypeType

Returns the unique logical identifier for the event type of the specified event.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


 Service Request                                  1073684491

 Trigger                                          3221168138

 Clear                                           1073684493

 VXI Signal                                       1073684512

 VXI/VME Interrupt                                 3221168161

 VXI/VME Sysfail                                   1073684509

 VXI/VME Sysreset                                 1073684510


                                                    © National Instruments 10073

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10073 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10074 ordinal=10074 -->
## Property and Method Reference

Property and Method Reference


         GPIB CIC                                        1073684498

         GPIB Talk                                        1073684499

         GPIB Listen                                      1073684500

          PXI Interrupt                                     1073684514

           Serial Break                                      1073684515

           Serial TermChar                                  1073684516

           Serial CTS                                       1073684521

           Serial DSR                                       1073684522

           Serial DCD                                       1073684524

           Serial RI                                         1073684526

           Serial Character                                  1073684533

        USB Interrupt                                    1073684535

             All Enabled                                      1073709055

    VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
     IdentificationIdentification

        Returns the VXI manufacturer ID of the manufacturer that created the VISA
        implementation.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


10074   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10074 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10075 ordinal=10075 -->
## Property and Method Reference

Property and Method Reference

VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
NameName

Returns the name of the manufacturer that created the implementation. This is not
related to the device manufacturer attributes. Note: Use the value of this property for
display purposes only and not for programmatic decisions. The value can change
between VISA implementations and/or revisions.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VersionVersion Information:VersionInformation:Version ofof
ImplementationImplementation

Returns the version of a given implementation. This value is defined by the individual
manufacturer and increments with each new revision. The format of the value has the
upper 12 bits as the major number of the version, the next lower 12 bits as the minor
number of the version, and the lowest 8 bits as the sub-minor number of the version.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only


                                                    © National Instruments 10075

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10075 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10076 ordinal=10076 -->
## Property and Method Reference

Property and Method Reference


           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    VersionVersion Information:VersionInformation:Version ofof SpecificationSpecification

        Returns the value that uniquely identifies the version of the VISA specification to which
        the implementation complies. The format of the value has the upper 12 bits as the
       major number of the version, the next lower 12 bits as the minor number of the
         version, and the lowest 8 bits as the sub-minor number of the version.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

      VXI/VMEVXI/VME SysresetSysreset EventEvent PropertiesProperties


          Property             Description

          Event
                               Returns the unique logical identifier for the event type of the specified
          Information:Event
                                 event.
         Type

           Version
          Information:Resource Returns the VXI manufacturer ID of the manufacturer that created the VISA
          Manufacturer         implementation.
            Identification

                               Returns the name of the manufacturer that created the implementation.
           Version               This is not related to the device manufacturer attributes. Note: Use the
          Information:Resource  value of this property for display purposes only and not for programmatic
          Manufacturer Name   decisions. The value can change between VISA implementations and/or
                                    revisions.

10076   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10076 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10077 ordinal=10077 -->
## Property and Method Reference

Property and Method Reference


 Property             Description

                      Returns the version of a given implementation. This value is defined by the
 Version                individual manufacturer and increments with each new revision. The format
 Information:Version   of the value has the upper 12 bits as the major number of the version, the
 of Implementation    next lower 12 bits as the minor number of the version, and the lowest 8 bits
                      as the sub-minor number of the version.

                      Returns the value that uniquely identifies the version of the VISA
 Version                specification to which the implementation complies. The format of the
 Information:Version   value has the upper 12 bits as the major number of the version, the next
 of Specification       lower 12 bits as the minor number of the version, and the lowest 8 bits as
                      the sub-minor number of the version.

EventEvent Information:EventInformation:Event TypeType

Returns the unique logical identifier for the event type of the specified event.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


 Service Request                                  1073684491

 Trigger                                          3221168138

 Clear                                           1073684493

 VXI Signal                                       1073684512

 VXI/VME Interrupt                                 3221168161

 VXI/VME Sysfail                                   1073684509

 VXI/VME Sysreset                                 1073684510


                                                    © National Instruments 10077

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10077 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10078 ordinal=10078 -->
## Property and Method Reference

Property and Method Reference


         GPIB CIC                                        1073684498

         GPIB Talk                                        1073684499

         GPIB Listen                                      1073684500

          PXI Interrupt                                     1073684514

           Serial Break                                      1073684515

           Serial TermChar                                  1073684516

           Serial CTS                                       1073684521

           Serial DSR                                       1073684522

           Serial DCD                                       1073684524

           Serial RI                                         1073684526

           Serial Character                                  1073684533

        USB Interrupt                                    1073684535

             All Enabled                                      1073709055

    VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
     IdentificationIdentification

        Returns the VXI manufacturer ID of the manufacturer that created the VISA
        implementation.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


10078   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10078 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10079 ordinal=10079 -->
## Property and Method Reference

Property and Method Reference

VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
NameName

Returns the name of the manufacturer that created the implementation. This is not
related to the device manufacturer attributes. Note: Use the value of this property for
display purposes only and not for programmatic decisions. The value can change
between VISA implementations and/or revisions.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VersionVersion Information:VersionInformation:Version ofof
ImplementationImplementation

Returns the version of a given implementation. This value is defined by the individual
manufacturer and increments with each new revision. The format of the value has the
upper 12 bits as the major number of the version, the next lower 12 bits as the minor
number of the version, and the lowest 8 bits as the sub-minor number of the version.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only


                                                    © National Instruments 10079

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10079 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10080 ordinal=10080 -->
## Property and Method Reference

Property and Method Reference


           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    VersionVersion Information:VersionInformation:Version ofof SpecificationSpecification

        Returns the value that uniquely identifies the version of the VISA specification to which
        the implementation complies. The format of the value has the upper 12 bits as the
       major number of the version, the next lower 12 bits as the minor number of the
         version, and the lowest 8 bits as the sub-minor number of the version.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

       EventEvent Information:EventInformation:Event TypeType

        Returns the unique logical identifier for the event type of the specified event.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


10080   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10080 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10081 ordinal=10081 -->
## Property and Method Reference

Property and Method Reference


 Service Request                                  1073684491

 Trigger                                          3221168138

 Clear                                           1073684493

 VXI Signal                                       1073684512

 VXI/VME Interrupt                                 3221168161

 VXI/VME Sysfail                                   1073684509

 VXI/VME Sysreset                                 1073684510

 GPIB CIC                                        1073684498

 GPIB Talk                                        1073684499

 GPIB Listen                                      1073684500

 PXI Interrupt                                     1073684514

 Serial Break                                      1073684515

 Serial TermChar                                  1073684516

 Serial CTS                                       1073684521

 Serial DSR                                       1073684522

 Serial DCD                                       1073684524

 Serial RI                                         1073684526

 Serial Character                                  1073684533

 USB Interrupt                                    1073684535

 All Enabled                                      1073709055

VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer IdentificationIdentification

Returns the VXI manufacturer ID of the manufacturer that created the VISA
implementation.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 10081

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10081 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10082 ordinal=10082 -->
## Property and Method Reference

Property and Method Reference


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

        VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer NameName

        Returns the name of the manufacturer that created the implementation. This is not
         related to the device manufacturer attributes. Note: Use the value of this property for
         display purposes only and not for programmatic decisions. The value can change
       between VISA implementations and/or revisions.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

        VersionVersion Information:VersionInformation:Version ofof ImplementationImplementation

        Returns the version of a given implementation. This value is defined by the individual
        manufacturer and increments with each new revision. The format of the value has the
       upper 12 bits as the major number of the version, the next lower 12 bits as the minor
       number of the version, and the lowest 8 bits as the sub-minor number of the version.

      Remarks

       The following table lists the characteristics of this property.


          Data type


10082   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10082 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10083 ordinal=10083 -->
## Property and Method Reference

Property and Method Reference


 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VersionVersion Information:VersionInformation:Version ofof SpecificationSpecification

Returns the value that uniquely identifies the version of the VISA specification to which
the implementation complies. The format of the value has the upper 12 bits as the
major number of the version, the next lower 12 bits as the minor number of the
version, and the lowest 8 bits as the sub-minor number of the version.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

I/OI/O SessionSession PropertiesProperties


 Property             Description

 General                Specifies the maximum number of events that can be queued at any time
 Settings:Maximum    on the given session. This property is read/write until the first time you call
 Queue Length        VISA Enable Event on a session. Thereafter, it is read only. The default is 50.

                      Returns the resource class of the resource string used to open the given
 General
                        session. For example, if the resource string for a given session is COM1 or
 Settings:Resource
                      ASRL1::INSTR, this property returns INSTR, regardless of the class of the I/O
 Class
                         control.

 General              Returns the current locking state of the resource associated with the given
 Settings:Resource     session. The resource can be unlocked, locked with an exclusive lock, or
 Lock State            locked with a shared lock. The default is Unlocked.


                                                    © National Instruments 10083

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10083 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10084 ordinal=10084 -->
## Property and Method Reference

Property and Method Reference


          Property             Description

          General
           Settings:Resource     Returns the unique identifier for a resource.
        Name

          General                Specifies the minimum timeout value, in milliseconds, to use when
          Settings:Timeout      accessing the device. Note that the actual timeout that VISA returns may be
          Value                 higher than the one requested. The default is 2000.

                                   Specifies a data value for the private use of an application. The VISA
          General Settings:User  implementation stores this value in a per-session location, so that user data
          Data              on other sessions does not affect the user data on this session. VISA does
                               not use this property for any purpose.

                                   Specifies human-readable text that describes the given interface. Note: Use           Interface
                               the value of this property for display purposes only and not for           Information:Interface                             programmatic decisions. The value can change between VISA           Description
                              implementations and/or revisions.

           Interface
           Information:Interface  Returns the board number for the given interface.
        Number

           Interface
           Information:Interface  Specifies the interface type of the given session.
         Type

           Version
          Information:Resource Returns a value that corresponds to the VXI manufacturer ID of the
          Manufacturer         manufacturer that created the VISA implementation.
            Identification

                               Returns the name of the manufacturer that created the implementation.
           Version               This is not related to the device manufacturer attributes. Note: Use the
          Information:Resource  value of this property for display purposes only and not for programmatic
          Manufacturer Name   decisions. The value can change between VISA implementations and/or
                                    revisions.

                               Returns the version of a given implementation. This value is defined by the
           Version                individual manufacturer and increments with each new revision. The format
           Information:Version   of the value has the upper 12 bits as the major number of the version, the
           of Implementation    next lower 12 bits as the minor number of the version, and the lowest 8 bits
                               as the sub-minor number of the version.

           Version              Returns the value that uniquely identifies the version of the VISA
           Information:Version   specification to which the implementation complies. The format of the
           of Specification       value has the upper 12 bits as the major number of the version, the next

10084   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10084 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10085 ordinal=10085 -->
## Property and Method Reference

Property and Method Reference


 Property             Description

                     lower 12 bits as the minor number of the version, and the lowest 8 bits as
                      the sub-minor number of the version.

FireWireFireWire InstrInstr PropertiesProperties


 Property              Description

 FireWire                         Specifies the upper 16 bits of the 48-bit destination address for a FireWire Settings:Destination                        device. The default is 0xFFFF. Upper Offset

 FireWire
 Settings:Lower Chip   Returns the lower chip ID for a FireWire device.
 ID

 FireWire                         Specifies the upper 16 bits of the 48-bit source address for a FireWire Settings:Source
                        device. The default is 0xFFFF. Upper Offset

 FireWire
 Settings:Upper Chip    Specifies the upper chip ID for a FireWire device.
 ID

 FireWire                      Returns the vendor ID for a FireWire device.
 Settings:Vendor ID

 FireWire                         Specifies the upper 16 bits of the 48-bit address for a FireWire device when
 Settings:Window                    a window is mapped. The default is 0xFFFF. Upper Offset

                      Returns the name of the manufacturer that created the device. Note: Use
 General
                      the value of this property for display purposes only and not for
 Settings:Manufacturer
                     programmatic decisions. The value can change between VISA
 Name
                      implementations and/or revisions.

 General                Specifies the maximum number of events that can be queued at any time
 Settings:Maximum    on the given session. This property is read/write until the first time you call
 Queue Length         VISA Enable Event on a session. Thereafter, it is read only. The default is 50.

                      Returns the model name of the device. Note: Use the value of this property
 General
                          for display purposes only and not for programmatic decisions. The value
 Settings:Model Name
                     can change between VISA implementations and/or revisions.

 General              Returns the resource class of the resource string used to open the given


                                                    © National Instruments 10085

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10085 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10086 ordinal=10086 -->
## Property and Method Reference

Property and Method Reference


          Property              Description

                                   session. For example, if the resource string for a given session is COM1 or           Settings:Resource                                ASRL1::INSTR, this property returns INSTR, regardless of the class of the I/O           Class                                    control.

          General              Returns the current locking state of the resource associated with the given
           Settings:Resource      session. The resource can be unlocked, locked with an exclusive lock, or
         Lock State            locked with a shared lock. The default is Unlocked.

          General
           Settings:Resource     Returns the unique identifier for a resource.
        Name

          General                Specifies the minimum timeout value, in milliseconds, to use when
          Settings:Timeout      accessing the device. Note that the actual timeout that VISA returns may be
          Value                 higher than the one requested. The default is 2000.

                                   Specifies a data value for the private use of an application. The VISA
          General Settings:User  implementation stores this value in a per-session location, so that user data
          Data               on other sessions does not affect the user data on this session. VISA does
                               not use this property for any purpose.

                                   Specifies human-readable text that describes the given interface. Note: Use
           Interface                                the value of this property for display purposes only and not for           Information:Interface                             programmatic decisions. The value can change between VISA
           Description                               implementations and/or revisions.

           Interface
           Information:Interface  Returns the board number for the given interface.
        Number

           Interface
           Information:Interface  Specifies the interface type of the given session.
         Type

                                   Specifies the number of elements by which to increment the destination
           Register Based
                               address on block move operations. Valid values include 0 and 1. The default
           Settings:Destination
                                            is 1. If this property is set to 0, VISA Move Out X operations always read from
          Increment Count
                                the same element, essentially treating the destination as a FIFO register.

                                   Specifies the number of elements by which to increment the source
           Register Based
                               address on block move operations. Valid values include 0 and 1. The default
           Settings:Source
                                            is 1. If this property is set to 0, VISA Move In X operations always read from
          Increment Count
                                the same element, essentially treating the source as a FIFO register.

           Register Based        Returns whether the current session has a mapped window, and if so,
          Settings:Window      whether the window allows direct pointer dereferences.


10086   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10086 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10087 ordinal=10087 -->
## Property and Method Reference

Property and Method Reference


 Property              Description

 Access

 Register Based        Returns the base interface address to which this window maps. If the
 Settings:Window Base Window Access property is Not Mapped, the value of this property is
 Address               undefined.

 Register Based        Returns the size of the region mapped to this window. If the Window Access
 Settings:Window Size  property is Not Mapped, the value of this property is undefined.

 Version
 Information:Resource  Returns a value that corresponds to the VXI manufacturer ID of the
 Manufacturer         manufacturer that created the VISA implementation.
 Identification

                      Returns the name of the manufacturer that created the implementation.
 Version                This is not related to the device manufacturer attributes. Note: Use the
 Information:Resource  value of this property for display purposes only and not for programmatic
 Manufacturer Name    decisions. The value can change between VISA implementations and/or
                          revisions.

                      Returns the version of a given implementation. This value is defined by the
 Version                individual manufacturer and increments with each new revision. The
 Information:Version   format of the value has the upper 12 bits as the major number of the
 of Implementation     version, the next lower 12 bits as the minor number of the version, and the
                       lowest 8 bits as the sub-minor number of the version.

                      Returns the value that uniquely identifies the version of the VISA
 Version                 specification to which the implementation complies. The format of the
 Information:Version    value has the upper 12 bits as the major number of the version, the next
 of Specification       lower 12 bits as the minor number of the version, and the lowest 8 bits as
                      the sub-minor number of the version.

FireWireFireWire Settings:DestinationSettings:Destination UpperUpper OffsetOffset

Specifies the upper 16 bits of the 48-bit destination address for a FireWire device. The
default is 0xFFFF.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 10087

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10087 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10088 ordinal=10088 -->
## Property and Method Reference

Property and Method Reference


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

     FireWireFireWire Settings:LowerSettings:Lower ChipChip IDID

        Returns the lower chip ID for a FireWire device.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

     FireWireFireWire Settings:SourceSettings:Source UpperUpper OffsetOffset

         Specifies the upper 16 bits of the 48-bit source address for a FireWire device. The
         default is 0xFFFF.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

10088   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10088 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10089 ordinal=10089 -->
## Property and Method Reference

Property and Method Reference

FireWireFireWire Settings:UpperSettings:Upper ChipChip IDID

Specifies the upper chip ID for a FireWire device.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

FireWireFireWire Settings:VendorSettings:Vendor IDID

Returns the vendor ID for a FireWire device.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

FireWireFireWire Settings:WindowSettings:Window UpperUpper OffsetOffset

Specifies the upper 16 bits of the 48-bit address for a FireWire device when a window is
mapped. The default is 0xFFFF.


                                                    © National Instruments 10089

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10089 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10090 ordinal=10090 -->
## Property and Method Reference

Property and Method Reference

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

    GeneralGeneral Settings:ManufacturerSettings:Manufacturer NameName

        Returns the name of the manufacturer that created the device. Note: Use the value of
          this property for display purposes only and not for programmatic decisions. The value
       can change between VISA implementations and/or revisions.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    GeneralGeneral Settings:MaximumSettings:Maximum QueueQueue LengthLength

         Specifies the maximum number of events that can be queued at any time on the given
         session. This property is read/write until the first time you call VISA Enable Event on a
         session. Thereafter, it is read only. The default is 50.


10090   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10090 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10091 ordinal=10091 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

GeneralGeneral Settings:ModelSettings:Model NameName

Returns the model name of the device. Note: Use the value of this property for display
purposes only and not for programmatic decisions. The value can change between
VISA implementations and/or revisions.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

GeneralGeneral Settings:ResourceSettings:Resource ClassClass

Returns the resource class of the resource string used to open the given session. For
example, if the resource string for a given session is COM1 or ASRL1::INSTR, this
property returns INSTR, regardless of the class of the I/O control.


                                                    © National Instruments 10091

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10091 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10092 ordinal=10092 -->
## Property and Method Reference

Property and Method Reference

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    GeneralGeneral Settings:ResourceSettings:Resource LockLock StateState

        Returns the current locking state of the resource associated with the given session.
       The resource can be unlocked, locked with an exclusive lock, or locked with a shared
         lock. The default is Unlocked.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


         Unlocked                                                     0

           Exclusive                                                     1

         Shared                                                       2

    GeneralGeneral Settings:ResourceSettings:Resource NameName

        Returns the unique identifier for a resource.

10092   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10092 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10093 ordinal=10093 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

GeneralGeneral Settings:TimeoutSettings:Timeout ValueValue

Specifies the minimum timeout value, in milliseconds, to use when accessing the
device. Note that the actual timeout that VISA returns may be higher than the one
requested. The default is 2000.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

GeneralGeneral Settings:UserSettings:User DataData

Specifies a data value for the private use of an application. The VISA implementation
stores this value in a per-session location, so that user data on other sessions does not
affect the user data on this session. VISA does not use this property for any purpose.


                                                    © National Instruments 10093

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10093 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10094 ordinal=10094 -->
## Property and Method Reference

Property and Method Reference

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

     InterfaceInterface Information:InterfaceInformation:Interface DescriptionDescription

         Specifies human-readable text that describes the given interface. Note: Use the value
         of this property for display purposes only and not for programmatic decisions. The
        value can change between VISA implementations and/or revisions.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

     InterfaceInterface Information:InterfaceInformation:Interface NumberNumber

        Returns the board number for the given interface.

      Remarks

       The following table lists the characteristics of this property.


10094   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10094 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10095 ordinal=10095 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

InterfaceInterface Information:InterfaceInformation:Interface TypeType

Specifies the interface type of the given session.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


 GPIB                                                       1

 VXI                                                         2

 GPIB-VXI                                                    3

 Serial                                                       4

 PXI                                                         5

 TCPIP                                                      6

 USB                                                        7

 FireWire                                                    9


                                                    © National Instruments 10095

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10095 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10096 ordinal=10096 -->
## Property and Method Reference

Property and Method Reference

     RegisterRegister BasedBased Settings:DestinationSettings:Destination
    IncrementIncrement CountCount

         Specifies the number of elements by which to increment the destination address on
        block move operations. Valid values include 0 and 1. The default is 1. If this property is
         set to 0, VISA Move Out X operations always read from the same element, essentially
         treating the destination as a FIFO register.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

     RegisterRegister BasedBased Settings:SourceSettings:Source IncrementIncrement
    CountCount

         Specifies the number of elements by which to increment the source address on block
      move operations. Valid values include 0 and 1. The default is 1. If this property is set to
          0, VISA Move In X operations always read from the same element, essentially treating
        the source as a FIFO register.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write


10096   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10096 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10097 ordinal=10097 -->
## Property and Method Reference

Property and Method Reference


 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

RegisterRegister BasedBased Settings:WindowSettings:Window AccessAccess

Returns whether the current session has a mapped window, and if so, whether the
window allows direct pointer dereferences.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


 Not Mapped                                                                1

 Use Peek/Poke Operations                                                    2

 Can Dereference Pointer                                                     3

 Pointer value is byte-swapped                                                4

RegisterRegister BasedBased Settings:WindowSettings:Window BaseBase
AddressAddress

Returns the base interface address to which this window maps. If the Window Access
property is Not Mapped, the value of this property is undefined.


                                                    © National Instruments 10097

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10097 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10098 ordinal=10098 -->
## Property and Method Reference

Property and Method Reference

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

     RegisterRegister BasedBased Settings:WindowSettings:Window SizeSize

        Returns the size of the region mapped to this window. If the Window Access property is
       Not Mapped, the value of this property is undefined.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
     IdentificationIdentification

        Returns a value that corresponds to the VXI manufacturer ID of the manufacturer that
        created the VISA implementation.


10098   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10098 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10099 ordinal=10099 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
NameName

Returns the name of the manufacturer that created the implementation. This is not
related to the device manufacturer attributes. Note: Use the value of this property for
display purposes only and not for programmatic decisions. The value can change
between VISA implementations and/or revisions.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VersionVersion Information:VersionInformation:Version ofof
ImplementationImplementation

Returns the version of a given implementation. This value is defined by the individual

                                                    © National Instruments 10099

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10099 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10100 ordinal=10100 -->
## Property and Method Reference

Property and Method Reference

        manufacturer and increments with each new revision. The format of the value has the
       upper 12 bits as the major number of the version, the next lower 12 bits as the minor
       number of the version, and the lowest 8 bits as the sub-minor number of the version.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    VersionVersion Information:VersionInformation:Version ofof SpecificationSpecification

        Returns the value that uniquely identifies the version of the VISA specification to which
        the implementation complies. The format of the value has the upper 12 bits as the
       major number of the version, the next lower 12 bits as the minor number of the
         version, and the lowest 8 bits as the sub-minor number of the version.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

      GPIBGPIB BoardInterfaceBoardInterface PropertiesProperties


10100   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10100 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10101 ordinal=10101 -->
## Property and Method Reference

Property and Method Reference


Property             Description

GPIB                     Returns whether the specified GPIB interface is not addressed (0),Settings:Addressed                    addressed to talk (1) or addressed to listen (2).State

                       Specifies the total number of meters (1-15) of GPIB cable used in theGPIB Settings:HS488
                       specified GPIB interface. The value 0 means that HS488 is disabled. TheCable Length                      value -1 means HS488 is not implemented.

GPIB Settings:Is       Returns whether the specified GPIB interface is currently CIC (Controller In
Controller In Charge   Charge).

GPIB Settings:Line                     Returns the current state of the GPIB ATN interface line.ATN State

GPIB Settings:Line                     Returns the current state of the GPIB NDAC interface line.
NDAC State

GPIB Settings:Line                     Returns the current state of the GPIB REN (Remote ENable) interface line.
REN State

GPIB Settings:Line                     Returns the current state of the GPIB SRQ interface line.
SRQ State

GPIB
Settings:Primary      Returns the primary address of the GPIB interface used by the given session.
Address

GPIB                 Returns the secondary address of the GPIB interface used by the given
Settings:Secondary    session. If the interface does not have a secondary address, the value of this
Address              property is 65535 (0xFFFF).

GPIB Settings:System  Specifies whether the specified GPIB interface is currently the system
Controller State        controller.

                       Specifies whether I/O accesses should attempt to use DMA (TRUE) or
General
                  Programmed I/O (FALSE). In some implementations, this property may have
Settings:Allow DMA
                      global effects even though it is documented as a local property. This
Transfers
                     behavior affects performance and not functionality.

General                Specifies the maximum number of events that can be queued at any time
Settings:Maximum    on the given session. This property is read/write until the first time you call
Queue Length        VISA Enable Event on a session. Thereafter, it is read only. The default is 50.

                     Returns the resource class of the resource string used to open the given
General
                       session. For example, if the resource string for a given session is COM1 or
Settings:Resource
                     ASRL1::INSTR, this property returns INSTR, regardless of the class of the I/O
Class
                        control.

                                                    © National Instruments 10101

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10101 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10102 ordinal=10102 -->
## Property and Method Reference

Property and Method Reference


          Property             Description

          General              Returns the current locking state of the resource associated with the given
           Settings:Resource     session. The resource can be unlocked, locked with an exclusive lock, or
         Lock State            locked with a shared lock. The default is Unlocked.

          General
           Settings:Resource     Returns the unique identifier for a resource.
        Name

          General                Specifies the minimum timeout value, in milliseconds, to use when
          Settings:Timeout      accessing the device. Note that the actual timeout that VISA returns may be
          Value                 higher than the one requested. The default is 2000.

                                   Specifies a data value for the private use of an application. The VISA
          General Settings:User  implementation stores this value in a per-session location, so that user data
          Data              on other sessions does not affect the user data on this session. VISA does
                               not use this property for any purpose.

                                   Specifies human-readable text that describes the given interface. Note: Use           Interface                               the value of this property for display purposes only and not for           Information:Interface
                             programmatic decisions. The value can change between VISA           Description                              implementations and/or revisions.

           Interface
           Information:Interface  Returns the board number for the given interface.
        Number

           Interface
           Information:Interface  Specifies the interface type of the given session.
         Type

         Message Based        Specifies the 488-style status byte of the local controller or device
           Settings:Device       associated with this session. If you write this property and set bit 6 (0x40),
           Status Byte             this device or controller asserts a service request (SRQ) on the interface.

                                   Specifies whether VISA Read To File appends or overwrites (truncates) when
         Message Based
                             opening a file. If this property is set to TRUE, VISA Read To File appends
            Settings:File Append
                         when opening a file. If this property is set to FALSE, VISA Read To
          Enable
                                       File overwrites (truncates) when opening a file. The default is FALSE.

                                   Specifies which protocol to use. In VXI, you can choose normal word serial
                                or fast data channel. In GPIB, you can choose normal or high-speed HS-488
         Message Based
                                     transfers. In serial, TCP/IP, or USB, you can choose normal transfers or
           Settings:IO Protocol
                                 488.2-defined strings. In USBTMC, you can choose normal or vendor-specific
                                     transfers. The default is Normal.

         Message Based        Specifies whether to send an END indicator on the last byte of each write


10102   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10102 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10103 ordinal=10103 -->
## Property and Method Reference

Property and Method Reference


Property             Description

                      operation. This property is relevant only in VISA Write and related
                       operations. The default is TRUE. On Serial Instr sessions, if this property is
                        set to FALSE, the write transmits the exact contents of the user buffer,
Settings:Send End     without modifying it and without appending anything to the data. If this
Enable               property is set to TRUE, VISA performs the behavior described in the
                     property End Mode for Writes (ASRL End Out). On GPIB, VXI, GPIB-VXI, TCP/
                       IP Instr, and USB Instr sessions, if this property is set to TRUE, VISA includes
                     the 488.2 defined end of message terminator.

Message Based        Specifies a character that, when read, causes a read operation to terminate.
Settings:Termination  The termination character also must be enabled. This default is 0x0A
Character               (linefeed).

Message Based
                       Specifies whether a read operation terminates when it receives theSettings:Termination                      termination character. The default is FALSE.
Character Enable

Version
Information:Resource Returns a value that corresponds to the VXI manufacturer ID of the
Manufacturer         manufacturer that created the VISA implementation.
Identification

                     Returns the name of the manufacturer that created the implementation.
Version               This is not related to the device manufacturer attributes. Note: Use the
Information:Resource  value of this property for display purposes only and not for programmatic
Manufacturer Name   decisions. The value can change between VISA implementations and/or
                         revisions.

                     Returns the version of a given implementation. This value is defined by the
Version                individual manufacturer and increments with each new revision. The format
Information:Version   of the value has the upper 12 bits as the major number of the version, the
of Implementation    next lower 12 bits as the minor number of the version, and the lowest 8 bits
                     as the sub-minor number of the version.

                     Returns the value that uniquely identifies the version of the VISA
Version                specification to which the implementation complies. The format of the
Information:Version   value has the upper 12 bits as the major number of the version, the next
of Specification       lower 12 bits as the minor number of the version, and the lowest 8 bits as
                     the sub-minor number of the version.


                                                    © National Instruments 10103

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10103 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10104 ordinal=10104 -->
## Property and Method Reference

Property and Method Reference

    GPIBGPIB Settings:AddressedSettings:Addressed StateState

        Returns whether the specified GPIB interface is not addressed (0), addressed to talk (1)
        or addressed to listen (2).

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


         Unaddressed                                                      0

           Talker                                                            1

           Listener                                                          2

    GPIBGPIB Settings:HS488Settings:HS488 CableCable LengthLength

         Specifies the total number of meters (1-15) of GPIB cable used in the specified GPIB
         interface. The value 0 means that HS488 is disabled. The value -1 means HS488 is not
        implemented.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes


10104   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10104 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10105 ordinal=10105 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                                  Yes

GPIBGPIB Settings:IsSettings:Is ControllerController InIn ChargeCharge

Returns whether the specified GPIB interface is currently CIC (Controller In Charge).

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

GPIBGPIB Settings:LineSettings:Line ATNATN StateState

Returns the current state of the GPIB ATN interface line.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


 Unknown                                                                 -1

 Unasserted                                                   0

 Asserted                                                     1

                                                    © National Instruments 10105

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10105 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10106 ordinal=10106 -->
## Property and Method Reference

Property and Method Reference

    GPIBGPIB Settings:LineSettings:Line NDACNDAC StateState

        Returns the current state of the GPIB NDAC interface line.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


        Unknown                                                                 -1

          Unasserted                                                   0

          Asserted                                                     1

    GPIBGPIB Settings:LineSettings:Line RENREN StateState

        Returns the current state of the GPIB REN (Remote ENable) interface line.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


10106   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10106 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10107 ordinal=10107 -->
## Property and Method Reference

Property and Method Reference


 Unknown                                                                 -1

 Unasserted                                                   0

 Asserted                                                     1

GPIBGPIB Settings:LineSettings:Line SRQSRQ StateState

Returns the current state of the GPIB SRQ interface line.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


 Unknown                                                                 -1

 Unasserted                                                   0

 Asserted                                                     1

GPIBGPIB Settings:PrimarySettings:Primary AddressAddress

Returns the primary address of the GPIB interface used by the given session.

Remarks

The following table lists the characteristics of this property.


 Data type


                                                    © National Instruments 10107

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10107 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10108 ordinal=10108 -->
## Property and Method Reference

Property and Method Reference


          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

    GPIBGPIB Settings:SecondarySettings:Secondary AddressAddress

        Returns the secondary address of the GPIB interface used by the given session. If the
         interface does not have a secondary address, the value of this property is 65535
         (0xFFFF).

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

    GPIBGPIB Settings:SystemSettings:System ControllerController StateState

         Specifies whether the specified GPIB interface is currently the system controller.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes


10108   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10108 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10109 ordinal=10109 -->
## Property and Method Reference

Property and Method Reference

GeneralGeneral Settings:AllowSettings:Allow DMADMA TransfersTransfers

Specifies whether I/O accesses should attempt to use DMA (TRUE) or Programmed I/O
(FALSE). In some implementations, this property may have global effects even though
it is documented as a local property. This behavior affects performance and not
functionality.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

GeneralGeneral Settings:MaximumSettings:Maximum QueueQueue LengthLength

Specifies the maximum number of events that can be queued at any time on the given
session. This property is read/write until the first time you call VISA Enable Event on a
session. Thereafter, it is read only. The default is 50.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


                                                    © National Instruments 10109

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10109 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10110 ordinal=10110 -->
## Property and Method Reference

Property and Method Reference

    GeneralGeneral Settings:ResourceSettings:Resource ClassClass

        Returns the resource class of the resource string used to open the given session. For
        example, if the resource string for a given session is COM1 or ASRL1::INSTR, this
        property returns INSTR, regardless of the class of the I/O control.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    GeneralGeneral Settings:ResourceSettings:Resource LockLock StateState

        Returns the current locking state of the resource associated with the given session.
       The resource can be unlocked, locked with an exclusive lock, or locked with a shared
         lock. The default is Unlocked.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


         Unlocked                                                     0


10110   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10110 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10111 ordinal=10111 -->
## Property and Method Reference

Property and Method Reference


 Exclusive                                                     1

 Shared                                                       2

GeneralGeneral Settings:ResourceSettings:Resource NameName

Returns the unique identifier for a resource.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

GeneralGeneral Settings:TimeoutSettings:Timeout ValueValue

Specifies the minimum timeout value, in milliseconds, to use when accessing the
device. Note that the actual timeout that VISA returns may be higher than the one
requested. The default is 2000.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


                                                    © National Instruments 10111

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10111 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10112 ordinal=10112 -->
## Property and Method Reference

Property and Method Reference

    GeneralGeneral Settings:UserSettings:User DataData

         Specifies a data value for the private use of an application. The VISA implementation
         stores this value in a per-session location, so that user data on other sessions does not
         affect the user data on this session. VISA does not use this property for any purpose.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

     InterfaceInterface Information:InterfaceInformation:Interface DescriptionDescription

         Specifies human-readable text that describes the given interface. Note: Use the value
         of this property for display purposes only and not for programmatic decisions. The
        value can change between VISA implementations and/or revisions.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


10112   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10112 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10113 ordinal=10113 -->
## Property and Method Reference

Property and Method Reference

InterfaceInterface Information:InterfaceInformation:Interface NumberNumber

Returns the board number for the given interface.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

InterfaceInterface Information:InterfaceInformation:Interface TypeType

Specifies the interface type of the given session.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


 GPIB                                                       1

 VXI                                                         2

 GPIB-VXI                                                    3

 Serial                                                       4


                                                    © National Instruments 10113

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10113 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10114 ordinal=10114 -->
## Property and Method Reference

Property and Method Reference


          PXI                                                         5

         TCPIP                                                      6

        USB                                                        7

          FireWire                                                    9

    MessageMessage BasedBased Settings:DeviceSettings:Device StatusStatus ByteByte

         Specifies the 488-style status byte of the local controller or device associated with this
         session. If you write this property and set bit 6 (0x40), this device or controller asserts a
         service request (SRQ) on the interface.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

    MessageMessage BasedBased Settings:FileSettings:File AppendAppend EnableEnable

         Specifies whether VISA Read To File appends or overwrites (truncates) when opening a
            file. If this property is set to TRUE, VISA Read To File appends when opening a file. If
          this property is set to FALSE, VISA Read To File overwrites (truncates) when opening a
            file. The default is FALSE.

      Remarks

       The following table lists the characteristics of this property.


          Data type


10114   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10114 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10115 ordinal=10115 -->
## Property and Method Reference

Property and Method Reference


 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

MessageMessage BasedBased Settings:IOSettings:IO ProtocolProtocol

Specifies which protocol to use. In VXI, you can choose normal word serial or fast data
channel. In GPIB, you can choose normal or high-speed HS-488 transfers. In serial,
TCP/IP, or USB, you can choose normal transfers or 488.2-defined strings. In USBTMC,
you can choose normal or vendor-specific transfers. The default is Normal.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


 Normal                                                                    1

 VXI/FDC                                                                   2

 GPIB/HS488                                                                3

 Serial-TCPIP-USB/488 Strings                                                 4

 USBTMC/Vendor-Specific                                                    5

MessageMessage BasedBased Settings:SendSettings:Send EndEnd EnableEnable

Specifies whether to send an END indicator on the last byte of each write operation.
This property is relevant only in VISA Write and related operations. The default is TRUE.
On Serial Instr sessions, if this property is set to FALSE, the write transmits the exact

                                                    © National Instruments 10115

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10115 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10116 ordinal=10116 -->
## Property and Method Reference

Property and Method Reference

        contents of the user buffer, without modifying it and without appending anything to
        the data. If this property is set to TRUE, VISA performs the behavior described in the
        property End Mode for Writes (ASRL End Out). On GPIB, VXI, GPIB-VXI, TCP/IP Instr, and
      USB Instr sessions, if this property is set to TRUE, VISA includes the 488.2 defined end
         of message terminator.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

    MessageMessage BasedBased Settings:TerminationSettings:Termination
    CharacterCharacter

         Specifies a character that, when read, causes a read operation to terminate. The
        termination character also must be enabled. This default is 0x0A (linefeed).

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes


10116   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10116 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10117 ordinal=10117 -->
## Property and Method Reference

Property and Method Reference

MessageMessage BasedBased Settings:TerminationSettings:Termination
CharacterCharacter EnableEnable

Specifies whether a read operation terminates when it receives the termination
character. The default is FALSE.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
IdentificationIdentification

Returns a value that corresponds to the VXI manufacturer ID of the manufacturer that
created the VISA implementation.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


                                                    © National Instruments 10117

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10117 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10118 ordinal=10118 -->
## Property and Method Reference

Property and Method Reference

    VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
   NameName

        Returns the name of the manufacturer that created the implementation. This is not
         related to the device manufacturer attributes. Note: Use the value of this property for
         display purposes only and not for programmatic decisions. The value can change
       between VISA implementations and/or revisions.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    VersionVersion Information:VersionInformation:Version ofof
    ImplementationImplementation

        Returns the version of a given implementation. This value is defined by the individual
        manufacturer and increments with each new revision. The format of the value has the
       upper 12 bits as the major number of the version, the next lower 12 bits as the minor
       number of the version, and the lowest 8 bits as the sub-minor number of the version.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only


10118   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10118 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10119 ordinal=10119 -->
## Property and Method Reference

Property and Method Reference


 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VersionVersion Information:VersionInformation:Version ofof SpecificationSpecification

Returns the value that uniquely identifies the version of the VISA specification to which
the implementation complies. The format of the value has the upper 12 bits as the
major number of the version, the next lower 12 bits as the minor number of the
version, and the lowest 8 bits as the sub-minor number of the version.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

GPIBGPIB InstrInstr PropertiesProperties


 Property              Description

 GPIB Settings:Line
                       Returns the current state of the GPIB REN (Remote ENable) interface line.
 REN State

 GPIB Settings:Primary
                       Returns the primary address of the GPIB device used by the given session.
 Address

 GPIB                   Specifies whether to use repeat addressing before each read or write
 Settings:Readdressing  operation. The default is TRUE.

 GPIB                 Returns the secondary address of the GPIB device used by the given
 Settings:Secondary     session. If the device does not have a secondary address, the value of this
 Address               property is 65535 (0xFFFF).

 GPIB                   Specifies whether to unaddress the device (UNT and UNL) after each read


                                                    © National Instruments 10119

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10119 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10120 ordinal=10120 -->
## Property and Method Reference

Property and Method Reference


          Property              Description

          Settings:Unaddressing  or write operation. The default is FALSE.

                                    Specifies whether I/O accesses should attempt to use DMA (TRUE) or
          General Settings:Allow Programmed I/O (FALSE). In some implementations, this property may
       DMA Transfers        have global effects even though it is documented as a local property. This
                                behavior affects performance and not functionality.

          General                 Specifies the maximum number of events that can be queued at any time
          Settings:Maximum    on the given session. This property is read/write until the first time you call
        Queue Length         VISA Enable Event on a session. Thereafter, it is read only. The default is 50.

                                Returns the resource class of the resource string used to open the given          General                                   session. For example, if the resource string for a given session is COM1 or           Settings:Resource                                ASRL1::INSTR, this property returns INSTR, regardless of the class of the I/O           Class
                                    control.

          General               Returns the current locking state of the resource associated with the given
           Settings:Resource      session. The resource can be unlocked, locked with an exclusive lock, or
         Lock State             locked with a shared lock. The default is Unlocked.

          General
           Settings:Resource      Returns the unique identifier for a resource.
        Name

          General                 Specifies the minimum timeout value, in milliseconds, to use when
          Settings:Timeout       accessing the device. Note that the actual timeout that VISA returns may be
          Value                 higher than the one requested. The default is 2000.

                                    Specifies a data value for the private use of an application. The VISA
          General Settings:User  implementation stores this value in a per-session location, so that user
          Data                  data on other sessions does not affect the user data on this session. VISA
                             does not use this property for any purpose.

                                    Specifies human-readable text that describes the given interface. Note: Use
           Interface
                                the value of this property for display purposes only and not for
           Information:Interface
                              programmatic decisions. The value can change between VISA
           Description
                               implementations and/or revisions.

           Interface
           Information:Interface   Returns the board number for the given interface.
        Number

           Interface
           Information:Interface   Specifies the interface type of the given session.
         Type


10120   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10120 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10121 ordinal=10121 -->
## Property and Method Reference

Property and Method Reference


Property              Description

                        Specifies whether VISA Read To File appends or overwrites (truncates)Message Based                  when opening a file. If this property is set to TRUE, VISA Read To FileSettings:File Append                   appends when opening a file. If this property is set to FALSE, VISA Read ToEnable                           File overwrites (truncates) when opening a file. The default is FALSE.

                        Specifies which protocol to use. In VXI, you can choose normal word serial
                       or fast data channel. In GPIB, you can choose normal or high-speed HS-488Message Based                          transfers. In serial, TCP/IP, or USB, you can choose normal transfers orSettings:IO Protocol                       488.2-defined strings. In USBTMC, you can choose normal or vendor-
                          specific transfers. The default is Normal.

                        Specifies whether to send an END indicator on the last byte of each write
                       operation. This property is relevant only in VISA Write and related
                       operations. The default is TRUE. On Serial Instr sessions, if this property is
Message Based         set to FALSE, the write transmits the exact contents of the user buffer,
Settings:Send End     without modifying it and without appending anything to the data. If this
Enable                property is set to TRUE, VISA performs the behavior described in the
                      property End Mode for Writes (ASRL End Out). On GPIB, VXI, GPIB-VXI, TCP/
                        IP Instr, and USB Instr sessions, if this property is set to TRUE, VISA includes
                      the 488.2 defined end of message terminator.

Message Based         Specifies a character that, when read, causes a read operation to
Settings:Termination   terminate. The termination character also must be enabled. This default is
Character            0x0A (linefeed).

Message Based                        Specifies whether a read operation terminates when it receives theSettings:Termination
                      termination character. The default is FALSE.Character Enable

Version
Information:Resource  Returns a value that corresponds to the VXI manufacturer ID of the
Manufacturer         manufacturer that created the VISA implementation.
Identification

                      Returns the name of the manufacturer that created the implementation.
Version                This is not related to the device manufacturer attributes. Note: Use the
Information:Resource  value of this property for display purposes only and not for programmatic
Manufacturer Name    decisions. The value can change between VISA implementations and/or
                         revisions.

                      Returns the version of a given implementation. This value is defined by the
Version                 individual manufacturer and increments with each new revision. The
Information:Version of  format of the value has the upper 12 bits as the major number of the
Implementation        version, the next lower 12 bits as the minor number of the version, and the
                      lowest 8 bits as the sub-minor number of the version.

                                                    © National Instruments 10121

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10121 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10122 ordinal=10122 -->
## Property and Method Reference

Property and Method Reference


          Property              Description

                                Returns the value that uniquely identifies the version of the VISA
           Version                 specification to which the implementation complies. The format of the
           Information:Version of  value has the upper 12 bits as the major number of the version, the next
           Specification          lower 12 bits as the minor number of the version, and the lowest 8 bits as
                                the sub-minor number of the version.

    GPIBGPIB Settings:LineSettings:Line RENREN StateState

        Returns the current state of the GPIB REN (Remote ENable) interface line.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


        Unknown                                                                 -1

          Unasserted                                                   0

          Asserted                                                     1

    GPIBGPIB Settings:PrimarySettings:Primary AddressAddress

        Returns the primary address of the GPIB device used by the given session.

      Remarks

       The following table lists the characteristics of this property.


10122   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10122 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10123 ordinal=10123 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

GPIBGPIB Settings:ReaddressingSettings:Readdressing

Specifies whether to use repeat addressing before each read or write operation. The
default is TRUE.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

GPIBGPIB Settings:SecondarySettings:Secondary AddressAddress

Returns the secondary address of the GPIB device used by the given session. If the
device does not have a secondary address, the value of this property is 65535 (0xFFFF).

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes


                                                    © National Instruments 10123

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10123 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10124 ordinal=10124 -->
## Property and Method Reference

Property and Method Reference


           Available in Real-Time Operating System                                   Yes

    GPIBGPIB Settings:UnaddressingSettings:Unaddressing

         Specifies whether to unaddress the device (UNT and UNL) after each read or write
         operation. The default is FALSE.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

    GeneralGeneral Settings:AllowSettings:Allow DMADMA TransfersTransfers

         Specifies whether I/O accesses should attempt to use DMA (TRUE) or Programmed I/O
         (FALSE). In some implementations, this property may have global effects even though
             it is documented as a local property. This behavior affects performance and not
         functionality.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes


10124   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10124 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10125 ordinal=10125 -->
## Property and Method Reference

Property and Method Reference

GeneralGeneral Settings:MaximumSettings:Maximum QueueQueue LengthLength

Specifies the maximum number of events that can be queued at any time on the given
session. This property is read/write until the first time you call VISA Enable Event on a
session. Thereafter, it is read only. The default is 50.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

GeneralGeneral Settings:ResourceSettings:Resource ClassClass

Returns the resource class of the resource string used to open the given session. For
example, if the resource string for a given session is COM1 or ASRL1::INSTR, this
property returns INSTR, regardless of the class of the I/O control.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


                                                    © National Instruments 10125

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10125 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10126 ordinal=10126 -->
## Property and Method Reference

Property and Method Reference

    GeneralGeneral Settings:ResourceSettings:Resource LockLock StateState

        Returns the current locking state of the resource associated with the given session.
       The resource can be unlocked, locked with an exclusive lock, or locked with a shared
         lock. The default is Unlocked.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


         Unlocked                                                     0

           Exclusive                                                     1

         Shared                                                       2

    GeneralGeneral Settings:ResourceSettings:Resource NameName

        Returns the unique identifier for a resource.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


10126   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10126 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10127 ordinal=10127 -->
## Property and Method Reference

Property and Method Reference

GeneralGeneral Settings:TimeoutSettings:Timeout ValueValue

Specifies the minimum timeout value, in milliseconds, to use when accessing the
device. Note that the actual timeout that VISA returns may be higher than the one
requested. The default is 2000.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

GeneralGeneral Settings:UserSettings:User DataData

Specifies a data value for the private use of an application. The VISA implementation
stores this value in a per-session location, so that user data on other sessions does not
affect the user data on this session. VISA does not use this property for any purpose.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


                                                    © National Instruments 10127

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10127 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10128 ordinal=10128 -->
## Property and Method Reference

Property and Method Reference

     InterfaceInterface Information:InterfaceInformation:Interface DescriptionDescription

         Specifies human-readable text that describes the given interface. Note: Use the value
         of this property for display purposes only and not for programmatic decisions. The
        value can change between VISA implementations and/or revisions.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

     InterfaceInterface Information:InterfaceInformation:Interface NumberNumber

        Returns the board number for the given interface.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

     InterfaceInterface Information:InterfaceInformation:Interface TypeType

         Specifies the interface type of the given session.


10128   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10128 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10129 ordinal=10129 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


 GPIB                                                       1

 VXI                                                         2

 GPIB-VXI                                                    3

 Serial                                                       4

 PXI                                                         5

 TCPIP                                                      6

 USB                                                        7

 FireWire                                                    9

MessageMessage BasedBased Settings:FileSettings:File AppendAppend EnableEnable

Specifies whether VISA Read To File appends or overwrites (truncates) when opening a
file. If this property is set to TRUE, VISA Read To File appends when opening a file. If
this property is set to FALSE, VISA Read To File overwrites (truncates) when opening a
file. The default is FALSE.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write


                                                    © National Instruments 10129

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10129 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10130 ordinal=10130 -->
## Property and Method Reference

Property and Method Reference


           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

    MessageMessage BasedBased Settings:IOSettings:IO ProtocolProtocol

         Specifies which protocol to use. In VXI, you can choose normal word serial or fast data
        channel. In GPIB, you can choose normal or high-speed HS-488 transfers. In serial,
         TCP/IP, or USB, you can choose normal transfers or 488.2-defined strings. In USBTMC,
       you can choose normal or vendor-specific transfers. The default is Normal.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes


         Normal                                                                    1

          VXI/FDC                                                                   2

         GPIB/HS488                                                                3

          Serial-TCPIP-USB/488 Strings                                                 4

          USBTMC/Vendor-Specific                                                    5

    MessageMessage BasedBased Settings:SendSettings:Send EndEnd EnableEnable

         Specifies whether to send an END indicator on the last byte of each write operation.
        This property is relevant only in VISA Write and related operations. The default is TRUE.
      On Serial Instr sessions, if this property is set to FALSE, the write transmits the exact
        contents of the user buffer, without modifying it and without appending anything to

10130   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10130 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10131 ordinal=10131 -->
## Property and Method Reference

Property and Method Reference

the data. If this property is set to TRUE, VISA performs the behavior described in the
property End Mode for Writes (ASRL End Out). On GPIB, VXI, GPIB-VXI, TCP/IP Instr, and
USB Instr sessions, if this property is set to TRUE, VISA includes the 488.2 defined end
of message terminator.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

MessageMessage BasedBased Settings:TerminationSettings:Termination
CharacterCharacter

Specifies a character that, when read, causes a read operation to terminate. The
termination character also must be enabled. This default is 0x0A (linefeed).

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


                                                    © National Instruments 10131

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10131 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10132 ordinal=10132 -->
## Property and Method Reference

Property and Method Reference

    MessageMessage BasedBased Settings:TerminationSettings:Termination
    CharacterCharacter EnableEnable

         Specifies whether a read operation terminates when it receives the termination
         character. The default is FALSE.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

    VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
     IdentificationIdentification

        Returns a value that corresponds to the VXI manufacturer ID of the manufacturer that
        created the VISA implementation.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


10132   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10132 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10133 ordinal=10133 -->
## Property and Method Reference

Property and Method Reference

VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
NameName

Returns the name of the manufacturer that created the implementation. This is not
related to the device manufacturer attributes. Note: Use the value of this property for
display purposes only and not for programmatic decisions. The value can change
between VISA implementations and/or revisions.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VersionVersion Information:VersionInformation:Version ofof
ImplementationImplementation

Returns the version of a given implementation. This value is defined by the individual
manufacturer and increments with each new revision. The format of the value has the
upper 12 bits as the major number of the version, the next lower 12 bits as the minor
number of the version, and the lowest 8 bits as the sub-minor number of the version.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only


                                                    © National Instruments 10133

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10133 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10134 ordinal=10134 -->
## Property and Method Reference

Property and Method Reference


           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    VersionVersion Information:VersionInformation:Version ofof SpecificationSpecification

        Returns the value that uniquely identifies the version of the VISA specification to which
        the implementation complies. The format of the value has the upper 12 bits as the
       major number of the version, the next lower 12 bits as the minor number of the
         version, and the lowest 8 bits as the sub-minor number of the version.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

        InstrInstr PropertiesProperties


          Property              Description

           FireWire
                                    Specifies the upper 16 bits of the 48-bit destination address for a FireWire
           Settings:Destination
                                   device. The default is 0xFFFF.
         Upper Offset

           FireWire
                                Returns the lower chip ID for a FireWire device.
          Settings:Lower Chip ID

           FireWire
                                    Specifies the upper 16 bits of the 48-bit source address for a FireWire
           Settings:Source Upper
                                   device. The default is 0xFFFF.
           Offset

           FireWire
          Settings:Upper Chip    Returns the upper chip ID for a FireWire device.
           ID

10134   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10134 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10135 ordinal=10135 -->
## Property and Method Reference

Property and Method Reference


Property              Description

FireWire                      Returns the vendor ID for a FireWire device.Settings:Vendor ID

FireWire                        Specifies the upper 16 bits of the 48-bit address for a FireWire device whenSettings:Window                    a window is mapped. The default is 0xFFFF.
Upper Offset

GPIB Settings:Line                      Returns the current state of the GPIB REN (Remote ENable) interface line.REN State

GPIB Settings:Primary                      Returns the primary address of the GPIB device used by the given session.
Address

GPIB                   Specifies whether to use repeat addressing before each read or write
Settings:Readdressing  operation. The default is TRUE.

GPIB                 Returns the secondary address of the GPIB device used by the given
Settings:Secondary     session. If the device does not have a secondary address, the value of this
Address               property is 65535 (0xFFFF).

GPIB                   Specifies whether to unaddress the device (UNT and UNL) after each read
Settings:Unaddressing  or write operation. The default is FALSE.

                        Specifies whether I/O accesses should attempt to use DMA (TRUE) or
                  Programmed I/O (FALSE). In some implementations, this property mayGeneral Settings:Allow                    have global effects even though it is documented as a local property. This
DMA Transfers                      behavior affects performance and not functionality. Note: In the Instr class,
                          this property is valid only for GPIB, GPIB-VXI, PXI, and VXI resources.

                      Returns the ID of the manufacturer that created the device. For VXI
                        resources, this refers to the VXI Manufacturer ID. For PXI/PCI resources, this
General                          refers to the Subsystem Vendor ID (SVID) if it is nonzero; otherwise, thisSettings:Manufacturer                          refers to the Vendor ID (VID). For USB resources, this refers to the Vendor ID
Identification
                           (VID). Note: In the Instr class, this property is valid only for GPIB-VXI, VXI,
                        PXI/PCI, and USB resources.

                      Returns the name of the manufacturer that created the device. Note: Use
General               the value of this property for display purposes only and not for
Settings:Manufacturer  programmatic decisions. The value can change between VISA
Name                implementations and/or revisions. Note: In the Instr class, this property is
                         valid only for GPIB-VXI, VXI, PXI/PCI, FireWire, and USB resources.

General                 Specifies the maximum number of events that can be queued at any time
Settings:Maximum    on the given session. This property is read/write until the first time you call
Queue Length         VISA Enable Event on a session. Thereafter, it is read only. The default is 50.


                                                    © National Instruments 10135

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10135 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10136 ordinal=10136 -->
## Property and Method Reference

Property and Method Reference


          Property              Description

                                Returns the device model code assigned by the manufacturer. For VXI
                                   resources, this refers to the VXI Model Code. For PXI/PCI resources, if the
          General              Subsystem Vendor ID is nonzero, this refers to the Subsystem ID (SSID);
          Settings:Model Code   otherwise, this refers to the Device ID (DID). For USB resources, this refers
                                  to the Product ID (PID). Note: In the Instr class, this property is valid only
                                      for GPIB-VXI, VXI, PXI/PCI, and USB resources.

                                Returns the model name of the device. Note: Use the value of this property
                                      for display purposes only and not for programmatic decisions. The value          General
                              can change between VISA implementations and/or revisions. Note: In the          Settings:Model Name                                       Instr class, this property is valid only for GPIB-VXI, VXI, PXI/PCI, FireWire,
                            and USB resources.

                                Returns the resource class of the resource string used to open the given
          General                                   session. For example, if the resource string for a given session is COM1 or           Settings:Resource
                                ASRL1::INSTR, this property returns INSTR, regardless of the class of the I/O           Class                                    control.

          General               Returns the current locking state of the resource associated with the given
           Settings:Resource      session. The resource can be unlocked, locked with an exclusive lock, or
         Lock State             locked with a shared lock. The default is Unlocked.

          General
           Settings:Resource      Returns the unique identifier for a resource.
        Name

                                Returns the physical slot location of the device. If the slot is unknown, the
          General Settings:Slot   value returned is -1. Note: In the Instr class, this property is valid only for
                                  GPIB-VXI, VXI, and PXI/PCI resources.

          General                 Specifies the minimum timeout value, in milliseconds, to use when
          Settings:Timeout       accessing the device. Note that the actual timeout that VISA returns may be
          Value                 higher than the one requested. The default is 2000.

                                    Specifies which trigger mechanism to use. In VXI systems, for example, you
          General
                              can choose between software triggers and hardware triggers on a specific
           Settings:Trigger
                                     trigger line. The default is Software. Note: In the Instr class, this property is
            Identifier
                                     valid only for GPIB-VXI, VXI, and PXI resources.

                                    Specifies a data value for the private use of an application. The VISA
          General Settings:User  implementation stores this value in a per-session location, so that user
          Data                  data on other sessions does not affect the user data on this session. VISA
                             does not use this property for any purpose.

           Interface               Specifies human-readable text that describes the given interface. Note: Use
           Information:Interface   the value of this property for display purposes only and not for

10136   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10136 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10137 ordinal=10137 -->
## Property and Method Reference

Property and Method Reference


Property              Description

                    programmatic decisions. The value can change between VISADescription                     implementations and/or revisions.

Interface
Information:Interface   Returns the board number for the given interface.
Number

Interface                      Returns the board number of the parent device. Note: In the Instr class, thisInformation:Interface                      property is valid only for GPIB-VXI resources.Number of Parent

Interface
Information:Interface   Specifies the interface type of the given session.
Type

                        Specifies whether VISA Read To File appends or overwrites (truncates)Message Based                  when opening a file. If this property is set to TRUE, VISA Read To FileSettings:File Append
                   appends when opening a file. If this property is set to FALSE, VISA Read ToEnable                           File overwrites (truncates) when opening a file. The default is FALSE.

                        Specifies which protocol to use. In VXI, you can choose normal word serial
                       or fast data channel. In GPIB, you can choose normal or high-speed HS-488
Message Based                          transfers. In serial, TCP/IP, or USB, you can choose normal transfers orSettings:IO Protocol                       488.2-defined strings. In USBTMC, you can choose normal or vendor-
                          specific transfers. The default is Normal.

Message Based
Settings:Is 488.2       Returns whether the device is 488.2 compliant.
Compliant

                        Specifies whether to send an END indicator on the last byte of each write
                       operation. This property is relevant only in VISA Write and related
                       operations. The default is TRUE. On Serial Instr sessions, if this property is
Message Based         set to FALSE, the write transmits the exact contents of the user buffer,
Settings:Send End     without modifying it and without appending anything to the data. If this
Enable                property is set to TRUE, VISA performs the behavior described in the
                      property End Mode for Writes (ASRL End Out). On GPIB, VXI, GPIB-VXI, TCP/
                        IP Instr, and USB Instr sessions, if this property is set to TRUE, VISA includes
                      the 488.2 defined end of message terminator.

                        Specifies whether to terminate a read operation due to an END condition.
Message Based         This property is relevant only in VISA Read and related operations. For all
Settings:Suppress End  session types that support this property, if this property is set to TRUE,
Enable               read does not terminate due to an END condition. However, a read may still
                      terminate successfully if the Message Based Settings:Termination


                                                    © National Instruments 10137

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10137 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10138 ordinal=10138 -->
## Property and Method Reference

Property and Method Reference


          Property              Description

                                 Character Enable (TermChar En) property is set to TRUE. Otherwise, read
                             does not terminate until it receives all of the requested data (or an error
                                    occurs). The default is FALSE (except for TCP/IP Socket sessions). On Serial
                                       Instr sessions, if this property is set to FALSE, VISA performs the behavior
                                described in the Serial Settings:End Mode for Reads (ASRL End In) property.
                        On USB Raw sessions, if this property is set to FALSE, VISA performs the
                                behavior described in the USB Settings:End Mode for Reads (USB End In)
                                  property. On TCP/IP Socket sessions, if this property is set to FALSE, if NI-
                                VISA reads some data and then detects a pause in the arrival of data
                                  packets, it terminates the read operation. On TCP/IP Socket sessions, the
                                   default value for the property is TRUE in NI-VISA. On VXI Instr sessions, if
                                      this property is set to FALSE, the END bit terminates read operations.

         Message Based         Specifies a character that, when read, causes a read operation to
           Settings:Termination   terminate. The termination character also must be enabled. This default is
          Character            0x0A (linefeed).

         Message Based                                    Specifies whether a read operation terminates when it receives the           Settings:Termination
                                 termination character. The default is FALSE.          Character Enable

                                    Specifies whether the implementation should attempt to combine bus
           PXI/PCI Settings:Allow  write transfers into a large transfer before bursting over the PCI bus. In
           Write Combining     some cases you may not be able to change the write combining behavior,
                               so reading this property value may not return the same value that was set.

           PXI/PCI
                                Returns the PCI Express link width negotiated between the PCI Express           Settings:Express                                host controller and the device. A value of -1 indicates that the device is not           Settings:Actual Link
                             a PXI/PCI Express device. Common values include 1, 2, 4, 8, and 16.         Width

           PXI/PCI
           Settings:Express       Returns the differential star bus number of this device. A value of -1 means
           Settings:D-Star Bus     that the chassis is unidentified or does not have a timing slot.
        Number

           PXI/PCI
                                Returns the set of differential star lines connected to this device. A value of
           Settings:Express
                                     -1 means that the chassis is unidentified or does not have a timing slot.
           Settings:D-Star Set

           PXI/PCI
           Settings:Express       Returns whether the device is PXI/PCI or PXI/PCI Express.
            Settings:Is PCI Express

           PXI/PCI               Returns the maximum PCI Express link width of the device. A value of -1


10138   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10138 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10139 ordinal=10139 -->
## Property and Method Reference

Property and Method Reference


Property              Description

Settings:Express                        indicates that the device is not a PXI/PCI Express device. Common valuesSettings:Maximum                       include 1, 2, 4, 8, and 16.Link Width

PXI/PCI                      Returns the PCI Express link width of the PXI Express peripheral slot in
Settings:Express                    which the device resides. A value of -1 indicates that the device is not a PXISettings:Slot Link                      Express device. Common values include 1, 4, and 8.Width

PXI/PCI Settings:PCI                      Returns the PCI bus number of the PXI/PCI resource.
Bus Number

PXI/PCI Settings:PCI                      Returns the PCI device number of the PXI/PCI resource.Device Number

                      Returns the PCI function number of the PXI/PCI resource. For most devices,
PXI/PCI Settings:PCI    the function number is 0, but a multifunction device may have a function
Function Number     number up to 7. The meaning of a function number other than 0 is device-
                           specific.

PXI/PCI Settings:PCI    Returns the system-assigned base this device uses in the given space. If the
Resources:BAR0        device does not request addresses in this space, the value of this property
Address Base              is undefined.

PXI/PCI Settings:PCI    Returns the requested address size of this device in the given space. If the
Resources:BAR0        device does not request addresses in this space, the value of this property
Address Size               is undefined.

PXI/PCI Settings:PCI    Returns what type of address requirements (memory or I/O) the device has
Resources:BAR0         for this Base Address Register. If the device does not request addresses in
Address Type            this space, this property returns None (0).

PXI/PCI Settings:PCI    Returns the system-assigned base this device uses in the given space. If the
Resources:BAR1        device does not request addresses in this space, the value of this property
Address Base              is undefined.

PXI/PCI Settings:PCI    Returns the requested address size of this device in the given space. If the
Resources:BAR1        device does not request addresses in this space, the value of this property
Address Size               is undefined.

PXI/PCI Settings:PCI    Returns what type of address requirements (memory or I/O) the device has
Resources:BAR1         for this Base Address Register. If the device does not request addresses in
Address Type            this space, this property returns None (0).

PXI/PCI Settings:PCI    Returns the system-assigned base this device uses in the given space. If the
Resources:BAR2        device does not request addresses in this space, the value of this property


                                                    © National Instruments 10139

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10139 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10140 ordinal=10140 -->
## Property and Method Reference

Property and Method Reference


          Property              Description

          Address Base              is undefined.

           PXI/PCI Settings:PCI    Returns the requested address size of this device in the given space. If the
          Resources:BAR2        device does not request addresses in this space, the value of this property
          Address Size               is undefined.

           PXI/PCI Settings:PCI    Returns what type of address requirements (memory or I/O) the device has
          Resources:BAR2         for this Base Address Register. If the device does not request addresses in
          Address Type            this space, this property returns None (0).

           PXI/PCI Settings:PCI    Returns the system-assigned base this device uses in the given space. If the
          Resources:BAR3        device does not request addresses in this space, the value of this property
          Address Base              is undefined.

           PXI/PCI Settings:PCI    Returns the requested address size of this device in the given space. If the
          Resources:BAR3        device does not request addresses in this space, the value of this property
          Address Size               is undefined.

           PXI/PCI Settings:PCI    Returns what type of address requirements (memory or I/O) the device has
          Resources:BAR3         for this Base Address Register. If the device does not request addresses in
          Address Type            this space, this property returns None (0).

           PXI/PCI Settings:PCI    Returns the system-assigned base this device uses in the given space. If the
          Resources:BAR4        device does not request addresses in this space, the value of this property
          Address Base              is undefined.

           PXI/PCI Settings:PCI    Returns the requested address size of this device in the given space. If the
          Resources:BAR4        device does not request addresses in this space, the value of this property
          Address Size               is undefined.

           PXI/PCI Settings:PCI    Returns what type of address requirements (memory or I/O) the device has
          Resources:BAR4         for this Base Address Register. If the device does not request addresses in
          Address Type            this space, this property returns None (0).

           PXI/PCI Settings:PCI    Returns the system-assigned base this device uses in the given space. If the
          Resources:BAR5        device does not request addresses in this space, the value of this property
          Address Base              is undefined.

           PXI/PCI Settings:PCI    Returns the requested address size of this device in the given space. If the
          Resources:BAR5        device does not request addresses in this space, the value of this property
          Address Size               is undefined.

           PXI/PCI Settings:PCI    Returns what type of address requirements (memory or I/O) the device has
          Resources:BAR5         for this Base Address Register. If the device does not request addresses in
          Address Type            this space, this property returns None (0).

           PXI/PCI Settings:PXI    Returns the PXI chassis number of this device. A value of -1 means the

10140   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10140 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10141 ordinal=10141 -->
## Property and Method Reference

Property and Method Reference


Property              Description

Chassis Number        chassis number is unknown. Other valid values are 0 to 255.

PXI/PCI Settings:Slot   Returns the slot number or special feature connected to the local bus left
Local Bus Left           lines of this device.

PXI/PCI Settings:Slot   Returns the slot number or special feature connected to the local bus right
Local Bus Right         lines of this device.

PXI/PCI Settings:Slot                      Returns the slot path of this device.Path

PXI/PCI Settings:Star                      Returns the star trigger bus number of this device.
Trigger Bus Number

PXI/PCI Settings:Star                      Returns the PXI_STAR line connected to this device.Trigger Line

PXI/PCI
Settings:Trigger Bus    Returns the trigger bus number of this device.
Number

                        Specifies the number of elements by which to increment the destination
Register Based        address on block move operations. Valid values include 0 and 1. The
Settings:Destination    default is 1. If this property is set to 0, VISA Move Out X operations always
Increment Count      read from the same element, essentially treating the destination as a FIFO
                           register.

                        Specifies the number of elements by which to increment the source
Register Based        address on block move operations. Valid values include 0 and 1. The
Settings:Source        default is 1. If this property is set to 0, VISA Move In X operations always
Increment Count      read from the same element, essentially treating the source as a FIFO
                           register.

Register Based
                      Returns whether the current session has a mapped window, and if so,
Settings:Window
                    whether the window allows direct pointer dereferences.
Access

Register Based         Returns the base interface address to which this window maps. If the
Settings:Window Base  Window Access property is Not Mapped, the value of this property is
Address               undefined.

Register Based         Returns the size of the region mapped to this window. If the Window Access
Settings:Window Size   property is Not Mapped, the value of this property is undefined.

                        Specifies whether to allow transmission. If FALSE, the serial port suspends
Serial Settings:Allow
                       transmission as if an XOFF character has been received. If TRUE, it resumes
Transmit
                       transmission as if an XON character has been received. If XON/XOFF flow

                                                    © National Instruments 10141

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10141 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10142 ordinal=10142 -->
## Property and Method Reference

Property and Method Reference


          Property              Description

                                  control (software handshaking) is not being used, FALSE is an invalid value.
                            The default is TRUE.

                                    Specifies the baud rate of the given communications port. The rate is
            Serial Settings:Baud    represented as an unsigned 32-bit integer so that any baud rate can be
          Rate                  used, but the communications port usually requires a commonly used rate
                              such as 300, 1200, 2400, or 9600 baud.

                                    Specifies the duration (in milliseconds) of the break signal asserted when
            Serial Settings:Break   End Mode for Writes (ASRL End Out) is set to Break (3). Valid values include
          Length                 1-500. The default is 250. If you want to control the assertion state and
                                 length of a break signal manually, use the VISA Serial Break VI instead.

                                    Specifies the number of data bits contained in each frame. Valid values            Serial Settings:Data
                                 include 5-8. The data bits for each frame are located in the low-order bits of            Bits                                every byte stored in memory.

                                    Specifies whether to discard each data byte whose value is 0. If this
            Serial Settings:Discard  property is TRUE, read operations discard NUL characters. If this property
        NUL Characters           is FALSE, read operations treat NUL characters as normal data characters.
                                For binary transfers, set this property to FALSE. The default is FALSE.

                                    Specifies the method used to terminate read operations. Valid values
            Serial Settings:End     include: (0) None, (1) Last Bit, (2) TermChar. If the value is (2) TermChar,
        Mode for Reads        then the value of the property Termination Character Enable (TermChar
                                En) is ignored. The default is (2) TermChar.

                                    Specifies the method used to terminate write operations. Valid values            Serial Settings:End                                   include: (0) None, (1) Last Bit, (2) TermChar, (3) Break. The default is (0)
        Mode for Writes                              None.

            Serial Settings:Error
                                    Specifies the character to use to replace incoming characters that arrive
         Replacement
                                with errors (such as a parity error). The default is 0.
          Character

                                    Specifies the flow control method used for both transmitting and receiving
                                   data. Valid values include: (0) Flow None, (1) Flow XON/XOFF, (2) Flow RTS/
            Serial Settings:Flow
                                CTS, (3) Flow XON/XOFF and RTS/CTS, (4) Flow DTR/DSR, (5) Flow XON/
          Control
                           XOFF and DTR/DSR. Certain values or combinations of values may not be
                               supported by all serial ports and/or operating systems.

                                    Specifies the value of the XOFF character used for XON/XOFF flow control
            Serial Settings:Flow
                                 (both directions). If XON/XOFF flow control (software handshaking) is not
          Control XOFF
                               being used, the value of this property is ignored. The default is 0x13
          Character
                                     (Control-S).


10142   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10142 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10143 ordinal=10143 -->
## Property and Method Reference

Property and Method Reference


Property              Description

                        Specifies the value of the XON character used for XON/XOFF flow control
Serial Settings:Flow    (both directions). If XON/XOFF flow control (software handshaking) is not
Control XON Character  being used, the value of this property is ignored. The default is 0x11
                        (Control-Q).

                      Returns whether the port is properly connected to another port or device.
Serial Settings:Is Port   This property is valid only with serial drivers developed by National
Connected            Instruments and documented to support this feature with the
                      corresponding National Instruments hardware.

                       Sets manual control of the serial port's break state. If asserted, this
                      property suspends character transmission and places the transmission lineSerial Settings:Modem                         in a break state until this property is unasserted. If you want VISA to send aLine Settings:Break                     break signal after each write operation automatically, use the Break Length
State                      (Break Len) and End Mode for Writes (ASRL End Out) properties instead.
                   The default is Unasserted.

Serial Settings:Modem
Line Settings:Line CTS  Returns the current state of the Clear To Send (CTS) input signal.
State

                        Specifies the current state of the Data Carrier Detect (DCD) input signal.
                       This is often used by modems to indicate the detection of a carrier
Serial Settings:Modem                  (modem) on the phone line. This signal is also known as Receive LineLine Settings:Line DCD                       Signal Detect (RLSD). This property is read only except when the Wire Mode
State                      property is set to RS232/DCE, or RS232/Auto with the hardware currently in
                      the DCE state.

Serial Settings:Modem
Line Settings:Line DSR  Returns the current state of the Data Set Ready (DSR) input signal.
State

Serial Settings:Modem
                        Asserts or unasserts the Data Terminal Ready (DTR) output signal
Line Settings:Line DTR
                      manually.
State

                        Specifies the current state of the Ring Indicator (RI) input signal. The RI
Serial Settings:Modem  signal is often used by modems to indicate that the telephone line is
Line Settings:Line RI    ringing. This property is read only except when the Wire Mode property is
State                   set to RS232/DCE or to RS232/Auto with the hardware currently in the DCE
                           state.

Serial Settings:Modem  Asserts or unasserts the Request To Send (RTS) output signal manually.
Line Settings:Line RTS  When the flow control is set to hardware handshaking, it is invalid to
State                change this property.


                                                    © National Instruments 10143

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10143 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10144 ordinal=10144 -->
## Property and Method Reference

Property and Method Reference


          Property              Description

            Serial                                Returns the number of bytes currently available at the serial port used by          Settings:Number of                                      this session.          Bytes at Serial Port

                                    Specifies the parity used with every frame that is transmitted or received.
                                    Valid values include: (0) Parity None, (1) Parity Odd, (2) Parity Even, (3)            Serial Settings:Parity                                     Parity Mark, (4) Parity Space. Mark means that the parity bit exists and is
                               always 1. Space means that the parity bit exists and is always 0.

            Serial Settings:Stop     Specifies the number of stop bits used to indicate the end of a frame. Valid
            Bits                   values include: (10) Stop One, (15) Stop One-and-a-Half, (20) Stop Two.

                                    Specifies the current wire/transceiver mode. For RS485 hardware, this
                                property is valid only with the RS485 serial driver developed by National
                                 Instruments. For RS232 hardware, the values RS232/DCE and RS232/Auto            Serial Settings:Wire                                 are valid only with RS232 serial drivers developed by National Instruments        Mode
                            and documented to support this feature with the corresponding National
                                Instruments hardware. When this feature is not supported, RS232/DTE is
                                the only valid value.

          TCP/IP
                                Returns the host name of the device. If no host name is available, this          Settings:Computer                                property returns an empty string.         Hostname

          TCP/IP Settings:Dot-    Returns the TCPIP address of the device to which the session is connected.
          Notation Address       This string is formatted in dot notation.

          TCP/IP Settings:HiSLIP
           Settings:Encryption    Controls and returns communication encryption.
         Enabled

          TCP/IP Settings:HiSLIP
                                    Specifies the HiSLIP maximum message size in kilobytes, where a kilobyte
          Settings:Maximum
                                            is 1024 bytes.
         Message KBytes

          TCP/IP Settings:HiSLIP
           Settings:Overlap        Specifies whether the HiSLIP 'overlap' mode is enabled.
         Enabled

          TCP/IP Settings:HiSLIP
           Settings:Protocol      Returns the negotiated HiSLIP protocol version.
           Version

          TCP/IP Settings:HiSLIP
                                Returns a string that indicates the SASL mechanism used to authenticate
           Settings:SASL
                                the client.
         Mechanism


10144   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10144 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10145 ordinal=10145 -->
## Property and Method Reference

Property and Method Reference


Property              Description

TCP/IP Settings:Is      Returns whether this session is using the HiSLIP protocol to communicate
HiSLIP                with the device.

                        Specifies whether to use keep-alive packets on TCP connections. Setting
                          this property to TRUE requests that a TCP/IP provider enable the use of
                       keep-alive packets on TCP connections. After the system detects a droppedTCP/IP Settings:Keep-                       connection, VISA returns a lost connection error code on subsequent I/OAlive Packets                           calls on the session. The time required for the system to detect the
                    dropped connection depends on the system and is not settable. The
                        default is FALSE.

TCP/IP Settings:LAN    Returns the LAN device name used by the VXI-11 protocol (for example,
Device Name            inst0) during connection.

                        Specifies whether the Nagle algorithm is enabled. The Nagle algorithm is
                       disabled when this property is TRUE (and vice versa). The Nagle algorithmTCP/IP Settings:No
                     improves network performance by buffering written data until a full-sizePacket Delay                      packet can be sent. This property is TRUE by default in VISA to verify that
                        writes get flushed immediately.

TCP/IP Settings:Server
                      Returns the expiration date of the server certificate. The form is ASN.1Certificate Expiration                   UTCTime “YYMMDDhhmm[ss]Z.Date

TCP/IP Settings:Server
Certificate Is            Indicates the certificate does not expire.
Perpetual

TCP/IP Settings:Server
Certificate Issuer       Returns the name of the CA that signed the certificate in RFC4514 format.
Name

TCP/IP Settings:Server
                      Returns the serial number and subject field from the certificate om
Certificate Subject
                    RFC4514 format.
Name

TCP/IP Settings:TLS
                      Returns a string that indicates the cipher suite used by TLS.
Cipher Suite

                        Specifies the maximum size of data stored by any given USB interrupt. If a
USB              USB interrupt contains more data than this size, the data in excess of this
Settings:Maximum      size is lost. This property is read/write when the corresponding session is
Interrupt Size          not enabled to receive USB interrupt events. When the session is enabled
                       to receive USB interrupt events, this property is read only.

USB Settings:Serial     Returns the USB serial number of this device.


                                                    © National Instruments 10145

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10145 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10146 ordinal=10146 -->
## Property and Method Reference

Property and Method Reference


          Property              Description

        Number

        USB Settings:USB                                Returns the USB interface number used by the given session.           Interface Number

        USB Settings:USB                                Returns the USB protocol used by the given session.
           Protocol

          VXI/VME                Specifies the address modifier to use in high-level access operations, such
           Settings:Destination    as VISA Out X and VISA Move Out X, when writing to the destination. The
          Access Privilege        default is Data/Privileged (0).

          VXI/VME                Specifies the byte order to use in high-level access operations, such as VISA
           Settings:Destination   Out X and VISA Move Out X, when writing to the destination. The default is
          Byte Order             Big Endian (0).

          VXI/VME Settings:Fast                                    Specifies whether FDC transfers use normal or streaming mode. The          Data Channel:Channel                                   default is Normal.
        Mode

          VXI/VME Settings:Fast                                    Specifies which FDC channel to use to transfer data buffers. Valid values
          Data Channel:Channel                                 include 0-7.        Number

          VXI/VME Settings:Fast                                    Specifies whether transfers use a pair of FDC channels. If you do not set          Data Channel:Use
                                      this property, transfers use only one FDC channel. The default is FALSE.         Channel Pairs

          VXI/VME
                                Returns whether the VXI device is an immediate servant of the local          Settings:Immediate                                      controller.          Servant

          VXI/VME                                Returns the lowest logical address in the mainframe in which the device
          Settings:Mainframe
                                     resides.
           Logical Address

          VXI/VME                Specifies the address modifier to use in high-level access operations, such
           Settings:Source        as VISA In X and VISA Move In X, when reading from the source. The default
          Access Privilege           is Data/Privileged (0).

          VXI/VME                Specifies the byte order to use in high-level access operations, such as VISA
           Settings:Source Byte    In X and VISA Move In X, when reading from the source. The default is Big
          Order                Endian (0).

          VXI/VME
                                Returns which VXI trigger lines this implementation supports. This property
          Settings:Supported
                                  returns a bit vector with bits 0-9 corresponding to TTL0 through ECL1.
           VXI Trigger Lines

10146   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10146 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10147 ordinal=10147 -->
## Property and Method Reference

Property and Method Reference


Property              Description

VXI/VME Settings:VXI
Commander Logical    Returns the logical address of the commander of the VXI device.
Address

VXI/VME Settings:VXI                      Returns the class to which the VXI or VME device belongs.
Device Class

VXI/VME Settings:VXI                      Returns the logical address of the VXI device.Logical Address

VXI/VME Settings:VXI
Memory Address       Returns the VXI address space used by the device.
Space

VXI/VME Settings:VXI                      Returns the base address of the device in VXI memory space.
Memory Base Address

VXI/VME Settings:VXI                      Returns the size of memory requested by the device in VXI memory space.
Memory Size

                        Specifies the directions of the mapped TTL triggers lines. This is a bit
                       vector where bits 0-7 represent TTL triggers 0-7 respectively. A bit value ofVXI/VME Settings:VXI                    0 means the corresponding line is routed out of the frame, and a value of 1
Trigger Directions                  means the line is routed into the frame. Lines must be enabled using VXI/
                 VME Settings:VXI Trigger Lines Enable.

                        Specifies which VXI TLL triggers have mappings. This is a bit vector where
                          bits 0-7 represent TTL triggers 0-7 respectively. A bit value of 0 means the
VXI/VME Settings:VXI                      corresponding trigger line is unmapped, and 1 means a mapping exists.Trigger Lines Enable                   Use VXI/VME Settings:VXI Trigger Directions to set an enabled line's
                         direction.

VXI/VME                Specifies the address modifier to use in low-level access operations, such
Settings:Window       as VISA Map Address, VISA Peek X, and VISA Poke X, when accessing the
Access Privilege      mapped window. The default is Data/Privileged (0).

VXI/VME                Specifies the byte order to use in low-level access operations, such as VISA
Settings:Window Byte  Map Address, VISA Peek X, and VISA Poke X, when accessing the mapped
Order               window. The default is Big Endian (0).

Version
Information:Resource  Returns a value that corresponds to the VXI manufacturer ID of the
Manufacturer         manufacturer that created the VISA implementation.
Identification

Version               Returns the name of the manufacturer that created the implementation.


                                                    © National Instruments 10147

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10147 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10148 ordinal=10148 -->
## Property and Method Reference

Property and Method Reference


          Property              Description

                                  This is not related to the device manufacturer attributes. Note: Use the
          Information:Resource  value of this property for display purposes only and not for programmatic
          Manufacturer Name    decisions. The value can change between VISA implementations and/or
                                     revisions.

                                Returns the version of a given implementation. This value is defined by the
           Version                 individual manufacturer and increments with each new revision. The
           Information:Version of  format of the value has the upper 12 bits as the major number of the
          Implementation        version, the next lower 12 bits as the minor number of the version, and the
                                lowest 8 bits as the sub-minor number of the version.

                                Returns the value that uniquely identifies the version of the VISA
           Version                 specification to which the implementation complies. The format of the
           Information:Version of  value has the upper 12 bits as the major number of the version, the next
           Specification          lower 12 bits as the minor number of the version, and the lowest 8 bits as
                                the sub-minor number of the version.

     FireWireFireWire Settings:DestinationSettings:Destination UpperUpper OffsetOffset

         Specifies the upper 16 bits of the 48-bit destination address for a FireWire device. The
         default is 0xFFFF.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

     FireWireFireWire Settings:LowerSettings:Lower ChipChip IDID

        Returns the lower chip ID for a FireWire device.


10148   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10148 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10149 ordinal=10149 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

FireWireFireWire Settings:SourceSettings:Source UpperUpper OffsetOffset

Specifies the upper 16 bits of the 48-bit source address for a FireWire device. The
default is 0xFFFF.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

FireWireFireWire Settings:UpperSettings:Upper ChipChip IDID

Returns the upper chip ID for a FireWire device.

Remarks

The following table lists the characteristics of this property.


 Data type

                                                    © National Instruments 10149

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10149 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10150 ordinal=10150 -->
## Property and Method Reference

Property and Method Reference


          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

     FireWireFireWire Settings:VendorSettings:Vendor IDID

        Returns the vendor ID for a FireWire device.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

     FireWireFireWire Settings:WindowSettings:Window UpperUpper OffsetOffset

         Specifies the upper 16 bits of the 48-bit address for a FireWire device when a window is
       mapped. The default is 0xFFFF.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes


10150   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10150 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10151 ordinal=10151 -->
## Property and Method Reference

Property and Method Reference

GPIBGPIB Settings:LineSettings:Line RENREN StateState

Returns the current state of the GPIB REN (Remote ENable) interface line.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


 Unknown                                                                 -1

 Unasserted                                                   0

 Asserted                                                     1

GPIBGPIB Settings:PrimarySettings:Primary AddressAddress

Returns the primary address of the GPIB device used by the given session.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


                                                    © National Instruments 10151

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10151 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10152 ordinal=10152 -->
## Property and Method Reference

Property and Method Reference

    GPIBGPIB Settings:ReaddressingSettings:Readdressing

         Specifies whether to use repeat addressing before each read or write operation. The
         default is TRUE.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

    GPIBGPIB Settings:SecondarySettings:Secondary AddressAddress

        Returns the secondary address of the GPIB device used by the given session. If the
        device does not have a secondary address, the value of this property is 65535 (0xFFFF).

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    GPIBGPIB Settings:UnaddressingSettings:Unaddressing

         Specifies whether to unaddress the device (UNT and UNL) after each read or write


10152   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10152 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10153 ordinal=10153 -->
## Property and Method Reference

Property and Method Reference

operation. The default is FALSE.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

GeneralGeneral Settings:AllowSettings:Allow DMADMA TransfersTransfers

Specifies whether I/O accesses should attempt to use DMA (TRUE) or Programmed I/O
(FALSE). In some implementations, this property may have global effects even though
it is documented as a local property. This behavior affects performance and not
functionality. Note: In the Instr class, this property is valid only for GPIB, GPIB-VXI, PXI,
and VXI resources.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

GeneralGeneral Settings:ManufacturerSettings:Manufacturer IdentificationIdentification

Returns the ID of the manufacturer that created the device. For VXI resources, this
refers to the VXI Manufacturer ID. For PXI/PCI resources, this refers to the Subsystem


                                                    © National Instruments 10153

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10153 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10154 ordinal=10154 -->
## Property and Method Reference

Property and Method Reference

       Vendor ID (SVID) if it is nonzero; otherwise, this refers to the Vendor ID (VID). For USB
         resources, this refers to the Vendor ID (VID). Note: In the Instr class, this property is
         valid only for GPIB-VXI, VXI, PXI/PCI, and USB resources.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    GeneralGeneral Settings:ManufacturerSettings:Manufacturer NameName

        Returns the name of the manufacturer that created the device. Note: Use the value of
          this property for display purposes only and not for programmatic decisions. The value
       can change between VISA implementations and/or revisions. Note: In the Instr class,
          this property is valid only for GPIB-VXI, VXI, PXI/PCI, FireWire, and USB resources.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    GeneralGeneral Settings:MaximumSettings:Maximum QueueQueue LengthLength

         Specifies the maximum number of events that can be queued at any time on the given


10154   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10154 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10155 ordinal=10155 -->
## Property and Method Reference

Property and Method Reference

session. This property is read/write until the first time you call VISA Enable Event on a
session. Thereafter, it is read only. The default is 50.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

GeneralGeneral Settings:ModelSettings:Model CodeCode

Returns the device model code assigned by the manufacturer. For VXI resources, this
refers to the VXI Model Code. For PXI/PCI resources, if the Subsystem Vendor ID is
nonzero, this refers to the Subsystem ID (SSID); otherwise, this refers to the Device ID
(DID). For USB resources, this refers to the Product ID (PID). Note: In the Instr class, this
property is valid only for GPIB-VXI, VXI, PXI/PCI, and USB resources.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

GeneralGeneral Settings:ModelSettings:Model NameName

Returns the model name of the device. Note: Use the value of this property for display


                                                    © National Instruments 10155

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10155 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10156 ordinal=10156 -->
## Property and Method Reference

Property and Method Reference

        purposes only and not for programmatic decisions. The value can change between
        VISA implementations and/or revisions. Note: In the Instr class, this property is valid
        only for GPIB-VXI, VXI, PXI/PCI, FireWire, and USB resources.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    GeneralGeneral Settings:ResourceSettings:Resource ClassClass

        Returns the resource class of the resource string used to open the given session. For
        example, if the resource string for a given session is COM1 or ASRL1::INSTR, this
        property returns INSTR, regardless of the class of the I/O control.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    GeneralGeneral Settings:ResourceSettings:Resource LockLock StateState

        Returns the current locking state of the resource associated with the given session.
       The resource can be unlocked, locked with an exclusive lock, or locked with a shared


10156   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10156 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10157 ordinal=10157 -->
## Property and Method Reference

Property and Method Reference

lock. The default is Unlocked.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


 Unlocked                                                     0

 Exclusive                                                     1

 Shared                                                       2

GeneralGeneral Settings:ResourceSettings:Resource NameName

Returns the unique identifier for a resource.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

GeneralGeneral Settings:SlotSettings:Slot

Returns the physical slot location of the device. If the slot is unknown, the value

                                                    © National Instruments 10157

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10157 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10158 ordinal=10158 -->
## Property and Method Reference

Property and Method Reference

        returned is -1. Note: In the Instr class, this property is valid only for GPIB-VXI, VXI, and
        PXI/PCI resources.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    GeneralGeneral Settings:TimeoutSettings:Timeout ValueValue

         Specifies the minimum timeout value, in milliseconds, to use when accessing the
         device. Note that the actual timeout that VISA returns may be higher than the one
        requested. The default is 2000.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

    GeneralGeneral Settings:TriggerSettings:Trigger IdentifierIdentifier

         Specifies which trigger mechanism to use. In VXI systems, for example, you can choose
       between software triggers and hardware triggers on a specific trigger line. The default
           is Software. Note: In the Instr class, this property is valid only for GPIB-VXI, VXI, and PXI


10158   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10158 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10159 ordinal=10159 -->
## Property and Method Reference

Property and Method Reference

resources.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


 Software                                                             -1

 TTL0                                                     0

 TTL1                                                     1

 TTL2                                                     2

 TTL3                                                     3

 TTL4                                                     4

 TTL5                                                     5

 TTL6                                                     6

 TTL7                                                     7

 ECL0                                                     8

 ECL1                                                     9

GeneralGeneral Settings:UserSettings:User DataData

Specifies a data value for the private use of an application. The VISA implementation
stores this value in a per-session location, so that user data on other sessions does not
affect the user data on this session. VISA does not use this property for any purpose.


                                                    © National Instruments 10159

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10159 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10160 ordinal=10160 -->
## Property and Method Reference

Property and Method Reference

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

     InterfaceInterface Information:InterfaceInformation:Interface DescriptionDescription

         Specifies human-readable text that describes the given interface. Note: Use the value
         of this property for display purposes only and not for programmatic decisions. The
        value can change between VISA implementations and/or revisions.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

     InterfaceInterface Information:InterfaceInformation:Interface NumberNumber

        Returns the board number for the given interface.

      Remarks

       The following table lists the characteristics of this property.


10160   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10160 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10161 ordinal=10161 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

InterfaceInterface Information:InterfaceInformation:Interface NumberNumber ofof
ParentParent

Returns the board number of the parent device. Note: In the Instr class, this property is
valid only for GPIB-VXI resources.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

InterfaceInterface Information:InterfaceInformation:Interface TypeType

Specifies the interface type of the given session.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only


                                                    © National Instruments 10161

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10161 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10162 ordinal=10162 -->
## Property and Method Reference

Property and Method Reference


           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


         GPIB                                                       1

          VXI                                                         2

          GPIB-VXI                                                    3

           Serial                                                       4

          PXI                                                         5

         TCPIP                                                      6

        USB                                                        7

          FireWire                                                    9

    MessageMessage BasedBased Settings:FileSettings:File AppendAppend EnableEnable

         Specifies whether VISA Read To File appends or overwrites (truncates) when opening a
            file. If this property is set to TRUE, VISA Read To File appends when opening a file. If
          this property is set to FALSE, VISA Read To File overwrites (truncates) when opening a
            file. The default is FALSE.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes


10162   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10162 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10163 ordinal=10163 -->
## Property and Method Reference

Property and Method Reference

MessageMessage BasedBased Settings:IOSettings:IO ProtocolProtocol

Specifies which protocol to use. In VXI, you can choose normal word serial or fast data
channel. In GPIB, you can choose normal or high-speed HS-488 transfers. In serial,
TCP/IP, or USB, you can choose normal transfers or 488.2-defined strings. In USBTMC,
you can choose normal or vendor-specific transfers. The default is Normal.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


 Normal                                                                    1

 VXI/FDC                                                                   2

 GPIB/HS488                                                                3

 Serial-TCPIP-USB/488 Strings                                                 4

 USBTMC/Vendor-Specific                                                    5

MessageMessage BasedBased Settings:IsSettings:Is 488.2488.2 CompliantCompliant

Returns whether the device is 488.2 compliant.

Remarks

The following table lists the characteristics of this property.


 Data type


                                                    © National Instruments 10163

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10163 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10164 ordinal=10164 -->
## Property and Method Reference

Property and Method Reference


          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    MessageMessage BasedBased Settings:SendSettings:Send EndEnd EnableEnable

         Specifies whether to send an END indicator on the last byte of each write operation.
        This property is relevant only in VISA Write and related operations. The default is TRUE.
      On Serial Instr sessions, if this property is set to FALSE, the write transmits the exact
        contents of the user buffer, without modifying it and without appending anything to
        the data. If this property is set to TRUE, VISA performs the behavior described in the
        property End Mode for Writes (ASRL End Out). On GPIB, VXI, GPIB-VXI, TCP/IP Instr, and
      USB Instr sessions, if this property is set to TRUE, VISA includes the 488.2 defined end
         of message terminator.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

    MessageMessage BasedBased Settings:SuppressSettings:Suppress EndEnd
    EnableEnable

         Specifies whether to terminate a read operation due to an END condition. This
        property is relevant only in VISA Read and related operations. For all session types that
        support this property, if this property is set to TRUE, read does not terminate due to an
      END condition. However, a read may still terminate successfully if the Message Based
        Settings:Termination Character Enable (TermChar En) property is set to TRUE.

10164   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10164 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10165 ordinal=10165 -->
## Property and Method Reference

Property and Method Reference

Otherwise, read does not terminate until it receives all of the requested data (or an
error occurs). The default is FALSE (except for TCP/IP Socket sessions). On Serial Instr
sessions, if this property is set to FALSE, VISA performs the behavior described in the
Serial Settings:End Mode for Reads (ASRL End In) property. On USB Raw sessions, if
this property is set to FALSE, VISA performs the behavior described in the USB
Settings:End Mode for Reads (USB End In) property. On TCP/IP Socket sessions, if this
property is set to FALSE, if NI-VISA reads some data and then detects a pause in the
arrival of data packets, it terminates the read operation. On TCP/IP Socket sessions,
the default value for the property is TRUE in NI-VISA. On VXI Instr sessions, if this
property is set to FALSE, the END bit terminates read operations.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

MessageMessage BasedBased Settings:TerminationSettings:Termination
CharacterCharacter

Specifies a character that, when read, causes a read operation to terminate. The
termination character also must be enabled. This default is 0x0A (linefeed).

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

                                                    © National Instruments 10165

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10165 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10166 ordinal=10166 -->
## Property and Method Reference

Property and Method Reference


           Available in Real-Time Operating System                                  Yes

    MessageMessage BasedBased Settings:TerminationSettings:Termination
    CharacterCharacter EnableEnable

         Specifies whether a read operation terminates when it receives the termination
         character. The default is FALSE.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

    PXI/PCIPXI/PCI Settings:AllowSettings:Allow WriteWrite CombiningCombining

         Specifies whether the implementation should attempt to combine bus write transfers
         into a large transfer before bursting over the PCI bus. In some cases you may not be
        able to change the write combining behavior, so reading this property value may not
         return the same value that was set.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes


10166   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10166 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10167 ordinal=10167 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                                  Yes

PXI/PCIPXI/PCI Settings:ExpressSettings:Express Settings:ActualSettings:Actual LinkLink
WidthWidth

Returns the PCI Express link width negotiated between the PCI Express host controller
and the device. A value of -1 indicates that the device is not a PXI/PCI Express device.
Common values include 1, 2, 4, 8, and 16.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

PXI/PCIPXI/PCI Settings:ExpressSettings:Express Settings:D-StarSettings:D-Star BusBus
NumberNumber

Returns the differential star bus number of this device. A value of -1 means that the
chassis is unidentified or does not have a timing slot.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only


                                                    © National Instruments 10167

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10167 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10168 ordinal=10168 -->
## Property and Method Reference

Property and Method Reference


           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    PXI/PCIPXI/PCI Settings:ExpressSettings:Express Settings:D-StarSettings:D-Star SetSet

        Returns the set of differential star lines connected to this device. A value of -1 means
         that the chassis is unidentified or does not have a timing slot.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    PXI/PCIPXI/PCI Settings:ExpressSettings:Express Settings:IsSettings:Is PCIPCI
    ExpressExpress

        Returns whether the device is PXI/PCI or PXI/PCI Express.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


10168   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10168 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10169 ordinal=10169 -->
## Property and Method Reference

Property and Method Reference

PXI/PCIPXI/PCI Settings:ExpressSettings:Express Settings:MaximumSettings:Maximum
LinkLink WidthWidth

Returns the maximum PCI Express link width of the device. A value of -1 indicates that
the device is not a PXI/PCI Express device. Common values include 1, 2, 4, 8, and 16.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

PXI/PCIPXI/PCI Settings:ExpressSettings:Express Settings:SlotSettings:Slot LinkLink
WidthWidth

Returns the PCI Express link width of the PXI Express peripheral slot in which the
device resides. A value of -1 indicates that the device is not a PXI Express device.
Common values include 1, 4, and 8.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


                                                    © National Instruments 10169

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10169 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10170 ordinal=10170 -->
## Property and Method Reference

Property and Method Reference

    PXI/PCIPXI/PCI Settings:PCISettings:PCI BusBus NumberNumber

        Returns the PCI bus number of the PXI/PCI resource.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    PXI/PCIPXI/PCI Settings:PCISettings:PCI DeviceDevice NumberNumber

        Returns the PCI device number of the PXI/PCI resource.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    PXI/PCIPXI/PCI Settings:PCISettings:PCI FunctionFunction NumberNumber

        Returns the PCI function number of the PXI/PCI resource. For most devices, the
        function number is 0, but a multifunction device may have a function number up to 7.
       The meaning of a function number other than 0 is device-specific.


10170   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10170 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10171 ordinal=10171 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

PXI/PCIPXI/PCI Settings:PCISettings:PCI Resources:BAR0Resources:BAR0
AddressAddress BaseBase

Returns the system-assigned base this device uses in the given space. If the device
does not request addresses in this space, the value of this property is undefined.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

PXI/PCIPXI/PCI Settings:PCISettings:PCI Resources:BAR0Resources:BAR0
AddressAddress SizeSize

Returns the requested address size of this device in the given space. If the device does
not request addresses in this space, the value of this property is undefined.


                                                    © National Instruments 10171

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10171 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10172 ordinal=10172 -->
## Property and Method Reference

Property and Method Reference

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    PXI/PCIPXI/PCI Settings:PCISettings:PCI Resources:BAR0Resources:BAR0
    AddressAddress TypeType

        Returns what type of address requirements (memory or I/O) the device has for this
       Base Address Register. If the device does not request addresses in this space, this
        property returns None (0).

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


        None                                                      0

        Memory                                                   1

           I/O                                                        2


10172   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10172 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10173 ordinal=10173 -->
## Property and Method Reference

Property and Method Reference

PXI/PCIPXI/PCI Settings:PCISettings:PCI Resources:BAR1Resources:BAR1
AddressAddress BaseBase

Returns the system-assigned base this device uses in the given space. If the device
does not request addresses in this space, the value of this property is undefined.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

PXI/PCIPXI/PCI Settings:PCISettings:PCI Resources:BAR1Resources:BAR1
AddressAddress SizeSize

Returns the requested address size of this device in the given space. If the device does
not request addresses in this space, the value of this property is undefined.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


                                                    © National Instruments 10173

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10173 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10174 ordinal=10174 -->
## Property and Method Reference

Property and Method Reference

    PXI/PCIPXI/PCI Settings:PCISettings:PCI Resources:BAR1Resources:BAR1
    AddressAddress TypeType

        Returns what type of address requirements (memory or I/O) the device has for this
       Base Address Register. If the device does not request addresses in this space, this
        property returns None (0).

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


        None                                                      0

        Memory                                                   1

           I/O                                                        2

    PXI/PCIPXI/PCI Settings:PCISettings:PCI Resources:BAR2Resources:BAR2
    AddressAddress BaseBase

        Returns the system-assigned base this device uses in the given space. If the device
       does not request addresses in this space, the value of this property is undefined.

      Remarks

       The following table lists the characteristics of this property.


10174   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10174 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10175 ordinal=10175 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

PXI/PCIPXI/PCI Settings:PCISettings:PCI Resources:BAR2Resources:BAR2
AddressAddress SizeSize

Returns the requested address size of this device in the given space. If the device does
not request addresses in this space, the value of this property is undefined.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

PXI/PCIPXI/PCI Settings:PCISettings:PCI Resources:BAR2Resources:BAR2
AddressAddress TypeType

Returns what type of address requirements (memory or I/O) the device has for this
Base Address Register. If the device does not request addresses in this space, this
property returns None (0).

Remarks

The following table lists the characteristics of this property.

                                                    © National Instruments 10175

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10175 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10176 ordinal=10176 -->
## Property and Method Reference

Property and Method Reference


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


        None                                                      0

        Memory                                                   1

           I/O                                                        2

    PXI/PCIPXI/PCI Settings:PCISettings:PCI Resources:BAR3Resources:BAR3
    AddressAddress BaseBase

        Returns the system-assigned base this device uses in the given space. If the device
       does not request addresses in this space, the value of this property is undefined.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    PXI/PCIPXI/PCI Settings:PCISettings:PCI Resources:BAR3Resources:BAR3
    AddressAddress SizeSize

        Returns the requested address size of this device in the given space. If the device does
        not request addresses in this space, the value of this property is undefined.

10176   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10176 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10177 ordinal=10177 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

PXI/PCIPXI/PCI Settings:PCISettings:PCI Resources:BAR3Resources:BAR3
AddressAddress TypeType

Returns what type of address requirements (memory or I/O) the device has for this
Base Address Register. If the device does not request addresses in this space, this
property returns None (0).

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


 None                                                      0

 Memory                                                   1

 I/O                                                        2


                                                    © National Instruments 10177

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10177 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10178 ordinal=10178 -->
## Property and Method Reference

Property and Method Reference

    PXI/PCIPXI/PCI Settings:PCISettings:PCI Resources:BAR4Resources:BAR4
    AddressAddress BaseBase

        Returns the system-assigned base this device uses in the given space. If the device
       does not request addresses in this space, the value of this property is undefined.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    PXI/PCIPXI/PCI Settings:PCISettings:PCI Resources:BAR4Resources:BAR4
    AddressAddress SizeSize

        Returns the requested address size of this device in the given space. If the device does
        not request addresses in this space, the value of this property is undefined.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


10178   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10178 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10179 ordinal=10179 -->
## Property and Method Reference

Property and Method Reference

PXI/PCIPXI/PCI Settings:PCISettings:PCI Resources:BAR4Resources:BAR4
AddressAddress TypeType

Returns what type of address requirements (memory or I/O) the device has for this
Base Address Register. If the device does not request addresses in this space, this
property returns None (0).

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


 None                                                      0

 Memory                                                   1

 I/O                                                        2

PXI/PCIPXI/PCI Settings:PCISettings:PCI Resources:BAR5Resources:BAR5
AddressAddress BaseBase

Returns the system-assigned base this device uses in the given space. If the device
does not request addresses in this space, the value of this property is undefined.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 10179

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10179 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10180 ordinal=10180 -->
## Property and Method Reference

Property and Method Reference


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    PXI/PCIPXI/PCI Settings:PCISettings:PCI Resources:BAR5Resources:BAR5
    AddressAddress SizeSize

        Returns the requested address size of this device in the given space. If the device does
        not request addresses in this space, the value of this property is undefined.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    PXI/PCIPXI/PCI Settings:PCISettings:PCI Resources:BAR5Resources:BAR5
    AddressAddress TypeType

        Returns what type of address requirements (memory or I/O) the device has for this
       Base Address Register. If the device does not request addresses in this space, this
        property returns None (0).

      Remarks

       The following table lists the characteristics of this property.

10180   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10180 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10181 ordinal=10181 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


 None                                                      0

 Memory                                                   1

 I/O                                                        2

PXI/PCIPXI/PCI Settings:PXISettings:PXI ChassisChassis NumberNumber

Returns the PXI chassis number of this device. A value of -1 means the chassis number
is unknown. Other valid values are 0 to 255.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

PXI/PCIPXI/PCI Settings:SlotSettings:Slot LocalLocal BusBus LeftLeft

Returns the slot number or special feature connected to the local bus left lines of this
device.

Remarks

The following table lists the characteristics of this property.

                                                    © National Instruments 10181

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10181 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10182 ordinal=10182 -->
## Property and Method Reference

Property and Method Reference


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    PXI/PCIPXI/PCI Settings:SlotSettings:Slot LocalLocal BusBus RightRight

        Returns the slot number or special feature connected to the local bus right lines of this
         device.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    PXI/PCIPXI/PCI Settings:SlotSettings:Slot PathPath

        Returns the slot path of this device.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

10182   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10182 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10183 ordinal=10183 -->
## Property and Method Reference

Property and Method Reference

PXI/PCIPXI/PCI Settings:StarSettings:Star TriggerTrigger BusBus NumberNumber

Returns the star trigger bus number of this device.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

PXI/PCIPXI/PCI Settings:StarSettings:Star TriggerTrigger LineLine

Returns the PXI_STAR line connected to this device.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

PXI/PCIPXI/PCI Settings:TriggerSettings:Trigger BusBus NumberNumber

Returns the trigger bus number of this device.


                                                    © National Instruments 10183

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10183 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10184 ordinal=10184 -->
## Property and Method Reference

Property and Method Reference

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

     RegisterRegister BasedBased Settings:DestinationSettings:Destination
    IncrementIncrement CountCount

         Specifies the number of elements by which to increment the destination address on
        block move operations. Valid values include 0 and 1. The default is 1. If this property is
         set to 0, VISA Move Out X operations always read from the same element, essentially
         treating the destination as a FIFO register.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

     RegisterRegister BasedBased Settings:SourceSettings:Source IncrementIncrement
    CountCount

         Specifies the number of elements by which to increment the source address on block

10184   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10184 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10185 ordinal=10185 -->
## Property and Method Reference

Property and Method Reference

move operations. Valid values include 0 and 1. The default is 1. If this property is set to
0, VISA Move In X operations always read from the same element, essentially treating
the source as a FIFO register.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

RegisterRegister BasedBased Settings:WindowSettings:Window AccessAccess

Returns whether the current session has a mapped window, and if so, whether the
window allows direct pointer dereferences.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


 Not Mapped                                                                1

 Use Peek/Poke Operations                                                    2

 Can Dereference Pointer                                                     3

 Pointer value is byte-swapped                                                4


                                                    © National Instruments 10185

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10185 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10186 ordinal=10186 -->
## Property and Method Reference

Property and Method Reference

     RegisterRegister BasedBased Settings:WindowSettings:Window BaseBase
    AddressAddress

        Returns the base interface address to which this window maps. If the Window Access
        property is Not Mapped, the value of this property is undefined.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

     RegisterRegister BasedBased Settings:WindowSettings:Window SizeSize

        Returns the size of the region mapped to this window. If the Window Access property is
       Not Mapped, the value of this property is undefined.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


10186   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10186 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10187 ordinal=10187 -->
## Property and Method Reference

Property and Method Reference

SerialSerial Settings:AllowSettings:Allow TransmitTransmit

Specifies whether to allow transmission. If FALSE, the serial port suspends
transmission as if an XOFF character has been received. If TRUE, it resumes
transmission as if an XON character has been received. If XON/XOFF flow control
(software handshaking) is not being used, FALSE is an invalid value. The default is
TRUE.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

SerialSerial Settings:BaudSettings:Baud RateRate

Specifies the baud rate of the given communications port. The rate is represented as
an unsigned 32-bit integer so that any baud rate can be used, but the communications
port usually requires a commonly used rate such as 300, 1200, 2400, or 9600 baud.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


                                                    © National Instruments 10187

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10187 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10188 ordinal=10188 -->
## Property and Method Reference

Property and Method Reference

     SerialSerial Settings:BreakSettings:Break LengthLength

         Specifies the duration (in milliseconds) of the break signal asserted when End Mode for
        Writes (ASRL End Out) is set to Break (3). Valid values include 1-500. The default is 250.
             If you want to control the assertion state and length of a break signal manually, use the
        VISA Serial Break VI instead.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

     SerialSerial Settings:DataSettings:Data BitsBits

         Specifies the number of data bits contained in each frame. Valid values include 5-8.
       The data bits for each frame are located in the low-order bits of every byte stored in
       memory.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes


10188   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10188 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10189 ordinal=10189 -->
## Property and Method Reference

Property and Method Reference

SerialSerial Settings:DiscardSettings:Discard NULNUL CharactersCharacters

Specifies whether to discard each data byte whose value is 0. If this property is TRUE,
read operations discard NUL characters. If this property is FALSE, read operations treat
NUL characters as normal data characters. For binary transfers, set this property to
FALSE. The default is FALSE.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

SerialSerial Settings:EndSettings:End ModeMode forfor ReadsReads

Specifies the method used to terminate read operations. Valid values include: (0)
None, (1) Last Bit, (2) TermChar. If the value is (2) TermChar, then the value of the
property Termination Character Enable (TermChar En) is ignored. The default is (2)
TermChar.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


                                                    © National Instruments 10189

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10189 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10190 ordinal=10190 -->
## Property and Method Reference

Property and Method Reference


        None                                                         0

          Last Bit                                                       1

         TermChar                                                     2

     SerialSerial Settings:EndSettings:End ModeMode forfor WritesWrites

         Specifies the method used to terminate write operations. Valid values include: (0)
       None, (1) Last Bit, (2) TermChar, (3) Break. The default is (0) None.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes


        None                                                         0

          Last Bit                                                       1

         TermChar                                                     2

         Break                                                        3

     SerialSerial Settings:ErrorSettings:Error ReplacementReplacement CharacterCharacter

         Specifies the character to use to replace incoming characters that arrive with errors
        (such as a parity error). The default is 0.

      Remarks

       The following table lists the characteristics of this property.

10190   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10190 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10191 ordinal=10191 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

SerialSerial Settings:FlowSettings:Flow ControlControl

Specifies the flow control method used for both transmitting and receiving data. Valid
values include: (0) Flow None, (1) Flow XON/XOFF, (2) Flow RTS/CTS, (3) Flow XON/
XOFF and RTS/CTS, (4) Flow DTR/DSR, (5) Flow XON/XOFF and DTR/DSR. Certain values
or combinations of values may not be supported by all serial ports and/or operating
systems.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


 None                                                                   0

 XON/XOFF                                                              1

 RTS/CTS                                                                2

 XON/XOFF & RTS/CTS                                                     3

 DTR/DSR                                                               4

 XON/XOFF & DTR/DSR                                                     5


                                                    © National Instruments 10191

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10191 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10192 ordinal=10192 -->
## Property and Method Reference

Property and Method Reference

     SerialSerial Settings:FlowSettings:Flow ControlControl XOFFXOFF CharacterCharacter

         Specifies the value of the XOFF character used for XON/XOFF flow control (both
         directions). If XON/XOFF flow control (software handshaking) is not being used, the
        value of this property is ignored. The default is 0x13 (Control-S).

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

     SerialSerial Settings:FlowSettings:Flow ControlControl XONXON CharacterCharacter

         Specifies the value of the XON character used for XON/XOFF flow control (both
         directions). If XON/XOFF flow control (software handshaking) is not being used, the
        value of this property is ignored. The default is 0x11 (Control-Q).

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes


10192   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10192 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10193 ordinal=10193 -->
## Property and Method Reference

Property and Method Reference

SerialSerial Settings:IsSettings:Is PortPort ConnectedConnected

Returns whether the port is properly connected to another port or device. This
property is valid only with serial drivers developed by National Instruments and
documented to support this feature with the corresponding National Instruments
hardware.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

SerialSerial Settings:ModemSettings:Modem LineLine Settings:BreakSettings:Break
StateState

Sets manual control of the serial port's break state. If asserted, this property suspends
character transmission and places the transmission line in a break state until this
property is unasserted. If you want VISA to send a break signal after each write
operation automatically, use the Break Length (Break Len) and End Mode for Writes
(ASRL End Out) properties instead. The default is Unasserted.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

                                                    © National Instruments 10193

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10193 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10194 ordinal=10194 -->
## Property and Method Reference

Property and Method Reference


           Available in Real-Time Operating System                                  Yes


        Unknown                                                                 -1

          Unasserted                                                   0

          Asserted                                                     1

     SerialSerial Settings:ModemSettings:Modem LineLine Settings:LineSettings:Line
    CTSCTS StateState

        Returns the current state of the Clear To Send (CTS) input signal.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


        Unknown                                                                 -1

          Unasserted                                                   0

          Asserted                                                     1

     SerialSerial Settings:ModemSettings:Modem LineLine Settings:LineSettings:Line
   DCDDCD StateState

         Specifies the current state of the Data Carrier Detect (DCD) input signal. This is often


10194   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10194 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10195 ordinal=10195 -->
## Property and Method Reference

Property and Method Reference

used by modems to indicate the detection of a carrier (modem) on the phone line. This
signal is also known as Receive Line Signal Detect (RLSD). This property is read only
except when the Wire Mode property is set to RS232/DCE, or RS232/Auto with the
hardware currently in the DCE state.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


 Unknown                                                                 -1

 Unasserted                                                   0

 Asserted                                                     1

SerialSerial Settings:ModemSettings:Modem LineLine Settings:LineSettings:Line
DSRDSR StateState

Returns the current state of the Data Set Ready (DSR) input signal.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


                                                    © National Instruments 10195

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10195 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10196 ordinal=10196 -->
## Property and Method Reference

Property and Method Reference


        Unknown                                                                 -1

          Unasserted                                                   0

          Asserted                                                     1

     SerialSerial Settings:ModemSettings:Modem LineLine Settings:LineSettings:Line
   DTRDTR StateState

         Asserts or unasserts the Data Terminal Ready (DTR) output signal manually.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes


        Unknown                                                                 -1

          Unasserted                                                   0

          Asserted                                                     1

     SerialSerial Settings:ModemSettings:Modem LineLine Settings:LineSettings:Line RIRI
     StateState

         Specifies the current state of the Ring Indicator (RI) input signal. The RI signal is often
       used by modems to indicate that the telephone line is ringing. This property is read
        only except when the Wire Mode property is set to RS232/DCE or to RS232/Auto with
        the hardware currently in the DCE state.

10196   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10196 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10197 ordinal=10197 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


 Unknown                                                                 -1

 Unasserted                                                   0

 Asserted                                                     1

SerialSerial Settings:ModemSettings:Modem LineLine Settings:LineSettings:Line RTSRTS
StateState

Asserts or unasserts the Request To Send (RTS) output signal manually. When the flow
control is set to hardware handshaking, it is invalid to change this property.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


 Unknown                                                                 -1

 Unasserted                                                   0

                                                    © National Instruments 10197

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10197 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10198 ordinal=10198 -->
## Property and Method Reference

Property and Method Reference


          Asserted                                                     1

     SerialSerial Settings:NumberSettings:Number ofof BytesBytes atat SerialSerial PortPort

        Returns the number of bytes currently available at the serial port used by this session.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

     SerialSerial Settings:ParitySettings:Parity

         Specifies the parity used with every frame that is transmitted or received. Valid values
         include: (0) Parity None, (1) Parity Odd, (2) Parity Even, (3) Parity Mark, (4) Parity Space.
       Mark means that the parity bit exists and is always 1. Space means that the parity bit
          exists and is always 0.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes


10198   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10198 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10199 ordinal=10199 -->
## Property and Method Reference

Property and Method Reference


 None                                                 0

 Odd                                                  1

 Even                                                 2

 Mark                                                 3

 Space                                                 4

SerialSerial Settings:StopSettings:Stop BitsBits

Specifies the number of stop bits used to indicate the end of a frame. Valid values
include: (10) Stop One, (15) Stop One-and-a-Half, (20) Stop Two.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


 1.0                                    10

 1.5                                    15

 2.0                                    20

SerialSerial Settings:WireSettings:Wire ModeMode

Specifies the current wire/transceiver mode. For RS485 hardware, this property is valid
only with the RS485 serial driver developed by National Instruments. For RS232
hardware, the values RS232/DCE and RS232/Auto are valid only with RS232 serial
drivers developed by National Instruments and documented to support this feature


                                                    © National Instruments 10199

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10199 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10200 ordinal=10200 -->
## Property and Method Reference

Property and Method Reference

        with the corresponding National Instruments hardware. When this feature is not
        supported, RS232/DTE is the only valid value.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes


        Unknown                                                                       -1

         RS485/Wire4                                                       0

         RS485/Wire2-EchoDTR                                               1

          RS485/Wire2-CtrlDTR                                                2

          RS485/Wire2-Auto                                                  3

         RS232/DTE                                                         128

         RS232/DCE                                                         129

         RS232/Auto                                                        130

    TCP/IPTCP/IP Settings:ComputerSettings:Computer HostnameHostname

        Returns the host name of the device. If no host name is available, this property returns
       an empty string.

      Remarks

       The following table lists the characteristics of this property.


          Data type


10200   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10200 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10201 ordinal=10201 -->
## Property and Method Reference

Property and Method Reference


 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

TCP/IPTCP/IP Settings:Dot-NotationSettings:Dot-Notation AddressAddress

Returns the TCPIP address of the device to which the session is connected. This string
is formatted in dot notation.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

TCP/IPTCP/IP Settings:HiSLIPSettings:HiSLIP Settings:EncryptionSettings:Encryption
EnabledEnabled

Controls and returns communication encryption.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes


                                                    © National Instruments 10201

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10201 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10202 ordinal=10202 -->
## Property and Method Reference

Property and Method Reference


           Available in Real-Time Operating System                                  Yes

    TCP/IPTCP/IP Settings:HiSLIPSettings:HiSLIP Settings:MaximumSettings:Maximum
    MessageMessage KBytesKBytes

         Specifies the HiSLIP maximum message size in kilobytes, where a kilobyte is 1024
         bytes.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

    TCP/IPTCP/IP Settings:HiSLIPSettings:HiSLIP Settings:OverlapSettings:Overlap
    EnabledEnabled

         Specifies whether the HiSLIP 'overlap' mode is enabled.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

10202   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10202 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10203 ordinal=10203 -->
## Property and Method Reference

Property and Method Reference

TCP/IPTCP/IP Settings:HiSLIPSettings:HiSLIP Settings:ProtocolSettings:Protocol
VersionVersion

Returns the negotiated HiSLIP protocol version.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

TCP/IPTCP/IP Settings:HiSLIPSettings:HiSLIP Settings:SASLSettings:SASL
MechanismMechanism

Returns a string that indicates the SASL mechanism used to authenticate the client.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


                                                    © National Instruments 10203

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10203 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10204 ordinal=10204 -->
## Property and Method Reference

Property and Method Reference

    TCP/IPTCP/IP Settings:IsSettings:Is HiSLIPHiSLIP

        Returns whether this session is using the HiSLIP protocol to communicate with the
         device.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    TCP/IPTCP/IP Settings:Keep-AliveSettings:Keep-Alive PacketsPackets

         Specifies whether to use keep-alive packets on TCP connections. Setting this property
         to TRUE requests that a TCP/IP provider enable the use of keep-alive packets on TCP
        connections. After the system detects a dropped connection, VISA returns a lost
        connection error code on subsequent I/O calls on the session. The time required for
        the system to detect the dropped connection depends on the system and is not
         settable. The default is FALSE.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes


10204   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10204 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10205 ordinal=10205 -->
## Property and Method Reference

Property and Method Reference

TCP/IPTCP/IP Settings:LANSettings:LAN DeviceDevice NameName

Returns the LAN device name used by the VXI-11 protocol (for example, inst0) during
connection.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

TCP/IPTCP/IP Settings:NoSettings:No PacketPacket DelayDelay

Specifies whether the Nagle algorithm is enabled. The Nagle algorithm is disabled
when this property is TRUE (and vice versa). The Nagle algorithm improves network
performance by buffering written data until a full-size packet can be sent. This
property is TRUE by default in VISA to verify that writes get flushed immediately.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


                                                    © National Instruments 10205

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10205 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10206 ordinal=10206 -->
## Property and Method Reference

Property and Method Reference

    TCP/IPTCP/IP Settings:ServerSettings:Server CertificateCertificate ExpirationExpiration
    DateDate

        Returns the expiration date of the server certificate. The form is ASN.1 UTCTime
       “YYMMDDhhmm[ss]Z.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    TCP/IPTCP/IP Settings:ServerSettings:Server CertificateCertificate IsIs
    PerpetualPerpetual

         Indicates the certificate does not expire.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


10206   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10206 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10207 ordinal=10207 -->
## Property and Method Reference

Property and Method Reference

TCP/IPTCP/IP Settings:ServerSettings:Server CertificateCertificate IssuerIssuer
NameName

Returns the name of the CA that signed the certificate in RFC4514 format.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

TCP/IPTCP/IP Settings:ServerSettings:Server CertificateCertificate SubjectSubject
NameName

Returns the serial number and subject field from the certificate om RFC4514 format.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


                                                    © National Instruments 10207

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10207 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10208 ordinal=10208 -->
## Property and Method Reference

Property and Method Reference

    TCP/IPTCP/IP Settings:TLSSettings:TLS CipherCipher SuiteSuite

        Returns a string that indicates the cipher suite used by TLS.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

   USBUSB Settings:MaximumSettings:Maximum InterruptInterrupt SizeSize

         Specifies the maximum size of data stored by any given USB interrupt. If a USB
         interrupt contains more data than this size, the data in excess of this size is lost. This
        property is read/write when the corresponding session is not enabled to receive USB
         interrupt events. When the session is enabled to receive USB interrupt events, this
        property is read only.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes


10208   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10208 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10209 ordinal=10209 -->
## Property and Method Reference

Property and Method Reference

USBUSB Settings:SerialSettings:Serial NumberNumber

Returns the USB serial number of this device.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

USBUSB Settings:USBSettings:USB InterfaceInterface NumberNumber

Returns the USB interface number used by the given session.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

USBUSB Settings:USBSettings:USB ProtocolProtocol

Returns the USB protocol used by the given session.


                                                    © National Instruments 10209

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10209 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10210 ordinal=10210 -->
## Property and Method Reference

Property and Method Reference

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    VXI/VMEVXI/VME Settings:DestinationSettings:Destination AccessAccess
     PrivilegePrivilege

         Specifies the address modifier to use in high-level access operations, such as VISA Out
       X and VISA Move Out X, when writing to the destination. The default is Data/Privileged
           (0).

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes


           Data/Privileged                                                           0

          Data/NonPrivileged                                                       1

          Program/Privileged                                                       2

          Program/NonPrivileged                                                    3

           Block/Privileged                                                          4


10210   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10210 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10211 ordinal=10211 -->
## Property and Method Reference

Property and Method Reference


 Block/NonPrivileged                                                      5

 D64/Privileged                                                           6

 D64/NonPrivileged                                                        7

VXI/VMEVXI/VME Settings:DestinationSettings:Destination ByteByte OrderOrder

Specifies the byte order to use in high-level access operations, such as VISA Out X and
VISA Move Out X, when writing to the destination. The default is Big Endian (0).

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


 Big Endian                                                        0

 Little Endian                                                      1

VXI/VMEVXI/VME Settings:FastSettings:Fast DataData Channel:ChannelChannel:Channel
ModeMode

Specifies whether FDC transfers use normal or streaming mode. The default is Normal.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 10211

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10211 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10212 ordinal=10212 -->
## Property and Method Reference

Property and Method Reference


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes


         Normal                                                   1

         Stream                                                   2

    VXI/VMEVXI/VME Settings:FastSettings:Fast DataData Channel:ChannelChannel:Channel
   NumberNumber

         Specifies which FDC channel to use to transfer data buffers. Valid values include 0-7.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

    VXI/VMEVXI/VME Settings:FastSettings:Fast DataData Channel:UseChannel:Use
    ChannelChannel PairsPairs

         Specifies whether transfers use a pair of FDC channels. If you do not set this property,
         transfers use only one FDC channel. The default is FALSE.


10212   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10212 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10213 ordinal=10213 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

VXI/VMEVXI/VME Settings:ImmediateSettings:Immediate ServantServant

Returns whether the VXI device is an immediate servant of the local controller.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VXI/VMEVXI/VME Settings:MainframeSettings:Mainframe LogicalLogical AddressAddress

Returns the lowest logical address in the mainframe in which the device resides.

Remarks

The following table lists the characteristics of this property.


 Data type


                                                    © National Instruments 10213

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10213 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10214 ordinal=10214 -->
## Property and Method Reference

Property and Method Reference


          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    VXI/VMEVXI/VME Settings:SourceSettings:Source AccessAccess PrivilegePrivilege

         Specifies the address modifier to use in high-level access operations, such as VISA In X
       and VISA Move In X, when reading from the source. The default is Data/Privileged (0).

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes


           Data/Privileged                                                           0

          Data/NonPrivileged                                                       1

          Program/Privileged                                                       2

          Program/NonPrivileged                                                    3

           Block/Privileged                                                          4

          Block/NonPrivileged                                                      5

          D64/Privileged                                                           6

          D64/NonPrivileged                                                        7

    VXI/VMEVXI/VME Settings:SourceSettings:Source ByteByte OrderOrder

         Specifies the byte order to use in high-level access operations, such as VISA In X and

10214   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10214 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10215 ordinal=10215 -->
## Property and Method Reference

Property and Method Reference

VISA Move In X, when reading from the source. The default is Big Endian (0).

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


 Big Endian                                                        0

 Little Endian                                                      1

VXI/VMEVXI/VME Settings:SupportedSettings:Supported VXIVXI TriggerTrigger LinesLines

Returns which VXI trigger lines this implementation supports. This property returns a
bit vector with bits 0-9 corresponding to TTL0 through ECL1.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


                                                    © National Instruments 10215

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10215 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10216 ordinal=10216 -->
## Property and Method Reference

Property and Method Reference

    VXI/VMEVXI/VME Settings:VXISettings:VXI CommanderCommander LogicalLogical
    AddressAddress

        Returns the logical address of the commander of the VXI device.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    VXI/VMEVXI/VME Settings:VXISettings:VXI DeviceDevice ClassClass

        Returns the class to which the VXI or VME device belongs.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


        Memory                                                     0

         Extended                                                    1

         Message                                                     2


10216   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10216 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10217 ordinal=10217 -->
## Property and Method Reference

Property and Method Reference


 Register                                                     3

 Other                                                       4

VXI/VMEVXI/VME Settings:VXISettings:VXI LogicalLogical AddressAddress

Returns the logical address of the VXI device.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VXI/VMEVXI/VME Settings:VXISettings:VXI MemoryMemory AddressAddress SpaceSpace

Returns the VXI address space used by the device.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


 VXI/VME A16                                                      1

 VXI/VME A24                                                      2

                                                    © National Instruments 10217

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10217 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10218 ordinal=10218 -->
## Property and Method Reference

Property and Method Reference


         VXI/VME A32                                                      3

         VXI/VME A64                                                      4

    VXI/VMEVXI/VME Settings:VXISettings:VXI MemoryMemory BaseBase AddressAddress

        Returns the base address of the device in VXI memory space.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    VXI/VMEVXI/VME Settings:VXISettings:VXI MemoryMemory SizeSize

        Returns the size of memory requested by the device in VXI memory space.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


10218   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10218 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10219 ordinal=10219 -->
## Property and Method Reference

Property and Method Reference

VXI/VMEVXI/VME Settings:VXISettings:VXI TriggerTrigger DirectionsDirections

Specifies the directions of the mapped TTL triggers lines. This is a bit vector where bits
0-7 represent TTL triggers 0-7 respectively. A bit value of 0 means the corresponding
line is routed out of the frame, and a value of 1 means the line is routed into the frame.
Lines must be enabled using VXI/VME Settings:VXI Trigger Lines Enable.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

VXI/VMEVXI/VME Settings:VXISettings:VXI TriggerTrigger LinesLines EnableEnable

Specifies which VXI TLL triggers have mappings. This is a bit vector where bits 0-7
represent TTL triggers 0-7 respectively. A bit value of 0 means the corresponding
trigger line is unmapped, and 1 means a mapping exists. Use VXI/VME Settings:VXI
Trigger Directions to set an enabled line's direction.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


                                                    © National Instruments 10219

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10219 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10220 ordinal=10220 -->
## Property and Method Reference

Property and Method Reference

    VXI/VMEVXI/VME Settings:WindowSettings:Window AccessAccess PrivilegePrivilege

         Specifies the address modifier to use in low-level access operations, such as VISA Map
        Address, VISA Peek X, and VISA Poke X, when accessing the mapped window. The
         default is Data/Privileged (0).

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes


           Data/Privileged                                                           0

          Data/NonPrivileged                                                       1

          Program/Privileged                                                       2

          Program/NonPrivileged                                                    3

           Block/Privileged                                                          4

          Block/NonPrivileged                                                      5

          D64/Privileged                                                           6

          D64/NonPrivileged                                                        7

    VXI/VMEVXI/VME Settings:WindowSettings:Window ByteByte OrderOrder

         Specifies the byte order to use in low-level access operations, such as VISA Map
        Address, VISA Peek X, and VISA Poke X, when accessing the mapped window. The
         default is Big Endian (0).


10220   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10220 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10221 ordinal=10221 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


 Big Endian                                                        0

 Little Endian                                                      1

VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
IdentificationIdentification

Returns a value that corresponds to the VXI manufacturer ID of the manufacturer that
created the VISA implementation.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


                                                    © National Instruments 10221

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10221 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10222 ordinal=10222 -->
## Property and Method Reference

Property and Method Reference

    VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
   NameName

        Returns the name of the manufacturer that created the implementation. This is not
         related to the device manufacturer attributes. Note: Use the value of this property for
         display purposes only and not for programmatic decisions. The value can change
       between VISA implementations and/or revisions.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    VersionVersion Information:VersionInformation:Version ofof
    ImplementationImplementation

        Returns the version of a given implementation. This value is defined by the individual
        manufacturer and increments with each new revision. The format of the value has the
       upper 12 bits as the major number of the version, the next lower 12 bits as the minor
       number of the version, and the lowest 8 bits as the sub-minor number of the version.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only


10222   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10222 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10223 ordinal=10223 -->
## Property and Method Reference

Property and Method Reference


 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VersionVersion Information:VersionInformation:Version ofof SpecificationSpecification

Returns the value that uniquely identifies the version of the VISA specification to which
the implementation complies. The format of the value has the upper 12 bits as the
major number of the version, the next lower 12 bits as the minor number of the
version, and the lowest 8 bits as the sub-minor number of the version.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

PXIPXI BackplaneBackplane PropertiesProperties


 Property              Description

                      Returns the name of the manufacturer that created the device. Note: Use
 General
                      the value of this property for display purposes only and not for
 Settings:Manufacturer
                     programmatic decisions. The value can change between VISA
 Name
                      implementations and/or revisions.

 General                Specifies the maximum number of events that can be queued at any time
 Settings:Maximum    on the given session. This property is read/write until the first time you call
 Queue Length         VISA Enable Event on a session. Thereafter, it is read only. The default is 50.

                      Returns the model name of the device. Note: Use the value of this property
 General
                          for display purposes only and not for programmatic decisions. The value
 Settings:Model Name
                     can change between VISA implementations and/or revisions.

 General              Returns the resource class of the resource string used to open the given

                                                    © National Instruments 10223

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10223 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10224 ordinal=10224 -->
## Property and Method Reference

Property and Method Reference


          Property              Description

                                   session. For example, if the resource string for a given session is COM1 or           Settings:Resource                                ASRL1::INSTR, this property returns INSTR, regardless of the class of the I/O           Class                                    control.

          General              Returns the current locking state of the resource associated with the given
           Settings:Resource      session. The resource can be unlocked, locked with an exclusive lock, or
         Lock State            locked with a shared lock. The default is Unlocked.

          General
           Settings:Resource     Returns the unique identifier for a resource.
        Name

          General                Specifies the minimum timeout value, in milliseconds, to use when
          Settings:Timeout      accessing the device. Note that the actual timeout that VISA returns may be
          Value                 higher than the one requested. The default is 2000.

          General                Specifies which trigger mechanism to use. In VXI systems, for example, you
           Settings:Trigger       can choose between software triggers and hardware triggers on a specific
            Identifier               trigger line. The default is Software.

                                   Specifies a data value for the private use of an application. The VISA
          General Settings:User  implementation stores this value in a per-session location, so that user data
          Data               on other sessions does not affect the user data on this session. VISA does
                               not use this property for any purpose.

                                   Specifies human-readable text that describes the given interface. Note: Use           Interface                                the value of this property for display purposes only and not for
           Information:Interface                             programmatic decisions. The value can change between VISA           Description                               implementations and/or revisions.

           Interface
           Information:Interface  Returns the board number for the given interface.
        Number

           Interface
           Information:Interface  Specifies the interface type of the given session.
         Type

                                   Specifies the segment to use to qualify the trigger destination in VISA Map
                                      Trigger. Note: Some PXI chassis, typically those with more than eight slots,
                             have multiple trigger buses (also called segments). The PXI Backplane
           PXI/PCI
                                resource uses the VISA Map Trigger to map a trigger between two trigger
           Settings:Destination
                                 buses. One trigger bus, specified by Source Trigger Bus Number, is the
           Trigger Bus Number
                                source or writer for this trigger line. The other trigger bus, specified by
                                 Destination Trigger Bus Number, is a reader. You can have multiple readers,
                               but only one writer for a given trigger line. For example, if you want to have

10224   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10224 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10225 ordinal=10225 -->
## Property and Method Reference

Property and Method Reference


Property              Description

                         triggers mapped from trigger bus 1 to trigger bus 2 and then from trigger
                    bus 2 to trigger bus 3. In this case trigger bus 1 is the writer for this line,
                        writing to both trigger bus 2 and trigger bus 3. Therefore, you should
                    perform VISA Map Trigger from 1 to 2 and from 1 to 3. Mapping from 1 to 2
                   and then 2 to 3 would not be allowed because it would require 2 to be a
                        writer (as well as 1). Note also that mapping from one line in the source
                         trigger bus to a different line in the destination trigger bus is dependent on
                    hardware capabilities and a specific software implementation. This
                     behavior might not be supported. A value of -1 means this feature is not
                    enabled or not applicable. On a single-segment chassis (eight slots or less),
                          this feature is not applicable. For a multi-segment chassis (more than eight
                            slots), the valid values are 1 to the number of chassis segments. You can
                     determine the number of segments from MAX (in the trigger reservation
                        panel), from the chassis documentation, and by looking at the dividing
                         lines on the physical front panel of the chassis itself.

PXI/PCI Settings:PXI    Returns the PXI chassis number of this resource. A value of -1 means the
Chassis Number       chassis number is unknown. Other valid values are 0 to 255.

                        Specifies the segment to use to qualify the trigger source in VISA Map
                          Trigger. Note: Some PXI chassis, typically those with more than eight slots,
                    have multiple trigger buses (also called segments). The PXI Backplane
                      resource uses the VISA Map Trigger to map a trigger between two trigger
                      buses. One trigger bus, specified by Source Trigger Bus Number, is the
                     source or writer for this trigger line. The other trigger bus, specified by
                       Destination Trigger Bus Number, is a reader. You can have multiple readers,
                     but only one writer for a given trigger line. For example, if you want to have
                         triggers mapped from trigger bus 1 to trigger bus 2 and then from trigger
                    bus 2 to trigger bus 3. In this case trigger bus 1 is the writer for this line,
PXI/PCI                writing to both trigger bus 2 and trigger bus 3. Therefore, you should
Settings:Source       perform VISA Map Trigger from 1 to 2 and from 1 to 3. Mapping from 1 to 2
Trigger Bus Number   and then 2 to 3 would not be allowed because it would require 2 to be a
                        writer (as well as 1). Note also that mapping from one line in the source
                         trigger bus to a different line in the destination trigger bus is dependent on
                    hardware capabilities and a specific software implementation. This
                     behavior might not be supported. A value of -1 means this feature is not
                    enabled or not applicable. On a single-segment chassis (eight slots or less),
                          this feature is not applicable. For a multi-segment chassis (more than eight
                            slots), the valid values are 1 to the number of chassis segments. You can
                     determine the number of segments from MAX (in the trigger reservation
                        panel), from the chassis documentation, and by looking at the dividing
                         lines on the physical front panel of the chassis itself. The default is -1.


                                                    © National Instruments 10225

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10225 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10226 ordinal=10226 -->
## Property and Method Reference

Property and Method Reference


          Property              Description

           PXI/PCI
           Settings:Trigger Bus    Specifies the trigger bus number of this device.
        Number

           Version
          Information:Resource  Returns a value that corresponds to the VXI manufacturer ID of the
          Manufacturer         manufacturer that created the VISA implementation.
            Identification

                                Returns the name of the manufacturer that created the implementation.
           Version                This is not related to the device manufacturer attributes. Note: Use the
          Information:Resource  value of this property for display purposes only and not for programmatic
          Manufacturer Name    decisions. The value can change between VISA implementations and/or
                                     revisions.

                                Returns the version of a given implementation. This value is defined by the
           Version                individual manufacturer and increments with each new revision. The
           Information:Version   format of the value has the upper 12 bits as the major number of the
           of Implementation     version, the next lower 12 bits as the minor number of the version, and the
                                lowest 8 bits as the sub-minor number of the version.

                                Returns the value that uniquely identifies the version of the VISA
           Version                 specification to which the implementation complies. The format of the
           Information:Version    value has the upper 12 bits as the major number of the version, the next
           of Specification       lower 12 bits as the minor number of the version, and the lowest 8 bits as
                                the sub-minor number of the version.

    GeneralGeneral Settings:ManufacturerSettings:Manufacturer NameName

        Returns the name of the manufacturer that created the device. Note: Use the value of
          this property for display purposes only and not for programmatic decisions. The value
       can change between VISA implementations and/or revisions.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only


10226   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10226 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10227 ordinal=10227 -->
## Property and Method Reference

Property and Method Reference


 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

GeneralGeneral Settings:MaximumSettings:Maximum QueueQueue LengthLength

Specifies the maximum number of events that can be queued at any time on the given
session. This property is read/write until the first time you call VISA Enable Event on a
session. Thereafter, it is read only. The default is 50.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

GeneralGeneral Settings:ModelSettings:Model NameName

Returns the model name of the device. Note: Use the value of this property for display
purposes only and not for programmatic decisions. The value can change between
VISA implementations and/or revisions.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

                                                    © National Instruments 10227

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10227 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10228 ordinal=10228 -->
## Property and Method Reference

Property and Method Reference

    GeneralGeneral Settings:ResourceSettings:Resource ClassClass

        Returns the resource class of the resource string used to open the given session. For
        example, if the resource string for a given session is COM1 or ASRL1::INSTR, this
        property returns INSTR, regardless of the class of the I/O control.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    GeneralGeneral Settings:ResourceSettings:Resource LockLock StateState

        Returns the current locking state of the resource associated with the given session.
       The resource can be unlocked, locked with an exclusive lock, or locked with a shared
         lock. The default is Unlocked.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


         Unlocked                                                     0


10228   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10228 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10229 ordinal=10229 -->
## Property and Method Reference

Property and Method Reference


 Exclusive                                                     1

 Shared                                                       2

GeneralGeneral Settings:ResourceSettings:Resource NameName

Returns the unique identifier for a resource.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

GeneralGeneral Settings:TimeoutSettings:Timeout ValueValue

Specifies the minimum timeout value, in milliseconds, to use when accessing the
device. Note that the actual timeout that VISA returns may be higher than the one
requested. The default is 2000.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


                                                    © National Instruments 10229

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10229 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10230 ordinal=10230 -->
## Property and Method Reference

Property and Method Reference

    GeneralGeneral Settings:TriggerSettings:Trigger IdentifierIdentifier

         Specifies which trigger mechanism to use. In VXI systems, for example, you can choose
       between software triggers and hardware triggers on a specific trigger line. The default
           is Software.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes


          Software                                                             -1

         TTL0                                                     0

         TTL1                                                     1

         TTL2                                                     2

         TTL3                                                     3

         TTL4                                                     4

         TTL5                                                     5

         TTL6                                                     6

         TTL7                                                     7

         ECL0                                                     8

         ECL1                                                     9

    GeneralGeneral Settings:UserSettings:User DataData

         Specifies a data value for the private use of an application. The VISA implementation

10230   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10230 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10231 ordinal=10231 -->
## Property and Method Reference

Property and Method Reference

stores this value in a per-session location, so that user data on other sessions does not
affect the user data on this session. VISA does not use this property for any purpose.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

InterfaceInterface Information:InterfaceInformation:Interface DescriptionDescription

Specifies human-readable text that describes the given interface. Note: Use the value
of this property for display purposes only and not for programmatic decisions. The
value can change between VISA implementations and/or revisions.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

InterfaceInterface Information:InterfaceInformation:Interface NumberNumber

Returns the board number for the given interface.


                                                    © National Instruments 10231

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10231 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10232 ordinal=10232 -->
## Property and Method Reference

Property and Method Reference

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

     InterfaceInterface Information:InterfaceInformation:Interface TypeType

         Specifies the interface type of the given session.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


         GPIB                                                       1

          VXI                                                         2

          GPIB-VXI                                                    3

           Serial                                                       4

          PXI                                                         5

         TCPIP                                                      6

        USB                                                        7

          FireWire                                                    9


10232   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10232 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10233 ordinal=10233 -->
## Property and Method Reference

Property and Method Reference

PXI/PCIPXI/PCI Settings:DestinationSettings:Destination TriggerTrigger BusBus
NumberNumber

Specifies the segment to use to qualify the trigger destination in VISA Map Trigger.
Note: Some PXI chassis, typically those with more than eight slots, have multiple
trigger buses (also called segments). The PXI Backplane resource uses the VISA Map
Trigger to map a trigger between two trigger buses. One trigger bus, specified by
Source Trigger Bus Number, is the source or writer for this trigger line. The other
trigger bus, specified by Destination Trigger Bus Number, is a reader. You can have
multiple readers, but only one writer for a given trigger line. For example, if you want
to have triggers mapped from trigger bus 1 to trigger bus 2 and then from trigger bus 2
to trigger bus 3. In this case trigger bus 1 is the writer for this line, writing to both
trigger bus 2 and trigger bus 3. Therefore, you should perform VISA Map Trigger from 1
to 2 and from 1 to 3. Mapping from 1 to 2 and then 2 to 3 would not be allowed
because it would require 2 to be a writer (as well as 1). Note also that mapping from
one line in the source trigger bus to a different line in the destination trigger bus is
dependent on hardware capabilities and a specific software implementation. This
behavior might not be supported. A value of -1 means this feature is not enabled or not
applicable. On a single-segment chassis (eight slots or less), this feature is not
applicable. For a multi-segment chassis (more than eight slots), the valid values are 1
to the number of chassis segments. You can determine the number of segments from
MAX (in the trigger reservation panel), from the chassis documentation, and by looking
at the dividing lines on the physical front panel of the chassis itself.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


                                                    © National Instruments 10233

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10233 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10234 ordinal=10234 -->
## Property and Method Reference

Property and Method Reference

    PXI/PCIPXI/PCI Settings:PXISettings:PXI ChassisChassis NumberNumber

        Returns the PXI chassis number of this resource. A value of -1 means the chassis
       number is unknown. Other valid values are 0 to 255.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    PXI/PCIPXI/PCI Settings:SourceSettings:Source TriggerTrigger BusBus NumberNumber

         Specifies the segment to use to qualify the trigger source in VISA Map Trigger. Note:
      Some PXI chassis, typically those with more than eight slots, have multiple trigger
        buses (also called segments). The PXI Backplane resource uses the VISA Map Trigger to
      map a trigger between two trigger buses. One trigger bus, specified by Source Trigger
       Bus Number, is the source or writer for this trigger line. The other trigger bus, specified
       by Destination Trigger Bus Number, is a reader. You can have multiple readers, but only
       one writer for a given trigger line. For example, if you want to have triggers mapped
       from trigger bus 1 to trigger bus 2 and then from trigger bus 2 to trigger bus 3. In this
        case trigger bus 1 is the writer for this line, writing to both trigger bus 2 and trigger bus
          3. Therefore, you should perform VISA Map Trigger from 1 to 2 and from 1 to 3.
       Mapping from 1 to 2 and then 2 to 3 would not be allowed because it would require 2
         to be a writer (as well as 1). Note also that mapping from one line in the source trigger
       bus to a different line in the destination trigger bus is dependent on hardware
         capabilities and a specific software implementation. This behavior might not be
        supported. A value of -1 means this feature is not enabled or not applicable. On a
        single-segment chassis (eight slots or less), this feature is not applicable. For a multi-
       segment chassis (more than eight slots), the valid values are 1 to the number of chassis
        segments. You can determine the number of segments from MAX (in the trigger

10234   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10234 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10235 ordinal=10235 -->
## Property and Method Reference

Property and Method Reference

reservation panel), from the chassis documentation, and by looking at the dividing
lines on the physical front panel of the chassis itself. The default is -1.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

PXI/PCIPXI/PCI Settings:TriggerSettings:Trigger BusBus NumberNumber

Specifies the trigger bus number of this device.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
IdentificationIdentification

Returns a value that corresponds to the VXI manufacturer ID of the manufacturer that
created the VISA implementation.


                                                    © National Instruments 10235

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10235 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10236 ordinal=10236 -->
## Property and Method Reference

Property and Method Reference

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
   NameName

        Returns the name of the manufacturer that created the implementation. This is not
         related to the device manufacturer attributes. Note: Use the value of this property for
         display purposes only and not for programmatic decisions. The value can change
       between VISA implementations and/or revisions.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    VersionVersion Information:VersionInformation:Version ofof
    ImplementationImplementation

        Returns the version of a given implementation. This value is defined by the individual

10236   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10236 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10237 ordinal=10237 -->
## Property and Method Reference

Property and Method Reference

manufacturer and increments with each new revision. The format of the value has the
upper 12 bits as the major number of the version, the next lower 12 bits as the minor
number of the version, and the lowest 8 bits as the sub-minor number of the version.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VersionVersion Information:VersionInformation:Version ofof SpecificationSpecification

Returns the value that uniquely identifies the version of the VISA specification to which
the implementation complies. The format of the value has the upper 12 bits as the
major number of the version, the next lower 12 bits as the minor number of the
version, and the lowest 8 bits as the sub-minor number of the version.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

PXIPXI InstrInstr PropertiesProperties


                                                    © National Instruments 10237

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10237 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10238 ordinal=10238 -->
## Property and Method Reference

Property and Method Reference


          Property              Description

                                   Specifies whether I/O accesses should attempt to use DMA (TRUE) or          General                           Programmed I/O (FALSE). In some implementations, this property may           Settings:Allow DMA                             have global effects even though it is documented as a local property. This           Transfers                                behavior affects performance and not functionality.

                                Returns the ID of the manufacturer that created the device. For VXI
          General                resources, this refers to the VXI Manufacturer ID. For PXI/PCI resources, this
           Settings:Manufacturer  refers to the Subsystem Vendor ID (SVID) if it is nonzero; otherwise, this
            Identification           refers to the Vendor ID (VID). For USB resources, this refers to the Vendor ID
                                       (VID).

                                Returns the name of the manufacturer that created the device. Note: Use          General                                the value of this property for display purposes only and not for           Settings:Manufacturer
                             programmatic decisions. The value can change between VISA        Name                               implementations and/or revisions.

          General                Specifies the maximum number of events that can be queued at any time
          Settings:Maximum    on the given session. This property is read/write until the first time you call
        Queue Length         VISA Enable Event on a session. Thereafter, it is read only. The default is 50.

                                Returns the device model code assigned by the manufacturer. For VXI
                                  resources, this refers to the VXI Model Code. For PXI/PCI resources, if the          General                             Subsystem Vendor ID is nonzero, this refers to the Subsystem ID (SSID);
          Settings:Model Code                                 otherwise, this refers to the Device ID (DID). For USB resources, this refers to
                                the Product ID (PID).

                                Returns the model name of the device. Note: Use the value of this property          General                                     for display purposes only and not for programmatic decisions. The value
          Settings:Model Name                             can change between VISA implementations and/or revisions.

                                Returns the resource class of the resource string used to open the given
          General
                                   session. For example, if the resource string for a given session is COM1 or
           Settings:Resource
                                ASRL1::INSTR, this property returns INSTR, regardless of the class of the I/O
           Class
                                    control.

          General              Returns the current locking state of the resource associated with the given
           Settings:Resource      session. The resource can be unlocked, locked with an exclusive lock, or
         Lock State            locked with a shared lock. The default is Unlocked.

          General
           Settings:Resource     Returns the unique identifier for a resource.
        Name

                                Returns the physical slot location of the device. If the slot is unknown, the
          General Settings:Slot
                                value returned is -1.


10238   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10238 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10239 ordinal=10239 -->
## Property and Method Reference

Property and Method Reference


Property              Description

General                Specifies the minimum timeout value, in milliseconds, to use when
Settings:Timeout      accessing the device. Note that the actual timeout that VISA returns may be
Value                 higher than the one requested. The default is 2000.

General                Specifies which trigger mechanism to use. In VXI systems, for example, you
Settings:Trigger       can choose between software triggers and hardware triggers on a specific
Identifier               trigger line. The default is Software.

                        Specifies a data value for the private use of an application. The VISA
General Settings:User  implementation stores this value in a per-session location, so that user data
Data               on other sessions does not affect the user data on this session. VISA does
                     not use this property for any purpose.

                        Specifies human-readable text that describes the given interface. Note: UseInterface
                      the value of this property for display purposes only and not forInformation:Interface                    programmatic decisions. The value can change between VISADescription
                     implementations and/or revisions.

Interface
Information:Interface  Returns the board number for the given interface.
Number

Interface
Information:Interface  Specifies the interface type of the given session.
Type

PXI/PCI
                     Returns the PCI Express link width negotiated between the PCI Express hostSettings:Express                        controller and the device. A value of -1 indicates that the device is not a PXI/Settings:Actual Link
                     PCI Express device. Common values include 1, 2, 4, 8, and 16.Width

PXI/PCI
Settings:Express       Returns the differential star bus number of this device. A value of -1 means
Settings:D-Star Bus     that the chassis is unidentified or does not have a timing slot.
Number

PXI/PCI
                     Returns the set of differential star lines connected to this device. A value of
Settings:Express
                         -1 means that the chassis is unidentified or does not have a timing slot.
Settings:D-Star Set

PXI/PCI
Settings:Express
                     Returns whether the device is PXI/PCI or PXI/PCI Express.
Settings:Is PCI
Express

PXI/PCI               Returns the maximum PCI Express link width of the device. A value of -1


                                                    © National Instruments 10239

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10239 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10240 ordinal=10240 -->
## Property and Method Reference

Property and Method Reference


          Property              Description

           Settings:Express                                   indicates that the device is not a PXI/PCI Express device. Common values          Settings:Maximum                                 include 1, 2, 4, 8, and 16.          Link Width

           PXI/PCI                                Returns the PCI Express link width of the PXI Express peripheral slot in
           Settings:Express                             which the device resides. A value of -1 indicates that the device is not a PXI           Settings:Slot Link                                Express device. Common values include 1, 4, and 8.         Width

           PXI/PCI Settings:PCI                                Returns the PCI bus number of the PXI/PCI resource.
         Bus Number

           PXI/PCI Settings:PCI                                Returns the PCI device number of the PXI/PCI resource.          Device Number

                                Returns the PCI function number of the PXI/PCI resource. For most devices,
           PXI/PCI Settings:PCI    the function number is 0, but a multifunction device may have a function
          Function Number     number up to 7. The meaning of a function number other than 0 is device-
                                      specific.

           PXI/PCI Settings:PCI    Returns the system-assigned base this device uses in the given space. If the
          Resources:BAR0       device does not request addresses in this space, the value of this property is
          Address Base          undefined.

           PXI/PCI Settings:PCI    Returns the requested address size of this device in the given space. If the
          Resources:BAR0       device does not request addresses in this space, the value of this property is
          Address Size          undefined.

           PXI/PCI Settings:PCI    Returns what type of address requirements (memory or I/O) the device has
          Resources:BAR0        for this Base Address Register. If the device does not request addresses in
          Address Type           this space, this property returns None (0).

           PXI/PCI Settings:PCI    Returns the system-assigned base this device uses in the given space. If the
          Resources:BAR1       device does not request addresses in this space, the value of this property is
          Address Base          undefined.

           PXI/PCI Settings:PCI    Returns the requested address size of this device in the given space. If the
          Resources:BAR1       device does not request addresses in this space, the value of this property is
          Address Size          undefined.

           PXI/PCI Settings:PCI    Returns what type of address requirements (memory or I/O) the device has
          Resources:BAR1        for this Base Address Register. If the device does not request addresses in
          Address Type           this space, this property returns None (0).

           PXI/PCI Settings:PCI    Returns the system-assigned base this device uses in the given space. If the
          Resources:BAR2       device does not request addresses in this space, the value of this property is


10240   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10240 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10241 ordinal=10241 -->
## Property and Method Reference

Property and Method Reference


Property              Description

Address Base          undefined.

PXI/PCI Settings:PCI    Returns the requested address size of this device in the given space. If the
Resources:BAR2       device does not request addresses in this space, the value of this property is
Address Size          undefined.

PXI/PCI Settings:PCI    Returns what type of address requirements (memory or I/O) the device has
Resources:BAR2        for this Base Address Register. If the device does not request addresses in
Address Type           this space, this property returns None (0).

PXI/PCI Settings:PCI    Returns the system-assigned base this device uses in the given space. If the
Resources:BAR3       device does not request addresses in this space, the value of this property is
Address Base          undefined.

PXI/PCI Settings:PCI    Returns the requested address size of this device in the given space. If the
Resources:BAR3       device does not request addresses in this space, the value of this property is
Address Size          undefined.

PXI/PCI Settings:PCI    Returns what type of address requirements (memory or I/O) the device has
Resources:BAR3        for this Base Address Register. If the device does not request addresses in
Address Type           this space, this property returns None (0).

PXI/PCI Settings:PCI    Returns the system-assigned base this device uses in the given space. If the
Resources:BAR4       device does not request addresses in this space, the value of this property is
Address Base          undefined.

PXI/PCI Settings:PCI    Returns the requested address size of this device in the given space. If the
Resources:BAR4       device does not request addresses in this space, the value of this property is
Address Size          undefined.

PXI/PCI Settings:PCI    Returns what type of address requirements (memory or I/O) the device has
Resources:BAR4        for this Base Address Register. If the device does not request addresses in
Address Type           this space, this property returns None (0).

PXI/PCI Settings:PCI    Returns the system-assigned base this device uses in the given space. If the
Resources:BAR5       device does not request addresses in this space, the value of this property is
Address Base          undefined.

PXI/PCI Settings:PCI    Returns the requested address size of this device in the given space. If the
Resources:BAR5       device does not request addresses in this space, the value of this property is
Address Size          undefined.

PXI/PCI Settings:PCI    Returns what type of address requirements (memory or I/O) the device has
Resources:BAR5        for this Base Address Register. If the device does not request addresses in
Address Type           this space, this property returns None (0).

PXI/PCI Settings:PXI    Returns the PXI chassis number of this device. A value of -1 means the

                                                    © National Instruments 10241

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10241 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10242 ordinal=10242 -->
## Property and Method Reference

Property and Method Reference


          Property              Description

          Chassis Number       chassis number is unknown. Other valid values are 0 to 255.

           PXI/PCI Settings:Slot   Returns the slot number or special feature connected to the local bus left
          Local Bus Left           lines of this device.

           PXI/PCI Settings:Slot   Returns the slot number or special feature connected to the local bus right
          Local Bus Right         lines of this device.

           PXI/PCI Settings:Slot                                Returns the slot path of this device.          Path

           PXI/PCI Settings:Star                                Returns the star trigger bus number of this device.
           Trigger Bus Number

           PXI/PCI Settings:Star                                Returns the PXI_STAR line connected to this device.           Trigger Line

           PXI/PCI
           Settings:Trigger Bus    Returns the trigger bus number of this device.
        Number

                                   Specifies the number of elements by which to increment the destination           Register Based
                               address on block move operations. Valid values include 0 and 1. The default           Settings:Destination                                            is 1. If this property is set to 0, VISA Move Out X operations always read from
          Increment Count                                the same element, essentially treating the destination as a FIFO register.

                                   Specifies the number of elements by which to increment the source
           Register Based                               address on block move operations. Valid values include 0 and 1. The default           Settings:Source                                            is 1. If this property is set to 0, VISA Move In X operations always read from
          Increment Count                                the same element, essentially treating the source as a FIFO register.

           Register Based
                                Returns whether the current session has a mapped window, and if so,          Settings:Window                             whether the window allows direct pointer dereferences.
          Access

           Register Based        Returns the base interface address to which this window maps. If the
          Settings:Window Base Window Access property is Not Mapped, the value of this property is
          Address               undefined.

           Register Based        Returns the size of the region mapped to this window. If the Window Access
          Settings:Window Size  property is Not Mapped, the value of this property is undefined.

           Version
          Information:Resource  Returns a value that corresponds to the VXI manufacturer ID of the
          Manufacturer         manufacturer that created the VISA implementation.
            Identification


10242   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10242 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10243 ordinal=10243 -->
## Property and Method Reference

Property and Method Reference


 Property              Description

                      Returns the name of the manufacturer that created the implementation.
 Version                This is not related to the device manufacturer attributes. Note: Use the
 Information:Resource  value of this property for display purposes only and not for programmatic
 Manufacturer Name    decisions. The value can change between VISA implementations and/or
                          revisions.

                      Returns the version of a given implementation. This value is defined by the
 Version                individual manufacturer and increments with each new revision. The
 Information:Version   format of the value has the upper 12 bits as the major number of the
 of Implementation     version, the next lower 12 bits as the minor number of the version, and the
                       lowest 8 bits as the sub-minor number of the version.

                      Returns the value that uniquely identifies the version of the VISA
 Version                 specification to which the implementation complies. The format of the
 Information:Version    value has the upper 12 bits as the major number of the version, the next
 of Specification       lower 12 bits as the minor number of the version, and the lowest 8 bits as
                      the sub-minor number of the version.

GeneralGeneral Settings:AllowSettings:Allow DMADMA TransfersTransfers

Specifies whether I/O accesses should attempt to use DMA (TRUE) or Programmed I/O
(FALSE). In some implementations, this property may have global effects even though
it is documented as a local property. This behavior affects performance and not
functionality.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


                                                    © National Instruments 10243

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10243 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10244 ordinal=10244 -->
## Property and Method Reference

Property and Method Reference

    GeneralGeneral Settings:ManufacturerSettings:Manufacturer IdentificationIdentification

        Returns the ID of the manufacturer that created the device. For VXI resources, this
         refers to the VXI Manufacturer ID. For PXI/PCI resources, this refers to the Subsystem
       Vendor ID (SVID) if it is nonzero; otherwise, this refers to the Vendor ID (VID). For USB
         resources, this refers to the Vendor ID (VID).

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    GeneralGeneral Settings:ManufacturerSettings:Manufacturer NameName

        Returns the name of the manufacturer that created the device. Note: Use the value of
          this property for display purposes only and not for programmatic decisions. The value
       can change between VISA implementations and/or revisions.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


10244   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10244 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10245 ordinal=10245 -->
## Property and Method Reference

Property and Method Reference

GeneralGeneral Settings:MaximumSettings:Maximum QueueQueue LengthLength

Specifies the maximum number of events that can be queued at any time on the given
session. This property is read/write until the first time you call VISA Enable Event on a
session. Thereafter, it is read only. The default is 50.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

GeneralGeneral Settings:ModelSettings:Model CodeCode

Returns the device model code assigned by the manufacturer. For VXI resources, this
refers to the VXI Model Code. For PXI/PCI resources, if the Subsystem Vendor ID is
nonzero, this refers to the Subsystem ID (SSID); otherwise, this refers to the Device ID
(DID). For USB resources, this refers to the Product ID (PID).

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


                                                    © National Instruments 10245

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10245 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10246 ordinal=10246 -->
## Property and Method Reference

Property and Method Reference

    GeneralGeneral Settings:ModelSettings:Model NameName

        Returns the model name of the device. Note: Use the value of this property for display
        purposes only and not for programmatic decisions. The value can change between
        VISA implementations and/or revisions.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    GeneralGeneral Settings:ResourceSettings:Resource ClassClass

        Returns the resource class of the resource string used to open the given session. For
        example, if the resource string for a given session is COM1 or ASRL1::INSTR, this
        property returns INSTR, regardless of the class of the I/O control.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


10246   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10246 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10247 ordinal=10247 -->
## Property and Method Reference

Property and Method Reference

GeneralGeneral Settings:ResourceSettings:Resource LockLock StateState

Returns the current locking state of the resource associated with the given session.
The resource can be unlocked, locked with an exclusive lock, or locked with a shared
lock. The default is Unlocked.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


 Unlocked                                                     0

 Exclusive                                                     1

 Shared                                                       2

GeneralGeneral Settings:ResourceSettings:Resource NameName

Returns the unique identifier for a resource.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


                                                    © National Instruments 10247

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10247 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10248 ordinal=10248 -->
## Property and Method Reference

Property and Method Reference

    GeneralGeneral Settings:SlotSettings:Slot

        Returns the physical slot location of the device. If the slot is unknown, the value
        returned is -1.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    GeneralGeneral Settings:TimeoutSettings:Timeout ValueValue

         Specifies the minimum timeout value, in milliseconds, to use when accessing the
         device. Note that the actual timeout that VISA returns may be higher than the one
        requested. The default is 2000.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes


10248   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10248 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10249 ordinal=10249 -->
## Property and Method Reference

Property and Method Reference

GeneralGeneral Settings:TriggerSettings:Trigger IdentifierIdentifier

Specifies which trigger mechanism to use. In VXI systems, for example, you can choose
between software triggers and hardware triggers on a specific trigger line. The default
is Software.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


 Software                                                             -1

 TTL0                                                     0

 TTL1                                                     1

 TTL2                                                     2

 TTL3                                                     3

 TTL4                                                     4

 TTL5                                                     5

 TTL6                                                     6

 TTL7                                                     7

 ECL0                                                     8

 ECL1                                                     9

GeneralGeneral Settings:UserSettings:User DataData

Specifies a data value for the private use of an application. The VISA implementation

                                                    © National Instruments 10249

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10249 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10250 ordinal=10250 -->
## Property and Method Reference

Property and Method Reference

         stores this value in a per-session location, so that user data on other sessions does not
         affect the user data on this session. VISA does not use this property for any purpose.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

     InterfaceInterface Information:InterfaceInformation:Interface DescriptionDescription

         Specifies human-readable text that describes the given interface. Note: Use the value
         of this property for display purposes only and not for programmatic decisions. The
        value can change between VISA implementations and/or revisions.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

     InterfaceInterface Information:InterfaceInformation:Interface NumberNumber

        Returns the board number for the given interface.


10250   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10250 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10251 ordinal=10251 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

InterfaceInterface Information:InterfaceInformation:Interface TypeType

Specifies the interface type of the given session.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


 GPIB                                                       1

 VXI                                                         2

 GPIB-VXI                                                    3

 Serial                                                       4

 PXI                                                         5

 TCPIP                                                      6

 USB                                                        7

 FireWire                                                    9


                                                    © National Instruments 10251

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10251 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10252 ordinal=10252 -->
## Property and Method Reference

Property and Method Reference

    PXI/PCIPXI/PCI Settings:ExpressSettings:Express Settings:ActualSettings:Actual LinkLink
    WidthWidth

        Returns the PCI Express link width negotiated between the PCI Express host controller
       and the device. A value of -1 indicates that the device is not a PXI/PCI Express device.
      Common values include 1, 2, 4, 8, and 16.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    PXI/PCIPXI/PCI Settings:ExpressSettings:Express Settings:D-StarSettings:D-Star BusBus
   NumberNumber

        Returns the differential star bus number of this device. A value of -1 means that the
         chassis is unidentified or does not have a timing slot.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


10252   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10252 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10253 ordinal=10253 -->
## Property and Method Reference

Property and Method Reference

PXI/PCIPXI/PCI Settings:ExpressSettings:Express Settings:D-StarSettings:D-Star SetSet

Returns the set of differential star lines connected to this device. A value of -1 means
that the chassis is unidentified or does not have a timing slot.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

PXI/PCIPXI/PCI Settings:ExpressSettings:Express Settings:IsSettings:Is PCIPCI
ExpressExpress

Returns whether the device is PXI/PCI or PXI/PCI Express.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


                                                    © National Instruments 10253

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10253 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10254 ordinal=10254 -->
## Property and Method Reference

Property and Method Reference

    PXI/PCIPXI/PCI Settings:ExpressSettings:Express Settings:MaximumSettings:Maximum
    LinkLink WidthWidth

        Returns the maximum PCI Express link width of the device. A value of -1 indicates that
        the device is not a PXI/PCI Express device. Common values include 1, 2, 4, 8, and 16.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    PXI/PCIPXI/PCI Settings:ExpressSettings:Express Settings:SlotSettings:Slot LinkLink
    WidthWidth

        Returns the PCI Express link width of the PXI Express peripheral slot in which the
        device resides. A value of -1 indicates that the device is not a PXI Express device.
      Common values include 1, 4, and 8.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


10254   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10254 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10255 ordinal=10255 -->
## Property and Method Reference

Property and Method Reference

PXI/PCIPXI/PCI Settings:PCISettings:PCI BusBus NumberNumber

Returns the PCI bus number of the PXI/PCI resource.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

PXI/PCIPXI/PCI Settings:PCISettings:PCI DeviceDevice NumberNumber

Returns the PCI device number of the PXI/PCI resource.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

PXI/PCIPXI/PCI Settings:PCISettings:PCI FunctionFunction NumberNumber

Returns the PCI function number of the PXI/PCI resource. For most devices, the
function number is 0, but a multifunction device may have a function number up to 7.
The meaning of a function number other than 0 is device-specific.


                                                    © National Instruments 10255

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10255 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10256 ordinal=10256 -->
## Property and Method Reference

Property and Method Reference

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    PXI/PCIPXI/PCI Settings:PCISettings:PCI Resources:BAR0Resources:BAR0
    AddressAddress BaseBase

        Returns the system-assigned base this device uses in the given space. If the device
       does not request addresses in this space, the value of this property is undefined.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    PXI/PCIPXI/PCI Settings:PCISettings:PCI Resources:BAR0Resources:BAR0
    AddressAddress SizeSize

        Returns the requested address size of this device in the given space. If the device does
        not request addresses in this space, the value of this property is undefined.


10256   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10256 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10257 ordinal=10257 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

PXI/PCIPXI/PCI Settings:PCISettings:PCI Resources:BAR0Resources:BAR0
AddressAddress TypeType

Returns what type of address requirements (memory or I/O) the device has for this
Base Address Register. If the device does not request addresses in this space, this
property returns None (0).

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


 None                                                      0

 Memory                                                   1

 I/O                                                        2


                                                    © National Instruments 10257

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10257 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10258 ordinal=10258 -->
## Property and Method Reference

Property and Method Reference

    PXI/PCIPXI/PCI Settings:PCISettings:PCI Resources:BAR1Resources:BAR1
    AddressAddress BaseBase

        Returns the system-assigned base this device uses in the given space. If the device
       does not request addresses in this space, the value of this property is undefined.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    PXI/PCIPXI/PCI Settings:PCISettings:PCI Resources:BAR1Resources:BAR1
    AddressAddress SizeSize

        Returns the requested address size of this device in the given space. If the device does
        not request addresses in this space, the value of this property is undefined.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


10258   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10258 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10259 ordinal=10259 -->
## Property and Method Reference

Property and Method Reference

PXI/PCIPXI/PCI Settings:PCISettings:PCI Resources:BAR1Resources:BAR1
AddressAddress TypeType

Returns what type of address requirements (memory or I/O) the device has for this
Base Address Register. If the device does not request addresses in this space, this
property returns None (0).

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


 None                                                      0

 Memory                                                   1

 I/O                                                        2

PXI/PCIPXI/PCI Settings:PCISettings:PCI Resources:BAR2Resources:BAR2
AddressAddress BaseBase

Returns the system-assigned base this device uses in the given space. If the device
does not request addresses in this space, the value of this property is undefined.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 10259

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10259 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10260 ordinal=10260 -->
## Property and Method Reference

Property and Method Reference


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    PXI/PCIPXI/PCI Settings:PCISettings:PCI Resources:BAR2Resources:BAR2
    AddressAddress SizeSize

        Returns the requested address size of this device in the given space. If the device does
        not request addresses in this space, the value of this property is undefined.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    PXI/PCIPXI/PCI Settings:PCISettings:PCI Resources:BAR2Resources:BAR2
    AddressAddress TypeType

        Returns what type of address requirements (memory or I/O) the device has for this
       Base Address Register. If the device does not request addresses in this space, this
        property returns None (0).

      Remarks

       The following table lists the characteristics of this property.

10260   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10260 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10261 ordinal=10261 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


 None                                                      0

 Memory                                                   1

 I/O                                                        2

PXI/PCIPXI/PCI Settings:PCISettings:PCI Resources:BAR3Resources:BAR3
AddressAddress BaseBase

Returns the system-assigned base this device uses in the given space. If the device
does not request addresses in this space, the value of this property is undefined.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

PXI/PCIPXI/PCI Settings:PCISettings:PCI Resources:BAR3Resources:BAR3
AddressAddress SizeSize

Returns the requested address size of this device in the given space. If the device does
not request addresses in this space, the value of this property is undefined.

                                                    © National Instruments 10261

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10261 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10262 ordinal=10262 -->
## Property and Method Reference

Property and Method Reference

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    PXI/PCIPXI/PCI Settings:PCISettings:PCI Resources:BAR3Resources:BAR3
    AddressAddress TypeType

        Returns what type of address requirements (memory or I/O) the device has for this
       Base Address Register. If the device does not request addresses in this space, this
        property returns None (0).

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


        None                                                      0

        Memory                                                   1

           I/O                                                        2


10262   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10262 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10263 ordinal=10263 -->
## Property and Method Reference

Property and Method Reference

PXI/PCIPXI/PCI Settings:PCISettings:PCI Resources:BAR4Resources:BAR4
AddressAddress BaseBase

Returns the system-assigned base this device uses in the given space. If the device
does not request addresses in this space, the value of this property is undefined.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

PXI/PCIPXI/PCI Settings:PCISettings:PCI Resources:BAR4Resources:BAR4
AddressAddress SizeSize

Returns the requested address size of this device in the given space. If the device does
not request addresses in this space, the value of this property is undefined.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


                                                    © National Instruments 10263

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10263 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10264 ordinal=10264 -->
## Property and Method Reference

Property and Method Reference

    PXI/PCIPXI/PCI Settings:PCISettings:PCI Resources:BAR4Resources:BAR4
    AddressAddress TypeType

        Returns what type of address requirements (memory or I/O) the device has for this
       Base Address Register. If the device does not request addresses in this space, this
        property returns None (0).

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


        None                                                      0

        Memory                                                   1

           I/O                                                        2

    PXI/PCIPXI/PCI Settings:PCISettings:PCI Resources:BAR5Resources:BAR5
    AddressAddress BaseBase

        Returns the system-assigned base this device uses in the given space. If the device
       does not request addresses in this space, the value of this property is undefined.

      Remarks

       The following table lists the characteristics of this property.


10264   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10264 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10265 ordinal=10265 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

PXI/PCIPXI/PCI Settings:PCISettings:PCI Resources:BAR5Resources:BAR5
AddressAddress SizeSize

Returns the requested address size of this device in the given space. If the device does
not request addresses in this space, the value of this property is undefined.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

PXI/PCIPXI/PCI Settings:PCISettings:PCI Resources:BAR5Resources:BAR5
AddressAddress TypeType

Returns what type of address requirements (memory or I/O) the device has for this
Base Address Register. If the device does not request addresses in this space, this
property returns None (0).

Remarks

The following table lists the characteristics of this property.

                                                    © National Instruments 10265

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10265 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10266 ordinal=10266 -->
## Property and Method Reference

Property and Method Reference


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


        None                                                      0

        Memory                                                   1

           I/O                                                        2

    PXI/PCIPXI/PCI Settings:PXISettings:PXI ChassisChassis NumberNumber

        Returns the PXI chassis number of this device. A value of -1 means the chassis number
           is unknown. Other valid values are 0 to 255.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    PXI/PCIPXI/PCI Settings:SlotSettings:Slot LocalLocal BusBus LeftLeft

        Returns the slot number or special feature connected to the local bus left lines of this
         device.

      Remarks

       The following table lists the characteristics of this property.

10266   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10266 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10267 ordinal=10267 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

PXI/PCIPXI/PCI Settings:SlotSettings:Slot LocalLocal BusBus RightRight

Returns the slot number or special feature connected to the local bus right lines of this
device.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

PXI/PCIPXI/PCI Settings:SlotSettings:Slot PathPath

Returns the slot path of this device.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

                                                    © National Instruments 10267

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10267 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10268 ordinal=10268 -->
## Property and Method Reference

Property and Method Reference

    PXI/PCIPXI/PCI Settings:StarSettings:Star TriggerTrigger BusBus NumberNumber

        Returns the star trigger bus number of this device.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    PXI/PCIPXI/PCI Settings:StarSettings:Star TriggerTrigger LineLine

        Returns the PXI_STAR line connected to this device.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    PXI/PCIPXI/PCI Settings:TriggerSettings:Trigger BusBus NumberNumber

        Returns the trigger bus number of this device.


10268   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10268 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10269 ordinal=10269 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

RegisterRegister BasedBased Settings:DestinationSettings:Destination
IncrementIncrement CountCount

Specifies the number of elements by which to increment the destination address on
block move operations. Valid values include 0 and 1. The default is 1. If this property is
set to 0, VISA Move Out X operations always read from the same element, essentially
treating the destination as a FIFO register.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

RegisterRegister BasedBased Settings:SourceSettings:Source IncrementIncrement
CountCount

Specifies the number of elements by which to increment the source address on block

                                                    © National Instruments 10269

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10269 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10270 ordinal=10270 -->
## Property and Method Reference

Property and Method Reference

      move operations. Valid values include 0 and 1. The default is 1. If this property is set to
          0, VISA Move In X operations always read from the same element, essentially treating
        the source as a FIFO register.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

     RegisterRegister BasedBased Settings:WindowSettings:Window AccessAccess

        Returns whether the current session has a mapped window, and if so, whether the
       window allows direct pointer dereferences.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


         Not Mapped                                                                1

         Use Peek/Poke Operations                                                    2

        Can Dereference Pointer                                                     3

          Pointer value is byte-swapped                                                4


10270   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10270 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10271 ordinal=10271 -->
## Property and Method Reference

Property and Method Reference

RegisterRegister BasedBased Settings:WindowSettings:Window BaseBase
AddressAddress

Returns the base interface address to which this window maps. If the Window Access
property is Not Mapped, the value of this property is undefined.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

RegisterRegister BasedBased Settings:WindowSettings:Window SizeSize

Returns the size of the region mapped to this window. If the Window Access property is
Not Mapped, the value of this property is undefined.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


                                                    © National Instruments 10271

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10271 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10272 ordinal=10272 -->
## Property and Method Reference

Property and Method Reference

    VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
     IdentificationIdentification

        Returns a value that corresponds to the VXI manufacturer ID of the manufacturer that
        created the VISA implementation.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
   NameName

        Returns the name of the manufacturer that created the implementation. This is not
         related to the device manufacturer attributes. Note: Use the value of this property for
         display purposes only and not for programmatic decisions. The value can change
       between VISA implementations and/or revisions.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes


10272   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10272 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10273 ordinal=10273 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                                   Yes

VersionVersion Information:VersionInformation:Version ofof
ImplementationImplementation

Returns the version of a given implementation. This value is defined by the individual
manufacturer and increments with each new revision. The format of the value has the
upper 12 bits as the major number of the version, the next lower 12 bits as the minor
number of the version, and the lowest 8 bits as the sub-minor number of the version.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VersionVersion Information:VersionInformation:Version ofof SpecificationSpecification

Returns the value that uniquely identifies the version of the VISA specification to which
the implementation complies. The format of the value has the upper 12 bits as the
major number of the version, the next lower 12 bits as the minor number of the
version, and the lowest 8 bits as the sub-minor number of the version.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

                                                    © National Instruments 10273

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10273 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10274 ordinal=10274 -->
## Property and Method Reference

Property and Method Reference


           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

       PXIPXI MemAccMemAcc PropertiesProperties


          Property             Description

          General                Specifies the maximum number of events that can be queued at any time
          Settings:Maximum    on the given session. This property is read/write until the first time you call
        Queue Length        VISA Enable Event on a session. Thereafter, it is read only. The default is 50.

                               Returns the resource class of the resource string used to open the given
          General                                   session. For example, if the resource string for a given session is COM1 or           Settings:Resource                                ASRL1::INSTR, this property returns INSTR, regardless of the class of the I/O           Class                                   control.

          General              Returns the current locking state of the resource associated with the given
           Settings:Resource     session. The resource can be unlocked, locked with an exclusive lock, or
         Lock State            locked with a shared lock. The default is Unlocked.

          General
           Settings:Resource     Returns the unique identifier for a resource.
        Name

          General                Specifies the minimum timeout value, in milliseconds, to use when
          Settings:Timeout      accessing the device. Note that the actual timeout that VISA returns may be
          Value                 higher than the one requested. The default is 2000.

                                   Specifies a data value for the private use of an application. The VISA
          General Settings:User  implementation stores this value in a per-session location, so that user data
          Data              on other sessions does not affect the user data on this session. VISA does
                               not use this property for any purpose.

                                   Specifies human-readable text that describes the given interface. Note: Use
           Interface
                               the value of this property for display purposes only and not for
           Information:Interface
                             programmatic decisions. The value can change between VISA
           Description
                              implementations and/or revisions.

           Interface
           Information:Interface  Returns the board number for the given interface.
        Number

           Interface
           Information:Interface  Specifies the interface type of the given session.
         Type

10274   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10274 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10275 ordinal=10275 -->
## Property and Method Reference

Property and Method Reference


Property             Description

                       Specifies the number of elements by which to increment the destinationRegister Based                     address on block move operations. Valid values include 0 and 1. The defaultSettings:Destination                             is 1. If this property is set to 0, VISA Move Out X operations always read fromIncrement Count                     the same element, essentially treating the destination as a FIFO register.

                       Specifies the number of elements by which to increment the source addressRegister Based                  on block move operations. Valid values include 0 and 1. The default is 1. IfSettings:Source                         this property is set to 0, VISA Move In X operations always read from theIncrement Count                 same element, essentially treating the source as a FIFO register.

Register Based                     Returns whether the current session has a mapped window, and if so,Settings:Window                    whether the window allows direct pointer dereferences.Access

Register Based        Returns the base interface address to which this window maps. If the
Settings:Window     Window Access property is Not Mapped, the value of this property is
Base Address         undefined.

Register Based        Returns the size of the region mapped to this window. If the Window Access
Settings:Window Size  property is Not Mapped, the value of this property is undefined.

Version
Information:Resource Returns a value that corresponds to the VXI manufacturer ID of the
Manufacturer         manufacturer that created the VISA implementation.
Identification

                     Returns the name of the manufacturer that created the implementation.
Version               This is not related to the device manufacturer attributes. Note: Use the
Information:Resource  value of this property for display purposes only and not for programmatic
Manufacturer Name   decisions. The value can change between VISA implementations and/or
                         revisions.

                     Returns the version of a given implementation. This value is defined by the
Version                individual manufacturer and increments with each new revision. The format
Information:Version   of the value has the upper 12 bits as the major number of the version, the
of Implementation    next lower 12 bits as the minor number of the version, and the lowest 8 bits
                     as the sub-minor number of the version.

                     Returns the value that uniquely identifies the version of the VISA
Version                specification to which the implementation complies. The format of the
Information:Version   value has the upper 12 bits as the major number of the version, the next
of Specification       lower 12 bits as the minor number of the version, and the lowest 8 bits as
                     the sub-minor number of the version.


                                                    © National Instruments 10275

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10275 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10276 ordinal=10276 -->
## Property and Method Reference

Property and Method Reference

    GeneralGeneral Settings:MaximumSettings:Maximum QueueQueue LengthLength

         Specifies the maximum number of events that can be queued at any time on the given
         session. This property is read/write until the first time you call VISA Enable Event on a
         session. Thereafter, it is read only. The default is 50.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

    GeneralGeneral Settings:ResourceSettings:Resource ClassClass

        Returns the resource class of the resource string used to open the given session. For
        example, if the resource string for a given session is COM1 or ASRL1::INSTR, this
        property returns INSTR, regardless of the class of the I/O control.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


10276   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10276 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10277 ordinal=10277 -->
## Property and Method Reference

Property and Method Reference

GeneralGeneral Settings:ResourceSettings:Resource LockLock StateState

Returns the current locking state of the resource associated with the given session.
The resource can be unlocked, locked with an exclusive lock, or locked with a shared
lock. The default is Unlocked.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


 Unlocked                                                     0

 Exclusive                                                     1

 Shared                                                       2

GeneralGeneral Settings:ResourceSettings:Resource NameName

Returns the unique identifier for a resource.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


                                                    © National Instruments 10277

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10277 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10278 ordinal=10278 -->
## Property and Method Reference

Property and Method Reference

    GeneralGeneral Settings:TimeoutSettings:Timeout ValueValue

         Specifies the minimum timeout value, in milliseconds, to use when accessing the
         device. Note that the actual timeout that VISA returns may be higher than the one
        requested. The default is 2000.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

    GeneralGeneral Settings:UserSettings:User DataData

         Specifies a data value for the private use of an application. The VISA implementation
         stores this value in a per-session location, so that user data on other sessions does not
         affect the user data on this session. VISA does not use this property for any purpose.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes


10278   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10278 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10279 ordinal=10279 -->
## Property and Method Reference

Property and Method Reference

InterfaceInterface Information:InterfaceInformation:Interface DescriptionDescription

Specifies human-readable text that describes the given interface. Note: Use the value
of this property for display purposes only and not for programmatic decisions. The
value can change between VISA implementations and/or revisions.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

InterfaceInterface Information:InterfaceInformation:Interface NumberNumber

Returns the board number for the given interface.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

InterfaceInterface Information:InterfaceInformation:Interface TypeType

Specifies the interface type of the given session.


                                                    © National Instruments 10279

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10279 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10280 ordinal=10280 -->
## Property and Method Reference

Property and Method Reference

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


         GPIB                                                       1

          VXI                                                         2

          GPIB-VXI                                                    3

           Serial                                                       4

          PXI                                                         5

         TCPIP                                                      6

        USB                                                        7

          FireWire                                                    9

     RegisterRegister BasedBased Settings:DestinationSettings:Destination
    IncrementIncrement CountCount

         Specifies the number of elements by which to increment the destination address on
        block move operations. Valid values include 0 and 1. The default is 1. If this property is
         set to 0, VISA Move Out X operations always read from the same element, essentially
         treating the destination as a FIFO register.

      Remarks

       The following table lists the characteristics of this property.


10280   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10280 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10281 ordinal=10281 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

RegisterRegister BasedBased Settings:SourceSettings:Source IncrementIncrement
CountCount

Specifies the number of elements by which to increment the source address on block
move operations. Valid values include 0 and 1. The default is 1. If this property is set to
0, VISA Move In X operations always read from the same element, essentially treating
the source as a FIFO register.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

RegisterRegister BasedBased Settings:WindowSettings:Window AccessAccess

Returns whether the current session has a mapped window, and if so, whether the
window allows direct pointer dereferences.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 10281

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10281 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10282 ordinal=10282 -->
## Property and Method Reference

Property and Method Reference


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


         Not Mapped                                                                1

         Use Peek/Poke Operations                                                    2

        Can Dereference Pointer                                                     3

          Pointer value is byte-swapped                                                4

     RegisterRegister BasedBased Settings:WindowSettings:Window BaseBase
    AddressAddress

        Returns the base interface address to which this window maps. If the Window Access
        property is Not Mapped, the value of this property is undefined.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

     RegisterRegister BasedBased Settings:WindowSettings:Window SizeSize

        Returns the size of the region mapped to this window. If the Window Access property is
       Not Mapped, the value of this property is undefined.


10282   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10282 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10283 ordinal=10283 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
IdentificationIdentification

Returns a value that corresponds to the VXI manufacturer ID of the manufacturer that
created the VISA implementation.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
NameName

Returns the name of the manufacturer that created the implementation. This is not
related to the device manufacturer attributes. Note: Use the value of this property for
display purposes only and not for programmatic decisions. The value can change

                                                    © National Instruments 10283

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10283 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10284 ordinal=10284 -->
## Property and Method Reference

Property and Method Reference

       between VISA implementations and/or revisions.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    VersionVersion Information:VersionInformation:Version ofof
    ImplementationImplementation

        Returns the version of a given implementation. This value is defined by the individual
        manufacturer and increments with each new revision. The format of the value has the
       upper 12 bits as the major number of the version, the next lower 12 bits as the minor
       number of the version, and the lowest 8 bits as the sub-minor number of the version.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    VersionVersion Information:VersionInformation:Version ofof SpecificationSpecification

        Returns the value that uniquely identifies the version of the VISA specification to which


10284   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10284 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10285 ordinal=10285 -->
## Property and Method Reference

Property and Method Reference

the implementation complies. The format of the value has the upper 12 bits as the
major number of the version, the next lower 12 bits as the minor number of the
version, and the lowest 8 bits as the sub-minor number of the version.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

SerialSerial InstrInstr PropertiesProperties


 Property             Description

                        Specifies whether I/O accesses should attempt to use DMA (TRUE) or General
                  Programmed I/O (FALSE). In some implementations, this property may have Settings:Allow DMA                       global effects even though it is documented as a local property. This Transfers
                      behavior affects performance and not functionality.

 General                Specifies the maximum number of events that can be queued at any time
 Settings:Maximum    on the given session. This property is read/write until the first time you call
 Queue Length        VISA Enable Event on a session. Thereafter, it is read only. The default is 50.

                      Returns the resource class of the resource string used to open the given General
                        session. For example, if the resource string for a given session is COM1 or
 Settings:Resource
                      ASRL1::INSTR, this property returns INSTR, regardless of the class of the I/O
 Class
                         control.

 General              Returns the current locking state of the resource associated with the given
 Settings:Resource     session. The resource can be unlocked, locked with an exclusive lock, or
 Lock State            locked with a shared lock. The default is Unlocked.

 General
 Settings:Resource     Returns the unique identifier for a resource.
 Name

 General                Specifies the minimum timeout value, in milliseconds, to use when
 Settings:Timeout      accessing the device. Note that the actual timeout that VISA returns may be

                                                    © National Instruments 10285

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10285 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10286 ordinal=10286 -->
## Property and Method Reference

Property and Method Reference


          Property             Description

          Value                 higher than the one requested. The default is 2000.

                                   Specifies a data value for the private use of an application. The VISA
          General Settings:User  implementation stores this value in a per-session location, so that user data
          Data              on other sessions does not affect the user data on this session. VISA does
                               not use this property for any purpose.

                                   Specifies human-readable text that describes the given interface. Note: Use           Interface                               the value of this property for display purposes only and not for           Information:Interface                             programmatic decisions. The value can change between VISA           Description
                              implementations and/or revisions.

           Interface
           Information:Interface  Returns the board number for the given interface.
        Number

           Interface
           Information:Interface  Specifies the interface type of the given session.
         Type

                                   Specifies whether VISA Read To File appends or overwrites (truncates) when         Message Based                             opening a file. If this property is set to TRUE, VISA Read To File appends
            Settings:File Append                         when opening a file. If this property is set to FALSE, VISA Read To          Enable                                       File overwrites (truncates) when opening a file. The default is FALSE.

                                   Specifies which protocol to use. In VXI, you can choose normal word serial
                                or fast data channel. In GPIB, you can choose normal or high-speed HS-488
         Message Based                                     transfers. In serial, TCP/IP, or USB, you can choose normal transfers or           Settings:IO Protocol                                 488.2-defined strings. In USBTMC, you can choose normal or vendor-specific
                                     transfers. The default is Normal.

                                   Specifies whether to send an END indicator on the last byte of each write
                                 operation. This property is relevant only in VISA Write and related
                                 operations. The default is TRUE. On Serial Instr sessions, if this property is
         Message Based        set to FALSE, the write transmits the exact contents of the user buffer,
          Settings:Send End     without modifying it and without appending anything to the data. If this
          Enable               property is set to TRUE, VISA performs the behavior described in the
                                property End Mode for Writes (ASRL End Out). On GPIB, VXI, GPIB-VXI, TCP/
                                   IP Instr, and USB Instr sessions, if this property is set to TRUE, VISA includes
                               the 488.2 defined end of message terminator.

                                   Specifies whether to terminate a read operation due to an END condition.
         Message Based
                                 This property is relevant only in VISA Read and related operations. For all
           Settings:Suppress
                                 session types that support this property, if this property is set to TRUE, read
         End Enable
                             does not terminate due to an END condition. However, a read may still


10286   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10286 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10287 ordinal=10287 -->
## Property and Method Reference

Property and Method Reference


Property             Description

                     terminate successfully if the Message Based Settings:Termination Character
                    Enable (TermChar En) property is set to TRUE. Otherwise, read does not
                     terminate until it receives all of the requested data (or an error occurs). The
                       default is FALSE (except for TCP/IP Socket sessions). On Serial Instr sessions,
                                    if this property is set to FALSE, VISA performs the behavior described in the
                         Serial Settings:End Mode for Reads (ASRL End In) property. On USB Raw
                       sessions, if this property is set to FALSE, VISA performs the behavior
                     described in the USB Settings:End Mode for Reads (USB End In) property.
                On TCP/IP Socket sessions, if this property is set to FALSE, if NI-VISA reads
                 some data and then detects a pause in the arrival of data packets, it
                      terminates the read operation. On TCP/IP Socket sessions, the default value
                         for the property is TRUE in NI-VISA. On VXI Instr sessions, if this property is
                        set to FALSE, the END bit terminates read operations.

Message Based        Specifies a character that, when read, causes a read operation to terminate.
Settings:Termination  The termination character also must be enabled. This default is 0x0A
Character               (linefeed).

Message Based
                       Specifies whether a read operation terminates when it receives theSettings:Termination                      termination character. The default is FALSE.Character Enable

                       Specifies whether to allow transmission. If FALSE, the serial port suspends
                      transmission as if an XOFF character has been received. If TRUE, it resumes
Serial Settings:Allow                      transmission as if an XON character has been received. If XON/XOFF flowTransmit                       control (software handshaking) is not being used, FALSE is an invalid value.
                   The default is TRUE.

                       Specifies the baud rate of the given communications port. The rate is
Serial Settings:Baud   represented as an unsigned 32-bit integer so that any baud rate can be
Rate                 used, but the communications port usually requires a commonly used rate
                    such as 300, 1200, 2400, or 9600 baud.

                       Specifies the duration (in milliseconds) of the break signal asserted when
Serial Settings:Break  End Mode for Writes (ASRL End Out) is set to Break (3). Valid values include
Length                1-500. The default is 250. If you want to control the assertion state and
                      length of a break signal manually, use the VISA Serial Break VI instead.

                       Specifies the number of data bits contained in each frame. Valid values
Serial Settings:Data
                      include 5-8. The data bits for each frame are located in the low-order bits of
Bits
                     every byte stored in memory.

Serial                  Specifies whether to discard each data byte whose value is 0. If this property
Settings:Discard NUL   is TRUE, read operations discard NUL characters. If this property is FALSE,
Characters           read operations treat NUL characters as normal data characters. For binary

                                                    © National Instruments 10287

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10287 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10288 ordinal=10288 -->
## Property and Method Reference

Property and Method Reference


          Property             Description

                                     transfers, set this property to FALSE. The default is FALSE.

                                   Specifies the method used to terminate read operations. Valid values
            Serial Settings:End     include: (0) None, (1) Last Bit, (2) TermChar. If the value is (2) TermChar, then
        Mode for Reads       the value of the property Termination Character Enable (TermChar En) is
                                 ignored. The default is (2) TermChar.

                                   Specifies the method used to terminate write operations. Valid values            Serial Settings:End                                  include: (0) None, (1) Last Bit, (2) TermChar, (3) Break. The default is (0)        Mode for Writes                             None.

            Serial Settings:Error                                   Specifies the character to use to replace incoming characters that arrive         Replacement                               with errors (such as a parity error). The default is 0.          Character

                                   Specifies the flow control method used for both transmitting and receiving
                                  data. Valid values include: (0) Flow None, (1) Flow XON/XOFF, (2) Flow RTS/            Serial Settings:Flow
                               CTS, (3) Flow XON/XOFF and RTS/CTS, (4) Flow DTR/DSR, (5) Flow XON/XOFF          Control                           and DTR/DSR. Certain values or combinations of values may not be
                              supported by all serial ports and/or operating systems.

                                   Specifies the value of the XOFF character used for XON/XOFF flow control
            Serial Settings:Flow                                (both directions). If XON/XOFF flow control (software handshaking) is not          Control XOFF                               being used, the value of this property is ignored. The default is 0x13
          Character                                    (Control-S).

                                   Specifies the value of the XON character used for XON/XOFF flow control
            Serial Settings:Flow                                (both directions). If XON/XOFF flow control (software handshaking) is not          Control XON                               being used, the value of this property is ignored. The default is 0x11
          Character                                   (Control-Q).

                               Returns whether the port is properly connected to another port or device.
            Serial Settings:Is Port  This property is valid only with serial drivers developed by National
         Connected           Instruments and documented to support this feature with the
                               corresponding National Instruments hardware.

                                 Sets manual control of the serial port's break state. If asserted, this property
                             suspends character transmission and places the transmission line in a break
            Serial
                                    state until this property is unasserted. If you want VISA to send a break
          Settings:Modem Line
                                   signal after each write operation automatically, use the Break Length (Break
           Settings:Break State
                                Len) and End Mode for Writes (ASRL End Out) properties instead. The
                                  default is Unasserted.

            Serial
          Settings:Modem Line  Returns the current state of the Clear To Send (CTS) input signal.
           Settings:Line CTS

10288   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10288 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10289 ordinal=10289 -->
## Property and Method Reference

Property and Method Reference


Property             Description

State

                       Specifies the current state of the Data Carrier Detect (DCD) input signal. ThisSerial                             is often used by modems to indicate the detection of a carrier (modem) onSettings:Modem Line                     the phone line. This signal is also known as Receive Line Signal DetectSettings:Line DCD
                      (RLSD). This property is read only except when the Wire Mode property is setState                      to RS232/DCE, or RS232/Auto with the hardware currently in the DCE state.

Serial
Settings:Modem Line                     Returns the current state of the Data Set Ready (DSR) input signal.
Settings:Line DSR
State

Serial
Settings:Modem Line                       Asserts or unasserts the Data Terminal Ready (DTR) output signal manually.Settings:Line DTR
State

                       Specifies the current state of the Ring Indicator (RI) input signal. The RISerial
                        signal is often used by modems to indicate that the telephone line is ringing.Settings:Modem Line                      This property is read only except when the Wire Mode property is set to
Settings:Line RI State                   RS232/DCE or to RS232/Auto with the hardware currently in the DCE state.

Serial
                       Asserts or unasserts the Request To Send (RTS) output signal manually.Settings:Modem Line                When the flow control is set to hardware handshaking, it is invalid to changeSettings:Line RTS
                         this property.State

Serial
                     Returns the number of bytes currently available at the serial port used bySettings:Number of                         this session.Bytes at Serial Port

                       Specifies the parity used with every frame that is transmitted or received.
                        Valid values include: (0) Parity None, (1) Parity Odd, (2) Parity Even, (3) Parity
Serial Settings:Parity
                     Mark, (4) Parity Space. Mark means that the parity bit exists and is always 1.
                   Space means that the parity bit exists and is always 0.

Serial Settings:Stop    Specifies the number of stop bits used to indicate the end of a frame. Valid
Bits                  values include: (10) Stop One, (15) Stop One-and-a-Half, (20) Stop Two.

                       Specifies the current wire/transceiver mode. For RS485 hardware, this
                     property is valid only with the RS485 serial driver developed by National
Serial Settings:Wire    Instruments. For RS232 hardware, the values RS232/DCE and RS232/Auto
Mode                 are valid only with RS232 serial drivers developed by National Instruments
                  and documented to support this feature with the corresponding National
                     Instruments hardware. When this feature is not supported, RS232/DTE is the

                                                    © National Instruments 10289

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10289 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10290 ordinal=10290 -->
## Property and Method Reference

Property and Method Reference


          Property             Description

                                only valid value.

           Version
          Information:Resource Returns a value that corresponds to the VXI manufacturer ID of the
          Manufacturer         manufacturer that created the VISA implementation.
            Identification

                               Returns the name of the manufacturer that created the implementation.
           Version               This is not related to the device manufacturer attributes. Note: Use the
          Information:Resource  value of this property for display purposes only and not for programmatic
          Manufacturer Name   decisions. The value can change between VISA implementations and/or
                                    revisions.

                               Returns the version of a given implementation. This value is defined by the
           Version                individual manufacturer and increments with each new revision. The format
           Information:Version   of the value has the upper 12 bits as the major number of the version, the
           of Implementation    next lower 12 bits as the minor number of the version, and the lowest 8 bits
                               as the sub-minor number of the version.

                               Returns the value that uniquely identifies the version of the VISA
           Version                specification to which the implementation complies. The format of the
           Information:Version   value has the upper 12 bits as the major number of the version, the next
           of Specification       lower 12 bits as the minor number of the version, and the lowest 8 bits as
                               the sub-minor number of the version.

    GeneralGeneral Settings:AllowSettings:Allow DMADMA TransfersTransfers

         Specifies whether I/O accesses should attempt to use DMA (TRUE) or Programmed I/O
         (FALSE). In some implementations, this property may have global effects even though
             it is documented as a local property. This behavior affects performance and not
         functionality.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write


10290   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10290 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10291 ordinal=10291 -->
## Property and Method Reference

Property and Method Reference


 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

GeneralGeneral Settings:MaximumSettings:Maximum QueueQueue LengthLength

Specifies the maximum number of events that can be queued at any time on the given
session. This property is read/write until the first time you call VISA Enable Event on a
session. Thereafter, it is read only. The default is 50.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

GeneralGeneral Settings:ResourceSettings:Resource ClassClass

Returns the resource class of the resource string used to open the given session. For
example, if the resource string for a given session is COM1 or ASRL1::INSTR, this
property returns INSTR, regardless of the class of the I/O control.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

                                                    © National Instruments 10291

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10291 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10292 ordinal=10292 -->
## Property and Method Reference

Property and Method Reference

    GeneralGeneral Settings:ResourceSettings:Resource LockLock StateState

        Returns the current locking state of the resource associated with the given session.
       The resource can be unlocked, locked with an exclusive lock, or locked with a shared
         lock. The default is Unlocked.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


         Unlocked                                                     0

           Exclusive                                                     1

         Shared                                                       2

    GeneralGeneral Settings:ResourceSettings:Resource NameName

        Returns the unique identifier for a resource.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


10292   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10292 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10293 ordinal=10293 -->
## Property and Method Reference

Property and Method Reference

GeneralGeneral Settings:TimeoutSettings:Timeout ValueValue

Specifies the minimum timeout value, in milliseconds, to use when accessing the
device. Note that the actual timeout that VISA returns may be higher than the one
requested. The default is 2000.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

GeneralGeneral Settings:UserSettings:User DataData

Specifies a data value for the private use of an application. The VISA implementation
stores this value in a per-session location, so that user data on other sessions does not
affect the user data on this session. VISA does not use this property for any purpose.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


                                                    © National Instruments 10293

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10293 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10294 ordinal=10294 -->
## Property and Method Reference

Property and Method Reference

     InterfaceInterface Information:InterfaceInformation:Interface DescriptionDescription

         Specifies human-readable text that describes the given interface. Note: Use the value
         of this property for display purposes only and not for programmatic decisions. The
        value can change between VISA implementations and/or revisions.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

     InterfaceInterface Information:InterfaceInformation:Interface NumberNumber

        Returns the board number for the given interface.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

     InterfaceInterface Information:InterfaceInformation:Interface TypeType

         Specifies the interface type of the given session.


10294   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10294 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10295 ordinal=10295 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


 GPIB                                                       1

 VXI                                                         2

 GPIB-VXI                                                    3

 Serial                                                       4

 PXI                                                         5

 TCPIP                                                      6

 USB                                                        7

 FireWire                                                    9

MessageMessage BasedBased Settings:FileSettings:File AppendAppend EnableEnable

Specifies whether VISA Read To File appends or overwrites (truncates) when opening a
file. If this property is set to TRUE, VISA Read To File appends when opening a file. If
this property is set to FALSE, VISA Read To File overwrites (truncates) when opening a
file. The default is FALSE.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write


                                                    © National Instruments 10295

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10295 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10296 ordinal=10296 -->
## Property and Method Reference

Property and Method Reference


           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

    MessageMessage BasedBased Settings:IOSettings:IO ProtocolProtocol

         Specifies which protocol to use. In VXI, you can choose normal word serial or fast data
        channel. In GPIB, you can choose normal or high-speed HS-488 transfers. In serial,
         TCP/IP, or USB, you can choose normal transfers or 488.2-defined strings. In USBTMC,
       you can choose normal or vendor-specific transfers. The default is Normal.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes


         Normal                                                                    1

          VXI/FDC                                                                   2

         GPIB/HS488                                                                3

          Serial-TCPIP-USB/488 Strings                                                 4

          USBTMC/Vendor-Specific                                                    5

    MessageMessage BasedBased Settings:SendSettings:Send EndEnd EnableEnable

         Specifies whether to send an END indicator on the last byte of each write operation.
        This property is relevant only in VISA Write and related operations. The default is TRUE.
      On Serial Instr sessions, if this property is set to FALSE, the write transmits the exact
        contents of the user buffer, without modifying it and without appending anything to

10296   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10296 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10297 ordinal=10297 -->
## Property and Method Reference

Property and Method Reference

the data. If this property is set to TRUE, VISA performs the behavior described in the
property End Mode for Writes (ASRL End Out). On GPIB, VXI, GPIB-VXI, TCP/IP Instr, and
USB Instr sessions, if this property is set to TRUE, VISA includes the 488.2 defined end
of message terminator.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

MessageMessage BasedBased Settings:SuppressSettings:Suppress EndEnd
EnableEnable

Specifies whether to terminate a read operation due to an END condition. This
property is relevant only in VISA Read and related operations. For all session types that
support this property, if this property is set to TRUE, read does not terminate due to an
END condition. However, a read may still terminate successfully if the Message Based
Settings:Termination Character Enable (TermChar En) property is set to TRUE.
Otherwise, read does not terminate until it receives all of the requested data (or an
error occurs). The default is FALSE (except for TCP/IP Socket sessions). On Serial Instr
sessions, if this property is set to FALSE, VISA performs the behavior described in the
Serial Settings:End Mode for Reads (ASRL End In) property. On USB Raw sessions, if
this property is set to FALSE, VISA performs the behavior described in the USB
Settings:End Mode for Reads (USB End In) property. On TCP/IP Socket sessions, if this
property is set to FALSE, if NI-VISA reads some data and then detects a pause in the
arrival of data packets, it terminates the read operation. On TCP/IP Socket sessions,
the default value for the property is TRUE in NI-VISA. On VXI Instr sessions, if this
property is set to FALSE, the END bit terminates read operations.


                                                    © National Instruments 10297

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10297 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10298 ordinal=10298 -->
## Property and Method Reference

Property and Method Reference

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

    MessageMessage BasedBased Settings:TerminationSettings:Termination
    CharacterCharacter

         Specifies a character that, when read, causes a read operation to terminate. The
        termination character also must be enabled. This default is 0x0A (linefeed).

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

    MessageMessage BasedBased Settings:TerminationSettings:Termination
    CharacterCharacter EnableEnable

         Specifies whether a read operation terminates when it receives the termination
         character. The default is FALSE.


10298   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10298 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10299 ordinal=10299 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

SerialSerial Settings:AllowSettings:Allow TransmitTransmit

Specifies whether to allow transmission. If FALSE, the serial port suspends
transmission as if an XOFF character has been received. If TRUE, it resumes
transmission as if an XON character has been received. If XON/XOFF flow control
(software handshaking) is not being used, FALSE is an invalid value. The default is
TRUE.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

SerialSerial Settings:BaudSettings:Baud RateRate

Specifies the baud rate of the given communications port. The rate is represented as
an unsigned 32-bit integer so that any baud rate can be used, but the communications
port usually requires a commonly used rate such as 300, 1200, 2400, or 9600 baud.


                                                    © National Instruments 10299

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10299 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10300 ordinal=10300 -->
## Property and Method Reference

Property and Method Reference

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

     SerialSerial Settings:BreakSettings:Break LengthLength

         Specifies the duration (in milliseconds) of the break signal asserted when End Mode for
        Writes (ASRL End Out) is set to Break (3). Valid values include 1-500. The default is 250.
             If you want to control the assertion state and length of a break signal manually, use the
        VISA Serial Break VI instead.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

     SerialSerial Settings:DataSettings:Data BitsBits

         Specifies the number of data bits contained in each frame. Valid values include 5-8.
       The data bits for each frame are located in the low-order bits of every byte stored in
       memory.


10300   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10300 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10301 ordinal=10301 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

SerialSerial Settings:DiscardSettings:Discard NULNUL CharactersCharacters

Specifies whether to discard each data byte whose value is 0. If this property is TRUE,
read operations discard NUL characters. If this property is FALSE, read operations treat
NUL characters as normal data characters. For binary transfers, set this property to
FALSE. The default is FALSE.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

SerialSerial Settings:EndSettings:End ModeMode forfor ReadsReads

Specifies the method used to terminate read operations. Valid values include: (0)
None, (1) Last Bit, (2) TermChar. If the value is (2) TermChar, then the value of the
property Termination Character Enable (TermChar En) is ignored. The default is (2)
TermChar.


                                                    © National Instruments 10301

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10301 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10302 ordinal=10302 -->
## Property and Method Reference

Property and Method Reference

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes


        None                                                         0

          Last Bit                                                       1

         TermChar                                                     2

     SerialSerial Settings:EndSettings:End ModeMode forfor WritesWrites

         Specifies the method used to terminate write operations. Valid values include: (0)
       None, (1) Last Bit, (2) TermChar, (3) Break. The default is (0) None.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes


        None                                                         0

          Last Bit                                                       1

         TermChar                                                     2


10302   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10302 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10303 ordinal=10303 -->
## Property and Method Reference

Property and Method Reference


 Break                                                        3

SerialSerial Settings:ErrorSettings:Error ReplacementReplacement CharacterCharacter

Specifies the character to use to replace incoming characters that arrive with errors
(such as a parity error). The default is 0.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

SerialSerial Settings:FlowSettings:Flow ControlControl

Specifies the flow control method used for both transmitting and receiving data. Valid
values include: (0) Flow None, (1) Flow XON/XOFF, (2) Flow RTS/CTS, (3) Flow XON/
XOFF and RTS/CTS, (4) Flow DTR/DSR, (5) Flow XON/XOFF and DTR/DSR. Certain values
or combinations of values may not be supported by all serial ports and/or operating
systems.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


                                                    © National Instruments 10303

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10303 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10304 ordinal=10304 -->
## Property and Method Reference

Property and Method Reference


        None                                                                   0

        XON/XOFF                                                              1

         RTS/CTS                                                                2

        XON/XOFF & RTS/CTS                                                     3

        DTR/DSR                                                               4

        XON/XOFF & DTR/DSR                                                     5

     SerialSerial Settings:FlowSettings:Flow ControlControl XOFFXOFF CharacterCharacter

         Specifies the value of the XOFF character used for XON/XOFF flow control (both
         directions). If XON/XOFF flow control (software handshaking) is not being used, the
        value of this property is ignored. The default is 0x13 (Control-S).

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

     SerialSerial Settings:FlowSettings:Flow ControlControl XONXON CharacterCharacter

         Specifies the value of the XON character used for XON/XOFF flow control (both
         directions). If XON/XOFF flow control (software handshaking) is not being used, the
        value of this property is ignored. The default is 0x11 (Control-Q).

      Remarks

       The following table lists the characteristics of this property.


10304   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10304 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10305 ordinal=10305 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

SerialSerial Settings:IsSettings:Is PortPort ConnectedConnected

Returns whether the port is properly connected to another port or device. This
property is valid only with serial drivers developed by National Instruments and
documented to support this feature with the corresponding National Instruments
hardware.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

SerialSerial Settings:ModemSettings:Modem LineLine Settings:BreakSettings:Break
StateState

Sets manual control of the serial port's break state. If asserted, this property suspends
character transmission and places the transmission line in a break state until this
property is unasserted. If you want VISA to send a break signal after each write
operation automatically, use the Break Length (Break Len) and End Mode for Writes
(ASRL End Out) properties instead. The default is Unasserted.


                                                    © National Instruments 10305

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10305 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10306 ordinal=10306 -->
## Property and Method Reference

Property and Method Reference

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes


        Unknown                                                                 -1

          Unasserted                                                   0

          Asserted                                                     1

     SerialSerial Settings:ModemSettings:Modem LineLine Settings:LineSettings:Line
    CTSCTS StateState

        Returns the current state of the Clear To Send (CTS) input signal.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


        Unknown                                                                 -1

          Unasserted                                                   0


10306   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10306 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10307 ordinal=10307 -->
## Property and Method Reference

Property and Method Reference


 Asserted                                                     1

SerialSerial Settings:ModemSettings:Modem LineLine Settings:LineSettings:Line
DCDDCD StateState

Specifies the current state of the Data Carrier Detect (DCD) input signal. This is often
used by modems to indicate the detection of a carrier (modem) on the phone line. This
signal is also known as Receive Line Signal Detect (RLSD). This property is read only
except when the Wire Mode property is set to RS232/DCE, or RS232/Auto with the
hardware currently in the DCE state.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


 Unknown                                                                 -1

 Unasserted                                                   0

 Asserted                                                     1

SerialSerial Settings:ModemSettings:Modem LineLine Settings:LineSettings:Line
DSRDSR StateState

Returns the current state of the Data Set Ready (DSR) input signal.


                                                    © National Instruments 10307

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10307 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10308 ordinal=10308 -->
## Property and Method Reference

Property and Method Reference

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


        Unknown                                                                 -1

          Unasserted                                                   0

          Asserted                                                     1

     SerialSerial Settings:ModemSettings:Modem LineLine Settings:LineSettings:Line
   DTRDTR StateState

         Asserts or unasserts the Data Terminal Ready (DTR) output signal manually.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes


        Unknown                                                                 -1

          Unasserted                                                   0


10308   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10308 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10309 ordinal=10309 -->
## Property and Method Reference

Property and Method Reference


 Asserted                                                     1

SerialSerial Settings:ModemSettings:Modem LineLine Settings:LineSettings:Line RIRI
StateState

Specifies the current state of the Ring Indicator (RI) input signal. The RI signal is often
used by modems to indicate that the telephone line is ringing. This property is read
only except when the Wire Mode property is set to RS232/DCE or to RS232/Auto with
the hardware currently in the DCE state.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


 Unknown                                                                 -1

 Unasserted                                                   0

 Asserted                                                     1

SerialSerial Settings:ModemSettings:Modem LineLine Settings:LineSettings:Line RTSRTS
StateState

Asserts or unasserts the Request To Send (RTS) output signal manually. When the flow
control is set to hardware handshaking, it is invalid to change this property.


                                                    © National Instruments 10309

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10309 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10310 ordinal=10310 -->
## Property and Method Reference

Property and Method Reference

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes


        Unknown                                                                 -1

          Unasserted                                                   0

          Asserted                                                     1

     SerialSerial Settings:NumberSettings:Number ofof BytesBytes atat SerialSerial PortPort

        Returns the number of bytes currently available at the serial port used by this session.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

     SerialSerial Settings:ParitySettings:Parity

         Specifies the parity used with every frame that is transmitted or received. Valid values
         include: (0) Parity None, (1) Parity Odd, (2) Parity Even, (3) Parity Mark, (4) Parity Space.
       Mark means that the parity bit exists and is always 1. Space means that the parity bit

10310   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10310 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10311 ordinal=10311 -->
## Property and Method Reference

Property and Method Reference

exists and is always 0.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


 None                                                 0

 Odd                                                  1

 Even                                                 2

 Mark                                                 3

 Space                                                 4

SerialSerial Settings:StopSettings:Stop BitsBits

Specifies the number of stop bits used to indicate the end of a frame. Valid values
include: (10) Stop One, (15) Stop One-and-a-Half, (20) Stop Two.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


                                                    © National Instruments 10311

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10311 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10312 ordinal=10312 -->
## Property and Method Reference

Property and Method Reference


           1.0                                    10

           1.5                                    15

           2.0                                    20

     SerialSerial Settings:WireSettings:Wire ModeMode

         Specifies the current wire/transceiver mode. For RS485 hardware, this property is valid
        only with the RS485 serial driver developed by National Instruments. For RS232
        hardware, the values RS232/DCE and RS232/Auto are valid only with RS232 serial
         drivers developed by National Instruments and documented to support this feature
        with the corresponding National Instruments hardware. When this feature is not
        supported, RS232/DTE is the only valid value.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes


        Unknown                                                                       -1

         RS485/Wire4                                                       0

         RS485/Wire2-EchoDTR                                               1

          RS485/Wire2-CtrlDTR                                                2

          RS485/Wire2-Auto                                                  3

         RS232/DTE                                                         128

         RS232/DCE                                                         129

         RS232/Auto                                                        130


10312   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10312 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10313 ordinal=10313 -->
## Property and Method Reference

Property and Method Reference

VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
IdentificationIdentification

Returns a value that corresponds to the VXI manufacturer ID of the manufacturer that
created the VISA implementation.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
NameName

Returns the name of the manufacturer that created the implementation. This is not
related to the device manufacturer attributes. Note: Use the value of this property for
display purposes only and not for programmatic decisions. The value can change
between VISA implementations and/or revisions.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes


                                                    © National Instruments 10313

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10313 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10314 ordinal=10314 -->
## Property and Method Reference

Property and Method Reference


           Available in Real-Time Operating System                                   Yes

    VersionVersion Information:VersionInformation:Version ofof
    ImplementationImplementation

        Returns the version of a given implementation. This value is defined by the individual
        manufacturer and increments with each new revision. The format of the value has the
       upper 12 bits as the major number of the version, the next lower 12 bits as the minor
       number of the version, and the lowest 8 bits as the sub-minor number of the version.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    VersionVersion Information:VersionInformation:Version ofof SpecificationSpecification

        Returns the value that uniquely identifies the version of the VISA specification to which
        the implementation complies. The format of the value has the upper 12 bits as the
       major number of the version, the next lower 12 bits as the minor number of the
         version, and the lowest 8 bits as the sub-minor number of the version.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

10314   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10314 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10315 ordinal=10315 -->
## Property and Method Reference

Property and Method Reference


 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

TCP/IPTCP/IP InstrInstr PropertiesProperties


 Property             Description

 General                Specifies the maximum number of events that can be queued at any time
 Settings:Maximum    on the given session. This property is read/write until the first time you call
 Queue Length        VISA Enable Event on a session. Thereafter, it is read only. The default is 50.

                      Returns the resource class of the resource string used to open the given
 General                        session. For example, if the resource string for a given session is COM1 or Settings:Resource                      ASRL1::INSTR, this property returns INSTR, regardless of the class of the I/O Class                         control.

 General              Returns the current locking state of the resource associated with the given
 Settings:Resource     session. The resource can be unlocked, locked with an exclusive lock, or
 Lock State            locked with a shared lock. The default is Unlocked.

 General
 Settings:Resource     Returns the unique identifier for a resource.
 Name

 General                Specifies the minimum timeout value, in milliseconds, to use when
 Settings:Timeout      accessing the device. Note that the actual timeout that VISA returns may be
 Value                 higher than the one requested. The default is 2000.

                        Specifies a data value for the private use of an application. The VISA
 General Settings:User  implementation stores this value in a per-session location, so that user data
 Data              on other sessions does not affect the user data on this session. VISA does
                     not use this property for any purpose.

                        Specifies human-readable text that describes the given interface. Note: Use
 Interface
                      the value of this property for display purposes only and not for
 Information:Interface
                    programmatic decisions. The value can change between VISA
 Description
                     implementations and/or revisions.

 Interface
 Information:Interface  Returns the board number for the given interface.
 Number

 Interface
 Information:Interface  Specifies the interface type of the given session.
 Type

                                                    © National Instruments 10315

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10315 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10316 ordinal=10316 -->
## Property and Method Reference

Property and Method Reference


          Property             Description

                                   Specifies whether VISA Read To File appends or overwrites (truncates) when         Message Based                             opening a file. If this property is set to TRUE, VISA Read To File appends            Settings:File Append                         when opening a file. If this property is set to FALSE, VISA Read To          Enable                                       File overwrites (truncates) when opening a file. The default is FALSE.

                                   Specifies whether to send an END indicator on the last byte of each write
                                 operation. This property is relevant only in VISA Write and related
                                 operations. The default is TRUE. On Serial Instr sessions, if this property is
         Message Based        set to FALSE, the write transmits the exact contents of the user buffer,
          Settings:Send End     without modifying it and without appending anything to the data. If this
          Enable               property is set to TRUE, VISA performs the behavior described in the
                                property End Mode for Writes (ASRL End Out). On GPIB, VXI, GPIB-VXI, TCP/
                                   IP Instr, and USB Instr sessions, if this property is set to TRUE, VISA includes
                               the 488.2 defined end of message terminator.

         Message Based        Specifies a character that, when read, causes a read operation to terminate.
           Settings:Termination  The termination character also must be enabled. This default is 0x0A
          Character               (linefeed).

         Message Based
                                   Specifies whether a read operation terminates when it receives the           Settings:Termination                                termination character. The default is FALSE.          Character Enable

          TCP/IP                               Returns the host name of the device. If no host name is available, this          Settings:Computer
                                property returns an empty string.         Hostname

          TCP/IP Settings:Dot-   Returns the TCPIP address of the device to which the session is connected.
          Notation Address      This string is formatted in dot notation.

                                   Specifies whether to use keep-alive packets on TCP connections. Setting
                                     this property to TRUE requests that a TCP/IP provider enable the use of
          TCP/IP Settings:Keep-  keep-alive packets on TCP connections. After the system detects a dropped
            Alive Packets          connection, VISA returns a lost connection error code on subsequent I/O
                                      calls on the session. The time required for the system to detect the dropped
                               connection depends on the system and is not settable. The default is FALSE.

          TCP/IP Settings:LAN   Returns the LAN device name used by the VXI-11 protocol (for example,
          Device Name           inst0) during connection.

                                   Specifies whether the Nagle algorithm is enabled. The Nagle algorithm is
                                disabled when this property is TRUE (and vice versa). The Nagle algorithm
          TCP/IP Settings:No
                              improves network performance by buffering written data until a full-size
          Packet Delay
                               packet can be sent. This property is TRUE by default in VISA to verify that
                                  writes get flushed immediately.


10316   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10316 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10317 ordinal=10317 -->
## Property and Method Reference

Property and Method Reference


 Property             Description

 Version
 Information:Resource Returns a value that corresponds to the VXI manufacturer ID of the
 Manufacturer         manufacturer that created the VISA implementation.
 Identification

                      Returns the name of the manufacturer that created the implementation.
 Version               This is not related to the device manufacturer attributes. Note: Use the
 Information:Resource  value of this property for display purposes only and not for programmatic
 Manufacturer Name   decisions. The value can change between VISA implementations and/or
                         revisions.

                      Returns the version of a given implementation. This value is defined by the
 Version                individual manufacturer and increments with each new revision. The format
 Information:Version   of the value has the upper 12 bits as the major number of the version, the
 of Implementation    next lower 12 bits as the minor number of the version, and the lowest 8 bits
                      as the sub-minor number of the version.

                      Returns the value that uniquely identifies the version of the VISA
 Version                specification to which the implementation complies. The format of the
 Information:Version   value has the upper 12 bits as the major number of the version, the next
 of Specification       lower 12 bits as the minor number of the version, and the lowest 8 bits as
                      the sub-minor number of the version.

GeneralGeneral Settings:MaximumSettings:Maximum QueueQueue LengthLength

Specifies the maximum number of events that can be queued at any time on the given
session. This property is read/write until the first time you call VISA Enable Event on a
session. Thereafter, it is read only. The default is 50.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


                                                    © National Instruments 10317

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10317 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10318 ordinal=10318 -->
## Property and Method Reference

Property and Method Reference

    GeneralGeneral Settings:ResourceSettings:Resource ClassClass

        Returns the resource class of the resource string used to open the given session. For
        example, if the resource string for a given session is COM1 or ASRL1::INSTR, this
        property returns INSTR, regardless of the class of the I/O control.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    GeneralGeneral Settings:ResourceSettings:Resource LockLock StateState

        Returns the current locking state of the resource associated with the given session.
       The resource can be unlocked, locked with an exclusive lock, or locked with a shared
         lock. The default is Unlocked.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


         Unlocked                                                     0


10318   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10318 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10319 ordinal=10319 -->
## Property and Method Reference

Property and Method Reference


 Exclusive                                                     1

 Shared                                                       2

GeneralGeneral Settings:ResourceSettings:Resource NameName

Returns the unique identifier for a resource.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

GeneralGeneral Settings:TimeoutSettings:Timeout ValueValue

Specifies the minimum timeout value, in milliseconds, to use when accessing the
device. Note that the actual timeout that VISA returns may be higher than the one
requested. The default is 2000.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


                                                    © National Instruments 10319

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10319 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10320 ordinal=10320 -->
## Property and Method Reference

Property and Method Reference

    GeneralGeneral Settings:UserSettings:User DataData

         Specifies a data value for the private use of an application. The VISA implementation
         stores this value in a per-session location, so that user data on other sessions does not
         affect the user data on this session. VISA does not use this property for any purpose.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

     InterfaceInterface Information:InterfaceInformation:Interface DescriptionDescription

         Specifies human-readable text that describes the given interface. Note: Use the value
         of this property for display purposes only and not for programmatic decisions. The
        value can change between VISA implementations and/or revisions.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


10320   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10320 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10321 ordinal=10321 -->
## Property and Method Reference

Property and Method Reference

InterfaceInterface Information:InterfaceInformation:Interface NumberNumber

Returns the board number for the given interface.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

InterfaceInterface Information:InterfaceInformation:Interface TypeType

Specifies the interface type of the given session.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


 GPIB                                                       1

 VXI                                                         2

 GPIB-VXI                                                    3

 Serial                                                       4


                                                    © National Instruments 10321

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10321 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10322 ordinal=10322 -->
## Property and Method Reference

Property and Method Reference


          PXI                                                         5

         TCPIP                                                      6

        USB                                                        7

          FireWire                                                    9

    MessageMessage BasedBased Settings:FileSettings:File AppendAppend EnableEnable

         Specifies whether VISA Read To File appends or overwrites (truncates) when opening a
            file. If this property is set to TRUE, VISA Read To File appends when opening a file. If
          this property is set to FALSE, VISA Read To File overwrites (truncates) when opening a
            file. The default is FALSE.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

    MessageMessage BasedBased Settings:SendSettings:Send EndEnd EnableEnable

         Specifies whether to send an END indicator on the last byte of each write operation.
        This property is relevant only in VISA Write and related operations. The default is TRUE.
      On Serial Instr sessions, if this property is set to FALSE, the write transmits the exact
        contents of the user buffer, without modifying it and without appending anything to
        the data. If this property is set to TRUE, VISA performs the behavior described in the
        property End Mode for Writes (ASRL End Out). On GPIB, VXI, GPIB-VXI, TCP/IP Instr, and
      USB Instr sessions, if this property is set to TRUE, VISA includes the 488.2 defined end
         of message terminator.


10322   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10322 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10323 ordinal=10323 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

MessageMessage BasedBased Settings:TerminationSettings:Termination
CharacterCharacter

Specifies a character that, when read, causes a read operation to terminate. The
termination character also must be enabled. This default is 0x0A (linefeed).

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

MessageMessage BasedBased Settings:TerminationSettings:Termination
CharacterCharacter EnableEnable

Specifies whether a read operation terminates when it receives the termination
character. The default is FALSE.


                                                    © National Instruments 10323

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10323 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10324 ordinal=10324 -->
## Property and Method Reference

Property and Method Reference

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

    TCP/IPTCP/IP Settings:ComputerSettings:Computer HostnameHostname

        Returns the host name of the device. If no host name is available, this property returns
       an empty string.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    TCP/IPTCP/IP Settings:Dot-NotationSettings:Dot-Notation AddressAddress

        Returns the TCPIP address of the device to which the session is connected. This string
           is formatted in dot notation.

      Remarks

       The following table lists the characteristics of this property.


10324   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10324 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10325 ordinal=10325 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

TCP/IPTCP/IP Settings:Keep-AliveSettings:Keep-Alive PacketsPackets

Specifies whether to use keep-alive packets on TCP connections. Setting this property
to TRUE requests that a TCP/IP provider enable the use of keep-alive packets on TCP
connections. After the system detects a dropped connection, VISA returns a lost
connection error code on subsequent I/O calls on the session. The time required for
the system to detect the dropped connection depends on the system and is not
settable. The default is FALSE.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

TCP/IPTCP/IP Settings:LANSettings:LAN DeviceDevice NameName

Returns the LAN device name used by the VXI-11 protocol (for example, inst0) during
connection.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 10325

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10325 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10326 ordinal=10326 -->
## Property and Method Reference

Property and Method Reference


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    TCP/IPTCP/IP Settings:NoSettings:No PacketPacket DelayDelay

         Specifies whether the Nagle algorithm is enabled. The Nagle algorithm is disabled
      when this property is TRUE (and vice versa). The Nagle algorithm improves network
        performance by buffering written data until a full-size packet can be sent. This
        property is TRUE by default in VISA to verify that writes get flushed immediately.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

    VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
     IdentificationIdentification

        Returns a value that corresponds to the VXI manufacturer ID of the manufacturer that
        created the VISA implementation.

      Remarks

       The following table lists the characteristics of this property.


10326   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10326 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10327 ordinal=10327 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
NameName

Returns the name of the manufacturer that created the implementation. This is not
related to the device manufacturer attributes. Note: Use the value of this property for
display purposes only and not for programmatic decisions. The value can change
between VISA implementations and/or revisions.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VersionVersion Information:VersionInformation:Version ofof
ImplementationImplementation

Returns the version of a given implementation. This value is defined by the individual
manufacturer and increments with each new revision. The format of the value has the
upper 12 bits as the major number of the version, the next lower 12 bits as the minor
number of the version, and the lowest 8 bits as the sub-minor number of the version.


                                                    © National Instruments 10327

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10327 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10328 ordinal=10328 -->
## Property and Method Reference

Property and Method Reference

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    VersionVersion Information:VersionInformation:Version ofof SpecificationSpecification

        Returns the value that uniquely identifies the version of the VISA specification to which
        the implementation complies. The format of the value has the upper 12 bits as the
       major number of the version, the next lower 12 bits as the minor number of the
         version, and the lowest 8 bits as the sub-minor number of the version.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

       TCP/IPTCP/IP SocketSocket PropertiesProperties


          Property             Description

          General                Specifies the maximum number of events that can be queued at any time
          Settings:Maximum    on the given session. This property is read/write until the first time you call
        Queue Length        VISA Enable Event on a session. Thereafter, it is read only. The default is 50.

          General              Returns the resource class of the resource string used to open the given


10328   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10328 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10329 ordinal=10329 -->
## Property and Method Reference

Property and Method Reference


Property             Description

                       session. For example, if the resource string for a given session is COM1 orSettings:Resource                     ASRL1::INSTR, this property returns INSTR, regardless of the class of the I/OClass                        control.

General              Returns the current locking state of the resource associated with the given
Settings:Resource     session. The resource can be unlocked, locked with an exclusive lock, or
Lock State            locked with a shared lock. The default is Unlocked.

General
Settings:Resource     Returns the unique identifier for a resource.
Name

General                Specifies the minimum timeout value, in milliseconds, to use when
Settings:Timeout      accessing the device. Note that the actual timeout that VISA returns may be
Value                 higher than the one requested. The default is 2000.

                       Specifies a data value for the private use of an application. The VISA
General Settings:User  implementation stores this value in a per-session location, so that user data
Data              on other sessions does not affect the user data on this session. VISA does
                     not use this property for any purpose.

                       Specifies human-readable text that describes the given interface. Note: Use
Interface                     the value of this property for display purposes only and not forInformation:Interface                    programmatic decisions. The value can change between VISA
Description                    implementations and/or revisions.

Interface
Information:Interface  Returns the board number for the given interface.
Number

Interface
Information:Interface  Specifies the interface type of the given session.
Type

                       Specifies whether VISA Read To File appends or overwrites (truncates) when
Message Based
                    opening a file. If this property is set to TRUE, VISA Read To File appends
Settings:File Append
                 when opening a file. If this property is set to FALSE, VISA Read To
Enable
                          File overwrites (truncates) when opening a file. The default is FALSE.

                       Specifies which protocol to use. In VXI, you can choose normal word serial
                      or fast data channel. In GPIB, you can choose normal or high-speed HS-488
Message Based
                         transfers. In serial, TCP/IP, or USB, you can choose normal transfers or
Settings:IO Protocol
                      488.2-defined strings. In USBTMC, you can choose normal or vendor-specific
                         transfers. The default is Normal.

Message Based        Specifies whether to send an END indicator on the last byte of each write


                                                    © National Instruments 10329

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10329 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10330 ordinal=10330 -->
## Property and Method Reference

Property and Method Reference


          Property             Description

                                 operation. This property is relevant only in VISA Write and related
                                 operations. The default is TRUE. On Serial Instr sessions, if this property is
                                   set to FALSE, the write transmits the exact contents of the user buffer,
          Settings:Send End     without modifying it and without appending anything to the data. If this
          Enable               property is set to TRUE, VISA performs the behavior described in the
                                property End Mode for Writes (ASRL End Out). On GPIB, VXI, GPIB-VXI, TCP/
                                   IP Instr, and USB Instr sessions, if this property is set to TRUE, VISA includes
                               the 488.2 defined end of message terminator.

                                   Specifies whether to terminate a read operation due to an END condition.
                                 This property is relevant only in VISA Read and related operations. For all
                                 session types that support this property, if this property is set to TRUE, read
                             does not terminate due to an END condition. However, a read may still
                                terminate successfully if the Message Based Settings:Termination Character
                              Enable (TermChar En) property is set to TRUE. Otherwise, read does not
                                terminate until it receives all of the requested data (or an error occurs). The
         Message Based        default is FALSE (except for TCP/IP Socket sessions). On Serial Instr sessions,
           Settings:Suppress        if this property is set to FALSE, VISA performs the behavior described in the
         End Enable             Serial Settings:End Mode for Reads (ASRL End In) property. On USB Raw
                                  sessions, if this property is set to FALSE, VISA performs the behavior
                               described in the USB Settings:End Mode for Reads (USB End In) property.
                        On TCP/IP Socket sessions, if this property is set to FALSE, if NI-VISA reads
                         some data and then detects a pause in the arrival of data packets, it
                                terminates the read operation. On TCP/IP Socket sessions, the default value
                                     for the property is TRUE in NI-VISA. On VXI Instr sessions, if this property is
                                   set to FALSE, the END bit terminates read operations.

         Message Based        Specifies a character that, when read, causes a read operation to terminate.
           Settings:Termination  The termination character also must be enabled. This default is 0x0A
          Character               (linefeed).

         Message Based
                                   Specifies whether a read operation terminates when it receives the
           Settings:Termination
                                termination character. The default is FALSE.
          Character Enable

          TCP/IP
                               Returns the host name of the device. If no host name is available, this
          Settings:Computer
                                property returns an empty string.
         Hostname

          TCP/IP Settings:Dot-   Returns the TCPIP address of the device to which the session is connected.
          Notation Address      This string is formatted in dot notation.

          TCP/IP Settings:Keep-  Specifies whether to use keep-alive packets on TCP connections. Setting
            Alive Packets           this property to TRUE requests that a TCP/IP provider enable the use of


10330   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10330 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10331 ordinal=10331 -->
## Property and Method Reference

Property and Method Reference


Property             Description

                       keep-alive packets on TCP connections. After the system detects a dropped
                      connection, VISA returns a lost connection error code on subsequent I/O
                          calls on the session. The time required for the system to detect the dropped
                     connection depends on the system and is not settable. The default is FALSE.

                       Specifies whether the Nagle algorithm is enabled. The Nagle algorithm is
                      disabled when this property is TRUE (and vice versa). The Nagle algorithmTCP/IP Settings:No                    improves network performance by buffering written data until a full-sizePacket Delay                     packet can be sent. This property is TRUE by default in VISA to verify that
                       writes get flushed immediately.

TCP/IP Settings:Port   Returns the port number for a given TCPIP address. For a TCPIP SOCKET
Number               resource, this is a required part of the address/resource string.

TCP/IP
Settings:Server       Returns the expiration date of the server certificate. The form is ASN.1
Certificate Expiration  UTCTime “YYMMDDhhmm[ss]Z.
Date

TCP/IP
Settings:Server
                       Indicates the certificate does not expire.Certificate Is
Perpetual

TCP/IP
Settings:Server
                     Returns the name of the CA that signed the certificate in RFC4514 format.Certificate Issuer
Name

TCP/IP
Settings:Server       Returns the serial number and subject field from the certificate om RFC4514
Certificate Subject     format.
Name

TCP/IP Settings:TLS
                     Returns a string that indicates the cipher suite used by TLS.
Cipher Suite

Version
Information:Resource Returns a value that corresponds to the VXI manufacturer ID of the
Manufacturer         manufacturer that created the VISA implementation.
Identification

                     Returns the name of the manufacturer that created the implementation.
Version
                      This is not related to the device manufacturer attributes. Note: Use the
Information:Resource
                      value of this property for display purposes only and not for programmatic
Manufacturer Name
                       decisions. The value can change between VISA implementations and/or

                                                    © National Instruments 10331

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10331 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10332 ordinal=10332 -->
## Property and Method Reference

Property and Method Reference


          Property             Description

                                    revisions.

                               Returns the version of a given implementation. This value is defined by the
           Version                individual manufacturer and increments with each new revision. The format
           Information:Version   of the value has the upper 12 bits as the major number of the version, the
           of Implementation    next lower 12 bits as the minor number of the version, and the lowest 8 bits
                               as the sub-minor number of the version.

                               Returns the value that uniquely identifies the version of the VISA
           Version                specification to which the implementation complies. The format of the
           Information:Version   value has the upper 12 bits as the major number of the version, the next
           of Specification       lower 12 bits as the minor number of the version, and the lowest 8 bits as
                               the sub-minor number of the version.

    GeneralGeneral Settings:MaximumSettings:Maximum QueueQueue LengthLength

         Specifies the maximum number of events that can be queued at any time on the given
         session. This property is read/write until the first time you call VISA Enable Event on a
         session. Thereafter, it is read only. The default is 50.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

    GeneralGeneral Settings:ResourceSettings:Resource ClassClass

        Returns the resource class of the resource string used to open the given session. For
        example, if the resource string for a given session is COM1 or ASRL1::INSTR, this
        property returns INSTR, regardless of the class of the I/O control.


10332   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10332 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10333 ordinal=10333 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

GeneralGeneral Settings:ResourceSettings:Resource LockLock StateState

Returns the current locking state of the resource associated with the given session.
The resource can be unlocked, locked with an exclusive lock, or locked with a shared
lock. The default is Unlocked.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


 Unlocked                                                     0

 Exclusive                                                     1

 Shared                                                       2

GeneralGeneral Settings:ResourceSettings:Resource NameName

Returns the unique identifier for a resource.

                                                    © National Instruments 10333

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10333 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10334 ordinal=10334 -->
## Property and Method Reference

Property and Method Reference

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    GeneralGeneral Settings:TimeoutSettings:Timeout ValueValue

         Specifies the minimum timeout value, in milliseconds, to use when accessing the
         device. Note that the actual timeout that VISA returns may be higher than the one
        requested. The default is 2000.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

    GeneralGeneral Settings:UserSettings:User DataData

         Specifies a data value for the private use of an application. The VISA implementation
         stores this value in a per-session location, so that user data on other sessions does not
         affect the user data on this session. VISA does not use this property for any purpose.


10334   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10334 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10335 ordinal=10335 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

InterfaceInterface Information:InterfaceInformation:Interface DescriptionDescription

Specifies human-readable text that describes the given interface. Note: Use the value
of this property for display purposes only and not for programmatic decisions. The
value can change between VISA implementations and/or revisions.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

InterfaceInterface Information:InterfaceInformation:Interface NumberNumber

Returns the board number for the given interface.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 10335

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10335 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10336 ordinal=10336 -->
## Property and Method Reference

Property and Method Reference


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

     InterfaceInterface Information:InterfaceInformation:Interface TypeType

         Specifies the interface type of the given session.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


         GPIB                                                       1

          VXI                                                         2

          GPIB-VXI                                                    3

           Serial                                                       4

          PXI                                                         5

         TCPIP                                                      6

        USB                                                        7

          FireWire                                                    9


10336   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10336 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10337 ordinal=10337 -->
## Property and Method Reference

Property and Method Reference

MessageMessage BasedBased Settings:FileSettings:File AppendAppend EnableEnable

Specifies whether VISA Read To File appends or overwrites (truncates) when opening a
file. If this property is set to TRUE, VISA Read To File appends when opening a file. If
this property is set to FALSE, VISA Read To File overwrites (truncates) when opening a
file. The default is FALSE.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

MessageMessage BasedBased Settings:IOSettings:IO ProtocolProtocol

Specifies which protocol to use. In VXI, you can choose normal word serial or fast data
channel. In GPIB, you can choose normal or high-speed HS-488 transfers. In serial,
TCP/IP, or USB, you can choose normal transfers or 488.2-defined strings. In USBTMC,
you can choose normal or vendor-specific transfers. The default is Normal.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


                                                    © National Instruments 10337

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10337 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10338 ordinal=10338 -->
## Property and Method Reference

Property and Method Reference


         Normal                                                                    1

          VXI/FDC                                                                   2

         GPIB/HS488                                                                3

          Serial-TCPIP-USB/488 Strings                                                 4

          USBTMC/Vendor-Specific                                                    5

    MessageMessage BasedBased Settings:SendSettings:Send EndEnd EnableEnable

         Specifies whether to send an END indicator on the last byte of each write operation.
        This property is relevant only in VISA Write and related operations. The default is TRUE.
      On Serial Instr sessions, if this property is set to FALSE, the write transmits the exact
        contents of the user buffer, without modifying it and without appending anything to
        the data. If this property is set to TRUE, VISA performs the behavior described in the
        property End Mode for Writes (ASRL End Out). On GPIB, VXI, GPIB-VXI, TCP/IP Instr, and
      USB Instr sessions, if this property is set to TRUE, VISA includes the 488.2 defined end
         of message terminator.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

    MessageMessage BasedBased Settings:SuppressSettings:Suppress EndEnd
    EnableEnable

         Specifies whether to terminate a read operation due to an END condition. This
        property is relevant only in VISA Read and related operations. For all session types that

10338   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10338 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10339 ordinal=10339 -->
## Property and Method Reference

Property and Method Reference

support this property, if this property is set to TRUE, read does not terminate due to an
END condition. However, a read may still terminate successfully if the Message Based
Settings:Termination Character Enable (TermChar En) property is set to TRUE.
Otherwise, read does not terminate until it receives all of the requested data (or an
error occurs). The default is FALSE (except for TCP/IP Socket sessions). On Serial Instr
sessions, if this property is set to FALSE, VISA performs the behavior described in the
Serial Settings:End Mode for Reads (ASRL End In) property. On USB Raw sessions, if
this property is set to FALSE, VISA performs the behavior described in the USB
Settings:End Mode for Reads (USB End In) property. On TCP/IP Socket sessions, if this
property is set to FALSE, if NI-VISA reads some data and then detects a pause in the
arrival of data packets, it terminates the read operation. On TCP/IP Socket sessions,
the default value for the property is TRUE in NI-VISA. On VXI Instr sessions, if this
property is set to FALSE, the END bit terminates read operations.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

MessageMessage BasedBased Settings:TerminationSettings:Termination
CharacterCharacter

Specifies a character that, when read, causes a read operation to terminate. The
termination character also must be enabled. This default is 0x0A (linefeed).

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 10339

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10339 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10340 ordinal=10340 -->
## Property and Method Reference

Property and Method Reference


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

    MessageMessage BasedBased Settings:TerminationSettings:Termination
    CharacterCharacter EnableEnable

         Specifies whether a read operation terminates when it receives the termination
         character. The default is FALSE.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

    TCP/IPTCP/IP Settings:ComputerSettings:Computer HostnameHostname

        Returns the host name of the device. If no host name is available, this property returns
       an empty string.

      Remarks

       The following table lists the characteristics of this property.


          Data type


10340   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10340 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10341 ordinal=10341 -->
## Property and Method Reference

Property and Method Reference


 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

TCP/IPTCP/IP Settings:Dot-NotationSettings:Dot-Notation AddressAddress

Returns the TCPIP address of the device to which the session is connected. This string
is formatted in dot notation.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

TCP/IPTCP/IP Settings:Keep-AliveSettings:Keep-Alive PacketsPackets

Specifies whether to use keep-alive packets on TCP connections. Setting this property
to TRUE requests that a TCP/IP provider enable the use of keep-alive packets on TCP
connections. After the system detects a dropped connection, VISA returns a lost
connection error code on subsequent I/O calls on the session. The time required for
the system to detect the dropped connection depends on the system and is not
settable. The default is FALSE.

Remarks

The following table lists the characteristics of this property.


 Data type


                                                    © National Instruments 10341

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10341 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10342 ordinal=10342 -->
## Property and Method Reference

Property and Method Reference


          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

    TCP/IPTCP/IP Settings:NoSettings:No PacketPacket DelayDelay

         Specifies whether the Nagle algorithm is enabled. The Nagle algorithm is disabled
      when this property is TRUE (and vice versa). The Nagle algorithm improves network
        performance by buffering written data until a full-size packet can be sent. This
        property is TRUE by default in VISA to verify that writes get flushed immediately.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

    TCP/IPTCP/IP Settings:PortSettings:Port NumberNumber

        Returns the port number for a given TCPIP address. For a TCPIP SOCKET resource, this
           is a required part of the address/resource string.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

10342   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10342 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10343 ordinal=10343 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                                   Yes

TCP/IPTCP/IP Settings:ServerSettings:Server CertificateCertificate ExpirationExpiration
DateDate

Returns the expiration date of the server certificate. The form is ASN.1 UTCTime
“YYMMDDhhmm[ss]Z.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

TCP/IPTCP/IP Settings:ServerSettings:Server CertificateCertificate IsIs
PerpetualPerpetual

Indicates the certificate does not expire.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

                                                    © National Instruments 10343

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10343 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10344 ordinal=10344 -->
## Property and Method Reference

Property and Method Reference

    TCP/IPTCP/IP Settings:ServerSettings:Server CertificateCertificate IssuerIssuer
   NameName

        Returns the name of the CA that signed the certificate in RFC4514 format.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    TCP/IPTCP/IP Settings:ServerSettings:Server CertificateCertificate SubjectSubject
   NameName

        Returns the serial number and subject field from the certificate om RFC4514 format.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


10344   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10344 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10345 ordinal=10345 -->
## Property and Method Reference

Property and Method Reference

TCP/IPTCP/IP Settings:TLSSettings:TLS CipherCipher SuiteSuite

Returns a string that indicates the cipher suite used by TLS.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
IdentificationIdentification

Returns a value that corresponds to the VXI manufacturer ID of the manufacturer that
created the VISA implementation.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


                                                    © National Instruments 10345

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10345 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10346 ordinal=10346 -->
## Property and Method Reference

Property and Method Reference

    VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
   NameName

        Returns the name of the manufacturer that created the implementation. This is not
         related to the device manufacturer attributes. Note: Use the value of this property for
         display purposes only and not for programmatic decisions. The value can change
       between VISA implementations and/or revisions.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    VersionVersion Information:VersionInformation:Version ofof
    ImplementationImplementation

        Returns the version of a given implementation. This value is defined by the individual
        manufacturer and increments with each new revision. The format of the value has the
       upper 12 bits as the major number of the version, the next lower 12 bits as the minor
       number of the version, and the lowest 8 bits as the sub-minor number of the version.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only


10346   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10346 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10347 ordinal=10347 -->
## Property and Method Reference

Property and Method Reference


 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VersionVersion Information:VersionInformation:Version ofof SpecificationSpecification

Returns the value that uniquely identifies the version of the VISA specification to which
the implementation complies. The format of the value has the upper 12 bits as the
major number of the version, the next lower 12 bits as the minor number of the
version, and the lowest 8 bits as the sub-minor number of the version.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

USBUSB InstrInstr PropertiesProperties


 Property              Description

                      Returns the ID of the manufacturer that created the device. For VXI
 General                resources, this refers to the VXI Manufacturer ID. For PXI/PCI resources, this
 Settings:Manufacturer  refers to the Subsystem Vendor ID (SVID) if it is nonzero; otherwise, this
 Identification           refers to the Vendor ID (VID). For USB resources, this refers to the Vendor ID
                           (VID).

                      Returns the name of the manufacturer that created the device. Note: Use
 General
                      the value of this property for display purposes only and not for
 Settings:Manufacturer
                     programmatic decisions. The value can change between VISA
 Name
                      implementations and/or revisions.

 General                Specifies the maximum number of events that can be queued at any time
 Settings:Maximum    on the given session. This property is read/write until the first time you call
 Queue Length         VISA Enable Event on a session. Thereafter, it is read only. The default is 50.

                                                    © National Instruments 10347

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10347 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10348 ordinal=10348 -->
## Property and Method Reference

Property and Method Reference


          Property              Description

                                Returns the device model code assigned by the manufacturer. For VXI
                                  resources, this refers to the VXI Model Code. For PXI/PCI resources, if the          General                             Subsystem Vendor ID is nonzero, this refers to the Subsystem ID (SSID);          Settings:Model Code                                 otherwise, this refers to the Device ID (DID). For USB resources, this refers to
                                the Product ID (PID).

                                Returns the model name of the device. Note: Use the value of this property          General                                     for display purposes only and not for programmatic decisions. The value          Settings:Model Name                             can change between VISA implementations and/or revisions.

                                Returns the resource class of the resource string used to open the given          General                                   session. For example, if the resource string for a given session is COM1 or           Settings:Resource                                ASRL1::INSTR, this property returns INSTR, regardless of the class of the I/O           Class                                    control.

          General              Returns the current locking state of the resource associated with the given
           Settings:Resource      session. The resource can be unlocked, locked with an exclusive lock, or
         Lock State            locked with a shared lock. The default is Unlocked.

          General
           Settings:Resource     Returns the unique identifier for a resource.
        Name

          General                Specifies the minimum timeout value, in milliseconds, to use when
          Settings:Timeout      accessing the device. Note that the actual timeout that VISA returns may be
          Value                 higher than the one requested. The default is 2000.

                                   Specifies a data value for the private use of an application. The VISA
          General Settings:User  implementation stores this value in a per-session location, so that user data
          Data               on other sessions does not affect the user data on this session. VISA does
                               not use this property for any purpose.

                                   Specifies human-readable text that describes the given interface. Note: Use
           Interface
                                the value of this property for display purposes only and not for
           Information:Interface
                             programmatic decisions. The value can change between VISA
           Description
                               implementations and/or revisions.

           Interface
           Information:Interface  Returns the board number for the given interface.
        Number

           Interface
           Information:Interface  Specifies the interface type of the given session.
         Type

         Message Based         Specifies which protocol to use. In VXI, you can choose normal word serial


10348   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10348 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10349 ordinal=10349 -->
## Property and Method Reference

Property and Method Reference


Property              Description

                      or fast data channel. In GPIB, you can choose normal or high-speed HS-488
                         transfers. In serial, TCP/IP, or USB, you can choose normal transfers orSettings:IO Protocol                       488.2-defined strings. In USBTMC, you can choose normal or vendor-
                         specific transfers. The default is Normal.

Message Based
Settings:Is 488.2       Returns whether the device is 488.2 compliant.
Compliant

                        Specifies whether to send an END indicator on the last byte of each write
                       operation. This property is relevant only in VISA Write and related
                       operations. The default is TRUE. On Serial Instr sessions, if this property is
Message Based         set to FALSE, the write transmits the exact contents of the user buffer,
Settings:Send End     without modifying it and without appending anything to the data. If this
Enable                property is set to TRUE, VISA performs the behavior described in the
                      property End Mode for Writes (ASRL End Out). On GPIB, VXI, GPIB-VXI, TCP/
                        IP Instr, and USB Instr sessions, if this property is set to TRUE, VISA includes
                      the 488.2 defined end of message terminator.

Message Based         Specifies a character that, when read, causes a read operation to terminate.
Settings:Termination  The termination character also must be enabled. This default is 0x0A
Character               (linefeed).

Message Based                        Specifies whether a read operation terminates when it receives theSettings:Termination
                      termination character. The default is FALSE.Character Enable

                        Specifies the maximum size of data stored by any given USB interrupt. If a
USB              USB interrupt contains more data than this size, the data in excess of this
Settings:Maximum      size is lost. This property is read/write when the corresponding session is
Interrupt Size         not enabled to receive USB interrupt events. When the session is enabled to
                       receive USB interrupt events, this property is read only.

USB Settings:Serial
                     Returns the USB serial number of this device.
Number

USB Settings:USB
                     Returns the USB interface number used by the given session.
Interface Number

USB Settings:USB
                     Returns the USB protocol used by the given session.
Protocol

Version
Information:Resource  Returns a value that corresponds to the VXI manufacturer ID of the
Manufacturer         manufacturer that created the VISA implementation.
Identification

                                                    © National Instruments 10349

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10349 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10350 ordinal=10350 -->
## Property and Method Reference

Property and Method Reference


          Property              Description

                                Returns the name of the manufacturer that created the implementation.
           Version                This is not related to the device manufacturer attributes. Note: Use the
          Information:Resource  value of this property for display purposes only and not for programmatic
          Manufacturer Name    decisions. The value can change between VISA implementations and/or
                                     revisions.

                                Returns the version of a given implementation. This value is defined by the
           Version                individual manufacturer and increments with each new revision. The
           Information:Version   format of the value has the upper 12 bits as the major number of the
           of Implementation     version, the next lower 12 bits as the minor number of the version, and the
                                lowest 8 bits as the sub-minor number of the version.

                                Returns the value that uniquely identifies the version of the VISA
           Version                 specification to which the implementation complies. The format of the
           Information:Version    value has the upper 12 bits as the major number of the version, the next
           of Specification       lower 12 bits as the minor number of the version, and the lowest 8 bits as
                                the sub-minor number of the version.

    GeneralGeneral Settings:ManufacturerSettings:Manufacturer IdentificationIdentification

        Returns the ID of the manufacturer that created the device. For VXI resources, this
         refers to the VXI Manufacturer ID. For PXI/PCI resources, this refers to the Subsystem
       Vendor ID (SVID) if it is nonzero; otherwise, this refers to the Vendor ID (VID). For USB
         resources, this refers to the Vendor ID (VID).

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


10350   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10350 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10351 ordinal=10351 -->
## Property and Method Reference

Property and Method Reference

GeneralGeneral Settings:ManufacturerSettings:Manufacturer NameName

Returns the name of the manufacturer that created the device. Note: Use the value of
this property for display purposes only and not for programmatic decisions. The value
can change between VISA implementations and/or revisions.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

GeneralGeneral Settings:MaximumSettings:Maximum QueueQueue LengthLength

Specifies the maximum number of events that can be queued at any time on the given
session. This property is read/write until the first time you call VISA Enable Event on a
session. Thereafter, it is read only. The default is 50.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


                                                    © National Instruments 10351

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10351 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10352 ordinal=10352 -->
## Property and Method Reference

Property and Method Reference

    GeneralGeneral Settings:ModelSettings:Model CodeCode

        Returns the device model code assigned by the manufacturer. For VXI resources, this
         refers to the VXI Model Code. For PXI/PCI resources, if the Subsystem Vendor ID is
        nonzero, this refers to the Subsystem ID (SSID); otherwise, this refers to the Device ID
         (DID). For USB resources, this refers to the Product ID (PID).

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    GeneralGeneral Settings:ModelSettings:Model NameName

        Returns the model name of the device. Note: Use the value of this property for display
        purposes only and not for programmatic decisions. The value can change between
        VISA implementations and/or revisions.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


10352   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10352 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10353 ordinal=10353 -->
## Property and Method Reference

Property and Method Reference

GeneralGeneral Settings:ResourceSettings:Resource ClassClass

Returns the resource class of the resource string used to open the given session. For
example, if the resource string for a given session is COM1 or ASRL1::INSTR, this
property returns INSTR, regardless of the class of the I/O control.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

GeneralGeneral Settings:ResourceSettings:Resource LockLock StateState

Returns the current locking state of the resource associated with the given session.
The resource can be unlocked, locked with an exclusive lock, or locked with a shared
lock. The default is Unlocked.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


 Unlocked                                                     0


                                                    © National Instruments 10353

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10353 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10354 ordinal=10354 -->
## Property and Method Reference

Property and Method Reference


           Exclusive                                                     1

         Shared                                                       2

    GeneralGeneral Settings:ResourceSettings:Resource NameName

        Returns the unique identifier for a resource.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    GeneralGeneral Settings:TimeoutSettings:Timeout ValueValue

         Specifies the minimum timeout value, in milliseconds, to use when accessing the
         device. Note that the actual timeout that VISA returns may be higher than the one
        requested. The default is 2000.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes


10354   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10354 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10355 ordinal=10355 -->
## Property and Method Reference

Property and Method Reference

GeneralGeneral Settings:UserSettings:User DataData

Specifies a data value for the private use of an application. The VISA implementation
stores this value in a per-session location, so that user data on other sessions does not
affect the user data on this session. VISA does not use this property for any purpose.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

InterfaceInterface Information:InterfaceInformation:Interface DescriptionDescription

Specifies human-readable text that describes the given interface. Note: Use the value
of this property for display purposes only and not for programmatic decisions. The
value can change between VISA implementations and/or revisions.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


                                                    © National Instruments 10355

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10355 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10356 ordinal=10356 -->
## Property and Method Reference

Property and Method Reference

     InterfaceInterface Information:InterfaceInformation:Interface NumberNumber

        Returns the board number for the given interface.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

     InterfaceInterface Information:InterfaceInformation:Interface TypeType

         Specifies the interface type of the given session.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


         GPIB                                                       1

          VXI                                                         2

          GPIB-VXI                                                    3

           Serial                                                       4


10356   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10356 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10357 ordinal=10357 -->
## Property and Method Reference

Property and Method Reference


 PXI                                                         5

 TCPIP                                                      6

 USB                                                        7

 FireWire                                                    9

MessageMessage BasedBased Settings:IOSettings:IO ProtocolProtocol

Specifies which protocol to use. In VXI, you can choose normal word serial or fast data
channel. In GPIB, you can choose normal or high-speed HS-488 transfers. In serial,
TCP/IP, or USB, you can choose normal transfers or 488.2-defined strings. In USBTMC,
you can choose normal or vendor-specific transfers. The default is Normal.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


 Normal                                                                    1

 VXI/FDC                                                                   2

 GPIB/HS488                                                                3

 Serial-TCPIP-USB/488 Strings                                                 4

 USBTMC/Vendor-Specific                                                    5

MessageMessage BasedBased Settings:IsSettings:Is 488.2488.2 CompliantCompliant

Returns whether the device is 488.2 compliant.


                                                    © National Instruments 10357

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10357 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10358 ordinal=10358 -->
## Property and Method Reference

Property and Method Reference

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    MessageMessage BasedBased Settings:SendSettings:Send EndEnd EnableEnable

         Specifies whether to send an END indicator on the last byte of each write operation.
        This property is relevant only in VISA Write and related operations. The default is TRUE.
      On Serial Instr sessions, if this property is set to FALSE, the write transmits the exact
        contents of the user buffer, without modifying it and without appending anything to
        the data. If this property is set to TRUE, VISA performs the behavior described in the
        property End Mode for Writes (ASRL End Out). On GPIB, VXI, GPIB-VXI, TCP/IP Instr, and
      USB Instr sessions, if this property is set to TRUE, VISA includes the 488.2 defined end
         of message terminator.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes


10358   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10358 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10359 ordinal=10359 -->
## Property and Method Reference

Property and Method Reference

MessageMessage BasedBased Settings:TerminationSettings:Termination
CharacterCharacter

Specifies a character that, when read, causes a read operation to terminate. The
termination character also must be enabled. This default is 0x0A (linefeed).

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

MessageMessage BasedBased Settings:TerminationSettings:Termination
CharacterCharacter EnableEnable

Specifies whether a read operation terminates when it receives the termination
character. The default is FALSE.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


                                                    © National Instruments 10359

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10359 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10360 ordinal=10360 -->
## Property and Method Reference

Property and Method Reference

   USBUSB Settings:MaximumSettings:Maximum InterruptInterrupt SizeSize

         Specifies the maximum size of data stored by any given USB interrupt. If a USB
         interrupt contains more data than this size, the data in excess of this size is lost. This
        property is read/write when the corresponding session is not enabled to receive USB
         interrupt events. When the session is enabled to receive USB interrupt events, this
        property is read only.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

   USBUSB Settings:SerialSettings:Serial NumberNumber

        Returns the USB serial number of this device.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


10360   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10360 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10361 ordinal=10361 -->
## Property and Method Reference

Property and Method Reference

USBUSB Settings:USBSettings:USB InterfaceInterface NumberNumber

Returns the USB interface number used by the given session.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

USBUSB Settings:USBSettings:USB ProtocolProtocol

Returns the USB protocol used by the given session.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
IdentificationIdentification

Returns a value that corresponds to the VXI manufacturer ID of the manufacturer that


                                                    © National Instruments 10361

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10361 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10362 ordinal=10362 -->
## Property and Method Reference

Property and Method Reference

        created the VISA implementation.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
   NameName

        Returns the name of the manufacturer that created the implementation. This is not
         related to the device manufacturer attributes. Note: Use the value of this property for
         display purposes only and not for programmatic decisions. The value can change
       between VISA implementations and/or revisions.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


10362   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10362 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10363 ordinal=10363 -->
## Property and Method Reference

Property and Method Reference

VersionVersion Information:VersionInformation:Version ofof
ImplementationImplementation

Returns the version of a given implementation. This value is defined by the individual
manufacturer and increments with each new revision. The format of the value has the
upper 12 bits as the major number of the version, the next lower 12 bits as the minor
number of the version, and the lowest 8 bits as the sub-minor number of the version.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VersionVersion Information:VersionInformation:Version ofof SpecificationSpecification

Returns the value that uniquely identifies the version of the VISA specification to which
the implementation complies. The format of the value has the upper 12 bits as the
major number of the version, the next lower 12 bits as the minor number of the
version, and the lowest 8 bits as the sub-minor number of the version.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes


                                                    © National Instruments 10363

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10363 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10364 ordinal=10364 -->
## Property and Method Reference

Property and Method Reference


           Available in Real-Time Operating System                                   Yes

     USBUSB RawRaw PropertiesProperties


          Property              Description

                                Returns the ID of the manufacturer that created the device. For VXI
          General                resources, this refers to the VXI Manufacturer ID. For PXI/PCI resources, this
           Settings:Manufacturer  refers to the Subsystem Vendor ID (SVID) if it is nonzero; otherwise, this
            Identification           refers to the Vendor ID (VID). For USB resources, this refers to the Vendor ID
                                       (VID).

                                Returns the name of the manufacturer that created the device. Note: Use          General                                the value of this property for display purposes only and not for           Settings:Manufacturer                             programmatic decisions. The value can change between VISA
        Name                               implementations and/or revisions.

          General                Specifies the maximum number of events that can be queued at any time
          Settings:Maximum    on the given session. This property is read/write until the first time you call
        Queue Length         VISA Enable Event on a session. Thereafter, it is read only. The default is 50.

                                Returns the device model code assigned by the manufacturer. For VXI
                                  resources, this refers to the VXI Model Code. For PXI/PCI resources, if the
          General                             Subsystem Vendor ID is nonzero, this refers to the Subsystem ID (SSID);          Settings:Model Code
                                 otherwise, this refers to the Device ID (DID). For USB resources, this refers to
                                the Product ID (PID).

                                Returns the model name of the device. Note: Use the value of this property          General                                     for display purposes only and not for programmatic decisions. The value          Settings:Model Name
                             can change between VISA implementations and/or revisions.

                                Returns the resource class of the resource string used to open the given
          General
                                   session. For example, if the resource string for a given session is COM1 or
           Settings:Resource
                                ASRL1::INSTR, this property returns INSTR, regardless of the class of the I/O
           Class
                                    control.

          General              Returns the current locking state of the resource associated with the given
           Settings:Resource      session. The resource can be unlocked, locked with an exclusive lock, or
         Lock State            locked with a shared lock. The default is Unlocked.

          General
           Settings:Resource     Returns the unique identifier for a resource.
        Name

          General                Specifies the minimum timeout value, in milliseconds, to use when


10364   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10364 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10365 ordinal=10365 -->
## Property and Method Reference

Property and Method Reference


Property              Description

Settings:Timeout      accessing the device. Note that the actual timeout that VISA returns may be
Value                 higher than the one requested. The default is 2000.

                        Specifies a data value for the private use of an application. The VISA
General Settings:User  implementation stores this value in a per-session location, so that user data
Data               on other sessions does not affect the user data on this session. VISA does
                     not use this property for any purpose.

                        Specifies human-readable text that describes the given interface. Note: UseInterface                      the value of this property for display purposes only and not forInformation:Interface
                    programmatic decisions. The value can change between VISADescription                     implementations and/or revisions.

Interface
Information:Interface  Returns the board number for the given interface.
Number

Interface
Information:Interface  Specifies the interface type of the given session.
Type

                        Specifies which protocol to use. In VXI, you can choose normal word serial
                      or fast data channel. In GPIB, you can choose normal or high-speed HS-488Message Based                         transfers. In serial, TCP/IP, or USB, you can choose normal transfers or
Settings:IO Protocol                       488.2-defined strings. In USBTMC, you can choose normal or vendor-
                         specific transfers. The default is Normal.

                        Specifies whether to terminate a read operation due to an END condition.
                       This property is relevant only in VISA Read and related operations. For all
                       session types that support this property, if this property is set to TRUE, read
                    does not terminate due to an END condition. However, a read may still
                      terminate successfully if the Message Based Settings:Termination Character
                     Enable (TermChar En) property is set to TRUE. Otherwise, read does not
                      terminate until it receives all of the requested data (or an error occurs). The
Message Based         default is FALSE (except for TCP/IP Socket sessions). On Serial Instr
Settings:Suppress      sessions, if this property is set to FALSE, VISA performs the behavior
End Enable           described in the Serial Settings:End Mode for Reads (ASRL End In) property.
                On USB Raw sessions, if this property is set to FALSE, VISA performs the
                     behavior described in the USB Settings:End Mode for Reads (USB End In)
                       property. On TCP/IP Socket sessions, if this property is set to FALSE, if NI-
                     VISA reads some data and then detects a pause in the arrival of data
                       packets, it terminates the read operation. On TCP/IP Socket sessions, the
                       default value for the property is TRUE in NI-VISA. On VXI Instr sessions, if
                          this property is set to FALSE, the END bit terminates read operations.


                                                    © National Instruments 10365

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10365 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10366 ordinal=10366 -->
## Property and Method Reference

Property and Method Reference


          Property              Description

         Message Based         Specifies a character that, when read, causes a read operation to terminate.
           Settings:Termination  The termination character also must be enabled. This default is 0x0A
          Character               (linefeed).

         Message Based                                   Specifies whether a read operation terminates when it receives the
           Settings:Termination                                termination character. The default is FALSE.          Character Enable

        USB                                   Specifies the USB alternate setting used by this USB interface. The default is           Settings:Alternate                                       0.
           Setting

                                   Specifies the endpoint number of the USB bulk-in pipe used by the given
        USB Settings:Bulk-In   session. An initial value of -1 signifies that this resource does not have any
          Pipe                   bulk-in pipes. Other valid values are 129 to 143 (0x81 to 0x8f). VISA Read
                           and related operations use this endpoint.

        USB Settings:Bulk-In   Specifies whether the USB bulk-in pipe used by the given session is stalled
          Pipe Status            or ready.

                                   Specifies the endpoint number of the USB bulk-out or interrupt-out pipe
        USB Settings:Bulk-    used by the given session. An initial value of -1 signifies that this resource
         Out Pipe             does not have any bulk-out or interrupt-out pipes. Other valid values are 1
                                  to 15 (0x01 to 0x0f). VISA Write and related operations use this endpoint.

        USB Settings:Bulk-     Specifies whether the USB bulk-out or interrupt-out pipe used by the given
         Out Pipe Status        session is stalled or ready.

                                   Specifies the endpoint address of the USB control pipe used by the given
                                   session. A value of 0 signifies the session will use the default control pipe.
        USB Settings:Control                                 This endpoint is used in VISA USB Control In and VISA USB Control Out          Pipe                                  operations. Valid values are 0 to 15 (0x00 to 0x0f). Non-zero values may not
                            be supported on all platforms. The default is 0.

                                   Specifies the method used to terminate read operations. Valid values
                                   include: (0) End None, (4) End Short, (5) End Short or Count. Use (0) End
        USB Settings:End     None to receive all requested data bytes regardless of any short packets.
        Mode for Reads       Use (4) End Short if the device sends a zero (short) packet when the last
                               data packet is full. Use (5) End Short or Count if the device does not send
                                 zero packets. The default is (5) End Short or Count.

                                   Specifies the endpoint number of the USB interrupt-in pipe used by the
        USB
                                given session. An initial value of -1 signifies that this resource does not have
            Settings:Interrupt-In
                             any interrupt-in pipes. Other valid values are 129 to 143 (0x81 to 0x8f). VISA
          Pipe
                              Enable Event uses this endpoint for the USB Interrupt Event.


10366   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10366 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10367 ordinal=10367 -->
## Property and Method Reference

Property and Method Reference


Property              Description

USB                        Specifies whether the USB interrupt-in pipe used by the given session isSettings:Interrupt-In                         stalled or ready.Pipe Status

                        Specifies the maximum size of data stored by any given USB interrupt. If a
USB              USB interrupt contains more data than this size, the data in excess of this
Settings:Maximum      size is lost. This property is read/write when the corresponding session is
Interrupt Size         not enabled to receive USB interrupt events. When the session is enabled to
                       receive USB interrupt events, this property is read only.

USB Settings:Number                     Returns the number of interfaces supported by this USB device.of Interfaces

USB Settings:Number                     Returns the number of pipes supported by this USB interface.
of Pipes

USB Settings:Serial                     Returns the USB serial number of this device.
Number

USB Settings:USB                     Returns the USB class used by the given session.
Class

USB Settings:USB
                     Returns the USB interface number used by the given session.Interface Number

USB Settings:USB
                     Returns the USB protocol used by the given session.Protocol

USB Settings:USB
                     Returns the USB subclass used by the given session.Subclass

Version
Information:Resource  Returns a value that corresponds to the VXI manufacturer ID of the
Manufacturer         manufacturer that created the VISA implementation.
Identification

                     Returns the name of the manufacturer that created the implementation.
Version                This is not related to the device manufacturer attributes. Note: Use the
Information:Resource  value of this property for display purposes only and not for programmatic
Manufacturer Name    decisions. The value can change between VISA implementations and/or
                         revisions.

                     Returns the version of a given implementation. This value is defined by the
Version
                        individual manufacturer and increments with each new revision. The
Information:Version
                     format of the value has the upper 12 bits as the major number of the
of Implementation
                        version, the next lower 12 bits as the minor number of the version, and the


                                                    © National Instruments 10367

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10367 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10368 ordinal=10368 -->
## Property and Method Reference

Property and Method Reference


          Property              Description

                                lowest 8 bits as the sub-minor number of the version.

                                Returns the value that uniquely identifies the version of the VISA
           Version                 specification to which the implementation complies. The format of the
           Information:Version    value has the upper 12 bits as the major number of the version, the next
           of Specification       lower 12 bits as the minor number of the version, and the lowest 8 bits as
                                the sub-minor number of the version.

    GeneralGeneral Settings:ManufacturerSettings:Manufacturer IdentificationIdentification

        Returns the ID of the manufacturer that created the device. For VXI resources, this
         refers to the VXI Manufacturer ID. For PXI/PCI resources, this refers to the Subsystem
       Vendor ID (SVID) if it is nonzero; otherwise, this refers to the Vendor ID (VID). For USB
         resources, this refers to the Vendor ID (VID).

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    GeneralGeneral Settings:ManufacturerSettings:Manufacturer NameName

        Returns the name of the manufacturer that created the device. Note: Use the value of
          this property for display purposes only and not for programmatic decisions. The value
       can change between VISA implementations and/or revisions.

      Remarks

       The following table lists the characteristics of this property.


10368   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10368 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10369 ordinal=10369 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

GeneralGeneral Settings:MaximumSettings:Maximum QueueQueue LengthLength

Specifies the maximum number of events that can be queued at any time on the given
session. This property is read/write until the first time you call VISA Enable Event on a
session. Thereafter, it is read only. The default is 50.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

GeneralGeneral Settings:ModelSettings:Model CodeCode

Returns the device model code assigned by the manufacturer. For VXI resources, this
refers to the VXI Model Code. For PXI/PCI resources, if the Subsystem Vendor ID is
nonzero, this refers to the Subsystem ID (SSID); otherwise, this refers to the Device ID
(DID). For USB resources, this refers to the Product ID (PID).

Remarks

The following table lists the characteristics of this property.


 Data type

                                                    © National Instruments 10369

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10369 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10370 ordinal=10370 -->
## Property and Method Reference

Property and Method Reference


          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    GeneralGeneral Settings:ModelSettings:Model NameName

        Returns the model name of the device. Note: Use the value of this property for display
        purposes only and not for programmatic decisions. The value can change between
        VISA implementations and/or revisions.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    GeneralGeneral Settings:ResourceSettings:Resource ClassClass

        Returns the resource class of the resource string used to open the given session. For
        example, if the resource string for a given session is COM1 or ASRL1::INSTR, this
        property returns INSTR, regardless of the class of the I/O control.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

10370   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10370 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10371 ordinal=10371 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                                   Yes

GeneralGeneral Settings:ResourceSettings:Resource LockLock StateState

Returns the current locking state of the resource associated with the given session.
The resource can be unlocked, locked with an exclusive lock, or locked with a shared
lock. The default is Unlocked.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


 Unlocked                                                     0

 Exclusive                                                     1

 Shared                                                       2

GeneralGeneral Settings:ResourceSettings:Resource NameName

Returns the unique identifier for a resource.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only


                                                    © National Instruments 10371

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10371 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10372 ordinal=10372 -->
## Property and Method Reference

Property and Method Reference


           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    GeneralGeneral Settings:TimeoutSettings:Timeout ValueValue

         Specifies the minimum timeout value, in milliseconds, to use when accessing the
         device. Note that the actual timeout that VISA returns may be higher than the one
        requested. The default is 2000.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

    GeneralGeneral Settings:UserSettings:User DataData

         Specifies a data value for the private use of an application. The VISA implementation
         stores this value in a per-session location, so that user data on other sessions does not
         affect the user data on this session. VISA does not use this property for any purpose.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

10372   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10372 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10373 ordinal=10373 -->
## Property and Method Reference

Property and Method Reference

InterfaceInterface Information:InterfaceInformation:Interface DescriptionDescription

Specifies human-readable text that describes the given interface. Note: Use the value
of this property for display purposes only and not for programmatic decisions. The
value can change between VISA implementations and/or revisions.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

InterfaceInterface Information:InterfaceInformation:Interface NumberNumber

Returns the board number for the given interface.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

InterfaceInterface Information:InterfaceInformation:Interface TypeType

Specifies the interface type of the given session.


                                                    © National Instruments 10373

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10373 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10374 ordinal=10374 -->
## Property and Method Reference

Property and Method Reference

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


         GPIB                                                       1

          VXI                                                         2

          GPIB-VXI                                                    3

           Serial                                                       4

          PXI                                                         5

         TCPIP                                                      6

        USB                                                        7

          FireWire                                                    9

    MessageMessage BasedBased Settings:IOSettings:IO ProtocolProtocol

         Specifies which protocol to use. In VXI, you can choose normal word serial or fast data
        channel. In GPIB, you can choose normal or high-speed HS-488 transfers. In serial,
         TCP/IP, or USB, you can choose normal transfers or 488.2-defined strings. In USBTMC,
       you can choose normal or vendor-specific transfers. The default is Normal.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write


10374   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10374 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10375 ordinal=10375 -->
## Property and Method Reference

Property and Method Reference


 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


 Normal                                                                    1

 VXI/FDC                                                                   2

 GPIB/HS488                                                                3

 Serial-TCPIP-USB/488 Strings                                                 4

 USBTMC/Vendor-Specific                                                    5

MessageMessage BasedBased Settings:SuppressSettings:Suppress EndEnd
EnableEnable

Specifies whether to terminate a read operation due to an END condition. This
property is relevant only in VISA Read and related operations. For all session types that
support this property, if this property is set to TRUE, read does not terminate due to an
END condition. However, a read may still terminate successfully if the Message Based
Settings:Termination Character Enable (TermChar En) property is set to TRUE.
Otherwise, read does not terminate until it receives all of the requested data (or an
error occurs). The default is FALSE (except for TCP/IP Socket sessions). On Serial Instr
sessions, if this property is set to FALSE, VISA performs the behavior described in the
Serial Settings:End Mode for Reads (ASRL End In) property. On USB Raw sessions, if
this property is set to FALSE, VISA performs the behavior described in the USB
Settings:End Mode for Reads (USB End In) property. On TCP/IP Socket sessions, if this
property is set to FALSE, if NI-VISA reads some data and then detects a pause in the
arrival of data packets, it terminates the read operation. On TCP/IP Socket sessions,
the default value for the property is TRUE in NI-VISA. On VXI Instr sessions, if this
property is set to FALSE, the END bit terminates read operations.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 10375

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10375 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10376 ordinal=10376 -->
## Property and Method Reference

Property and Method Reference


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

    MessageMessage BasedBased Settings:TerminationSettings:Termination
    CharacterCharacter

         Specifies a character that, when read, causes a read operation to terminate. The
        termination character also must be enabled. This default is 0x0A (linefeed).

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

    MessageMessage BasedBased Settings:TerminationSettings:Termination
    CharacterCharacter EnableEnable

         Specifies whether a read operation terminates when it receives the termination
         character. The default is FALSE.

      Remarks

       The following table lists the characteristics of this property.


10376   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10376 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10377 ordinal=10377 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

USBUSB Settings:AlternateSettings:Alternate SettingSetting

Specifies the USB alternate setting used by this USB interface. The default is 0.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

USBUSB Settings:Bulk-InSettings:Bulk-In PipePipe

Specifies the endpoint number of the USB bulk-in pipe used by the given session. An
initial value of -1 signifies that this resource does not have any bulk-in pipes. Other
valid values are 129 to 143 (0x81 to 0x8f). VISA Read and related operations use this
endpoint.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write


                                                    © National Instruments 10377

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10377 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10378 ordinal=10378 -->
## Property and Method Reference

Property and Method Reference


           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

   USBUSB Settings:Bulk-InSettings:Bulk-In PipePipe StatusStatus

         Specifies whether the USB bulk-in pipe used by the given session is stalled or ready.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes


        Unknown                                                             -1

         Ready                                                     0

           Stalled                                                    1

   USBUSB Settings:Bulk-OutSettings:Bulk-Out PipePipe

         Specifies the endpoint number of the USB bulk-out or interrupt-out pipe used by the
        given session. An initial value of -1 signifies that this resource does not have any bulk-
        out or interrupt-out pipes. Other valid values are 1 to 15 (0x01 to 0x0f). VISA Write and
         related operations use this endpoint.

      Remarks

       The following table lists the characteristics of this property.


10378   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10378 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10379 ordinal=10379 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

USBUSB Settings:Bulk-OutSettings:Bulk-Out PipePipe StatusStatus

Specifies whether the USB bulk-out or interrupt-out pipe used by the given session is
stalled or ready.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


 Unknown                                                             -1

 Ready                                                     0

 Stalled                                                    1

USBUSB Settings:ControlSettings:Control PipePipe

Specifies the endpoint address of the USB control pipe used by the given session. A
value of 0 signifies the session will use the default control pipe. This endpoint is used
in VISA USB Control In and VISA USB Control Out operations. Valid values are 0 to 15
(0x00 to 0x0f). Non-zero values may not be supported on all platforms. The default is 0.


                                                    © National Instruments 10379

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10379 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10380 ordinal=10380 -->
## Property and Method Reference

Property and Method Reference

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

   USBUSB Settings:EndSettings:End ModeMode forfor ReadsReads

         Specifies the method used to terminate read operations. Valid values include: (0) End
       None, (4) End Short, (5) End Short or Count. Use (0) End None to receive all requested
        data bytes regardless of any short packets. Use (4) End Short if the device sends a zero
         (short) packet when the last data packet is full. Use (5) End Short or Count if the device
       does not send zero packets. The default is (5) End Short or Count.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes


        None                                                              0

          Short                                                              4

          Short or Count                                                      5


10380   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10380 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10381 ordinal=10381 -->
## Property and Method Reference

Property and Method Reference

USBUSB Settings:Interrupt-InSettings:Interrupt-In PipePipe

Specifies the endpoint number of the USB interrupt-in pipe used by the given session.
An initial value of -1 signifies that this resource does not have any interrupt-in pipes.
Other valid values are 129 to 143 (0x81 to 0x8f). VISA Enable Event uses this endpoint
for the USB Interrupt Event.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

USBUSB Settings:Interrupt-InSettings:Interrupt-In PipePipe StatusStatus

Specifies whether the USB interrupt-in pipe used by the given session is stalled or
ready.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


 Unknown                                                             -1


                                                    © National Instruments 10381

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10381 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10382 ordinal=10382 -->
## Property and Method Reference

Property and Method Reference


         Ready                                                     0

           Stalled                                                    1

   USBUSB Settings:MaximumSettings:Maximum InterruptInterrupt SizeSize

         Specifies the maximum size of data stored by any given USB interrupt. If a USB
         interrupt contains more data than this size, the data in excess of this size is lost. This
        property is read/write when the corresponding session is not enabled to receive USB
         interrupt events. When the session is enabled to receive USB interrupt events, this
        property is read only.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

   USBUSB Settings:NumberSettings:Number ofof InterfacesInterfaces

        Returns the number of interfaces supported by this USB device.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

10382   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10382 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10383 ordinal=10383 -->
## Property and Method Reference

Property and Method Reference

USBUSB Settings:NumberSettings:Number ofof PipesPipes

Returns the number of pipes supported by this USB interface.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

USBUSB Settings:SerialSettings:Serial NumberNumber

Returns the USB serial number of this device.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

USBUSB Settings:USBSettings:USB ClassClass

Returns the USB class used by the given session.


                                                    © National Instruments 10383

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10383 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10384 ordinal=10384 -->
## Property and Method Reference

Property and Method Reference

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

   USBUSB Settings:USBSettings:USB InterfaceInterface NumberNumber

        Returns the USB interface number used by the given session.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

   USBUSB Settings:USBSettings:USB ProtocolProtocol

        Returns the USB protocol used by the given session.

      Remarks

       The following table lists the characteristics of this property.


          Data type


10384   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10384 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10385 ordinal=10385 -->
## Property and Method Reference

Property and Method Reference


 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

USBUSB Settings:USBSettings:USB SubclassSubclass

Returns the USB subclass used by the given session.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
IdentificationIdentification

Returns a value that corresponds to the VXI manufacturer ID of the manufacturer that
created the VISA implementation.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes


                                                    © National Instruments 10385

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10385 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10386 ordinal=10386 -->
## Property and Method Reference

Property and Method Reference


           Available in Real-Time Operating System                                   Yes

    VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
   NameName

        Returns the name of the manufacturer that created the implementation. This is not
         related to the device manufacturer attributes. Note: Use the value of this property for
         display purposes only and not for programmatic decisions. The value can change
       between VISA implementations and/or revisions.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    VersionVersion Information:VersionInformation:Version ofof
    ImplementationImplementation

        Returns the version of a given implementation. This value is defined by the individual
        manufacturer and increments with each new revision. The format of the value has the
       upper 12 bits as the major number of the version, the next lower 12 bits as the minor
       number of the version, and the lowest 8 bits as the sub-minor number of the version.

      Remarks

       The following table lists the characteristics of this property.


10386   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10386 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10387 ordinal=10387 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VersionVersion Information:VersionInformation:Version ofof SpecificationSpecification

Returns the value that uniquely identifies the version of the VISA specification to which
the implementation complies. The format of the value has the upper 12 bits as the
major number of the version, the next lower 12 bits as the minor number of the
version, and the lowest 8 bits as the sub-minor number of the version.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VXIVXI ServantServant PropertiesProperties


 Property             Description

                        Specifies whether I/O accesses should attempt to use DMA (TRUE) or
 General
                  Programmed I/O (FALSE). In some implementations, this property may have
 Settings:Allow DMA
                       global effects even though it is documented as a local property. This
 Transfers
                      behavior affects performance and not functionality.

 General                Specifies the maximum number of events that can be queued at any time
 Settings:Maximum    on the given session. This property is read/write until the first time you call
 Queue Length        VISA Enable Event on a session. Thereafter, it is read only. The default is 50.

 General              Returns the resource class of the resource string used to open the given


                                                    © National Instruments 10387

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10387 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10388 ordinal=10388 -->
## Property and Method Reference

Property and Method Reference


          Property             Description

                                   session. For example, if the resource string for a given session is COM1 or           Settings:Resource                                ASRL1::INSTR, this property returns INSTR, regardless of the class of the I/O           Class                                   control.

          General              Returns the current locking state of the resource associated with the given
           Settings:Resource     session. The resource can be unlocked, locked with an exclusive lock, or
         Lock State            locked with a shared lock. The default is Unlocked.

          General
           Settings:Resource     Returns the unique identifier for a resource.
        Name

          General                Specifies the minimum timeout value, in milliseconds, to use when
          Settings:Timeout      accessing the device. Note that the actual timeout that VISA returns may be
          Value                 higher than the one requested. The default is 2000.

                                   Specifies a data value for the private use of an application. The VISA
          General Settings:User  implementation stores this value in a per-session location, so that user data
          Data              on other sessions does not affect the user data on this session. VISA does
                               not use this property for any purpose.

                                   Specifies human-readable text that describes the given interface. Note: Use
           Interface                               the value of this property for display purposes only and not for           Information:Interface                             programmatic decisions. The value can change between VISA
           Description                              implementations and/or revisions.

           Interface
           Information:Interface  Returns the board number for the given interface.
        Number

           Interface
           Information:Interface  Specifies the interface type of the given session.
         Type

         Message Based        Specifies the 488-style status byte of the local controller or device
           Settings:Device       associated with this session. If you write this property and set bit 6 (0x40),
           Status Byte             this device or controller asserts a service request (SRQ) on the interface.

                                   Specifies whether VISA Read To File appends or overwrites (truncates) when
         Message Based
                             opening a file. If this property is set to TRUE, VISA Read To File appends
            Settings:File Append
                         when opening a file. If this property is set to FALSE, VISA Read To
          Enable
                                       File overwrites (truncates) when opening a file. The default is FALSE.

         Message Based        Specifies whether to send an END indicator on the last byte of each write
          Settings:Send End     operation. This property is relevant only in VISA Write and related
          Enable                operations. The default is TRUE. On Serial Instr sessions, if this property is


10388   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10388 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10389 ordinal=10389 -->
## Property and Method Reference

Property and Method Reference


Property             Description

                        set to FALSE, the write transmits the exact contents of the user buffer,
                     without modifying it and without appending anything to the data. If this
                     property is set to TRUE, VISA performs the behavior described in the
                     property End Mode for Writes (ASRL End Out). On GPIB, VXI, GPIB-VXI, TCP/
                       IP Instr, and USB Instr sessions, if this property is set to TRUE, VISA includes
                     the 488.2 defined end of message terminator.

Message Based        Specifies a character that, when read, causes a read operation to terminate.
Settings:Termination  The termination character also must be enabled. This default is 0x0A
Character               (linefeed).

Message Based                       Specifies whether a read operation terminates when it receives theSettings:Termination                      termination character. The default is FALSE.Character Enable

VXI/VME Settings:VXI
Commander Logical   Returns the logical address of the commander of the VXI device.
Address

VXI/VME Settings:VXI                     Returns the logical address of the VXI device.Logical Address

VXI/VME Settings:VXI/                     Returns the current state of the VXI/VME SYSFAIL (SYStem FAILure)VME System Failure
                    backplane line.State

Version
Information:Resource Returns a value that corresponds to the VXI manufacturer ID of the
Manufacturer         manufacturer that created the VISA implementation.
Identification

                     Returns the name of the manufacturer that created the implementation.
Version               This is not related to the device manufacturer attributes. Note: Use the
Information:Resource  value of this property for display purposes only and not for programmatic
Manufacturer Name   decisions. The value can change between VISA implementations and/or
                         revisions.

                     Returns the version of a given implementation. This value is defined by the
Version                individual manufacturer and increments with each new revision. The format
Information:Version   of the value has the upper 12 bits as the major number of the version, the
of Implementation    next lower 12 bits as the minor number of the version, and the lowest 8 bits
                     as the sub-minor number of the version.

Version              Returns the value that uniquely identifies the version of the VISA
Information:Version   specification to which the implementation complies. The format of the
of Specification       value has the upper 12 bits as the major number of the version, the next

                                                    © National Instruments 10389

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10389 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10390 ordinal=10390 -->
## Property and Method Reference

Property and Method Reference


          Property             Description

                               lower 12 bits as the minor number of the version, and the lowest 8 bits as
                               the sub-minor number of the version.

    GeneralGeneral Settings:AllowSettings:Allow DMADMA TransfersTransfers

         Specifies whether I/O accesses should attempt to use DMA (TRUE) or Programmed I/O
         (FALSE). In some implementations, this property may have global effects even though
             it is documented as a local property. This behavior affects performance and not
         functionality.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

    GeneralGeneral Settings:MaximumSettings:Maximum QueueQueue LengthLength

         Specifies the maximum number of events that can be queued at any time on the given
         session. This property is read/write until the first time you call VISA Enable Event on a
         session. Thereafter, it is read only. The default is 50.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write


10390   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10390 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10391 ordinal=10391 -->
## Property and Method Reference

Property and Method Reference


 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

GeneralGeneral Settings:ResourceSettings:Resource ClassClass

Returns the resource class of the resource string used to open the given session. For
example, if the resource string for a given session is COM1 or ASRL1::INSTR, this
property returns INSTR, regardless of the class of the I/O control.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

GeneralGeneral Settings:ResourceSettings:Resource LockLock StateState

Returns the current locking state of the resource associated with the given session.
The resource can be unlocked, locked with an exclusive lock, or locked with a shared
lock. The default is Unlocked.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

                                                    © National Instruments 10391

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10391 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10392 ordinal=10392 -->
## Property and Method Reference

Property and Method Reference


         Unlocked                                                     0

           Exclusive                                                     1

         Shared                                                       2

    GeneralGeneral Settings:ResourceSettings:Resource NameName

        Returns the unique identifier for a resource.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    GeneralGeneral Settings:TimeoutSettings:Timeout ValueValue

         Specifies the minimum timeout value, in milliseconds, to use when accessing the
         device. Note that the actual timeout that VISA returns may be higher than the one
        requested. The default is 2000.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes


10392   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10392 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10393 ordinal=10393 -->
## Property and Method Reference

Property and Method Reference

GeneralGeneral Settings:UserSettings:User DataData

Specifies a data value for the private use of an application. The VISA implementation
stores this value in a per-session location, so that user data on other sessions does not
affect the user data on this session. VISA does not use this property for any purpose.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

InterfaceInterface Information:InterfaceInformation:Interface DescriptionDescription

Specifies human-readable text that describes the given interface. Note: Use the value
of this property for display purposes only and not for programmatic decisions. The
value can change between VISA implementations and/or revisions.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


                                                    © National Instruments 10393

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10393 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10394 ordinal=10394 -->
## Property and Method Reference

Property and Method Reference

     InterfaceInterface Information:InterfaceInformation:Interface NumberNumber

        Returns the board number for the given interface.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

     InterfaceInterface Information:InterfaceInformation:Interface TypeType

         Specifies the interface type of the given session.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


         GPIB                                                       1

          VXI                                                         2

          GPIB-VXI                                                    3

           Serial                                                       4


10394   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10394 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10395 ordinal=10395 -->
## Property and Method Reference

Property and Method Reference


 PXI                                                         5

 TCPIP                                                      6

 USB                                                        7

 FireWire                                                    9

MessageMessage BasedBased Settings:DeviceSettings:Device StatusStatus ByteByte

Specifies the 488-style status byte of the local controller or device associated with this
session. If you write this property and set bit 6 (0x40), this device or controller asserts a
service request (SRQ) on the interface.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

MessageMessage BasedBased Settings:FileSettings:File AppendAppend EnableEnable

Specifies whether VISA Read To File appends or overwrites (truncates) when opening a
file. If this property is set to TRUE, VISA Read To File appends when opening a file. If
this property is set to FALSE, VISA Read To File overwrites (truncates) when opening a
file. The default is FALSE.

Remarks

The following table lists the characteristics of this property.


 Data type


                                                    © National Instruments 10395

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10395 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10396 ordinal=10396 -->
## Property and Method Reference

Property and Method Reference


          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

    MessageMessage BasedBased Settings:SendSettings:Send EndEnd EnableEnable

         Specifies whether to send an END indicator on the last byte of each write operation.
        This property is relevant only in VISA Write and related operations. The default is TRUE.
      On Serial Instr sessions, if this property is set to FALSE, the write transmits the exact
        contents of the user buffer, without modifying it and without appending anything to
        the data. If this property is set to TRUE, VISA performs the behavior described in the
        property End Mode for Writes (ASRL End Out). On GPIB, VXI, GPIB-VXI, TCP/IP Instr, and
      USB Instr sessions, if this property is set to TRUE, VISA includes the 488.2 defined end
         of message terminator.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

    MessageMessage BasedBased Settings:TerminationSettings:Termination
    CharacterCharacter

         Specifies a character that, when read, causes a read operation to terminate. The
        termination character also must be enabled. This default is 0x0A (linefeed).


10396   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10396 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10397 ordinal=10397 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

MessageMessage BasedBased Settings:TerminationSettings:Termination
CharacterCharacter EnableEnable

Specifies whether a read operation terminates when it receives the termination
character. The default is FALSE.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

VXI/VMEVXI/VME Settings:VXISettings:VXI CommanderCommander LogicalLogical
AddressAddress

Returns the logical address of the commander of the VXI device.


                                                    © National Instruments 10397

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10397 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10398 ordinal=10398 -->
## Property and Method Reference

Property and Method Reference

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    VXI/VMEVXI/VME Settings:VXISettings:VXI LogicalLogical AddressAddress

        Returns the logical address of the VXI device.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    VXI/VMEVXI/VME Settings:VXI/VMESettings:VXI/VME SystemSystem FailureFailure
     StateState

        Returns the current state of the VXI/VME SYSFAIL (SYStem FAILure) backplane line.

      Remarks

       The following table lists the characteristics of this property.


10398   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10398 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10399 ordinal=10399 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


 Unknown                                                                 -1

 Unasserted                                                   0

 Asserted                                                     1

VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
IdentificationIdentification

Returns a value that corresponds to the VXI manufacturer ID of the manufacturer that
created the VISA implementation.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
NameName

Returns the name of the manufacturer that created the implementation. This is not
related to the device manufacturer attributes. Note: Use the value of this property for

                                                    © National Instruments 10399

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10399 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10400 ordinal=10400 -->
## Property and Method Reference

Property and Method Reference

         display purposes only and not for programmatic decisions. The value can change
       between VISA implementations and/or revisions.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    VersionVersion Information:VersionInformation:Version ofof
    ImplementationImplementation

        Returns the version of a given implementation. This value is defined by the individual
        manufacturer and increments with each new revision. The format of the value has the
       upper 12 bits as the major number of the version, the next lower 12 bits as the minor
       number of the version, and the lowest 8 bits as the sub-minor number of the version.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


10400   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10400 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10401 ordinal=10401 -->
## Property and Method Reference

Property and Method Reference

VersionVersion Information:VersionInformation:Version ofof SpecificationSpecification

Returns the value that uniquely identifies the version of the VISA specification to which
the implementation complies. The format of the value has the upper 12 bits as the
major number of the version, the next lower 12 bits as the minor number of the
version, and the lowest 8 bits as the sub-minor number of the version.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VXI/GPIB-VXIVXI/GPIB-VXI BackplaneBackplane PropertiesProperties


 Property             Description

 GPIB
 Settings:Primary      Returns the primary address of the GPIB device used by the given session.
 Address

 GPIB                 Returns the secondary address of the GPIB device used by the given
 Settings:Secondary    session. If the device does not have a secondary address, the value of this
 Address              property is 65535 (0xFFFF).

 General                Specifies the maximum number of events that can be queued at any time
 Settings:Maximum    on the given session. This property is read/write until the first time you call
 Queue Length        VISA Enable Event on a session. Thereafter, it is read only. The default is 50.

                      Returns the resource class of the resource string used to open the given
 General
                        session. For example, if the resource string for a given session is COM1 or
 Settings:Resource
                      ASRL1::INSTR, this property returns INSTR, regardless of the class of the I/O
 Class
                         control.

 General              Returns the current locking state of the resource associated with the given
 Settings:Resource     session. The resource can be unlocked, locked with an exclusive lock, or

                                                    © National Instruments 10401

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10401 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10402 ordinal=10402 -->
## Property and Method Reference

Property and Method Reference


          Property             Description

         Lock State            locked with a shared lock. The default is Unlocked.

          General
           Settings:Resource     Returns the unique identifier for a resource.
        Name

          General                Specifies the minimum timeout value, in milliseconds, to use when
          Settings:Timeout      accessing the device. Note that the actual timeout that VISA returns may be
          Value                 higher than the one requested. The default is 2000.

          General                Specifies which trigger mechanism to use. In VXI systems, for example, you
           Settings:Trigger      can choose between software triggers and hardware triggers on a specific
            Identifier               trigger line. The default is Software.

                                   Specifies a data value for the private use of an application. The VISA
          General Settings:User  implementation stores this value in a per-session location, so that user data
          Data              on other sessions does not affect the user data on this session. VISA does
                               not use this property for any purpose.

                                   Specifies human-readable text that describes the given interface. Note: Use           Interface
                               the value of this property for display purposes only and not for           Information:Interface                             programmatic decisions. The value can change between VISA
           Description                              implementations and/or revisions.

           Interface
           Information:Interface  Returns the board number for the given interface.
        Number

           Interface
           Information:Interface  Returns the board number of the parent device.
        Number of Parent

           Interface
           Information:Interface  Specifies the interface type of the given session.
         Type

          VXI/VME
                               Returns the current state of the VXI trigger lines. This property returns a bit
           Settings:Asserted VXI
                                 vector with bits 0-9 corresponding to TTL0 through ECL1.
           Trigger Lines

          VXI/VME
           Settings:Asserted     Returns the current state of the VXI/VME interrupt lines. This property
          VXI/VME Interrupt      returns a bit vector with bits 0-6 corresponding to interrupt lines 1-7.
           Lines

          VXI/VME              Returns the lowest logical address in the mainframe in which the device


10402   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10402 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10403 ordinal=10403 -->
## Property and Method Reference

Property and Method Reference


 Property             Description

 Settings:Mainframe                         resides. Logical Address

 VXI/VME                      Returns which VXI trigger lines this implementation supports. This property Settings:Supported                       returns a bit vector with bits 0-9 corresponding to TTL0 through ECL1.
 VXI Trigger Lines

 VXI/VME Settings:VXI/                      Returns the current state of the VXI/VME SYSFAIL (SYStem FAILure) VME System Failure                     backplane line. State

 Version
 Information:Resource Returns a value that corresponds to the VXI manufacturer ID of the
 Manufacturer         manufacturer that created the VISA implementation.
 Identification

                      Returns the name of the manufacturer that created the implementation.
 Version               This is not related to the device manufacturer attributes. Note: Use the
 Information:Resource  value of this property for display purposes only and not for programmatic
 Manufacturer Name   decisions. The value can change between VISA implementations and/or
                         revisions.

                      Returns the version of a given implementation. This value is defined by the
 Version                individual manufacturer and increments with each new revision. The format
 Information:Version   of the value has the upper 12 bits as the major number of the version, the
 of Implementation    next lower 12 bits as the minor number of the version, and the lowest 8 bits
                      as the sub-minor number of the version.

                      Returns the value that uniquely identifies the version of the VISA
 Version                specification to which the implementation complies. The format of the
 Information:Version   value has the upper 12 bits as the major number of the version, the next
 of Specification       lower 12 bits as the minor number of the version, and the lowest 8 bits as
                      the sub-minor number of the version.

GPIBGPIB Settings:PrimarySettings:Primary AddressAddress

Returns the primary address of the GPIB device used by the given session.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 10403

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10403 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10404 ordinal=10404 -->
## Property and Method Reference

Property and Method Reference


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    GPIBGPIB Settings:SecondarySettings:Secondary AddressAddress

        Returns the secondary address of the GPIB device used by the given session. If the
        device does not have a secondary address, the value of this property is 65535 (0xFFFF).

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    GeneralGeneral Settings:MaximumSettings:Maximum QueueQueue LengthLength

         Specifies the maximum number of events that can be queued at any time on the given
         session. This property is read/write until the first time you call VISA Enable Event on a
         session. Thereafter, it is read only. The default is 50.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write


10404   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10404 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10405 ordinal=10405 -->
## Property and Method Reference

Property and Method Reference


 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

GeneralGeneral Settings:ResourceSettings:Resource ClassClass

Returns the resource class of the resource string used to open the given session. For
example, if the resource string for a given session is COM1 or ASRL1::INSTR, this
property returns INSTR, regardless of the class of the I/O control.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

GeneralGeneral Settings:ResourceSettings:Resource LockLock StateState

Returns the current locking state of the resource associated with the given session.
The resource can be unlocked, locked with an exclusive lock, or locked with a shared
lock. The default is Unlocked.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

                                                    © National Instruments 10405

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10405 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10406 ordinal=10406 -->
## Property and Method Reference

Property and Method Reference


         Unlocked                                                     0

           Exclusive                                                     1

         Shared                                                       2

    GeneralGeneral Settings:ResourceSettings:Resource NameName

        Returns the unique identifier for a resource.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    GeneralGeneral Settings:TimeoutSettings:Timeout ValueValue

         Specifies the minimum timeout value, in milliseconds, to use when accessing the
         device. Note that the actual timeout that VISA returns may be higher than the one
        requested. The default is 2000.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes


10406   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10406 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10407 ordinal=10407 -->
## Property and Method Reference

Property and Method Reference

GeneralGeneral Settings:TriggerSettings:Trigger IdentifierIdentifier

Specifies which trigger mechanism to use. In VXI systems, for example, you can choose
between software triggers and hardware triggers on a specific trigger line. The default
is Software.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


 Software                                                             -1

 TTL0                                                     0

 TTL1                                                     1

 TTL2                                                     2

 TTL3                                                     3

 TTL4                                                     4

 TTL5                                                     5

 TTL6                                                     6

 TTL7                                                     7

 ECL0                                                     8

 ECL1                                                     9

GeneralGeneral Settings:UserSettings:User DataData

Specifies a data value for the private use of an application. The VISA implementation

                                                    © National Instruments 10407

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10407 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10408 ordinal=10408 -->
## Property and Method Reference

Property and Method Reference

         stores this value in a per-session location, so that user data on other sessions does not
         affect the user data on this session. VISA does not use this property for any purpose.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

     InterfaceInterface Information:InterfaceInformation:Interface DescriptionDescription

         Specifies human-readable text that describes the given interface. Note: Use the value
         of this property for display purposes only and not for programmatic decisions. The
        value can change between VISA implementations and/or revisions.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

     InterfaceInterface Information:InterfaceInformation:Interface NumberNumber

        Returns the board number for the given interface.


10408   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10408 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10409 ordinal=10409 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

InterfaceInterface Information:InterfaceInformation:Interface NumberNumber ofof
ParentParent

Returns the board number of the parent device.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

InterfaceInterface Information:InterfaceInformation:Interface TypeType

Specifies the interface type of the given session.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 10409

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10409 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10410 ordinal=10410 -->
## Property and Method Reference

Property and Method Reference


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


         GPIB                                                       1

          VXI                                                         2

          GPIB-VXI                                                    3

           Serial                                                       4

          PXI                                                         5

         TCPIP                                                      6

        USB                                                        7

          FireWire                                                    9

    VXI/VMEVXI/VME Settings:AssertedSettings:Asserted VXIVXI TriggerTrigger LinesLines

        Returns the current state of the VXI trigger lines. This property returns a bit vector with
          bits 0-9 corresponding to TTL0 through ECL1.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


10410   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10410 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10411 ordinal=10411 -->
## Property and Method Reference

Property and Method Reference

VXI/VMEVXI/VME Settings:AssertedSettings:Asserted VXI/VMEVXI/VME InterruptInterrupt
LinesLines

Returns the current state of the VXI/VME interrupt lines. This property returns a bit
vector with bits 0-6 corresponding to interrupt lines 1-7.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VXI/VMEVXI/VME Settings:MainframeSettings:Mainframe LogicalLogical AddressAddress

Returns the lowest logical address in the mainframe in which the device resides.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


                                                    © National Instruments 10411

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10411 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10412 ordinal=10412 -->
## Property and Method Reference

Property and Method Reference

    VXI/VMEVXI/VME Settings:SupportedSettings:Supported VXIVXI TriggerTrigger LinesLines

        Returns which VXI trigger lines this implementation supports. This property returns a
          bit vector with bits 0-9 corresponding to TTL0 through ECL1.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    VXI/VMEVXI/VME Settings:VXI/VMESettings:VXI/VME SystemSystem FailureFailure
     StateState

        Returns the current state of the VXI/VME SYSFAIL (SYStem FAILure) backplane line.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


        Unknown                                                                 -1

          Unasserted                                                   0


10412   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10412 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10413 ordinal=10413 -->
## Property and Method Reference

Property and Method Reference


 Asserted                                                     1

VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
IdentificationIdentification

Returns a value that corresponds to the VXI manufacturer ID of the manufacturer that
created the VISA implementation.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
NameName

Returns the name of the manufacturer that created the implementation. This is not
related to the device manufacturer attributes. Note: Use the value of this property for
display purposes only and not for programmatic decisions. The value can change
between VISA implementations and/or revisions.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

                                                    © National Instruments 10413

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10413 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10414 ordinal=10414 -->
## Property and Method Reference

Property and Method Reference


           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    VersionVersion Information:VersionInformation:Version ofof
    ImplementationImplementation

        Returns the version of a given implementation. This value is defined by the individual
        manufacturer and increments with each new revision. The format of the value has the
       upper 12 bits as the major number of the version, the next lower 12 bits as the minor
       number of the version, and the lowest 8 bits as the sub-minor number of the version.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    VersionVersion Information:VersionInformation:Version ofof SpecificationSpecification

        Returns the value that uniquely identifies the version of the VISA specification to which
        the implementation complies. The format of the value has the upper 12 bits as the
       major number of the version, the next lower 12 bits as the minor number of the
         version, and the lowest 8 bits as the sub-minor number of the version.

      Remarks

       The following table lists the characteristics of this property.


          Data type

10414   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10414 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10415 ordinal=10415 -->
## Property and Method Reference

Property and Method Reference


 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VXI/GPIB-VXIVXI/GPIB-VXI MBDMBD InstrInstr PropertiesProperties


 Property              Description

 GPIB Settings:Line                       Returns the current state of the GPIB REN (Remote ENable) interface line. REN State

 GPIB Settings:Primary
                       Returns the primary address of the GPIB device used by the given session. Address

 GPIB                   Specifies whether to use repeat addressing before each read or write
 Settings:Readdressing  operation. The default is TRUE.

 GPIB                 Returns the secondary address of the GPIB device used by the given
 Settings:Secondary     session. If the device does not have a secondary address, the value of this
 Address               property is 65535 (0xFFFF).

 GPIB                   Specifies whether to unaddress the device (UNT and UNL) after each read
 Settings:Unaddressing  or write operation. The default is FALSE.

                         Specifies whether I/O accesses should attempt to use DMA (TRUE) or
 General Settings:Allow Programmed I/O (FALSE). In some implementations, this property may
 DMA Transfers        have global effects even though it is documented as a local property. This
                       behavior affects performance and not functionality.

                       Returns the ID of the manufacturer that created the device. For VXI
 General                resources, this refers to the VXI Manufacturer ID. For PXI/PCI resources, this
 Settings:Manufacturer  refers to the Subsystem Vendor ID (SVID) if it is nonzero; otherwise, this
 Identification           refers to the Vendor ID (VID). For USB resources, this refers to the Vendor ID
                            (VID).

                       Returns the name of the manufacturer that created the device. Note: Use
 General
                       the value of this property for display purposes only and not for
 Settings:Manufacturer
                     programmatic decisions. The value can change between VISA
 Name
                      implementations and/or revisions.

 General                 Specifies the maximum number of events that can be queued at any time
 Settings:Maximum    on the given session. This property is read/write until the first time you call
 Queue Length         VISA Enable Event on a session. Thereafter, it is read only. The default is 50.

 General               Returns the device model code assigned by the manufacturer. For VXI

                                                    © National Instruments 10415

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10415 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10416 ordinal=10416 -->
## Property and Method Reference

Property and Method Reference


          Property              Description

                                   resources, this refers to the VXI Model Code. For PXI/PCI resources, if the
                             Subsystem Vendor ID is nonzero, this refers to the Subsystem ID (SSID);          Settings:Model Code                                  otherwise, this refers to the Device ID (DID). For USB resources, this refers
                                  to the Product ID (PID).

                                Returns the model name of the device. Note: Use the value of this property          General                                      for display purposes only and not for programmatic decisions. The value          Settings:Model Name                              can change between VISA implementations and/or revisions.

                                Returns the resource class of the resource string used to open the given          General
                                   session. For example, if the resource string for a given session is COM1 or           Settings:Resource                                ASRL1::INSTR, this property returns INSTR, regardless of the class of the I/O           Class                                    control.

          General               Returns the current locking state of the resource associated with the given
           Settings:Resource      session. The resource can be unlocked, locked with an exclusive lock, or
         Lock State             locked with a shared lock. The default is Unlocked.

          General
           Settings:Resource      Returns the unique identifier for a resource.
        Name

                                Returns the physical slot location of the device. If the slot is unknown, the          General Settings:Slot                                 value returned is -1.

          General                 Specifies the minimum timeout value, in milliseconds, to use when
          Settings:Timeout       accessing the device. Note that the actual timeout that VISA returns may be
          Value                 higher than the one requested. The default is 2000.

          General                 Specifies which trigger mechanism to use. In VXI systems, for example, you
           Settings:Trigger       can choose between software triggers and hardware triggers on a specific
            Identifier                trigger line. The default is Software.

                                    Specifies a data value for the private use of an application. The VISA
          General Settings:User  implementation stores this value in a per-session location, so that user
          Data                  data on other sessions does not affect the user data on this session. VISA
                             does not use this property for any purpose.

                                    Specifies human-readable text that describes the given interface. Note: Use
           Interface
                                the value of this property for display purposes only and not for
           Information:Interface
                              programmatic decisions. The value can change between VISA
           Description
                               implementations and/or revisions.

           Interface
           Information:Interface   Returns the board number for the given interface.
        Number


10416   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10416 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10417 ordinal=10417 -->
## Property and Method Reference

Property and Method Reference


Property              Description

Interface
Information:Interface   Returns the board number of the parent device.
Number of Parent

Interface
Information:Interface   Specifies the interface type of the given session.
Type

                        Specifies whether VISA Read To File appends or overwrites (truncates)Message Based                  when opening a file. If this property is set to TRUE, VISA Read To FileSettings:File Append
                   appends when opening a file. If this property is set to FALSE, VISA Read ToEnable                           File overwrites (truncates) when opening a file. The default is FALSE.

                        Specifies which protocol to use. In VXI, you can choose normal word serial
                       or fast data channel. In GPIB, you can choose normal or high-speed HS-488Message Based                          transfers. In serial, TCP/IP, or USB, you can choose normal transfers orSettings:IO Protocol
                       488.2-defined strings. In USBTMC, you can choose normal or vendor-
                          specific transfers. The default is Normal.

Message Based
Settings:Is 488.2       Returns whether the device is 488.2 compliant.
Compliant

                        Specifies whether to send an END indicator on the last byte of each write
                       operation. This property is relevant only in VISA Write and related
                       operations. The default is TRUE. On Serial Instr sessions, if this property is
Message Based         set to FALSE, the write transmits the exact contents of the user buffer,
Settings:Send End     without modifying it and without appending anything to the data. If this
Enable                property is set to TRUE, VISA performs the behavior described in the
                      property End Mode for Writes (ASRL End Out). On GPIB, VXI, GPIB-VXI, TCP/
                        IP Instr, and USB Instr sessions, if this property is set to TRUE, VISA includes
                      the 488.2 defined end of message terminator.

                        Specifies whether to terminate a read operation due to an END condition.
                       This property is relevant only in VISA Read and related operations. For all
                       session types that support this property, if this property is set to TRUE,
                      read does not terminate due to an END condition. However, a read may still
Message Based        terminate successfully if the Message Based Settings:Termination
Settings:Suppress End  Character Enable (TermChar En) property is set to TRUE. Otherwise, read
Enable              does not terminate until it receives all of the requested data (or an error
                         occurs). The default is FALSE (except for TCP/IP Socket sessions). On Serial
                           Instr sessions, if this property is set to FALSE, VISA performs the behavior
                      described in the Serial Settings:End Mode for Reads (ASRL End In) property.
                 On USB Raw sessions, if this property is set to FALSE, VISA performs the


                                                    © National Instruments 10417

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10417 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10418 ordinal=10418 -->
## Property and Method Reference

Property and Method Reference


          Property              Description

                                behavior described in the USB Settings:End Mode for Reads (USB End In)
                                  property. On TCP/IP Socket sessions, if this property is set to FALSE, if NI-
                                VISA reads some data and then detects a pause in the arrival of data
                                  packets, it terminates the read operation. On TCP/IP Socket sessions, the
                                   default value for the property is TRUE in NI-VISA. On VXI Instr sessions, if
                                      this property is set to FALSE, the END bit terminates read operations.

         Message Based         Specifies a character that, when read, causes a read operation to
           Settings:Termination   terminate. The termination character also must be enabled. This default is
          Character            0x0A (linefeed).

         Message Based                                    Specifies whether a read operation terminates when it receives the           Settings:Termination                                 termination character. The default is FALSE.          Character Enable

                                    Specifies the number of elements by which to increment the destination
           Register Based        address on block move operations. Valid values include 0 and 1. The
           Settings:Destination    default is 1. If this property is set to 0, VISA Move Out X operations always
          Increment Count      read from the same element, essentially treating the destination as a FIFO
                                        register.

                                    Specifies the number of elements by which to increment the source
           Register Based        address on block move operations. Valid values include 0 and 1. The
           Settings:Source        default is 1. If this property is set to 0, VISA Move In X operations always
          Increment Count      read from the same element, essentially treating the source as a FIFO
                                        register.

           Register Based
                                Returns whether the current session has a mapped window, and if so,          Settings:Window                              whether the window allows direct pointer dereferences.          Access

           Register Based         Returns the base interface address to which this window maps. If the
          Settings:Window Base  Window Access property is Not Mapped, the value of this property is
          Address               undefined.

           Register Based         Returns the size of the region mapped to this window. If the Window Access
          Settings:Window Size   property is Not Mapped, the value of this property is undefined.

          VXI/VME                Specifies the address modifier to use in high-level access operations, such
           Settings:Destination    as VISA Out X and VISA Move Out X, when writing to the destination. The
          Access Privilege        default is Data/Privileged (0).

          VXI/VME                Specifies the byte order to use in high-level access operations, such as VISA
           Settings:Destination   Out X and VISA Move Out X, when writing to the destination. The default is
          Byte Order             Big Endian (0).


10418   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10418 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10419 ordinal=10419 -->
## Property and Method Reference

Property and Method Reference


Property              Description

VXI/VME Settings:Fast                        Specifies whether FDC transfers use normal or streaming mode. TheData Channel:Channel                        default is Normal.Mode

VXI/VME Settings:Fast                        Specifies which FDC channel to use to transfer data buffers. Valid values
Data Channel:Channel                       include 0-7.Number

VXI/VME Settings:Fast                        Specifies whether transfers use a pair of FDC channels. If you do not setData Channel:Use                          this property, transfers use only one FDC channel. The default is FALSE.
Channel Pairs

VXI/VME                      Returns whether the VXI device is an immediate servant of the localSettings:Immediate                          controller.
Servant

VXI/VME                      Returns the lowest logical address in the mainframe in which the device
Settings:Mainframe                         resides.Logical Address

VXI/VME                Specifies the address modifier to use in high-level access operations, such
Settings:Source        as VISA In X and VISA Move In X, when reading from the source. The default
Access Privilege           is Data/Privileged (0).

VXI/VME                Specifies the byte order to use in high-level access operations, such as VISA
Settings:Source Byte    In X and VISA Move In X, when reading from the source. The default is Big
Order                Endian (0).

VXI/VME                      Returns which VXI trigger lines this implementation supports. This propertySettings:Supported
                       returns a bit vector with bits 0-9 corresponding to TTL0 through ECL1.VXI Trigger Lines

VXI/VME Settings:VXI
Commander Logical    Returns the logical address of the commander of the VXI device.
Address

VXI/VME Settings:VXI
                      Returns the class to which the VXI or VME device belongs.
Device Class

VXI/VME Settings:VXI
                      Returns the logical address of the VXI device.
Logical Address

VXI/VME Settings:VXI
Memory Address       Returns the VXI address space used by the device.
Space

VXI/VME Settings:VXI   Returns the base address of the device in VXI memory space.

                                                    © National Instruments 10419

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10419 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10420 ordinal=10420 -->
## Property and Method Reference

Property and Method Reference


          Property              Description

        Memory Base Address

          VXI/VME Settings:VXI                                Returns the size of memory requested by the device in VXI memory space.        Memory Size

                                    Specifies the directions of the mapped TTL triggers lines. This is a bit
                                  vector where bits 0-7 represent TTL triggers 0-7 respectively. A bit value of          VXI/VME Settings:VXI                              0 means the corresponding line is routed out of the frame, and a value of 1           Trigger Directions                           means the line is routed into the frame. Lines must be enabled using VXI/
                         VME Settings:VXI Trigger Lines Enable.

                                    Specifies which VXI TLL triggers have mappings. This is a bit vector where
                                      bits 0-7 represent TTL triggers 0-7 respectively. A bit value of 0 means the          VXI/VME Settings:VXI                                corresponding trigger line is unmapped, and 1 means a mapping exists.           Trigger Lines Enable
                            Use VXI/VME Settings:VXI Trigger Directions to set an enabled line's
                                     direction.

          VXI/VME                Specifies the address modifier to use in low-level access operations, such
          Settings:Window       as VISA Map Address, VISA Peek X, and VISA Poke X, when accessing the
          Access Privilege      mapped window. The default is Data/Privileged (0).

          VXI/VME                Specifies the byte order to use in low-level access operations, such as VISA
          Settings:Window Byte  Map Address, VISA Peek X, and VISA Poke X, when accessing the mapped
          Order               window. The default is Big Endian (0).

           Version
          Information:Resource  Returns a value that corresponds to the VXI manufacturer ID of the
          Manufacturer         manufacturer that created the VISA implementation.
            Identification

                                Returns the name of the manufacturer that created the implementation.
           Version                This is not related to the device manufacturer attributes. Note: Use the
          Information:Resource  value of this property for display purposes only and not for programmatic
          Manufacturer Name    decisions. The value can change between VISA implementations and/or
                                     revisions.

                                Returns the version of a given implementation. This value is defined by the
           Version                 individual manufacturer and increments with each new revision. The
           Information:Version of  format of the value has the upper 12 bits as the major number of the
          Implementation        version, the next lower 12 bits as the minor number of the version, and the
                                lowest 8 bits as the sub-minor number of the version.

                                Returns the value that uniquely identifies the version of the VISA
           Version
                                    specification to which the implementation complies. The format of the
           Information:Version of
                                 value has the upper 12 bits as the major number of the version, the next
           Specification
                               lower 12 bits as the minor number of the version, and the lowest 8 bits as

10420   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10420 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10421 ordinal=10421 -->
## Property and Method Reference

Property and Method Reference


 Property              Description

                       the sub-minor number of the version.

GPIBGPIB Settings:LineSettings:Line RENREN StateState

Returns the current state of the GPIB REN (Remote ENable) interface line.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


 Unknown                                                                 -1

 Unasserted                                                   0

 Asserted                                                     1

GPIBGPIB Settings:PrimarySettings:Primary AddressAddress

Returns the primary address of the GPIB device used by the given session.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

                                                    © National Instruments 10421

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10421 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10422 ordinal=10422 -->
## Property and Method Reference

Property and Method Reference


           Available in Real-Time Operating System                                   Yes

    GPIBGPIB Settings:ReaddressingSettings:Readdressing

         Specifies whether to use repeat addressing before each read or write operation. The
         default is TRUE.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

    GPIBGPIB Settings:SecondarySettings:Secondary AddressAddress

        Returns the secondary address of the GPIB device used by the given session. If the
        device does not have a secondary address, the value of this property is 65535 (0xFFFF).

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


10422   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10422 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10423 ordinal=10423 -->
## Property and Method Reference

Property and Method Reference

GPIBGPIB Settings:UnaddressingSettings:Unaddressing

Specifies whether to unaddress the device (UNT and UNL) after each read or write
operation. The default is FALSE.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

GeneralGeneral Settings:AllowSettings:Allow DMADMA TransfersTransfers

Specifies whether I/O accesses should attempt to use DMA (TRUE) or Programmed I/O
(FALSE). In some implementations, this property may have global effects even though
it is documented as a local property. This behavior affects performance and not
functionality.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


                                                    © National Instruments 10423

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10423 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10424 ordinal=10424 -->
## Property and Method Reference

Property and Method Reference

    GeneralGeneral Settings:ManufacturerSettings:Manufacturer IdentificationIdentification

        Returns the ID of the manufacturer that created the device. For VXI resources, this
         refers to the VXI Manufacturer ID. For PXI/PCI resources, this refers to the Subsystem
       Vendor ID (SVID) if it is nonzero; otherwise, this refers to the Vendor ID (VID). For USB
         resources, this refers to the Vendor ID (VID).

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    GeneralGeneral Settings:ManufacturerSettings:Manufacturer NameName

        Returns the name of the manufacturer that created the device. Note: Use the value of
          this property for display purposes only and not for programmatic decisions. The value
       can change between VISA implementations and/or revisions.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


10424   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10424 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10425 ordinal=10425 -->
## Property and Method Reference

Property and Method Reference

GeneralGeneral Settings:MaximumSettings:Maximum QueueQueue LengthLength

Specifies the maximum number of events that can be queued at any time on the given
session. This property is read/write until the first time you call VISA Enable Event on a
session. Thereafter, it is read only. The default is 50.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

GeneralGeneral Settings:ModelSettings:Model CodeCode

Returns the device model code assigned by the manufacturer. For VXI resources, this
refers to the VXI Model Code. For PXI/PCI resources, if the Subsystem Vendor ID is
nonzero, this refers to the Subsystem ID (SSID); otherwise, this refers to the Device ID
(DID). For USB resources, this refers to the Product ID (PID).

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


                                                    © National Instruments 10425

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10425 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10426 ordinal=10426 -->
## Property and Method Reference

Property and Method Reference

    GeneralGeneral Settings:ModelSettings:Model NameName

        Returns the model name of the device. Note: Use the value of this property for display
        purposes only and not for programmatic decisions. The value can change between
        VISA implementations and/or revisions.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    GeneralGeneral Settings:ResourceSettings:Resource ClassClass

        Returns the resource class of the resource string used to open the given session. For
        example, if the resource string for a given session is COM1 or ASRL1::INSTR, this
        property returns INSTR, regardless of the class of the I/O control.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


10426   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10426 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10427 ordinal=10427 -->
## Property and Method Reference

Property and Method Reference

GeneralGeneral Settings:ResourceSettings:Resource LockLock StateState

Returns the current locking state of the resource associated with the given session.
The resource can be unlocked, locked with an exclusive lock, or locked with a shared
lock. The default is Unlocked.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


 Unlocked                                                     0

 Exclusive                                                     1

 Shared                                                       2

GeneralGeneral Settings:ResourceSettings:Resource NameName

Returns the unique identifier for a resource.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


                                                    © National Instruments 10427

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10427 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10428 ordinal=10428 -->
## Property and Method Reference

Property and Method Reference

    GeneralGeneral Settings:SlotSettings:Slot

        Returns the physical slot location of the device. If the slot is unknown, the value
        returned is -1.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    GeneralGeneral Settings:TimeoutSettings:Timeout ValueValue

         Specifies the minimum timeout value, in milliseconds, to use when accessing the
         device. Note that the actual timeout that VISA returns may be higher than the one
        requested. The default is 2000.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes


10428   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10428 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10429 ordinal=10429 -->
## Property and Method Reference

Property and Method Reference

GeneralGeneral Settings:TriggerSettings:Trigger IdentifierIdentifier

Specifies which trigger mechanism to use. In VXI systems, for example, you can choose
between software triggers and hardware triggers on a specific trigger line. The default
is Software.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


 Software                                                             -1

 TTL0                                                     0

 TTL1                                                     1

 TTL2                                                     2

 TTL3                                                     3

 TTL4                                                     4

 TTL5                                                     5

 TTL6                                                     6

 TTL7                                                     7

 ECL0                                                     8

 ECL1                                                     9

GeneralGeneral Settings:UserSettings:User DataData

Specifies a data value for the private use of an application. The VISA implementation

                                                    © National Instruments 10429

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10429 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10430 ordinal=10430 -->
## Property and Method Reference

Property and Method Reference

         stores this value in a per-session location, so that user data on other sessions does not
         affect the user data on this session. VISA does not use this property for any purpose.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

     InterfaceInterface Information:InterfaceInformation:Interface DescriptionDescription

         Specifies human-readable text that describes the given interface. Note: Use the value
         of this property for display purposes only and not for programmatic decisions. The
        value can change between VISA implementations and/or revisions.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

     InterfaceInterface Information:InterfaceInformation:Interface NumberNumber

        Returns the board number for the given interface.


10430   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10430 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10431 ordinal=10431 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

InterfaceInterface Information:InterfaceInformation:Interface NumberNumber ofof
ParentParent

Returns the board number of the parent device.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

InterfaceInterface Information:InterfaceInformation:Interface TypeType

Specifies the interface type of the given session.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 10431

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10431 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10432 ordinal=10432 -->
## Property and Method Reference

Property and Method Reference


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


         GPIB                                                       1

          VXI                                                         2

          GPIB-VXI                                                    3

           Serial                                                       4

          PXI                                                         5

         TCPIP                                                      6

        USB                                                        7

          FireWire                                                    9

    MessageMessage BasedBased Settings:FileSettings:File AppendAppend EnableEnable

         Specifies whether VISA Read To File appends or overwrites (truncates) when opening a
            file. If this property is set to TRUE, VISA Read To File appends when opening a file. If
          this property is set to FALSE, VISA Read To File overwrites (truncates) when opening a
            file. The default is FALSE.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes


10432   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10432 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10433 ordinal=10433 -->
## Property and Method Reference

Property and Method Reference

MessageMessage BasedBased Settings:IOSettings:IO ProtocolProtocol

Specifies which protocol to use. In VXI, you can choose normal word serial or fast data
channel. In GPIB, you can choose normal or high-speed HS-488 transfers. In serial,
TCP/IP, or USB, you can choose normal transfers or 488.2-defined strings. In USBTMC,
you can choose normal or vendor-specific transfers. The default is Normal.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


 Normal                                                                    1

 VXI/FDC                                                                   2

 GPIB/HS488                                                                3

 Serial-TCPIP-USB/488 Strings                                                 4

 USBTMC/Vendor-Specific                                                    5

MessageMessage BasedBased Settings:IsSettings:Is 488.2488.2 CompliantCompliant

Returns whether the device is 488.2 compliant.

Remarks

The following table lists the characteristics of this property.


 Data type


                                                    © National Instruments 10433

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10433 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10434 ordinal=10434 -->
## Property and Method Reference

Property and Method Reference


          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    MessageMessage BasedBased Settings:SendSettings:Send EndEnd EnableEnable

         Specifies whether to send an END indicator on the last byte of each write operation.
        This property is relevant only in VISA Write and related operations. The default is TRUE.
      On Serial Instr sessions, if this property is set to FALSE, the write transmits the exact
        contents of the user buffer, without modifying it and without appending anything to
        the data. If this property is set to TRUE, VISA performs the behavior described in the
        property End Mode for Writes (ASRL End Out). On GPIB, VXI, GPIB-VXI, TCP/IP Instr, and
      USB Instr sessions, if this property is set to TRUE, VISA includes the 488.2 defined end
         of message terminator.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

    MessageMessage BasedBased Settings:SuppressSettings:Suppress EndEnd
    EnableEnable

         Specifies whether to terminate a read operation due to an END condition. This
        property is relevant only in VISA Read and related operations. For all session types that
        support this property, if this property is set to TRUE, read does not terminate due to an
      END condition. However, a read may still terminate successfully if the Message Based
        Settings:Termination Character Enable (TermChar En) property is set to TRUE.

10434   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10434 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10435 ordinal=10435 -->
## Property and Method Reference

Property and Method Reference

Otherwise, read does not terminate until it receives all of the requested data (or an
error occurs). The default is FALSE (except for TCP/IP Socket sessions). On Serial Instr
sessions, if this property is set to FALSE, VISA performs the behavior described in the
Serial Settings:End Mode for Reads (ASRL End In) property. On USB Raw sessions, if
this property is set to FALSE, VISA performs the behavior described in the USB
Settings:End Mode for Reads (USB End In) property. On TCP/IP Socket sessions, if this
property is set to FALSE, if NI-VISA reads some data and then detects a pause in the
arrival of data packets, it terminates the read operation. On TCP/IP Socket sessions,
the default value for the property is TRUE in NI-VISA. On VXI Instr sessions, if this
property is set to FALSE, the END bit terminates read operations.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

MessageMessage BasedBased Settings:TerminationSettings:Termination
CharacterCharacter

Specifies a character that, when read, causes a read operation to terminate. The
termination character also must be enabled. This default is 0x0A (linefeed).

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

                                                    © National Instruments 10435

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10435 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10436 ordinal=10436 -->
## Property and Method Reference

Property and Method Reference


           Available in Real-Time Operating System                                  Yes

    MessageMessage BasedBased Settings:TerminationSettings:Termination
    CharacterCharacter EnableEnable

         Specifies whether a read operation terminates when it receives the termination
         character. The default is FALSE.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

     RegisterRegister BasedBased Settings:DestinationSettings:Destination
    IncrementIncrement CountCount

         Specifies the number of elements by which to increment the destination address on
        block move operations. Valid values include 0 and 1. The default is 1. If this property is
         set to 0, VISA Move Out X operations always read from the same element, essentially
         treating the destination as a FIFO register.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

10436   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10436 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10437 ordinal=10437 -->
## Property and Method Reference

Property and Method Reference


 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

RegisterRegister BasedBased Settings:SourceSettings:Source IncrementIncrement
CountCount

Specifies the number of elements by which to increment the source address on block
move operations. Valid values include 0 and 1. The default is 1. If this property is set to
0, VISA Move In X operations always read from the same element, essentially treating
the source as a FIFO register.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

RegisterRegister BasedBased Settings:WindowSettings:Window AccessAccess

Returns whether the current session has a mapped window, and if so, whether the
window allows direct pointer dereferences.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only


                                                    © National Instruments 10437

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10437 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10438 ordinal=10438 -->
## Property and Method Reference

Property and Method Reference


           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


         Not Mapped                                                                1

         Use Peek/Poke Operations                                                    2

        Can Dereference Pointer                                                     3

          Pointer value is byte-swapped                                                4

     RegisterRegister BasedBased Settings:WindowSettings:Window BaseBase
    AddressAddress

        Returns the base interface address to which this window maps. If the Window Access
        property is Not Mapped, the value of this property is undefined.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

     RegisterRegister BasedBased Settings:WindowSettings:Window SizeSize

        Returns the size of the region mapped to this window. If the Window Access property is
       Not Mapped, the value of this property is undefined.


10438   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10438 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10439 ordinal=10439 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VXI/VMEVXI/VME Settings:DestinationSettings:Destination AccessAccess
PrivilegePrivilege

Specifies the address modifier to use in high-level access operations, such as VISA Out
X and VISA Move Out X, when writing to the destination. The default is Data/Privileged
(0).

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


 Data/Privileged                                                           0

 Data/NonPrivileged                                                       1

 Program/Privileged                                                       2

 Program/NonPrivileged                                                    3

 Block/Privileged                                                          4


                                                    © National Instruments 10439

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10439 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10440 ordinal=10440 -->
## Property and Method Reference

Property and Method Reference


          Block/NonPrivileged                                                      5

          D64/Privileged                                                           6

          D64/NonPrivileged                                                        7

    VXI/VMEVXI/VME Settings:DestinationSettings:Destination ByteByte OrderOrder

         Specifies the byte order to use in high-level access operations, such as VISA Out X and
        VISA Move Out X, when writing to the destination. The default is Big Endian (0).

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes


          Big Endian                                                        0

            Little Endian                                                      1

    VXI/VMEVXI/VME Settings:FastSettings:Fast DataData Channel:ChannelChannel:Channel
   ModeMode

         Specifies whether FDC transfers use normal or streaming mode. The default is Normal.

      Remarks

       The following table lists the characteristics of this property.


10440   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10440 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10441 ordinal=10441 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


 Normal                                                   1

 Stream                                                   2

VXI/VMEVXI/VME Settings:FastSettings:Fast DataData Channel:ChannelChannel:Channel
NumberNumber

Specifies which FDC channel to use to transfer data buffers. Valid values include 0-7.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

VXI/VMEVXI/VME Settings:FastSettings:Fast DataData Channel:UseChannel:Use
ChannelChannel PairsPairs

Specifies whether transfers use a pair of FDC channels. If you do not set this property,
transfers use only one FDC channel. The default is FALSE.


                                                    © National Instruments 10441

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10441 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10442 ordinal=10442 -->
## Property and Method Reference

Property and Method Reference

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

    VXI/VMEVXI/VME Settings:ImmediateSettings:Immediate ServantServant

        Returns whether the VXI device is an immediate servant of the local controller.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    VXI/VMEVXI/VME Settings:MainframeSettings:Mainframe LogicalLogical AddressAddress

        Returns the lowest logical address in the mainframe in which the device resides.

      Remarks

       The following table lists the characteristics of this property.


          Data type


10442   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10442 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10443 ordinal=10443 -->
## Property and Method Reference

Property and Method Reference


 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VXI/VMEVXI/VME Settings:SourceSettings:Source AccessAccess PrivilegePrivilege

Specifies the address modifier to use in high-level access operations, such as VISA In X
and VISA Move In X, when reading from the source. The default is Data/Privileged (0).

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


 Data/Privileged                                                           0

 Data/NonPrivileged                                                       1

 Program/Privileged                                                       2

 Program/NonPrivileged                                                    3

 Block/Privileged                                                          4

 Block/NonPrivileged                                                      5

 D64/Privileged                                                           6

 D64/NonPrivileged                                                        7

VXI/VMEVXI/VME Settings:SourceSettings:Source ByteByte OrderOrder

Specifies the byte order to use in high-level access operations, such as VISA In X and

                                                    © National Instruments 10443

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10443 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10444 ordinal=10444 -->
## Property and Method Reference

Property and Method Reference

        VISA Move In X, when reading from the source. The default is Big Endian (0).

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes


          Big Endian                                                        0

            Little Endian                                                      1

    VXI/VMEVXI/VME Settings:SupportedSettings:Supported VXIVXI TriggerTrigger LinesLines

        Returns which VXI trigger lines this implementation supports. This property returns a
          bit vector with bits 0-9 corresponding to TTL0 through ECL1.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


10444   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10444 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10445 ordinal=10445 -->
## Property and Method Reference

Property and Method Reference

VXI/VMEVXI/VME Settings:VXISettings:VXI CommanderCommander LogicalLogical
AddressAddress

Returns the logical address of the commander of the VXI device.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VXI/VMEVXI/VME Settings:VXISettings:VXI DeviceDevice ClassClass

Returns the class to which the VXI or VME device belongs.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


 Memory                                                     0

 Extended                                                    1

 Message                                                     2


                                                    © National Instruments 10445

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10445 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10446 ordinal=10446 -->
## Property and Method Reference

Property and Method Reference


           Register                                                     3

         Other                                                       4

    VXI/VMEVXI/VME Settings:VXISettings:VXI LogicalLogical AddressAddress

        Returns the logical address of the VXI device.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    VXI/VMEVXI/VME Settings:VXISettings:VXI MemoryMemory AddressAddress SpaceSpace

        Returns the VXI address space used by the device.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


         VXI/VME A16                                                      1

         VXI/VME A24                                                      2

10446   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10446 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10447 ordinal=10447 -->
## Property and Method Reference

Property and Method Reference


 VXI/VME A32                                                      3

 VXI/VME A64                                                      4

VXI/VMEVXI/VME Settings:VXISettings:VXI MemoryMemory BaseBase AddressAddress

Returns the base address of the device in VXI memory space.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VXI/VMEVXI/VME Settings:VXISettings:VXI MemoryMemory SizeSize

Returns the size of memory requested by the device in VXI memory space.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


                                                    © National Instruments 10447

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10447 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10448 ordinal=10448 -->
## Property and Method Reference

Property and Method Reference

    VXI/VMEVXI/VME Settings:VXISettings:VXI TriggerTrigger DirectionsDirections

         Specifies the directions of the mapped TTL triggers lines. This is a bit vector where bits
        0-7 represent TTL triggers 0-7 respectively. A bit value of 0 means the corresponding
          line is routed out of the frame, and a value of 1 means the line is routed into the frame.
        Lines must be enabled using VXI/VME Settings:VXI Trigger Lines Enable.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

    VXI/VMEVXI/VME Settings:VXISettings:VXI TriggerTrigger LinesLines EnableEnable

         Specifies which VXI TLL triggers have mappings. This is a bit vector where bits 0-7
        represent TTL triggers 0-7 respectively. A bit value of 0 means the corresponding
         trigger line is unmapped, and 1 means a mapping exists. Use VXI/VME Settings:VXI
         Trigger Directions to set an enabled line's direction.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes


10448   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10448 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10449 ordinal=10449 -->
## Property and Method Reference

Property and Method Reference

VXI/VMEVXI/VME Settings:WindowSettings:Window AccessAccess PrivilegePrivilege

Specifies the address modifier to use in low-level access operations, such as VISA Map
Address, VISA Peek X, and VISA Poke X, when accessing the mapped window. The
default is Data/Privileged (0).

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


 Data/Privileged                                                           0

 Data/NonPrivileged                                                       1

 Program/Privileged                                                       2

 Program/NonPrivileged                                                    3

 Block/Privileged                                                          4

 Block/NonPrivileged                                                      5

 D64/Privileged                                                           6

 D64/NonPrivileged                                                        7

VXI/VMEVXI/VME Settings:WindowSettings:Window ByteByte OrderOrder

Specifies the byte order to use in low-level access operations, such as VISA Map
Address, VISA Peek X, and VISA Poke X, when accessing the mapped window. The
default is Big Endian (0).


                                                    © National Instruments 10449

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10449 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10450 ordinal=10450 -->
## Property and Method Reference

Property and Method Reference

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes


          Big Endian                                                        0

            Little Endian                                                      1

    VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
     IdentificationIdentification

        Returns a value that corresponds to the VXI manufacturer ID of the manufacturer that
        created the VISA implementation.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


10450   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10450 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10451 ordinal=10451 -->
## Property and Method Reference

Property and Method Reference

VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
NameName

Returns the name of the manufacturer that created the implementation. This is not
related to the device manufacturer attributes. Note: Use the value of this property for
display purposes only and not for programmatic decisions. The value can change
between VISA implementations and/or revisions.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VersionVersion Information:VersionInformation:Version ofof
ImplementationImplementation

Returns the version of a given implementation. This value is defined by the individual
manufacturer and increments with each new revision. The format of the value has the
upper 12 bits as the major number of the version, the next lower 12 bits as the minor
number of the version, and the lowest 8 bits as the sub-minor number of the version.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only


                                                    © National Instruments 10451

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10451 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10452 ordinal=10452 -->
## Property and Method Reference

Property and Method Reference


           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    VersionVersion Information:VersionInformation:Version ofof SpecificationSpecification

        Returns the value that uniquely identifies the version of the VISA specification to which
        the implementation complies. The format of the value has the upper 12 bits as the
       major number of the version, the next lower 12 bits as the minor number of the
         version, and the lowest 8 bits as the sub-minor number of the version.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

       VXI/GPIB-VXI/VMEVXI/GPIB-VXI/VME MemAccMemAcc PropertiesProperties


          Property             Description

         GPIB Settings:Line
                               Returns the current state of the GPIB REN (Remote ENable) interface line.
        REN State

         GPIB
                               Returns the primary address of the GPIB controller used by the given
           Settings:Primary
                                   session.
          Address

         GPIB                 Returns the secondary address of the GPIB controller used by the given
          Settings:Secondary    session. If the controller does not have a secondary address, the value of
          Address                 this property is 65535 (0xFFFF).

          General                Specifies whether I/O accesses should attempt to use DMA (TRUE) or
           Settings:Allow DMA   Programmed I/O (FALSE). In some implementations, this property may have
           Transfers              global effects even though it is documented as a local property. This

10452   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10452 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10453 ordinal=10453 -->
## Property and Method Reference

Property and Method Reference


Property             Description

                     behavior affects performance and not functionality.

General                Specifies the maximum number of events that can be queued at any time
Settings:Maximum    on the given session. This property is read/write until the first time you call
Queue Length        VISA Enable Event on a session. Thereafter, it is read only. The default is 50.

                     Returns the resource class of the resource string used to open the givenGeneral                       session. For example, if the resource string for a given session is COM1 orSettings:Resource                     ASRL1::INSTR, this property returns INSTR, regardless of the class of the I/OClass                        control.

General              Returns the current locking state of the resource associated with the given
Settings:Resource     session. The resource can be unlocked, locked with an exclusive lock, or
Lock State            locked with a shared lock. The default is Unlocked.

General
Settings:Resource     Returns the unique identifier for a resource.
Name

General                Specifies the minimum timeout value, in milliseconds, to use when
Settings:Timeout      accessing the device. Note that the actual timeout that VISA returns may be
Value                 higher than the one requested. The default is 2000.

                       Specifies a data value for the private use of an application. The VISA
General Settings:User  implementation stores this value in a per-session location, so that user data
Data              on other sessions does not affect the user data on this session. VISA does
                     not use this property for any purpose.

                       Specifies human-readable text that describes the given interface. Note: UseInterface                     the value of this property for display purposes only and not for
Information:Interface                    programmatic decisions. The value can change between VISADescription                    implementations and/or revisions.

Interface
Information:Interface  Returns the board number for the given interface.
Number

Interface
Information:Interface  Returns the board number of the parent device.
Number of Parent

Interface
Information:Interface  Specifies the interface type of the given session.
Type

Register Based         Specifies the number of elements by which to increment the destination


                                                    © National Instruments 10453

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10453 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10454 ordinal=10454 -->
## Property and Method Reference

Property and Method Reference


          Property             Description

                               address on block move operations. Valid values include 0 and 1. The default           Settings:Destination                                           is 1. If this property is set to 0, VISA Move Out X operations always read from          Increment Count                               the same element, essentially treating the destination as a FIFO register.

                                   Specifies the number of elements by which to increment the source address           Register Based
                          on block move operations. Valid values include 0 and 1. The default is 1. If           Settings:Source                                     this property is set to 0, VISA Move In X operations always read from the          Increment Count                          same element, essentially treating the source as a FIFO register.

           Register Based                               Returns whether the current session has a mapped window, and if so,
          Settings:Window                             whether the window allows direct pointer dereferences.          Access

           Register Based        Returns the base interface address to which this window maps. If the
          Settings:Window     Window Access property is Not Mapped, the value of this property is
         Base Address         undefined.

           Register Based        Returns the size of the region mapped to this window. If the Window Access
          Settings:Window Size  property is Not Mapped, the value of this property is undefined.

          VXI/VME               Specifies the address modifier to use in high-level access operations, such
           Settings:Destination   as VISA Out X and VISA Move Out X, when writing to the destination. The
          Access Privilege        default is Data/Privileged (0).

          VXI/VME               Specifies the byte order to use in high-level access operations, such as VISA
           Settings:Destination   Out X and VISA Move Out X, when writing to the destination. The default is
          Byte Order            Big Endian (0).

          VXI/VME               Specifies the address modifier to use in high-level access operations, such
           Settings:Source       as VISA In X and VISA Move In X, when reading from the source. The default
          Access Privilege          is Data/Privileged (0).

          VXI/VME               Specifies the byte order to use in high-level access operations, such as VISA
           Settings:Source Byte   In X and VISA Move In X, when reading from the source. The default is Big
          Order               Endian (0).

          VXI/VME Settings:VXI
                               Returns the logical address of the local VXI controller.
           Logical Address

          VXI/VME               Specifies the address modifier to use in low-level access operations, such as
          Settings:Window      VISA Map Address, VISA Peek X, and VISA Poke X, when accessing the
          Access Privilege     mapped window. The default is Data/Privileged (0).

          VXI/VME               Specifies the byte order to use in low-level access operations, such as VISA
          Settings:Window     Map Address, VISA Peek X, and VISA Poke X, when accessing the mapped
          Byte Order          window. The default is Big Endian (0).


10454   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10454 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10455 ordinal=10455 -->
## Property and Method Reference

Property and Method Reference


 Property             Description

 Version
 Information:Resource Returns a value that corresponds to the VXI manufacturer ID of the
 Manufacturer         manufacturer that created the VISA implementation.
 Identification

                      Returns the name of the manufacturer that created the implementation.
 Version               This is not related to the device manufacturer attributes. Note: Use the
 Information:Resource  value of this property for display purposes only and not for programmatic
 Manufacturer Name   decisions. The value can change between VISA implementations and/or
                         revisions.

                      Returns the version of a given implementation. This value is defined by the
 Version                individual manufacturer and increments with each new revision. The format
 Information:Version   of the value has the upper 12 bits as the major number of the version, the
 of Implementation    next lower 12 bits as the minor number of the version, and the lowest 8 bits
                      as the sub-minor number of the version.

                      Returns the value that uniquely identifies the version of the VISA
 Version                specification to which the implementation complies. The format of the
 Information:Version   value has the upper 12 bits as the major number of the version, the next
 of Specification       lower 12 bits as the minor number of the version, and the lowest 8 bits as
                      the sub-minor number of the version.

GPIBGPIB Settings:LineSettings:Line RENREN StateState

Returns the current state of the GPIB REN (Remote ENable) interface line.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


 Unknown                                                                 -1

                                                    © National Instruments 10455

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10455 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10456 ordinal=10456 -->
## Property and Method Reference

Property and Method Reference


          Unasserted                                                   0

          Asserted                                                     1

    GPIBGPIB Settings:PrimarySettings:Primary AddressAddress

        Returns the primary address of the GPIB controller used by the given session.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    GPIBGPIB Settings:SecondarySettings:Secondary AddressAddress

        Returns the secondary address of the GPIB controller used by the given session. If the
         controller does not have a secondary address, the value of this property is 65535
         (0xFFFF).

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


10456   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10456 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10457 ordinal=10457 -->
## Property and Method Reference

Property and Method Reference

GeneralGeneral Settings:AllowSettings:Allow DMADMA TransfersTransfers

Specifies whether I/O accesses should attempt to use DMA (TRUE) or Programmed I/O
(FALSE). In some implementations, this property may have global effects even though
it is documented as a local property. This behavior affects performance and not
functionality.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

GeneralGeneral Settings:MaximumSettings:Maximum QueueQueue LengthLength

Specifies the maximum number of events that can be queued at any time on the given
session. This property is read/write until the first time you call VISA Enable Event on a
session. Thereafter, it is read only. The default is 50.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


                                                    © National Instruments 10457

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10457 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10458 ordinal=10458 -->
## Property and Method Reference

Property and Method Reference

    GeneralGeneral Settings:ResourceSettings:Resource ClassClass

        Returns the resource class of the resource string used to open the given session. For
        example, if the resource string for a given session is COM1 or ASRL1::INSTR, this
        property returns INSTR, regardless of the class of the I/O control.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    GeneralGeneral Settings:ResourceSettings:Resource LockLock StateState

        Returns the current locking state of the resource associated with the given session.
       The resource can be unlocked, locked with an exclusive lock, or locked with a shared
         lock. The default is Unlocked.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


         Unlocked                                                     0


10458   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10458 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10459 ordinal=10459 -->
## Property and Method Reference

Property and Method Reference


 Exclusive                                                     1

 Shared                                                       2

GeneralGeneral Settings:ResourceSettings:Resource NameName

Returns the unique identifier for a resource.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

GeneralGeneral Settings:TimeoutSettings:Timeout ValueValue

Specifies the minimum timeout value, in milliseconds, to use when accessing the
device. Note that the actual timeout that VISA returns may be higher than the one
requested. The default is 2000.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


                                                    © National Instruments 10459

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10459 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10460 ordinal=10460 -->
## Property and Method Reference

Property and Method Reference

    GeneralGeneral Settings:UserSettings:User DataData

         Specifies a data value for the private use of an application. The VISA implementation
         stores this value in a per-session location, so that user data on other sessions does not
         affect the user data on this session. VISA does not use this property for any purpose.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

     InterfaceInterface Information:InterfaceInformation:Interface DescriptionDescription

         Specifies human-readable text that describes the given interface. Note: Use the value
         of this property for display purposes only and not for programmatic decisions. The
        value can change between VISA implementations and/or revisions.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


10460   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10460 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10461 ordinal=10461 -->
## Property and Method Reference

Property and Method Reference

InterfaceInterface Information:InterfaceInformation:Interface NumberNumber

Returns the board number for the given interface.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

InterfaceInterface Information:InterfaceInformation:Interface NumberNumber ofof
ParentParent

Returns the board number of the parent device.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

InterfaceInterface Information:InterfaceInformation:Interface TypeType

Specifies the interface type of the given session.


                                                    © National Instruments 10461

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10461 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10462 ordinal=10462 -->
## Property and Method Reference

Property and Method Reference

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


         GPIB                                                       1

          VXI                                                         2

          GPIB-VXI                                                    3

           Serial                                                       4

          PXI                                                         5

         TCPIP                                                      6

        USB                                                        7

          FireWire                                                    9

     RegisterRegister BasedBased Settings:DestinationSettings:Destination
    IncrementIncrement CountCount

         Specifies the number of elements by which to increment the destination address on
        block move operations. Valid values include 0 and 1. The default is 1. If this property is
         set to 0, VISA Move Out X operations always read from the same element, essentially
         treating the destination as a FIFO register.

      Remarks

       The following table lists the characteristics of this property.


10462   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10462 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10463 ordinal=10463 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

RegisterRegister BasedBased Settings:SourceSettings:Source IncrementIncrement
CountCount

Specifies the number of elements by which to increment the source address on block
move operations. Valid values include 0 and 1. The default is 1. If this property is set to
0, VISA Move In X operations always read from the same element, essentially treating
the source as a FIFO register.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

RegisterRegister BasedBased Settings:WindowSettings:Window AccessAccess

Returns whether the current session has a mapped window, and if so, whether the
window allows direct pointer dereferences.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 10463

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10463 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10464 ordinal=10464 -->
## Property and Method Reference

Property and Method Reference


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


         Not Mapped                                                                1

         Use Peek/Poke Operations                                                    2

        Can Dereference Pointer                                                     3

          Pointer value is byte-swapped                                                4

     RegisterRegister BasedBased Settings:WindowSettings:Window BaseBase
    AddressAddress

        Returns the base interface address to which this window maps. If the Window Access
        property is Not Mapped, the value of this property is undefined.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

     RegisterRegister BasedBased Settings:WindowSettings:Window SizeSize

        Returns the size of the region mapped to this window. If the Window Access property is
       Not Mapped, the value of this property is undefined.


10464   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10464 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10465 ordinal=10465 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VXI/VMEVXI/VME Settings:DestinationSettings:Destination AccessAccess
PrivilegePrivilege

Specifies the address modifier to use in high-level access operations, such as VISA Out
X and VISA Move Out X, when writing to the destination. The default is Data/Privileged
(0).

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


 Data/Privileged                                                           0

 Data/NonPrivileged                                                       1

 Program/Privileged                                                       2

 Program/NonPrivileged                                                    3

 Block/Privileged                                                          4


                                                    © National Instruments 10465

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10465 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10466 ordinal=10466 -->
## Property and Method Reference

Property and Method Reference


          Block/NonPrivileged                                                      5

          D64/Privileged                                                           6

          D64/NonPrivileged                                                        7

    VXI/VMEVXI/VME Settings:DestinationSettings:Destination ByteByte OrderOrder

         Specifies the byte order to use in high-level access operations, such as VISA Out X and
        VISA Move Out X, when writing to the destination. The default is Big Endian (0).

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes


          Big Endian                                                        0

            Little Endian                                                      1

    VXI/VMEVXI/VME Settings:SourceSettings:Source AccessAccess PrivilegePrivilege

         Specifies the address modifier to use in high-level access operations, such as VISA In X
       and VISA Move In X, when reading from the source. The default is Data/Privileged (0).

      Remarks

       The following table lists the characteristics of this property.


          Data type


10466   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10466 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10467 ordinal=10467 -->
## Property and Method Reference

Property and Method Reference


 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


 Data/Privileged                                                           0

 Data/NonPrivileged                                                       1

 Program/Privileged                                                       2

 Program/NonPrivileged                                                    3

 Block/Privileged                                                          4

 Block/NonPrivileged                                                      5

 D64/Privileged                                                           6

 D64/NonPrivileged                                                        7

VXI/VMEVXI/VME Settings:SourceSettings:Source ByteByte OrderOrder

Specifies the byte order to use in high-level access operations, such as VISA In X and
VISA Move In X, when reading from the source. The default is Big Endian (0).

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


 Big Endian                                                        0

 Little Endian                                                      1


                                                    © National Instruments 10467

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10467 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10468 ordinal=10468 -->
## Property and Method Reference

Property and Method Reference

    VXI/VMEVXI/VME Settings:VXISettings:VXI LogicalLogical AddressAddress

        Returns the logical address of the local VXI controller.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    VXI/VMEVXI/VME Settings:WindowSettings:Window AccessAccess PrivilegePrivilege

         Specifies the address modifier to use in low-level access operations, such as VISA Map
        Address, VISA Peek X, and VISA Poke X, when accessing the mapped window. The
         default is Data/Privileged (0).

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes


           Data/Privileged                                                           0

          Data/NonPrivileged                                                       1

          Program/Privileged                                                       2


10468   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10468 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10469 ordinal=10469 -->
## Property and Method Reference

Property and Method Reference


 Program/NonPrivileged                                                    3

 Block/Privileged                                                          4

 Block/NonPrivileged                                                      5

 D64/Privileged                                                           6

 D64/NonPrivileged                                                        7

VXI/VMEVXI/VME Settings:WindowSettings:Window ByteByte OrderOrder

Specifies the byte order to use in low-level access operations, such as VISA Map
Address, VISA Peek X, and VISA Poke X, when accessing the mapped window. The
default is Big Endian (0).

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


 Big Endian                                                        0

 Little Endian                                                      1

VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
IdentificationIdentification

Returns a value that corresponds to the VXI manufacturer ID of the manufacturer that
created the VISA implementation.


                                                    © National Instruments 10469

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10469 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10470 ordinal=10470 -->
## Property and Method Reference

Property and Method Reference

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
   NameName

        Returns the name of the manufacturer that created the implementation. This is not
         related to the device manufacturer attributes. Note: Use the value of this property for
         display purposes only and not for programmatic decisions. The value can change
       between VISA implementations and/or revisions.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    VersionVersion Information:VersionInformation:Version ofof
    ImplementationImplementation

        Returns the version of a given implementation. This value is defined by the individual

10470   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10470 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10471 ordinal=10471 -->
## Property and Method Reference

Property and Method Reference

manufacturer and increments with each new revision. The format of the value has the
upper 12 bits as the major number of the version, the next lower 12 bits as the minor
number of the version, and the lowest 8 bits as the sub-minor number of the version.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VersionVersion Information:VersionInformation:Version ofof SpecificationSpecification

Returns the value that uniquely identifies the version of the VISA specification to which
the implementation complies. The format of the value has the upper 12 bits as the
major number of the version, the next lower 12 bits as the minor number of the
version, and the lowest 8 bits as the sub-minor number of the version.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VXI/GPIB-VXI/VMEVXI/GPIB-VXI/VME RBDRBD InstrInstr PropertiesProperties


                                                    © National Instruments 10471

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10471 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10472 ordinal=10472 -->
## Property and Method Reference

Property and Method Reference


          Property              Description

         GPIB Settings:Line                                Returns the current state of the GPIB REN (Remote ENable) interface line.        REN State

         GPIB Settings:Primary                                Returns the primary address of the GPIB device used by the given session.          Address

         GPIB                 Returns the secondary address of the GPIB device used by the given
          Settings:Secondary    session. If the device does not have a secondary address, the value of this
          Address               property is 65535 (0xFFFF).

                                   Specifies whether I/O accesses should attempt to use DMA (TRUE) or          General
                           Programmed I/O (FALSE). In some implementations, this property may           Settings:Allow DMA                             have global effects even though it is documented as a local property. This           Transfers                                behavior affects performance and not functionality.

                                Returns the ID of the manufacturer that created the device. For VXI
          General                resources, this refers to the VXI Manufacturer ID. For PXI/PCI resources, this
           Settings:Manufacturer  refers to the Subsystem Vendor ID (SVID) if it is nonzero; otherwise, this
            Identification           refers to the Vendor ID (VID). For USB resources, this refers to the Vendor ID
                                       (VID).

                                Returns the name of the manufacturer that created the device. Note: Use
          General                                the value of this property for display purposes only and not for           Settings:Manufacturer                             programmatic decisions. The value can change between VISA
        Name                               implementations and/or revisions.

          General                Specifies the maximum number of events that can be queued at any time
          Settings:Maximum    on the given session. This property is read/write until the first time you call
        Queue Length         VISA Enable Event on a session. Thereafter, it is read only. The default is 50.

                                Returns the device model code assigned by the manufacturer. For VXI
                                  resources, this refers to the VXI Model Code. For PXI/PCI resources, if the
          General
                             Subsystem Vendor ID is nonzero, this refers to the Subsystem ID (SSID);
          Settings:Model Code
                                 otherwise, this refers to the Device ID (DID). For USB resources, this refers to
                                the Product ID (PID).

                                Returns the model name of the device. Note: Use the value of this property
          General
                                     for display purposes only and not for programmatic decisions. The value
          Settings:Model Name
                             can change between VISA implementations and/or revisions.

                                Returns the resource class of the resource string used to open the given
          General
                                   session. For example, if the resource string for a given session is COM1 or
           Settings:Resource
                                ASRL1::INSTR, this property returns INSTR, regardless of the class of the I/O
           Class
                                    control.

          General              Returns the current locking state of the resource associated with the given

10472   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10472 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10473 ordinal=10473 -->
## Property and Method Reference

Property and Method Reference


Property              Description

Settings:Resource      session. The resource can be unlocked, locked with an exclusive lock, or
Lock State            locked with a shared lock. The default is Unlocked.

General
Settings:Resource     Returns the unique identifier for a resource.
Name

                     Returns the physical slot location of the device. If the slot is unknown, theGeneral Settings:Slot                      value returned is -1.

General                Specifies the minimum timeout value, in milliseconds, to use when
Settings:Timeout      accessing the device. Note that the actual timeout that VISA returns may be
Value                 higher than the one requested. The default is 2000.

General                Specifies which trigger mechanism to use. In VXI systems, for example, you
Settings:Trigger       can choose between software triggers and hardware triggers on a specific
Identifier               trigger line. The default is Software.

                        Specifies a data value for the private use of an application. The VISA
General Settings:User  implementation stores this value in a per-session location, so that user data
Data               on other sessions does not affect the user data on this session. VISA does
                     not use this property for any purpose.

                        Specifies human-readable text that describes the given interface. Note: UseInterface                      the value of this property for display purposes only and not for
Information:Interface                    programmatic decisions. The value can change between VISADescription                     implementations and/or revisions.

Interface
Information:Interface  Returns the board number for the given interface.
Number

Interface
Information:Interface  Returns the board number of the parent device.
Number of Parent

Interface
Information:Interface  Specifies the interface type of the given session.
Type

                        Specifies the number of elements by which to increment the destination
Register Based
                     address on block move operations. Valid values include 0 and 1. The default
Settings:Destination
                              is 1. If this property is set to 0, VISA Move Out X operations always read from
Increment Count
                      the same element, essentially treating the destination as a FIFO register.

Register Based         Specifies the number of elements by which to increment the source


                                                    © National Instruments 10473

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10473 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10474 ordinal=10474 -->
## Property and Method Reference

Property and Method Reference


          Property              Description

                               address on block move operations. Valid values include 0 and 1. The default           Settings:Source                                            is 1. If this property is set to 0, VISA Move In X operations always read from          Increment Count                                the same element, essentially treating the source as a FIFO register.

           Register Based                                Returns whether the current session has a mapped window, and if so,
          Settings:Window                             whether the window allows direct pointer dereferences.          Access

           Register Based        Returns the base interface address to which this window maps. If the
          Settings:Window Base Window Access property is Not Mapped, the value of this property is
          Address               undefined.

           Register Based        Returns the size of the region mapped to this window. If the Window Access
          Settings:Window Size  property is Not Mapped, the value of this property is undefined.

          VXI/VME                Specifies the address modifier to use in high-level access operations, such
           Settings:Destination   as VISA Out X and VISA Move Out X, when writing to the destination. The
          Access Privilege        default is Data/Privileged (0).

          VXI/VME                Specifies the byte order to use in high-level access operations, such as VISA
           Settings:Destination   Out X and VISA Move Out X, when writing to the destination. The default is
          Byte Order            Big Endian (0).

          VXI/VME                                Returns whether the VXI device is an immediate servant of the local          Settings:Immediate
                                     controller.          Servant

          VXI/VME
                                Returns the lowest logical address in the mainframe in which the device          Settings:Mainframe                                    resides.           Logical Address

          VXI/VME                Specifies the address modifier to use in high-level access operations, such
           Settings:Source       as VISA In X and VISA Move In X, when reading from the source. The default
          Access Privilege          is Data/Privileged (0).

          VXI/VME                Specifies the byte order to use in high-level access operations, such as VISA
           Settings:Source Byte   In X and VISA Move In X, when reading from the source. The default is Big
          Order               Endian (0).

          VXI/VME
                                Returns which VXI trigger lines this implementation supports. This property
          Settings:Supported
                                  returns a bit vector with bits 0-9 corresponding to TTL0 through ECL1.
           VXI Trigger Lines

          VXI/VME Settings:VXI
        Commander Logical   Returns the logical address of the commander of the VXI device.
          Address


10474   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10474 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10475 ordinal=10475 -->
## Property and Method Reference

Property and Method Reference


Property              Description

VXI/VME Settings:VXI                     Returns the class to which the VXI or VME device belongs.Device Class

VXI/VME Settings:VXI                     Returns the logical address of the VXI device.Logical Address

VXI/VME Settings:VXI
Memory Address      Returns the VXI address space used by the device.
Space

VXI/VME Settings:VXI                     Returns the base address of the device in VXI memory space.
Memory Base Address

VXI/VME Settings:VXI                     Returns the size of memory requested by the device in VXI memory space.Memory Size

                        Specifies the directions of the mapped TTL triggers lines. This is a bit vector
                   where bits 0-7 represent TTL triggers 0-7 respectively. A bit value of 0 meansVXI/VME Settings:VXI
                      the corresponding line is routed out of the frame, and a value of 1 meansTrigger Directions                      the line is routed into the frame. Lines must be enabled using VXI/VME
                        Settings:VXI Trigger Lines Enable.

                        Specifies which VXI TLL triggers have mappings. This is a bit vector where
VXI/VME Settings:VXI    bits 0-7 represent TTL triggers 0-7 respectively. A bit value of 0 means the
Trigger Lines Enable   corresponding trigger line is unmapped, and 1 means a mapping exists. Use
                    VXI/VME Settings:VXI Trigger Directions to set an enabled line's direction.

VXI/VME                Specifies the address modifier to use in low-level access operations, such
Settings:Window      as VISA Map Address, VISA Peek X, and VISA Poke X, when accessing the
Access Privilege      mapped window. The default is Data/Privileged (0).

VXI/VME                Specifies the byte order to use in low-level access operations, such as VISA
Settings:Window Byte Map Address, VISA Peek X, and VISA Poke X, when accessing the mapped
Order               window. The default is Big Endian (0).

Version
Information:Resource  Returns a value that corresponds to the VXI manufacturer ID of the
Manufacturer         manufacturer that created the VISA implementation.
Identification

                     Returns the name of the manufacturer that created the implementation.
Version                This is not related to the device manufacturer attributes. Note: Use the
Information:Resource  value of this property for display purposes only and not for programmatic
Manufacturer Name    decisions. The value can change between VISA implementations and/or
                         revisions.


                                                    © National Instruments 10475

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10475 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10476 ordinal=10476 -->
## Property and Method Reference

Property and Method Reference


          Property              Description

                                Returns the version of a given implementation. This value is defined by the
           Version                individual manufacturer and increments with each new revision. The
           Information:Version   format of the value has the upper 12 bits as the major number of the
           of Implementation     version, the next lower 12 bits as the minor number of the version, and the
                                lowest 8 bits as the sub-minor number of the version.

                                Returns the value that uniquely identifies the version of the VISA
           Version                 specification to which the implementation complies. The format of the
           Information:Version    value has the upper 12 bits as the major number of the version, the next
           of Specification       lower 12 bits as the minor number of the version, and the lowest 8 bits as
                                the sub-minor number of the version.

    GPIBGPIB Settings:LineSettings:Line RENREN StateState

        Returns the current state of the GPIB REN (Remote ENable) interface line.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


        Unknown                                                                 -1

          Unasserted                                                   0

          Asserted                                                     1

    GPIBGPIB Settings:PrimarySettings:Primary AddressAddress

        Returns the primary address of the GPIB device used by the given session.


10476   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10476 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10477 ordinal=10477 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

GPIBGPIB Settings:SecondarySettings:Secondary AddressAddress

Returns the secondary address of the GPIB device used by the given session. If the
device does not have a secondary address, the value of this property is 65535 (0xFFFF).

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

GeneralGeneral Settings:AllowSettings:Allow DMADMA TransfersTransfers

Specifies whether I/O accesses should attempt to use DMA (TRUE) or Programmed I/O
(FALSE). In some implementations, this property may have global effects even though
it is documented as a local property. This behavior affects performance and not
functionality.


                                                    © National Instruments 10477

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10477 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10478 ordinal=10478 -->
## Property and Method Reference

Property and Method Reference

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

    GeneralGeneral Settings:ManufacturerSettings:Manufacturer IdentificationIdentification

        Returns the ID of the manufacturer that created the device. For VXI resources, this
         refers to the VXI Manufacturer ID. For PXI/PCI resources, this refers to the Subsystem
       Vendor ID (SVID) if it is nonzero; otherwise, this refers to the Vendor ID (VID). For USB
         resources, this refers to the Vendor ID (VID).

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    GeneralGeneral Settings:ManufacturerSettings:Manufacturer NameName

        Returns the name of the manufacturer that created the device. Note: Use the value of
          this property for display purposes only and not for programmatic decisions. The value
       can change between VISA implementations and/or revisions.


10478   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10478 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10479 ordinal=10479 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

GeneralGeneral Settings:MaximumSettings:Maximum QueueQueue LengthLength

Specifies the maximum number of events that can be queued at any time on the given
session. This property is read/write until the first time you call VISA Enable Event on a
session. Thereafter, it is read only. The default is 50.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

GeneralGeneral Settings:ModelSettings:Model CodeCode

Returns the device model code assigned by the manufacturer. For VXI resources, this
refers to the VXI Model Code. For PXI/PCI resources, if the Subsystem Vendor ID is
nonzero, this refers to the Subsystem ID (SSID); otherwise, this refers to the Device ID
(DID). For USB resources, this refers to the Product ID (PID).


                                                    © National Instruments 10479

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10479 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10480 ordinal=10480 -->
## Property and Method Reference

Property and Method Reference

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    GeneralGeneral Settings:ModelSettings:Model NameName

        Returns the model name of the device. Note: Use the value of this property for display
        purposes only and not for programmatic decisions. The value can change between
        VISA implementations and/or revisions.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    GeneralGeneral Settings:ResourceSettings:Resource ClassClass

        Returns the resource class of the resource string used to open the given session. For
        example, if the resource string for a given session is COM1 or ASRL1::INSTR, this
        property returns INSTR, regardless of the class of the I/O control.


10480   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10480 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10481 ordinal=10481 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

GeneralGeneral Settings:ResourceSettings:Resource LockLock StateState

Returns the current locking state of the resource associated with the given session.
The resource can be unlocked, locked with an exclusive lock, or locked with a shared
lock. The default is Unlocked.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


 Unlocked                                                     0

 Exclusive                                                     1

 Shared                                                       2

GeneralGeneral Settings:ResourceSettings:Resource NameName

Returns the unique identifier for a resource.

                                                    © National Instruments 10481

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10481 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10482 ordinal=10482 -->
## Property and Method Reference

Property and Method Reference

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    GeneralGeneral Settings:SlotSettings:Slot

        Returns the physical slot location of the device. If the slot is unknown, the value
        returned is -1.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    GeneralGeneral Settings:TimeoutSettings:Timeout ValueValue

         Specifies the minimum timeout value, in milliseconds, to use when accessing the
         device. Note that the actual timeout that VISA returns may be higher than the one
        requested. The default is 2000.

      Remarks

       The following table lists the characteristics of this property.


10482   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10482 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10483 ordinal=10483 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

GeneralGeneral Settings:TriggerSettings:Trigger IdentifierIdentifier

Specifies which trigger mechanism to use. In VXI systems, for example, you can choose
between software triggers and hardware triggers on a specific trigger line. The default
is Software.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


 Software                                                             -1

 TTL0                                                     0

 TTL1                                                     1

 TTL2                                                     2

 TTL3                                                     3

 TTL4                                                     4

 TTL5                                                     5

 TTL6                                                     6

 TTL7                                                     7

 ECL0                                                     8

                                                    © National Instruments 10483

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10483 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10484 ordinal=10484 -->
## Property and Method Reference

Property and Method Reference


         ECL1                                                     9

    GeneralGeneral Settings:UserSettings:User DataData

         Specifies a data value for the private use of an application. The VISA implementation
         stores this value in a per-session location, so that user data on other sessions does not
         affect the user data on this session. VISA does not use this property for any purpose.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

     InterfaceInterface Information:InterfaceInformation:Interface DescriptionDescription

         Specifies human-readable text that describes the given interface. Note: Use the value
         of this property for display purposes only and not for programmatic decisions. The
        value can change between VISA implementations and/or revisions.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


10484   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10484 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10485 ordinal=10485 -->
## Property and Method Reference

Property and Method Reference

InterfaceInterface Information:InterfaceInformation:Interface NumberNumber

Returns the board number for the given interface.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

InterfaceInterface Information:InterfaceInformation:Interface NumberNumber ofof
ParentParent

Returns the board number of the parent device.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

InterfaceInterface Information:InterfaceInformation:Interface TypeType

Specifies the interface type of the given session.


                                                    © National Instruments 10485

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10485 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10486 ordinal=10486 -->
## Property and Method Reference

Property and Method Reference

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


         GPIB                                                       1

          VXI                                                         2

          GPIB-VXI                                                    3

           Serial                                                       4

          PXI                                                         5

         TCPIP                                                      6

        USB                                                        7

          FireWire                                                    9

     RegisterRegister BasedBased Settings:DestinationSettings:Destination
    IncrementIncrement CountCount

         Specifies the number of elements by which to increment the destination address on
        block move operations. Valid values include 0 and 1. The default is 1. If this property is
         set to 0, VISA Move Out X operations always read from the same element, essentially
         treating the destination as a FIFO register.

      Remarks

       The following table lists the characteristics of this property.


10486   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10486 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10487 ordinal=10487 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

RegisterRegister BasedBased Settings:SourceSettings:Source IncrementIncrement
CountCount

Specifies the number of elements by which to increment the source address on block
move operations. Valid values include 0 and 1. The default is 1. If this property is set to
0, VISA Move In X operations always read from the same element, essentially treating
the source as a FIFO register.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

RegisterRegister BasedBased Settings:WindowSettings:Window AccessAccess

Returns whether the current session has a mapped window, and if so, whether the
window allows direct pointer dereferences.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 10487

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10487 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10488 ordinal=10488 -->
## Property and Method Reference

Property and Method Reference


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


         Not Mapped                                                                1

         Use Peek/Poke Operations                                                    2

        Can Dereference Pointer                                                     3

          Pointer value is byte-swapped                                                4

     RegisterRegister BasedBased Settings:WindowSettings:Window BaseBase
    AddressAddress

        Returns the base interface address to which this window maps. If the Window Access
        property is Not Mapped, the value of this property is undefined.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

     RegisterRegister BasedBased Settings:WindowSettings:Window SizeSize

        Returns the size of the region mapped to this window. If the Window Access property is
       Not Mapped, the value of this property is undefined.


10488   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10488 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10489 ordinal=10489 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VXI/VMEVXI/VME Settings:DestinationSettings:Destination AccessAccess
PrivilegePrivilege

Specifies the address modifier to use in high-level access operations, such as VISA Out
X and VISA Move Out X, when writing to the destination. The default is Data/Privileged
(0).

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


 Data/Privileged                                                           0

 Data/NonPrivileged                                                       1

 Program/Privileged                                                       2

 Program/NonPrivileged                                                    3

 Block/Privileged                                                          4


                                                    © National Instruments 10489

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10489 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10490 ordinal=10490 -->
## Property and Method Reference

Property and Method Reference


          Block/NonPrivileged                                                      5

          D64/Privileged                                                           6

          D64/NonPrivileged                                                        7

    VXI/VMEVXI/VME Settings:DestinationSettings:Destination ByteByte OrderOrder

         Specifies the byte order to use in high-level access operations, such as VISA Out X and
        VISA Move Out X, when writing to the destination. The default is Big Endian (0).

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes


          Big Endian                                                        0

            Little Endian                                                      1

    VXI/VMEVXI/VME Settings:ImmediateSettings:Immediate ServantServant

        Returns whether the VXI device is an immediate servant of the local controller.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only


10490   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10490 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10491 ordinal=10491 -->
## Property and Method Reference

Property and Method Reference


 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VXI/VMEVXI/VME Settings:MainframeSettings:Mainframe LogicalLogical AddressAddress

Returns the lowest logical address in the mainframe in which the device resides.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VXI/VMEVXI/VME Settings:SourceSettings:Source AccessAccess PrivilegePrivilege

Specifies the address modifier to use in high-level access operations, such as VISA In X
and VISA Move In X, when reading from the source. The default is Data/Privileged (0).

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


 Data/Privileged                                                           0


                                                    © National Instruments 10491

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10491 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10492 ordinal=10492 -->
## Property and Method Reference

Property and Method Reference


          Data/NonPrivileged                                                       1

          Program/Privileged                                                       2

          Program/NonPrivileged                                                    3

           Block/Privileged                                                          4

          Block/NonPrivileged                                                      5

          D64/Privileged                                                           6

          D64/NonPrivileged                                                        7

    VXI/VMEVXI/VME Settings:SourceSettings:Source ByteByte OrderOrder

         Specifies the byte order to use in high-level access operations, such as VISA In X and
        VISA Move In X, when reading from the source. The default is Big Endian (0).

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes


          Big Endian                                                        0

            Little Endian                                                      1

    VXI/VMEVXI/VME Settings:SupportedSettings:Supported VXIVXI TriggerTrigger LinesLines

        Returns which VXI trigger lines this implementation supports. This property returns a
          bit vector with bits 0-9 corresponding to TTL0 through ECL1.


10492   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10492 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10493 ordinal=10493 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VXI/VMEVXI/VME Settings:VXISettings:VXI CommanderCommander LogicalLogical
AddressAddress

Returns the logical address of the commander of the VXI device.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VXI/VMEVXI/VME Settings:VXISettings:VXI DeviceDevice ClassClass

Returns the class to which the VXI or VME device belongs.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 10493

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10493 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10494 ordinal=10494 -->
## Property and Method Reference

Property and Method Reference


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes


        Memory                                                     0

         Extended                                                    1

         Message                                                     2

           Register                                                     3

         Other                                                       4

    VXI/VMEVXI/VME Settings:VXISettings:VXI LogicalLogical AddressAddress

        Returns the logical address of the VXI device.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    VXI/VMEVXI/VME Settings:VXISettings:VXI MemoryMemory AddressAddress SpaceSpace

        Returns the VXI address space used by the device.


10494   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10494 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10495 ordinal=10495 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes


 VXI/VME A16                                                      1

 VXI/VME A24                                                      2

 VXI/VME A32                                                      3

 VXI/VME A64                                                      4

VXI/VMEVXI/VME Settings:VXISettings:VXI MemoryMemory BaseBase AddressAddress

Returns the base address of the device in VXI memory space.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VXI/VMEVXI/VME Settings:VXISettings:VXI MemoryMemory SizeSize

Returns the size of memory requested by the device in VXI memory space.


                                                    © National Instruments 10495

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10495 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10496 ordinal=10496 -->
## Property and Method Reference

Property and Method Reference

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    VXI/VMEVXI/VME Settings:VXISettings:VXI TriggerTrigger DirectionsDirections

         Specifies the directions of the mapped TTL triggers lines. This is a bit vector where bits
        0-7 represent TTL triggers 0-7 respectively. A bit value of 0 means the corresponding
          line is routed out of the frame, and a value of 1 means the line is routed into the frame.
        Lines must be enabled using VXI/VME Settings:VXI Trigger Lines Enable.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes

    VXI/VMEVXI/VME Settings:VXISettings:VXI TriggerTrigger LinesLines EnableEnable

         Specifies which VXI TLL triggers have mappings. This is a bit vector where bits 0-7
        represent TTL triggers 0-7 respectively. A bit value of 0 means the corresponding
         trigger line is unmapped, and 1 means a mapping exists. Use VXI/VME Settings:VXI
         Trigger Directions to set an enabled line's direction.


10496   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10496 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10497 ordinal=10497 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

VXI/VMEVXI/VME Settings:WindowSettings:Window AccessAccess PrivilegePrivilege

Specifies the address modifier to use in low-level access operations, such as VISA Map
Address, VISA Peek X, and VISA Poke X, when accessing the mapped window. The
default is Data/Privileged (0).

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


 Data/Privileged                                                           0

 Data/NonPrivileged                                                       1

 Program/Privileged                                                       2

 Program/NonPrivileged                                                    3

 Block/Privileged                                                          4

 Block/NonPrivileged                                                      5

 D64/Privileged                                                           6

                                                    © National Instruments 10497

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10497 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10498 ordinal=10498 -->
## Property and Method Reference

Property and Method Reference


          D64/NonPrivileged                                                        7

    VXI/VMEVXI/VME Settings:WindowSettings:Window ByteByte OrderOrder

         Specifies the byte order to use in low-level access operations, such as VISA Map
        Address, VISA Peek X, and VISA Poke X, when accessing the mapped window. The
         default is Big Endian (0).

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                          Read/Write

           Available in Run-Time Engine                                             Yes

           Available in Real-Time Operating System                                  Yes


          Big Endian                                                        0

            Little Endian                                                      1

    VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
     IdentificationIdentification

        Returns a value that corresponds to the VXI manufacturer ID of the manufacturer that
        created the VISA implementation.

      Remarks

       The following table lists the characteristics of this property.


          Data type

10498   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10498 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10499 ordinal=10499 -->
## Property and Method Reference

Property and Method Reference


 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VersionVersion Information:ResourceInformation:Resource ManufacturerManufacturer
NameName

Returns the name of the manufacturer that created the implementation. This is not
related to the device manufacturer attributes. Note: Use the value of this property for
display purposes only and not for programmatic decisions. The value can change
between VISA implementations and/or revisions.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

VersionVersion Information:VersionInformation:Version ofof
ImplementationImplementation

Returns the version of a given implementation. This value is defined by the individual
manufacturer and increments with each new revision. The format of the value has the
upper 12 bits as the major number of the version, the next lower 12 bits as the minor
number of the version, and the lowest 8 bits as the sub-minor number of the version.


                                                    © National Instruments 10499

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10499 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10500 ordinal=10500 -->
## Property and Method Reference

Property and Method Reference

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

    VersionVersion Information:VersionInformation:Version ofof SpecificationSpecification

        Returns the value that uniquely identifies the version of the VISA specification to which
        the implementation complies. The format of the value has the upper 12 bits as the
       major number of the version, the next lower 12 bits as the minor number of the
         version, and the lowest 8 bits as the sub-minor number of the version.

      Remarks

       The following table lists the characteristics of this property.


          Data type

          Permissions                                                     Read Only

           Available in Run-Time Engine                                              Yes

           Available in Real-Time Operating System                                   Yes

       GeneralGeneral Settings:MaximumSettings:Maximum QueueQueue LengthLength

         Specifies the maximum number of events that can be queued at any time on the given
         session. This property is read/write until the first time you call VISA Enable Event on a
         session. Thereafter, it is read only. The default is 50.


10500   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:10500 -->

