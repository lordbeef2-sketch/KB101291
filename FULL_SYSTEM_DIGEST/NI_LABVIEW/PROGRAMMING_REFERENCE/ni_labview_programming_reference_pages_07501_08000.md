# NI_LABVIEW_PROGRAMMING_REFERENCE

<!--SYSTEM_CORPUS id=NI_LABVIEW_PROGRAMMING_REFERENCE format=markdown generated=2026-07-14T12:02:18+00:00 -->
- title: LabVIEW Programming Reference Manual
- source: https://docs-be.ni.com/bundle/labview-api-ref/preprocessedpdf/enus
- source_sha256: 7a54c389b4f3d78e2215f55c9f156124d3668ce61d0d5018094e356004d895ac
- versions: 2024 Q1|2024 Q3|2025 Q1|2025 Q3|2026 Q1
- fidelity: full-text-records

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7501 ordinal=7501 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                 Read Only

WritableWritable

Indicates whether the variable object includes a writable data value.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                 Read Only

VariableVariable ObjectObject MethodsMethods


 Method  Description

 Is Kind   Indicates whether the variable object is a member or descendant of the class specified by
 Of       Class Id.

         Returns the URL of the variable object you specify. If you wire a value of TRUE to the Norm
          localhost? input and the host name of the URL corresponds to the local host, this property
 URL          replaces the IP address or DNS name of the local host with the string localhost in the URL.
        The default value for this input is FALSE.

IsIs KindKind OfOf

Indicates whether the variable object is a member or descendant of the class specified
by Class Id.

Parameters

 Name               Data type             Required             Description

 Class Id                                      Yes


                                                    © National Instruments 7501

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7501 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7502 ordinal=7502 -->
## Property and Method Reference

Property and Method Reference


      Name               Data type             Required             Description

           Is Kind Of                           No

     URLURL

       Returns the URL of the variable object you specify. If you wire a value of TRUE to the
     Norm localhost? input and the host name of the URL corresponds to the local host, this
       property replaces the IP address or DNS name of the local host with the string
       localhost in the URL. The default value for this input is FALSE.

     Parameters

      Name                       Data type          Required          Description

       Norm localhost?                                    Yes

       URL                                    No

     VIVI ServerServer PropertiesProperties andand MethodsMethods

       This section describes each VI Server property and method and lists the class to which
      each object belongs.

        VI Server property and method classes are arranged in a hierarchy with each class
        inheriting the properties and methods associated with the class in the preceding level.

    © 2005–2023 National Instruments Corporation. All rights reserved. Refer to the
     <National Instruments>\_Legal Information directory for information
      about NI copyright, patents, trademarks, warranties, product warnings, and export
       compliance.

      VIVI ServerServer PropertyProperty andand MethodMethod CharacteristicsCharacteristics

      The following list defines the characteristics for each property and method.

            • Data type—Specifies the data type of the property or method.
            • Permissions—Specifies if this property is Read Only, Write Only, Read/Write, or

7502   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7502 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7503 ordinal=7503 -->
## Property and Method Reference

Property and Method Reference

  WriteInEditOnly. If the property is WriteInEditOnly, you can write to the property
  only when the VI is in edit mode.
• Available in Run-Time Engine—Specifies if you can use this property or method in
  built applications. The value in parentheses indicates the permission for the
  property or method in the Run-Time Engine. Values include Read Only, Write Only,
  Read/Write, WriteInEditOnly, or no. Some properties and methods are only
  available during editing. If this characteristic value is No, LabVIEW returns error
  1043 if you use this property or method in built applications. If you use
  SharedVariableIO properties or methods, you must install the Datalogging and
  Supervisory Control (DSC) Module Run-Time System. Refer to the National
  Instruments Web site for information about the DSC Module Run-Time System.
• Available in Real-Time Operating System—Specifies if you can use this property or
  method in the Real-Time Operating System. The value in parentheses indicates the
  permission for the property or method in the Real-Time Operating System. Values
  include Read Only, Write Only, Read/Write, WriteInEditOnly, or no. Some properties
  and methods are only available during editing. If this characteristic value is No,
  LabVIEW returns error 1043 if you use this property or method in the Real-Time
  Operating System.
• Settable when the VI is running—Specifies if you can write a value to this property
  or method when the VI is running. If this characteristic value is No, LabVIEW returns
  error 1000 or 1073 if you try to write a value when the VI is running. This
  characteristic does not apply to the properties and methods in the Application
  class.
• Loads the front panel into memory—Specifies if LabVIEW loads the front panel
  into memory. If this characteristic value is Yes, LabVIEW returns error 1013 if the
  front panel cannot be loaded into memory. This characteristic does not apply to
  the properties and methods in the Application class.
• Need to authenticate before use—Specifies if you need to authenticate the VI
  before you can use the property or method. For example, you might need to
  unlock a password-protected VI before using a method with a characteristic value
  of Yes. If this characteristic value is Yes, LabVIEW returns error 1040 or 1044 if you
  did not authenticate the VI.
• Loads the block diagram into memory—Specifies if LabVIEW loads the block
  diagram into memory. If this characteristic value is Yes, LabVIEW returns error 1012
   if the block diagram cannot be loaded into memory. This characteristic does not
  apply to the properties and methods in the Application class.
• Remote access allowed—Specifies if access to this property or method is allowed


                                                   © National Instruments 7503

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7503 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7504 ordinal=7504 -->
## Property and Method Reference

Property and Method Reference

          with a permission error by a remote application instance. If this characteristic
          value is No, LabVIEW returns error 1032 if you try to use a remote reference to this
          property or method.
            • Must wait until user interface is idle—Specifies if you can use this property or
         method while the user is selecting items in a dialog box, tracking a control, and so
          on.
            • Available with control VIs—Specifies if you can use this property or method with
            VIs that are controls. If this characteristic value is No, LabVIEW returns error 1035 if
         you use this property or method with VIs that are controls. This characteristic
           applies only to the properties and methods in the VI class.
            • Available with global VIs—Specifies if you can use this property or method with VIs
           that are globals. If this characteristic value is No, LabVIEW returns error 1035 if you
          use this property or method with VIs that are globals. This characteristic applies
          only to the properties and methods in the VI class.
            • Available with strict type definitions—Specifies if you can use this property or
         method with strict type definitions. This characteristic does not apply to the
           properties and methods in the Application and VI classes.
            • Available with polymorphic VIs—Specifies if you can use this property or method
          with polymorphic VIs. If this characteristic value is No, LabVIEW returns error 1035
                 if you use this property or method with polymorphic VIs. This characteristic applies
          only to the properties and methods in the VI class.

     EventEvent SourceSource

      The following table describes the source of LabVIEW events.


        0   LabVIEW UI—All user interface events that LabVIEW generates internally.

        1    ActiveX—All events that ActiveX generates.

        2    .NET—All events that .NET generates.

        25   User Event—All events that the user creates programmatically.

      VIVI ServerServer ClassClass HierarchyHierarchy

            • Application
            • Generic

7504   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7504 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7505 ordinal=7505 -->
## Property and Method Reference

Property and Method Reference

◦ Bus
◦ ConnectorPane
◦ Cursor
◦ FlatSequenceFrame
  ▪ TimeSequenceFrame
◦ GObject
  ▪ AbstractDiagram
   ▪ Diagram
     ▪ CompanionDiagram
     ▪ SDF Companion Diagram
     ▪ SDFDiagram
     ▪ ScDiagram
     ▪ SimDiagram
     ▪ TopLevelDiagram
   ▪ MathDiagram
  ▪ Constant
   ▪ AbsTimeConstant
   ▪ ArrayConstant
   ▪ BooleanConstant
   ▪ ClusterConstant
   ▪ ColorBoxConstant
   ▪ FixedConstant
   ▪ IONameConstant
     ▪ DAQChannelNameConstant
     ▪ DAQmxNameConstant
     ▪ DSCTagConstant
     ▪ GenClassTagFlatRefConstant
     ▪ GenClassTagRefConstant
     ▪ IVILogicalNameConstant
     ▪ VISAResourceNameConstant
   ▪ LabVIEWClassConstant
   ▪ MapConstant
   ▪ NumericConstant
     ▪ DigitalNumericConstant
     ▪ NamedNumericConstant
      ▪ EnumConstant
      ▪ RingConstant


                                                 © National Instruments 7505

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7505 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7506 ordinal=7506 -->
## Property and Method Reference

Property and Method Reference

        ▪ PathConstant
        ▪ RefNumConstant
          ▪ ClassSpecifierConstant
          ▪ GenClassRefConst
          ▪ TypedRefNumConstant
           ▪ DataValRefNumConstant
        ▪ SetConstant
        ▪ StringConstant
          ▪ ComboBoxConstant
      ▪ Control
        ▪ AbsTime
        ▪ ActiveXContainer
        ▪ Array
        ▪ Boolean
        ▪ Cluster
          ▪ RadioButtonsControl
        ▪ ColorBox
        ▪ DigitalTable
        ▪ GraphChart
          ▪ IntensityChart
          ▪ IntensityGraph
          ▪ MixedSignalGraph
          ▪ WaveformChart
          ▪ WaveformGraph
           ▪ DigitalGraph
           ▪ XYGraph
        ▪ IOName
          ▪ DAQChannelName
          ▪ DAQmxName
          ▪ DSCTag
          ▪ GenClassTagFlatRef
          ▪ GenClassTagRef
          ▪ IVILogicalName
          ▪ VISAResourceName
        ▪ LVVariant
        ▪ LabVIEWClassControl
        ▪ ListBox


7506   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7506 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7507 ordinal=7507 -->
## Property and Method Reference

Property and Method Reference

  ▪ Map
  ▪ MixedCheckbox
  ▪ MultiSegmentPipe
  ▪ MulticolumnListbox
  ▪ Numeric
   ▪ ColorRamp
   ▪ Digital
   ▪ NamedNumeric
     ▪ Enum
     ▪ Ring
   ▪ NumericWithScale
     ▪ Knob
     ▪ Slide
  ▪ PageSelector
   ▪ TabControl
  ▪ Path
  ▪ Picture
  ▪ Pixmap
  ▪ PlugInControl
  ▪ PlugInDDODummyContainer
  ▪ RefNum
   ▪ GenClassRef
   ▪ LVObjectRefNum
     ▪ VIRefNum
   ▪ TypedRefNum
     ▪ DataValRefNum
  ▪ SceneGraphDisplay
  ▪ Scrollbar
  ▪ Set
  ▪ String
   ▪ ComboBox
  ▪ StubDDO
  ▪ SubPanel
  ▪ Table
  ▪ TreeControl
  ▪ WaveformData
▪ Decoration


                                              © National Instruments 7507

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7507 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7508 ordinal=7508 -->
## Property and Method Reference

Property and Method Reference

        ▪ Text
          ▪ NumericText
      ▪ FlatSequence
        ▪ TimeFlatSequence
      ▪ FlatSequenceInnerTunnel
      ▪ FlatSequenceOuterTunnel
      ▪ FormulaParameter
        ▪ MathScriptNodeParameter
        ▪ ScriptNodeParameter
      ▪ Node
        ▪ CallByRef
        ▪ ControlReferenceConstant
        ▪ FeedbackNode
        ▪ Formula
          ▪ InlineCNode
          ▪ MathScriptNode
          ▪ ScriptNode
        ▪ Function
          ▪ ArrayToCluster
          ▪ Comparison
           ▪ InRangeAndCoerce
          ▪ FileDialog
          ▪ FlattenUnflattenString
           ▪ FlattenString
          ▪ GPIBReadWrite
          ▪ ReadWriteFile
          ▪ TypeCast
        ▪ Global
        ▪ GrowableFunction
          ▪ AssertStructuralTypeMismatchNode
          ▪ BuildClusterArray
          ▪ BuildMapNode
          ▪ BuildSetNode
          ▪ Bundler
           ▪ BuildArray
           ▪ NamedBundler
          ▪ CIN


7508   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7508 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7509 ordinal=7509 -->
## Property and Method Reference

Property and Method Reference

  ▪ CallLibrary
  ▪ CompoundArithmetic
  ▪ FormatScanString
  ▪ IndexArray
  ▪ ObjectFunction
   ▪ Constructor
   ▪ Invoke
   ▪ Property
  ▪ RegisterForEvents
  ▪ Unbundler
   ▪ NamedUnbundler
▪ InPlaceBorderNode
  ▪ InPlaceArrayNode
  ▪ InPlaceArraySplitNode
  ▪ InPlaceClusterNode
  ▪ InPlaceDataValRefNode
  ▪ InPlaceElementNode
  ▪ InPlaceMapNode
  ▪ InPlaceVariantAttributeNode
  ▪ InPlaceVariantNode
▪ Local
▪ MathScriptCallByRef
▪ SharedVariableDynamicOpen
▪ SharedVariableDynamicRead
▪ SharedVariableDynamicWrite
▪ SharedVariableNode
▪ StaticVIReference
▪ Structure
  ▪ ClosureStructureNode
  ▪ InPlaceElementStructure
  ▪ Loop
   ▪ ForLoop
   ▪ WhileLoop
     ▪ TimedLoop
  ▪ MultiFrameStructure
   ▪ CaseStructure
   ▪ DisableStructure


                                           © National Instruments 7509

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7509 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7510 ordinal=7510 -->
## Property and Method Reference

Property and Method Reference

           ▪ EventStructure
           ▪ RaceStructureNode
           ▪ Sequence
             ▪ ExternalNode
          ▪ SimulationNode
          ▪ StatechartStructureNode
           ▪ ForkNode
           ▪ JoinNode
           ▪ JunctionNode
           ▪ RegionNode
           ▪ StateNode
          ▪ SynchronousDataFlowNode
          ▪ TargetStructureNode
          ▪ TimedSequence
        ▪ SubVI
          ▪ AbstractDynamicDispatch
           ▪ CallParentNode
           ▪ DynamicDispatchSubVI
          ▪ ConfNode
          ▪ GenericSubVI
          ▪ PolymorphicSubVI
        ▪ TextBaseNode
          ▪ ExpressionNode
        ▪ UnitCast
        ▪ XNode
          ▪ XDataNode
      ▪ Pane
      ▪ Panel
      ▪ PolymorphicVISelector
      ▪ PropertyItem
      ▪ Scale
        ▪ ColorGraphScale
        ▪ ColorScale
          ▪ RotaryColorScale
        ▪ GraphScale
        ▪ SlideScale
      ▪ SequenceLocal


7510   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7510 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7511 ordinal=7511 -->
## Property and Method Reference

Property and Method Reference

   ▪ SimulationDCO
   ▪ Splitter
   ▪ SynchronousDataFlowDCO
   ▪ Terminal
    ▪ ControlTerminal
    ▪ InnerTerminal
    ▪ OuterTerminal
    ▪ ParameterTerminal
      ▪ OverridableParameterTerminal
   ▪ TimedStructDCO
   ▪ Tunnel
    ▪ ConditionalTunnel
      ▪ SelectorTunnel
    ▪ LeftShiftRegister
    ▪ LoopTunnel
    ▪ RegionTunnel
    ▪ RightShiftRegister
   ▪ Wire
 ◦ MasterWizard
 ◦ Page
 ◦ Plot
 ◦ Probe
 ◦ SubWizard
   ▪ CodeWizard
   ▪ ExternalEditorWizard
   ▪ StateDiagramWizard
• Project
• ProjectItem
 ◦ BuildSpecification
 ◦ LVClassPropDefFolder
 ◦ Library
   ▪ LVClassLibrary
   ▪ StatechartLibrary
   ▪ XInterfaceLibrary
    ▪ XControlLibrary
    ▪ XNodeLibrary
 ◦ LibraryData


                                                   © National Instruments 7511

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7511 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7512 ordinal=7512 -->
## Property and Method Reference

Property and Method Reference

     ◦ PropertyFolder
      ▪ XPropertyFolder
     ◦ TargetItem
            • Scene
     ◦ SceneDrawable
      ▪ SceneGeometry
        ▪ SceneBox
        ▪ SceneCone
        ▪ SceneCylinder
        ▪ SceneHeightField
        ▪ SceneMesh
        ▪ SceneSphere
      ▪ SceneText
     ◦ SceneNode
      ▪ SceneClipPlane
      ▪ SceneLight
      ▪ SceneObject
     ◦ SceneTexture
     ◦ SceneWindow
            • Variable
            • VI
     ◦ FacadeVI
     ◦ MethodVI
     ◦ PolymorphicVI
     ◦ SubsystemVI

      ApplicationApplication

       Application Methods

       Application Properties

       Application Events

       ApplicationApplication MethodsMethods


7512   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7512 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7513 ordinal=7513 -->
## Property and Method Reference

Property and Method Reference


Method                        Description

                       On Windows and macOS, brings the application windows to theBring To Front                                    front.

                            Launches the DataSocket Browser dialog box to establish aBrowse DataSocket                              connection to a DataSocket item.

                              Gets the operator VI associated with the specified class. ReturnsClass Operator:Get                            FALSE if it does not find the operator VI.

                          Removes the operator VI associated with the specified class.Class Operator:Remove                              Returns FALSE if it does not find the operator VI.

Class Operator:Remove All     Removes all operator VIs associated with all classes.

Class Operator:Set              Sets an operator VI for the specified class. Returns FALSE if it fails.

                                Deletes all VI object files from the object cache that a buildClear Application Builder Cache
                                  specification compiles.

Clear Compiled Object Cache    Deletes all compiled code in the User object cache.

Clipboard:Empty                Clears the clipboard.

                              Returns the image currently stored on the clipboard.

Clipboard:Get Image          The LabVIEW Run-Time Engine does not support the
                               Clipboard:Get Image method. If you include this method in a built
                                  application, the method does not work properly.

Clipboard:Read From Clipboard  Reads text from the system clipboard.

Clipboard:Write to Clipboard     Writes text to the system clipboard.

Connection
                            Checks if the VI Server connection is responsive.
Responsiveness:Check

Connection                    Gets and sets how often LabVIEW checks if a VI Server connection
Responsiveness:Information      is responsive.

Data Type Color                Returns the color associated with a data type.

Debug Connection:Close Debug  Closes the connection to the application or shared library
Connection                      specified in Debug Name.

Debug Connection:List
                              Returns the list of applications and shared libraries you can debug
Applications or Shared
                          on the computer specified by Server Address.
Libraries

                                                    © National Instruments 7513

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7513 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7514 ordinal=7514 -->
## Property and Method Reference

Property and Method Reference


       Method                        Description

       Debug Connection:Open Debug Opens a connection to the application or shared library you can
        Connection                   debug.

                                       Returns a reference to the VI whose window is currently active
        Get Active VI Reference           (focused). If the active window is not a VI, this method returns
                              Not A Ref.

        Get Environment Mode Display                                       Returns the display name of the environment mode you specify.      Name

        Get VI Hierarchy Image Scaled   Gets the scaled image of the VI Hierarchy.

                                       Returns the bookmark information for the VI specified in VI Path.
                                   You do not need to load the VI into memory in order to read the
                                 bookmark information. This method returns an error if the VI is        Get VI:Bookmarks                                   password protected, if the VI is saved in an earlier version of
                                   LabVIEW and is not currently in memory, or if the VI does not have
                                   a block diagram.

                                       Returns the data type of the connector pane as variant data        Get VI:ConPane DataType                                      without loading the VI.

                                       Returns the description stored in the VI description field on the
                                    Documentation page of the VI Properties dialog box for the
        Get VI:Description                                           specified VI. Unlike the VI Description property, this method does
                                      not load the VI into memory.

                                       Returns the version of LabVIEW that last saved the VI. The version
                                           of LabVIEW that last saved the VI might be different from the file
                                      format version of the VI. For example, if you use LabVIEW 9.0.1 to
                                      save a VI, the VI has a file format version of 9.0.

                                   To obtain the file format version of the VI, use the Get VI:Version
                                   method.        Get VI:Editor Version
                                   LabVIEW does not open the VI when retrieving the version
                                         information. If you specify a path to a file that is not a VI, LabVIEW
                                         returns error 6559.

                                                                If the VI has "Separate compiled code from source file" set, then
                                              this method returns the current LabVIEW editor version.

                                       Returns Help path, Help tag, Help Used, and Help URL from the
        Get VI:Help Info
                                    Documentation page of the VI Properties dialog box for the

7514   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7514 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7515 ordinal=7515 -->
## Property and Method Reference

Property and Method Reference


Method                        Description

                                 specified VI. This method does not load the VI into memory.

                              Returns the icon of the specified VI without loading the VI intoGet VI:Icon                          memory.

Get VI:Is Probe                 Returns whether the specified VI is a probe without loading the VI.

                              Returns the qualified name of the referenced VI without loadingGet VI:Qualified Name                              the VI.

                              Returns the revision history that appears when you click the
                               Revision History button on the General page of the VI PropertiesGet VI:Revision History
                                dialog box of the specified VI. This method does not load the VI
                                  into memory.

                              Returns the name that appears in the title bar of the specified VI.Get VI:Title
                                This method does not load the VI into memory.

                              Returns the LabVIEW file format version of the VI. The file format
                                version of the VI might be different from the version of LabVIEW in
                            which the VI was last saved. For example, if you use LabVIEW 9.0.1
                                to save a VI, the VI has a file format version of 9.0.

Get VI:Version                To obtain the version of LabVIEW in which the VI was last saved,
                             use the Get VI:Editor Version method.

                           LabVIEW does not open the VI when retrieving the version
                                information. If you specify a path to a file that is not a VI, LabVIEW
                                returns error 6559.

                              Disconnects the open connection between LabVIEW and an RT
LVRT:Disconnect From Slave
                                    target.

                              Returns an array of names and an array of paths for all methods of
LabVIEW Class:All Methods of    a class. The methods of the class are member VIs that can be
LVClass                          called as subVIs. In other words, LabVIEW excludes global VIs,
                                 control VIs, and polymorphic VIs from the output arrays.

LabVIEW Class:Create           Creates a new LabVIEW class.

LabVIEW Class:Create Interface  Creates a new LabVIEW interface.

                              Returns the path to the VI that implements the specified method
LabVIEW Class:Get
                                within the specified class. If the specified class does not
Implementing VI Path
                           implement the method, this method returns an ancestor VI

                                                    © National Instruments 7515

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7515 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7516 ordinal=7516 -->
## Property and Method Reference

Property and Method Reference


       Method                        Description

                                      implementation.

        LabVIEW Class:Open          Opens the LabVIEW class specified by Path.

         Library:Create                  Creates a new LabVIEW project library.

         Library:Deploy Libraries        Deploys library files to the specified computer.

         Library:Deploy Library          Deploys a library file to the specified computer.

                                       Returns the LabVIEW file format version of the library. The file
                                      format version of the library might be different from the version of         Library:Get File LabVIEW                                   LabVIEW in which the library was last saved. For example, if you         Version
                                     use LabVIEW 9.0.1 to save a library, the library has a file format
                                         version of 9.0.

                                          Retrieves a reference to a LabVIEW project library that is already
         Library:Get Ref By Qualified                                     loaded within the application instance. If the library cannot be
      Name                                    found in memory, LabVIEW returns Not A Refnum.

         Library:Open                Opens the LabVIEW project library specified by Path.

         Library:Undeploy Libraries      Undeploys library files from the specified computer.

         Library:Undeploy Library      Removes a library from a target.

                                    Loads and compiles VIs in a directory, including VIs in        Mass Compile                                           subdirectories, for the specified application instance.

                                        Refreshes the File, Tools, and Help menus from disk        Menus:Refresh                                        programmatically.

                                          Validates the access control list with the current application user         NI Security:Get Access Rights                                      logged in.

         NI Security:Invoke Login Dialog  Invokes the NI Security Login dialog box programmatically.

         NI Security:Login              Logs a user into the NI domain.

                                     Logs the current user out of the NI domain and reverts to the
         NI Security:Logout
                                          default user.

                                        Creates a new LabVIEW document. This method achieves the
      New LabVIEW Document       same results as when you create a new document in the New
                                         dialog box.

        Open:LabVIEW Document      Opens a LabVIEW document.

                                 Opens the file specified by Index from the most recently used file
        Open:Recently Opened File
                                                            list.

7516   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7516 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7517 ordinal=7517 -->
## Property and Method Reference

Property and Method Reference


Method                        Description

                          Opens the project specified by Index from the most recently usedOpen:Recently Opened Project                                 project list.

                               Closes the Controls and Functions palette sets programmatically.
Palettes:Close All Palettes      To close the palette sets, add the Palettes:Close All Palettes
                         method to the block diagram and run the VI.

Palettes:Get Palette Item Path   Returns the path to the palette item you specify.

                            Updates the Controls and Functions palette set programmatically.

                           To update the palette set, place the Palettes:Refresh method on
                              the block diagram to the right of the Write Palette VI and run the
Palettes:Refresh                                         VI.

                                This method is similar to the Save Changes button on the Edit
                               Controls and Functions Palette Set dialog box.

                              Returns the LabVIEW file format version of the project. ThisProject:Get File LabVIEW                                version might be different from the version of LabVIEW in which
Version                              the project was last saved.

                               Creates a new, empty LabVIEW project. You also can use the
Project:New                                 Project Explorer window to create a new project.

                               Creates a new, empty LabVIEW project and prompts the user to
Project:New with Prompts                          add any open VIs from the main application instance.

                            Loads a LabVIEW project from disk. If the project is already in
                          memory, this method returns a reference to the existing project.
                           You can use this reference with the Project properties.Project:Open
                           You also can select File»Open Project to navigate to and open a
                                   project.

                            Loads a LabVIEW project from disk. If the project is already in
                          memory, this method returns an error. Within the loaded project,
                              the "source-only" setting on all VIs, all controls, and all libraries is
Project:Open And Suppress
                              suppressed. This means that anything loaded within the project
Source-Only
                                      will get a "has unsaved changes" mark if it needs to update itself
                                to match the LabVIEW version, the OS environment, or any of its
                            dependencies (subVIs, typedefs, etc).

                                                    © National Instruments 7517

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7517 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7518 ordinal=7518 -->
## Property and Method Reference

Property and Method Reference


       Method                        Description

                                       Gets the list of most recently used files from LabVIEW and displays
         Recently Opened:LV Files        the paths and filenames. This method returns the same list as if
                                   you selected File»Recent Files.

                                       Gets the list of most recently used LabVIEW projects from LabVIEW
         Recently Opened:LV Projects    and displays the paths and project names. This method returns
                                       the same list as if you selected File»Recent Projects.

                                       Returns control of the remote front panel to the server. The server       Remote Panel:Client Release                                         grants control to the next client in the queue or regains control if         Control
                                 no requests are in the queue.

       Remote Panel:Client Request                                      Requests control of the front panel of a VI on the server computer.         Control

       Remote Panel:Close                                        Closes a connection to a VI on the server computer.        Connection To Server

                                 Opens a connection to a server and displays the front panel of a VI       Remote Panel:Open                                 on the server computer. You also can request control of the front        Connection To Server
                                         panel.

                                         Quits and then restarts LabVIEW. This method is supported only
         Restart                                 on Windows.

        Scene:Drawable:Geometry:New  Creates a geometry that you can use to set an object in a 3D scene
        Box                             to a box.

        Scene:Drawable:Geometry:New  Creates a geometry that you can use to set an object in a 3D scene
       Cone                           to a cone.

        Scene:Drawable:Geometry:New  Creates a geometry that you can use to set an object in a 3D scene
         Cylinder                        to a cylinder.

        Scene:Drawable:Geometry:New
                                        Creates a new height field in a 3D scene.
        Height Field

        Scene:Drawable:Geometry:New
                                        Creates a new mesh in a 3D scene.
       Mesh

        Scene:Drawable:Geometry:New  Creates a geometry that you can use to set an object in a 3D scene
        Sphere                         to a sphere.

        Scene:Drawable:New Text       Creates a new text object in a 3D scene.

        Scene:New Clip Plane           Creates a new clip plane in a 3D scene.

        Scene:New Light                Creates a new light in a 3D scene.


7518   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7518 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7519 ordinal=7519 -->
## Property and Method Reference

Property and Method Reference


Method                        Description

Scene:New Object              Creates a new object in a 3D scene.

Scene:New Texture             Gets a reference to a texture to apply to a geometry in a 3D scene.

Scene:New Window             Creates a new window in which LabVIEW generates the 3D scene.

                            Reads a 3D scene file that you create with the Scene:Write Scene
Scene:Read Scene File            File method. The file being read must have a .lvsg or .dae
                                 extension.

                                Writes a new 3D scene file. The filename must end with a .lvsg
Scene:Write Scene File
                               or .dae extension.

Statechart:Create               Creates a new statechart. You must save the statechart to disk.

Statechart:Open             Opens the statechart specified by Path.

User Interaction:Hilight Palette  Opens the Controls or Functions palette and highlights the
Menu Item                       specified control or function.

                              Simulates the user selecting a menu item. In general, this methodUser Interaction:Invoke Menu                            works on global menu items but not document-specific menu
Item                                 items, in which case the method fails silently.

                               Places an object on the cursor so the object is ready to add to the
User Interaction:Place Object                                  front panel window or the block diagram window. You can specifyOn Cursor                              the object using either style or path.

User Interaction:Place Palette    Places a palette object on the cursor so the object is ready to add
Object on Cursor                to the front panel window or the block diagram window.

                            Updates the Context Help window to show content for a palette
                                object you specify, similar to when you mouse over the palette
                       menu item. This method also returns a Boolean to indicate
User Interaction:Show Palette   whether the specified palette object is found. If the Context Help
Object Context Help          window is closed when this method runs, the Context Help
                         window displays the content for the specified palette object when
                           you open the Context Help window unless you moved the mouse
                            onto another item after the method runs.

                               Exports to a tagged text file all the User Interface related strings of
VIs Strings:Export
                              the VIs specified by VI Array.

                              Imports to a tagged text file all the User Interface related strings of
VIs Strings:Import
                              the VIs specified by VI Array.

                               Configures the LabVIEW Web Server with the given file. If you do
Web Server:Configure
                              not wire Web Server to the configuration file, Web Server uses the

                                                    © National Instruments 7519

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7519 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7520 ordinal=7520 -->
## Property and Method Reference

Property and Method Reference


       Method                        Description

                                          default configuration file.

         XControl:Create                Creates an XControl library.

        XControl:Open              Opens an XControl library and returns a reference to it.

    BringBring ToTo FrontFront

     On Windows and macOS, brings the application windows to the front.

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                             Yes

       Remote access allowed                                             Yes

   BrowseBrowse DataSocketDataSocket

      Launches the DataSocket Browser dialog box to establish a connection to a
      DataSocket item.

     Parameters

                 Data
      Name           Required  Description
                 type

                                       Specifies the title of the DataSocket Browser dialog box. The default
       Prompt        No
                                                 is Browse for DataSocket Item.


7520   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7520 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7521 ordinal=7521 -->
## Property and Method Reference

Property and Method Reference


          Data Name           Required  Description
          type

 Selected               URL of the connection specified by the user in the DataSocket              No URL                     Browser dialog box.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                             Yes

 Remote access allowed                                  No

ClassClass Operator:GetOperator:Get

Gets the operator VI associated with the specified class. Returns FALSE if it does not
find the operator VI.

Parameters

 Name               Data type     Required     Description

 Class Name                          Yes         The class of the operator VI.


 Operator Name                      Yes        Name of the operator VI.


 VI Reference                         Yes         The reference to the operator VI.


                                                    © National Instruments 7521

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7521 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7522 ordinal=7522 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                                      Yes

         Available in Real-Time Operating System                                            Yes

       Remote access allowed                                             No

    ClassClass Operator:RemoveOperator:Remove

      Removes the operator VI associated with the specified class. Returns FALSE if it does
       not find the operator VI.

     Parameters

      Name               Data type     Required     Description

         Class Name                          Yes         The class of the operator VI.


        Operator Name                      Yes        Name of the operator VI.


          VI Reference                   No          The reference to the operator VI.


     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                                      Yes

         Available in Real-Time Operating System                                            Yes

7522   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7522 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7523 ordinal=7523 -->
## Property and Method Reference

Property and Method Reference


 Remote access allowed                                             No

ClassClass Operator:RemoveOperator:Remove AllAll

Removes all operator VIs associated with all classes.

Parameters

 Name                 Data type       Required       Description

 Operator Name                          Yes         Name of the operator VI.


Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                                      Yes

 Available in Real-Time Operating System                                            Yes

 Remote access allowed                                             No

ClassClass Operator:SetOperator:Set

Sets an operator VI for the specified class. Returns FALSE if it fails.

Parameters

 Name              Data type    Required    Description

 Class Name                        Yes        The class of the operator VI.


                                                    © National Instruments 7523

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7523 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7524 ordinal=7524 -->
## Property and Method Reference

Property and Method Reference


      Name              Data type    Required    Description

        Operator Name                    Yes       Name of the operator VI.


          VI Path                            Yes         Path to the operator VI.


        Old VI Reference               No          Reference to the previous operator VI.


     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                                      Yes

         Available in Real-Time Operating System                                            Yes

       Remote access allowed                                             No

    ClearClear ApplicationApplication BuilderBuilder CacheCache

       Deletes all VI object files from the object cache that a build specification compiles.

       This method is similar to selecting Application Builder from the Cache list in the Clear
      Compiled Object Cache dialog box and clicking the Delete button.

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

7524   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7524 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7525 ordinal=7525 -->
## Property and Method Reference

Property and Method Reference


 Remote access allowed                                             Yes

ClearClear CompiledCompiled ObjectObject CacheCache

Deletes all compiled code in the User object cache.

The User object cache contains the compiled code for the following kinds of files:

  • Files that have separate compiled code
  • VIs that you deploy to an RT target

This method is similar to selecting User from the Cache list in the Clear Compiled
Object Cache dialog box and clicking the Delete button.

      Note This method does not clear the Application Builder object cache. Use
       the Clear Application Builder Cache method to clear the Application Builder
        object cache programmatically.

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                              No

 Available in Real-Time Operating System                      No

 Remote access allowed                                             Yes

Clipboard:EmptyClipboard:Empty

Clears the clipboard.


                                                    © National Instruments 7525

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7525 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7526 ordinal=7526 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

       Remote access allowed                                             Yes

    Clipboard:GetClipboard:Get ImageImage

       Returns the image currently stored on the clipboard.

      The LabVIEW Run-Time Engine does not support the Clipboard:Get Image method. If
      you include this method in a built application, the method does not work properly.

     Parameters

                Data
      Name        Required  Description                type

                                    Specifies the color depth of the image, which is the number of bits to use
        Image                  No        to describe the color of each pixel in the image. Valid values include 1, 4,
        Depth
                         8 (default), and 24 bits per pixel.

                                   Array of bytes that describes the color of each pixel in the image in raster
                                     order. The value of Image Depth determines how LabVIEW interprets the
                                  value of this output.

                                                      If Image Depth is 24, each pixel has three bytes to describe its color. The
                                               first byte for each pixel describes the red value, the second byte        Image       No
                                  describes the green value, and the third byte describes the blue value.

                                                      If Image Depth is 8, each pixel has one byte to describe its color. The
                                  value of each bit corresponds to an element in colors, which stores
                                     32-bit RGB values where the most-significant byte is zero, followed in


7526   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7526 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7527 ordinal=7527 -->
## Property and Method Reference

Property and Method Reference


         Data Name        Required  Description
         type

                         order by red, green, and blue values.

                                         If Image Depth is 4, the behavior is similar to when Image Depth is 8
                         except valid values in Image include 0 through 15.

                                         If Image Depth is 1, any value of zero in Image corresponds to element 0
                             in colors. All other values correspond to element 1 in Colors.

                      The size of the array might be larger than expected due to padding.

                          Array of RGB color values that correspond to the values in Image. The
                          value of Image Depth determines how LabVIEW interprets the value of
 Colors       No         this output. If Image Depth is 24, LabVIEW ignores this output. If Image
                      Depth is 8, the array has 256 elements. If Image Depth is 4, the array has
                       16 elements. If Image Depth is 1, the array has 2 elements.


                         Returns the bounding rectangle of the image as top, left, bottom, and Bounds      No                             right values.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                             Yes

 Remote access allowed                                             Yes

Clipboard:ReadClipboard:Read FromFrom ClipboardClipboard

Reads text from the system clipboard.


                                                    © National Instruments 7527

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7527 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7528 ordinal=7528 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                                      Yes

         Available in Real-Time Operating System                                 No

       Remote access allowed                                             No

    Clipboard:WriteClipboard:Write toto ClipboardClipboard

       Writes text to the system clipboard.

     Parameters

      Name    Data type      Required      Description

         Text                      Yes             Text to write to the system clipboard.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                      No

       Remote access allowed                                  No

   ConnectionConnection Responsiveness:CheckResponsiveness:Check

      Checks if the VI Server connection is responsive.

7528   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7528 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7529 ordinal=7529 -->
## Property and Method Reference

Property and Method Reference

Use this method to check the status of a VI Server connection. If the connection is not
responsive, the method returns network connection error code 1130. The method
prompts the server for a message and considers the connection unresponsive if
LabVIEW does not receive a message within the time you specify in PingDelay. Use the
Connection Responsiveness:Information method to set PingDelay.

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                             Yes

 Remote access allowed                                             Yes

ConnectionConnection Responsiveness:InformationResponsiveness:Information

Gets and sets how often LabVIEW checks if a VI Server connection is responsive.

Set the PingDelay and PingTimeout parameters of this method to configure how
LabVIEW checks the connection. If LabVIEW does not receive a message in the time you
specify in PingDelay, LabVIEW sends a query to prompt the VI Server network
connection for a message. After sending the query, if LabVIEW does not receive a
message in the time you specified in PingTimeout, LabVIEW considers the connection
unresponsive. Then, all VIs and functions waiting on the connection return network
connection error code 1130.

For example, if you set PingDelay to 3000 and PingTimeout to 1000, LabVIEW sends
a query to verify the status of the VI Server network connection every time 3 seconds
elapse without LabVIEW receiving a message over the connection. If LabVIEW does not
receive a reply from the network, LabVIEW waits 1 second before all VIs and functions
waiting on the connection return network connection error 1130, which you can
handle on the block diagram.

Default for PingDelay and PingTimeout is 10,000 ms, which means LabVIEW checks

                                                    © National Instruments 7529

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7529 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7530 ordinal=7530 -->
## Property and Method Reference

Property and Method Reference

       the connection every 10 seconds and waits up to 10 seconds for the connection to
       respond.

           Note If a network operation times out according to the timeout value you
               specify in PingTimeout, LabVIEW considers the connection unresponsive but
             does not close the connection. All current and future calls waiting on the
              connection return a connection error. LabVIEW does not send another
            message to query the connection status until LabVIEW considers the
              connection responsive again. A connection becomes responsive again when
            LabVIEW receives a message over the connection.

     Parameters

                 Data      Name         Required  Description                 type

                                     Specifies how long between queries LabVIEW waits, in milliseconds. If
                              you specify a value of –1 (infinity) LabVIEW does not check the
        Ping                     connection unless you use the Connection Responsiveness:Check                  No        Delay                  method. If you want LabVIEW to check the connection, you must set
                                PingDelay to a positive number or use the Connection
                                 Responsiveness:Check method.

         Previous
        Ping         No       PingDelay in milliseconds you previously specified.
        Delay

                                     Specifies how long in milliseconds before LabVIEW times out after
        Ping                   LabVIEW sends a query to prompt the VI Server network connection for
                  No
        Timeout                a message. If a timeout occurs, all VIs and functions waiting on the
                                 connection return a connection unresponsive error.

         Previous
        Ping         No       PingTimeout in milliseconds you previously specified.
        Timeout


7530   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7530 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7531 ordinal=7531 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                             Yes

 Remote access allowed                                             Yes

DataData TypeType ColorColor

Returns the color associated with a data type.

Parameters

 Name       Data type    Required    Description

 Data Type                 Yes       Name of the data type whose color you want.


Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                                      Yes

 Available in Real-Time Operating System                                            Yes

 Remote access allowed                                                           Yes

DebugDebug Connection:CloseConnection:Close DebugDebug ConnectionConnection

Closes the connection to the application or shared library specified in Debug Name.

                                                    © National Instruments 7531

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7531 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7532 ordinal=7532 -->
## Property and Method Reference

Property and Method Reference

     Parameters

      Name            Data type   Required    Description

       Debug Name                   Yes

         Server Address                  Yes          IP address or computer name of the server.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

       Remote access allowed                                             Yes

   DebugDebug Connection:ListConnection:List ApplicationsApplications oror
   SharedShared LibrariesLibraries

       Returns the list of applications and shared libraries you can debug on the computer
       specified by Server Address.

     Parameters

                     Data
      Name                  Required  Description
                      type

         Server
                                  Yes        IP address or computer name of the server.
        Address


       Debug Names            Yes      Name(s) of the applications and shared libraries you can


7532   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7532 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7533 ordinal=7533 -->
## Property and Method Reference

Property and Method Reference


              Data Name                  Required  Description
               type

                                  debug.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                              No

 Available in Real-Time Operating System                      No

 Remote access allowed                                             Yes

DebugDebug Connection:OpenConnection:Open DebugDebug ConnectionConnection

Opens a connection to the application or shared library you can debug.

Parameters

 Name            Data type   Required    Description

 Debug Name                   Yes

 Server Address                  Yes          IP address or computer name of the server.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                              No


                                                    © National Instruments 7533

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7533 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7534 ordinal=7534 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                      No

       Remote access allowed                                             Yes

   GetGet ActiveActive VIVI ReferenceReference

       Returns a reference to the VI whose window is currently active (focused). If the active
      window is not a VI, this method returns Not A Ref.

     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                         No

         Available in Real-Time Operating System                                 No

       Remote access allowed                                                           Yes

   GetGet EnvironmentEnvironment ModeMode DisplayDisplay NameName

       Returns the display name of the environment mode you specify.

     Parameters

      Name     Data type       Required       Description

       Mode                      Yes              Specifies the environment mode.


     Remarks

      The following table lists the characteristics of this method.


7534   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7534 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7535 ordinal=7535 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Available in Run-Time Engine                                                      Yes

 Available in Real-Time Operating System                                            Yes

 Remote access allowed                                                           Yes

GetGet VIVI HierarchyHierarchy ImageImage ScaledScaled

Gets the scaled image of the VI Hierarchy.

Parameters

          Data Name          Required  Description           type

                              Indicates the color depth, or number of supported colors, of the Image                 Yes       image: 1 (1-bit, black and white), 4 (4-bit, 16 colors), 8 (8-bit, 256
 Depth                                colors), or 24 (24-bit, true color). The default is 8.

                            Information about the image so you can use the Draw Flattened
                        Pixmap VI to draw it as a picture or use the Graphics Formats VIs to
                          save the image to a file. This cluster is similar to the image data
                          output of the Read JPEG File, Read PNG File, and Read BMP File VIs.

                                            • image type—Reserved for future use.
                                            • image depth—Specifies the color depth of the image, which is the
                          number of bits to use to describe the color of each pixel in the
                               image. Valid values include 1, 4, 8, and 24 bits per pixel. image
 Image                      depth affects how LabVIEW interprets the values of image and                 Yes
 Data                              colors.
                                            • image—Array of bytes that describes the color of each pixel in the
                            image in raster order. The value of image depth determines how
                            LabVIEW interprets the value of this output.

                                                    If image depth is 24, each pixel has three bytes to describe its
                                     color. The first byte for each pixel describes the red value, the
                             second byte describes the green value, and the third byte
                                describes the blue value.


                                                    © National Instruments 7535

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7535 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7536 ordinal=7536 -->
## Property and Method Reference

Property and Method Reference


                  Data      Name          Required  Description
                  type

                                                                If image depth is 8, each pixel has one byte to describe its color.
                                  The value of each bit corresponds to an element in colors, which
                                           stores 32-bit RGB values where the most-significant byte is zero,
                                       followed in order by red, green, and blue values.

                                                                If image depth is 4, the behavior is similar to when image depth
                                                      is 8 except valid values in image include 0 through 15.

                                                                If image depth is 1, any value of zero in image corresponds to
                                    element 0 in colors. All other values correspond to element 1 in
                                            colors.

                                  The size of the array might be larger than expected due to
                                       padding.
                                                        • mask—Array of bytes in which each bit describes mask
                                        information for a pixel. The first byte describes the first eight
                                               pixels, the second byte describes the next eight pixels, and so on.
                                                                If a bit is zero, LabVIEW draws the corresponding pixel as
                                          transparent. If the array is empty, LabVIEW draws all pixels
                                      without transparency. If the array does not contain a bit for each
                                             pixel in the image, LabVIEW draws any pixels missing from the
                                          array without transparency.
                                                        • colors—Array of RGB color values that correspond to the values in
                                     image. The value of image depth determines how LabVIEW
                                            interprets the value of this output. If image depth is 24, LabVIEW
                                         ignores this output. If image depth is 8, the array has 256
                                       elements. If image depth is 4, the array has 16 elements. If image
                                   depth is 1, the array has 2 elements.
                                                        • Rectangle—Cluster that contains coordinates that describe the
                                   bounding rectangle of the image, where the upper-left corner is at
                                                   (0,0). The bottom right edges of the bounds does not include the
                                      image.


                                       Specifies the width of the returned image. If this input is 0, the width
                                      of the returned image is the same size as the default image when it is
       Maximum
                         Yes       displayed in the VI Hierarchy window. Also, LabVIEW cannot distort the
        Width
                                   returned image if the specifiedMaximum Width and Maximum Height
                                  parameters do not retain the same ratio as the default image.


7536   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7536 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7537 ordinal=7537 -->
## Property and Method Reference

Property and Method Reference


          Data Name          Required  Description
           type

                              Specifies the height of the returned image. If this input is 0, the height
                              of the returned image is the same size as the default image when it is Maximum                 Yes       displayed in the VI Hierarchy window. Also, LabVIEW cannot distort the Height
                           returned image if the specifiedMaximum Width and Maximum Height
                          parameters do not retain the same ratio as the default image.


                              Specifies the VI to highlight within the hierarchy image. In addition to VI To                 Yes       placing a purple border around the specified VI, LabVIEW expands or Highlight                             collapses the hierarchy to focus on the VI.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                             Yes

 Remote access allowed                                             Yes

GetGet VI:BookmarksVI:Bookmarks

Returns the bookmark information for the VI specified in VI Path. You do not need to
load the VI into memory in order to read the bookmark information. This method
returns an error if the VI is password protected, if the VI is saved in an earlier version of
LabVIEW and is not currently in memory, or if the VI does not have a block diagram.


                                                    © National Instruments 7537

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7537 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7538 ordinal=7538 -->
## Property and Method Reference

Property and Method Reference

     Parameters

                      Data      Name                Required  Description
                       type

          VI Path                Yes       Path to the VI whose help information you want to get.


       Bookmark                        Array of clusters that contain the bookmark ID, the bookmark                                Yes         Information                         tag, and the full text of the label.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                             Yes

       Remote access allowed                                             Yes

   GetGet VI:ConPaneVI:ConPane DataTypeDataType

       Returns the data type of the connector pane as variant data without loading the VI.

      Use the VIs in the labview\vi.lib\Utility\VariantDataType directory to
        retrieve information from the variant output.

           Note To ensure the information returned by this method is current, make
              sure the VI whose connector pane you reference has been recompiled in the
               current version of LabVIEW.


7538   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7538 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7539 ordinal=7539 -->
## Property and Method Reference

Property and Method Reference

Parameters

 Name                 Data type    Required     Description

 VI Path                                Yes          Path to the VI.


 ConPane DataType                     Yes          Data type of the connector pane.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                             Yes

 Remote access allowed                                             Yes

GetGet VI:DescriptionVI:Description

Returns the description stored in the VI description field on the Documentation page
of the VI Properties dialog box for the specified VI. Unlike the VI Description property,
this method does not load the VI into memory.

Parameters

 Name          Data type   Required   Description

 VI Path                      Yes        Path to the VI whose description you want to get.


 VI Description                Yes         Description of the VI.


                                                    © National Instruments 7539

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7539 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7540 ordinal=7540 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                             Yes

       Remote access allowed                                             Yes

   GetGet VI:EditorVI:Editor VersionVersion

       Returns the version of LabVIEW that last saved the VI. The version of LabVIEW that last
      saved the VI might be different from the file format version of the VI. For example, if
      you use LabVIEW 9.0.1 to save a VI, the VI has a file format version of 9.0.

      To obtain the file format version of the VI, use the Get VI:Version method.

      LabVIEW does not open the VI when retrieving the version information. If you specify a
      path to a file that is not a VI, LabVIEW returns error 6559.

           If the VI has "Separate compiled code from source file" set, then this method returns
       the current LabVIEW editor version.

     Parameters

      Name            Data type   Required   Description

          VI Path                         Yes        Path to the VI whose version you want to get.


         Version Number                 Yes         Version number of the VI wired into VI Path.


7540   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7540 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7541 ordinal=7541 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                                      Yes

 Available in Real-Time Operating System                                            Yes

 Remote access allowed                                                           Yes

GetGet VI:HelpVI:Help InfoInfo

Returns Help path, Help tag, Help Used, and Help URL from the Documentation page
of the VI Properties dialog box for the specified VI. This method does not load the VI
into memory.

Parameters

       Data Name       Required  Description
       type

 VI              Yes       Path to the VI whose help information you want to get. Path

 VI
                      Help path of the VI. The help path is located on the Documentation page Help       No
                          of the VI Properties dialog box.
 Path


                      Help tag of the VI. The help tag links a VI to a specific topic within a
 VI
                      compiled help file or links a VI to a bookmark within an HTML help file.
 Help       No
                     The help tag is located on the Documentation page of the VI Properties
 Tag
                         dialog box.

 VI
 Help                Web-based URL of the help file for the VI. The help URL is located on the
          No
 Web                 Documentation page of the VI Properties dialog box.
 URL

                                                    © National Instruments 7541

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7541 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7542 ordinal=7542 -->
## Property and Method Reference

Property and Method Reference


              Data      Name       Required  Description
               type

        Use                     Indicates whether to link to a web-based help file from the Detailed help
      Web       No         link in theContext Help window for a VI.Web URL is located on the
       URL                  Documentation page of the VI Properties dialog box.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                             Yes

       Remote access allowed                                             Yes

   GetGet VI:IconVI:Icon

       Returns the icon of the specified VI without loading the VI into memory.

     Parameters

      Name    Data type     Required     Description

        Path                    Yes          Path to the VI whose icon you want to get.


     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                                      Yes

7542   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7542 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7543 ordinal=7543 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                                 No

 Remote access allowed                                                           Yes

GetGet VI:IsVI:Is ProbeProbe

Returns whether the specified VI is a probe without loading the VI.

Parameters

 Name    Data type   Required   Description

 VI Path                Yes        Path to the VI whose help information you want to get.


 Is Probe               Yes        Returns whether the VI is a probe.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                              No

 Available in Real-Time Operating System                      No

 Remote access allowed                                             Yes

GetGet VI:QualifiedVI:Qualified NameName

Returns the qualified name of the referenced VI without loading the VI.


                                                    © National Instruments 7543

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7543 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7544 ordinal=7544 -->
## Property and Method Reference

Property and Method Reference

     Parameters

      Name            Data type  Required  Description

          VI Path                       Yes       Path to the VI whose help information you want to get.


          VI Qualified Name             Yes        Qualified name of the VI.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                             Yes

       Remote access allowed                                             Yes

   GetGet VI:RevisionVI:Revision HistoryHistory

       Returns the revision history that appears when you click the Revision History button
      on the General page of the VI Properties dialog box of the specified VI. This method
      does not load the VI into memory.

     Parameters

      Name           Data type  Required  Description

          VI Path                      Yes       Path to the VI whose help information you want to get.


         Revision History              Yes        Revision history of the VI.


7544   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7544 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7545 ordinal=7545 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                             Yes

 Remote access allowed                                             Yes

GetGet VI:TitleVI:Title

Returns the name that appears in the title bar of the specified VI. This method does not
load the VI into memory.

Parameters

 Name    Data type    Required    Description

 VI Path                Yes         Path to the VI whose window title you want to get.


 VI Title                Yes        Window title of the VI.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                             Yes

 Remote access allowed                                             Yes


                                                    © National Instruments 7545

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7545 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7546 ordinal=7546 -->
## Property and Method Reference

Property and Method Reference

   GetGet VI:VersionVI:Version

       Returns the LabVIEW file format version of the VI. The file format version of the VI
      might be different from the version of LabVIEW in which the VI was last saved. For
      example, if you use LabVIEW 9.0.1 to save a VI, the VI has a file format version of 9.0.

      To obtain the version of LabVIEW in which the VI was last saved, use the Get VI:Editor
       Version method.

      LabVIEW does not open the VI when retrieving the version information. If you specify a
      path to a file that is not a VI, LabVIEW returns error 6559.

     Parameters

      Name            Data type   Required   Description

          VI Path                         Yes        Path to the VI whose version you want to get.


         Version Number                 Yes         Version number of the VI wired into VI Path.


     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                                      Yes

         Available in Real-Time Operating System                                            Yes

       Remote access allowed                                                           Yes

   LVRT:DisconnectLVRT:Disconnect FromFrom SlaveSlave

       Disconnects the open connection between LabVIEW and an RT target.

7546   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7546 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7547 ordinal=7547 -->
## Property and Method Reference

Property and Method Reference

This is equivalent to right-clicking the target in the project and selecting Disconnect
from the shortcut menu. This method applies to Real-Time Module applications only.

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                              No

 Available in Real-Time Operating System                      No

 Remote access allowed                                             Yes

LabVIEWLabVIEW Class:AllClass:All MethodsMethods ofof LVClassLVClass

Returns an array of names and an array of paths for all methods of a class. The
methods of the class are member VIs that can be called as subVIs. In other words,
LabVIEW excludes global VIs, control VIs, and polymorphic VIs from the output arrays.

Parameters

         Data Name        Required  Description
         type

 Method                         Returns an array of filenames for all methods of the class, including File           Yes
                      methods of ancestor classes.
 Names


 Method                 Returns an array of paths to all methods of the class, including methods
               Yes
 Paths                     of ancestor classes.


                            Specifies the path to the .lvclass file for the class whose methods
 LVClass                you want to access. If the class is not in memory, this method will not               Yes
 Path                     return the expected results because it will omit any malleable VI
                       methods.


                                                    © National Instruments 7547

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7547 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7548 ordinal=7548 -->
## Property and Method Reference

Property and Method Reference


                Data      Name        Required  Description
                type

                                    Specifies which methods LabVIEW returns. The default is only the public
                              methods.

                               0           invalid scope
         Access                  No        1          public        Scope
                               2          private

                               3          protected

                               4        community


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                             Yes

       Remote access allowed                                             Yes

   LabVIEWLabVIEW Class:CreateClass:Create

       Creates a new LabVIEW class.

     Parameters

                     Data
      Name              Required  Description
                      type

         Create:Default
                      No        Specifies whether you want to set a default palette for all VIs the
         Palette


7548   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7548 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7549 ordinal=7549 -->
## Property and Method Reference

Property and Method Reference


              Data Name              Required  Description
               type

                            LabVIEW class owns. The default is FALSE, which does not set a
                                  default palette.


                                  Specifies the name of the LabVIEW class. If you do not wire the
 Name            No     Name input, a dialog box appears at run time prompting the user
                                 to name the new class.

 Directory         No

Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                         No

 Available in Real-Time Operating System                                 No

 Remote access allowed                                                           Yes

LabVIEWLabVIEW Class:CreateClass:Create InterfaceInterface

Creates a new LabVIEW interface.

Parameters

                  Data
 Name                     Required  Description
                   type

 Create:Default                            Specifies whether to create a default palette to save the
                      No
 Palette                                     interface.


                                                    © National Instruments 7549

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7549 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7550 ordinal=7550 -->
## Property and Method Reference

Property and Method Reference


                         Data      Name                     Required  Description
                          type

      Name                 No        Specifies the name of the interface.

         Directory               No

     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                         No

         Available in Real-Time Operating System                                 No

       Remote access allowed                                                           Yes

   LabVIEWLabVIEW Class:GetClass:Get ImplementingImplementing VIVI PathPath

       Returns the path to the VI that implements the specified method within the specified
        class. If the specified class does not implement the method, this method returns an
       ancestor VI implementation.

     Parameters

                Data
      Name          Required  Description
                 type

        Path To                   Returns the path to the VI that implements the method specified by
                         Yes
          VI                        the Path To Class and Method Name inputs.


        Path To                     Specifies the path to the .lvclass file in memory whose method                         Yes
         Class                    implementation you want to locate.


7550   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7550 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7551 ordinal=7551 -->
## Property and Method Reference

Property and Method Reference


         Data Name          Required  Description
         type

 Method                     Specifies the filename of the method for which you want to know the                 Yes Name                   implementing VI.


                             Specifies which VIs LabVIEW returns. The default is only public VIs.

                         0           invalid scope
 Access                   1          public                 Yes Scope                         2          private

                         3         protected

                         4        community


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                             Yes

 Remote access allowed                                             Yes

LabVIEWLabVIEW Class:OpenClass:Open

Opens the LabVIEW class specified by Path.


                                                    © National Instruments 7551

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7551 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7552 ordinal=7552 -->
## Property and Method Reference

Property and Method Reference

     Parameters

      Name   Data type    Required    Description

        Path                  Yes           Specifies the path to the LabVIEW class to open.


     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                         No

         Available in Real-Time Operating System                                 No

       Remote access allowed                                                           Yes

    Library:CreateLibrary:Create

       Creates a new LabVIEW project library.

     Parameters

                     Data
      Name              Required  Description                      type

                                           Specifies whether you want to set a default palette for all VIs the
         Create:Default
                      No        project library owns. The default is FALSE, which does not set a
         Palette
                                          default palette.


     Remarks

      The following table lists the characteristics of this method.


7552   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7552 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7553 ordinal=7553 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Available in Run-Time Engine                                         No

 Available in Real-Time Operating System                                 No

 Remote access allowed                                                           Yes

Library:DeployLibrary:Deploy LibrariesLibraries

Deploys library files to the specified computer.

If you deploy a library programmatically that contains both shared variables and VIs,
LabVIEW generates error code 1 and does not deploy the library to the engine. Deploy
the library manually to avoid the error.

Parameters

          Data Name          Required  Description           type

 Library                 Yes        Specifies the paths to each library. Paths


                              Specifies the IP address of the target where the library is deployed. If
 Target             No       you do not wire this input, the method deploys the library file to the IPAddress                               local computer.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                      No

 Remote access allowed                                             Yes

                                                    © National Instruments 7553

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7553 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7554 ordinal=7554 -->
## Property and Method Reference

Property and Method Reference

    Library:DeployLibrary:Deploy LibraryLibrary

      Deploys a library file to the specified computer.

           If you deploy a library programmatically that contains both shared variables and VIs,
      LabVIEW generates error code 1 and does not deploy the library to the engine. Deploy
       the library manually to avoid the error.

     Parameters

                  Data      Name          Required  Description                  type

         Library                         Yes        Specifies the path to the library.        Path


                                      Specifies the IP address of the target where the library is deployed. If         Target
                   No       you do not wire this input, the method deploys the library file to the         IPAddress                                        local computer.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                      No

       Remote access allowed                                             Yes

    Library:GetLibrary:Get FileFile LabVIEWLabVIEW VersionVersion

       Returns the LabVIEW file format version of the library. The file format version of the
        library might be different from the version of LabVIEW in which the library was last


7554   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7554 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7555 ordinal=7555 -->
## Property and Method Reference

Property and Method Reference

saved. For example, if you use LabVIEW 9.0.1 to save a library, the library has a file
format version of 9.0.

Parameters

 Name               Data type     Required     Description

 Lib Path                              Yes            Specifies the path to the library.


 Version Number                 No           Returns the version number.


Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                                      Yes

 Available in Real-Time Operating System                                            Yes

 Remote access allowed                                                           Yes

Library:GetLibrary:Get RefRef ByBy QualifiedQualified NameName

Retrieves a reference to a LabVIEW project library that is already loaded within the
application instance. If the library cannot be found in memory, LabVIEW returns Not
A Refnum.

Parameters

            Data
 Name              Required  Description
            type

 Qualified
                     Yes        Qualified name of the project library to which you want LabVIEW
 Name


                                                    © National Instruments 7555

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7555 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7556 ordinal=7556 -->
## Property and Method Reference

Property and Method Reference


                   Data      Name              Required  Description
                    type

                                         to return a reference.


     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                                      Yes

         Available in Real-Time Operating System                                            Yes

       Remote access allowed                                             No

    Library:OpenLibrary:Open

      Opens the LabVIEW project library specified by Path.

     Parameters

      Name   Data type    Required    Description

        Path                  Yes           Specifies the path to the project library to open.


     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                                      Yes

         Available in Real-Time Operating System                                 No


7556   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7556 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7557 ordinal=7557 -->
## Property and Method Reference

Property and Method Reference


 Remote access allowed                                                           Yes

Library:UndeployLibrary:Undeploy LibrariesLibraries

Undeploys library files from the specified computer.

Parameters

 Name               Data type     Required     Description

 Library Paths                        Yes           Specifies the paths to each library.


 Target IPAddress                No            IP address of the computer.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                      No

 Remote access allowed                                             Yes

Library:UndeployLibrary:Undeploy LibraryLibrary

Removes a library from a target.


                                                    © National Instruments 7557

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7557 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7558 ordinal=7558 -->
## Property and Method Reference

Property and Method Reference

     Parameters

                  Data      Name          Required  Description
                  type

         Library                         Yes        Specifies the path to the library.        Path


                                      Specifies the IP address of the target where the library is deployed. If         Target                   No       you do not wire this input, the method deploys the library file to the         IPAddress                                        local computer.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                      No

       Remote access allowed                                             Yes

   MassMass CompileCompile

      Loads and compiles VIs in a directory, including VIs in subdirectories, for the specified
       application instance.

       This method is similar to the Mass Compile option in the Mass Compile dialog box.


7558   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7558 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7559 ordinal=7559 -->
## Property and Method Reference

Property and Method Reference

Parameters

          Data Name          Required  Description
          type

 Directory
 to              Yes        Specifies the directory where the mass compile should begin.
 Compile

 Log File                     Specifies a file path where results of the mass compile should be             No Path                       placed. The default is no file.


 Append                             Specifies whether results should be appended to the log file. The to Log        No                             default is FALSE.
 File

 Number                             Specifies the number of VIs that should be allowed to remain in of VIs to       No                     memory during the mass compile. The default is none.
 Cache


                                            If TRUE, causes CINs in VIs to be ignored and the application to search Reload             No         for them. Useful when a large number of CINs have been recompiled LVSBs
                       and need to be reloaded. The default is FALSE.


 User             No        Indicates whether the user stopped the mass compile operation. Stopped

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                              No

 Available in Real-Time Operating System                      No

 Remote access allowed                                             Yes


                                                    © National Instruments 7559

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7559 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7560 ordinal=7560 -->
## Property and Method Reference

Property and Method Reference

   Menus:RefreshMenus:Refresh

       Refreshes the File, Tools, and Help menus from disk programmatically.

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

       Remote access allowed                                  No

    NINI Security:GetSecurity:Get AccessAccess RightsRights

       Validates the access control list with the current application user logged in.

     Parameters

                Data      Name        Required  Description
                type

         Access                   Displays the access rights granted to specific users and groups. If a user
         Control        Yes      and a group that the user is a member of both appear in the list,
           List                   LabVIEW uses the setting granting the greatest level of access.


         Access
                       Yes        Indicates the level of access for the current user logged in.
         Rights

     Remarks

      The following table lists the characteristics of this method.


7560   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7560 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7561 ordinal=7561 -->
## Property and Method Reference

Property and Method Reference


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                             Yes

 Remote access allowed                                  No

NINI Security:InvokeSecurity:Invoke LoginLogin DialogDialog

Invokes the NI Security Login dialog box programmatically.

Parameters

             Data Name             Required  Description             type

 Password                                 Specifies when the password is set to expire. You can configure the Expiration          Yes                           password expiration time using the Domain Account Manager.
 Time

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                      No

 Remote access allowed                                  No

NINI Security:LoginSecurity:Login

Logs a user into the NI domain.


                                                    © National Instruments 7561

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7561 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7562 ordinal=7562 -->
## Property and Method Reference

Property and Method Reference

     Parameters

                    Data      Name             Required  Description
                     type

                                          Specifies the domain to which you want to log in. You can configure         NI Domain          Yes                                      the domain using the Domain Account Manager.


                                 The name used to log in to the domain. You can configure the user        User Name         Yes                             name using the Domain Account Manager.


                                 The password used to log in to the domain. You can configure the        Password           Yes
                                  password using the Domain Account Manager.


        Password                                          Specifies when the password is set to expire. You can configure the         Expiration          Yes
                                  password expiration time using the Domain Account Manager.       Time

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                             Yes

       Remote access allowed                                  No

    NINI Security:LogoutSecurity:Logout

      Logs the current user out of the NI domain and reverts to the default user.


7562   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7562 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7563 ordinal=7563 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                             Yes

 Remote access allowed                                  No

NewNew LabVIEWLabVIEW DocumentDocument

Creates a new LabVIEW document. This method achieves the same results as when
you create a new document in the New dialog box.

Parameters

              Data Name                Required  Description              type

                                     Specifies the type of document you want to create.

                               0   VI

                               1   Global

                               2  Custom Control

                               3  Run-time Menu
 File Type               Yes
                               4  Polymorphic VI

                               5   Project

                               6   VI Template

                               7   Global Template

                               8   Control Template


                                                    © National Instruments 7563

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7563 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7564 ordinal=7564 -->
## Property and Method Reference

Property and Method Reference


                     Data      Name                Required  Description
                     type


                                              Simulation Subsystem (requires Control Design and                                       9                                              Simulation Module)

                                       10  Statechart (requires Statechart Module)

                                       11 Ladder Diagram (if supported)


         Parent                        No        Specifies the LabVIEW project to contain the new document.         Reference

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

       Remote access allowed                                             Yes

   Open:LabVIEWOpen:LabVIEW DocumentDocument

      Opens a LabVIEW document.

       This method is similar to selecting File»Open and browsing to the document.

     Parameters

                   Data
      Name            Required  Description
                    type

        Path              Yes       Path to the file you want to open.


7564   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7564 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7565 ordinal=7565 -->
## Property and Method Reference

Property and Method Reference


            Data Name            Required  Description
            type

                                               If TRUE, LabVIEW might display dialog boxes while opening the file. Interactive?      No                             For example, LabVIEW might prompt you to locate missing subVIs.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                              No

 Available in Real-Time Operating System                      No

 Remote access allowed                                             Yes

Open:RecentlyOpen:Recently OpenedOpened FileFile

Opens the file specified by Index from the most recently used file list.

Parameters

 Name  Data type   Required   Description

 Index               Yes         Specifies the index of the file or project you want to open.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes


                                                    © National Instruments 7565

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7565 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7566 ordinal=7566 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                             Yes

       Remote access allowed                                             Yes

   Open:RecentlyOpen:Recently OpenedOpened ProjectProject

      Opens the project specified by Index from the most recently used project list.

     Parameters

      Name  Data type   Required   Description

         Index               Yes         Specifies the index of the file or project you want to open.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                             Yes

       Remote access allowed                                             Yes

    Palettes:ClosePalettes:Close AllAll PalettesPalettes

       Closes the Controls and Functions palette sets programmatically. To close the palette
        sets, add the Palettes:Close All Palettes method to the block diagram and run the VI.

     Remarks

      The following table lists the characteristics of this method.


7566   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7566 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7567 ordinal=7567 -->
## Property and Method Reference

Property and Method Reference


 Data type                                            No return value

 Available in Run-Time Engine                              No

 Available in Real-Time Operating System                      No

 Remote access allowed                                  No

Palettes:GetPalettes:Get PalettePalette ItemItem PathPath

Returns the path to the palette item you specify.

Parameters

 Name                   Data type      Required      Description

 Palette Item Name                   No         Name of the palette item.


Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                                      Yes

 Available in Real-Time Operating System                                            Yes

 Remote access allowed                                                           Yes

Palettes:RefreshPalettes:Refresh

Updates the Controls and Functions palette set programmatically.

To update the palette set, place the Palettes:Refresh method on the block diagram to
the right of the Write Palette VI and run the VI.


                                                    © National Instruments 7567

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7567 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7568 ordinal=7568 -->
## Property and Method Reference

Property and Method Reference

       This method is similar to the Save Changes button on the Edit Controls and Functions
       Palette Set dialog box.

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

       Remote access allowed                                  No

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Application Control\Palette Editing API\
        Update Palette.vi
    Project:GetProject:Get FileFile LabVIEWLabVIEW VersionVersion

       Returns the LabVIEW file format version of the project. This version might be different
      from the version of LabVIEW in which the project was last saved.

     Parameters

      Name               Data type     Required     Description

         Project Path                         Yes            Specifies the path to the project.


         Version Number                 No           Returns the version number.


7568   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7568 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7569 ordinal=7569 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                                      Yes

 Available in Real-Time Operating System                                            Yes

 Remote access allowed                                                           Yes

Project:NewProject:New

Creates a new, empty LabVIEW project. You also can use the Project Explorer window
to create a new project.

Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                         No

 Available in Real-Time Operating System                                 No

 Remote access allowed                                                           Yes

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Application Control\VI Server\
   Manipulating Projects\Add Files to Project.vi


                                                    © National Instruments 7569

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7569 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7570 ordinal=7570 -->
## Property and Method Reference

Property and Method Reference

   Project:NewProject:New withwith PromptsPrompts

       Creates a new, empty LabVIEW project and prompts the user to add any open VIs from
       the main application instance.

     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                         No

         Available in Real-Time Operating System                                 No

       Remote access allowed                                                           Yes

   Project:OpenProject:Open

      Loads a LabVIEW project from disk. If the project is already in memory, this method
       returns a reference to the existing project. You can use this reference with the Project
       properties.

      You also can select File»Open Project to navigate to and open a project.

     Parameters

      Name        Data type           Required            Description

        Path                               Yes                Path to the project.


     Remarks

      The following table lists the characteristics of this method.


7570   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7570 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7571 ordinal=7571 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Available in Run-Time Engine                                                      Yes

 Available in Real-Time Operating System                                 No

 Remote access allowed                                                           Yes

Project:OpenProject:Open AndAnd SuppressSuppress Source-OnlySource-Only

Loads a LabVIEW project from disk. If the project is already in memory, this method
returns an error. Within the loaded project, the "source-only" setting on all VIs, all
controls, and all libraries is suppressed. This means that anything loaded within the
project will get a "has unsaved changes" mark if it needs to update itself to match the
LabVIEW version, the OS environment, or any of its dependencies (subVIs, typedefs,
etc).

Parameters

 Name          Data type              Required               Description

 Path                                     Yes

Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                         No

 Available in Real-Time Operating System                                 No

 Remote access allowed                                                           Yes

RecentlyRecently Opened:LVOpened:LV FilesFiles

Gets the list of most recently used files from LabVIEW and displays the paths and


                                                    © National Instruments 7571

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7571 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7572 ordinal=7572 -->
## Property and Method Reference

Property and Method Reference

       filenames. This method returns the same list as if you selected File»Recent Files.

     Parameters

      Name                          Data type    Required    Description

         Recently Opened File Paths                      Yes         Returns the list of file paths.


         Recently Opened File Names                     Yes         Returns the list of filenames.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

       Remote access allowed                                  No

    RecentlyRecently Opened:LVOpened:LV ProjectsProjects

       Gets the list of most recently used LabVIEW projects from LabVIEW and displays the
       paths and project names. This method returns the same list as if you selected
       File»Recent Projects.

     Parameters

      Name                         Data type  Required  Description

         Recently Opened Project Paths                 Yes        Returns the list of paths.


7572   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7572 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7573 ordinal=7573 -->
## Property and Method Reference

Property and Method Reference


 Name                         Data type  Required  Description

 Recently Opened Project Names               Yes        Returns the list of project filenames.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                              No

 Available in Real-Time Operating System                      No

 Remote access allowed                                  No

RemoteRemote Panel:ClientPanel:Client ReleaseRelease ControlControl

Returns control of the remote front panel to the server. The server grants control to the
next client in the queue or regains control if no requests are in the queue.

This method is similar to the Release Control of VI shortcut menu item.

This method can return networking error codes.

Parameters

         Data
 Name         Required  Description
         type

                   Name of the VI or project on the server. To specify a VI that is part of a
                       LabVIEW project, you must include the project name, the project library,
 VI                    and the target in the path of the VI, when applicable. For example, if
                Yes Name               MyVI.vi resides in a project called MyProject.lvproj under
                            target My Computer, enter the VI name as MyProject.lvproj/My
                    Computer/MyVI.vi. If the VI resides in a project library called


                                                    © National Instruments 7573

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7573 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7574 ordinal=7574 -->
## Property and Method Reference

Property and Method Reference


                Data      Name         Required  Description
                type

                           MyLibrary, also include the project library in the path, as in
                         MyProject.lvproj/My Computer/
                          MyLibrary.lvlib:MyVI.vi. If the VI is not in a project or project
                                         library, you can enter the VI name without any additional information.


         Server                        Yes        IP address or computer name of the server.        Address

         Server                        Yes       Port on which the Web Server is located.         Port

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                             Yes

       Remote access allowed                                  No

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Data Communication\Remote Panels\Remote
        Panel Methods.lvproj
   RemoteRemote Panel:ClientPanel:Client RequestRequest ControlControl

      Requests control of the front panel of a VI on the server computer.


7574   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7574 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7575 ordinal=7575 -->
## Property and Method Reference

Property and Method Reference

This method is similar to the Request Control of VI shortcut menu item.

This method can return networking error codes.

Parameters

         Data Name         Required  Description         type

                   Name of the VI or project on the server. To specify a VI that is part of a
                       LabVIEW project, you must include the project name, the project library,
                      and the target in the path of the VI, when applicable. For example, if
                   MyVI.vi resides in a project called MyProject.lvproj under
 VI                          target My Computer, enter the VI name as MyProject.lvproj/My                Yes Name               Computer/MyVI.vi. If the VI resides in a project library called
                     MyLibrary, also include the project library in the path, as in
                   MyProject.lvproj/My Computer/
                    MyLibrary.lvlib:MyVI.vi. If the VI is not in a project or project
                                library, you can enter the VI name without any additional information.


 Server                Yes        IP address or computer name of the server. Address

 Server                Yes       Port on which the Web Server is located. Port

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                             Yes

 Remote access allowed                                  No


                                                    © National Instruments 7575

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7575 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7576 ordinal=7576 -->
## Property and Method Reference

Property and Method Reference

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Data Communication\Remote Panels\Remote
        Panel Methods.lvproj
   RemoteRemote Panel:ClosePanel:Close ConnectionConnection ToTo ServerServer

       Closes a connection to a VI on the server computer.

       This method can return networking error codes.

     Parameters

                  Data      Name             Required  Description
                   type

                            Name of the VI or project path to the VI on the server whose          VI Name            Yes
                                     connection you want to close.


         Server                            Yes        IP address or computer name of the server.        Address

         Server                            Yes       Port on which the Web Server is located.
         Port

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                             Yes

       Remote access allowed                                  No

7576   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7576 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7577 ordinal=7577 -->
## Property and Method Reference

Property and Method Reference

RemoteRemote Panel:OpenPanel:Open ConnectionConnection ToTo ServerServer

Opens a connection to a server and displays the front panel of a VI on the server
computer. You also can request control of the front panel.

This method is similar to the Connect to Remote Panel dialog box.

This method can return networking error codes.

Parameters

            Data Name            Required  Description
            type

                     Name of the VI on the server to which you want to connect. To
                               specify a VI that is part of a LabVIEW project, you must include the
                               project name, the project library, and the target in the path of the VI,
                       when applicable. For example, if MyVI.vi resides in a project
                               called MyProject.lvproj under target My Computer, enter
 VI Name           Yes       the VI name as MyProject.lvproj/My Computer/MyVI.vi.
                                               If the VI resides in a project library called MyLibrary, also include
                             the project library in the path, as in MyProject.lvproj/My
                      Computer/MyLibrary.lvlib:MyVI.vi. If the VI is not in a
                               project or project library, you can enter the VI name without any
                               additional information.


 Server
                   Yes        IP address or computer name of the server.
 Address


 Server Port        Yes       Port on which the Web Server is located.


                                               If TRUE (default), the client requests control of the front panel
 Request                    immediately after opening a connection to the server. The server
              No
 Control                   queues the request if another client currently controls the front
                              panel.


                                                    © National Instruments 7577

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7577 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7578 ordinal=7578 -->
## Property and Method Reference

Property and Method Reference


                   Data      Name            Required  Description
                    type

        Secure                    No        Specifies whether to establish a secure connection.        Connection

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                             Yes

       Remote access allowed                                  No

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Data Communication\Remote Panels\Remote
        Panel Methods.lvproj
    RestartRestart

       Quits and then restarts LabVIEW. This method is supported only on Windows.

           Note When you invoke this method with unsaved files open, a dialog box
             prompts you to save any changes you made before the application
               terminates. If you cancel the dialog box, LabVIEW does not restart.

       This method is useful for restarting LabVIEW after you change the environment in a
     way that requires you to restart. For example, in an application that activates a license
        for a LabVIEW third-party add-on, you can use this method to programmatically restart
      LabVIEW, which then updates the status of the license.

7578   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7578 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7579 ordinal=7579 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                             Yes

 Remote access allowed                                             Yes

Scene:Drawable:Geometry:NewScene:Drawable:Geometry:New BoxBox

Creates a geometry that you can use to set an object in a 3D scene to a box.

Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                                      Yes

 Available in Real-Time Operating System                                            Yes

 Remote access allowed                                                           Yes

Scene:Drawable:Geometry:NewScene:Drawable:Geometry:New ConeCone

Creates a geometry that you can use to set an object in a 3D scene to a cone.

Remarks

The following table lists the characteristics of this method.


 Data type


                                                    © National Instruments 7579

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7579 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7580 ordinal=7580 -->
## Property and Method Reference

Property and Method Reference


         Available in Run-Time Engine                                                      Yes

         Available in Real-Time Operating System                                            Yes

       Remote access allowed                                                           Yes

   Scene:Drawable:Geometry:NewScene:Drawable:Geometry:New CylinderCylinder

       Creates a geometry that you can use to set an object in a 3D scene to a cylinder.

     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                                      Yes

         Available in Real-Time Operating System                                            Yes

       Remote access allowed                                                           Yes

   Scene:Drawable:Geometry:NewScene:Drawable:Geometry:New HeightHeight FieldField

       Creates a new height field in a 3D scene.

      The collection of values in the height field specify elevations at points above a grid.

     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                                      Yes

         Available in Real-Time Operating System                                            Yes

       Remote access allowed                                                           Yes


7580   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7580 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7581 ordinal=7581 -->
## Property and Method Reference

Property and Method Reference

Scene:Drawable:Geometry:NewScene:Drawable:Geometry:New MeshMesh

Creates a new mesh in a 3D scene.

The collection of polygons and vertices in the mesh define the shape of the 3D object.

Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                                      Yes

 Available in Real-Time Operating System                                            Yes

 Remote access allowed                                                           Yes

Scene:Drawable:Geometry:NewScene:Drawable:Geometry:New SphereSphere

Creates a geometry that you can use to set an object in a 3D scene to a sphere.

Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                                      Yes

 Available in Real-Time Operating System                                            Yes

 Remote access allowed                                                           Yes

Scene:Drawable:NewScene:Drawable:New TextText

Creates a new text object in a 3D scene.


                                                    © National Instruments 7581

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7581 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7582 ordinal=7582 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                                      Yes

         Available in Real-Time Operating System                                            Yes

       Remote access allowed                                                           Yes

   Scene:NewScene:New ClipClip PlanePlane

       Creates a new clip plane in a 3D scene.

      The clip plane defines values beyond which an object can or cannot be drawn. An
       object that encounters a clip plane will be cut off at the point at which it intersects the
       plane.

     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                                      Yes

         Available in Real-Time Operating System                                            Yes

       Remote access allowed                                                           Yes

   Scene:NewScene:New LightLight

       Creates a new light in a 3D scene.


7582   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7582 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7583 ordinal=7583 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                                      Yes

 Available in Real-Time Operating System                                            Yes

 Remote access allowed                                                           Yes

Scene:NewScene:New ObjectObject

Creates a new object in a 3D scene.

You must assign a geometry to the object before it can appear in the 3D scene.

Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                                      Yes

 Available in Real-Time Operating System                                            Yes

 Remote access allowed                                                           Yes

Scene:NewScene:New TextureTexture

Gets a reference to a texture to apply to a geometry in a 3D scene.

Remarks

The following table lists the characteristics of this method.


                                                    © National Instruments 7583

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7583 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7584 ordinal=7584 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Available in Run-Time Engine                                                      Yes

         Available in Real-Time Operating System                                            Yes

       Remote access allowed                                                           Yes

   Scene:NewScene:New WindowWindow

       Creates a new window in which LabVIEW generates the 3D scene.

     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                                      Yes

         Available in Real-Time Operating System                                            Yes

       Remote access allowed                                                           Yes

   Scene:ReadScene:Read SceneScene FileFile

      Reads a 3D scene file that you create with the Scene:Write Scene File method. The file
       being read must have a .lvsg or .dae extension.

           If you read a scene saved to disk with textures, this method attempts to load the
       textures from the location where Scene:Write Scene File created the external images.


7584   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7584 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7585 ordinal=7585 -->
## Property and Method Reference

Property and Method Reference

Parameters

       Data Name         Required  Description
       type

                            Specifies the filename for the 3D scene. The filename must end with a
 File            Yes                    .lvsg or .dae extension.


Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                                      Yes

 Available in Real-Time Operating System                                            Yes

 Remote access allowed                                                           Yes

Scene:WriteScene:Write SceneScene FileFile

Writes a new 3D scene file. The filename must end with a .lvsg or .dae extension.

If the scene includes textures, this method writes the textures as .png files to the
same directory as the .lvsg or .dae file. The filenames for the textures consist of an
enumerated integer followed by the name of the .lvsg or .dae file.

Parameters

       Data
 Name         Required  Description
       type

 Scene          Yes       Reference to a 3D scene.


                                                    © National Instruments 7585

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7585 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7586 ordinal=7586 -->
## Property and Method Reference

Property and Method Reference


              Data      Name         Required  Description
               type

                                     Specifies the filename for the 3D scene. The filename must end with a
           File            Yes                          .lvsg or .dae extension.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                             Yes

       Remote access allowed                                             Yes

    Statechart:CreateStatechart:Create

       Creates a new statechart. You must save the statechart to disk.

     Parameters

      Name    Data type     Required     Description

        Path                    Yes          Path where you want to save the statechart.


     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                         No


7586   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7586 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7587 ordinal=7587 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                                 No

 Remote access allowed                                                           Yes

Statechart:OpenStatechart:Open

Opens the statechart specified by Path.

Parameters

 Name    Data type     Required      Description

 Path                     Yes           Path to the statechart you want to open.


Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                         No

 Available in Real-Time Operating System                                 No

 Remote access allowed                                                           Yes

UserUser Interaction:HilightInteraction:Hilight PalettePalette MenuMenu ItemItem

Opens the Controls or Functions palette and highlights the specified control or
function.


                                                    © National Instruments 7587

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7587 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7588 ordinal=7588 -->
## Property and Method Reference

Property and Method Reference

     Parameters

                  Data      Name           Required  Description
                   type

       FuncName        Yes        Specifies the name of the control or function you want to highlight.


                                       Specifies the position on the screen for LabVIEW to open the palette.
         Position       No      The default is (0, 0), which opens the palette in the upper-left corner
                                       of the screen.


     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                         No

         Available in Real-Time Operating System                                 No

       Remote access allowed                                                           Yes

   UserUser Interaction:InvokeInteraction:Invoke MenuMenu ItemItem

       Simulates the user selecting a menu item. In general, this method works on global
     menu items but not document-specific menu items, in which case the method fails
         silently.

     Parameters

      Name             Data type    Required     Description

       Menu Item Tag                    Yes           Specifies the name of the menu item.


7588   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7588 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7589 ordinal=7589 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                      No

 Remote access allowed                                  No

UserUser Interaction:PlaceInteraction:Place ObjectObject OnOn CursorCursor

Places an object on the cursor so the object is ready to add to the front panel window
or the block diagram window. You can specify the object using either style or path.

This method enables you to access objects that do not exist on the Controls or
Functions palette. You can use the User Interaction:Place Palette Object on Cursor
method to access palette objects by name.

Parameters

         Data Name         Required  Description
         type

                            Specifies the palette object to place on the cursor. This parameter is the style        No
                     same as the style input in the New VI Object function.


                            Specifies the location on disk of the VI or control to place on the cursor.
 path        No
                                          If you wire anything non-zero to the style input, path is ignored.


                                          If TRUE, directs LabVIEW to place the contents of the VI, rather than the
                              VI itself, on the cursor. If the VI contains more than one block diagram
 mergeVI      No
                             object, LabVIEW places the VI on the cursor instead of its contents. You
                      must specify a path to a VI in path.


                                                    © National Instruments 7589

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7589 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7590 ordinal=7590 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                              No

         Available in Real-Time Operating System                      No

       Remote access allowed                                  No

   UserUser Interaction:PlaceInteraction:Place PalettePalette ObjectObject onon
   CursorCursor

       Places a palette object on the cursor so the object is ready to add to the front panel
      window or the block diagram window.

     Parameters

                         Data      Name                    Required  Description                         type

          Ctl or Function                          Specifies the name of the control or function to place on                                    Yes      Name                                the cursor.


     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                         No

         Available in Real-Time Operating System                                 No

       Remote access allowed                                                           Yes


7590   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7590 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7591 ordinal=7591 -->
## Property and Method Reference

Property and Method Reference

UserUser Interaction:ShowInteraction:Show PalettePalette ObjectObject
ContextContext HelpHelp

Updates the Context Help window to show content for a palette object you specify,
similar to when you mouse over the palette menu item. This method also returns a
Boolean to indicate whether the specified palette object is found. If the Context Help
window is closed when this method runs, the Context Help window displays the
content for the specified palette object when you open the Context Help window
unless you moved the mouse onto another item after the method runs.

Parameters

                 Data Name                    Required  Description                  type

 Ctl or Function                          Specifies the name of the control or function to place on                            Yes Name                                the cursor.


Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                         No

 Available in Real-Time Operating System                                 No

 Remote access allowed                                                           Yes

VIsVIs Strings:ExportStrings:Export

Exports to a tagged text file all the User Interface related strings of the VIs specified by
VI Array.


                                                    © National Instruments 7591

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7591 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7592 ordinal=7592 -->
## Property and Method Reference

Property and Method Reference

       Exports the following strings about VI and front panel objects to a tagged text file: VI
     name and description, object caption labels, object free labels, default data (string,
        table, path, and array default data), private data (listbox item names, table row and
      column headers, graph plot names, graph cursor names, graph annotation names, and
       tab control page captions), and polymorphic VI data (instance names in the
      polymorphic VI and selector shortcut menus).

     Parameters

                  Data      Name           Required  Description                   type

          VI Ref                          Yes       Path to an array of VI references.         Array


                                  Path to the VI strings file, including the filename. If you do not enter a
         String File        Yes       filename, set Interactive to TRUE so the user can set the VI strings
                                      filename.


                                       Specifies whether to display the file dialog box to select the name of          Interactive      No
                                    the strings file. The default value is FALSE.


                                  Path to the log file created to list errors that occur while exporting VI        Log File        No                                         strings to a tagged text file. The default value is no logging.


         Create                       Specifies whether control captions should be automatically created.
                    No
        Captions                 The default value is FALSE.


         Export                       Specifies whether to export block diagram strings. The default value
                    No
        Diagram                           is FALSE.


         Error
                    No       Returns an array of error clusters.
         Array


7592   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7592 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7593 ordinal=7593 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                              No

 Available in Real-Time Operating System                      No

 Remote access allowed                                             Yes

VIsVIs Strings:ImportStrings:Import

Imports to a tagged text file all the User Interface related strings of the VIs specified by
VI Array.

Imports the following strings about VI and front panel objects to a tagged text file: VI
name and description, object caption labels, object free labels, default data (string,
table, path, and array default data), private data (listbox item names, table row and
column headers, graph plot names, graph cursor names, graph annotation names, and
tab control page captions), and polymorphic VI data (instance names in the
polymorphic VI and selector shortcut menus).

Parameters

           Data Name           Required  Description
           type

 VI Ref
                  Yes       Path to an array of VI references.
 Array


                           Path to the VI strings file, including the filename. If you do not enter a
 String File        Yes       filename, set Interactive to TRUE so the user can set the VI strings
                             filename.


                                                    © National Instruments 7593

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7593 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7594 ordinal=7594 -->
## Property and Method Reference

Property and Method Reference


                  Data      Name           Required  Description
                   type

                                       Specifies whether to display the file dialog box to select the name of          Interactive      No                                    the strings file. The default value is FALSE.


                                  Path to the log file created to list errors that occur while importing VI        Log File        No                                         strings from a tagged text file. The default value is no logging.


         Error
                    No       Returns an array of error clusters.         Array

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                      No

       Remote access allowed                                             Yes

   WebWeb Server:ConfigureServer:Configure

       Configures the LabVIEW Web Server with the given file. If you do not wire Web Server
       to the configuration file, Web Server uses the default configuration file.

     Parameters

      Name             Data type  Required  Description

         Configuration File           No        Path to the file to use to configure the Web Server.


7594   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7594 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7595 ordinal=7595 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                             Yes

 Remote access allowed                                  No

XControl:CreateXControl:Create

Creates an XControl library.

Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                         No

 Available in Real-Time Operating System                                 No

 Remote access allowed                                                           Yes

XControl:OpenXControl:Open

Opens an XControl library and returns a reference to it.

Parameters

 Name        Data type           Required            Description

 Path                               Yes                 Path to the library.


                                                    © National Instruments 7595

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7595 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7596 ordinal=7596 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                         No

         Available in Real-Time Operating System                                 No

       Remote access allowed                                                           Yes

       ApplicationApplication PropertiesProperties

      Use the print properties to configure what is to be printed. Set all the custom printing
       properties because they default to their previous settings. To actually print VI
       information, you must use a VI Class print method.


        Property                      Description

         Application:Active:Application   Gets an application reference to the active VIs owning application.

          Application:Active:VI           Returns the name of the active VI in the application.

          Application:All Libraries in                                               Lists all Libraries currently in memory in this application instance.
         Application Instance

                                      Returns a list of VIs in memory for the specified application
                                           instance. This property returns an error if you wire a remote
          Application:All VIs In Memory    application reference to the reference input. For a remote
                                           application, use the Exported VIs in Memory property to return a
                                                         list of exported VIs.

         Application:Auto-Route Wires   Returns whether LabVIEW automatically finds a route for a wire.

        Application:Command Line     Returns an array of user-defined command-line arguments passed
        Arguments                when LabVIEW launched.

                                      Gets or sets how complex a VI must be before the compiler limits
                                        optimizations to improve editor responsiveness. If the complexity
         Application:Compiler
                                          of a VI is lower than the threshold indicated by this value, the
        Threshold
                                      compiler does not limit optimizations, thereby improving the
                                       execution speed of the VI. If the complexity of a VI is higher than


7596   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7596 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7597 ordinal=7597 -->
## Property and Method Reference

Property and Method Reference


Property                      Description

                              the threshold, the compiler limits optimizations in order to
                            improve editor responsiveness for the VI.

                           To determine the complexity of a specific VI, refer to the Compiled
                         Code Complexity value on the Memory Usage page of the VI
                                Properties dialog box or use the Compiled:Code Complexity
                                property.

                                This property provides programmatic access to the Compiler
                              optimizations slider on the Environment page of the Options
                                dialog box.

                              Returns the current environment mode of LabVIEW, such as
Application:Current          robotics. If you call this property from a VI in the LabVIEW
Environment Mode           development system environment, this property returns an empty
                                     string.

                              Returns the name used for opening a debugging connection to
Application:Debug Name         this application or shared library. This method is only useful in
                                    built applications or shared libraries.

Application:Default:Application Returns the default application reference.

Application:Default:Data                             Path to the default data directory.Directory

Application:Delete FP Terminal  Returns whether LabVIEW deletes terminals corresponding to
from Diagram                    front panel objects from diagram operations.

Application:Directory Path      Absolute path to the directory where the application is located.

Application:Exported VIs In
                              Returns a list of exported VIs in memory.
Memory

                                 Indicates the LabVIEW instance the VI is running in, including
Application:Kind
                                  invalid application types.

                                 Indicates the language of the LabVIEW environment or stand-
Application:Language          alone application as a string according to ISO 639. Values include
                            en, de, fr, ja, ko, and zh-cn.

                              Returns a reference to the application instance that launched the
Application:Menu Launch:App
                                   calling VI from a menu selection.

Application:Menu Launch:VI     Returns the name of the VI that launched the calling VI from a

                                                    © National Instruments 7597

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7597 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7598 ordinal=7598 -->
## Property and Method Reference

Property and Method Reference


        Property                      Description

                             menu selection.

        Application:Name             Filename of the application.

                                      Returns the version number of the LabVIEW file format to which
                                  LabVIEW documents are saved. This version number might be
         Application:Save Version         different from the version number of the application. For example,
                                  LabVIEW with the version number 9.0.1 saves LabVIEW documents
                                      with a file format version number of 9.0.

                                An array of the LabVIEW versions to which this version of LabVIEW
                                   can save. The array is in reverse chronological order, with the
         Application:Saveable Versions   zeroth element being the current version of LabVIEW. Each
                                    element of the array is a valid version to pass to VI server functions
                                   which save to previous versions.

                                         Writing the property: Setting this property to TRUE enables the
                                         display of tip strips on front panel controls. Setting the property to
         Application:Show FP Tip Strips  FALSE prevents them from being displayed. Reading the property:
                                           Specifies whether tip strips display when idling over controls on
                                      the front panel.

         Application:Target:CPU          Indicates the target CPU of an application.

         Application:Target:Data Cache   Returns an array of the entry sizes, in bytes, for all cache levels the
         Entry Sizes                  computer or target contains.

         Application:Target:Data Cache   Returns an array of the cache sizes, in bytes, for each cache level
         Sizes                         the computer or target contains.

         Application:Target:Number of   Returns the number of cores per package the computer or target
        Cores per Package              contains.

         Application:Target:Number of   Returns the number of processing units the computer or target
         Logical Processors              contains.

         Application:Target:Number of   Returns the number of logical processors per core the computer
         Logical Processors per Core     or target contains.

         Application:Target:Number of   Returns the number of packages, or chips, the computer or target
        Packages                       contains.

                                          Indicates the operating system for which the application was built.
         Application:Target:Operating
                               Mac OS refers to Mac OS versions 9 and 8. Carbon refers to Mac OS
        System
                                  X (32-bit).

         Application:User Interface           If you are not targeted to a real-time (RT) platform, this property is


7598   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7598 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7599 ordinal=7599 -->
## Property and Method Reference

Property and Method Reference


Property                      Description

                             always TRUE. If you are targeted to an RT-platform and the host is
                              connected, this property is TRUE. When this property is FALSE, the
                              host is not connected, requiring that the Real-Time ModuleAvailable                                application must be able to handle all operations independent of
                              the host. Use this property to determine when it is safe to display
                           a dialog box that requires user interaction.

Application:User Name         User name used to open the application.

Application:VI Of Top Most      Returns a reference to the block diagram highest in the Z order,
Block Diagram               which is most likely the last block diagram accessed.

                               Version number of the application. In a stand-alone application or
Application:Version Number    shared library, this property returns the version of the LabVIEW
                           Run-Time Engine.

                               Version year of the application. In a stand-alone application or
Application:Version Year        shared library, this property returns the version year of the
                           LabVIEW Run-Time Engine.

                             Determines whether the Debug Server is enabled. You can use thisDebug Server:Server Active                              property only in LabVIEW-built applications or shared libraries.

                                     List that describes which TCP/IP addresses of remote clients canDebug Server:TCP/IP Access                              access the Debug Server. You can use this property only in
List                               LabVIEW-built applications or shared libraries.

                              Returns information about all the monitors on the computer,
Display:All Monitors                                including their bit depths and bounding rectangles.

Display:Primary Workspace     Gives the bounding rectangle of the computer's primary monitor.

NI Security:Nobody Logged In?  Determines if anyone is logged in.

                                 Indicates the name of the user who is currently logged in, using
NI Security:User                              the format of <Domain Name>\<User Name>.

                               Build number of the actual operating system. This string returns
Operating System:Build       an alphanumeric value of the build number that you can use to
Number                    compare the build version of operating systems. This property is
                             read only.

                                Detailed name of the operating system where the application is
Operating System:Detailed
                                 actually running. This string value returns the operating system
Name
                          and its version. This property is similar to a combination of


                                                    © National Instruments 7599

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7599 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7600 ordinal=7600 -->
## Property and Method Reference

Property and Method Reference


        Property                      Description

                             OSName and OSVersion, which return the platform name and a
                                    numeric version number respectively. This property is read only.

                             Name of the operating system where the application is actually        Operating System:Name                                        running.

        Operating System:Version                                        Version number of the actual operating system.       Number

                                      Returns the names of all the items in the Controls palettes for a         Palettes:Controls Names                                       given application reference.

                                      Returns the names of all the items in the Functions palettes for a         Palettes:Functions Names                                       given application reference.

                                      Returns an alphabetized array of printer names available on the          Printing:Available Printers
                                     computer.

                                                                If TRUE, LabVIEW sends color/grayscale output to the printer. If         Printing:Color/Grayscale?
                                      FALSE, LabVIEW sends monochrome output to the printer.

                                           Specifies whether to print all controls or only the controls wired to
         Printing:Custom All Controls?   the connector pane when using the custom format with one of the
                                           print documentation VI methods.

                                           Specifies whether to print the hidden contents of iconified cluster
         Printing:Custom Cluster         constants that might be present on the block diagram when using
         Constants?                    the custom format with one of the print documentation VI
                                    methods.

                                           Specifies whether to print the connector pane and icon of VIs
         Printing:Custom Connector?   when using the custom format with one of the print
                                    documentation VI methods.

                                           Specifies whether to print descriptions of front panel controls
         Printing:Custom Control
                               when using the custom format with one of the print
         Descriptions?
                                    documentation VI methods.

                                           Specifies whether to print the label and/or caption for each
         Printing:Custom Control Label/
                                         control when using the custom format with one of the print
        Caption?
                                    documentation VI methods.

                                           Specifies whether to print data type information for front panel
         Printing:Custom Control
                                         controls when using the custom format with one of the print
        Types?
                                    documentation VI methods.

         Printing:Custom Controls?       Specifies whether to print front panel control information when


7600   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7600 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7601 ordinal=7601 -->
## Property and Method Reference

Property and Method Reference


Property                      Description

                              using the custom format with one of the print documentation VI
                            methods.

                                 Specifies whether to print VI descriptions when using the customPrinting:Custom Description?                             format with one of the print documentation VI methods.

                                 Specifies whether to print the hidden frames in Case and Stacked
Printing:Custom Diagram      Sequence structures that might be present on the block diagram
Hidden?                  when using the custom format with one of the print
                            documentation VI methods.

                                 Specifies whether to print visible subdiagrams of each Case,
                                Event, and Stacked Sequence structure in sequence with the non-Printing:Custom Diagram                                    visible subdiagrams when using the custom format with one ofRepeat?
                              the print documentation VI methods. If you print the visible
                            subdiagrams in sequence, those subdiagrams print twice.

                                 Specifies whether to print block diagrams when using the customPrinting:Custom Diagram?                             format with one of the print documentation VI methods.

                                 Specifies whether to print the configuration information for anyPrinting:Custom Express VI                              Express VIs on the block diagram when using the custom format
Configuration?                              with one of the print documentation VI methods.

                                 Specifies whether to print the hierarchy of the VI in memory when
Printing:Custom Hierarchy?     using the custom format with one of the print documentation VI
                            methods.

                                 Specifies whether to print the VI revision history information when
Printing:Custom History?       using the custom format with one of the print documentation VI
                            methods.

                                 Specifies whether to print a list of the subVIs and Express VIs
                                including the icon, name, and path when using the custom format
                              with one of the print documentation VI methods. If a polymorphic
                                   VI is a subVI, LabVIEW prints the instance used in the top-level VI
Printing:Custom List of SubVIs?
                                including the icon, name, and path. If the top-level VI is
                              polymorphic, LabVIEW prints a list of all the instances of the
                            polymorphic VI including the icon, name, and path of each
                                 instance.

                                 Specifies whether to print the front panel with a border when
Printing:Custom Panel Border?  using the custom format with one of the print documentation VI
                            methods.

Printing:Custom Panel?          Specifies whether to print the front panel when using the custom


                                                    © National Instruments 7601

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7601 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7602 ordinal=7602 -->
## Property and Method Reference

Property and Method Reference


        Property                      Description

                                     format with one of the print documentation VI methods.

         Printing:Default Printer         Gets or sets the name of the default printer in LabVIEW.

                              Maximum number of characters on a single line in a file. Affects
                                      the Print:VI To HTML, Print:VI To RTF, and Print:VI To Text          Printing:File Wrap Text Length
                                    methods. Set this property to 0 to print all the characters on one
                                              line so the text does not wrap.

                                      Percentage value from 0 to 100 specifying the level of quality you
                                  want for the JPEG graphic in VIs printed either interactively or
                                      with the Print:VI To HTML method. The scale balances image
         Printing:JPEG Quality           quality and file size. A value in the 75 to 95 range produces a
                                   compressed file with a high-quality image, and a value below 50
                                    produces a smaller file size with a low-quality image. The default
                                                     is 80.

         Printing:Method               Gets or sets how LabVIEW prints.

                               Number between 0 and 9 that specifies the level of compression
                                  you want for the PNG file for graphics in VIs printed either
                                             interactively or with the Print:VI To HTML method. The quality of
                                      the graphic is not affected by the compression, but the graphic file
         Printing:PNG Compression       size and speed of compression are affected by this value. Valid
         Level                          values range from 0 to 9 and balance file compression with speed.
                                    0 designates no compression. 1 designates less compression, but
                                             faster speed. 9 designates high compression, but slower speed. If
                                  you enter –1, LabVIEW selects the best combination of speed and
                                      compression.

                                      Returns a reference to the LabVIEW project that is active when this
                                       property executes. A project is active if the user has the associated
          Project:Active Project
                                          project window in focus or any member of the project in focus,
                                         including VIs, controls, and project libraries.

                                      Returns a reference to the project that owns the referenced
        Project:Owning Project
                                           application.

                                      Returns an array of references to each LabVIEW project in
          Project:Projects[]
                                 memory. You can use these references with the Project properties.

                                      Returns the associated target item of the application reference
         Project:Target Item
                                  you specify.

       Remote Panel:Connections To   Returns an array of clusters containing connection information
          Clients                      about the clients currently connected to the computer.


7602   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7602 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7603 ordinal=7603 -->
## Property and Method Reference

Property and Method Reference


Property                      Description

Remote Panel:Connections To   Returns an array of clusters containing connection information
Servers                     about the servers to which the computer is currently connected.

                                 Specifies whether the TCP interface to the VI Server is loggingServer:Logging Enabled                               operations to a file.

Server:Logging File Path        Path of the log file created during TCP/IP communication.

                              Gets or sets the LabVIEW VI server port. LabVIEW returns an error ifServer:Port                           you attempt to access this property on a remote application.

Server:Service Name           Gets or sets the service name for the LabVIEW VI Server.

                                 Specifies whether the TCP interface to the VI Server is currentlyServer:TCP Listener Active                               accepting connections.

                                     List that describes which TCP/IP addresses of remote clients mayServer:TCP/IP Access List
                              access the VI server.

                                     List that describes which VIs on the VI server are accessible byServer:VI Access List
                           remote clients.

Web Server:Config File Path    The path of the LabVIEW Web Server configuration file.

Web Server:Default Config File  The path of the Web Server configuration file that contains the
Path                       LabVIEW default configuration.

                          The port to which the built-in Web Server listens for HTTPWeb Server:HTTP Port                                requests.

                             Determines whether the built-in Web Server logs to a fileWeb Server:Logging Enabled                               information about HTTP requests.

Web Server:Logging File Path   Determines where the built-in Web Server places the log file.

                             Determines how long the built-in Web Server waits for read
Web Server:Read Timeout      operations to complete when the Web Server reads HTTP requests
                            from HTTP clients.

Web Server:Root Directory       Specifies the root directory from which the built-in Web Server
Path                          loads files for document requests.

                             Determines whether the built-in Web Server is enabled. This
                              property immediately changes the status of the Web Server
Web Server:Server Active       without requiring you to restart LabVIEW. Changes using this
                              property are not saved across sessions of LabVIEW and are not
                                 reflected on the Web Server page of the Options dialog box.

Web Server:TCP/IP Access List   Sets or gets the TCP/IP addresses that have access to the Web

                                                    © National Instruments 7603

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7603 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7604 ordinal=7604 -->
## Property and Method Reference

Property and Method Reference


        Property                      Description

                                           Server. This property also sets or gets whether each address has
                                       access to view a VI remotely, view and control a VI remotely, or
                                   does not have access to the Web Server.

                                        Sets or gets the VIs that are visible through the Web Server. This
      Web Server:VI Access List       property also sets or gets whether LabVIEW allows access to each
                                                    VI.

    Application:Active:ApplicationApplication:Active:Application

       Gets an application reference to the active VIs owning application.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                               Read Only

         Available in Run-Time Engine                                        Yes (Read Only)

         Available in Real-Time Operating System                             Yes

       Remote access allowed                                             Yes

    Application:Active:VIApplication:Active:VI

       Returns the name of the active VI in the application.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only


7604   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7604 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7605 ordinal=7605 -->
## Property and Method Reference

Property and Method Reference


 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

 Remote access allowed                                                   Yes

Application:AllApplication:All LibrariesLibraries inin ApplicationApplication
InstanceInstance

Lists all Libraries currently in memory in this application instance.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

 Remote access allowed                                                   Yes

Application:AllApplication:All VIsVIs InIn MemoryMemory

Returns a list of VIs in memory for the specified application instance. This property
returns an error if you wire a remote application reference to the reference input. For a
remote application, use the Exported VIs in Memory property to return a list of
exported VIs.

      Note If you have multiple application instances open simultaneously, this
       property returns only the VIs in memory in the specified application instance.
       LabVIEW creates a new application instance each time you open a LabVIEW
        project or target for a LabVIEW project.


                                                    © National Instruments 7605

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7605 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7606 ordinal=7606 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                               Read Only

         Available in Run-Time Engine                                        Yes (Read Only)

         Available in Real-Time Operating System                             Yes

       Remote access allowed                                  No

    Application:Auto-RouteApplication:Auto-Route WiresWires

       Returns whether LabVIEW automatically finds a route for a wire.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

       Remote access allowed                                                  Yes

   Application:CommandApplication:Command LineLine ArgumentsArguments

       Returns an array of user-defined command-line arguments passed when LabVIEW
       launched.

       User-defined arguments start after two hyphens (--) surrounded by spaces in the
     command line.


7606   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7606 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7607 ordinal=7607 -->
## Property and Method Reference

Property and Method Reference

The first string in the array is the name of the executable launched. This property does
not return the name of the VI launched or the LLB that contains the VI. If a user-defined
command-line argument contains double quotation marks ("), this property returns
the argument without the quotation marks.

If you use this property in a stand-alone application, you can avoid the need to enter
two hyphens before user-defined arguments by placing a checkmark in the Pass all
command line arguments to application checkbox on the Advanced page of the
Application Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                               Read Only

 Available in Run-Time Engine                                        Yes (Read Only)

 Available in Real-Time Operating System                             Yes

 Remote access allowed                                             Yes

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Application Control\VI Server\Passing
   Command Line Parameters\Passing Command Line
   Parameters.vi
Application:CompilerApplication:Compiler ThresholdThreshold

Gets or sets how complex a VI must be before the compiler limits optimizations to
improve editor responsiveness. If the complexity of a VI is lower than the threshold
indicated by this value, the compiler does not limit optimizations, thereby improving
the execution speed of the VI. If the complexity of a VI is higher than the threshold, the
compiler limits optimizations in order to improve editor responsiveness for the VI.

                                                    © National Instruments 7607

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7607 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7608 ordinal=7608 -->
## Property and Method Reference

Property and Method Reference

      To determine the complexity of a specific VI, refer to the Compiled Code Complexity
       value on the Memory Usage page of the VI Properties dialog box or use the
      Compiled:Code Complexity property.

       This property provides programmatic access to the Compiler optimizations slider on
       the Environment page of the Options dialog box.

      Possible Errors

           If you set this property to a value greater than 10, this property returns error 1.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

       Remote access allowed                                                  Yes

    Application:CurrentApplication:Current EnvironmentEnvironment ModeMode

       Returns the current environment mode of LabVIEW, such as robotics. If you call this
       property from a VI in the LabVIEW development system environment, this property
       returns an empty string.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

7608   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7608 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7609 ordinal=7609 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                                  Yes

 Remote access allowed                                                  Yes

Application:DebugApplication:Debug NameName

Returns the name used for opening a debugging connection to this application or
shared library. This method is only useful in built applications or shared libraries.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                           No

 Remote access allowed                                                   Yes

Application:Default:ApplicationApplication:Default:Application

Returns the default application reference.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

 Remote access allowed                                       No


                                                    © National Instruments 7609

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7609 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7610 ordinal=7610 -->
## Property and Method Reference

Property and Method Reference

    Application:Default:DataApplication:Default:Data DirectoryDirectory

      Path to the default data directory.

      You can use this directory to store the data files LabVIEW generates, such as .lvm or
     .txt files. When you install LabVIEW, the installer creates a LabVIEW Data
       subdirectory in the default file directory for the operating system to help you organize
      and locate the data files LabVIEW generates.

       This property is similar to the Default Data Directory option on the Paths page of the
      Options dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                               Read Only

         Available in Run-Time Engine                                        Yes (Read Only)

         Available in Real-Time Operating System                             Yes

       Remote access allowed                                             Yes

    Application:DeleteApplication:Delete FPFP TerminalTerminal fromfrom
   DiagramDiagram

       Returns whether LabVIEW deletes terminals corresponding to front panel objects from
      diagram operations.

     Remarks

      The following table lists the characteristics of this property.


7610   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7610 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7611 ordinal=7611 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Remote access allowed                                                  Yes

Application:DirectoryApplication:Directory PathPath

Absolute path to the directory where the application is located.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                               Read Only

 Available in Run-Time Engine                                        Yes (Read Only)

 Available in Real-Time Operating System                             Yes

 Remote access allowed                                             Yes

Application:ExportedApplication:Exported VIsVIs InIn MemoryMemory

Returns a list of exported VIs in memory.

This property is similar to the Exported VIs list option in the Exported VIs section on
the VI Server page of the Options dialog box.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 7611

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7611 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7612 ordinal=7612 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                               Read Only

         Available in Run-Time Engine                                        Yes (Read Only)

         Available in Real-Time Operating System                             Yes

       Remote access allowed                                             Yes

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Application Control\VI Server\Exporting
        VIs\Exporting VIs.lvproj
    Application:KindApplication:Kind

       Indicates the LabVIEW instance the VI is running in, including invalid application types.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                               Read Only

         Available in Run-Time Engine                                        Yes (Read Only)

         Available in Real-Time Operating System                             Yes

       Remote access allowed                                             Yes

    Application:LanguageApplication:Language

       Indicates the language of the LabVIEW environment or stand-alone application as a
        string according to ISO 639. Values include en, de, fr, ja, ko, and zh-cn.


7612   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7612 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7613 ordinal=7613 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                               Read Only

 Available in Run-Time Engine                                        Yes (Read Only)

 Available in Real-Time Operating System                             Yes

 Remote access allowed                                             Yes

Application:MenuApplication:Menu Launch:AppLaunch:App

Returns a reference to the application instance that launched the calling VI from a
menu selection.

If the calling VI was not launched from a menu selection, this property returns an error.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                               Read Only

 Available in Run-Time Engine                                        Yes (Read Only)

 Available in Real-Time Operating System                             Yes

 Remote access allowed                                             Yes

Application:MenuApplication:Menu Launch:VILaunch:VI

Returns the name of the VI that launched the calling VI from a menu selection.

If the calling VI was not launched from a menu selection, this property returns an error.

                                                    © National Instruments 7613

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7613 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7614 ordinal=7614 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                               Read Only

         Available in Run-Time Engine                                        Yes (Read Only)

         Available in Real-Time Operating System                             Yes

       Remote access allowed                                             Yes

   Application:NameApplication:Name

      Filename of the application.

       This property is similar to the Target filename option on the Information page of the
       Application Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                               Read Only

         Available in Run-Time Engine                                        Yes (Read Only)

         Available in Real-Time Operating System                             Yes

       Remote access allowed                                             Yes

    Application:SaveApplication:Save VersionVersion

       Returns the version number of the LabVIEW file format to which LabVIEW documents
       are saved. This version number might be different from the version number of the
       application. For example, LabVIEW with the version number 9.0.1 saves LabVIEW

7614   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7614 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7615 ordinal=7615 -->
## Property and Method Reference

Property and Method Reference

documents with a file format version number of 9.0.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                               Read Only

 Available in Run-Time Engine                                        Yes (Read Only)

 Available in Real-Time Operating System                             Yes

 Remote access allowed                                             Yes

Application:SaveableApplication:Saveable VersionsVersions

An array of the LabVIEW versions to which this version of LabVIEW can save. The array
is in reverse chronological order, with the zeroth element being the current version of
LabVIEW. Each element of the array is a valid version to pass to VI server functions
which save to previous versions.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Remote access allowed                                                   Yes

Application:ShowApplication:Show FPFP TipTip StripsStrips

Writing the property: Setting this property to TRUE enables the display of tip strips on

                                                    © National Instruments 7615

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7615 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7616 ordinal=7616 -->
## Property and Method Reference

Property and Method Reference

       front panel controls. Setting the property to FALSE prevents them from being
       displayed. Reading the property: Specifies whether tip strips display when idling over
       controls on the front panel.

       This property is similar to the Show tip strips on front panel controls option on the
       Front Panel page of the Options dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

       Remote access allowed                                                  Yes

    Application:Target:CPUApplication:Target:CPU

       Indicates the target CPU of an application.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                               Read Only

         Available in Run-Time Engine                                        Yes (Read Only)

         Available in Real-Time Operating System                             Yes

       Remote access allowed                                             Yes


7616   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7616 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7617 ordinal=7617 -->
## Property and Method Reference

Property and Method Reference

Application:Target:DataApplication:Target:Data CacheCache EntryEntry SizesSizes

Returns an array of the entry sizes, in bytes, for all cache levels the computer or target
contains.

Use this property to obtain information from a LabVIEW application running on a
remote computer or target about the system on which the application runs. LabVIEW
returns 0 if you use this property with a target for which the information is not
available.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

 Remote access allowed                                                   Yes

Application:Target:DataApplication:Target:Data CacheCache SizesSizes

Returns an array of the cache sizes, in bytes, for each cache level the computer or
target contains.

Use this property to obtain information from a LabVIEW application running on a
remote computer or target about the system on which the application runs. LabVIEW
returns 0 if you use this property with a target for which the information is not
available.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 7617

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7617 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7618 ordinal=7618 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                                   Yes

       Remote access allowed                                                   Yes

    Application:Target:NumberApplication:Target:Number ofof CoresCores perper
   PackagePackage

       Returns the number of cores per package the computer or target contains.

      Use this property to obtain information from a LabVIEW application running on a
      remote computer or target about the system on which the application runs. LabVIEW
       returns 1 if you use this property with a target for which the information is not
        available.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                                   Yes

       Remote access allowed                                                   Yes


7618   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7618 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7619 ordinal=7619 -->
## Property and Method Reference

Property and Method Reference

Application:Target:NumberApplication:Target:Number ofof LogicalLogical
ProcessorsProcessors

Returns the number of processing units the computer or target contains.

This property returns the total number of logical processors, which might be different
from the number currently available to LabVIEW. For example, the property includes
disabled processors in the number of logical processors it returns.

Use this property to obtain information from a LabVIEW application running on a
remote computer or target about the system on which the application runs. LabVIEW
returns 1 if you use this property with a target for which the information is not
available.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

 Remote access allowed                                                   Yes

Application:Target:NumberApplication:Target:Number ofof LogicalLogical
ProcessorsProcessors perper CoreCore

Returns the number of logical processors per core the computer or target contains.

Use this property to obtain information from a LabVIEW application running on a
remote computer or target about the system on which the application runs. LabVIEW
returns 1 if you use this property with a target for which the information is not

                                                    © National Instruments 7619

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7619 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7620 ordinal=7620 -->
## Property and Method Reference

Property and Method Reference

        available.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                                   Yes

       Remote access allowed                                                   Yes

    Application:Target:NumberApplication:Target:Number ofof PackagesPackages

       Returns the number of packages, or chips, the computer or target contains.

      Use this property to obtain information from a LabVIEW application running on a
      remote computer or target about the system on which the application runs. LabVIEW
       returns 1 if you use this property with a target for which the information is not
        available.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                                   Yes

       Remote access allowed                                                   Yes


7620   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7620 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7621 ordinal=7621 -->
## Property and Method Reference

Property and Method Reference

Application:Target:OperatingApplication:Target:Operating SystemSystem

Indicates the operating system for which the application was built. Mac OS refers to
Mac OS versions 9 and 8. Carbon refers to Mac OS X (32-bit).

The LabVIEW Real-Time Module always returns Phar Lap or VxWorks.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                               Read Only

 Available in Run-Time Engine                                        Yes (Read Only)

 Available in Real-Time Operating System                             Yes

 Remote access allowed                                             Yes

Application:UserApplication:User InterfaceInterface AvailableAvailable

If you are not targeted to a real-time (RT) platform, this property is always TRUE. If you
are targeted to an RT-platform and the host is connected, this property is TRUE. When
this property is FALSE, the host is not connected, requiring that the Real-Time Module
application must be able to handle all operations independent of the host. Use this
property to determine when it is safe to display a dialog box that requires user
interaction.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

                                                    © National Instruments 7621

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7621 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7622 ordinal=7622 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                                   Yes

       Remote access allowed                                                   Yes

    Application:UserApplication:User NameName

      User name used to open the application.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read/Write

         Available in Run-Time Engine                                        Yes (Read Only)

         Available in Real-Time Operating System                             Yes

       Remote access allowed                                             Yes

    Application:VIApplication:VI OfOf TopTop MostMost BlockBlock DiagramDiagram

       Returns a reference to the block diagram highest in the Z order, which is most likely the
        last block diagram accessed.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                           No

       Remote access allowed                                                   Yes


7622   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7622 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7623 ordinal=7623 -->
## Property and Method Reference

Property and Method Reference

Application:VersionApplication:Version NumberNumber

Version number of the application. In a stand-alone application or shared library, this
property returns the version of the LabVIEW Run-Time Engine.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                               Read Only

 Available in Run-Time Engine                                        Yes (Read Only)

 Available in Real-Time Operating System                             Yes

 Remote access allowed                                             Yes

Application:VersionApplication:Version YearYear

Version year of the application. In a stand-alone application or shared library, this
property returns the version year of the LabVIEW Run-Time Engine.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                               Read Only

 Available in Run-Time Engine                                        Yes (Read Only)

 Available in Real-Time Operating System                             Yes

 Remote access allowed                                             Yes


                                                    © National Instruments 7623

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7623 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7624 ordinal=7624 -->
## Property and Method Reference

Property and Method Reference

   DebugDebug Server:ServerServer:Server ActiveActive

      Determines whether the Debug Server is enabled. You can use this property only in
       LabVIEW-built applications or shared libraries.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

       Remote access allowed                                      No

   DebugDebug Server:TCP/IPServer:TCP/IP AccessAccess ListList

        List that describes which TCP/IP addresses of remote clients can access the Debug
       Server. You can use this property only in LabVIEW-built applications or shared libraries.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

       Remote access allowed                                      No


7624   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7624 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7625 ordinal=7625 -->
## Property and Method Reference

Property and Method Reference

Display:AllDisplay:All MonitorsMonitors

Returns information about all the monitors on the computer, including their bit depths
and bounding rectangles.

Elements

 Name   Description

          Cluster that defines the bounding rectangle of the content area of all the monitors on the
         computer.

                 • Left—The horizontal coordinate of the left edge of the bounding rectangle.
 Bounds                 • Top—The vertical coordinate of the top edge of the bounding rectangle.
                 • Right—The horizontal coordinate of the right edge of the bounding rectangle.
                 • Bottom—The vertical coordinate of the bottom edge of the bounding rectangle.

 Depth   The bit depth of all the monitors on the computer.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                               Read Only

 Available in Run-Time Engine                                        Yes (Read Only)

 Available in Real-Time Operating System                             Yes

 Remote access allowed                                             Yes

Display:PrimaryDisplay:Primary WorkspaceWorkspace

Gives the bounding rectangle of the computer's primary monitor.


                                                    © National Instruments 7625

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7625 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7626 ordinal=7626 -->
## Property and Method Reference

Property and Method Reference

     Elements

      Name   Description

               The horizontal coordinate of the left edge of the bounding rectangle of the computer's          Left                primary monitor.

               The vertical coordinate of the top edge of the bounding rectangle of the computer's        Top                primary monitor.

               The horizontal coordinate of the right edge of the bounding rectangle of the computer's         Right                primary monitor.

               The vertical coordinate of the bottom edge of the bounding rectangle of the computer's        Bottom                primary monitor.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                               Read Only

         Available in Run-Time Engine                                        Yes (Read Only)

         Available in Real-Time Operating System                             Yes

       Remote access allowed                                             Yes

    NINI Security:NobodySecurity:Nobody LoggedLogged In?In?

      Determines if anyone is logged in.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only


7626   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7626 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7627 ordinal=7627 -->
## Property and Method Reference

Property and Method Reference


 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

 Remote access allowed                                       No

NINI Security:UserSecurity:User

Indicates the name of the user who is currently logged in, using the format of
<Domain Name>\<User Name>.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

 Remote access allowed                                       No

OperatingOperating System:BuildSystem:Build NumberNumber

Build number of the actual operating system. This string returns an alphanumeric
value of the build number that you can use to compare the build version of operating
systems. This property is read only.

      Note A newer version of an operating system often returns a larger
       alphanumeric value.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 7627

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7627 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7628 ordinal=7628 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                           No

       Remote access allowed                                                   Yes

   OperatingOperating System:DetailedSystem:Detailed NameName

       Detailed name of the operating system where the application is actually running. This
        string value returns the operating system and its version. This property is similar to a
      combination of OSName and OSVersion, which return the platform name and a
      numeric version number respectively. This property is read only.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                           No

       Remote access allowed                                                   Yes

   OperatingOperating System:NameSystem:Name

     Name of the operating system where the application is actually running.

       Refer to the following for a partial list of operating systems this property might return:

            • Linux
            • Mac OS
            • Mac OS X x64

7628   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7628 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7629 ordinal=7629 -->
## Property and Method Reference

Property and Method Reference

  • PharLap
  • RTX
  • Solaris
  • VxWorks
  • Windows NT

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                               Read Only

 Available in Run-Time Engine                                        Yes (Read Only)

 Available in Real-Time Operating System                             Yes

 Remote access allowed                                             Yes

OperatingOperating System:VersionSystem:Version NumberNumber

Version number of the actual operating system.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                               Read Only

 Available in Run-Time Engine                                        Yes (Read Only)

 Available in Real-Time Operating System                             Yes

 Remote access allowed                                             Yes


                                                    © National Instruments 7629

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7629 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7630 ordinal=7630 -->
## Property and Method Reference

Property and Method Reference

    Palettes:ControlsPalettes:Controls NamesNames

       Returns the names of all the items in the Controls palettes for a given application
       reference.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No

       Remote access allowed                                       No

    Palettes:FunctionsPalettes:Functions NamesNames

       Returns the names of all the items in the Functions palettes for a given application
       reference.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No

       Remote access allowed                                       No


7630   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7630 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7631 ordinal=7631 -->
## Property and Method Reference

Property and Method Reference

Printing:AvailablePrinting:Available PrintersPrinters

Returns an alphabetized array of printer names available on the computer.

      Note This property is available only on Windows.

This property is similar to the System Configured Printers output of the Query
Available Printers VI.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

 Remote access allowed                                                   Yes

Printing:Color/Grayscale?Printing:Color/Grayscale?

If TRUE, LabVIEW sends color/grayscale output to the printer. If FALSE, LabVIEW sends
monochrome output to the printer.

      Note (macOS) LabVIEW supports only grayscale printing. You cannot use
         this property to change printing settings on macOS.

This property is similar to the Color/Grayscale printing checkbox on the Printing page
of the Options dialog box.


                                                    © National Instruments 7631

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7631 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7632 ordinal=7632 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

       Remote access allowed                                                  Yes

    Printing:CustomPrinting:Custom AllAll Controls?Controls?

       Specifies whether to print all controls or only the controls wired to the connector pane
     when using the custom format with one of the print documentation VI methods.

       This property does not affect the image of the front panel, just the list of controls and
       indicators in the generated documentation.

       This property is similar to the All controls and Connected controls options on the VI
      Documentation page of the Print dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

       Remote access allowed                                                  Yes


7632   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7632 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7633 ordinal=7633 -->
## Property and Method Reference

Property and Method Reference

Printing:CustomPrinting:Custom ClusterCluster Constants?Constants?

Specifies whether to print the hidden contents of iconified cluster constants that might
be present on the block diagram when using the custom format with one of the print
documentation VI methods.

This property is similar to the Iconified Cluster Constants option on the VI
Documentation page of the Print dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Remote access allowed                                                  Yes

Printing:CustomPrinting:Custom Connector?Connector?

Specifies whether to print the connector pane and icon of VIs when using the custom
format with one of the print documentation VI methods.

This property is similar to the Icon and connector pane option on the VI
Documentation page of the Print dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write


                                                    © National Instruments 7633

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7633 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7634 ordinal=7634 -->
## Property and Method Reference

Property and Method Reference


         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

       Remote access allowed                                                  Yes

    Printing:CustomPrinting:Custom ControlControl Descriptions?Descriptions?

       Specifies whether to print descriptions of front panel controls when using the custom
       format with one of the print documentation VI methods.

       This property is similar to the Descriptions option on the VI Documentation page of
       the Print dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

       Remote access allowed                                                  Yes

    Printing:CustomPrinting:Custom ControlControl Label/Caption?Label/Caption?

       Specifies whether to print the label and/or caption for each control when using the
      custom format with one of the print documentation VI methods.

     Remarks

      The following table lists the characteristics of this property.


        Data type


7634   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7634 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7635 ordinal=7635 -->
## Property and Method Reference

Property and Method Reference


 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Remote access allowed                                                  Yes

Printing:CustomPrinting:Custom ControlControl Types?Types?

Specifies whether to print data type information for front panel controls when using
the custom format with one of the print documentation VI methods.

This property is similar to the Data type information option on the VI Documentation
page of the Print dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Remote access allowed                                                  Yes

Printing:CustomPrinting:Custom Controls?Controls?

Specifies whether to print front panel control information when using the custom
format with one of the print documentation VI methods.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 7635

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7635 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7636 ordinal=7636 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

       Remote access allowed                                                  Yes

    Printing:CustomPrinting:Custom Description?Description?

       Specifies whether to print VI descriptions when using the custom format with one of
       the print documentation VI methods.

       This property is similar to the Description option on the VI Documentation page of the
       Print dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

       Remote access allowed                                                  Yes

    Printing:CustomPrinting:Custom DiagramDiagram Hidden?Hidden?

       Specifies whether to print the hidden frames in Case and Stacked Sequence structures
       that might be present on the block diagram when using the custom format with one of
       the print documentation VI methods.

       This property is similar to the Hidden frames option on the VI Documentation page of
       the Print dialog box.

7636   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7636 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7637 ordinal=7637 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Remote access allowed                                                  Yes

Printing:CustomPrinting:Custom DiagramDiagram Repeat?Repeat?

Specifies whether to print visible subdiagrams of each Case, Event, and Stacked
Sequence structure in sequence with the non-visible subdiagrams when using the
custom format with one of the print documentation VI methods. If you print the visible
subdiagrams in sequence, those subdiagrams print twice.

This property is similar to the Ordered (Repeat from higher level if nested) option on
the VI Documentation page of the Print dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Remote access allowed                                                  Yes


                                                    © National Instruments 7637

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7637 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7638 ordinal=7638 -->
## Property and Method Reference

Property and Method Reference

    Printing:CustomPrinting:Custom Diagram?Diagram?

       Specifies whether to print block diagrams when using the custom format with one of
       the print documentation VI methods.

       This property is similar to the Block diagram option on the VI Documentation page of
       the Print dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

       Remote access allowed                                                  Yes

    Printing:CustomPrinting:Custom ExpressExpress VIVI Configuration?Configuration?

       Specifies whether to print the configuration information for any Express VIs on the
       block diagram when using the custom format with one of the print documentation VI
      methods.

       This property is similar to the Express VI configuration information checkbox on the VI
      Documentation page of the Print dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write


7638   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7638 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7639 ordinal=7639 -->
## Property and Method Reference

Property and Method Reference


 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Remote access allowed                                                  Yes

Printing:CustomPrinting:Custom Hierarchy?Hierarchy?

Specifies whether to print the hierarchy of the VI in memory when using the custom
format with one of the print documentation VI methods.

This property is similar to the VI hierarchy option on the VI Documentation page of the
Print dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Remote access allowed                                                  Yes

Printing:CustomPrinting:Custom History?History?

Specifies whether to print the VI revision history information when using the custom
format with one of the print documentation VI methods.

This property is similar to the VI revision history option on the VI Documentation page
of the Print dialog box.

Remarks

The following table lists the characteristics of this property.

                                                    © National Instruments 7639

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7639 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7640 ordinal=7640 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

       Remote access allowed                                                  Yes

    Printing:CustomPrinting:Custom ListList ofof SubVIs?SubVIs?

       Specifies whether to print a list of the subVIs and Express VIs including the icon, name,
      and path when using the custom format with one of the print documentation VI
      methods. If a polymorphic VI is a subVI, LabVIEW prints the instance used in the top-
        level VI including the icon, name, and path. If the top-level VI is polymorphic, LabVIEW
        prints a list of all the instances of the polymorphic VI including the icon, name, and
      path of each instance.

       This property is similar to the List of subVIs and Express VIs option on the VI
      Documentation page of the Print dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

       Remote access allowed                                                  Yes

    Printing:CustomPrinting:Custom PanelPanel Border?Border?

       Specifies whether to print the front panel with a border when using the custom format
       with one of the print documentation VI methods.

7640   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7640 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7641 ordinal=7641 -->
## Property and Method Reference

Property and Method Reference

This property is similar to the Surround front panel with border option on the Print
Options page of the VI Properties dialog box and the Surround panel with border
option on the Printer page of the Print dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Remote access allowed                                                  Yes

Printing:CustomPrinting:Custom Panel?Panel?

Specifies whether to print the front panel when using the custom format with one of
the print documentation VI methods.

This property is similar to the Front panel option on the VI Documentation page of the
Print dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Remote access allowed                                                  Yes


                                                    © National Instruments 7641

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7641 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7642 ordinal=7642 -->
## Property and Method Reference

Property and Method Reference

    Printing:DefaultPrinting:Default PrinterPrinter

       Gets or sets the name of the default printer in LabVIEW.

      To set the default printer, enter the full path to the printer, such as \\myprinter\
      ab01.

           Note This property is available only on Windows.

       This property is similar to the Default Printer output of the Query Available Printers VI.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

       Remote access allowed                                                  Yes

    Printing:FilePrinting:File WrapWrap TextText LengthLength

     Maximum number of characters on a single line in a file. Affects the Print:VI To HTML,
        Print:VI To RTF, and Print:VI To Text methods. Set this property to 0 to print all the
       characters on one line so the text does not wrap.

     Remarks

      The following table lists the characteristics of this property.


        Data type


7642   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7642 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7643 ordinal=7643 -->
## Property and Method Reference

Property and Method Reference


 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Remote access allowed                                                  Yes

Printing:JPEGPrinting:JPEG QualityQuality

Percentage value from 0 to 100 specifying the level of quality you want for the JPEG
graphic in VIs printed either interactively or with the Print:VI To HTML method. The
scale balances image quality and file size. A value in the 75 to 95 range produces a
compressed file with a high-quality image, and a value below 50 produces a smaller
file size with a low-quality image. The default is 80.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                  No

 Available in Real-Time Operating System                          No

 Remote access allowed                                                  Yes

Printing:MethodPrinting:Method

Gets or sets how LabVIEW prints.

This property is similar to the Standard printing, PostScript printing, and Bitmap
printing options on the Printing page of the Options dialog box.


                                                    © National Instruments 7643

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7643 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7644 ordinal=7644 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

       Remote access allowed                                                  Yes

    Printing:PNGPrinting:PNG CompressionCompression LevelLevel

     Number between 0 and 9 that specifies the level of compression you want for the PNG
          file for graphics in VIs printed either interactively or with the Print:VI To HTML method.
      The quality of the graphic is not affected by the compression, but the graphic file size
      and speed of compression are affected by this value. Valid values range from 0 to 9 and
       balance file compression with speed. 0 designates no compression. 1 designates less
       compression, but faster speed. 9 designates high compression, but slower speed. If
      you enter –1, LabVIEW selects the best combination of speed and compression.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                  No

         Available in Real-Time Operating System                          No

       Remote access allowed                                                  Yes


7644   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7644 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7645 ordinal=7645 -->
## Property and Method Reference

Property and Method Reference

Project:ActiveProject:Active ProjectProject

Returns a reference to the LabVIEW project that is active when this property executes.
A project is active if the user has the associated project window in focus or any
member of the project in focus, including VIs, controls, and project libraries.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Remote access allowed                                                   Yes

Project:OwningProject:Owning ProjectProject

Returns a reference to the project that owns the referenced application.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Remote access allowed                                                   Yes


                                                    © National Instruments 7645

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7645 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7646 ordinal=7646 -->
## Property and Method Reference

Property and Method Reference

    Project:Projects[]Project:Projects[]

       Returns an array of references to each LabVIEW project in memory. You can use these
       references with the Project properties.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                                   Yes

       Remote access allowed                                                   Yes

    Project:TargetProject:Target ItemItem

       Returns the associated target item of the application reference you specify.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                           No

       Remote access allowed                                                   Yes


7646   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7646 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7647 ordinal=7647 -->
## Property and Method Reference

Property and Method Reference

RemoteRemote Panel:ConnectionsPanel:Connections ToTo ClientsClients

Returns an array of clusters containing connection information about the clients
currently connected to the computer.

LabVIEW opens a connection on the server computer when another application
instance or a related application, such as a Web browser, requests to view the front
panel of a VI in memory on the server computer.

This property is similar to the Total Network Traffic option on the Remote Panel
Connection Manager dialog box.

Elements

 Name      Description

         Name of the VI on the server to which you want to connect. To specify a VI that is part of
           a LabVIEW project, you must include the project name, the project library, and the
             target in the path of the VI, when applicable. For example, if MyVI.vi resides in a
             project called MyProject.lvproj under target My Computer, enter the VI name
 VI Name   as MyProject.lvproj/My Computer/MyVI.vi. If the VI resides in a project
              library called MyLibrary, also include the project library in the path, as in
         MyProject.lvproj/My Computer/MyLibrary.lvlib:MyVI.vi. If the VI is
            not in a project or project library, you can enter the VI name without any additional
            information.

 Remote    IP address of the client.

 UserName LabVIEW user name of the client connected to the server computer.

 Port       Port number currently being used by the client computer.

 Status    An enumeration type that specifies the controlling status of the connection.

 Create
          A time stamp that specifies in seconds when the connection was created.
 Time

 Status     A time stamp that specifies in seconds when the client changed to its current
 Time      connection status.

          A time stamp that indicates when the server will regain control of the VI or transfer
 Control             control to another client. A value of MM/DD/YY indicates that you did not set a time End Time
              limit for the VI in the Web Server page of the Options dialog box.


                                                    © National Instruments 7647

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7647 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7648 ordinal=7648 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                               Read Only

         Available in Run-Time Engine                                        Yes (Read Only)

         Available in Real-Time Operating System                             Yes

       Remote access allowed                                  No

   RemoteRemote Panel:ConnectionsPanel:Connections ToTo ServersServers

       Returns an array of clusters containing connection information about the servers to
      which the computer is currently connected.

     Elements

      Name      Description

               Name of the VI on the server to which you want to connect. To specify a VI that is part of
                  a LabVIEW project, you must include the project name, the project library, and the
                      target in the path of the VI, when applicable. For example, if MyVI.vi resides in a
                     project called MyProject.lvproj under target My Computer, enter the VI name
          VI Name   as MyProject.lvproj/My Computer/MyVI.vi. If the VI resides in a project
                       library called MyLibrary, also include the project library in the path, as in
               MyProject.lvproj/My Computer/MyLibrary.lvlib:MyVI.vi. If the VI is
                   not in a project or project library, you can enter the VI name without any additional
                     information.

       Remote    IP address of the server to which you are connected.

       UserName Your current LabVIEW user name.

         Port       Port number currently being used by the server computer.

         Status    An enumeration type that specifies the controlling status of the connection.

         Create
                 A time stamp that specifies in seconds when the connection was created.
       Time


7648   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7648 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7649 ordinal=7649 -->
## Property and Method Reference

Property and Method Reference


 Name      Description

 Status     A time stamp that specifies in seconds when the server changed to its current
 Time      connection status.

          A time stamp that indicates when the server will regain control of the VI or transfer
 Control             control to another client. A value of MM/DD/YY indicates that the server administrator End Time
            did not set a time limit for the VI in the Web Server page of the Options dialog box.

Use the Remote Panel:Open Connection To Server method to open a connection to a
server.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                               Read Only

 Available in Run-Time Engine                                        Yes (Read Only)

 Available in Real-Time Operating System                             Yes

 Remote access allowed                                  No

Server:LoggingServer:Logging EnabledEnabled

Specifies whether the TCP interface to the VI Server is logging operations to a file.

If you do not wire the Property Node reference input, LabVIEW uses the application
instance for the calling VI.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write


                                                    © National Instruments 7649

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7649 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7650 ordinal=7650 -->
## Property and Method Reference

Property and Method Reference


         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

       Remote access allowed                                      No

    Server:LoggingServer:Logging FileFile PathPath

      Path of the log file created during TCP/IP communication.

           If you do not wire the Property Node reference input, LabVIEW uses the application
       instance for the calling VI.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

       Remote access allowed                                      No

    Server:PortServer:Port

       Gets or sets the LabVIEW VI server port. LabVIEW returns an error if you attempt to
       access this property on a remote application.

           If you do not wire the Property Node reference input, LabVIEW uses the application
       instance for the calling VI.

       This property is similar to the Port option in the Protocols section on the VI Server
      page on the Options dialog box.


7650   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7650 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7651 ordinal=7651 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Remote access allowed                                      No

Server:ServiceServer:Service NameName

Gets or sets the service name for the LabVIEW VI Server.

This property is similar to the Service name option on the VI Server page of the
Options dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Remote access allowed                                      No

Server:TCPServer:TCP ListenerListener ActiveActive

Specifies whether the TCP interface to the VI Server is currently accepting connections.

If the Property Node reference input is unwired, LabVIEW gets or sets the VI server port

                                                    © National Instruments 7651

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7651 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7652 ordinal=7652 -->
## Property and Method Reference

Property and Method Reference

        for the calling VI application instance.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

       Remote access allowed                                      No

    Server:TCP/IPServer:TCP/IP AccessAccess ListList

        List that describes which TCP/IP addresses of remote clients may access the VI server.

      Each element in the array should start with '+' to allow access, or with '-' to deny
       access. For example, the array with the elements ['+*.site.com', '-private.site.com']
       allows access for all hosts in the site.com domain, with the exception of
        private.site.com. This property is available only on local versions of LabVIEW. If the
       Property Node reference input is unwired, LabVIEW gets or sets the VI server port for
       the calling VI application instance.

       This property is similar to the Machine access list option in the Machine access section
      on the VI Server page of the Options dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes


7652   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7652 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7653 ordinal=7653 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                                  Yes

 Remote access allowed                                      No

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Application Control\VI Server\Exporting
   VIs\Exporting VIs.lvproj
Server:VIServer:VI AccessAccess ListList

List that describes which VIs on the VI server are accessible by remote clients.

Each element in the array should start with '+' to allow access, or with '-' to deny
access. For example, the array with the element ['+Server*'] allows access to all VIs
whose name starts with 'Server'. This property is available only on local versions of
LabVIEW. If the Property Node reference input is unwired, LabVIEW gets or sets the VI
server port for the calling VI application instance.

This property is similar to the Exported VIs list option in the Exported VIs section on
the VI Server page of the Options dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Remote access allowed                                      No


                                                    © National Instruments 7653

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7653 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7654 ordinal=7654 -->
## Property and Method Reference

Property and Method Reference

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Application Control\VI Server\Exporting
        VIs\Exporting VIs.lvproj
   WebWeb Server:ConfigServer:Config FileFile PathPath

      The path of the LabVIEW Web Server configuration file.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                                   Yes

       Remote access allowed                                                   Yes

   WebWeb Server:DefaultServer:Default ConfigConfig FileFile PathPath

      The path of the Web Server configuration file that contains the LabVIEW default
       configuration.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

7654   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7654 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7655 ordinal=7655 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                                   Yes

 Remote access allowed                                                   Yes

WebWeb Server:HTTPServer:HTTP PortPort

The port to which the built-in Web Server listens for HTTP requests.

This property is similar to the HTTP Port option on the Web Server page of the Options
dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Remote access allowed                                      No

WebWeb Server:LoggingServer:Logging EnabledEnabled

Determines whether the built-in Web Server logs to a file information about HTTP
requests.

This property is similar to the Use Log File option on the Web Server page of the
Options dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

                                                    © National Instruments 7655

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7655 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7656 ordinal=7656 -->
## Property and Method Reference

Property and Method Reference


         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

       Remote access allowed                                      No

   WebWeb Server:LoggingServer:Logging FileFile PathPath

      Determines where the built-in Web Server places the log file.

       This property is similar to the Log File Path option on the Web Server page of the
       Options dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

       Remote access allowed                                      No

   WebWeb Server:ReadServer:Read TimeoutTimeout

      Determines how long the built-in Web Server waits for read operations to complete
     when the Web Server reads HTTP requests from HTTP clients.

       This property is similar to the Timeout option on the Web Server page of the Options
       dialog box.


7656   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7656 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7657 ordinal=7657 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Remote access allowed                                      No

WebWeb Server:RootServer:Root DirectoryDirectory PathPath

Specifies the root directory from which the built-in Web Server loads files for
document requests.

This property is similar to the Root Directory option on the Web Server page of the
Options dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Remote access allowed                                      No

WebWeb Server:ServerServer:Server ActiveActive

Determines whether the built-in Web Server is enabled. This property immediately
changes the status of the Web Server without requiring you to restart LabVIEW.

                                                    © National Instruments 7657

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7657 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7658 ordinal=7658 -->
## Property and Method Reference

Property and Method Reference

      Changes using this property are not saved across sessions of LabVIEW and are not
       reflected on the Web Server page of the Options dialog box.

       This property is similar to the Enable Remote Panel Server option on the Web Server
      page of the Options dialog box. However, you must restart LabVIEW to apply changes
       to this option. Unlike the Web Server:Server Active property, changes to this option are
      saved and appear the next time you open LabVIEW.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

       Remote access allowed                                      No

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Data Communication\Remote Panels\Remote
        Panel Methods.lvproj
   WebWeb Server:TCP/IPServer:TCP/IP AccessAccess ListList

       Sets or gets the TCP/IP addresses that have access to the Web Server. This property
       also sets or gets whether each address has access to view a VI remotely, view and
       control a VI remotely, or does not have access to the Web Server.

      You can use wildcards in the address you enter. This property is an array of strings,
      where each string is an address that begins with c+, +, or -.

            • c+ specifies that the address has access to view and control a VI remotely.

7658   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7658 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7659 ordinal=7659 -->
## Property and Method Reference

Property and Method Reference

  • + specifies that the address has access to view a VI remotely.
  • - specifies that the address does not have access to the Web Server.

This property is similar to the Web Server page of the Options dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Remote access allowed                                      No

WebWeb Server:VIServer:VI AccessAccess ListList

Sets or gets the VIs that are visible through the Web Server. This property also sets or
gets whether LabVIEW allows access to each VI.

This property is an array of strings, where each string is a VI name that begins with + or
-. If you specify a non-default control time limit for a VI, the value appears before +.

  • + specifies that LabVIEW allows access to the VI.
  • - specifies that LabVIEW does not allow access to the VI.

      Note You can use this property to limit access to clones already in memory
         for remote front panel connections. Limiting access to clones is useful when
       you have a limited number of resources. To limit the number of clones
        created for remote front panel connections, use the Open VI Reference
        function to create the required number of clones. Use the VI Clone Name
       property to get the name of each clone. Limit the access to only those clones
       you created by adding each clone name beginning with + to the array and by
       adding the name of the original reentrant VI beginning with - to the array.

                                                    © National Instruments 7659

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7659 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7660 ordinal=7660 -->
## Property and Method Reference

Property and Method Reference

       This property is similar to the Web Server page of the Options dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

       Remote access allowed                                      No

       ApplicationApplication EventsEvents


        Event        Description

         Application                     Occurs when the user activates LabVIEW.
         Activation

                 When registered for in a VI running inside a LabVIEW project, generated when the
                       application instance of the project is closed for any reason, such as when you close         Application                     the Project Explorer window, when you select File»Close All or File»Quit, or when         Instance
                   you run a VI that executes the Quit LabVIEW function. When registered for in a VI         Close                     running outside a project, generated when you exit LabVIEW through the user
                        interface or with the Quit LabVIEW function.

                 When registered for in a VI running inside a LabVIEW project, this event is generated
         Application  when the application instance of the project is closed interactively, such as when you
         Instance      close the Project Explorer window or when you select File»Close All or File»Quit.
         Close?     When registered for in a VI running outside a project, this event is generated only
                 when you exit LabVIEW through the user interface.

       Bookmark
                    Generated when the user changes a bookmark.
          Info Change

        Context
        Help
                     Occurs when the Context Help window is updated.
       Window
        Updated

         NI Security   Generated when the user logs into the application.

7660   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7660 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7661 ordinal=7661 -->
## Property and Method Reference

Property and Method Reference


 Event        Description

 User
 Change

             Occurs when the Event structure times out. Wire a value to the Timeout terminal at
 Timeout     the top left of the Event structure to specify the number of milliseconds the Event
               structure should wait for an event to occur before generating a Timeout event.

 VI Activation  Generated when you activate a VI window.

 VI           Generated when you deactivate a VI window. This event fires when you remove focus
 Deactivation from a VI.

             Generated when the scroll position of the active VI window changes or when you VI Scroll                resize the window.

ApplicationApplication ActivationActivation

Occurs when the user activates LabVIEW.

Event Data Fields

 Name   Description

         Source of the event. LabVIEW UI refers to any built-in user interface event.

 Source
         0            LabVIEW UI


 Type    Type of event that occurred, such as Mouse Down, Value Change, Timeout, and so on.


 Time    Value of the millisecond timer when the event occurred.


 AppRef  Reference to the application on which this event occurred.


                                                    © National Instruments 7661

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7661 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7662 ordinal=7662 -->
## Property and Method Reference

Property and Method Reference

    ApplicationApplication InstanceInstance CloseClose

     When registered for in a VI running inside a LabVIEW project, generated when the
       application instance of the project is closed for any reason, such as when you close the
       Project Explorer window, when you select File»Close All or File»Quit, or when you run
      a VI that executes the Quit LabVIEW function. When registered for in a VI running
       outside a project, generated when you exit LabVIEW through the user interface or with
       the Quit LabVIEW function.

     Event Data Fields

      Name   Description

                Source of the event. LabVIEW UI refers to any built-in user interface event.

        Source
                0            LabVIEW UI


        Type    Type of event that occurred, such as Mouse Down, Value Change, Timeout, and so on.


       Time    Value of the millisecond timer when the event occurred.


        AppRef  Reference to the application on which this event occurred.

    ApplicationApplication InstanceInstance Close?Close?

     When registered for in a VI running inside a LabVIEW project, this event is generated
     when the application instance of the project is closed interactively, such as when you
       close the Project Explorer window or when you select File»Close All or File»Quit. When
       registered for in a VI running outside a project, this event is generated only when you
        exit LabVIEW through the user interface.


7662   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7662 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7663 ordinal=7663 -->
## Property and Method Reference

Property and Method Reference

Event Data Fields

 Name           Description

                Source of the event. LabVIEW UI refers to any built-in user interface event.

 Source
                0           LabVIEW UI


               Type of event that occurred, such as Mouse Down, Value Change, Timeout, and so Type                 on.


 Time            Value of the millisecond timer when the event occurred.


 AppRef          Reference to the application on which this event occurred.


                 Allows you to prompt users with a Quitting will abort all running
             VIs. dialog box. Users then can save any modified VIs before exiting LabVIEW. If
 SilentShutdown you do not need a silent shutdown, leave SilentShutdown unwired because
                  wiring a FALSE value overrides other VIs that have previously handled this event
              and sets this value to TRUE.

                 Allows you to prevent LabVIEW from processing the event, bypassing the Discard?
                 behavior normally triggered by that event. The default is FALSE.

BookmarkBookmark InfoInfo ChangeChange

Generated when the user changes a bookmark.

Use this event if you are creating a new bookmark manager.


                                                    © National Instruments 7663

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7663 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7664 ordinal=7664 -->
## Property and Method Reference

Property and Method Reference

     Event Data Fields

      Name   Description

                 Source of the event. LabVIEW UI refers to any built-in user interface event.

        Source
                 0            LabVIEW UI


        Type    Type of event that occurred, such as Mouse Down, Value Change, Timeout, and so on.


       Time    Value of the millisecond timer when the event occurred.


       App Ref  Reference to the application on which this event occurred.

        Paths

       Names

   ContextContext HelpHelp WindowWindow UpdatedUpdated

      Occurs when the Context Help window is updated.

     Event Data Fields

      Name     Description

                  Source of the event. LabVIEW UI refers to any built-in user interface event.

        Source
                  0            LabVIEW UI


7664   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7664 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7665 ordinal=7665 -->
## Property and Method Reference

Property and Method Reference


 Name     Description

 Type     Type of event that occurred, such as Mouse Down, Value Change, Timeout, and so on.


 Time     Value of the millisecond timer when the event occurred.


 AppRef   Reference to the application on which this event occurred.


          Path or symbolic path to the HTML file or to the compiled help file linked to from the
 HelpPath Context Help window. If this field is empty, the blue Detailed help link does not appear
            in the Context Help window, and the Detailed help button is dimmed.


        HTML filename or index keyword of the topic that is launched from the Context Help
 HelpTag          window.


 Label     Text contained in the label for the object.


 Caption   Text contained in the caption for the object.


           Description of the object entered by right-clicking the object and selecting Description Desc
         and Tip from the shortcut menu to display the Description and Tip dialog box.

NINI SecuritySecurity UserUser ChangeChange

Generated when the user logs into the application.


                                                    © National Instruments 7665

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7665 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7666 ordinal=7666 -->
## Property and Method Reference

Property and Method Reference

     Event Data Fields

      Name   Description

                Source of the event. LabVIEW UI refers to any built-in user interface event.

        Source
                0            LabVIEW UI


        Type    Type of event that occurred, such as Mouse Down, Value Change, Timeout, and so on.


       Time    Value of the millisecond timer when the event occurred.


        AppRef  Reference to the application on which this event occurred.

   TimeoutTimeout

      Occurs when the Event structure times out. Wire a value to the Timeout terminal at the
      top left of the Event structure to specify the number of milliseconds the Event
       structure should wait for an event to occur before generating a Timeout event.

      The time stamp is a millisecond counter you can use to compute the time elapsed
      between two events or to determine the order of occurrence.

     Event Data Fields

      Name   Description

                Source of the event. LabVIEW UI refers to any built-in user interface event.

        Source
                0            LabVIEW UI


7666   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7666 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7667 ordinal=7667 -->
## Property and Method Reference

Property and Method Reference


 Name   Description

 Type    Type of event that occurred, such as Mouse Down, Value Change, Timeout, and so on.


 Time    Value of the millisecond timer when the event occurred.

VIVI ActivationActivation

Generated when you activate a VI window.

Event Data Fields

 Name     Description

           Source of the event. LabVIEW UI refers to any built-in user interface event.

 Source
           0            LabVIEW UI


 Type      Type of event that occurred, such as Mouse Down, Value Change, Timeout, and so on.


 Time      Value of the millisecond timer when the event occurred.


 AppRef    Reference to the application on which this event occurred.


 VIName   Name of the VI in which this event occurred.


 VIWindow Number that corresponds to the VI window you activated.


                                                    © National Instruments 7667

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7667 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7668 ordinal=7668 -->
## Property and Method Reference

Property and Method Reference


      Name     Description

        VIAppRef   Reference to the VI in which this event occurred.

    VIVI DeactivationDeactivation

      Generated when you deactivate a VI window. This event fires when you remove focus
      from a VI.

     Event Data Fields

      Name     Description

                   Source of the event. LabVIEW UI refers to any built-in user interface event.

        Source
                   0            LabVIEW UI


        Type      Type of event that occurred, such as Mouse Down, Value Change, Timeout, and so on.


       Time      Value of the millisecond timer when the event occurred.


        AppRef    Reference to the application on which this event occurred.


       VIName   Name of the VI in which this event occurred.


        VIWindow Number that corresponds to the VI window you activated.


        VIAppRef   Reference to the VI in which this event occurred.


7668   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7668 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7669 ordinal=7669 -->
## Property and Method Reference

Property and Method Reference

VIVI ScrollScroll

Generated when the scroll position of the active VI window changes or when you resize
the window.

Event Data Fields

 Name         Description

              Source of the event. LabVIEW UI refers to any built-in user interface event.

 Source
               0           LabVIEW UI


              Type of event that occurred, such as Mouse Down, Value Change, Timeout, and so
 Type                on.


 Time          Value of the millisecond timer when the event occurred.


 AppRef        Reference to the application on which this event occurred.

 VisibleBounds

GenericGeneric

Generic Methods

Generic Properties

GenericGeneric MethodsMethods


 Method           Description

 Class               Calls the VI associated with the Operator Name, on the object. Returns FALSE if

                                                    © National Instruments 7669

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7669 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7670 ordinal=7670 -->
## Property and Method Reference

Property and Method Reference


       Method           Description

         Operator:Call     no operator VI is associated with the class of the object.

         Class              Traverses the object tree of a specified object and performs a function on any
         Operator:Traverse  object that has a process specified. If the traverse fails, LabVIEW returns FALSE.

                            Deletes the object. After LabVIEW deletes the object, all references to the object         Delete
                           are invalid.

                          Returns a tag value associated with the tag. Returns FALSE if the tag does not         Tag:Get Tag                                  exist.

        Tag:Remove Tag   Removes the specified tag. Returns FALSE if LabVIEW did not remove the tag.

         Tag:Set Tag        Sets a tag value. Returns FALSE if LabVIEW does not set the tag value.

         Tag:Set Tag                            Sets the persistence of the tag. Returns FALSE if not found.         Persistence

    ClassClass Operator:CallOperator:Call

        Calls the VI associated with the Operator Name, on the object. Returns FALSE if no
       operator VI is associated with the class of the object.

     Parameters

      Name                 Data type       Required       Description

        Operator Name                          Yes         Name of the operator VI.


        Context Data                             Yes            Context data.


     Remarks

      The following table lists the characteristics of this method.


        Data type


7670   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7670 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7671 ordinal=7671 -->
## Property and Method Reference

Property and Method Reference


 Available in Run-Time Engine                                                      Yes

 Available in Real-Time Operating System                                            Yes

 Settable when the VI is running                                                    Yes

 Loads the front panel into memory                                     No

 Need to authenticate before use                                       No

 Loads the block diagram into memory                                   No

 Remote access allowed                                             No

ClassClass Operator:TraverseOperator:Traverse

Traverses the object tree of a specified object and performs a function on any object
that has a process specified. If the traverse fails, LabVIEW returns FALSE.

Traverse is a way to find object references without having to recursively find them in a
VI or block diagram.

      Caution Do not attempt to modify code in traverse callbacks. This changes
       the stack the traverse operation is iterating through and can cause LabVIEW
        to crash.

Parameters

 Name          Data type  Required  Description

 Operator Name              Yes      Name of the operator VI.


 Context Data                 Yes        Context data.


 Traverse All              No        Determines whether to traverse the entire hierarchy.


                                                    © National Instruments 7671

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7671 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7672 ordinal=7672 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                                      Yes

         Available in Real-Time Operating System                                            Yes

         Settable when the VI is running                                                    Yes

        Loads the front panel into memory                                     No

       Need to authenticate before use                                       No

        Loads the block diagram into memory                                   No

       Remote access allowed                                             No

    DeleteDelete

       Deletes the object. After LabVIEW deletes the object, all references to the object are
        invalid.

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


7672   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7672 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7673 ordinal=7673 -->
## Property and Method Reference

Property and Method Reference

Tag:GetTag:Get TagTag

Returns a tag value associated with the tag. Returns FALSE if the tag does not exist.

Parameters

           Data Name             Required  Description            type

 Tag Name           Yes       Current tag of the item whose tag you want to set.


 Is                               Specifies whether the tag is persistent. The default is FALSE, which                No
 Persistent?                           is not persistent.


 Value           No       Returns the value of the tag.


Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                                      Yes

 Available in Real-Time Operating System                                            Yes

 Settable when the VI is running                                                    Yes

 Loads the front panel into memory                                     No

 Need to authenticate before use                                       No

 Loads the block diagram into memory                                   No

 Remote access allowed                                                           Yes


                                                    © National Instruments 7673

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7673 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7674 ordinal=7674 -->
## Property and Method Reference

Property and Method Reference

   Tag:RemoveTag:Remove TagTag

      Removes the specified tag. Returns FALSE if LabVIEW did not remove the tag.

     Parameters

      Name      Data type   Required   Description

        Tag Name                Yes         Current tag of the item whose tag you want to set.


        Old Value            No         Value of the tag before the change.


     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                                      Yes

         Available in Real-Time Operating System                                            Yes

         Settable when the VI is running                                                    Yes

        Loads the front panel into memory                                     No

       Need to authenticate before use                                       No

        Loads the block diagram into memory                                   No

       Remote access allowed                                                           Yes

    Tag:SetTag:Set TagTag

       Sets a tag value. Returns FALSE if LabVIEW does not set the tag value.


7674   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7674 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7675 ordinal=7675 -->
## Property and Method Reference

Property and Method Reference

Parameters

           Data Name             Required  Description
            type

 Tag Name           Yes       Current tag of the item whose tag you want to set.


 Value               Yes       Value to which you want to set the tag.


 Is                               Specifies whether the tag is persistent. The default is FALSE, which                No Persistent?                           is not persistent.


 Old Value         No       Value of the tag before the change.


Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                                      Yes

 Available in Real-Time Operating System                                            Yes

 Settable when the VI is running                                                    Yes

 Loads the front panel into memory                                     No

 Need to authenticate before use                                       No

 Loads the block diagram into memory                                   No

 Remote access allowed                                                           Yes

Tag:SetTag:Set TagTag PersistencePersistence

Sets the persistence of the tag. Returns FALSE if not found.

                                                    © National Instruments 7675

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7675 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7676 ordinal=7676 -->
## Property and Method Reference

Property and Method Reference

     Parameters

                  Data      Name             Required  Description
                   type

        Tag Name           Yes       Current tag of the item whose tag you want to set.


           Is                               Specifies whether the tag is persistent. The default is FALSE, which                             Yes         Persistent?                           is not persistent.


     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                                      Yes

         Available in Real-Time Operating System                                            Yes

         Settable when the VI is running                                                    Yes

        Loads the front panel into memory                                     No

       Need to authenticate before use                                       No

        Loads the block diagram into memory                                   No

       Remote access allowed                                                           Yes

      GenericGeneric PropertiesProperties

      You can set these properties on controls.


        Property  Description

         Class ID   Class identifier of the object.

         Class
              Name of the VI Server class that contains the object.
      Name


7676   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7676 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7677 ordinal=7677 -->
## Property and Method Reference

Property and Method Reference


 Property  Description

 Is On
 Block     Returns TRUE when the object is located on the block diagram.
 Diagram?

           Reference to the owning object. The type of the reference is Generic. An object of class
 Owner    Panel does not have an owner (it is the top-level object) and always returns Not A
         Refnum.

           Returns a reference to the VI that owns this object. Close this reference when you are
            finished using it. The reference this property returns does not keep the VI in memory. If Owning           the owning VI is removed from memory, this reference becomes invalid. Use the Open VI VI           Reference function to obtain a reference to a VI that stays in memory until you explicitly
           close the reference.

ClassClass IDID

Class identifier of the object.

This integer uniquely identifies the class of a LabVIEW object. To view the
corresponding class name of a LabVIEW object, use the Class Name property.

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


                                                    © National Instruments 7677

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7677 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7678 ordinal=7678 -->
## Property and Method Reference

Property and Method Reference

    ClassClass NameName

     Name of the VI Server class that contains the object.

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

     IsIs OnOn BlockBlock Diagram?Diagram?

       Returns TRUE when the object is located on the block diagram.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                                   Yes

         Settable when the VI is running                                  No

7678   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7678 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7679 ordinal=7679 -->
## Property and Method Reference

Property and Method Reference


 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

OwnerOwner

Reference to the owning object. The type of the reference is Generic. An object of class
Panel does not have an owner (it is the top-level object) and always returns Not A
Refnum.

All objects in LabVIEW have an owning object. For example, the front panel and block
diagram are the owning objects of all the objects contained within each, including
controls and indicators. However, if a control is a cluster, the cluster would the owning
object of all the objects inside it. Likewise, if the block diagram contains a sequence
structure, the structure is the owning object of all the objects inside it. Individual
controls also can be the owning object of less obvious objects. For example, numeric
controls own their label, caption, and the increment and decrement buttons.

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


                                                    © National Instruments 7679

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7679 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7680 ordinal=7680 -->
## Property and Method Reference

Property and Method Reference

   OwningOwning VIVI

       Returns a reference to the VI that owns this object. Close this reference when you are
       finished using it. The reference this property returns does not keep the VI in memory. If
       the owning VI is removed from memory, this reference becomes invalid. Use the Open
        VI Reference function to obtain a reference to a VI that stays in memory until you
        explicitly close the reference.

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

      GObjectGObject

      GObject Methods

      GObject Properties
   GObjectGObject MethodsMethods


       Method   Description

        Get Help   Returns the help information for the object.

7680   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7680 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7681 ordinal=7681 -->
## Property and Method Reference

Property and Method Reference


 Method   Description

 Info

 Move     Moves the object to the specified position.

 Object           Given a Gobject Reference, this method scrolls to and highlights the object. Highlight

           Replaces the current object with a new object and returns a reference to the new object.
 Replace   Use only one of the following inputs to specify the new object: Style, Path, or Palette
             String.

           Replaces the current object with a new object and returns a reference to the new object. Replace
          Use only one of the following inputs to specify the new object: Style, Path, or Palette No             String. This method does not maintain any size or color attributes of the object you Attributes            replace.

GetGet HelpHelp InfoInfo

Returns the help information for the object.

Parameters

         Data Name         Required  Description
          type

                         Path or symbolic path to the HTML file or to the compiled help file
 help                       linked to from the Context Help window. If this field is empty, the blue            No path                     Detailed help link does not appear in the Context Help window, and the
                           Detailed help button is dimmed.


                    HTML filename or index keyword of the topic that is launched from the
 help tag      No
                          Context Help window.


 has
            No        Indicates whether the object has an example.
 example


                                                    © National Instruments 7681

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7681 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7682 ordinal=7682 -->
## Property and Method Reference

Property and Method Reference

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

   MoveMove

      Moves the object to the specified position.

           Note If you attempt to move an object to the owning VI of another object,
            LabVIEW makes a copy of the object instead of moving the object.

     Parameters

                  Data
      Name           Required  Description
                   type

                               The location where you want to move the object. The position is
         position          Yes
                                          relative to the owning object.


                               The owning object. If you specify the owner, LabVIEW moves the
       owner         No
                                     object into the owning object.


7682   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7682 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7683 ordinal=7683 -->
## Property and Method Reference

Property and Method Reference


           Data Name           Required  Description
           type

                                              If TRUE, LabVIEW makes a copy of the object instead of moving the Duplicate?              No        object. If the owner you specify is located in a different VI, LabVIEW (F)                        assumes Duplicate? is TRUE.


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

ObjectObject HighlightHighlight

Given a Gobject Reference, this method scrolls to and highlights the object.

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                      No


                                                    © National Instruments 7683

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7683 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7684 ordinal=7684 -->
## Property and Method Reference

Property and Method Reference


         Settable when the VI is running                                      Yes

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

   ReplaceReplace

       Replaces the current object with a new object and returns a reference to the new
       object. Use only one of the following inputs to specify the new object: Style, Path, or
       Palette String.

     Parameters

               Data      Name        Required  Description
                type

         Style       No       Replaces the current object with a built-in object.


        Path       No       Replaces the current object with a control or a subVI.

                                    Specifies the name of the object on the palettes.

                               Note The Palette String of an object on the palettes differs         Palette
                 No              between the English version of LabVIEW and each localized         String
                                           version of LabVIEW. Also, the Palette String might change
                                    between different versions of LabVIEW.


     Remarks

      The following table lists the characteristics of this method.


        Data type

7684   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7684 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7685 ordinal=7685 -->
## Property and Method Reference

Property and Method Reference


 Available in Run-Time Engine                                         No

 Available in Real-Time Operating System                                 No

 Settable when the VI is running                                        No

 Loads the front panel into memory                                     No

 Need to authenticate before use                                       No

 Loads the block diagram into memory                                   No

 Remote access allowed                                                           Yes

ReplaceReplace NoNo AttributesAttributes

Replaces the current object with a new object and returns a reference to the new
object. Use only one of the following inputs to specify the new object: Style, Path, or
Palette String. This method does not maintain any size or color attributes of the object
you replace.

Parameters

        Data
 Name        Required  Description        type

 Style       No       Replaces the current object with a built-in object.


 Path       No       Replaces the current object with a control or a subVI.

                           Specifies the name of the object on the palettes.

                         Note The Palette String of an object on the palettes differs Palette
           No              between the English version of LabVIEW and each localized String
                                   version of LabVIEW. Also, the Palette String might change
                             between different versions of LabVIEW.


                                                    © National Instruments 7685

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7685 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7686 ordinal=7686 -->
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

   GObjectGObject PropertiesProperties


        Property              Description

                        Maximum bounding area of the object specified in terms of width and       Bounds                               height in pixels.

        Bounds:Area Height    Height of the maximum bounding area of the object in pixels.

        Bounds:Area Width    Width of the maximum bounding area of the object in pixels.

                              Returns the array of qualified names listing every dependency of the given
                                object loaded into memory.

        Dependencies:Found  For a standard subVI node, this might be one qualified name for the subVI.
       Dependency Names    For a polymorphic VI subVI node, this might be two names: one name for
                              the polymorphic VI and one name for the instance VI. For typedef controls,
                               only a single name will be returned even if the typedef has nested typedefs.
                                   Call this property on the nested controls to get the nested typedef names.


        Dependencies:Found  Returns the array of paths listing every dependency that is not missing of
       Dependency Paths     the given object.


7686   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7686 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7687 ordinal=7687 -->
## Property and Method Reference

Property and Method Reference


Property              Description

                      For a standard subVI node, this might be a single path to the subVI. For a
                     polymorphic VI subVI node, this might be two paths: one path for the
                     polymorphic VI and one path for the instance VI. For typedef controls, only
                    a single path will be returned even if the typedef has nested typedefs. Call
                          this property on the nested controls to get the nested typedef paths.


                      Returns the array of qualified names listing every missing dependency of
                      the given object.

                      For a standard subVI node, this might be one qualified name for the subVI.
Dependencies:Missing                      For a polymorphic VI subVI node, this might be two names: one name for
Dependency Names                      the polymorphic VI and one name for the instance VI. For typedef controls,
                      only a single name will be returned even if the typedef has nested typedefs
                       that are also missing. Call this property on the nested controls to get the
                      missing nested typedef names.


                      Returns the array of paths listing every missing dependency of the given
                        object.

                      For a standard subVI node, this might be a single path to the subVI. For a
Dependencies:Missing                     polymorphic VI subVI node, this might be two paths: one path for the
Dependency Paths                     polymorphic VI and one path for the instance VI. For typedef controls, only
                    a single path will be returned even if the typedef has nested typedefs that
                      are also missing. Call this property on the nested controls to get the
                      missing nested typedef paths.

                      Returns an array of GObject references to all members of the same front
Group Member Refs[]
                     panel grouping (including locked groups) as the source object.

                      Returns TRUE if and only if the GObject is a member of a group (including
Grouped
                      locked groups).

Locked               Returns TRUE if and only if the GObject has been locked to prevent editing.

                      Returns the coordinates of all the sides of the object excluding labels,
Master Bounds Rect
                       captions, and other visible parts connected to the object.

                       Position of the top left corner of the bounding rectangle of the object on
Position
                      the front panel window in terms of left and top coordinates.


                                                    © National Instruments 7687

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7687 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7688 ordinal=7688 -->
## Property and Method Reference

Property and Method Reference


        Property              Description

                                Position of the left corner of the bounding rectangle of the object on the          Position:Left                                  front panel window.

                                Position of the top corner of the bounding rectangle of the object on the         Position:Top                                  front panel window.

         Selected              Returns TRUE if the GObject is selected.

                              Returns the coordinates of all sides of the entire object including labels,         Total Bounds Rect                                 captions, and other visible parts connected to the object.

                              Returns the unique identifier (UID) for the object. UIDs are identifiers for
        UID                LabVIEW objects and are always unique within the same VI. Inspect the UID
                                 of an object to verify that it is the exact object that you want to manipulate.

   BoundsBounds

     Maximum bounding area of the object specified in terms of width and height in pixels.

       For a front panel object, this property returns the dimensions of the rectangle
       enclosing all the visible object components, such as the control, caption, label, graph
       legends, and so on.

      You cannot use this property to change the size of an object. To change the size of an
       object programmatically, use more specific properties such as Text Width or Plot
        Area:Size.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                               Read Only

         Available in Run-Time Engine                                        Yes (Read Only)

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                             No


7688   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7688 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7689 ordinal=7689 -->
## Property and Method Reference

Property and Method Reference


 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

Bounds:AreaBounds:Area HeightHeight

Height of the maximum bounding area of the object in pixels.

This property is an element of the Bounds property.

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

Bounds:AreaBounds:Area WidthWidth

Width of the maximum bounding area of the object in pixels.

This property is an element of the Bounds property.


                                                    © National Instruments 7689

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7689 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7690 ordinal=7690 -->
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

   Dependencies:FoundDependencies:Found DependencyDependency NamesNames

       Returns the array of qualified names listing every dependency of the given object
      loaded into memory.

       For a standard subVI node, this might be one qualified name for the subVI. For a
      polymorphic VI subVI node, this might be two names: one name for the polymorphic VI
      and one name for the instance VI. For typedef controls, only a single name will be
       returned even if the typedef has nested typedefs. Call this property on the nested
       controls to get the nested typedef names.

       Special behavior exists for some objects

            • Network shared variables: The path is always empty. The object is always
          considered found even if the library that defines the variable is missing, because
          the variable may be found at run time.
            • Dynamic dispatch subVI: The path is to the class and name is to the member VI.
            • LabVIEW class property node: The path is to the class and name is to the member
            VI even if the member VI is static dispatch. These objects are classified as found if


7690   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7690 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7691 ordinal=7691 -->
## Property and Method Reference

Property and Method Reference

   the class is found even if the member VIs are missing.

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

Dependencies:FoundDependencies:Found DependencyDependency PathsPaths

Returns the array of paths listing every dependency that is not missing of the given
object.

For a standard subVI node, this might be a single path to the subVI. For a polymorphic
VI subVI node, this might be two paths: one path for the polymorphic VI and one path
for the instance VI. For typedef controls, only a single path will be returned even if the
typedef has nested typedefs. Call this property on the nested controls to get the nested
typedef paths.

  • Network shared variables: The path is always empty. The object is always
   considered found even if the library that defines the variable is missing, because
   the variable may be found at run time.
  • Dynamic dispatch subVIs: The path is to the class and name is to the member VI.
  • LabVIEW class property nodes: The path is to the class and name is to the member
    VI even if the member VI is static dispatch. These objects are classified as found if


                                                    © National Instruments 7691

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7691 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7692 ordinal=7692 -->
## Property and Method Reference

Property and Method Reference

          the class is found even if the member VIs are missing.

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

   Dependencies:MissingDependencies:Missing DependencyDependency NamesNames

       Returns the array of qualified names listing every missing dependency of the given
       object.

       For a standard subVI node, this might be one qualified name for the subVI. For a
      polymorphic VI subVI node, this might be two names: one name for the polymorphic VI
      and one name for the instance VI. For typedef controls, only a single name will be
       returned even if the typedef has nested typedefs that are also missing. Call this
       property on the nested controls to get the missing nested typedef names.

       Special behavior exists for some objects

            • Network shared variables: The path is always empty. The object is always
          considered found even if the library that defines the variable is missing, because
          the variable may be found at run time.
            • Dynamic dispatch subVIs: The path is to the class and name is to the member VI.
            • LabVIEW class property nodes: The path is to the class and name is to the member

7692   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7692 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7693 ordinal=7693 -->
## Property and Method Reference

Property and Method Reference

    VI even if the member VI is static dispatch. These objects are classified as found if
   the class is found even if the member VIs are missing.

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

Dependencies:MissingDependencies:Missing DependencyDependency PathsPaths

Returns the array of paths listing every missing dependency of the given object.

For a standard subVI node, this might be a single path to the subVI. For a polymorphic
VI subVI node, this might be two paths: one path for the polymorphic VI and one path
for the instance VI. For typedef controls, only a single path will be returned even if the
typedef has nested typedefs that are also missing. Call this property on the nested
controls to get the missing nested typedef paths.

Special behavior exists for some objects

  • Network shared variables: The path is always empty. The object is always
   considered found even if the library that defines the variable is missing, because
   the variable may be found at run time.
  • Dynamic dispatch subVIs: The path is to the class and name is to the member VI.
  • LabVIEW class property nodes: The path is to the class and name is to the member

                                                    © National Instruments 7693

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7693 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7694 ordinal=7694 -->
## Property and Method Reference

Property and Method Reference

            VI even if the member VI is static dispatch. These objects are classified as found if
          the class is found even if the member VIs are missing.

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

   GroupGroup MemberMember Refs[]Refs[]

       Returns an array of GObject references to all members of the same front panel
      grouping (including locked groups) as the source object.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No


7694   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7694 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7695 ordinal=7695 -->
## Property and Method Reference

Property and Method Reference


 Loads the front panel into memory                                         Yes

 Need to authenticate before use                                 No

 Loads the block diagram into memory                                      Yes

 Remote access allowed                                                   Yes

GroupedGrouped

Returns TRUE if and only if the GObject is a member of a group (including locked
groups).

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

LockedLocked

Returns TRUE if and only if the GObject has been locked to prevent editing.

Remarks

The following table lists the characteristics of this property.

                                                    © National Instruments 7695

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7695 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7696 ordinal=7696 -->
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

   MasterMaster BoundsBounds RectRect

       Returns the coordinates of all the sides of the object excluding labels, captions, and
       other visible parts connected to the object.

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


7696   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7696 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7697 ordinal=7697 -->
## Property and Method Reference

Property and Method Reference

PositionPosition

Position of the top left corner of the bounding rectangle of the object on the front
panel window in terms of left and top coordinates.

The bounding rectangle of the object includes all visible parts of the object. For
example, if the object label is visible and you wire the top coordinate to this property,
LabVIEW positions the top of the label at the coordinate you wired. If the object label is
not visible, LabVIEW positions the top of the remaining visible parts of the object at the
coordinate you wired.

      Note LabVIEW sets the origin for this property when you create a VI. When
       you scroll the owning pane, the origin does not change but instead scrolls
       with the owning pane. If you do not move the object, this property returns
       the same coordinates for the object regardless of whether you scroll the
       owning pane. Use the Origin property with this property to calculate the
        current position of an object in relation to the owning pane. For most front
       panel objects, this property returns the position of the object relative to the
        origin of the owning pane. For panes, this property returns the position of the
      pane relative to the global panel coordinate system.

If you attempt to reposition an object that is grouped with other objects, LabVIEW
repositions only the object you specify, not the whole group.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

                                                    © National Instruments 7697

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7697 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7698 ordinal=7698 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    Position:LeftPosition:Left

       Position of the left corner of the bounding rectangle of the object on the front panel
      window.

       This property is an element of the Position property.

           Note For most front panel objects, this property returns the position of the
               object relative to the origin of the owning pane. For panes, this property
               returns the position of the pane relative to the global panel coordinate
              system.

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


7698   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7698 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7699 ordinal=7699 -->
## Property and Method Reference

Property and Method Reference

Position:TopPosition:Top

Position of the top corner of the bounding rectangle of the object on the front panel
window.

This property is an element of the Position property.

      Note For most front panel objects, this property returns the position of the
        object relative to the origin of the owning pane. For panes, this property
        returns the position of the pane relative to the global panel coordinate
       system.

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

SelectedSelected

Returns TRUE if the GObject is selected.


                                                    © National Instruments 7699

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7699 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7700 ordinal=7700 -->
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

    TotalTotal BoundsBounds RectRect

       Returns the coordinates of all sides of the entire object including labels, captions, and
       other visible parts connected to the object.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                                   Yes

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No


7700   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7700 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7701 ordinal=7701 -->
## Property and Method Reference

Property and Method Reference


 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

UIDUID

Returns the unique identifier (UID) for the object. UIDs are identifiers for LabVIEW
objects and are always unique within the same VI. Inspect the UID of an object to verify
that it is the exact object that you want to manipulate.

A UID is always associated with the same object, even after you save the VI. However, if
you delete an object, LabVIEW might assign the UID for that deleted object to a
different object in the future. To detect this situation and ensure each UID refers to the
object that you expect, check the Class Name property or Label property of the object
in addition to the UID.

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

DecorationDecoration

Decoration Properties

                                                    © National Instruments 7701

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7701 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7702 ordinal=7702 -->
## Property and Method Reference

Property and Method Reference

   DecorationDecoration PropertiesProperties


        Property       Description

                        Colors of the decoration expressed in terms of (Foreground Color, Background
         Colors                         Color) pair.

         Colors:BG                     Background color of the decoration.         Color

         Colors:FG
                      Foreground color of the decoration.         Color

       Owning Pane   Returns a reference to the owning pane of the referenced decoration.

         Size          Bounding area of the decoration specified in terms of width and height in pixels.

         Size:Height    Height of the bounding area of the decoration in pixels.

         Size:Width     Width of the bounding area of the decoration in pixels.

          Visible          Indicates whether the decoration is visible.

    ColorsColors

       Colors of the decoration expressed in terms of (Foreground Color, Background Color)
        pair.

           If the description is a text label, then you must set the Text Colors:BG Color property to
       transparent to see the decoration colors of an object.

      You can set the color of the front panel object by wiring a hexadecimal number with
       the form RRGGBB or by wiring the color box constant to the property.

       This property is similar to using the color picker to specify the foreground and
      background colors of the decoration.

     Remarks

      The following table lists the characteristics of this property.


7702   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7702 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7703 ordinal=7703 -->
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

Colors:BGColors:BG ColorColor

Background color of the decoration.

You can set the color of the front panel object by wiring a hexadecimal number with
the form RRGGBB or by wiring the color box constant to the property.

This property is an element of the Colors property.

This property is similar to using the color picker to specify the background color of the
decoration.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes


                                                    © National Instruments 7703

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7703 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7704 ordinal=7704 -->
## Property and Method Reference

Property and Method Reference


        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    Colors:FGColors:FG ColorColor

      Foreground color of the decoration.

      You can set the color of the front panel object by wiring a hexadecimal number with
       the form RRGGBB or by wiring the color box constant to the property.

       This property is an element of the Colors property.

       This property is similar to using the color picker to specify the foreground color of the
       decoration.

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


7704   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7704 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7705 ordinal=7705 -->
## Property and Method Reference

Property and Method Reference

OwningOwning PanePane

Returns a reference to the owning pane of the referenced decoration.

For nested decorations, this property returns a reference to the pane that owns the
object that contains the referenced decoration.

      Note If a cluster contains the decoration, the property returns a reference to
       the pane inside the cluster and not the pane that owns the cluster.

If the decoration is not on a pane, this property returns Not a Refnum.

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

SizeSize

Bounding area of the decoration specified in terms of width and height in pixels.

This property is similar to setting the width and height of the decoration in the Resize
Objects dialog box.

                                                    © National Instruments 7705

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7705 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7706 ordinal=7706 -->
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

    Size:HeightSize:Height

       Height of the bounding area of the decoration in pixels.

       This property is an element of the Size property.

       This property is similar to the Height item in the Resize Objects dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes


7706   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7706 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7707 ordinal=7707 -->
## Property and Method Reference

Property and Method Reference


 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Size:WidthSize:Width

Width of the bounding area of the decoration in pixels.

This property is an element of the Size property.

This property is similar to the Width item in the Resize Objects dialog box.

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

Indicates whether the decoration is visible.


                                                    © National Instruments 7707

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7707 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7708 ordinal=7708 -->
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

    TextText

       Text Methods

       Text Properties
    TextText MethodsMethods


       Method                       Description

       Move to Default Location      Move a label to its default location relative to its owner.

   MoveMove toto DefaultDefault LocationLocation
   MoveMove toto DefaultDefault LocationLocation

      Move a label to its default location relative to its owner.

7708   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7708 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7709 ordinal=7709 -->
## Property and Method Reference

Property and Method Reference

If you use the Move to Default Location method after you use the Lock property
programmatically, the label does not remain locked to the position you select, but
returns to the default location. The label then is locked to the default position until
you unlock the label.

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                             Yes

 Settable when the VI is running                                      Yes

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

TextText PropertiesProperties


 Property       Description

 Attached       Gets or sets the reference to a block diagram object to which a text label is
 Object          attached. This property only works with free labels on the block diagram.

 Document
                Returns the size required to display the entire text.
 Bounds

 Document
                Returns the height required to display the entire text.
 Bounds:Height

 Document
                Returns the width required to display the entire text.
 Bounds:Width

 Enable         Automatically detects URLs of the form proto://domain, displays them in
 Hyperlinks     underlined blue text, and opens them in the default web browser when clicked.

 Font            Cluster of font name, size, bold, italic, underline, strikeout.

                                                    © National Instruments 7709

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7709 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7710 ordinal=7710 -->
## Property and Method Reference

Property and Method Reference


        Property       Description

         Font:Bold       Indicates whether the text is bold.

                         Sets the color of the currently selected text. You can use the Selection property to         Font:Color                           select a subset of a string.

          Font:Italic       Indicates whether the text is italic.

                       Font name. Predefined font names include App Font, Sys Font, and Dlg
        Font:Name
                     Font. If you provide an empty string, this property returns an error.

         Font:Size       Font size.

         Font:Strikeout  Indicates whether the text is in the strikeout font.

         Font:Underline  Indicates whether the text is underlined.

          Justification    Gets and sets the justification of text.

                       Locks the label or caption to the owning control, indicator, or terminal. You cannot
                          set this property on text fields that are not labels or captions, such as Boolean text,
        Lock          numeric text, free labels, and so on.

                         This property is similar to the Lock Label option in the shortcut menu.

          Scroll Position  Position of the scroll box in the scroll bar.

                         Text selection specified in terms of character positions for the beginning of
         Selection       selection (inclusive) and end of selection (not inclusive). If you set the start and
                    end to be the same, LabVIEW inserts a caret into the text.

         Selection:End   Allows you to select the end point of text in a text string.

          Selection:Start  Character position for the beginning of selection (inclusive).

                         Sets whether the size of the text object changes according to the text included. You
         Size to Text?
                      can write this property only for free labels, control labels, and captions.

                         Text as displayed in the front panel object. For example, if you set a string control
         Text            to use Password Display, this property returns the password string, such as ****,
                       not the Normal Display of the string.

         Text Colors     Changes the foreground and background color of a text string.

         Text Colors:BG
                      Background color of text object.
         Color

         Text            Text color for all fonts in the text.


7710   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7710 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7711 ordinal=7711 -->
## Property and Method Reference

Property and Method Reference


 Property       Description

 Colors:Text
 Color

 Text Overflow   Display a gradient overflow visual effect when text gets clipped by the controls.

 Vertical        Gets and sets the vertical arrangement for the text. You can set the vertical
 Arrangement   arrangement for labels, captions, and free labels.

AttachedAttached ObjectObject
AttachedAttached ObjectObject

Gets or sets the reference to a block diagram object to which a text label is attached.
This property only works with free labels on the block diagram.

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


                                                    © National Instruments 7711

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7711 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7712 ordinal=7712 -->
## Property and Method Reference

Property and Method Reference

   DocumentDocument BoundsBounds
   DocumentDocument BoundsBounds

       Returns the size required to display the entire text.

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

   DocumentDocument Bounds:HeightBounds:Height
   DocumentDocument Bounds:HeightBounds:Height

       Returns the height required to display the entire text.

     Remarks

      The following table lists the characteristics of this property.


        Data type

7712   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7712 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7713 ordinal=7713 -->
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

DocumentDocument Bounds:WidthBounds:Width
DocumentDocument Bounds:WidthBounds:Width

Returns the width required to display the entire text.

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


                                                    © National Instruments 7713

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7713 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7714 ordinal=7714 -->
## Property and Method Reference

Property and Method Reference

   EnableEnable HyperlinksHyperlinks
   EnableEnable HyperlinksHyperlinks

       Automatically detects URLs of the form proto://domain, displays them in
       underlined blue text, and opens them in the default web browser when clicked.

       This property is only valid when the text is a free label. For other types of text, using
        this property returns error 1077.

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

   FontFont
   FontFont

       Cluster of font name, size, bold, italic, underline, strikeout.

       This property is similar to the Font option in the Font Style dialog box.


7714   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7714 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7715 ordinal=7715 -->
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

Font:BoldFont:Bold
Font:BoldFont:Bold

Indicates whether the text is bold.

This property is an element of the Font property.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

                                                    © National Instruments 7715

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7715 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7716 ordinal=7716 -->
## Property and Method Reference

Property and Method Reference


        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   Font:ColorFont:Color
    Font:ColorFont:Color

       Sets the color of the currently selected text. You can use the Selection property to
        select a subset of a string.

      You can set the color of the front panel object by wiring a hexadecimal number with
       the form RRGGBB or by wiring the color box constant to the property.

       This property is an element of the Font property.

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


7716   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7716 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7717 ordinal=7717 -->
## Property and Method Reference

Property and Method Reference

Font:ItalicFont:Italic
Font:ItalicFont:Italic

Indicates whether the text is italic.

This property is an element of the Font property.

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

Font:NameFont:Name
Font:NameFont:Name

Font name. Predefined font names include App Font, Sys Font, and Dlg Font.
If you provide an empty string, this property returns an error.

This property is an element of the Font property.


                                                    © National Instruments 7717

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7717 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7718 ordinal=7718 -->
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

   Font:SizeFont:Size
    Font:SizeFont:Size

      Font size.

       This property is an element of the Font property.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

7718   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7718 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7719 ordinal=7719 -->
## Property and Method Reference

Property and Method Reference


 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Font:StrikeoutFont:Strikeout
Font:StrikeoutFont:Strikeout

Indicates whether the text is in the strikeout font.

This property is an element of the Font property.

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


                                                    © National Instruments 7719

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7719 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7720 ordinal=7720 -->
## Property and Method Reference

Property and Method Reference

   Font:UnderlineFont:Underline
    Font:UnderlineFont:Underline

       Indicates whether the text is underlined.

       This property is an element of the Font property.

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

    JustificationJustification
    JustificationJustification

       Gets and sets the justification of text.

       Values include

            • Left


7720   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7720 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7721 ordinal=7721 -->
## Property and Method Reference

Property and Method Reference

  • Center
  • Right

This property is similar to the Align option in the Font Style dialog box.

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

LockLock
LockLock

Locks the label or caption to the owning control, indicator, or terminal. You cannot set
this property on text fields that are not labels or captions, such as Boolean text,
numeric text, free labels, and so on.

This property is similar to the Lock Label option in the shortcut menu.

      Note You cannot lock labels to wires.

You can use the Position:Left and Position:Top properties to move a label

                                                    © National Instruments 7721

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7721 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7722 ordinal=7722 -->
## Property and Method Reference

Property and Method Reference

       programmatically. You also can use the Move to Default Location method to return the
       label to its default position programmatically.

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

    ScrollScroll PositionPosition
    ScrollScroll PositionPosition

       Position of the scroll box in the scroll bar.

      To set the position, wire a numeric value to this property that represents the line
      number to which you want to scroll. LabVIEW pins the numeric value that you wire to
       the property to the last line of the scroll box. If you want to scroll to the last line of text,
       wire the maximum numeric value for the line number to the property.

           If you wire a negative numeric value or a numeric valuer larger than the scroll bar
     maximum to this property, the scroll box scrolls to the last line of text.

      The position is 0-indexed. For example, if a string control contains 6 lines of text, you
      can wire a value of 2 to this property to move the scroll box to the position of the third

7722   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7722 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7723 ordinal=7723 -->
## Property and Method Reference

Property and Method Reference

line.

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

SelectionSelection
SelectionSelection

Text selection specified in terms of character positions for the beginning of selection
(inclusive) and end of selection (not inclusive). If you set the start and end to be the
same, LabVIEW inserts a caret into the text.

If you want to highlight the text, you must set key focus on a control before you use the
Selection property.

Remarks

The following table lists the characteristics of this property.


 Data type


                                                    © National Instruments 7723

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7723 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7724 ordinal=7724 -->
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

   Selection:EndSelection:End
    Selection:EndSelection:End

       Allows you to select the end point of text in a text string.

      Use this property in conjunction with the Text Properties to programmatically change
      a property of a subset of a string.

       This property is an element of the Selection property.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

7724   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7724 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7725 ordinal=7725 -->
## Property and Method Reference

Property and Method Reference


 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Selection:StartSelection:Start
Selection:StartSelection:Start

Character position for the beginning of selection (inclusive).

Use this property in conjunction with the Text Properties to programmatically change
a property of a subset of a string.

This property is an element of the Selection property.

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


                                                    © National Instruments 7725

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7725 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7726 ordinal=7726 -->
## Property and Method Reference

Property and Method Reference

    SizeSize toto Text?Text?
    SizeSize toto Text?Text?

       Sets whether the size of the text object changes according to the text included. You can
       write this property only for free labels, control labels, and captions.

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

   TextText
    TextText

       Text as displayed in the front panel object. For example, if you set a string control to
      use Password Display, this property returns the password string, such as ****, not the
      Normal Display of the string.

           If the text string is a free label or a caption, you can write this property when the VI is
       running, and it is available in the Run-Time Engine. If the text string is an owned label,

7726   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7726 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7727 ordinal=7727 -->
## Property and Method Reference

Property and Method Reference

you cannot write this property when the VI is running, and it is available in the Run-
Time Engine only for reading.

If the text string is a unit label, you can write this property when the VI is running, and
it is available in the Run-Time Engine. However, the unit you write must be compatible
with the existing unit. If the units are not compatible, LabVIEW returns an error and
sets the unit label to the base unit.

If you read or write this property for a nonexistent caption in a VI that is not running,
LabVIEW creates the caption. If the VI is running, LabVIEW returns an error.

If you want to determine whether a front panel object has a caption, use the Has
Caption property instead of comparing the value of the Text property to an empty
string. When you read the Text property of a nonexistent caption, LabVIEW creates a
caption and copies the label into the caption. Therefore, the Text property does not
accurately reflect whether the caption contained text before the Text property was
called.

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


                                                    © National Instruments 7727

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7727 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7728 ordinal=7728 -->
## Property and Method Reference

Property and Method Reference

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Controls and Indicators\Numeric\Numeric
        with Units.vi
   TextText ColorsColors
    TextText ColorsColors

      Changes the foreground and background color of a text string.

      You can set the color of the front panel object by wiring a hexadecimal number with
       the form RRGGBB or by wiring the color box constant to the property.

       This property is similar to the Color option in the Font Style dialog box.

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


7728   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7728 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7729 ordinal=7729 -->
## Property and Method Reference

Property and Method Reference

TextText Colors:BGColors:BG ColorColor
TextText Colors:BGColors:BG ColorColor

Background color of text object.

You can set the color of the front panel object by wiring a hexadecimal number with
the form RRGGBB or by wiring the color box constant to the property.

This property is an element of the Text Colors property.

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

TextText Colors:TextColors:Text ColorColor
TextText Colors:TextColors:Text ColorColor

Text color for all fonts in the text.


                                                    © National Instruments 7729

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7729 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7730 ordinal=7730 -->
## Property and Method Reference

Property and Method Reference

      You can set the color of the front panel object by wiring a hexadecimal number with
       the form RRGGBB or by wiring the color box constant to the property.

       This property is an element of the Text Colors property.

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

   TextText OverflowOverflow
    TextText OverflowOverflow

       Display a gradient overflow visual effect when text gets clipped by the controls.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

7730   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7730 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7731 ordinal=7731 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

VerticalVertical ArrangementArrangement
VerticalVertical ArrangementArrangement

Gets and sets the vertical arrangement for the text. You can set the vertical
arrangement for labels, captions, and free labels.

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

NumericTextNumericText


                                                    © National Instruments 7731

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7731 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7732 ordinal=7732 -->
## Property and Method Reference

Property and Method Reference

      NumericText Properties
   NumericTextNumericText PropertiesProperties
   NumericTextNumericText PropertiesProperties


        Property         Description

                            Specifies the format and precision of the numeric text. Format can be 0-Decimal,
                               1-Scientific, 2-Engineering, 3-Binary, 4-Octal, 5-Hexadecimal, 6-Relative Time,         Display Format                         7-Time and Date, 8-SI, or 9-Custom (read-only). Precision is the number of digits
                              after the decimal point.

                            Specifies the format of the numeric text. This property accepts the following
                         format values: 0-Decimal, 1-Scientific, 2-Engineering, 3-Binary, 4-Octal,
                         5-Hexadecimal, 6-Relative Time, 7-Time and Date, 8-SI, and 9-Custom (read-
         Display                              only). You cannot wire a value of 9 to this property because the value is read-        Format:Format
                             only. This property returns a value of 9 if the object uses automatic formatting,
                          the format string contains text, or the format string includes more than one
                         format specifier.

         Display        Number of digits after the decimal point. If you wire a value of 9 to the Format
         Format:Precision  property, this property returns an error.

        Format String     Gets and sets the format of the numeric control.

   DisplayDisplay FormatFormat
    DisplayDisplay FormatFormat

       Specifies the format and precision of the numeric text. Format can be 0-Decimal,
        1-Scientific, 2-Engineering, 3-Binary, 4-Octal, 5-Hexadecimal, 6-Relative Time, 7-Time
      and Date, 8-SI, or 9-Custom (read-only). Precision is the number of digits after the
      decimal point.

       This property is similar to the Display Format item on the shortcut menu of a numeric
       control or indicator.


7732   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7732 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7733 ordinal=7733 -->
## Property and Method Reference

Property and Method Reference

This property is similar to the options on the Display Format page of the Properties
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

DisplayDisplay Format:FormatFormat:Format
DisplayDisplay Format:FormatFormat:Format

Specifies the format of the numeric text. This property accepts the following format
values: 0-Decimal, 1-Scientific, 2-Engineering, 3-Binary, 4-Octal, 5-Hexadecimal,
6-Relative Time, 7-Time and Date, 8-SI, and 9-Custom (read-only). You cannot wire a
value of 9 to this property because the value is read-only. This property returns a value
of 9 if the object uses automatic formatting, the format string contains text, or the
format string includes more than one format specifier.

If you select floating point representation for the numeric text, you cannot wire a value
of 3, 4, or 5 to this property. Binary, Octal, and Hexadecimal formats are not valid for
floating point numbers. If you wire one of these values, this property returns an error.

This property is an element of the Display Format property.

                                                    © National Instruments 7733

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7733 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7734 ordinal=7734 -->
## Property and Method Reference

Property and Method Reference

       This property is similar to the Format option on the Display Format page of the
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

   DisplayDisplay Format:PrecisionFormat:Precision
    DisplayDisplay Format:PrecisionFormat:Precision

     Number of digits after the decimal point. If you wire a value of 9 to the Format
       property, this property returns an error.

       This property is an element of the Display Format property.

       This property is similar to the Precision Type option on the Display Format page of the
       Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


7734   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7734 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7735 ordinal=7735 -->
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

FormatFormat StringString
FormatFormat StringString

Gets and sets the format of the numeric control.

Refer to the valid format specifiers for numeric data types table for information about
which format specifiers you can set depending on the data type of the numeric control
and the format specifiers syntax elements table for descriptions of the syntax
elements.

If you want to format a string to display time, enclose the string with %<>T.

You also can use the Display Format:Format property to get or set the format of the
numeric control. Setting the format of the numeric control using the Format &
Precision:Format property overwrites any formatting you set using the Format String
property.

This property is similar to the Format string option on the Display Format page of the
Properties dialog box. Access the Format string option by selecting the Advanced
editing mode option on the Display Format page of the Properties dialog box.


                                                    © National Instruments 7735

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7735 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7736 ordinal=7736 -->
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

    ScaleScale

       Scale Properties
    ScaleScale PropertiesProperties


        Property         Description

                            Specifies the format and precision of the scale. Format can be 0-Decimal,
                               1-Scientific, 2-Engineering, 3-Binary, 4-Octal, 5-Hexadecimal, 6-Relative Time,
         Display Format
                         7-Time and Date, 8-SI, or 9-Custom (read-only). Precision is the number of digits
                               after the decimal point.

                            Specifies the format of the numeric increments of the scale. This property
                          accepts the following format values: 0-Decimal, 1-Scientific, 2-Engineering,
                            3-Binary, 4-Octal, 5-Hexadecimal, 6-Relative Time, 7-Time and Date, 8-SI, and
         Display                       9-Custom (read-only). You cannot wire a value of 9 to this property because the        Format:Format
                          value is read-only. This property returns a value of 9 if the object uses automatic
                            formatting, the format string contains text, or the format string includes more
                        than one format specifier.


7736   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7736 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7737 ordinal=7737 -->
## Property and Method Reference

Property and Method Reference


Property         Description

Display        Number of digits after the decimal point. If you wire a value of 9 to the Format
Format:Precision  property, this property returns an error.

Editable          Allows editing of scale values.

                            If TRUE, reverses the positions of the minimum and maximum values on theFlipped
                    scale.

Format String     Sets the format string of the scale.

Mapping Mode    Scale mapping mode: 0-Linear, 1-Logarithmic.

Marker           Reference to the scale marker.

Marker Colors     Text color and background color of scale marker.

Marker                Background color of the scale marker.Colors:BG Color

Marker                 Color of the scale marker text.Colors:Text Color

              A scale is a component of many front panel objects in LabVIEW, such as the X
               and Y scales of graphs and charts. The scale consists of a range of values,Range
                   specified as a cluster of (Minimum, Maximum, Increment, Minor Increment, and
                     Start).

                Increment value of scale. Use this property to determine the distance betweenRange:Increment                    tick marks.

             Maximum value of scale. Use this property to set the maximum value allowed inRange:Maximum                 the range.

              Minimum value of scale. Use this property to set the minimum value allowed inRange:Minimum
                 the range.

Range:Minor     Minor increment value of scale. Use this property to determine the distance
Increment       between minor tick marks.

                   Start value of scale. Use this property to determine the value of the first tick
Range:Start
                marker after the minimum.

                 Gets or sets the style of the marks on a scale. The values (0-8) for this property
                correspond with the options on the Style shortcut menu, available by right-
Style
                    clicking a scale on a graph or chart and selecting Style, from top-left (0) to
                  bottom-right (8).

Tick Colors       Gets or sets the tick color and minor tick color of the scale.


                                                    © National Instruments 7737

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7737 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7738 ordinal=7738 -->
## Property and Method Reference

Property and Method Reference


        Property         Description

         Tick
         Colors:Minor      Color of the minor tick mark.
         Tick Color

         Tick Colors:Tick                          Color of the tick mark.
         Color

        Uniform Marker                        Determines whether the markers are uniformly spaced.        Spacing?

          Visible         Shows the scale.

    DisplayDisplay FormatFormat

       Specifies the format and precision of the scale. Format can be 0-Decimal, 1-Scientific,
       2-Engineering, 3-Binary, 4-Octal, 5-Hexadecimal, 6-Relative Time, 7-Time and Date,
        8-SI, or 9-Custom (read-only). Precision is the number of digits after the decimal point.

       This property is similar to the options on the Display Format page of the Properties
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


7738   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7738 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7739 ordinal=7739 -->
## Property and Method Reference

Property and Method Reference

DisplayDisplay Format:FormatFormat:Format

Specifies the format of the numeric increments of the scale. This property accepts the
following format values: 0-Decimal, 1-Scientific, 2-Engineering, 3-Binary, 4-Octal,
5-Hexadecimal, 6-Relative Time, 7-Time and Date, 8-SI, and 9-Custom (read-only). You
cannot wire a value of 9 to this property because the value is read-only. This property
returns a value of 9 if the object uses automatic formatting, the format string contains
text, or the format string includes more than one format specifier.

If you select floating point representation for the numeric increments, you cannot wire
a value of 3, 4, or 5 to this property. Binary, Octal, and Hexadecimal formats are not
valid for floating point numbers. If you wire one of these values, this property returns
an error.

This property is an element of the Display Format property.

This property is similar to the options on the Display Format page of the Properties
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


                                                    © National Instruments 7739

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7739 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7740 ordinal=7740 -->
## Property and Method Reference

Property and Method Reference

    DisplayDisplay Format:PrecisionFormat:Precision

     Number of digits after the decimal point. If you wire a value of 9 to the Format
       property, this property returns an error.

       This property is an element of the Display Format property.

       This property is similar to the Digits option on the Display Format page of the
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

    EditableEditable

       Allows editing of scale values.

     Remarks

      The following table lists the characteristics of this property.


7740   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7740 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7741 ordinal=7741 -->
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

FlippedFlipped

If TRUE, reverses the positions of the minimum and maximum values on the scale.

This property is similar to the Inverted option on the Scale page of the Properties
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


                                                    © National Instruments 7741

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7741 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7742 ordinal=7742 -->
## Property and Method Reference

Property and Method Reference

   FormatFormat StringString

       Sets the format string of the scale.

       Refer to the valid format specifiers for numeric data types table for information about
      which format specifiers you can set depending on the data type of the numeric control
      and the format specifiers syntax elements table for descriptions of the syntax
       elements.

           If you want to format a string to display time, enclose the string with %<>T.

       This property is similar to the Format string option on the Display Format page of the
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

   MappingMapping ModeMode

       Scale mapping mode: 0-Linear, 1-Logarithmic.

       This property is similar to the Mapping item on the shortcut menu of a scale.

7742   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7742 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7743 ordinal=7743 -->
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

MarkerMarker

Reference to the scale marker.

You can use this reference with the Text properties.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

                                                    © National Instruments 7743

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7743 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7744 ordinal=7744 -->
## Property and Method Reference

Property and Method Reference


        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

   MarkerMarker ColorsColors

       Text color and background color of scale marker.

      You can set the color of the front panel object by wiring a hexadecimal number with
       the form RRGGBB or by wiring the color box constant to the property.

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

   MarkerMarker Colors:BGColors:BG ColorColor

      Background color of the scale marker.

      You can set the color of the front panel object by wiring a hexadecimal number with
       the form RRGGBB or by wiring the color box constant to the property.

       This property is an element of the Marker Colors property.

7744   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7744 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7745 ordinal=7745 -->
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

MarkerMarker Colors:TextColors:Text ColorColor

Color of the scale marker text.

You can set the color of the front panel object by wiring a hexadecimal number with
the form RRGGBB or by wiring the color box constant to the property.

This property is similar to the Marker text color option on the Scales page of the
Properties dialog box.

This property is an element of the Marker Colors property.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write


                                                    © National Instruments 7745

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7745 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7746 ordinal=7746 -->
## Property and Method Reference

Property and Method Reference


         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   RangeRange

      A scale is a component of many front panel objects in LabVIEW, such as the X and Y
       scales of graphs and charts. The scale consists of a range of values, specified as a
        cluster of (Minimum, Maximum, Increment, Minor Increment, and Start).

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


7746   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7746 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7747 ordinal=7747 -->
## Property and Method Reference

Property and Method Reference

Range:IncrementRange:Increment

Increment value of scale. Use this property to determine the distance between tick
marks.

This property is an element of the Range property.

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

Range:MaximumRange:Maximum

Maximum value of scale. Use this property to set the maximum value allowed in the
range.

This property is an element of the Range property.

This property is similar to the Maximum option on the Scales page of the Properties
dialog box.


                                                    © National Instruments 7747

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7747 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7748 ordinal=7748 -->
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

   Range:MinimumRange:Minimum

     Minimum value of scale. Use this property to set the minimum value allowed in the
       range.

       This property is an element of the Range property.

       This property is similar to the Minimum option on the Scales page of the Properties
       dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

7748   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7748 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7749 ordinal=7749 -->
## Property and Method Reference

Property and Method Reference


 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Range:MinorRange:Minor IncrementIncrement

Minor increment value of scale. Use this property to determine the distance between
minor tick marks.

This property is an element of the Range property.

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

Range:StartRange:Start

Start value of scale. Use this property to determine the value of the first tick marker
after the minimum.

                                                    © National Instruments 7749

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7749 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7750 ordinal=7750 -->
## Property and Method Reference

Property and Method Reference

       This property is an element of the Range property.

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

    StyleStyle

       Gets or sets the style of the marks on a scale. The values (0-8) for this property
      correspond with the options on the Style shortcut menu, available by right-clicking a
       scale on a graph or chart and selecting Style, from top-left (0) to bottom-right (8).

       This property is similar to the Style item on the shortcut menu of a scale.

      The following image shows the Style shortcut menu:


       Refer to the following table for a description of each value:


7750   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7750 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7751 ordinal=7751 -->
## Property and Method Reference

Property and Method Reference


 Value  Icon  Description

 0            Displays evenly-spaced, periodic values and marks for each of those values.

              Displays only the endpoint values and marks for endpoint values with no values or 1            marks in between.

 2            Displays evenly-spaced, periodic marks with no values.

 3            Displays evenly-spaced, periodic values with no marks.

 4            Displays only the endpoint values with no marks and no values or marks in between.

 5            Displays no values or marks.

              Displays evenly-spaced, periodic values and marks for each of those values as well as 6
              incremental marks in between values.

              Displays only the endpoint values and marks for endpoint values as well as 7
              incremental marks in between endpoint values.

              Displays evenly-spaced, periodic marks with no values as well as incremental marks 8
                in between.

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


                                                    © National Instruments 7751

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7751 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7752 ordinal=7752 -->
## Property and Method Reference

Property and Method Reference

    TickTick ColorsColors

       Gets or sets the tick color and minor tick color of the scale.

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

    TickTick Colors:MinorColors:Minor TickTick ColorColor

       Color of the minor tick mark.

      You can set the color of the front panel object by wiring a hexadecimal number with
       the form RRGGBB or by wiring the color box constant to the property.

       This property is similar to the Minor tick color option on the Scales page of the
       Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


7752   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7752 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7753 ordinal=7753 -->
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

TickTick Colors:TickColors:Tick ColorColor

Color of the tick mark.

You can set the color of the front panel object by wiring a hexadecimal number with
the form RRGGBB or by wiring the color box constant to the property.

This property is similar to the Major tick color option on the Scales page of the
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

                                                    © National Instruments 7753

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7753 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7754 ordinal=7754 -->
## Property and Method Reference

Property and Method Reference


        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   UniformUniform MarkerMarker Spacing?Spacing?

      Determines whether the markers are uniformly spaced.

       This property is similar to the Marker Spacing item on the shortcut menu of a scale.

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

      Shows the scale.

       This property is similar to the Show scale option on the Scales page of the Properties
       dialog box.


7754   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7754 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7755 ordinal=7755 -->
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

ColorScaleColorScale

ColorScale Properties
ColorScaleColorScale PropertiesProperties


 Property         Description

 High Color       Color for values greater than last array element.

 Interpolate
                   Interpolates between array colors.
 Color

 Low Color        Color for values less than first array element.

                   Array of (value, color) cluster pairs which specify the marker locations and
 Marker Values[]
                    colors.

 Ramp Visible    Shows color ramp.


                                                    © National Instruments 7755

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7755 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7756 ordinal=7756 -->
## Property and Method Reference

Property and Method Reference

   HighHigh ColorColor
   HighHigh ColorColor

       Color for values greater than last array element.

      You can set the color of the front panel object by wiring a hexadecimal number with
       the form RRGGBB or by wiring the color box constant to the property.

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

   InterpolateInterpolate ColorColor
    InterpolateInterpolate ColorColor

       Interpolates between array colors.

       This property is similar to the Interpolate Color item on the shortcut menu of a color
        scale.


7756   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7756 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7757 ordinal=7757 -->
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

LowLow ColorColor
LowLow ColorColor

Color for values less than first array element.

You can set the color of the front panel object by wiring a hexadecimal number with
the form RRGGBB or by wiring the color box constant to the property.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


                                                    © National Instruments 7757

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7757 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7758 ordinal=7758 -->
## Property and Method Reference

Property and Method Reference


         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   MarkerMarker Values[]Values[]
   MarkerMarker Values[]Values[]

       Array of (value, color) cluster pairs which specify the marker locations and colors.

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


7758   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7758 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7759 ordinal=7759 -->
## Property and Method Reference

Property and Method Reference

RampRamp VisibleVisible
RampRamp VisibleVisible

Shows color ramp.

This property is similar to the Visible Items»Ramp item on the shortcut menu of a
color scale.

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

RotaryColorScaleRotaryColorScale

RotaryColorScale Properties
RotaryColorScaleRotaryColorScale PropertiesProperties
RotaryColorScaleRotaryColorScale PropertiesProperties


                                                    © National Instruments 7759

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7759 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7760 ordinal=7760 -->
## Property and Method Reference

Property and Method Reference


        Property       Description

         Scale Position   Specifies the position of the rotary scale. This property is not writable for meters.

         Scale           Specifies the clockwise range, in radians, of the scale from the start position. This
         Position:Range  property is not writable for meters.

                          Specifies where the scale begins. The 3 o'clock position is 0, 12 o'clock position is         Scale
                             pi/2, 9 0'clock position is pi, 6 o'clock position is 3*pi/2, and so on. This property is          Position:Start                       not writable for meters.

   ScaleScale PositionPosition
    ScaleScale PositionPosition

       Specifies the position of the rotary scale. This property is not writable for meters.

     Elements

      Name  Description

                 Specifies where the scale begins. The 3 o'clock position is 0; the 12 o'clock position is pi/2;
          Start                the 9 o'clock position is pi; the 6 o'clock position is 3*pi/2, and so on.

        Range  Specifies the clockwise range, in radians, of the scale from the start position.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No


7760   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7760 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7761 ordinal=7761 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

ScaleScale Position:RangePosition:Range
ScaleScale Position:RangePosition:Range

Specifies the clockwise range, in radians, of the scale from the start position. This
property is not writable for meters.

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

ScaleScale Position:StartPosition:Start
ScaleScale Position:StartPosition:Start

Specifies where the scale begins. The 3 o'clock position is 0, 12 o'clock position is pi/2,

                                                    © National Instruments 7761

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7761 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7762 ordinal=7762 -->
## Property and Method Reference

Property and Method Reference

      9 0'clock position is pi, 6 o'clock position is 3*pi/2, and so on. This property is not
       writable for meters.

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

   GraphScaleGraphScale

      GraphScale Properties
   GraphScaleGraphScale PropertiesProperties


        Property            Description

                                              If TRUE, displays digital waveform data as individual data lines. If FALSE,
        Expand Digital
                              displays the data as a bus. This property is available only for digital waveform
        Buses
                             graphs.

         Grid Colors          Cluster of grid colors (major and minor) of a graph scale.

         Grid Colors:Major
                             Color of the major grid on the scale.
         Color

         Grid Colors:Minor    Color of the minor grid on the scale.

7762   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7762 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7763 ordinal=7763 -->
## Property and Method Reference

Property and Method Reference


 Property            Description

 Color

                                  If TRUE, LabVIEW rounds the end markers to a multiple of the increment used Loose Fit                        for the scale.

                     Array of user-defined marker values. LabVIEW ignores this array if it cannot Marker Values[]
                  draw numbers without overlapping.

 Name Label         Reference to the scale name label.

 Offset and           Cluster of offset(Xo) and multiplier(deltaX) for scaling values such that the
 Multiplier             final value equals (deltaX)*X + Xo.

 Offset and                        Multiplier, or interval, for scaling data using (deltaX)*X + Xo. Multiplier:Multiplier

 Offset and                        Offset, or initial value, for scaling data using (deltaX)*X + Xo.
 Multiplier:Offset

 Scale Fit               Fits the scale to data.

                    Reference to the unit label. You can use this reference with the Text Unit Label                      properties.

ExpandExpand DigitalDigital BusesBuses
ExpandExpand DigitalDigital BusesBuses

If TRUE, displays digital waveform data as individual data lines. If FALSE, displays the
data as a bus. This property is available only for digital waveform graphs.

This property applies only to the active X-scale or active Y-scale.

This property is similar to the Expand Digital Buses item on the shortcut menu of a
digital waveform scale.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 7763

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7763 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7764 ordinal=7764 -->
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

   GridGrid ColorsColors
    GridGrid ColorsColors

       Cluster of grid colors (major and minor) of a graph scale.

      You can set the color of the front panel object by wiring a hexadecimal number with
       the form RRGGBB or by wiring the color box constant to the property. This property
       applies only to the active X-scale or active Y-scale.

       This property is similar to the Grid Style and Colors option on the Scales page of the
       Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes


7764   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7764 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7765 ordinal=7765 -->
## Property and Method Reference

Property and Method Reference


 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

GridGrid Colors:MajorColors:Major ColorColor
GridGrid Colors:MajorColors:Major ColorColor

Color of the major grid on the scale.

You can set the color of the front panel object by wiring a hexadecimal number with
the form RRGGBB or by wiring the color box constant to the property. This property
applies only to the active X-scale or active Y-scale.

This property is an element of the Grid Colors property.

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


                                                    © National Instruments 7765

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7765 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7766 ordinal=7766 -->
## Property and Method Reference

Property and Method Reference

   GridGrid Colors:MinorColors:Minor ColorColor
    GridGrid Colors:MinorColors:Minor ColorColor

       Color of the minor grid on the scale.

      You can set the color of the front panel object by wiring a hexadecimal number with
       the form RRGGBB or by wiring the color box constant to the property. This property
       applies only to the active X-scale or active Y-scale.

       This property is an element of the Grid Colors property.

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

   LooseLoose FitFit
   LooseLoose FitFit

           If TRUE, LabVIEW rounds the end markers to a multiple of the increment used for the


7766   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7766 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7767 ordinal=7767 -->
## Property and Method Reference

Property and Method Reference

scale.

This property applies only to the active X-scale or active Y-scale.

This property is similar to the Loose Fit item on the shortcut menu of a graph or chart.

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

MarkerMarker Values[]Values[]
MarkerMarker Values[]Values[]

Array of user-defined marker values. LabVIEW ignores this array if it cannot draw
numbers without overlapping.

This property applies only to the active X-scale or active Y-scale.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 7767

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7767 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7768 ordinal=7768 -->
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

  NameName LabelLabel
   NameName LabelLabel

       Reference to the scale name label.

      You can use this reference with the Text properties. This property applies only to the
       active X-scale or active Y-scale.

       This property is similar to the Name option on the Scales page of the Properties dialog
       box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                                   Yes

         Settable when the VI is running                                  No

7768   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7768 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7769 ordinal=7769 -->
## Property and Method Reference

Property and Method Reference


 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

OffsetOffset andand MultiplierMultiplier
OffsetOffset andand MultiplierMultiplier

Cluster of offset(Xo) and multiplier(deltaX) for scaling values such that the final value
equals (deltaX)*X + Xo.

This property applies only to the active X-scale or active Y-scale.

This property is similar to the Offset and Multiplier options on the Scales page of the
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


                                                    © National Instruments 7769

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7769 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7770 ordinal=7770 -->
## Property and Method Reference

Property and Method Reference

    OffsetOffset andand Multiplier:MultiplierMultiplier:Multiplier
    OffsetOffset andand Multiplier:MultiplierMultiplier:Multiplier

        Multiplier, or interval, for scaling data using (deltaX)*X + Xo.

       This property applies only to the active X-scale or active Y-scale. This property is an
      element of the Offset and Multiplier property.

       This property is similar to the Multiplier option on the Scales page of the Properties
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

    OffsetOffset andand Multiplier:OffsetMultiplier:Offset
    OffsetOffset andand Multiplier:OffsetMultiplier:Offset

        Offset, or initial value, for scaling data using (deltaX)*X + Xo.


7770   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7770 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7771 ordinal=7771 -->
## Property and Method Reference

Property and Method Reference

If you change the offset, the scale no longer uses 0 as the origin of the plot. This
property applies only to the active X-scale or active Y-scale. This property is an element
of the Offset and Multiplier property.

This property is similar to the Offset option on the Scales page of the Properties dialog
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

ScaleScale FitFit
ScaleScale FitFit

Fits the scale to data.

This property applies only to the active X-scale or active Y-scale.

This property is similar to the AutoScale items on the shortcut menu of an x- or y-scale
and to the Autoscale checkbox on the Scales page of the Properties dialog box.


                                                    © National Instruments 7771

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7771 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7772 ordinal=7772 -->
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

   UnitUnit LabelLabel
    UnitUnit LabelLabel

       Reference to the unit label. You can use this reference with the Text properties.

       This property applies only to the active X-scale or active Y-scale.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                                   Yes

         Settable when the VI is running                                  No

7772   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7772 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7773 ordinal=7773 -->
## Property and Method Reference

Property and Method Reference


 Loads the front panel into memory                                         Yes

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Controls and Indicators\Numeric\Numeric
   with Units.vi
ColorGraphScaleColorGraphScale

ColorGraphScale Properties
ColorGraphScaleColorGraphScale PropertiesProperties


 Property              Description

 High Color            Color for values greater than last array element.

 Interpolate Color       Interpolates between array colors.

                                     If TRUE, LabVIEW rounds the end markers to a multiple of the increment Loose Fit
                     used for the scale.

 Low Color             Color for values less than first array element.

                        Array of (value, color) cluster pairs which specify the marker locations and
 Marker Values[]
                          colors.

 Name Label           Reference to the scale name label.

                         Cluster of offset(Xo) and multiplier(deltaX) for scaling values using
 Offset and Multiplier
                         (deltaX)*X + Xo.

 Offset and
                           Multiplier, or interval, for scaling data using (deltaX)*X + Xo.
 Multiplier:Multiplier


                                                    © National Instruments 7773

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7773 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7774 ordinal=7774 -->
## Property and Method Reference

Property and Method Reference


        Property              Description

         Offset and                                    Offset, or initial value, for scaling data using (deltaX)*X + Xo.          Multiplier:Offset

      Ramp Visible        Shows color ramp.

         Scale Fit                  Fits the scale to data.

                              Reference to the unit label of a front panel control. You can use this         Unit Label                                reference with the Text properties.

   HighHigh ColorColor
   HighHigh ColorColor

       Color for values greater than last array element.

      You can set the color of the front panel object by wiring a hexadecimal number with
       the form RRGGBB or by wiring the color box constant to the property.

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


7774   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7774 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7775 ordinal=7775 -->
## Property and Method Reference

Property and Method Reference

InterpolateInterpolate ColorColor
InterpolateInterpolate ColorColor

Interpolates between array colors.

This property is similar to the Interpolate Color item on the shortcut menu of an
intensity graph and to the Interpolate color option on the Scales page of the Intensity
Graph Properties dialog box.

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

LooseLoose FitFit
LooseLoose FitFit

If TRUE, LabVIEW rounds the end markers to a multiple of the increment used for the
scale.


                                                    © National Instruments 7775

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7775 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7776 ordinal=7776 -->
## Property and Method Reference

Property and Method Reference

       This property is similar to the Loose Fit item on the shortcut menu of an intensity
       graph.

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

   LowLow ColorColor
   LowLow ColorColor

       Color for values less than first array element.

      You can set the color of the front panel object by wiring a hexadecimal number with
       the form RRGGBB or by wiring the color box constant to the property.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write


7776   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7776 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7777 ordinal=7777 -->
## Property and Method Reference

Property and Method Reference


 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

MarkerMarker Values[]Values[]
MarkerMarker Values[]Values[]

Array of (value, color) cluster pairs which specify the marker locations and colors.

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


                                                    © National Instruments 7777

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7777 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7778 ordinal=7778 -->
## Property and Method Reference

Property and Method Reference

  NameName LabelLabel
   NameName LabelLabel

       Reference to the scale name label.

      You can use this reference with the Text properties.

       This property is similar to the Name option on the Scales page of the Intensity Graph
       Properties dialog box.

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

    OffsetOffset andand MultiplierMultiplier
    OffsetOffset andand MultiplierMultiplier

       Cluster of offset(Xo) and multiplier(deltaX) for scaling values using (deltaX)*X + Xo.


7778   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7778 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7779 ordinal=7779 -->
## Property and Method Reference

Property and Method Reference

This property is similar to the Offset and Multiplier options on the Scales page of the
Intensity Graph Properties dialog box.

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

OffsetOffset andand Multiplier:MultiplierMultiplier:Multiplier
OffsetOffset andand Multiplier:MultiplierMultiplier:Multiplier

Multiplier, or interval, for scaling data using (deltaX)*X + Xo.

This property is an element of the Offset and Multiplier property.

This property is similar to the Offset option on the Scales page of the Intensity Graph
Properties dialog box.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 7779

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7779 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7780 ordinal=7780 -->
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

    OffsetOffset andand Multiplier:OffsetMultiplier:Offset
    OffsetOffset andand Multiplier:OffsetMultiplier:Offset

        Offset, or initial value, for scaling data using (deltaX)*X + Xo.

           If you change the offset, the scale no longer uses 0 as the origin of the plot. This
       property is an element of the Offset and Multiplier property.

       This property is similar to the Offset option on the Scales page of the Intensity Graph
       Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

7780   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7780 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7781 ordinal=7781 -->
## Property and Method Reference

Property and Method Reference


 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

RampRamp VisibleVisible
RampRamp VisibleVisible

Shows color ramp.

This property is similar to the Visible Items»Ramp item on the shortcut menu of an
intensity graph and to the Show color ramp option on the Scales page of the Intensity
Graph Properties dialog box.

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


                                                    © National Instruments 7781

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7781 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7782 ordinal=7782 -->
## Property and Method Reference

Property and Method Reference

   ScaleScale FitFit
    ScaleScale FitFit

        Fits the scale to data.

       This property is similar to the AutoScale items on the shortcut menu of an x- or y-scale
      and to the Autoscale checkbox on the Scales page of the Properties dialog box.

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

   UnitUnit LabelLabel
    UnitUnit LabelLabel

       Reference to the unit label of a front panel control. You can use this reference with the
       Text properties.


7782   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7782 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7783 ordinal=7783 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

 Settable when the VI is running                                  No

 Loads the front panel into memory                                         Yes

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Controls and Indicators\Numeric\Numeric
   with Units.vi
SlideScaleSlideScale

SlideScale Properties
SlideScaleSlideScale PropertiesProperties


 Property                       Description

 Marker Values[]                  Array of arbitrary marker values.


                                                    © National Instruments 7783

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7783 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7784 ordinal=7784 -->
## Property and Method Reference

Property and Method Reference

   MarkerMarker Values[]Values[]
   MarkerMarker Values[]Values[]

       Array of arbitrary marker values.

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

    ControlControl

       Control Methods

       Control Properties

       Control Events
    ControlControl MethodsMethods


7784   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7784 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7785 ordinal=7785 -->
## Property and Method Reference

Property and Method Reference


Method          Description

                 National Instruments recommends using front panel data binding through the
                Shared Variable Engine or using the Bind To Network Path method to attach a
                 data connection to a control.Attach
DataSocket                  This method allows you to attach an opc, ftp, and http connection to a
                  control on Windows, and a dstp and file connection to a control on all
                LabVIEW-supported platforms. You can add new connections only at edit time.

Create:Control
                  Creates a control reference for the control and returns a reference to it.Reference

Create:Invoke                  Creates an Invoke Node for the control and returns a reference to it.Node

Create:Local                  Creates a local variable for the control and returns a reference to it.Variable

Create:Property                  Creates a Property Node for the control and returns a reference to it.
Node

Data                 Binds a control to an NI Publish-Subscribe Protocol (NI-PSP) network path. You
Binding:Bind To                can add new connections only at edit time.Network Path

Data                Unbinds a control from an NI Publish-Subscribe Protocol (NI-PSP) network path.Binding:Unbind

Data
Operations:Copy  Copies data from the control to the clipboard.
Data

Data
Operations:Paste  Pastes data from the clipboard to the control.
Data

Disconnect From  Disconnects the control from the type definition and returns TRUE. If the control
Typedef             is not connected to a type definition, LabVIEW returns FALSE.

Fit Control To     Resizes the control to the size of the pane that contains it and sets the control to
Pane              scale with the pane.

Get Image        Returns an image of a front panel object.

Get Terminal
                 Returns an image of the block diagram terminal of a front panel object.
Image

                                                    © National Instruments 7785

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7785 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7786 ordinal=7786 -->
## Property and Method Reference

Property and Method Reference


       Method          Description

          Reinitialize To                              Reinitializes the value of the control to the default value.         Default

       Remove        Removes an opc, ftp, and http connection from a control on Windows, and a
        DataSocket     dstp and file connection from a control on all LabVIEW-supported platforms.

          Start Drag         Starts a drag and drop operation using the specified control as the source.

        Update From     Updates the control from the type definition and returns TRUE. If the control is
        Typedef         not connected to a type definition, LabVIEW returns FALSE.

    AttachAttach DataSocketDataSocket

       National Instruments recommends using front panel data binding through the Shared
       Variable Engine or using the Bind To Network Path method to attach a data connection
       to a control.

       This method allows you to attach an opc, ftp, and http connection to a control on
      Windows, and a dstp and file connection to a control on all LabVIEW-supported
       platforms. You can add new connections only at edit time.

       This method is similar to the Data Binding Selection, Path, and Access Type options
      on the Data Binding page of the Properties dialog box.

           Note If you use this method with a Boolean control in a radio buttons
                control, this method returns an error.

     Parameters

                Data
      Name         Required  Description
                 type

       URL            Yes        Specifies the URL to establish a connection.


7786   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7786 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7787 ordinal=7787 -->
## Property and Method Reference

Property and Method Reference


         Data Name         Required  Description
         type

                            Specifies the mode of the connection. The connection mode can be No Mode          Yes                          DataSocket, Publish, Subscribe, or Publish & Subscribe.


 Enabled        Yes        Specifies if a connection is enabled.


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

Create:ControlCreate:Control ReferenceReference

Creates a control reference for the control and returns a reference to it.

Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                         No

                                                    © National Instruments 7787

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7787 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7788 ordinal=7788 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                                 No

         Settable when the VI is running                                        No

        Loads the front panel into memory                                     No

       Need to authenticate before use                                       No

        Loads the block diagram into memory                                              Yes

       Remote access allowed                                                           Yes

    Create:InvokeCreate:Invoke NodeNode

       Creates an Invoke Node for the control and returns a reference to it.

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

    Create:LocalCreate:Local VariableVariable

       Creates a local variable for the control and returns a reference to it.

     Remarks

      The following table lists the characteristics of this method.

7788   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7788 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7789 ordinal=7789 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Available in Run-Time Engine                                         No

 Available in Real-Time Operating System                                 No

 Settable when the VI is running                                        No

 Loads the front panel into memory                                     No

 Need to authenticate before use                                       No

 Loads the block diagram into memory                                              Yes

 Remote access allowed                                                           Yes

Create:PropertyCreate:Property NodeNode

Creates a Property Node for the control and returns a reference to it.

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

DataData Binding:BindBinding:Bind ToTo NetworkNetwork PathPath

Binds a control to an NI Publish-Subscribe Protocol (NI-PSP) network path. You can
add new connections only at edit time.

                                                    © National Instruments 7789

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7789 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7790 ordinal=7790 -->
## Property and Method Reference

Property and Method Reference

       This method is similar to the Data Binding Selection and Access Type options on the
      Data Binding page of the Properties dialog box.

     Parameters

              Data      Name           Required  Description               type

       URL             Yes        String where you specify the URL to establish a connection.


                            Mode of the connection. Options are: No PSP, Read, Write, or Write &       Mode            Yes
                                   Read.


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

   DataData Binding:UnbindBinding:Unbind

      Unbinds a control from an NI Publish-Subscribe Protocol (NI-PSP) network path.


7790   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7790 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7791 ordinal=7791 -->
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

DataData Operations:CopyOperations:Copy DataData

Copies data from the control to the clipboard.

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


                                                    © National Instruments 7791

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7791 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7792 ordinal=7792 -->
## Property and Method Reference

Property and Method Reference

   DataData Operations:PasteOperations:Paste DataData

       Pastes data from the clipboard to the control.

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

   DisconnectDisconnect FromFrom TypedefTypedef

       Disconnects the control from the type definition and returns TRUE. If the control is not
      connected to a type definition, LabVIEW returns FALSE.

     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                         No

         Available in Real-Time Operating System                                 No

         Settable when the VI is running                                        No

        Loads the front panel into memory                                     No

7792   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7792 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7793 ordinal=7793 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                                       No

 Loads the block diagram into memory                                   No

 Remote access allowed                                                           Yes

FitFit ControlControl ToTo PanePane

Resizes the control to the size of the pane that contains it and sets the control to scale
with the pane.

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

GetGet ImageImage

Returns an image of a front panel object.

This method is similar to the Front Panel:Get Image method.

If a front panel is not visible, LabVIEW does not update the values in the objects on the
front panel. If you call a VI whose front panel is not visible and you use the Get Image
method to create an image of a front panel object, the image does not reflect any value
changes that occurred when you ran the VI.

                                                    © National Instruments 7793

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7793 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7794 ordinal=7794 -->
## Property and Method Reference

Property and Method Reference

           If you want the image to reflect value changes, make sure the front panel is open
       before any values change. If you do not want to display the front panel but want the
      image to reflect value changes, create a Property Node from any terminal on the block
      diagram of the VI for which you want to create a front panel control image.

      You also can use the Append Control Image to Report VI to create an image of a front
       panel object and append it to a report.

     Parameters

                    Data      Name            Required  Description
                    type

                                        Indicates the color depth, or number of supported colors, of the        Image                     No       image: 1 (1-bit, black and white), 4 (4-bit, 16 colors), 8 (8-bit, 256        Depth
                                            colors), or 24 (24-bit, true color). The default is 8.


        Background                     No        Specifies the background color of the image.         Color

                                     Information about the image so you can use the Draw Flattened
                                Pixmap VI to draw it as a picture or use the Graphics Formats VIs to
                                    save the image to a file. This cluster is similar to the image data
                                    output of the Read JPEG File, Read PNG File, and Read BMP File VIs.

                                                           • image type—Reserved for future use.
                                                           • image depth—Specifies the color depth of the image, which is
                                         the number of bits to use to describe the color of each pixel in
                                         the image. Valid values include 1, 4, 8, and 24 bits per pixel.
                                    image depth affects how LabVIEW interprets the values of        Image Data      No
                                    image and colors.
                                                           • image—Array of bytes that describes the color of each pixel in
                                         the image in raster order. The value of image depth determines
                               how LabVIEW interprets the value of this output.

                                                                    If image depth is 24, each pixel has three bytes to describe its
                                                 color. The first byte for each pixel describes the red value, the
                                      second byte describes the green value, and the third byte
                                          describes the blue value.


7794   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7794 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7795 ordinal=7795 -->
## Property and Method Reference

Property and Method Reference


            Data Name            Required  Description
             type

                                                       If image depth is 8, each pixel has one byte to describe its
                                        color. The value of each bit corresponds to an element in
                                     colors, which stores 32-bit RGB values where the most-
                                       significant byte is zero, followed in order by red, green, and
                                 blue values.

                                                       If image depth is 4, the behavior is similar to when image
                              depth is 8 except valid values in image include 0 through 15.

                                                       If image depth is 1, any value of zero in image corresponds to
                               element 0 in colors. All other values correspond to element 1 in
                                     colors.

                             The size of the array might be larger than expected due to
                                 padding.
                                               • mask—Array of bytes in which each bit describes mask
                                  information for a pixel. The first byte describes the first eight
                                        pixels, the second byte describes the next eight pixels, and so
                                  on. If a bit is zero, LabVIEW draws the corresponding pixel as
                                    transparent. If the array is empty, LabVIEW draws all pixels
                                 without transparency. If the array does not contain a bit for
                               each pixel in the image, LabVIEW draws any pixels missing from
                                 the array without transparency.
                                               • colors—Array of RGB color values that correspond to the values
                                      in image. The value of image depth determines how LabVIEW
                                     interprets the value of this output. If image depth is 24,
                              LabVIEW ignores this output. If image depth is 8, the array has
                               256 elements. If image depth is 4, the array has 16 elements. If
                             image depth is 1, the array has 2 elements.
                                               • Rectangle—Cluster that contains coordinates that describe the
                              bounding rectangle of the image, where the upper-left corner is
                                     at (0,0). The bottom right edges of the bounds does not include
                                 the image.


Remarks

The following table lists the characteristics of this method.


                                                    © National Instruments 7795

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7795 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7796 ordinal=7796 -->
## Property and Method Reference

Property and Method Reference


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                                      Yes

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

   GetGet TerminalTerminal ImageImage

       Returns an image of the block diagram terminal of a front panel object.

     Parameters

                    Data      Name            Required  Description
                    type

                                      Sets the color depth, or number of supported colors, of the image: 1
        Image                     No          (1-bit, black and white), 4 (4-bit, 16 colors), 8 (8-bit, 256 colors), or        Depth                                  24 (24-bit, true color). The default is 8.


        Background
                     No        Specifies the background color of the image.
         Color

                                     Information about the image so you can use the Draw Flattened
                                Pixmap VI to draw it as a picture or use the Graphics Formats VIs to
                                    save the image to a file. This cluster is similar to the image data
                                    output of the Read JPEG File, Read PNG File, and Read BMP File VIs.
        Image Data      No                                                           • image type—Reserved for future use.
                                                           • image depth—Specifies the color depth of the image, which is
                                         the number of bits to use to describe the color of each pixel in
                                         the image. Valid values include 1, 4, 8, and 24 bits per pixel.


7796   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7796 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7797 ordinal=7797 -->
## Property and Method Reference

Property and Method Reference


            DataName            Required  Description
            type

                            image depth affects how LabVIEW interprets the values of
                            image and colors.
                                              • image—Array of bytes that describes the color of each pixel in
                                the image in raster order. The value of image depth determines
                         how LabVIEW interprets the value of this output.

                                                      If image depth is 24, each pixel has three bytes to describe its
                                       color. The first byte for each pixel describes the red value, the
                              second byte describes the green value, and the third byte
                                  describes the blue value.

                                                      If image depth is 8, each pixel has one byte to describe its
                                       color. The value of each bit corresponds to an element in
                                     colors, which stores 32-bit RGB values where the most-
                                      significant byte is zero, followed in order by red, green, and
                                blue values.

                                                      If image depth is 4, the behavior is similar to when image
                             depth is 8 except valid values in image include 0 through 15.

                                                      If image depth is 1, any value of zero in image corresponds to
                              element 0 in colors. All other values correspond to element 1 in
                                     colors.

                            The size of the array might be larger than expected due to
                                padding.
                                              • mask—Array of bytes in which each bit describes mask
                                 information for a pixel. The first byte describes the first eight
                                       pixels, the second byte describes the next eight pixels, and so
                                 on. If a bit is zero, LabVIEW draws the corresponding pixel as
                                   transparent. If the array is empty, LabVIEW draws all pixels
                                without transparency. If the array does not contain a bit for
                              each pixel in the image, LabVIEW draws any pixels missing from
                                the array without transparency.
                                              • colors—Array of RGB color values that correspond to the values
                                      in image. The value of image depth determines how LabVIEW
                                    interprets the value of this output. If image depth is 24,
                             LabVIEW ignores this output. If image depth is 8, the array has
                              256 elements. If image depth is 4, the array has 16 elements. If


                                                    © National Instruments 7797

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7797 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7798 ordinal=7798 -->
## Property and Method Reference

Property and Method Reference


                    Data      Name            Required  Description
                    type

                                    image depth is 1, the array has 2 elements.
                                                           • Rectangle—Cluster that contains coordinates that describe the
                                     bounding rectangle of the image, where the upper-left corner is
                                             at (0,0). The bottom right edges of the bounds does not include
                                         the image.


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

    ReinitializeReinitialize ToTo DefaultDefault

        Reinitializes the value of the control to the default value.

       This method is similar to the Data Operations»Reinitialize to Default Value item on
       the shortcut menu of a control.

           Note If you use this method with a Boolean control in a radio buttons
                control, this method returns an error.


7798   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7798 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7799 ordinal=7799 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                             Yes

 Settable when the VI is running                                      Yes

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

RemoveRemove DataSocketDataSocket

Removes an opc, ftp, and http connection from a control on Windows, and a dstp
and file connection from a control on all LabVIEW-supported platforms.

This method is similar to the Unbound option of the Data Binding Selection pull-down
menu on the Data Binding page of the Properties dialog box.

      Note If you use this method with a Boolean control in a radio buttons
        control, this method returns an error.

Use the Data Binding:Unbind method to remove psp connections.

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

                                                    © National Instruments 7799

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7799 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7800 ordinal=7800 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

    StartStart DragDrag

        Starts a drag and drop operation using the specified control as the source.

      You can use this method to start drag and drop operations in response to user-defined
       actions instead of the built-in behavior with string, tree, listbox, and multicolumn
        listbox controls. For controls other than the string, tree, listbox, and multicolumn
        listbox, the Start Drag method is the only way to start a drag using this control as a
      drag source.

      You must specify what data to provide during the drag and drop operation. Optionally,
      you can specify the drag mode, and corresponding default cursor feedback, to reflect
      whether this drag and drop operation supports moving the data instead of only
       copying it. During a drag and drop operation, only drag and drop events are available.
      Mouse events are not available.

           If there is already a drag in progress, LabVIEW returns an error. If you pass an empty
       array for the data parameter, the drag operation does not start and LabVIEW returns an
        error. If the array of data passed contains duplicate data names or data that conflicts
       with built-in types, LabVIEW returns an error.

        After you use this method, LabVIEW remains in the middle of a drag and drop
       operation until the user cancels the drag by pressing the <Esc> key or lifting the mouse
       button, or until a window opens in front of the window that has the source control.

      The Drag Data parameter is an array of clusters, each cluster containing a label and
       corresponding data. Each label must be unique and cannot use the LV_ prefix. Each
      element of the array must be of the same data type. The Drag Mode parameter

7800   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7800 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7801 ordinal=7801 -->
## Property and Method Reference

Property and Method Reference

specifies the operation of the drag, such as copy, move, or copy and move. If you select
copy or move, pressing the <Ctrl> key copies the item.

Parameters

       Data Name       Required  Description       type

                          Indicates the LabVIEW or user-defined name that identifies the data type.
                     You cannot use the prefix LV_ on a user-defined data name, because it is
                        reserved for LabVIEW data types. You can use the following built-in
                     LabVIEW data types and names:

                     LabVIEW Data Type     Definition

                   LV_TEXT               String

                   LV_TREE_TAG         String

                                                 Array of a cluster containing an array of strings,
                                           from left to right, in the item you are dragging,
                                         an integer representing the glyph index
                   LV_TREE_ITEMS      associated with the item from which you are
 Drag                                          dragging data, and an integer representing the              Yes Data                                          indent level of the item from which you are
                                                 dragging.

                                                   Cluster containing an array of strings from the
                                        row that you are dragging data and an integer
                   LV_LISTBOX                                                representing the glyph index associated with
                                               the row from which you are dragging data.

                                                 Array of a cluster containing an array of strings,
                                           from left to right, in the item you are dragging
                   LV_LISTBOX_ITEMS and an integer representing the glyph index
                                                associated with the item from which you are
                                               dragging data.

                   LV_PATH             Path


 Drag                     Specifies the operations that this control supports during the drag, such
          No
 Mode                  as copy or move, copy only, move only. If you select copy or move,


                                                    © National Instruments 7801

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7801 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7802 ordinal=7802 -->
## Property and Method Reference

Property and Method Reference


              Data      Name       Required  Description
               type

                                 pressing the <Ctrl> key copies the item. The operations you support
                                  control the values that the Results output of the Drag Ended and Drag
                              Source Update events can provide.

                                For filter events, you can modify this field to change the drag mode when
                                     this event is generated.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                      No

         Settable when the VI is running                                      Yes

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Structures\Event Structure\Drag and Drop
        - Initiating a Custom Drag.vi
   UpdateUpdate FromFrom TypedefTypedef

      Updates the control from the type definition and returns TRUE. If the control is not


7802   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7802 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7803 ordinal=7803 -->
## Property and Method Reference

Property and Method Reference

connected to a type definition, LabVIEW returns FALSE.

In most cases, LabVIEW correctly preserves the default values of each instance when
updating from the type definition. However, if LabVIEW is unable to map the previous
default values to the updated controls or constants when updating instances, LabVIEW
may lose or incorrectly preserve the default values of instances LabVIEW updates
programmatically. Avoid updating type definition instances programmatically if the
instances have custom default values and you plan to make extensive changes to the
type definition.

      Note After the update, obtain a new reference to the control because the
       update might have changed type of the control.

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

ControlControl PropertiesProperties


 Property            Description

 Auto-Update From
                                  If TRUE, the control automatically updates when the type definition changes.
 Typedef

 Blinking                     If TRUE, the control blinks.

                                                    © National Instruments 7803

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7803 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7804 ordinal=7804 -->
## Property and Method Reference

Property and Method Reference


        Property            Description

          Built-In Mouse       Sets the conditions under which the control responds to mouse wheel
        Wheel Support      movement.

                            Reference to the caption object. You can use this reference with the Text        Caption                               properties.

                            Gets the index of the control or indicator you specify. If the control or
         Control Index        indicator for which you want to get the index does not have a terminal on the
                            block diagram, this property returns an error.

         Control Reference                            Returns references to the control reference nodes of this control.
        Nodes[]

        Data
         Binding:Binding     Returns the type of binding.
        Type

        Data Binding:LED                        Shows or hides the data binding indicator.
          Visible

        Data Binding:Mode   Gets or sets the mode of the data connection.

                          Reads or writes the NI Publish-Subscribe Protocol (NI-PSP) URL to which the
        Data Binding:Path    control is connected. To write this property, you must bind the control to the
                        PSP URL before you begin writing.

                            Returns the status of the data connection. The connection status can be
        Data Binding:Status  Invalid Status, Unconnected, Active, Idle, Error, or
                       Connecting.

                              This is the enabled state of the opc, ftp, and http connection on Windows,
        DataSocket:Enabled and the dstp and file connection on all LabVIEW-supported platforms. A
                            connection can transfer data only when enabled.

        DataSocket:LED
                        Shows or hides the connection status indicator.
          Visible

        DataSocket:Mode    Gets or sets the mode of the data connection.

                            Returns the status of the data connection. The connection status can be
         DataSocket:Status   Invalid Status, Unconnected, Active, Idle, Error, or
                       Connecting.

                            Gets or sets the URL to which the control is connected. Valid URLs for using
                            the DataSocket properties to connect controls are the opc, ftp, and http
        DataSocket:URL
                              protocols on Windows, and the dstp and file protocols on all LabVIEW-
                           supported platforms.


7804   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7804 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7805 ordinal=7805 -->
## Property and Method Reference

Property and Method Reference


Property            Description

Default Value        Default value of the control (LabVIEW variant).

Default Value        Default value of the control.

                     Default value of the control (LabVIEW variant).
Default Value
(Undoable)          This property behaves identically to writing the Default Value property except
                     that LabVIEW records changes to this property if a transaction starts on the VI.

                     Description of the front panel object that appears in the Context Help
Description        window when you move the cursor over the object and in VI documentation
                  you generate.

Disabled             Indicates whether you can operate the control.

Focus Key Binding   Sets a shortcut key to navigate to this control.

Grow Info           Returns the growing abilities for this control.

Grow Info:Can Grow
                    Returns if this control can grow horizontally.Horizontally

Grow Info:Can Grow
                    Returns if this control can grow vertically.Vertically

Grow Info:Max
                    Returns the maximum size horizontally this control can grow.Horizontally

Grow Info:Max                    Returns the maximum size vertically this control can grow.Vertically

Grow Info:Min                    Returns the minimum size horizontally this control can grow.
Horizontally

Grow Info:Min
                    Returns the minimum size vertically this control can grow.
Vertically

Has Caption         Returns TRUE if the control has a caption.

Indicator                   If TRUE, the front panel object is an indicator. If FALSE, the object is a control.

Invoke Nodes[]      Returns references to the invoke nodes of this control.

Is On Connector
                    Returns whether a control or indicator is on the connector pane of a VI.
Pane

Is Typedef?          Returns whether the control is linked to the type definition.


                                                    © National Instruments 7805

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7805 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7806 ordinal=7806 -->
## Property and Method Reference

Property and Method Reference


        Property            Description

                                               If TRUE, the control has key focus and receives the keys pressed on the        Key Focus                            keyboard.

         Label               Reference to the label object.

         Local Variables[]     Returns references to the local variables of this control.

       Owning Pane        Returns a reference to the pane that owns the referenced control.

         Property Nodes[]    Returns references to the property nodes of this control.

         Skip When Tabbing    If TRUE, LabVIEW skips this control when you tab through the front panel.

         Style ID             Returns a numeric identifier for the style of the control.

                      When TRUE, enables synchronous display that shows every update to a data
        Synchronous        value in a control or indicator. When FALSE, asynchronous display permits
         Display             the execution system to reduce updates to a slower rate and spend more
                           time executing VIs.

                            Returns the reference to the block diagram terminal of this control. Use this        Terminal
                             property to navigate between the front panel and the block diagram of a VI.

                              Sets or returns the tip strip of a control. A tip strip is the brief description of
                            the object that appears when you move the cursor over the object.         Tip Strip
                           Other products refer to tip strips as tooltips.

                            Returns the path to the type definition if the control is linked to a type         Typedef:Path                                 definition. Otherwise, LabVIEW returns an empty path.

                            Returns a reference to the type definition if the control is connected to a type
         Typedef:VI                                 definition. Otherwise, LabVIEW returns <NotARef>.

                           Data value of the control (LV variant). If this is a Boolean value configured
                            with a latching mechanical action, this property always returns an error. Due
         Value                to race conditions that can occur when you have a Boolean value with
                               latching mechanical action, you cannot programmatically read Boolean
                             values that are set with a latching mechanical action.

                           Data value of this control. If this is a Boolean value configured with a latching
                           mechanical action, this property always returns an error. Due to race
         Value                conditions that can occur when you have a Boolean value with latching
                           mechanical action, you cannot programmatically read Boolean values that
                             are set with a latching mechanical action.


7806   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7806 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7807 ordinal=7807 -->
## Property and Method Reference

Property and Method Reference


 Property            Description

 Value (Signaling)     Sets the value of the control (LV variant) and generates a Value Change event.

 Value (Signaling)     Sets the value of the control and generates a Value Change event.

                    Data value of the control (LabVIEW variant).

                      This property behaves identically to writing the Value property except that
 Value (Undoable)                  LabVIEW records changes to this property if a transaction starts on the VI. For
                   a Boolean value configured with a latching mechanical action, this property
                    always returns an error.

 Visible               Displays the front panel control.

 XControl:Container                     Sets or gets the container bounds of the XControl. Bounds

 XControl:Container                    Height of the XControl. Bounds:Height

 XControl:Container                   Width of the XControl. Bounds:Width

 XControl:Is                     Returns TRUE if the control is an XControl, FALSE otherwise. XControl?

Auto-UpdateAuto-Update FromFrom TypedefTypedef

If TRUE, the control automatically updates when the type definition changes.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


                                                    © National Instruments 7807

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7807 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7808 ordinal=7808 -->
## Property and Method Reference

Property and Method Reference


         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    BlinkingBlinking

           If TRUE, the control blinks.

      Keep in mind the following caveats when using this property:

            •  If you set this property to TRUE for system controls, the controls might not blink
            correctly. System controls are designed specifically for use in dialog boxes and are
          not designed to blink because standard dialog boxes usually do not contain
           blinking controls.
            • You cannot use this property with XControls or controls on a subpanel.
            • Do notuse this property with elements in an array. This property works on only
         one element in the array, not the entire array. Use a cluster instead of an array to
        make all the elements blink.

       This property is similar to the Blink Foreground and Blink Background options on the
      Environment page of the Options dialog box, and to the Blink delay for front panel
       controls (milliseconds) option on the Front Panel page of the Options dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes


7808   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7808 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7809 ordinal=7809 -->
## Property and Method Reference

Property and Method Reference


 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Built-InBuilt-In MouseMouse WheelWheel SupportSupport

Sets the conditions under which the control responds to mouse wheel movement.

For example, you can specify whether a control responds when you either hover over
the control or the control has key focus. This property is similar to the Built-In Mouse
Wheel Support option on the Key Navigation page of the Properties dialog box.

      Note You can use the key focus functionality only on Windows operating
       systems.

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

 Remote access allowed                                                  Yes


                                                    © National Instruments 7809

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7809 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7810 ordinal=7810 -->
## Property and Method Reference

Property and Method Reference

   CaptionCaption

       Reference to the caption object. You can use this reference with the Text properties.

           Note You first must create the caption before you use this property, or
            LabVIEW returns an error. LabVIEW creates the caption the first time you set
              the caption to visible.

       This property is similar to the Visible Items»Caption option on the shortcut menu of
       front panel controls and the Caption Visible and Caption Text item on the Appearance
      page of the Properties dialog box.

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

    ControlControl IndexIndex

       Gets the index of the control or indicator you specify. If the control or indicator for
      which you want to get the index does not have a terminal on the block diagram, this
       property returns an error.


7810   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7810 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7811 ordinal=7811 -->
## Property and Method Reference

Property and Method Reference

You can use this property to specify the controls for which you get or set values with
the Get Control Values by Index or Set Control Values by Index functions.

(Real-Time Module) Use the Get Control Index by Name method instead of the Control
Index property to get control indexes. You can use the Control Index property on
LabVIEW Real-Time systems only while connected to the RT target from the LabVIEW
project. As a result, this property can work in the development environment but does
not work in RT built applications.

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

ControlControl ReferenceReference Nodes[]Nodes[]

Returns references to the control reference nodes of this control.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

                                                    © National Instruments 7811

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7811 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7812 ordinal=7812 -->
## Property and Method Reference

Property and Method Reference


         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                                         Yes

       Need to authenticate before use                                 No

        Loads the block diagram into memory                                      Yes

       Remote access allowed                                                   Yes

   DataData Binding:BindingBinding:Binding TypeType

       Returns the type of binding.

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

   DataData Binding:LEDBinding:LED VisibleVisible

      Shows or hides the data binding indicator.


7812   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7812 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7813 ordinal=7813 -->
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

DataData Binding:ModeBinding:Mode

Gets or sets the mode of the data connection.

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


                                                    © National Instruments 7813

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7813 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7814 ordinal=7814 -->
## Property and Method Reference

Property and Method Reference


       Remote access allowed                                                  Yes

   DataData Binding:PathBinding:Path

      Reads or writes the NI Publish-Subscribe Protocol (NI-PSP) URL to which the control is
       connected. To write this property, you must bind the control to the PSP URL before you
       begin writing.

           Note If the control is bound to a project item instead of a PSP URL and you
              attempt to write this property, this property returns an error.

      To bind the control to a PSP URL, use the Bind to Network Path method while the VI is
       not running.

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

   DataData Binding:StatusBinding:Status

       Returns the status of the data connection. The connection status can be Invalid

7814   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7814 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7815 ordinal=7815 -->
## Property and Method Reference

Property and Method Reference

Status, Unconnected, Active, Idle, Error, or Connecting.

Elements

 Name  Description

       The connection status. Valid values are Invalid Status, Unconnected, Active,
 Code
       Idle, Error, or Connecting.

 Text   Displays a message describing the current status.

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

DataSocket:EnabledDataSocket:Enabled

This is the enabled state of the opc, ftp, and http connection on Windows, and the
dstp and file connection on all LabVIEW-supported platforms. A connection can
transfer data only when enabled.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 7815

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7815 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7816 ordinal=7816 -->
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

   DataSocket:LEDDataSocket:LED VisibleVisible

      Shows or hides the connection status indicator.

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


7816   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7816 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7817 ordinal=7817 -->
## Property and Method Reference

Property and Method Reference

DataSocket:ModeDataSocket:Mode

Gets or sets the mode of the data connection.

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

DataSocket:StatusDataSocket:Status

Returns the status of the data connection. The connection status can be Invalid
Status, Unconnected, Active, Idle, Error, or Connecting.

Elements

 Name  Description

       The connection status. Valid values are Invalid Status, Unconnected, Active,
 Code
       Idle, Error, or Connecting.

 Text   Displays a message describing the current status.


                                                    © National Instruments 7817

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7817 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7818 ordinal=7818 -->
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

   DataSocket:URLDataSocket:URL

       Gets or sets the URL to which the control is connected. Valid URLs for using the
      DataSocket properties to connect controls are the opc, ftp, and http protocols on
      Windows, and the dstp and file protocols on all LabVIEW-supported platforms.

      To set the URL, use the Attach DataSocket and Remove DataSocket methods when the
        VI is not running. Use front panel data bindings to bind controls to shared variables or
       to NI Publish-Subscribe Protocol (NI-PSP) data items.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

7818   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7818 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7819 ordinal=7819 -->
## Property and Method Reference

Property and Method Reference


 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

DefaultDefault ValueValue

Default value of the control (LabVIEW variant).

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read/Write

 Available in Run-Time Engine                                        Yes (Read Only)

 Available in Real-Time Operating System                             Yes

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

DefaultDefault ValueValue

Default value of the control.

Remarks

The following table lists the characteristics of this property.

                                                    © National Instruments 7819

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7819 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7820 ordinal=7820 -->
## Property and Method Reference

Property and Method Reference


        Data type                                                  Dynamic

         Permissions                                                     Read/Write

         Available in Run-Time Engine                                        Yes (Read Only)

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

    DefaultDefault ValueValue (Undoable)(Undoable)

       Default value of the control (LabVIEW variant).

       This property behaves identically to writing the Default Value property except that
      LabVIEW records changes to this property if a transaction starts on the VI.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                               Write Only

         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                 No

        Loads the front panel into memory                               No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                   Yes


7820   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7820 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7821 ordinal=7821 -->
## Property and Method Reference

Property and Method Reference

DescriptionDescription

Description of the front panel object that appears in the Context Help window when
you move the cursor over the object and in VI documentation you generate.

You can format the text in the description to appear bold in the Context Help window.

If you want to display a carriage return in the Context Help window, you must separate
paragraphs with two carriage returns

This property is similar to the VI description text box on the Documentation page of
the VI Properties dialog box.

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

DisabledDisabled

Indicates whether you can operate the control.

This property is similar to Advanced»Enabled State item on the shortcut menu of a
front panel control or indicator and to the Enabled State option on the Appearance

                                                    © National Instruments 7821

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7821 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7822 ordinal=7822 -->
## Property and Method Reference

Property and Method Reference

      page of the Properties dialog box.

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

   FocusFocus KeyKey BindingBinding

       Sets a shortcut key to navigate to this control.

       This property is similar to the Focus option on the Key Navigation page of the
       Properties dialog box.

     Elements

      Name   Description

         Control  If TRUE, the keyboard shortcut includes the <Ctrl> key.

          Shift       If TRUE, the keyboard shortcut includes the <Shift> key.

               The name of the shortcut key. (macOS) LabVIEW does not support <VolumeUp>,
        Key    <VolumeDown>, and function keys <F15> to <F24> as shortcut keys on macOS. Key must
               match one of the following values:


7822   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7822 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7823 ordinal=7823 -->
## Property and Method Reference

Property and Method Reference


Name   Description

                • <
             Clear
           >
                • <
              Ins
           >
                • <
             Del
           >
                • <
         Home
           >
                • <
          End
           >
                • <
           PageUp
           >
                • <
          PageDown
           >
                • <
            Escape
           >
                • <
             Enter
           >

                Note The <Enter> key on the alphanumeric keyboard and <Enter> key on
                     the numeric keypad are the same value.

                • <
             Play
           >
                • <
          VolumeUp
           >
                • <
          VolumeDown
           >


                                                    © National Instruments 7823

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7823 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7824 ordinal=7824 -->
## Property and Method Reference

Property and Method Reference


      Name   Description

                            • <
                  Mute
                   >
                            • F1
                            • F2
                            • F3
                            • F4
                            • F5
                            • F6
                            • F7
                            • F8
                            • F9
                            • F10
                            • F11
                            • F12
                            • F13
                            • F14
                            • F15
                            • F16
                            • F17
                            • F18
                            • F19
                            • F20
                            • F21
                            • F22
                            • F23
                            • F24

                   Note You must use the English Key name when wiring a shortcut key value.


     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write


7824   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7824 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7825 ordinal=7825 -->
## Property and Method Reference

Property and Method Reference


 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

GrowGrow InfoInfo

Returns the growing abilities for this control.

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

GrowGrow Info:CanInfo:Can GrowGrow HorizontallyHorizontally

Returns if this control can grow horizontally.


                                                    © National Instruments 7825

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7825 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7826 ordinal=7826 -->
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

   GrowGrow Info:CanInfo:Can GrowGrow VerticallyVertically

       Returns if this control can grow vertically.

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


7826   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7826 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7827 ordinal=7827 -->
## Property and Method Reference

Property and Method Reference


 Remote access allowed                                                   Yes

GrowGrow Info:MaxInfo:Max HorizontallyHorizontally

Returns the maximum size horizontally this control can grow.

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

GrowGrow Info:MaxInfo:Max VerticallyVertically

Returns the maximum size vertically this control can grow.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

                                                    © National Instruments 7827

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7827 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7828 ordinal=7828 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                                   Yes

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

   GrowGrow Info:MinInfo:Min HorizontallyHorizontally

       Returns the minimum size horizontally this control can grow.

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

   GrowGrow Info:MinInfo:Min VerticallyVertically

       Returns the minimum size vertically this control can grow.


7828   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7828 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7829 ordinal=7829 -->
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

HasHas CaptionCaption

Returns TRUE if the control has a caption.

A control has a caption after you complete one of the following actions:

  • Display the caption by right-clicking the control and selecting Visible»Caption
   from the shortcut menu.
  • Programmatically get or set the caption text by using the Text property of the
    control.

      Note LabVIEW continues to store the caption for the control even if you hide
       the caption or use the text editor tool to delete the text of the caption. This
       behavior enables LabVIEW to display the caption if you choose to make it
         visible again. Therefore, this property continues to return TRUE for hidden
        captions.


                                                    © National Instruments 7829

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7829 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7830 ordinal=7830 -->
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

    IndicatorIndicator

           If TRUE, the front panel object is an indicator. If FALSE, the object is a control.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read/Write

         Available in Run-Time Engine                                        Yes (Read Only)

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No


7830   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7830 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7831 ordinal=7831 -->
## Property and Method Reference

Property and Method Reference


 Remote access allowed                                             Yes

InvokeInvoke Nodes[]Nodes[]

Returns references to the invoke nodes of this control.

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

IsIs OnOn ConnectorConnector PanePane

Returns whether a control or indicator is on the connector pane of a VI.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

                                                    © National Instruments 7831

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7831 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7832 ordinal=7832 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                                   Yes

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

     IsIs Typedef?Typedef?

       Returns whether the control is linked to the type definition.

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

   KeyKey FocusFocus

           If TRUE, the control has key focus and receives the keys pressed on the keyboard.


7832   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7832 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7833 ordinal=7833 -->
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

LabelLabel

Reference to the label object.

You can use this reference with the Text properties.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

 Settable when the VI is running                                  No

 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

                                                    © National Instruments 7833

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7833 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7834 ordinal=7834 -->
## Property and Method Reference

Property and Method Reference


        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

    LocalLocal Variables[]Variables[]

       Returns references to the local variables of this control.

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

   OwningOwning PanePane

       Returns a reference to the pane that owns the referenced control.

       For nested controls, this property returns a reference to the pane that owns the object
       that contains the control. For example, if you use this property on a control within a
       tab control, the property returns a reference to the pane that owns the tab control.

           Note If a cluster contains the control, the property returns a reference to the
            pane inside the cluster and not the pane that owns the cluster.

7834   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7834 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7835 ordinal=7835 -->
## Property and Method Reference

Property and Method Reference

If the referenced control is not on a pane, this property returns Not a Refnum.

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

PropertyProperty Nodes[]Nodes[]

Returns references to the property nodes of this control.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                   No

 Available in Real-Time Operating System                           No

 Settable when the VI is running                                  No

 Loads the front panel into memory                                         Yes

 Need to authenticate before use                                 No

                                                    © National Instruments 7835

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7835 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7836 ordinal=7836 -->
## Property and Method Reference

Property and Method Reference


        Loads the block diagram into memory                                      Yes

       Remote access allowed                                                   Yes

   SkipSkip WhenWhen TabbingTabbing

           If TRUE, LabVIEW skips this control when you tab through the front panel.

       This property is similar to the Skip this control when tabbing option on the Key
       Navigation page of the Properties dialog box.

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

    StyleStyle IDID

       Returns a numeric identifier for the style of the control.

        In most cases, the value of the Style ID property matches the value of the style input of
       the New VI Object function. To see a list of styles supported by the New VI Object
       function, create a constant from the style terminal of the New VI Object function and
       review the items in the ring constant that LabVIEW creates. Right-click the ring

7836   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7836 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7837 ordinal=7837 -->
## Property and Method Reference

Property and Method Reference

constant and select Visible Items»Digital Display to see the numeric values that
correspond to the Style ID property.

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

SynchronousSynchronous DisplayDisplay

When TRUE, enables synchronous display that shows every update to a data value in a
control or indicator. When FALSE, asynchronous display permits the execution system
to reduce updates to a slower rate and spend more time executing VIs.

In multithreaded systems, you can use this property to set whether to defer updates
for controls and indicators. With asynchronous displays, after the execution system
passes data to front panel controls and indicators, it can immediately continue
execution.

This property is similar to the Advanced»Synchronous Display option on the shortcut
menu of controls and indicators.

You also can use the Defer Panel Updates property to defer all new requests for front
panel updates.


                                                    © National Instruments 7837

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7837 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7838 ordinal=7838 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read/Write

         Available in Run-Time Engine                                        Yes (Read Only)

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

   TerminalTerminal

       Returns the reference to the block diagram terminal of this control. Use this property
       to navigate between the front panel and the block diagram of a VI.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                   No

         Available in Real-Time Operating System                           No

         Settable when the VI is running                                  No

        Loads the front panel into memory                                         Yes

       Need to authenticate before use                                 No


7838   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7838 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7839 ordinal=7839 -->
## Property and Method Reference

Property and Method Reference


 Loads the block diagram into memory                                      Yes

 Remote access allowed                                                   Yes

TipTip StripStrip

Sets or returns the tip strip of a control. A tip strip is the brief description of the object
that appears when you move the cursor over the object.

Other products refer to tip strips as tooltips.

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

Typedef:PathTypedef:Path

Returns the path to the type definition if the control is linked to a type definition.
Otherwise, LabVIEW returns an empty path.

Remarks

The following table lists the characteristics of this property.

                                                    © National Instruments 7839

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7839 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7840 ordinal=7840 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                               Read Only

         Available in Run-Time Engine                                        Yes (Read Only)

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                             No

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

    Typedef:VITypedef:VI

       Returns a reference to the type definition if the control is connected to a type
        definition. Otherwise, LabVIEW returns <NotARef>.

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


7840   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7840 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7841 ordinal=7841 -->
## Property and Method Reference

Property and Method Reference

ValueValue

Data value of the control (LV variant). If this is a Boolean value configured with a
latching mechanical action, this property always returns an error. Due to race
conditions that can occur when you have a Boolean value with latching mechanical
action, you cannot programmatically read Boolean values that are set with a latching
mechanical action.

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

ValueValue

Data value of this control. If this is a Boolean value configured with a latching
mechanical action, this property always returns an error. Due to race conditions that
can occur when you have a Boolean value with latching mechanical action, you cannot
programmatically read Boolean values that are set with a latching mechanical action.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 7841

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7841 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7842 ordinal=7842 -->
## Property and Method Reference

Property and Method Reference


        Data type                                                      Dynamic

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   ValueValue (Signaling)(Signaling)

       Sets the value of the control (LV variant) and generates a Value Change event.

       This property updates the value of an object similar to the Value property. However,
       Value (Signaling) also causes LabVIEW to generate an event as if the user had
        interactively changed the value of the object. National Instruments recommends you
      use this property only when you rely on LabVIEW generating an event in response to
       the programmatic value change.

           If this is a Boolean value configured with a latching mechanical action, this property
      always returns an error. Due to race conditions that can occur when you have a
      Boolean value with latching mechanical action, you cannot programmatically read
      Boolean values that are set with a latching mechanical action.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                               Write Only

         Available in Run-Time Engine                                              Yes


7842   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7842 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7843 ordinal=7843 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                                   Yes

 Settable when the VI is running                                            Yes

 Loads the front panel into memory                               No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                   Yes

ValueValue (Signaling)(Signaling)

Sets the value of the control and generates a Value Change event.

This property updates the value of an object similar to the Value property. However,
Value (Signaling) also causes LabVIEW to generate an event as if the user had
interactively changed the value of the object. National Instruments recommends you
use this property only when you rely on LabVIEW generating an event in response to
the programmatic value change.

If this is a Boolean value configured with a latching mechanical action, this property
always returns an error. Due to race conditions that can occur when you have a
Boolean value with latching mechanical action, you cannot programmatically read
Boolean values that are set with a latching mechanical action.

Remarks

The following table lists the characteristics of this property.


 Data type                                                       Dynamic

 Permissions                                                               Write Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

 Settable when the VI is running                                            Yes

 Loads the front panel into memory                               No


                                                    © National Instruments 7843

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7843 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7844 ordinal=7844 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                   Yes

   ValueValue (Undoable)(Undoable)

      Data value of the control (LabVIEW variant).

       This property behaves identically to writing the Value property except that LabVIEW
       records changes to this property if a transaction starts on the VI. For a Boolean value
       configured with a latching mechanical action, this property always returns an error.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                               Write Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                                   Yes

         Settable when the VI is running                                            Yes

        Loads the front panel into memory                               No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                   Yes

    VisibleVisible

       Displays the front panel control.

       This property is similar to the Show Control and Hide Control options on the shortcut


7844   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7844 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7845 ordinal=7845 -->
## Property and Method Reference

Property and Method Reference

menu of a control.

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

XControl:ContainerXControl:Container BoundsBounds

Sets or gets the container bounds of the XControl.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

                                                    © National Instruments 7845

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7845 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7846 ordinal=7846 -->
## Property and Method Reference

Property and Method Reference


        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

    XControl:ContainerXControl:Container Bounds:HeightBounds:Height

       Height of the XControl.

       This property is an element of the XControl:Container Bounds property.

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

    XControl:ContainerXControl:Container Bounds:WidthBounds:Width

      Width of the XControl.

       This property is an element of the XControl:Container Bounds property.

     Remarks

      The following table lists the characteristics of this property.

7846   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7846 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7847 ordinal=7847 -->
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

XControl:IsXControl:Is XControl?XControl?

Returns TRUE if the control is an XControl, FALSE otherwise.

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

ControlControl EventsEvents

                                                    © National Instruments 7847

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7847 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7848 ordinal=7848 -->
## Property and Method Reference

Property and Method Reference


        Event      Description

        Drag                   Generated after a drag and drop operation completes.       Ended

                   Generated when there is a drag operation pending and the cursor enters the bounds of        Drag Enter                  a control.

                   Generated when there is a drag operation pending and the mouse leaves a control that
        Drag Leave can accept a drag, or if a user cancels a drag and drop operation when hovering over a
                       control.

                   Generated when there is a drag and drop operation pending, as the mouse moves over        Drag Over
                  a control.

        Drag                   Generated when the mouse moves or a key state changes during a drag and drop        Source                     operation.
        Update

                   Generated when the user lifts the mouse when hovering over a control when there is a        Drop
                    drag and drop operation pending.

                   Generated on a control that has keyboard focus. If a key press matches a keyboard
        Key Down   shortcut in the VI menu, such as Ctrl-C or Ctrl-V, LabVIEW does not generate a Key
               Down event, regardless of whether the menu item is enabled.

                   Generated on a control that has keyboard focus. If a key press matches a keyboard
        Key Down?  shortcut in the VI menu, such as Ctrl-C or Ctrl-V, LabVIEW does not generate a Key
               Down event, regardless of whether the menu item is enabled.

        Key        Generated at regular intervals when the user presses and holds a key in a front panel
        Repeat      control.

        Key
                   Generated when the user presses and holds a key in a front panel control.        Repeat?

                   Generated when the user releases a key on the keyboard in a specific control on the
        Key Up
                      front panel.

       Mouse
                   Generated when you click the mouse button on a specific control.
      Down

       Mouse
                   Generated when you click the mouse button on a specific control.
       Down?

       Mouse
                   Generated when the cursor enters the bounds of the front panel object.
         Enter

       Mouse
                   Generated when the cursor leaves the bounds of the front panel object.
        Leave

7848   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7848 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7849 ordinal=7849 -->
## Property and Method Reference

Property and Method Reference


 Event      Description

 Mouse            Generated when you move the mouse over a control. Move

            Generated when you release the mouse button on a specific control. LabVIEW does not Mouse Up            generate this event if a shortcut menu appears when you click the mouse button.

 Mouse            Generated when you scroll the mouse wheel over a control. Wheel

 Shortcut
 Menu      Generated when the user right-clicks a control to display the shortcut menu.
 Activation?

 Shortcut            Generated when the user dismisses a shortcut menu, either by pressing escape or Menu              clicking somewhere outside the menu bounds. This is a notify event.
 Dismissed

 Shortcut   Generated when the user selects an application item from the shortcut menu of a
 Menu       control. Use the Shortcut Menu Selection (User) event to generate an event when the
 Selection   user selects a user-defined menu item. This event is posted after the built-in shortcut
 (App)     menu item is processed by LabVIEW.

 Shortcut
            Generated when the user selects a user-defined item from the shortcut menu. Use the Menu            Shortcut Menu Selection (App) event to generate an event when the user selects an Selection
             application item from the shortcut menu. (User)

 Shortcut
 Menu      Generated when the user selects an application item from the shortcut menu. This
 Selection?  event is posted before the application item is processed by LabVIEW.
 (App)

 Value      Generated when the user changes the value of a control. You must read the terminal of
 Change    a latched Boolean control in its Value Change event case.

DragDrag EndedEnded

Generated after a drag and drop operation completes.

This event occurs after a drop operation, after the user cancels the drag and drop
operation by pressing the <Esc> key, or the drag source window loses focus. You can
use this event in conjunction with other control events to implement custom drag-


                                                    © National Instruments 7849

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7849 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7850 ordinal=7850 -->
## Property and Method Reference

Property and Method Reference

      and-drop behavior. Use this event to implement Drag Moving or to provide notification
     when a drag and drop operation is completed. If you move data during a drag and do
       not copy it as well, you should delete the source data in the Drag Ended event.

     Event Data Fields

      Name  Description

                Source of the event. LabVIEW UI refers to any built-in user interface event.

        Source
                0            LabVIEW UI


        Type   Type of event that occurred, such as Mouse Down, Value Change, Timeout, and so on.


       Time   Value of the millisecond timer when the event occurred.


         CtlRef  Reference to the control on which the event occurred.


                  Indicates the current state of the drag operation. Use this value to update the cursor if
                 necessary.

                0 Drop Cancel—Indicates that no target accepted the data.
         Result                 Drop Move—Indicates that the drop target accepted the drag data and expects the
                1
                   drag source to delete its copy of the data.

                 Drop Copy—Indicates that a drop target accepted the drag data and expects the data
                2
                     to remain at the source.


     Examples

       Refer to the following example files included with LabVIEW.


7850   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7850 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7851 ordinal=7851 -->
## Property and Method Reference

Property and Method Reference

  • labview\examples\Structures\Event Structure\Drag and Drop
   - Initiating a Custom Drag.vi
DragDrag EnterEnter

Generated when there is a drag operation pending and the cursor enters the bounds of
a control.

You can use this event in conjunction with other control events to implement custom
drag-and-drop behavior. Use this event to report to the drag source that the drop
target accepts the drag data.

Event Data Fields

 Name               Description

                    Source of the event. LabVIEW UI refers to any built-in user interface event.

 Source
                    0          LabVIEW UI


                   Type of event that occurred, such as Mouse Down, Value Change, Timeout, Type                  and so on.


 Time                Value of the millisecond timer when the event occurred.


 CtlRef               Reference to the control on which the event occurred.


                     Coordinates of the location of the mouse click at the time the event occurs.
 Coords              Coordinates are relative to the drop target's owning pane origin, excluding
                         clusters.


                                                    © National Instruments 7851

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7851 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7852 ordinal=7852 -->
## Property and Method Reference

Property and Method Reference


      Name               Description

                             Value that corresponds to which mouse button the user clicked. Left mouse
                            button is 1, right mouse button is 2. Operating systems might assign higher        Button                         numbers if you have a mouse with more than two buttons. For filter events,
                          you can modify the data returned by this event data field.


                                Cluster of Booleans that contain platform-independent modifiers. LabVIEW
                               returns all platform-dependent modifiers in the PlatMods event data field.
                             For key events, this event returns a Boolean indicating if the event occurred
                        on the numeric keypad. For mouse events, this event returns a Boolean       Mods                                indicating if the event was a double-click. For both events, a Boolean is
                             returned if the platform-independent menu key, such as <Ctrl> on Windows
                              or <Command> on macOS, was pressed when the event occurred. For filter
                               events, you can modify the data returned by this event data field.


                                Cluster of Booleans that contain platform-dependent modifiers. Specifies if
                            platform-dependent keys, such as <Ctrl>, <Shift>, <Alt>, <Command>, and
                           <Option> were held down when the event was triggered. For filter events,
        PlatMods          you can modify the data returned by this event data field. A key can be both a
                     Mod and PlatMod. For example, <Ctrl> is the platform-independent menu
                           key on Windows, but you also can use it in platform-dependent
                           programming.


                              Array of unique names of data types available during this drag and drop
        AvailableDataNames  operation. Use this array to determine if a data type is available that the drop
                                target can accept


                             Reports to the drag source the action that the drop target would take if the
        Accepted?          drop occurred at this moment. TRUE, if the target would accept the drop,
                          FALSE otherwise.


     Examples

       Refer to the following example files included with LabVIEW.


7852   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7852 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7853 ordinal=7853 -->
## Property and Method Reference

Property and Method Reference

  • labview\examples\Structures\Event Structure\Drag and Drop
   - Initiating a Custom Drag.vi
DragDrag LeaveLeave

Generated when there is a drag operation pending and the mouse leaves a control that
can accept a drag, or if a user cancels a drag and drop operation when hovering over a
control.

You can use this event in conjunction with other control events to implement custom
drag-and-drop behavior. Use this event if you need notifications when the mouse
leaves the drop target or if the user cancels drag and drop operation when hovering
over the drop target.

Event Data Fields

 Name               Description

                    Source of the event. LabVIEW UI refers to any built-in user interface event.

 Source
                    0          LabVIEW UI


                   Type of event that occurred, such as Mouse Down, Value Change, Timeout, Type
                  and so on.


 Time                Value of the millisecond timer when the event occurred.


 CtlRef               Reference to the control on which the event occurred.


                      Array of unique names of data types available during this drag and drop
 AvailableDataNames  operation. Use this array to determine if a data type is available that the drop
                       target can accept


                                                    © National Instruments 7853

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7853 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7854 ordinal=7854 -->
## Property and Method Reference

Property and Method Reference

   DragDrag OverOver

      Generated when there is a drag and drop operation pending, as the mouse moves over
      a control.

      You can use this event in conjunction with other control events to implement custom
       drag-and-drop behavior. Use this event if the drop target allows or disallows dropping
      on it depending on where the mouse is located. For example, you can use this event if
      you only want to allow a user to drop in a graph plot area and nowhere else on the
       graph.

      You may want to use the Drag Enter event instead if the mouse location on the target is
       inconsequential. Because the Drag Over event fires continuously as it checks to see if
       the drag is accepted, as opposed to the Drag Enter event which fires once, you also
     may want to use the Drag Enter event if you do not need to specify a location on the
        target.

     Event Data Fields

      Name               Description

                           Source of the event. LabVIEW UI refers to any built-in user interface event.

        Source
                           0          LabVIEW UI


                          Type of event that occurred, such as Mouse Down, Value Change, Timeout,
        Type
                         and so on.


       Time                Value of the millisecond timer when the event occurred.


         CtlRef               Reference to the control on which the event occurred.


7854   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7854 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7855 ordinal=7855 -->
## Property and Method Reference

Property and Method Reference


Name               Description

                    Coordinates of the location of the mouse click at the time the event occurs.
Coords              Coordinates are relative to the drop target's owning pane origin, excluding
                        clusters.


                    Value that corresponds to which mouse button the user clicked. Left mouse
                    button is 1, right mouse button is 2. Operating systems might assign higher
Button                 numbers if you have a mouse with more than two buttons. For filter events,
                  you can modify the data returned by this event data field.


                      Cluster of Booleans that contain platform-independent modifiers. LabVIEW
                      returns all platform-dependent modifiers in the PlatMods event data field.
                    For key events, this event returns a Boolean indicating if the event occurred
                 on the numeric keypad. For mouse events, this event returns a BooleanMods                      indicating if the event was a double-click. For both events, a Boolean is
                    returned if the platform-independent menu key, such as <Ctrl> on Windows
                     or <Command> on macOS, was pressed when the event occurred. For filter
                      events, you can modify the data returned by this event data field.


                      Cluster of Booleans that contain platform-dependent modifiers. Specifies if
                    platform-dependent keys, such as <Ctrl>, <Shift>, <Alt>, <Command>, and
                   <Option> were held down when the event was triggered. For filter events,
PlatMods          you can modify the data returned by this event data field. A key can be both a
               Mod and PlatMod. For example, <Ctrl> is the platform-independent menu
                   key on Windows, but you also can use it in platform-dependent
                   programming.


                     Array of unique names of data types available during this drag and drop
AvailableDataNames  operation. Use this array to determine if a data type is available that the drop
                       target can accept


                    Reports to the drag source the action that the drop target would take if the
Accepted?          drop occurred at this moment. TRUE, if the target would accept the drop,
                  FALSE otherwise.


                                                    © National Instruments 7855

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7855 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7856 ordinal=7856 -->
## Property and Method Reference

Property and Method Reference

   DragDrag SourceSource UpdateUpdate

      Generated when the mouse moves or a key state changes during a drag and drop
       operation.

      You can use this event in conjunction with other control events to implement custom
       drag-and-drop behavior. Use this event to use custom drag and drop cursors or to
       receive notifications of the current state of a drag and drop operation.

     Event Data Fields

      Name  Description

                Source of the event. LabVIEW UI refers to any built-in user interface event.

        Source
                0            LabVIEW UI


        Type   Type of event that occurred, such as Mouse Down, Value Change, Timeout, and so on.


       Time   Value of the millisecond timer when the event occurred.


         CtlRef  Reference to the control on which the event occurred.


                  Indicates the current state of the drag operation. Use this value to update the cursor if
                 necessary.

                0 Drop Cancel—Indicates that no target accepted the data.
         Result
                 Drop Move—Indicates that the drop target accepted the drag data and expects the
                1
                   drag source to delete its copy of the data.

                2 Drop Copy—Indicates that a drop target accepted the drag data and expects the data


7856   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7856 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7857 ordinal=7857 -->
## Property and Method Reference

Property and Method Reference


 Name  Description


             to remain at the source.


       The cursor that LabVIEW uses until the next drag source update. Wire Not a Refnum or Cursor
         leave unwired to use the system-defined drag and drop cursors based on the result.

DropDrop

Generated when the user lifts the mouse when hovering over a control when there is a
drag and drop operation pending.

Use this event to implement custom drop behavior.

Event Data Fields

 Name               Description

                    Source of the event. LabVIEW UI refers to any built-in user interface event.

 Source
                    0          LabVIEW UI


                   Type of event that occurred, such as Mouse Down, Value Change, Timeout,
 Type
                  and so on.


 Time                Value of the millisecond timer when the event occurred.


 CtlRef               Reference to the control on which the event occurred.


                                                    © National Instruments 7857

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7857 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7858 ordinal=7858 -->
## Property and Method Reference

Property and Method Reference


      Name               Description

                             Coordinates of the location of the mouse click at the time the event occurs.
        Coords              Coordinates are relative to the drop target's owning pane origin, excluding
                                  clusters.


                             Value that corresponds to which mouse button the user clicked. Left mouse
                            button is 1, right mouse button is 2. Operating systems might assign higher
        Button                         numbers if you have a mouse with more than two buttons. For filter events,
                          you can modify the data returned by this event data field.


                                Cluster of Booleans that contain platform-independent modifiers. LabVIEW
                               returns all platform-dependent modifiers in the PlatMods event data field.
                             For key events, this event returns a Boolean indicating if the event occurred
                        on the numeric keypad. For mouse events, this event returns a Boolean       Mods                                indicating if the event was a double-click. For both events, a Boolean is
                             returned if the platform-independent menu key, such as <Ctrl> on Windows
                              or <Command> on macOS, was pressed when the event occurred. For filter
                               events, you can modify the data returned by this event data field.


                                Cluster of Booleans that contain platform-dependent modifiers. Specifies if
                            platform-dependent keys, such as <Ctrl>, <Shift>, <Alt>, <Command>, and
                           <Option> were held down when the event was triggered. For filter events,
        PlatMods          you can modify the data returned by this event data field. A key can be both a
                     Mod and PlatMod. For example, <Ctrl> is the platform-independent menu
                           key on Windows, but you also can use it in platform-dependent
                           programming.


                              Array of unique names of data types available during this drag and drop
        AvailableDataNames  operation. Use this array to determine if a data type is available that the drop
                                target can accept


                             Reports to the drag source the action that the drop target would take if the
        Accepted?          drop occurred at this moment. TRUE, if the target would accept the drop,
                          FALSE otherwise.


7858   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7858 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7859 ordinal=7859 -->
## Property and Method Reference

Property and Method Reference

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Structures\Event Structure\Drag and Drop
   - Initiating a Custom Drag.vi
KeyKey DownDown

Generated on a control that has keyboard focus. If a key press matches a keyboard
shortcut in the VI menu, such as Ctrl-C or Ctrl-V, LabVIEW does not generate a Key
Down event, regardless of whether the menu item is enabled.

Key Down Event Caveats

  • (Windows) F3 generates a Key Down event only in the LabVIEW Run-Time Engine.
  • LabVIEW only generates events for the Cluster»All Elements source when the
    cluster has keyboard focus, not when an individual element inside the cluster has
   keyboard focus.

Event Data Fields

 Name     Description

           Source of the event. LabVIEW UI refers to any built-in user interface event.

 Source
           0            LabVIEW UI


 Type      Type of event that occurred, such as Mouse Down, Value Change, Timeout, and so on.


 Time      Value of the millisecond timer when the event occurred.


                                                    © National Instruments 7859

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7859 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7860 ordinal=7860 -->
## Property and Method Reference

Property and Method Reference


      Name     Description

         CtlRef     Reference to the control on which the event occurred.


                     Integer value that corresponds to the key pressed on the keyboard and represents a
                    character from the current code page that your system uses. You also can modify the
        Char                   data returned by this event data field. Search for code pages on the Microsoft Web
                        site for a listing of the code page tables supported by Windows.

                 Enumerated type indicating the virtual key code of the key pressed. Values include
                      ASCII, Shift, NumLock, F1, and so on. You also can modify the data received from this
                   event data field.
        VKey
                     Note VKey has separate values for the <Enter> key on the alphanumeric
                          keyboard and <Enter> key on the numeric keypad.


                 Scan code unique for each key on the keyboard. The values are unique for each physical       ScanCode                     key, and allow you to match Key Up and Key Down events.


                     Cluster of Booleans that contain platform-independent modifiers. LabVIEW returns all
                   platform-dependent modifiers in the PlatMods event data field. For key events, this
                   event returns a Boolean indicating if the event occurred on the numeric keypad. For
       Mods     mouse events, this event returns a Boolean indicating if the event was a double-click.
                   For both events, a Boolean is returned if the platform-independent menu key, such as
                     <Ctrl> on Windows or <Command> on macOS, was pressed when the event occurred.
                   For filter events, you can modify the data returned by this event data field.


                     Cluster of Booleans that contain platform-dependent modifiers. Specifies if platform-
                 dependent keys, such as <Ctrl>, <Shift>, <Alt>, <Command>, and <Option> were held
               down when the event was triggered. For filter events, you can modify the data returned
        PlatMods
                 by this event data field. A key can be both a Mod and PlatMod. For example, <Ctrl> is
                   the platform-independent menu key on Windows, but you also can use it in platform-
                 dependent programming.


7860   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7860 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7861 ordinal=7861 -->
## Property and Method Reference

Property and Method Reference


 Name     Description

          A reference to the object that has keyboard focus. When the event is for a control, it
 FocusObj  might be a sub-component, like a scale, label, and so on, rather than the control itself.
          You also can modify the data returned by this event data field.

KeyKey Down?Down?

Generated on a control that has keyboard focus. If a key press matches a keyboard
shortcut in the VI menu, such as Ctrl-C or Ctrl-V, LabVIEW does not generate a Key
Down event, regardless of whether the menu item is enabled.

Key Down Event Caveats

  • (Windows) F3 generates a Key Down event only in the LabVIEW Run-Time Engine.
  • LabVIEW only generates events for the Cluster»All Elements source when the
    cluster has keyboard focus, not when an individual element inside the cluster has
   keyboard focus.

Event Data Fields

 Name     Description

           Source of the event. LabVIEW UI refers to any built-in user interface event.

 Source
           0            LabVIEW UI


 Type      Type of event that occurred, such as Mouse Down, Value Change, Timeout, and so on.


 Time      Value of the millisecond timer when the event occurred.


                                                    © National Instruments 7861

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7861 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7862 ordinal=7862 -->
## Property and Method Reference

Property and Method Reference


      Name     Description

         CtlRef     Reference to the control on which the event occurred.


                     Integer value that corresponds to the key pressed on the keyboard and represents a
                    character from the current code page that your system uses. You also can modify the
        Char                   data returned by this event data field. Search for code pages on the Microsoft Web
                        site for a listing of the code page tables supported by Windows.

                 Enumerated type indicating the virtual key code of the key pressed. Values include
                      ASCII, Shift, NumLock, F1, and so on. You also can modify the data received from this
                   event data field.
        VKey
                     Note VKey has separate values for the <Enter> key on the alphanumeric
                          keyboard and <Enter> key on the numeric keypad.


                 Scan code unique for each key on the keyboard. The values are unique for each physical       ScanCode                     key, and allow you to match Key Up and Key Down events.


                     Cluster of Booleans that contain platform-independent modifiers. LabVIEW returns all
                   platform-dependent modifiers in the PlatMods event data field. For key events, this
                   event returns a Boolean indicating if the event occurred on the numeric keypad. For
       Mods     mouse events, this event returns a Boolean indicating if the event was a double-click.
                   For both events, a Boolean is returned if the platform-independent menu key, such as
                     <Ctrl> on Windows or <Command> on macOS, was pressed when the event occurred.
                   For filter events, you can modify the data returned by this event data field.


                     Cluster of Booleans that contain platform-dependent modifiers. Specifies if platform-
                 dependent keys, such as <Ctrl>, <Shift>, <Alt>, <Command>, and <Option> were held
               down when the event was triggered. For filter events, you can modify the data returned
        PlatMods
                 by this event data field. A key can be both a Mod and PlatMod. For example, <Ctrl> is
                   the platform-independent menu key on Windows, but you also can use it in platform-
                 dependent programming.


7862   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7862 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7863 ordinal=7863 -->
## Property and Method Reference

Property and Method Reference


 Name     Description

          A reference to the object that has keyboard focus. When the event is for a control, it
 FocusObj  might be a sub-component, like a scale, label, and so on, rather than the control itself.
          You also can modify the data returned by this event data field.

           Allows you to prevent LabVIEW from processing the event, bypassing the behavior Discard?           normally triggered by that event. The default is FALSE.

KeyKey RepeatRepeat

Generated at regular intervals when the user presses and holds a key in a front panel
control.

      Note LabVIEW only generates events for the Cluster»All Elements source
      when the cluster has keyboard focus, not when an individual element inside
       the cluster has keyboard focus.

Event Data Fields

 Name     Description

           Source of the event. LabVIEW UI refers to any built-in user interface event.

 Source
           0            LabVIEW UI


 Type      Type of event that occurred, such as Mouse Down, Value Change, Timeout, and so on.


 Time      Value of the millisecond timer when the event occurred.


 CtlRef     Reference to the control on which the event occurred.


                                                    © National Instruments 7863

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7863 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7864 ordinal=7864 -->
## Property and Method Reference

Property and Method Reference


      Name     Description

                     Integer value that corresponds to the key pressed on the keyboard and represents a
                    character from the current code page that your system uses. You also can modify the
        Char                   data returned by this event data field. Search for code pages on the Microsoft Web
                        site for a listing of the code page tables supported by Windows.

                 Enumerated type indicating the virtual key code of the key pressed. Values include
                      ASCII, Shift, NumLock, F1, and so on. You also can modify the data received from this
                   event data field.
        VKey
                     Note VKey has separate values for the <Enter> key on the alphanumeric
                          keyboard and <Enter> key on the numeric keypad.


                 Scan code unique for each key on the keyboard. The values are unique for each physical
       ScanCode                     key, and allow you to match Key Up and Key Down events.


                     Cluster of Booleans that contain platform-independent modifiers. LabVIEW returns all
                   platform-dependent modifiers in the PlatMods event data field. For key events, this
                   event returns a Boolean indicating if the event occurred on the numeric keypad. For
       Mods     mouse events, this event returns a Boolean indicating if the event was a double-click.
                   For both events, a Boolean is returned if the platform-independent menu key, such as
                     <Ctrl> on Windows or <Command> on macOS, was pressed when the event occurred.
                   For filter events, you can modify the data returned by this event data field.


                     Cluster of Booleans that contain platform-dependent modifiers. Specifies if platform-
                 dependent keys, such as <Ctrl>, <Shift>, <Alt>, <Command>, and <Option> were held
               down when the event was triggered. For filter events, you can modify the data returned
        PlatMods
                 by this event data field. A key can be both a Mod and PlatMod. For example, <Ctrl> is
                   the platform-independent menu key on Windows, but you also can use it in platform-
                 dependent programming.


                A reference to the object that has keyboard focus. When the event is for a control, it
        FocusObj  might be a sub-component, like a scale, label, and so on, rather than the control itself.
                 You also can modify the data returned by this event data field.


7864   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7864 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7865 ordinal=7865 -->
## Property and Method Reference

Property and Method Reference

KeyKey Repeat?Repeat?

Generated when the user presses and holds a key in a front panel control.

      Note LabVIEW only generates events for the Cluster»All Elements source
      when the cluster has keyboard focus, not when an individual element inside
       the cluster has keyboard focus.

Event Data Fields

 Name     Description

           Source of the event. LabVIEW UI refers to any built-in user interface event.

 Source
           0            LabVIEW UI


 Type      Type of event that occurred, such as Mouse Down, Value Change, Timeout, and so on.


 Time      Value of the millisecond timer when the event occurred.


 CtlRef     Reference to the control on which the event occurred.


            Integer value that corresponds to the key pressed on the keyboard and represents a
            character from the current code page that your system uses. You also can modify the
 Char           data returned by this event data field. Search for code pages on the Microsoft Web
              site for a listing of the code page tables supported by Windows.

          Enumerated type indicating the virtual key code of the key pressed. Values include
 VKey       ASCII, Shift, NumLock, F1, and so on. You also can modify the data received from this
           event data field.


                                                    © National Instruments 7865

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7865 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7866 ordinal=7866 -->
## Property and Method Reference

Property and Method Reference


      Name     Description

                     Note VKey has separate values for the <Enter> key on the alphanumeric
                          keyboard and <Enter> key on the numeric keypad.


                 Scan code unique for each key on the keyboard. The values are unique for each physical       ScanCode
                     key, and allow you to match Key Up and Key Down events.


                     Cluster of Booleans that contain platform-independent modifiers. LabVIEW returns all
                   platform-dependent modifiers in the PlatMods event data field. For key events, this
                   event returns a Boolean indicating if the event occurred on the numeric keypad. For
       Mods     mouse events, this event returns a Boolean indicating if the event was a double-click.
                   For both events, a Boolean is returned if the platform-independent menu key, such as
                     <Ctrl> on Windows or <Command> on macOS, was pressed when the event occurred.
                   For filter events, you can modify the data returned by this event data field.


                     Cluster of Booleans that contain platform-dependent modifiers. Specifies if platform-
                 dependent keys, such as <Ctrl>, <Shift>, <Alt>, <Command>, and <Option> were held
               down when the event was triggered. For filter events, you can modify the data returned        PlatMods                 by this event data field. A key can be both a Mod and PlatMod. For example, <Ctrl> is
                   the platform-independent menu key on Windows, but you also can use it in platform-
                 dependent programming.


                A reference to the object that has keyboard focus. When the event is for a control, it
        FocusObj  might be a sub-component, like a scale, label, and so on, rather than the control itself.
                 You also can modify the data returned by this event data field.

                   Allows you to prevent LabVIEW from processing the event, bypassing the behavior
         Discard?
                   normally triggered by that event. The default is FALSE.

   KeyKey UpUp

      Generated when the user releases a key on the keyboard in a specific control on the
       front panel.


7866   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7866 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7867 ordinal=7867 -->
## Property and Method Reference

Property and Method Reference

      Note LabVIEW only generates events for the Cluster»All Elements source
      when the cluster has keyboard focus, not when an individual element inside
       the cluster has keyboard focus.

Event Data Fields

 Name     Description

           Source of the event. LabVIEW UI refers to any built-in user interface event.

 Source
           0            LabVIEW UI


 Type      Type of event that occurred, such as Mouse Down, Value Change, Timeout, and so on.


 Time      Value of the millisecond timer when the event occurred.


 CtlRef     Reference to the control on which the event occurred.


          Scan code unique for each key on the keyboard. The values are unique for each physical ScanCode
             key, and allow you to match Key Up and Key Down events.


            Cluster of Booleans that contain platform-independent modifiers. LabVIEW returns all
           platform-dependent modifiers in the PlatMods event data field. For key events, this
           event returns a Boolean indicating if the event occurred on the numeric keypad. For
 Mods     mouse events, this event returns a Boolean indicating if the event was a double-click.
           For both events, a Boolean is returned if the platform-independent menu key, such as
             <Ctrl> on Windows or <Command> on macOS, was pressed when the event occurred.
           For filter events, you can modify the data returned by this event data field.


 PlatMods  Cluster of Booleans that contain platform-dependent modifiers. Specifies if platform-


                                                    © National Instruments 7867

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7867 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7868 ordinal=7868 -->
## Property and Method Reference

Property and Method Reference


      Name     Description

                 dependent keys, such as <Ctrl>, <Shift>, <Alt>, <Command>, and <Option> were held
               down when the event was triggered. For filter events, you can modify the data returned
                 by this event data field. A key can be both a Mod and PlatMod. For example, <Ctrl> is
                   the platform-independent menu key on Windows, but you also can use it in platform-
                 dependent programming.


                A reference to the object that has keyboard focus. When the event is for a control, it
        FocusObj  might be a sub-component, like a scale, label, and so on, rather than the control itself.
                 You also can modify the data returned by this event data field.

   MouseMouse DownDown

      Generated when you click the mouse button on a specific control.

     Event Data Fields

      Name     Description

                  Source of the event. LabVIEW UI refers to any built-in user interface event.

        Source
                  0            LabVIEW UI


        Type     Type of event that occurred, such as Mouse Down, Value Change, Timeout, and so on.


       Time     Value of the millisecond timer when the event occurred.


         CtlRef     Reference to the control on which the event occurred.

        Coords


7868   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7868 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7869 ordinal=7869 -->
## Property and Method Reference

Property and Method Reference


 Name     Description

           Value that corresponds to which mouse button the user clicked. Left mouse button is 1,
            right mouse button is 2. Operating systems might assign higher numbers if you have a Button         mouse with more than two buttons. For filter events, you can modify the data returned
          by this event data field.


            Cluster of Booleans that contain platform-independent modifiers. LabVIEW returns all
          platform-dependent modifiers in the PlatMods event data field. For key events, this
          event returns a Boolean indicating if the event occurred on the numeric keypad. For
 Mods    mouse events, this event returns a Boolean indicating if the event was a double-click.
           For both events, a Boolean is returned if the platform-independent menu key, such as
            <Ctrl> on Windows or <Command> on macOS, was pressed when the event occurred.
           For filter events, you can modify the data returned by this event data field.


            Cluster of Booleans that contain platform-dependent modifiers. Specifies if platform-
          dependent keys, such as <Ctrl>, <Shift>, <Alt>, <Command>, and <Option> were held
        down when the event was triggered. For filter events, you can modify the data returned
 PlatMods          by this event data field. A key can be both a Mod and PlatMod. For example, <Ctrl> is the
           platform-independent menu key on Windows, but you also can use it in platform-
          dependent programming.

MouseMouse Down?Down?

Generated when you click the mouse button on a specific control.

Event Data Fields

 Name     Description

          Source of the event. LabVIEW UI refers to any built-in user interface event.

 Source
           0            LabVIEW UI


                                                    © National Instruments 7869

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7869 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7870 ordinal=7870 -->
## Property and Method Reference

Property and Method Reference


      Name     Description

        Type     Type of event that occurred, such as Mouse Down, Value Change, Timeout, and so on.


       Time     Value of the millisecond timer when the event occurred.


         CtlRef     Reference to the control on which the event occurred.

        Coords

                   Value that corresponds to which mouse button the user clicked. Left mouse button is 1,
                     right mouse button is 2. Operating systems might assign higher numbers if you have a        Button
               mouse with more than two buttons. For filter events, you can modify the data returned
                 by this event data field.


                    Cluster of Booleans that contain platform-independent modifiers. LabVIEW returns all
                  platform-dependent modifiers in the PlatMods event data field. For key events, this
                  event returns a Boolean indicating if the event occurred on the numeric keypad. For
       Mods    mouse events, this event returns a Boolean indicating if the event was a double-click.
                   For both events, a Boolean is returned if the platform-independent menu key, such as
                     <Ctrl> on Windows or <Command> on macOS, was pressed when the event occurred.
                   For filter events, you can modify the data returned by this event data field.


                    Cluster of Booleans that contain platform-dependent modifiers. Specifies if platform-
                 dependent keys, such as <Ctrl>, <Shift>, <Alt>, <Command>, and <Option> were held
              down when the event was triggered. For filter events, you can modify the data returned
        PlatMods
                 by this event data field. A key can be both a Mod and PlatMod. For example, <Ctrl> is the
                  platform-independent menu key on Windows, but you also can use it in platform-
                 dependent programming.

                   Allows you to prevent LabVIEW from processing the event, bypassing the behavior
         Discard?
                  normally triggered by that event. The default is FALSE.


7870   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7870 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7871 ordinal=7871 -->
## Property and Method Reference

Property and Method Reference

MouseMouse EnterEnter

Generated when the cursor enters the bounds of the front panel object.

Event Data Fields

 Name   Description

         Source of the event. LabVIEW UI refers to any built-in user interface event.

 Source
         0            LabVIEW UI


 Type    Type of event that occurred, such as Mouse Down, Value Change, Timeout, and so on.


 Time    Value of the millisecond timer when the event occurred.


 CtlRef   Reference to the control on which the event occurred.

MouseMouse LeaveLeave

Generated when the cursor leaves the bounds of the front panel object.

Event Data Fields

 Name   Description

         Source of the event. LabVIEW UI refers to any built-in user interface event.

 Source
         0            LabVIEW UI


                                                    © National Instruments 7871

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7871 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7872 ordinal=7872 -->
## Property and Method Reference

Property and Method Reference


      Name   Description

        Type    Type of event that occurred, such as Mouse Down, Value Change, Timeout, and so on.


       Time    Value of the millisecond timer when the event occurred.


         CtlRef   Reference to the control on which the event occurred.

   MouseMouse MoveMove

      Generated when you move the mouse over a control.

     Event Data Fields

      Name   Description

                Source of the event. LabVIEW UI refers to any built-in user interface event.

        Source
                0            LabVIEW UI


        Type    Type of event that occurred, such as Mouse Down, Value Change, Timeout, and so on.


       Time    Value of the millisecond timer when the event occurred.


         CtlRef   Reference to the control on which the event occurred.

        Coords


7872   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7872 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7873 ordinal=7873 -->
## Property and Method Reference

Property and Method Reference

MouseMouse UpUp

Generated when you release the mouse button on a specific control. LabVIEW does not
generate this event if a shortcut menu appears when you click the mouse button.

Event Data Fields

 Name     Description

          Source of the event. LabVIEW UI refers to any built-in user interface event.

 Source
           0            LabVIEW UI


 Type     Type of event that occurred, such as Mouse Down, Value Change, Timeout, and so on.


 Time     Value of the millisecond timer when the event occurred.


 CtlRef     Reference to the control on which the event occurred.

 Coords

           Value that corresponds to which mouse button the user clicked. Left mouse button is 1,
            right mouse button is 2. Operating systems might assign higher numbers if you have a
 Button
         mouse with more than two buttons. For filter events, you can modify the data returned
          by this event data field.


            Cluster of Booleans that contain platform-independent modifiers. LabVIEW returns all
          platform-dependent modifiers in the PlatMods event data field. For key events, this
          event returns a Boolean indicating if the event occurred on the numeric keypad. For
 Mods
         mouse events, this event returns a Boolean indicating if the event was a double-click.
           For both events, a Boolean is returned if the platform-independent menu key, such as
            <Ctrl> on Windows or <Command> on macOS, was pressed when the event occurred.


                                                    © National Instruments 7873

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7873 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7874 ordinal=7874 -->
## Property and Method Reference

Property and Method Reference


      Name     Description

                   For filter events, you can modify the data returned by this event data field.


                    Cluster of Booleans that contain platform-dependent modifiers. Specifies if platform-
                 dependent keys, such as <Ctrl>, <Shift>, <Alt>, <Command>, and <Option> were held
              down when the event was triggered. For filter events, you can modify the data returned        PlatMods                 by this event data field. A key can be both a Mod and PlatMod. For example, <Ctrl> is the
                  platform-independent menu key on Windows, but you also can use it in platform-
                 dependent programming.

   MouseMouse WheelWheel

      Generated when you scroll the mouse wheel over a control.

     Event Data Fields

      Name       Description

                    Source of the event. LabVIEW UI refers to any built-in user interface event.

        Source
                    0           LabVIEW UI


        Type       Type of event that occurred, such as Mouse Down, Value Change, Timeout, and so on.


       Time        Value of the millisecond timer when the event occurred.


         CtlRef       Reference to the control on which the event occurred.


        Coords      Coordinates of the mouse at the time of the event. Coordinates are relative to the


7874   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7874 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7875 ordinal=7875 -->
## Property and Method Reference

Property and Method Reference


Name       Description

              origin of the pane.


           The distance the mouse wheel moved. (Windows) A positive value indicates a forward
              rotation of the wheel away from you. A negative value indicates a backward rotation
Delta         of the wheel towards you. (macOS) Navigate to the system settings of the computer
             to specify how the operating system interprets the direction of the mouse wheel
                scroll. macOS 10.7 and later inverts the scroll direction of the mouse by default.


             Value that corresponds to the orientation of the scroll bar and indicates whether theOrientation             user initiated this event on a horizontal or vertical scroll bar.


              Cluster of Booleans that corresponds to the mouse button(s) the user pressed and
ButtonMods held during the mouse wheel movement. The Booleans indicate whether the user
            pressed the left, right, or middle button(s).


              Cluster of Booleans that contain platform-independent modifiers. LabVIEW returns all
            platform-dependent modifiers in the PlatMods event data field. For key events, this
            event returns a Boolean indicating if the event occurred on the numeric keypad. For
Mods      mouse events, this event returns a Boolean indicating if the event was a double-click.
             For both events, a Boolean is returned if the platform-independent menu key, such as
              <Ctrl> on Windows or <Command> on macOS, was pressed when the event occurred.
             For filter events, you can modify the data returned by this event data field.


              Cluster of Booleans that contain platform-dependent modifiers. Specifies if platform-
           dependent keys, such as <Ctrl>, <Shift>, <Alt>, <Command>, and <Option> were held
          down when the event was triggered. For filter events, you can modify the data
PlatMods
             returned by this event data field. A key can be both a Mod and PlatMod. For example,
              <Ctrl> is the platform-independent menu key on Windows, but you also can use it in
            platform-dependent programming.


                                                    © National Instruments 7875

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7875 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7876 ordinal=7876 -->
## Property and Method Reference

Property and Method Reference

    ShortcutShortcut MenuMenu Activation?Activation?

      Generated when the user right-clicks a control to display the shortcut menu.

     Event Data Fields

      Name    Description

                 Source of the event. LabVIEW UI refers to any built-in user interface event.

        Source
                 0            LabVIEW UI


        Type     Type of event that occurred, such as Mouse Down, Value Change, Timeout, and so on.


       Time     Value of the millisecond timer when the event occurred.


         CtlRef    Reference to the control on which the event occurred.


                  Reference to the control shortcut menu that you can modify during this event. MenuRef
       MenuRef                         is valid only during this event case.

        Coords

                  Reference to the object on which the event occurred. For example, if the user right-clicks
                a cluster that contains several controls, the SubObj might be a control within the cluster.
        SubObj
                You might want to add menu items only if the user right-clicks certain controls within a
                      cluster. You can check the value of SubObj.

                  Allows you to prevent LabVIEW from processing the event, bypassing the behavior
         Discard?
                  normally triggered by that event. The default is FALSE.


7876   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7876 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7877 ordinal=7877 -->
## Property and Method Reference

Property and Method Reference

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Dialog and User Interface\Menu\
   Customizing Shortcut Menus\Customizing Shortcut Menus.vi
ShortcutShortcut MenuMenu DismissedDismissed

Generated when the user dismisses a shortcut menu, either by pressing escape or
clicking somewhere outside the menu bounds. This is a notify event.

Event Data Fields

 Name   Description

         Source of the event. LabVIEW UI refers to any built-in user interface event.

 Source
         0            LabVIEW UI


 Type    Type of event that occurred, such as Mouse Down, Value Change, Timeout, and so on.


 Time    Value of the millisecond timer when the event occurred.


 CtlRef   Reference to the control on which the event occurred.

ShortcutShortcut MenuMenu SelectionSelection (App)(App)

Generated when the user selects an application item from the shortcut menu of a
control. Use the Shortcut Menu Selection (User) event to generate an event when the
user selects a user-defined menu item. This event is posted after the built-in shortcut

                                                    © National Instruments 7877

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7877 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7878 ordinal=7878 -->
## Property and Method Reference

Property and Method Reference

     menu item is processed by LabVIEW.

     Event Data Fields

      Name    Description

                 Source of the event. LabVIEW UI refers to any built-in user interface event.

        Source
                  0            LabVIEW UI


        Type     Type of event that occurred, such as Mouse Down, Value Change, Timeout, and so on.


       Time     Value of the millisecond timer when the event occurred.


         CtlRef    Reference to the control on which the event occurred.


                  Reference to the control shortcut menu that you can modify during this event. MenuRef
       MenuRef                         is valid only during this event case.


              Name of the LabVIEW shortcut menu item the user selected, such as
        ItemTag               APP_SC_COPY_DATA.


                  Path of the LabVIEW shortcut menu item that the user selected, such as
        ItemPath              APP_SC_VISIBLE_ITEMS:APP_SC_SCALE_LEGEND.

        Coords

                  Reference to the object on which the event occurred. For example, if the user right-clicks
        SubObj   a cluster that contains several controls, the SubObj might be a control within the cluster,
                 even if the cluster added the shortcut menu item.


7878   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7878 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7879 ordinal=7879 -->
## Property and Method Reference

Property and Method Reference

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Dialog and User Interface\Menu\
   Customizing Shortcut Menus\Customizing Shortcut Menus.vi
ShortcutShortcut MenuMenu SelectionSelection (User)(User)

Generated when the user selects a user-defined item from the shortcut menu. Use the
Shortcut Menu Selection (App) event to generate an event when the user selects an
application item from the shortcut menu.

Event Data Fields

 Name    Description

          Source of the event. LabVIEW UI refers to any built-in user interface event.

 Source
          0            LabVIEW UI


 Type     Type of event that occurred, such as Mouse Down, Value Change, Timeout, and so on.


 Time     Value of the millisecond timer when the event occurred.


 CtlRef    Reference to the control on which the event occurred.


           Reference to the control shortcut menu that you can modify during this event. MenuRef
 MenuRef
               is valid only during this event case.


 ItemTag  Name of the user-defined shortcut menu item the user selected, such as


                                                    © National Instruments 7879

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7879 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7880 ordinal=7880 -->
## Property and Method Reference

Property and Method Reference


      Name    Description

               USER_MY_HELP.


                  Path of the user-defined shortcut menu item that the user selected, such as
        ItemPath              APP_HELP:USER_MY_HELP.

        Coords

                  Reference to the object on which the event occurred. For example, if the user right-clicks
        SubObj   a cluster that contains several controls, the SubObj might be a control within the cluster,
                 even if the cluster added the shortcut menu item.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Dialog and User Interface\Menu\
        Customizing Shortcut Menus\Customizing Shortcut Menus.vi
    ShortcutShortcut MenuMenu Selection?Selection? (App)(App)

      Generated when the user selects an application item from the shortcut menu. This
       event is posted before the application item is processed by LabVIEW.

     Event Data Fields

      Name    Description

                 Source of the event. LabVIEW UI refers to any built-in user interface event.

        Source
                  0            LabVIEW UI


7880   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7880 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7881 ordinal=7881 -->
## Property and Method Reference

Property and Method Reference


 Name    Description

 Type     Type of event that occurred, such as Mouse Down, Value Change, Timeout, and so on.


 Time     Value of the millisecond timer when the event occurred.


 CtlRef    Reference to the control on which the event occurred.


           Reference to the control shortcut menu that you can modify during this event. MenuRef MenuRef               is valid only during this event case.


        Name of the LabVIEW shortcut menu item the user selected, such as
 ItemTag        APP_SC_COPY_DATA.


          Path of the LabVIEW shortcut menu item that the user selected, such as
 ItemPath        APP_SC_VISIBLE_ITEMS:APP_SC_SCALE_LEGEND.

 Coords

           Reference to the object on which the event occurred. For example, if the user right-clicks
 SubObj   a cluster that contains several controls, the SubObj might be a control within the cluster,
          even if the cluster added the shortcut menu item.

           Allows you to prevent LabVIEW from processing the event, bypassing the behavior
 Discard?
          normally triggered by that event. The default is FALSE.

ValueValue ChangeChange

Generated when the user changes the value of a control. You must read the terminal of
a latched Boolean control in its Value Change event case.

LabVIEW generates this event even if the user enters the same value as the current


                                                    © National Instruments 7881

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7881 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7882 ordinal=7882 -->
## Property and Method Reference

Property and Method Reference

       control value. When used with a slide control, LabVIEW generates all intermediate
       values of the slide each time a user changes the value, including values that register
       before the user releases the mouse.

           Note If you click a combo box control or I/O control but do not change the
               value, LabVIEW generates this event.

     Event Data Fields

      Name   Description

                Source of the event. LabVIEW UI refers to any built-in user interface event.

        Source
                 0            LabVIEW UI


        Type    Type of event that occurred, such as Mouse Down, Value Change, Timeout, and so on.


       Time    Value of the millisecond timer when the event occurred.


         CtlRef   Reference to the control on which the event occurred.


         OldVal   Value of the control before the data change.


        NewVal  Value of the control after the data change.

   ColorBoxColorBox

      ColorBox Properties


7882   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7882 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7883 ordinal=7883 -->
## Property and Method Reference

Property and Method Reference

ColorBoxColorBox PropertiesProperties


 Property              Description

 Allow Transparent         If TRUE, allows the user to select the transparent (T) box in the color picker.

 Color Area Size         Size of the color area in terms of width and height in pixels.

 Color Area Size:Height  Height of the color area in pixels.

 Color Area Size:Width  Width of the color area in pixels.

 Default Value          Gets or sets the default value of the color box.

 Value                 Value of the color box.

 Value (Signaling)       Sets the value of the control and generates a Value Change event.

AllowAllow TransparentTransparent
AllowAllow TransparentTransparent

If TRUE, allows the user to select the transparent (T) box in the color picker.

This property is similar to the Allow Transparent item on the shortcut menu of a color
box control and to the Allow Transparent option on the Appearance page of the
Framed Color Box Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes


                                                    © National Instruments 7883

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7883 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7884 ordinal=7884 -->
## Property and Method Reference

Property and Method Reference


        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   ColorColor AreaArea SizeSize
    ColorColor AreaArea SizeSize

       Size of the color area in terms of width and height in pixels.

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

   ColorColor AreaArea Size:HeightSize:Height
    ColorColor AreaArea Size:HeightSize:Height

       Height of the color area in pixels.

7884   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7884 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7885 ordinal=7885 -->
## Property and Method Reference

Property and Method Reference

This property is an element of the Color Area Size property.

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

ColorColor AreaArea Size:WidthSize:Width
ColorColor AreaArea Size:WidthSize:Width

Width of the color area in pixels.

This property is an element of the Color Area Size property.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes


                                                    © National Instruments 7885

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7885 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7886 ordinal=7886 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   DefaultDefault ValueValue
    DefaultDefault ValueValue

       Gets or sets the default value of the color box.

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


7886   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7886 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7887 ordinal=7887 -->
## Property and Method Reference

Property and Method Reference

ValueValue
ValueValue

Value of the color box.

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

ValueValue (Signaling)(Signaling)
ValueValue (Signaling)(Signaling)

Sets the value of the control and generates a Value Change event.

This property updates the value of an object similar to the Value property. However,
Value (Signaling) also causes LabVIEW to generate an event as if the user had
interactively changed the value of the object. National Instruments recommends you
use this property only when you rely on LabVIEW generating an event in response to
the programmatic value change.

                                                    © National Instruments 7887

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7887 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7888 ordinal=7888 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                               Write Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                                   Yes

         Settable when the VI is running                                            Yes

        Loads the front panel into memory                               No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                   Yes

   BooleanBoolean

      Boolean Properties
   BooleanBoolean PropertiesProperties


        Property    Description

        Boolean    Reference to the Boolean text object. You can use this reference to change the text
         Text          color, font, size, and so on of the Boolean text object.

        Button
                  The width and height of the button in pixels.
         Size

        Button
                    Height of the button in pixels.
         Size:Height

        Button
                   Width of the button in pixels.
         Size:Width

                     Array of up to six (Foreground Color, Background Color) pairs, where Foreground Color
         Colors [4]
                            is the foreground color of the Boolean control and Background Color is the

7888   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7888 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7889 ordinal=7889 -->
## Property and Method Reference

Property and Method Reference


 Property    Description

           background color of the Boolean control. Color pairs include False, True, True to False,
           and False to True. If the Boolean control has hover states, the color pairs will
              additionally include Mouse Over False and Mouse Over True.

 Lock
 Boolean     Indicates whether the Boolean text should be locked in the center of the Boolean
 Text In       object.
 Center

 Mechanical            Mechanical action (0-5) as shown in the shortcut menu from top left to bottom right.
 Action

 Multiple              Specifies whether the Boolean control has multiple text strings. Text String

             Array of up to 4 strings. Strings include text for False, True, True to False, and False to Strings [4]              True.

 Toggle Key             Sets a shortcut key to toggle this control. Binding

BooleanBoolean TextText
BooleanBoolean TextText

Reference to the Boolean text object. You can use this reference to change the text
color, font, size, and so on of the Boolean text object.

You can use this reference with the Text properties.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes


                                                    © National Instruments 7889

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7889 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7890 ordinal=7890 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                                   Yes

         Settable when the VI is running                                  No

        Loads the front panel into memory                               No

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

   ButtonButton SizeSize
   ButtonButton SizeSize

      The width and height of the button in pixels.

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


7890   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7890 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7891 ordinal=7891 -->
## Property and Method Reference

Property and Method Reference

ButtonButton Size:HeightSize:Height
ButtonButton Size:HeightSize:Height

Height of the button in pixels.

This property is an element of the Button Size property.

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

ButtonButton Size:WidthSize:Width
ButtonButton Size:WidthSize:Width

Width of the button in pixels.

This property is an element of the Button Size property.


                                                    © National Instruments 7891

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7891 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7892 ordinal=7892 -->
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

   ColorsColors [4][4]
    ColorsColors [4][4]

       Array of up to six (Foreground Color, Background Color) pairs, where Foreground Color
         is the foreground color of the Boolean control and Background Color is the
      background color of the Boolean control. Color pairs include False, True, True to False,
      and False to True. If the Boolean control has hover states, the color pairs will
       additionally include Mouse Over False and Mouse Over True.

      You can set the color of the front panel object by wiring a hexadecimal number with
       the form RRGGBB or by wiring the color box constant to the property.

       This property is similar to the Colors option on the Appearance page of the Boolean
       Properties dialog box.

           If the Boolean control has four (Foreground Color, Background Color) pairs for the four
        states, this property always returns an array of four (Foreground Color, Background
       Color) pairs when reading. When writing, you can pass in an array of length 1, 2 or 4. If

7892   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7892 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7893 ordinal=7893 -->
## Property and Method Reference

Property and Method Reference

you pass in only one element, this property uses that element value for all four states.
If you pass in two elements, this property uses the first element value for the False and
True to False states. Similarly, this property uses the second element for the True and
False to True states.

If the Boolean control has only one (Foreground Color, Background Color) pair for all
four states, this property returns an array of one (Foreground Color, Background Color)
pair when reading, and uses the first array element when writing. You cannot change a
Boolean control with one (Foreground Color, Background Color) pair to a Boolean
control with multiple (Foreground Color, Background Color) pairs.

This property only uses the True to False and False to True states when you set the
Boolean control to latch or switch when released. You can get and set these
(Foreground Color, Background Color) pairs even if you do not have the control set to
latch or switch when released; they just are not used.

Because this property does not change the data of the Boolean control, you can set it
at any time.

You can use this property for Boolean controls on the Classic, Express, Fuse Design
System, Modern, and Silver palettes. You cannot use this property for Boolean
controls on the System palette.

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


                                                    © National Instruments 7893

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7893 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7894 ordinal=7894 -->
## Property and Method Reference

Property and Method Reference


       Remote access allowed                                                  Yes

   LockLock BooleanBoolean TextText InIn CenterCenter
   LockLock BooleanBoolean TextText InIn CenterCenter

       Indicates whether the Boolean text should be locked in the center of the Boolean
       object.

       This property is similar to the Release Text and Lock Text in Center items on the
       shortcut menu of a Boolean object.

       This property also is similar to the Lock text in center option on the Appearance page
       of the Boolean Properties dialog box.

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


7894   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7894 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7895 ordinal=7895 -->
## Property and Method Reference

Property and Method Reference

MechanicalMechanical ActionAction
MechanicalMechanical ActionAction

Mechanical action (0-5) as shown in the shortcut menu from top left to bottom right.

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

MultipleMultiple TextText StringString
MultipleMultiple TextText StringString

Specifies whether the Boolean control has multiple text strings.

Remarks

The following table lists the characteristics of this property.


 Data type

                                                    © National Instruments 7895

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7895 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7896 ordinal=7896 -->
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

    StringsStrings [4][4]
    StringsStrings [4][4]

       Array of up to 4 strings. Strings include text for False, True, True to False, and False to
       True.

           If you set the Boolean control to allow multiple strings, this property always returns an
       array of four strings when reading. When writing, you can pass in an array of length 1, 2
       or 4. If you pass in only one element, this property uses that element value for all four
        states. If you pass in two elements, this property uses the first element value for the
       False and True to False states. Similarly, this property uses the second element for the
       True and False to True states.

           If you do not set the Boolean control to allow multiple strings, this property returns an
       array of one string when reading, and uses the first array element when writing.

       This property only uses the True to False and False to True states when you set the
      Boolean control to latch or switch when released. You can get and set these strings
      even if you do not have the control set to latch or switch when released; they just are
       not used.


7896   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7896 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7897 ordinal=7897 -->
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

ToggleToggle KeyKey BindingBinding
ToggleToggle KeyKey BindingBinding

Sets a shortcut key to toggle this control.

This property is similar to the Toggle option on the Key Navigation page of the
Boolean Properties dialog box.

Elements

 Name   Description

 Focus     If TRUE, the shortcut key toggles and navigates to this control.

 Control  If TRUE, the keyboard shortcut includes the <Ctrl> key.

 Shift       If TRUE, the keyboard shortcut includes the <Shift> key.

        The name of the shortcut key. (Mac OS X) LabVIEW does not support <VolumeUp>,
 Key
        <VolumeDown>, and function keys <F15> to <F24> as shortcut keys on Mac OS X. Key must


                                                    © National Instruments 7897

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7897 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7898 ordinal=7898 -->
## Property and Method Reference

Property and Method Reference


      Name   Description

               match one of the following values:

                            • <
                      Clear
                   >
                            • <
                       Ins
                   >
                            • <
                     Del
                   >
                            • <
               Home
                   >
                            • <
                  End
                   >
                            • <
                  PageUp
                   >
                            • <
                 PageDown
                   >
                            • <
                    Escape
                   >
                            • <
                     Enter
                   >

                      Note The <Enter> key on the alphanumeric keyboard and <Enter> key on
                              the numeric keypad are the same value.

                            • <
                     Play
                   >
                            • <
                  VolumeUp
                   >
                            • <
                 VolumeDown


7898   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7898 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7899 ordinal=7899 -->
## Property and Method Reference

Property and Method Reference


 Name   Description

            >
                 • <
            Mute
            >
                 • F1
                 • F2
                 • F3
                 • F4
                 • F5
                 • F6
                 • F7
                 • F8
                 • F9
                 • F10
                 • F11
                 • F12
                 • F13
                 • F14
                 • F15
                 • F16
                 • F17
                 • F18
                 • F19
                 • F20
                 • F21
                 • F22
                 • F23
                 • F24

             Note You must use the English Key name when wiring a shortcut key value.


Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

                                                    © National Instruments 7899

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7899 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7900 ordinal=7900 -->
## Property and Method Reference

Property and Method Reference


         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   RefNumRefNum
   TypedRefNumTypedRefNum

      TypedRefNum Properties
   TypedRefNumTypedRefNum PropertiesProperties
   TypedRefNumTypedRefNum PropertiesProperties


        Property                  Description

        Element                  Reference to the element.

   ElementElement
   ElementElement

       Reference to the element.

      You can use this reference with the Control properties.


7900   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7900 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7901 ordinal=7901 -->
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

DataValRefNumDataValRefNum
DataValRefNumDataValRefNum

DataValRefNum Properties
DataValRefNumDataValRefNum PropertiesProperties
DataValRefNumDataValRefNum PropertiesProperties


 Property  Description

          Gets or sets whether the data value reference is an external data value reference. You
 Is
           also can change a data value reference to an external data value reference by right-
 External
            clicking the data value reference and selecting External from the shortcut menu.


                                                    © National Instruments 7901

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7901 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7902 ordinal=7902 -->
## Property and Method Reference

Property and Method Reference

    IsIs ExternalExternal
     IsIs ExternalExternal

       Gets or sets whether the data value reference is an external data value reference. You
       also can change a data value reference to an external data value reference by right-
        clicking the data value reference and selecting External from the shortcut menu.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read/Write

         Available in Run-Time Engine                                        Yes (Read Only)

         Available in Real-Time Operating System                      No

         Settable when the VI is running                             No

        Loads the front panel into memory                                  Yes

       Need to authenticate before use                            No

        Loads the block diagram into memory                               Yes

       Remote access allowed                                             Yes

   LVObjectRefNumLVObjectRefNum
   VIRefNumVIRefNum
   VIRefNumVIRefNum

      VIRefNum Methods


7902   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7902 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7903 ordinal=7903 -->
## Property and Method Reference

Property and Method Reference

VIRefNum Properties
VIRefNumVIRefNum MethodsMethods
VIRefNumVIRefNum MethodsMethods


 Method             Description

 Make Non-Strict
                    Converts the VI reference into a non-strict VI reference. Reference

 Make Strict         Uses the connector pane pattern of the specified VI to convert the VI reference
 Reference            into a strict VI reference.

 Set Conpane        Sets the connector pane of a VI.

MakeMake Non-StrictNon-Strict ReferenceReference
MakeMake Non-StrictNon-Strict ReferenceReference

Converts the VI reference into a non-strict VI reference.

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                             Yes

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No


                                                    © National Instruments 7903

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7903 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7904 ordinal=7904 -->
## Property and Method Reference

Property and Method Reference


       Remote access allowed                                             Yes

   MakeMake StrictStrict ReferenceReference
   MakeMake StrictStrict ReferenceReference

      Uses the connector pane pattern of the specified VI to convert the VI reference into a
         strict VI reference.

     Parameters

      Name  Data type  Required  Description

          VI Ref             Yes       Reference to the VI whose connector pane pattern you want to use.


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


7904   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7904 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7905 ordinal=7905 -->
## Property and Method Reference

Property and Method Reference

SetSet ConpaneConpane
SetSet ConpaneConpane

Sets the connector pane of a VI.

Parameters

 Name      Data type    Required    Description

 Conpane                  Yes         The connector pane you want the VI to have.


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

VIRefNumVIRefNum PropertiesProperties
VIRefNumVIRefNum PropertiesProperties


                                                    © National Instruments 7905

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7905 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7906 ordinal=7906 -->
## Property and Method Reference

Property and Method Reference


        Property     Description

           Is Strict?     Returns TRUE if the VI reference is a strict type. FALSE otherwise.

    IsIs Strict?Strict?
     IsIs Strict?Strict?

       Returns TRUE if the VI reference is a strict type. FALSE otherwise.

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

   GenClassRefGenClassRef
    LVVariantLVVariant
   PathPath


7906   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7906 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7907 ordinal=7907 -->
## Property and Method Reference

Property and Method Reference

Path Methods

Path Properties
PathPath MethodsMethods


 Method                Description

 Browse for Path       Open a file dialog to allow the user to select a path.

BrowseBrowse forfor PathPath
BrowseBrowse forfor PathPath

Open a file dialog to allow the user to select a path.

Parameters

 Name      Data type   Required    Description

 Cancelled                Yes         Returns TRUE if the user cancelled the file dialog.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                      No

 Settable when the VI is running                                      Yes

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

                                                    © National Instruments 7907

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7907 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7908 ordinal=7908 -->
## Property and Method Reference

Property and Method Reference


        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

      History

            • LabVIEW 2024 Q1: introduced.
   PathPath PropertiesProperties


        Property          Description

                                           If TRUE, the control automatically accepts paths dragged to it, including the
                    LV_PATH data type from drag and drop events. The LV_PATH data type is of
        Allow Dropping    type path. If FALSE, LabVIEW does not automatically accept any drops, including
                        from the operating system, at run time. LabVIEW returns error 1157 if you set
                               this property on an indicator.

        Browse Button    Returns the coordinates of the rectangle that encloses the browse button for
         Rect              the path control.

        Browse                             Specifies whether the browse button of a path control can be operated.         Button:Disabled

        Browse                             Specifies if the path control browse button is visible.         Button:Visible

                           Set or get the file dialog box options. The options include prompt, mode, start        Browse Options                            path, and button text.

        Browse
                             Specifies the label to display in the file dialog box for the accept or OK button. If
         Options:Button
                       you do not specify a label, the button text defaults to OK.
         Text

        Browse
        Options:Match     Set or get the match pattern string of the browse dialog box.
         Pattern

        Browse
                          Label to display in the file dialog box next to the custom pattern. Use the
         Options:Pattern
                       Browse Options:Match Pattern property to set a custom pattern.
         Label

        Browse
                           Set or get the prompt string of the browse dialog box.
        Options:Prompt


7908   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7908 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7909 ordinal=7909 -->
## Property and Method Reference

Property and Method Reference


 Property          Description

 Browse
 Options:Selection  Set or get the selection mode of the browse dialog box.
 Mode

 Browse
 Options:Start      Set or get the start path of browse dialog box.
 Path

 Default Value      Gets or sets the default value of the path control.

 Path Text         Reference to the path text.

                    Specifies how to display a path that is too long to fit in the path control or Path Too Long To                      indicator. LabVIEW applies the value of this property only if the scrollbar of the Fit                    control or indicator is hidden.

 Scrollbar Visible   Displays a vertical scroll bar for a path object.

 Shows            Returns whether the referenced path control or indicator is currently
 Abbreviated       abbreviating the path. This property returns FALSE if the object is set to clip the
 Behavior?         path, if the scrollbar is visible, or if the path fits in the path object.

                 Width and height in pixels of the frame around the text area of the path control, Size                  not including the browse button.

 Size:Height       Height of the path control in pixels.

 Size:Width        Width of the path control in pixels.

 Value             Value of the path control.

 Value (Signaling)   Sets the value of the control and generates a Value Change event.

AllowAllow DroppingDropping
AllowAllow DroppingDropping

If TRUE, the control automatically accepts paths dragged to it, including the LV_PATH
data type from drag and drop events. The LV_PATH data type is of type path. If FALSE,
LabVIEW does not automatically accept any drops, including from the operating
system, at run time. LabVIEW returns error 1157 if you set this property on an indicator.

Use the Control events for more control over how users drag items within controls.

                                                    © National Instruments 7909

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7909 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7910 ordinal=7910 -->
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

   BrowseBrowse ButtonButton RectRect
   BrowseBrowse ButtonButton RectRect

       Returns the coordinates of the rectangle that encloses the browse button for the path
        control.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                                   Yes

         Settable when the VI is running                                  No


7910   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7910 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7911 ordinal=7911 -->
## Property and Method Reference

Property and Method Reference


 Loads the front panel into memory                               No

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

BrowseBrowse Button:DisabledButton:Disabled
BrowseBrowse Button:DisabledButton:Disabled

Specifies whether the browse button of a path control can be operated.

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

BrowseBrowse Button:VisibleButton:Visible
BrowseBrowse Button:VisibleButton:Visible

Specifies if the path control browse button is visible.

                                                    © National Instruments 7911

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7911 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7912 ordinal=7912 -->
## Property and Method Reference

Property and Method Reference

       This property is similar to the Visible Items»Browse Button item on the shortcut menu
       of a path control and Show browse button checkbox on the Appearance page of the
      Path Properties dialog box.

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

   BrowseBrowse OptionsOptions
   BrowseBrowse OptionsOptions

       Set or get the file dialog box options. The options include prompt, mode, start path,
      and button text.

       This property is similar to the options on the Browse Options page of the Path
       Properties dialog box.

     Elements

      Name    Description

       Prompt   Sets or gets the prompt string of the browse dialog box.


7912   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7912 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7913 ordinal=7913 -->
## Property and Method Reference

Property and Method Reference


 Name    Description

 Match          Sets or gets the match pattern string of the browse dialog box. Pattern

 Select          Sets or gets the selection mode of the browse dialog box. Mode

 Start          Sets or gets the start path of browse dialog box. Path

 Pattern          Label to display in the file dialog box next to the custom pattern. Label

 Button   Specifies the label to display in the file dialog box for the accept or OK button. If you do
 Text     not specify a label, the button text defaults to OK.

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

BrowseBrowse Options:ButtonOptions:Button TextText
BrowseBrowse Options:ButtonOptions:Button TextText

Specifies the label to display in the file dialog box for the accept or OK button. If you do

                                                    © National Instruments 7913

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7913 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7914 ordinal=7914 -->
## Property and Method Reference

Property and Method Reference

       not specify a label, the button text defaults to OK.

       This property is similar to the button label parameter in the File Dialog Express VI and
       the Button Text option on the Browse Options page of the Path Properties dialog box.

       This property is an element of the Browse Options property.

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

   BrowseBrowse Options:MatchOptions:Match PatternPattern
   BrowseBrowse Options:MatchOptions:Match PatternPattern

       Set or get the match pattern string of the browse dialog box.

       This property is similar to the pattern parameter in the File Dialog Express VI and the
       Pattern option on the Browse Options page of the Path Properties dialog box.

       This property is an element of the Browse Options property.


7914   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7914 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7915 ordinal=7915 -->
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

BrowseBrowse Options:PatternOptions:Pattern LabelLabel
BrowseBrowse Options:PatternOptions:Pattern LabelLabel

Label to display in the file dialog box next to the custom pattern. Use the Browse
Options:Match Pattern property to set a custom pattern.

This property is similar to the pattern label parameter in the File Dialog Express VI and
the Pattern Label option on the Browse Options page of the Path Properties dialog
box.

This property is an element of the Browse Options property.

Remarks

The following table lists the characteristics of this property.


 Data type


                                                    © National Instruments 7915

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7915 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7916 ordinal=7916 -->
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

   BrowseBrowse Options:PromptOptions:Prompt
   BrowseBrowse Options:PromptOptions:Prompt

       Set or get the prompt string of the browse dialog box.

       This property is similar to the prompt parameter in the File Dialog Express VI and the
      Prompt option on the Browse Options page of the Path Properties dialog box.

       This property is an element of the Browse Options property.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

7916   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7916 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7917 ordinal=7917 -->
## Property and Method Reference

Property and Method Reference


 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

BrowseBrowse Options:SelectionOptions:Selection ModeMode
BrowseBrowse Options:SelectionOptions:Selection ModeMode

Set or get the selection mode of the browse dialog box.

This property is similar to the Selection Mode section in the configuration dialog box
for the File Dialog Express VI and the Selection Mode section on the Browse Options
page of the Path Properties dialog box.

This property is an element of the Browse Options property.

The following table lists the possible file or directory enum values for the Browse
Options:Selection Mode property.

File or Directory
existing file
new file
new or existing file
existing dir
new dir
new or existing dir
existing file (use LLBs)
new file (use LLBs)
new or existing file (use LLBs)
new or existing file or directory (use LLBs)
existing dir (use LLBs)
new dir (use LLBs)
new or existing dir (use LLBs)

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 7917

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7917 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7918 ordinal=7918 -->
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

   BrowseBrowse Options:StartOptions:Start PathPath
   BrowseBrowse Options:StartOptions:Start PathPath

       Set or get the start path of browse dialog box.

       This property is similar to the start path parameter in the File Dialog Express VI and the
       Start Path option on the Browse Options page of the Path Properties dialog box.

       This property is an element of the Browse Options property.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

7918   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7918 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7919 ordinal=7919 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

DefaultDefault ValueValue
DefaultDefault ValueValue

Gets or sets the default value of the path control.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read/Write

 Available in Run-Time Engine                                        Yes (Read Only)

 Available in Real-Time Operating System                             Yes

 Settable when the VI is running                             No

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

PathPath TextText
PathPath TextText

Reference to the path text.


                                                    © National Instruments 7919

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7919 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7920 ordinal=7920 -->
## Property and Method Reference

Property and Method Reference

      You can use this reference with the Text properties.

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

   PathPath TooToo LongLong ToTo FitFit
   PathPath TooToo LongLong ToTo FitFit

       Specifies how to display a path that is too long to fit in the path control or indicator.
      LabVIEW applies the value of this property only if the scrollbar of the control or
       indicator is hidden.

      You also can use the Path too long to fit pull-down menu on the Appearance page of
       the Properties dialog box to specify how to display long paths.

     Remarks

      The following table lists the characteristics of this property.


        Data type


7920   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7920 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7921 ordinal=7921 -->
## Property and Method Reference

Property and Method Reference


 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

ScrollbarScrollbar VisibleVisible
ScrollbarScrollbar VisibleVisible

Displays a vertical scroll bar for a path object.

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


                                                    © National Instruments 7921

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7921 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7922 ordinal=7922 -->
## Property and Method Reference

Property and Method Reference

   ShowsShows AbbreviatedAbbreviated Behavior?Behavior?
   ShowsShows AbbreviatedAbbreviated Behavior?Behavior?

       Returns whether the referenced path control or indicator is currently abbreviating the
       path. This property returns FALSE if the object is set to clip the path, if the scrollbar is
        visible, or if the path fits in the path object.

       This property is similar to the Path too long to fit pull-down menu on the Appearance
      page of the Properties dialog box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                                   Yes

         Settable when the VI is running                                            Yes

        Loads the front panel into memory                                         Yes

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

    SizeSize
    SizeSize

      Width and height in pixels of the frame around the text area of the path control, not
       including the browse button.

7922   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7922 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7923 ordinal=7923 -->
## Property and Method Reference

Property and Method Reference

This property is similar to the Size Height and Size Width options on the Appearance
page of the Properties dialog box.

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

Size:HeightSize:Height
Size:HeightSize:Height

Height of the path control in pixels.

This property is an element of the Size property. This property is similar to the Size
Height and Size Width options on the Appearance page of the Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write


                                                    © National Instruments 7923

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7923 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7924 ordinal=7924 -->
## Property and Method Reference

Property and Method Reference


         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   Size:WidthSize:Width
    Size:WidthSize:Width

      Width of the path control in pixels.

       This property is an element of the Size property. This property is similar to the Size
      Width option on the Appearance page of the Properties dialog box.

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


7924   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7924 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7925 ordinal=7925 -->
## Property and Method Reference

Property and Method Reference

ValueValue
ValueValue

Value of the path control.

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

ValueValue (Signaling)(Signaling)
ValueValue (Signaling)(Signaling)

Sets the value of the control and generates a Value Change event.

This property updates the value of an object similar to the Value property. However,
Value (Signaling) also causes LabVIEW to generate an event as if the user had
interactively changed the value of the object. National Instruments recommends you
use this property only when you rely on LabVIEW generating an event in response to
the programmatic value change.

                                                    © National Instruments 7925

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7925 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7926 ordinal=7926 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                               Write Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                                   Yes

         Settable when the VI is running                                            Yes

        Loads the front panel into memory                               No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                   Yes

    ListBoxListBox

       ListBox Methods

       ListBox Properties

       ListBox Events
    ListBoxListBox MethodsMethods


       Method         Description

       Custom Item    Returns the item symbol as a cluster of image data so you can draw it as a picture
        Symbols:Get    using the Draw Flattened Pixmap VI or save the image to a file using the Graphics
       Symbol        Formats VIs.

       Custom Item    Returns the item symbols as an array of clusters of image data so you can draw
        Symbols:Get    them as pictures using the Draw Flattened Pixmap VI or save the images to files
       Symbol Array    using the Graphics Formats VIs.


7926   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7926 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7927 ordinal=7927 -->
## Property and Method Reference

Property and Method Reference


 Method         Description

 Custom Item
 Symbols:Revert                 Resets all item symbols to the default symbols. All To Built In
 Symbols

 Custom Item
 Symbols:Revert                 Resets an item symbol to the default symbol for its index. To Built In
 Symbol

 Custom Item
 Symbols:Set To                 Sets the image of an item symbol. Custom
 Symbol

 Custom Item
 Symbols:Set To                 Sets the images of all item symbols. Custom
 Symbol Array

                Gets the row number the user double-clicked. The first row on the top is
 Get Double-    numbered zero. A value of –2 means that no row has been double-clicked. After
 Clicked Row      this method reads the value, it changes the value back to –2. This method does
                not respond to a double-click on the header.

                Converts a pixel coordinate to a row in the coordinates of the control. This
 Point to Row    method also returns whether the point is inside the bounds of the content
                 rectangle and whether the point is within the custom symbol of the cell.

CustomCustom ItemItem Symbols:GetSymbols:Get SymbolSymbol
CustomCustom ItemItem Symbols:GetSymbols:Get SymbolSymbol

Returns the item symbol as a cluster of image data so you can draw it as a picture
using the Draw Flattened Pixmap VI or save the image to a file using the Graphics
Formats VIs.

The cluster returned by this method is similar to the image data output of the Read
JPEG File, Read PNG File, and Read BMP File VIs.


                                                    © National Instruments 7927

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7927 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7928 ordinal=7928 -->
## Property and Method Reference

Property and Method Reference

     Parameters

      Name  Data type  Required  Description

         Index              Yes       The index of the symbol whose image data you want to obtain.


     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                                      Yes

         Available in Real-Time Operating System                                            Yes

         Settable when the VI is running                                                    Yes

        Loads the front panel into memory                                     No

       Need to authenticate before use                                       No

        Loads the block diagram into memory                                   No

       Remote access allowed                                                           Yes

   CustomCustom ItemItem Symbols:GetSymbols:Get SymbolSymbol ArrayArray
   CustomCustom ItemItem Symbols:GetSymbols:Get SymbolSymbol ArrayArray

       Returns the item symbols as an array of clusters of image data so you can draw them
       as pictures using the Draw Flattened Pixmap VI or save the images to files using the
       Graphics Formats VIs.

      The clusters returned by this method are similar to the image data output of the Read
      JPEG File, Read PNG File, and Read BMP File VIs.


7928   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7928 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7929 ordinal=7929 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this method.


 Data type

 Available in Run-Time Engine                                                      Yes

 Available in Real-Time Operating System                                            Yes

 Settable when the VI is running                                                    Yes

 Loads the front panel into memory                                     No

 Need to authenticate before use                                       No

 Loads the block diagram into memory                                   No

 Remote access allowed                                                           Yes

CustomCustom ItemItem Symbols:RevertSymbols:Revert AllAll ToTo BuiltBuilt
InIn SymbolsSymbols
CustomCustom ItemItem Symbols:RevertSymbols:Revert AllAll ToTo BuiltBuilt InIn
SymbolsSymbols

Resets all item symbols to the default symbols.

You can use a listbox symbol ring constant to view the default item symbols.

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                             Yes

                                                    © National Instruments 7929

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7929 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7930 ordinal=7930 -->
## Property and Method Reference

Property and Method Reference


         Settable when the VI is running                                      Yes

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

   CustomCustom ItemItem Symbols:RevertSymbols:Revert ToTo BuiltBuilt InIn
   SymbolSymbol
   CustomCustom ItemItem Symbols:RevertSymbols:Revert ToTo BuiltBuilt InIn
   SymbolSymbol

       Resets an item symbol to the default symbol for its index.

     Parameters

              Data      Name       Required  Description               type

                           The index of the symbol you want to set. The default is 0. You also can
         Index        Yes       wire a listbox symbol ring constant to this parameter to select the custom
                              item symbol you want to replace with a default item symbol.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                             Yes


7930   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7930 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7931 ordinal=7931 -->
## Property and Method Reference

Property and Method Reference


 Settable when the VI is running                                      Yes

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

CustomCustom ItemItem Symbols:SetSymbols:Set ToTo CustomCustom
SymbolSymbol
CustomCustom ItemItem Symbols:SetSymbols:Set ToTo CustomCustom
SymbolSymbol

Sets the image of an item symbol.

If you want to use a picture to set the symbol, use the Picture to Pixmap VI to convert
the data to an image data cluster before using this method. The image cluster you wire
to this method is similar to the image data input of the Write JPEG File, Write PNG File,
and Write BMP File VIs.

Parameters

       Data
 Name       Required  Description
        type

                     The index of the symbol you want to set. The default is 0. You also can
 Index        Yes       wire a listbox symbol ring constant to this parameter to select the custom
                       item symbol you want to replace with a default item symbol.


                        Describes the image you want to use for the item symbol. Images that are
 Image        Yes        less than or equal to 16 × 16 pixels appear as their actual size. If you use
                     an image that is larger than 16 × 16 pixels, LabVIEW shrinks the image to


                                                    © National Instruments 7931

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7931 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7932 ordinal=7932 -->
## Property and Method Reference

Property and Method Reference


               Data      Name       Required  Description
               type

                             16 × 16 pixels before displaying it as a listbox control item symbol.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                                      Yes

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

   CustomCustom ItemItem Symbols:SetSymbols:Set ToTo CustomCustom
   SymbolSymbol ArrayArray
   CustomCustom ItemItem Symbols:SetSymbols:Set ToTo CustomCustom
   SymbolSymbol ArrayArray

       Sets the images of all item symbols.

           If you want to use a picture to set the symbols, use the Picture to Pixmap VI to convert
       the data to an image data cluster before using this method. The image clusters you
       wire to this method are similar to the image data input of the Write JPEG File, Write
     PNG File, and Write BMP File VIs.

7932   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7932 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7933 ordinal=7933 -->
## Property and Method Reference

Property and Method Reference

Parameters

         Data Name         Required  Description
          type

                      An array of clusters that describe the images you want to use for the
                         item symbols. Images that are less than or equal to 16 × 16 pixels
 Symbols        Yes       appear as their actual size. If you use an image that is larger than 16 ×
                        16 pixels, LabVIEW shrinks the image to 16 × 16 pixels before displaying
                                         it as a tree control item symbol.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                             Yes

 Settable when the VI is running                                      Yes

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

GetGet Double-ClickedDouble-Clicked RowRow
GetGet Double-ClickedDouble-Clicked RowRow

Gets the row number the user double-clicked. The first row on the top is numbered
zero. A value of –2 means that no row has been double-clicked. After this method reads
the value, it changes the value back to –2. This method does not respond to a double-
click on the header.


                                                    © National Instruments 7933

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7933 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7934 ordinal=7934 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this method.


        Data type

         Available in Run-Time Engine                                                      Yes

         Available in Real-Time Operating System                                            Yes

         Settable when the VI is running                                                    Yes

        Loads the front panel into memory                                                 Yes

       Need to authenticate before use                                       No

        Loads the block diagram into memory                                   No

       Remote access allowed                                                           Yes

   PointPoint toto RowRow
    PointPoint toto RowRow

       Converts a pixel coordinate to a row in the coordinates of the control. This method also
       returns whether the point is inside the bounds of the content rectangle and whether
       the point is within the custom symbol of the cell.

     Parameters

                 Data
      Name             Required  Description
                  type

         Point              Yes        Specifies the pixel coordinate to translate into a row.


          In                           Returns TRUE if the point is inside the bounds of the content
                            Yes
        Bounds?                       rectangle.


7934   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7934 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7935 ordinal=7935 -->
## Property and Method Reference

Property and Method Reference


          Data Name             Required  Description
          type

 Row               Yes       Returns the row of the cell in which the point lies.


 In                           Returns TRUE if the point is within the bounds of the custom                    Yes Symbol?                   symbol of the cell.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                             Yes

 Settable when the VI is running                                      Yes

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

ListBoxListBox PropertiesProperties


 Property         Description

 Active
                  Sets the active row. A value of –1 indicates the column header. A value of –2
 Row:Active Row
                   indicates all rows.
 Number

 Active
               The coordinate in pixels, relative to the origin of the owning pane, of the top-left
 Row:Active Row
                   position of the active row(s).
 Position

 Active          The coordinate in pixels, relative to the origin of the owning pane, of the left edge

                                                    © National Instruments 7935

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7935 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7936 ordinal=7936 -->
## Property and Method Reference

Property and Method Reference


        Property         Description

         Row:Active Row                            of the active row.          Position:Left

         Active                      The coordinate in pixels, relative to the origin of the owning pane, of the top edge         Row:Active Row                            of the active row.
         Position:Top

         Active Row:Cell
        Background     The background color of the active cell(s).
         Color

         Active Row:Cell                      The font of the active cell in the listbox control.        Font

         Active Row:Cell                           Indicates whether the text in the active cell is bold.
         Font:Bold

         Active Row:Cell                      The text font color in the active cell.
         Font:Color

         Active Row:Cell                           Indicates whether the text in the active cell is italic.
          Font:Italic

         Active Row:Cell  The name of the font in the active cell. Predefined font names include App
        Font:Name      Font, Sys Font, and Dlg Font.

         Active Row:Cell
                      The size of the font in the active cell.         Font:Size

         Active Row:Cell
                           Indicates whether to strike out the text in the active cell.         Font:Strikeout

         Active Row:Cell
                           Indicates whether the text in the active cell is underlined.         Font:Underline

         Active Row:Cell
                      The height of the active cell(s) in pixels.
        Height

         Active Row:Cell
                         Gets or sets the justification of text within the active row of the listbox.
          Justification

                                          If TRUE, users can edit non-header cells in the listbox at run time by clicking the
        Allow Editing
                                cell text and then clicking the text a second time after a short pause. If FALSE,
          Cells
                          users cannot edit non-header cells.

         Autosizing Row   Determines whether the rows autosize their height to display all text when fonts
        Height          change or when the number of lines in a cell changes.


7936   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7936 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7937 ordinal=7937 -->
## Property and Method Reference

Property and Method Reference


Property         Description

Column Header               The string in the column header.String

Content Rect               The size in pixels of the content rectangle of the listbox control.Bounds

Content Rect               The height in pixels of the content rectangle of the listbox control.Bounds:Height

Content Rect               The width in pixels of the content rectangle of the listbox control.Bounds:Width

Content Rect    The coordinate in pixels, relative to the origin of the owning pane, of the top-left
Position          position of the content rectangle of the listbox control.

Content Rect    The coordinate in pixels, relative to the origin of the owning pane, of the left edge
Position:Left      of the content rectangle of the listbox control.

Content Rect    The coordinate in pixels, relative to the origin of the owning pane, of the top edge
Position:Top      of the content rectangle of the listbox control.

Disabled Items   Array of indexes of disabled items (first item is 0).

Drag/
Drop:Allow Drag   If TRUE, this enables the control to drag items to other controls and accept drags
and Drop        from other controls.
Outside Control

Drag/                   If TRUE, LabVIEW automatically begins a drag and drop operation from the
Drop:Allow       control when you use the Operating tool to select and drag an item from the
Dragging          control.

                            If TRUE, LabVIEW automatically accepts drops containing the LV_LISTBOX,
              LV_TEXT, or LV_LISTBOX_ITEMS data types. The LV_LISTBOX data type is
               a cluster that contains an array of strings from the row that you are dragging
Drag/             data, and a numeric indicating the glyph associated with the row from which you
Drop:Allow       are dragging. The LV_TEXT data type is of type string. The
Dropping      LV_LISTBOX_ITEMS data type is an array of a cluster containing an array of
                    strings, from left to right, in the item you are dragging and an integer
                 representing the glyph index associated with the item from which you are
                 dragging data.

                 Sets the default behavior for a drag and drop operation for the control. The
Drag/Drop:Drag
                   settings apply only when the control configured is the source of the drag and
Mode
               drop operation.


                                                    © National Instruments 7937

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7937 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7938 ordinal=7938 -->
## Property and Method Reference

Property and Method Reference


        Property         Description

                      The row of the current text entry. A value of 0 indicates the top row. A value of –1
                            indicates the column header. A value of –2 indicates that no edits are being made
                           to the text of the control.         Edit Row
                         Before you use this property to set text focus on a control, set key focus of the
                            control.

                      The row that has focus, used as the basis for key navigation such as the up and        Focus Row                    down arrows.

           Is Array?         Returns TRUE if the listbox has an array data type.

        Item Names      Array of the strings for the selectable items.

                          Array of item symbols. Item symbols (0-40) are as shown in the listbox symbol
        Item Symbols                            ring constant.

                          Sets how to handle upper and lowercase characters when you type characters in
        Keyboard Mode  a listbox at run time. Valid values include 0 (System Default), 1 (Case Sensitive),
                      and 2 (Case Insensitive).

                                          If TRUE, you can enter multiple lines of text in the listbox cells by pressing the
                         <Enter> key on the keyboard. If FALSE, pressing the <Enter> key on the keyboard
         Multiple Line                          while editing cells causes LabVIEW to commit the edits in the current cell and         Input
                    move the text focus to the next cell. This property does not affect run-time
                         behavior of the listbox.

       Number of Rows Number of visible items in the listbox. This property counts partially visible rows.

         Select Entire                           Highlights the entire row if you select a row in the tree.
       Rows

         Selection Color   Color used to draw the data selection.

                    Number of items the user can select. Valid values include 0 (zero or one), 1 (one),
         Selection Mode
                       2 (zero or more), and 3 (one or more).

         Size           The width and height in pixels of the listbox control.

         Size:Height      The height of the listbox control in pixels.

         Size:Width      The width of the listbox control in pixels.

                   Row number currently at the top of the listbox. The number of visible items in the
        Top Row
                             listbox does not limit the row number you can select for this property.

          Visible                  If TRUE, displays the column header.

7938   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7938 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7939 ordinal=7939 -->
## Property and Method Reference

Property and Method Reference


 Property         Description

 Items:Column
 Header Visible

 Visible
 Items:Horizontal  If TRUE, displays horizontal lines that separate rows in the listbox.
 Lines Visible

 Visible
 Items:Symbols     If TRUE, displays the item symbols.
 Visible

 Visible
 Items:Vertical       If TRUE, displays the vertical scroll bar.
 Scrollbar Visible

ActiveActive Row:ActiveRow:Active RowRow NumberNumber
ActiveActive Row:ActiveRow:Active RowRow NumberNumber

Sets the active row. A value of –1 indicates the column header. A value of –2 indicates
all rows.

The active row is the row of a listbox to which you can apply property changes. The
active row is not the same as the selected row and the active row does not change if
you manually select a different row.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes


                                                    © National Instruments 7939

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7939 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7940 ordinal=7940 -->
## Property and Method Reference

Property and Method Reference


        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   ActiveActive Row:ActiveRow:Active RowRow PositionPosition
    ActiveActive Row:ActiveRow:Active RowRow PositionPosition

      The coordinate in pixels, relative to the origin of the owning pane, of the top-left
       position of the active row(s).

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                                   Yes

         Settable when the VI is running                                  No

        Loads the front panel into memory                                         Yes

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes


7940   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7940 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7941 ordinal=7941 -->
## Property and Method Reference

Property and Method Reference

ActiveActive Row:ActiveRow:Active RowRow Position:LeftPosition:Left
ActiveActive Row:ActiveRow:Active RowRow Position:LeftPosition:Left

The coordinate in pixels, relative to the origin of the owning pane, of the left edge of
the active row.

This property is an element of the Active Row:Active Row Position property.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

 Settable when the VI is running                                  No

 Loads the front panel into memory                                         Yes

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

ActiveActive Row:ActiveRow:Active RowRow Position:TopPosition:Top
ActiveActive Row:ActiveRow:Active RowRow Position:TopPosition:Top

The coordinate in pixels, relative to the origin of the owning pane, of the top edge of
the active row.

This property is an element of the Active Row:Active Row Position property.


                                                    © National Instruments 7941

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7941 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7942 ordinal=7942 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                                   Yes

         Settable when the VI is running                                  No

        Loads the front panel into memory                                         Yes

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

   ActiveActive Row:CellRow:Cell BackgroundBackground ColorColor
    ActiveActive Row:CellRow:Cell BackgroundBackground ColorColor

      The background color of the active cell(s).

      You can set the color of the front panel object by wiring a hexadecimal number with
       the form RRGGBB or by wiring the color box constant to the property.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes


7942   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7942 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7943 ordinal=7943 -->
## Property and Method Reference

Property and Method Reference


 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

ActiveActive Row:CellRow:Cell FontFont
ActiveActive Row:CellRow:Cell FontFont

The font of the active cell in the listbox control.

Use this property to change the size, style, or color of the cell font. You cannot use this
property with a strict type definition.

Elements

 Name          Description

 Size          The size of the font in the active cell.

 Bold            Indicates whether the text in the active cell is bold.

 Italic            Indicates whether the text in the active cell is italic.

 Underline       Indicates whether the text in the active cell is underlined.

 Strikeout       Indicates whether to strike out the text in the active cell.

 Color         The text font color in the active cell.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write


                                                    © National Instruments 7943

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7943 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7944 ordinal=7944 -->
## Property and Method Reference

Property and Method Reference


         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   ActiveActive Row:CellRow:Cell Font:BoldFont:Bold
    ActiveActive Row:CellRow:Cell Font:BoldFont:Bold

       Indicates whether the text in the active cell is bold.

       This property is an element of the Active Row:Cell Font property.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes


7944   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7944 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7945 ordinal=7945 -->
## Property and Method Reference

Property and Method Reference

ActiveActive Row:CellRow:Cell Font:ColorFont:Color
ActiveActive Row:CellRow:Cell Font:ColorFont:Color

The text font color in the active cell.

This property is an element of the Active Row:Cell Font property.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

ActiveActive Row:CellRow:Cell Font:ItalicFont:Italic
ActiveActive Row:CellRow:Cell Font:ItalicFont:Italic

Indicates whether the text in the active cell is italic.

This property is an element of the Active Row:Cell Font property.


                                                    © National Instruments 7945

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7945 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7946 ordinal=7946 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   ActiveActive Row:CellRow:Cell Font:NameFont:Name
    ActiveActive Row:CellRow:Cell Font:NameFont:Name

      The name of the font in the active cell. Predefined font names include App Font,
     Sys Font, and Dlg Font.

       This property is an element of the Active Row:Cell Font property.

           If you select an invalid font, this property returns an error.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

7946   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7946 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7947 ordinal=7947 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

ActiveActive Row:CellRow:Cell Font:SizeFont:Size
ActiveActive Row:CellRow:Cell Font:SizeFont:Size

The size of the font in the active cell.

This property is an element of the Active Row:Cell Font property.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes


                                                    © National Instruments 7947

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7947 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7948 ordinal=7948 -->
## Property and Method Reference

Property and Method Reference

   ActiveActive Row:CellRow:Cell Font:StrikeoutFont:Strikeout
    ActiveActive Row:CellRow:Cell Font:StrikeoutFont:Strikeout

       Indicates whether to strike out the text in the active cell.

       This property is an element of the Active Row:Cell Font property.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   ActiveActive Row:CellRow:Cell Font:UnderlineFont:Underline
    ActiveActive Row:CellRow:Cell Font:UnderlineFont:Underline

       Indicates whether the text in the active cell is underlined.

       This property is an element of the Active Row:Cell Font property.


7948   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7948 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7949 ordinal=7949 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

ActiveActive Row:CellRow:Cell HeightHeight
ActiveActive Row:CellRow:Cell HeightHeight

The height of the active cell(s) in pixels.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No


                                                    © National Instruments 7949

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7949 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7950 ordinal=7950 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   ActiveActive Row:CellRow:Cell JustificationJustification
    ActiveActive Row:CellRow:Cell JustificationJustification

       Gets or sets the justification of text within the active row of the listbox.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   AllowAllow EditingEditing CellsCells
   AllowAllow EditingEditing CellsCells

           If TRUE, users can edit non-header cells in the listbox at run time by clicking the cell
        text and then clicking the text a second time after a short pause. If FALSE, users cannot

7950   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7950 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7951 ordinal=7951 -->
## Property and Method Reference

Property and Method Reference

edit non-header cells.

This property is similar to the Editable Cells item on the shortcut menu of a listbox.

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

AutosizingAutosizing RowRow HeightHeight
AutosizingAutosizing RowRow HeightHeight

Determines whether the rows autosize their height to display all text when fonts
change or when the number of lines in a cell changes.

If FALSE, you can have clipped text in cells, and the user will be unable to manually
resize the row height at run time to see all of the text. This property affects only user
input. If you use the Value property to set the listbox strings, the rows do not
automatically resize. To resize the rows, set this property to FALSE and then set it back
to TRUE.

This property is similar to the Autosize Row Height item on the shortcut menu of a
single-column listbox.

                                                    © National Instruments 7951

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7951 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7952 ordinal=7952 -->
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

   ColumnColumn HeaderHeader StringString
   ColumnColumn HeaderHeader StringString

      The string in the column header.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No


7952   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7952 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7953 ordinal=7953 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

ContentContent RectRect BoundsBounds
ContentContent RectRect BoundsBounds

The size in pixels of the content rectangle of the listbox control.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

 Settable when the VI is running                                  No

 Loads the front panel into memory                                         Yes

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

ContentContent RectRect Bounds:HeightBounds:Height
ContentContent RectRect Bounds:HeightBounds:Height

The height in pixels of the content rectangle of the listbox control.


                                                    © National Instruments 7953

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7953 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7954 ordinal=7954 -->
## Property and Method Reference

Property and Method Reference

       This property is an element of the Content Rect Bounds property.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                                   Yes

         Settable when the VI is running                                  No

        Loads the front panel into memory                                         Yes

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

   ContentContent RectRect Bounds:WidthBounds:Width
   ContentContent RectRect Bounds:WidthBounds:Width

      The width in pixels of the content rectangle of the listbox control.

       This property is an element of the Content Rect Bounds property.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes


7954   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7954 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7955 ordinal=7955 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                                   Yes

 Settable when the VI is running                                  No

 Loads the front panel into memory                                         Yes

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

ContentContent RectRect PositionPosition
ContentContent RectRect PositionPosition

The coordinate in pixels, relative to the origin of the owning pane, of the top-left
position of the content rectangle of the listbox control.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

 Settable when the VI is running                                  No

 Loads the front panel into memory                                         Yes

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes


                                                    © National Instruments 7955

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7955 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7956 ordinal=7956 -->
## Property and Method Reference

Property and Method Reference

   ContentContent RectRect Position:LeftPosition:Left
   ContentContent RectRect Position:LeftPosition:Left

      The coordinate in pixels, relative to the origin of the owning pane, of the left edge of
       the content rectangle of the listbox control.

       This property is an element of the Content Rect Position property.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                                   Yes

         Settable when the VI is running                                  No

        Loads the front panel into memory                                         Yes

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

       Remote access allowed                                                   Yes

   ContentContent RectRect Position:TopPosition:Top
   ContentContent RectRect Position:TopPosition:Top

      The coordinate in pixels, relative to the origin of the owning pane, of the top edge of
       the content rectangle of the listbox control.

       This property is an element of the Content Rect Position property.


7956   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7956 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7957 ordinal=7957 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

 Settable when the VI is running                                  No

 Loads the front panel into memory                                         Yes

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

 Remote access allowed                                                   Yes

DisabledDisabled ItemsItems
DisabledDisabled ItemsItems

Array of indexes of disabled items (first item is 0).

If you set this property for an item that is not in the listbox, this property returns an
error.

This property is similar to the Disable Item item on the shortcut menu of a listbox.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

                                                    © National Instruments 7957

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7957 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7958 ordinal=7958 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   Drag/Drop:AllowDrag/Drop:Allow DragDrag andand DropDrop OutsideOutside
   ControlControl
   Drag/Drop:AllowDrag/Drop:Allow DragDrag andand DropDrop OutsideOutside
    ControlControl

           If TRUE, this enables the control to drag items to other controls and accept drags from
       other controls.

      Use the Control events for more control over how users drag items within controls.

      You can use this property with the Drag/Drop:Allow Dragging and the Drag/Drop:Allow
      Dropping properties to allow data dragging to other controls and to accept data drops
      from other controls.

       This property is similar to the Allow Drag Drop Outside Control item on the shortcut
     menu of a listbox control.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write


7958   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7958 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7959 ordinal=7959 -->
## Property and Method Reference

Property and Method Reference


 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

Drag/Drop:AllowDrag/Drop:Allow DraggingDragging
Drag/Drop:AllowDrag/Drop:Allow DraggingDragging

If TRUE, LabVIEW automatically begins a drag and drop operation from the control
when you use the Operating tool to select and drag an item from the control.

Use the Control events for more control over how users drag items within controls.
This property is similar to the Allow Dragging item on the shortcut menu of a listbox
control.

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

                                                    © National Instruments 7959

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7959 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7960 ordinal=7960 -->
## Property and Method Reference

Property and Method Reference


       Remote access allowed                                                  Yes

   Drag/Drop:AllowDrag/Drop:Allow DroppingDropping
   Drag/Drop:AllowDrag/Drop:Allow DroppingDropping

           If TRUE, LabVIEW automatically accepts drops containing the LV_LISTBOX,
      LV_TEXT, or LV_LISTBOX_ITEMS data types. The LV_LISTBOX data type is a
        cluster that contains an array of strings from the row that you are dragging data, and a
      numeric indicating the glyph associated with the row from which you are dragging.
      The LV_TEXT data type is of type string. The LV_LISTBOX_ITEMS data type is an
       array of a cluster containing an array of strings, from left to right, in the item you are
       dragging and an integer representing the glyph index associated with the item from
      which you are dragging data.

      Use the Control events for more control over how users drag items within controls.
       This property is similar to the Allow Dropping item on the shortcut menu of a listbox
        control.

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


7960   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7960 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7961 ordinal=7961 -->
## Property and Method Reference

Property and Method Reference

Drag/Drop:DragDrag/Drop:Drag ModeMode
Drag/Drop:DragDrag/Drop:Drag ModeMode

Sets the default behavior for a drag and drop operation for the control. The settings
apply only when the control configured is the source of the drag and drop operation.

Use the Control events for more control over how users drag items within controls.

This property is similar to the Drag Mode item on the shortcut menu of a listbox
control.

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

EditEdit RowRow
EditEdit RowRow

The row of the current text entry. A value of 0 indicates the top row. A value of –1


                                                    © National Instruments 7961

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7961 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7962 ordinal=7962 -->
## Property and Method Reference

Property and Method Reference

       indicates the column header. A value of –2 indicates that no edits are being made to
       the text of the control.

       Before you use this property to set text focus on a control, set key focus of the control.

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

   FocusFocus RowRow
   FocusFocus RowRow

      The row that has focus, used as the basis for key navigation such as the up and down
       arrows.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write


7962   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7962 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7963 ordinal=7963 -->
## Property and Method Reference

Property and Method Reference


 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

IsIs Array?Array?
IsIs Array?Array?

Returns TRUE if the listbox has an array data type.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                 No

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                                    Yes

 Remote access allowed                                                  Yes


                                                    © National Instruments 7963

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7963 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7964 ordinal=7964 -->
## Property and Method Reference

Property and Method Reference

   ItemItem NamesNames
   ItemItem NamesNames

       Array of the strings for the selectable items.

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

   ItemItem SymbolsSymbols
   ItemItem SymbolsSymbols

       Array of item symbols. Item symbols (0-40) are as shown in the listbox symbol ring
       constant.

       This property is similar to the Item Symbols item on the shortcut menu of a listbox.


7964   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7964 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7965 ordinal=7965 -->
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

KeyboardKeyboard ModeMode
KeyboardKeyboard ModeMode

Sets how to handle upper and lowercase characters when you type characters in a
listbox at run time. Valid values include 0 (System Default), 1 (Case Sensitive), and 2
(Case Insensitive).

This property is similar to the Keyboard Mode item on the shortcut menu of a listbox.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes


                                                    © National Instruments 7965

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7965 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7966 ordinal=7966 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   MultipleMultiple LineLine InputInput
    MultipleMultiple LineLine InputInput

           If TRUE, you can enter multiple lines of text in the listbox cells by pressing the <Enter>
      key on the keyboard. If FALSE, pressing the <Enter> key on the keyboard while editing
        cells causes LabVIEW to commit the edits in the current cell and move the text focus to
       the next cell. This property does not affect run-time behavior of the listbox.

       This property is similar to the Multi-line Input item on the shortcut menu of a single-
      column listbox.

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


7966   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7966 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7967 ordinal=7967 -->
## Property and Method Reference

Property and Method Reference


 Remote access allowed                                                  Yes

NumberNumber ofof RowsRows
NumberNumber ofof RowsRows

Number of visible items in the listbox. This property counts partially visible rows.

If you wire a value of 0 to this property, LabVIEW displays the topmost row. The listbox
resizes according to the number of rows you set.

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

SelectSelect EntireEntire RowsRows
SelectSelect EntireEntire RowsRows

Highlights the entire row if you select a row in the tree.


                                                    © National Instruments 7967

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7967 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7968 ordinal=7968 -->
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

   SelectionSelection ColorColor
    SelectionSelection ColorColor

       Color used to draw the data selection.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No


7968   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7968 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7969 ordinal=7969 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

SelectionSelection ModeMode
SelectionSelection ModeMode

Number of items the user can select. Valid values include 0 (zero or one), 1 (one), 2
(zero or more), and 3 (one or more).

A single-selection listbox has a scalar data type, and a multiple-selection listbox has an
array data type. If you set this property for a single-selection listbox to a value of 2 or 3,
LabVIEW returns an error because LabVIEW cannot change the data type from scalar to
array at run time.

This property is similar to the Selection Mode item on the shortcut menu of a listbox.

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


                                                    © National Instruments 7969

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7969 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7970 ordinal=7970 -->
## Property and Method Reference

Property and Method Reference

    SizeSize
    SizeSize

      The width and height in pixels of the listbox control.

       This property is similar to the Size Height and Size Width options on the Appearance
      page of the Properties dialog box.

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

   Size:HeightSize:Height
    Size:HeightSize:Height

      The height of the listbox control in pixels.

       This property is an element of the Size property. This property is also similar to the
       Size Height option on the Appearance page of the Properties dialog box.


7970   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7970 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7971 ordinal=7971 -->
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

Size:WidthSize:Width
Size:WidthSize:Width

The width of the listbox control in pixels.

This property is an element of the Size property. This property is also similar to the
Size Width option on the Appearance page of the Properties dialog box.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


                                                    © National Instruments 7971

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7971 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7972 ordinal=7972 -->
## Property and Method Reference

Property and Method Reference


         Settable when the VI is running                                           Yes

        Loads the front panel into memory                              No

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   TopTop RowRow
   TopTop RowRow

     Row number currently at the top of the listbox. The number of visible items in the
        listbox does not limit the row number you can select for this property.

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


7972   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7972 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7973 ordinal=7973 -->
## Property and Method Reference

Property and Method Reference

VisibleVisible Items:ColumnItems:Column HeaderHeader VisibleVisible
VisibleVisible Items:ColumnItems:Column HeaderHeader VisibleVisible

If TRUE, displays the column header.

This property is similar to the Visible Items»Column Header item on the shortcut
menu of a single-column listbox.

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

VisibleVisible Items:HorizontalItems:Horizontal LinesLines VisibleVisible
VisibleVisible Items:HorizontalItems:Horizontal LinesLines VisibleVisible

If TRUE, displays horizontal lines that separate rows in the listbox.

This property is similar to the Visible Items»Horizontal Lines item on the shortcut
menu of a listbox and the Show horizontal lines option on the Appearance page of the


                                                    © National Instruments 7973

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7973 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7974 ordinal=7974 -->
## Property and Method Reference

Property and Method Reference

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

    VisibleVisible Items:SymbolsItems:Symbols VisibleVisible
    VisibleVisible Items:SymbolsItems:Symbols VisibleVisible

           If TRUE, displays the item symbols.

       This property is similar to the Visible Items»Symbols item on the shortcut menu of a
        listbox and the Show symbols option on the Appearance page of the Properties dialog
       box.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write


7974   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7974 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7975 ordinal=7975 -->
## Property and Method Reference

Property and Method Reference


 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                              No

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

VisibleVisible Items:VerticalItems:Vertical ScrollbarScrollbar VisibleVisible
VisibleVisible Items:VerticalItems:Vertical ScrollbarScrollbar VisibleVisible

If TRUE, displays the vertical scroll bar.

This property is similar to the Visible Items»Vertical Scrollbar item on the shortcut
menu of a listbox.

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


                                                    © National Instruments 7975

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7975 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7976 ordinal=7976 -->
## Property and Method Reference

Property and Method Reference

    ListBoxListBox EventsEvents


        Event      Description

        Double
                   Generated when a user double-clicks an item in a listbox.          Click

        Drag                   Generated when you start a drag from a listbox control.         Starting

        Drag
                   Generated when you start a drag from a listbox control.          Starting?

         Edit Cell    Generated when the user enters new text or changes text in a cell.

                   Generated when the user enters new text or changes text in a cell but before the new or
         Edit Cell?                  changed text appears.

   DoubleDouble ClickClick
   DoubleDouble ClickClick

      Generated when a user double-clicks an item in a listbox.

       This event behaves similarly to the Get Double-Clicked Row method. However, this
       event returns information about any keys the user pressed while double-clicking a
       row.

     Event Data Fields

      Name     Description

                  Source of the event. LabVIEW UI refers to any built-in user interface event.

        Source
                  0            LabVIEW UI


7976   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7976 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7977 ordinal=7977 -->
## Property and Method Reference

Property and Method Reference


Name     Description

Type     Type of event that occurred, such as Mouse Down, Value Change, Timeout, and so on.


Time     Value of the millisecond timer when the event occurred.


CtlRef     Reference to the control on which the event occurred.

Coords

          Value that corresponds to which mouse button the user clicked. Left mouse button is 1,
            right mouse button is 2. Operating systems might assign higher numbers if you have aButton
        mouse with more than two buttons. For filter events, you can modify the data returned
         by this event data field.


           Cluster of Booleans that contain platform-independent modifiers. LabVIEW returns all
          platform-dependent modifiers in the PlatMods event data field. For key events, this
          event returns a Boolean indicating if the event occurred on the numeric keypad. For
Mods    mouse events, this event returns a Boolean indicating if the event was a double-click.
          For both events, a Boolean is returned if the platform-independent menu key, such as
           <Ctrl> on Windows or <Command> on macOS, was pressed when the event occurred.
          For filter events, you can modify the data returned by this event data field.


           Cluster of Booleans that contain platform-dependent modifiers. Specifies if platform-
         dependent keys, such as <Ctrl>, <Shift>, <Alt>, <Command>, and <Option> were held
        down when the event was triggered. For filter events, you can modify the data returned
PlatMods
         by this event data field. A key can be both a Mod and PlatMod. For example, <Ctrl> is the
          platform-independent menu key on Windows, but you also can use it in platform-
         dependent programming.


        Number of the row the user double-clicked. The first row on the top is 0. The column
Row
         header is –1.


                                                    © National Instruments 7977

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7977 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7978 ordinal=7978 -->
## Property and Method Reference

Property and Method Reference

   DragDrag StartingStarting
   DragDrag StartingStarting

      Generated when you start a drag from a listbox control.

      Use this event to signal when a drag and drop operation begins from a specific control.
       This event is generated only when LabVIEW begins a drag and drop operation on a
        listbox control. You can use the Start Drag method to begin a drag from other controls.

     Event Data Fields

      Name     Description

                  Source of the event. LabVIEW UI refers to any built-in user interface event.

        Source
                  0            LabVIEW UI


        Type     Type of event that occurred, such as Mouse Down, Value Change, Timeout, and so on.


       Time     Value of the millisecond timer when the event occurred.


         CtlRef     Reference to the control on which the event occurred.


                  Coordinates of the location of the mouse click at the time the event occurs. Coordinates
        Coords
                   are relative to the drop target's owning pane origin, excluding clusters.


                   Value that corresponds to which mouse button the user clicked. Left mouse button is 1,
        Button    right mouse button is 2. Operating systems might assign higher numbers if you have a
               mouse with more than two buttons. For filter events, you can modify the data returned


7978   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7978 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7979 ordinal=7979 -->
## Property and Method Reference

Property and Method Reference


Name     Description

         by this event data field.


           Cluster of Booleans that contain platform-independent modifiers. LabVIEW returns all
          platform-dependent modifiers in the PlatMods event data field. For key events, this
          event returns a Boolean indicating if the event occurred on the numeric keypad. For
Mods    mouse events, this event returns a Boolean indicating if the event was a double-click.
          For both events, a Boolean is returned if the platform-independent menu key, such as
           <Ctrl> on Windows or <Command> on macOS, was pressed when the event occurred.
          For filter events, you can modify the data returned by this event data field.


           Cluster of Booleans that contain platform-dependent modifiers. Specifies if platform-
         dependent keys, such as <Ctrl>, <Shift>, <Alt>, <Command>, and <Option> were held
        down when the event was triggered. For filter events, you can modify the data returnedPlatMods         by this event data field. A key can be both a Mod and PlatMod. For example, <Ctrl> is the
          platform-independent menu key on Windows, but you also can use it in platform-
         dependent programming.

           Indicates the data provided during the drag and drop operation. For filter events, you
         can modify this field to provide your own custom data for the drag and drop operation.
         You cannot use the prefix LV_ on a user-defined data name, because it is reserved for
         LabVIEW data types. You can use the built-in LabVIEW data types and names.

         LabVIEW Data Type     Description

        LV_TEXT               String

        LV_TREE_TAG         String
Data                                   Array of a cluster containing an array of strings, from left to
                                         right, in the item you are dragging, an integer representing
        LV_TREE_ITEMS     the glyph index associated with the item from which you are
                                 dragging data, and an integer representing the indent level of
                                 the item from which you are dragging.

                                    Cluster containing an array of strings from the row that you
        LV_LISTBOX          are dragging data and an integer representing the glyph index
                                  associated with the row from which you are dragging data.


                                                    © National Instruments 7979

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7979 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7980 ordinal=7980 -->
## Property and Method Reference

Property and Method Reference


      Name     Description

                 LabVIEW Data Type     Description

                                            Array of a cluster containing an array of strings, from left to
                                                   right, in the item you are dragging and an integer
               LV_LISTBOX_ITEMS                                           representing the glyph index associated with the item from
                                      which you are dragging data.

               LV_PATH             Path


                    Specifies the operations that this control supports during the drag, such as copy or
                 move, copy only, move only. If you select copy or move, pressing the <Ctrl> key copies
                   the item. The operations you support control the values that the Results output of the        Drag
                 Drag Ended and Drag Source Update events can provide.       Mode
                   For filter events, you can modify this field to change the drag mode when this event is
                   generated.

   DragDrag Starting?Starting?
   DragDrag Starting?Starting?

      Generated when you start a drag from a listbox control.

      Use this event to signal when a drag and drop operation begins from a specific control.
       This event is generated only when LabVIEW begins a drag and drop operation on a
        listbox control. You can use the Start Drag method to begin a drag from other controls.

     Event Data Fields

      Name     Description

        Source    Source of the event. LabVIEW UI refers to any built-in user interface event.


7980   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7980 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7981 ordinal=7981 -->
## Property and Method Reference

Property and Method Reference


Name     Description


          0            LabVIEW UI


Type     Type of event that occurred, such as Mouse Down, Value Change, Timeout, and so on.


Time     Value of the millisecond timer when the event occurred.


CtlRef     Reference to the control on which the event occurred.


          Coordinates of the location of the mouse click at the time the event occurs. CoordinatesCoords          are relative to the drop target's owning pane origin, excluding clusters.


          Value that corresponds to which mouse button the user clicked. Left mouse button is 1,
            right mouse button is 2. Operating systems might assign higher numbers if you have aButton        mouse with more than two buttons. For filter events, you can modify the data returned
         by this event data field.


           Cluster of Booleans that contain platform-independent modifiers. LabVIEW returns all
          platform-dependent modifiers in the PlatMods event data field. For key events, this
          event returns a Boolean indicating if the event occurred on the numeric keypad. For
Mods    mouse events, this event returns a Boolean indicating if the event was a double-click.
          For both events, a Boolean is returned if the platform-independent menu key, such as
           <Ctrl> on Windows or <Command> on macOS, was pressed when the event occurred.
          For filter events, you can modify the data returned by this event data field.


           Cluster of Booleans that contain platform-dependent modifiers. Specifies if platform-
         dependent keys, such as <Ctrl>, <Shift>, <Alt>, <Command>, and <Option> were held
PlatMods down when the event was triggered. For filter events, you can modify the data returned
         by this event data field. A key can be both a Mod and PlatMod. For example, <Ctrl> is the
          platform-independent menu key on Windows, but you also can use it in platform-


                                                    © National Instruments 7981

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7981 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7982 ordinal=7982 -->
## Property and Method Reference

Property and Method Reference


      Name     Description

                 dependent programming.

                    Indicates the data provided during the drag and drop operation. For filter events, you
                 can modify this field to provide your own custom data for the drag and drop operation.
                 You cannot use the prefix LV_ on a user-defined data name, because it is reserved for
                LabVIEW data types. You can use the built-in LabVIEW data types and names.

                 LabVIEW Data Type     Description

               LV_TEXT               String

               LV_TREE_TAG         String

                                            Array of a cluster containing an array of strings, from left to
                                                   right, in the item you are dragging, an integer representing
               LV_TREE_ITEMS     the glyph index associated with the item from which you are
        Data                                          dragging data, and an integer representing the indent level of
                                          the item from which you are dragging.

                                              Cluster containing an array of strings from the row that you
               LV_LISTBOX          are dragging data and an integer representing the glyph index
                                           associated with the row from which you are dragging data.

                                            Array of a cluster containing an array of strings, from left to
                                                   right, in the item you are dragging and an integer
               LV_LISTBOX_ITEMS                                           representing the glyph index associated with the item from
                                      which you are dragging data.

               LV_PATH             Path


                    Specifies the operations that this control supports during the drag, such as copy or
                 move, copy only, move only. If you select copy or move, pressing the <Ctrl> key copies
                   the item. The operations you support control the values that the Results output of the        Drag
                 Drag Ended and Drag Source Update events can provide.       Mode
                   For filter events, you can modify this field to change the drag mode when this event is
                   generated.

                   Allows you to prevent LabVIEW from processing the event, bypassing the behavior
         Discard?
                  normally triggered by that event. The default is FALSE.


7982   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7982 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7983 ordinal=7983 -->
## Property and Method Reference

Property and Method Reference

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Structures\Event Structure\Drag and Drop
   - Passing Custom Drag Data.vi
EditEdit CellCell
EditEdit CellCell

Generated when the user enters new text or changes text in a cell.

Event Data Fields

 Name   Description

         Source of the event. LabVIEW UI refers to any built-in user interface event.

 Source
         0            LabVIEW UI


 Type    Type of event that occurred, such as Mouse Down, Value Change, Timeout, and so on.


 Time    Value of the millisecond timer when the event occurred.


 CtlRef   Reference to the control on which the event occurred.


 String   Text string that the user entered.


 Row    The row of the cell in which the event occurred.


                                                    © National Instruments 7983

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7983 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7984 ordinal=7984 -->
## Property and Method Reference

Property and Method Reference

   EditEdit Cell?Cell?
    EditEdit Cell?Cell?

      Generated when the user enters new text or changes text in a cell but before the new
       or changed text appears.

     Event Data Fields

      Name    Description

                 Source of the event. LabVIEW UI refers to any built-in user interface event.

        Source
                 0            LabVIEW UI


        Type    Type of event that occurred, such as Mouse Down, Value Change, Timeout, and so on.


       Time     Value of the millisecond timer when the event occurred.


         CtlRef    Reference to the control on which the event occurred.


         String    Text string that the user entered.


      Row     The row of the cell in which the event occurred.

                  Allows you to prevent LabVIEW from processing the event, bypassing the behavior
         Discard?
                 normally triggered by that event. The default is FALSE.

   TableTable


7984   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7984 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7985 ordinal=7985 -->
## Property and Method Reference

Property and Method Reference

Table Methods

Table Properties
TableTable MethodsMethods


 Method     Description

 Export Data             Exports the table data to the clipboard in a tab-delimited format, which is accepted by to           most spreadsheet applications. Clipboard

 Export Data             Exports the table data to Excel. to Excel

 Export
             Exports an image of a table to the clipboard or disk. Image

 Point to     Converts a pixel coordinate to a row-column pair in the coordinates of the control.
 Row         This method also returns whether the point is inside the bounds of the content
 Column     rectangle.

 Set Cell     Sets the value of a cell specified by the row and column index. If you specify –2 for the
 Value      row and column index, LabVIEW returns error 1.

ExportExport DataData toto ClipboardClipboard
ExportExport DataData toto ClipboardClipboard

Exports the table data to the clipboard in a tab-delimited format, which is accepted by
most spreadsheet applications.

Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes


                                                    © National Instruments 7985

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7985 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7986 ordinal=7986 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                                      Yes

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

   ExportExport DataData toto ExcelExcel
    ExportExport DataData toto ExcelExcel

       Exports the table data to Excel.

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                                      Yes

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes


7986   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7986 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7987 ordinal=7987 -->
## Property and Method Reference

Property and Method Reference

ExportExport ImageImage
ExportExport ImageImage

Exports an image of a table to the clipboard or disk.

This method is similar to the Export Simplified Image option on the shortcut menu of a
table.

Parameters

          Data Name          Required  Description
           type

                              Specifies the format of the file. You can export into one of the
                             following formats:

                         (Windows) .emf, .bmp (default), and .eps files File Type        Yes
                        (macOS) .pict, .bmp (default), and .eps files

                              (Linux) .bmp (default) and .eps files


                              Specifies whether to save the image to the clipboard or to disk. When Target           Yes                        you set Target to File, you must specify a Path.


                          Path to the LabVIEW project library file. LabVIEW ignores this
 Path         No       parameter if you set Target to Clipboard. When you set Target to File,
                        you must specify a Path.


 Always                                 If TRUE, LabVIEW overwrites an existing file without prompting you. If
             No
 Overwrite                FALSE (default), LabVIEW prompts you to overwrite an existing file.


                                                    © National Instruments 7987

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7987 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7988 ordinal=7988 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                      No

         Settable when the VI is running                                      Yes

        Loads the front panel into memory                                  Yes

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

   PointPoint toto RowRow ColumnColumn
    PointPoint toto RowRow ColumnColumn

       Converts a pixel coordinate to a row-column pair in the coordinates of the control. This
      method also returns whether the point is inside the bounds of the content rectangle.

     Parameters

                   Data
      Name               Required  Description
                   type

                                            Specifies the pixel coordinate to translate into a row-column
         Point                 Yes
                                                  pair.


                                        Returns TRUE if the point is inside the bounds of the content
          In Bounds?            Yes
                                            rectangle.

          Cell                  Yes       Returns the row and column of the cell in which the point lies.


7988   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7988 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7989 ordinal=7989 -->
## Property and Method Reference

Property and Method Reference


            Data Name               Required  Description
            type

                                                   • Row—Returns the row of the cell in which the point lies.
 Position                                       • Column—Returns the column of the cell in which the point
                                                  lies.


Remarks

The following table lists the characteristics of this method.


 Data type                                            No return value

 Available in Run-Time Engine                                       Yes

 Available in Real-Time Operating System                             Yes

 Settable when the VI is running                                      Yes

 Loads the front panel into memory                          No

 Need to authenticate before use                            No

 Loads the block diagram into memory                        No

 Remote access allowed                                             Yes

SetSet CellCell ValueValue
SetSet CellCell ValueValue

Sets the value of a cell specified by the row and column index. If you specify –2 for the
row and column index, LabVIEW returns error 1.


                                                    © National Instruments 7989

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7989 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7990 ordinal=7990 -->
## Property and Method Reference

Property and Method Reference

     Parameters

              Data      Name       Required  Description
               type

                                   Specifies the column or horizontal index of the table. The index is zero-        X                      Yes      based so the top-left cell in the table is (X,Y)= (0,0). A value of –1 indicates         Index                               the column header.


                                   Specifies the row or vertical index of the table. The index is zero-based so
        Y                      Yes       the top-left cell in the table is (X,Y)= (0,0). A value of –1 indicates the row         Index                                header.


         Value        Yes       Value you want in the specified table cell.


     Remarks

      The following table lists the characteristics of this method.


        Data type                                            No return value

         Available in Run-Time Engine                                       Yes

         Available in Real-Time Operating System                             Yes

         Settable when the VI is running                                      Yes

        Loads the front panel into memory                          No

       Need to authenticate before use                            No

        Loads the block diagram into memory                        No

       Remote access allowed                                             Yes

   TableTable PropertiesProperties


7990   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7990 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7991 ordinal=7991 -->
## Property and Method Reference

Property and Method Reference


Property         Description

Active                  Sets the row and column of the active cell(s).Cell:Active Cell

Active Cell:Cell
Background     The background color of active cell(s).
Color

Active Cell:Cell               The font of the active cell in the table control.Font

Active Cell:Cell                  Indicates whether the text in the active cell is bold.
Font:Bold

Active Cell:Cell               The text font color in the active cell.Font:Color

Active Cell:Cell                  Indicates whether the text in the active cell is italic.Font:Italic

Active Cell:Cell   The name of the font in the active cell. Predefined font names include App
Font:Name      Font, Sys Font, and Dlg Font.

Active Cell:Cell               The size of the font in the active cell.Font:Size

Active Cell:Cell                  Indicates whether to strike out the text in the active cell.Font:Strikeout

Active Cell:Cell                  Indicates whether the text in the active cell is underlined.Font:Underline

Active Cell:Cell                 Gets and sets the justification of text within a table cell.
Justification

Active Cell:Cell
               The size of the active cell(s) in pixels.
Size

Active Cell:Cell
               The height of the active cell(s) in pixels.
Size:Height

Active Cell:Cell
               The width of the active cell(s) in pixels.
Size:Width

Active          The coordinate in pixels, relative to the origin of the owning pane, of the top-left
Cell:Position      position of the active cell(s).

Active          The coordinate in pixels, relative to the origin of the owning pane, of the left
Cell:Position:Left edge of the active cell.

                                                    © National Instruments 7991

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7991 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7992 ordinal=7992 -->
## Property and Method Reference

Property and Method Reference


        Property         Description

         Active          The coordinate in pixels, relative to the origin of the owning pane, of the top
         Cell:Position:Top edge of the active cell.

         Autosizing Row   Determines whether the rows autosize their height to display all text when fonts
        Height          change or when the number of lines in a cell changes.

       Column Header                     An array of the strings in the column headers.          Strings[]

        Content Rect                      The size in pixels of the content rectangle of the table control.       Bounds

        Content Rect                      The height in pixels of the content rectangle of the table control.        Bounds:Height

        Content Rect                      The width in pixels of the content rectangle of the table control.
        Bounds:Width

        Content Rect    The coordinate in pixels, relative to the origin of the owning pane, of the top-left
         Position          position of the content rectangle of the table control.

        Content Rect    The coordinate in pixels, relative to the origin of the owning pane, of the left
          Position:Left     edge of the content rectangle of the table control.

        Content Rect    The coordinate in pixels, relative to the origin of the owning pane, of the top
         Position:Top     edge of the content rectangle of the table control.

         Default Value     Gets or sets the default value of the table control.

                      The row-column pair index of the current text entry. Values of (0,0) indicate the
                              top-left text entry. A value of –1 indicates the row or column header but they
                        cannot be edited using this property. Values of (–2, –2) indicate that no edits are
         Edit Position     being made to the text of the control.

                          Before you use this property to set text focus on a control, set key focus of the
                             control.

                   Row and column index of the cell displayed in the top left corner. If you display
         Index Values
                         the row and column headers, the non-header cell is the top left corner.

                                          If TRUE, you can enter multiple lines of text in the table cells by pressing the
                         <Enter> key on the keyboard. If FALSE, pressing the <Enter> key on the keyboard
         Multiple Line
                          while editing cells causes LabVIEW to commit the edits in the current cell and the
         Input
                              text focus moves to the next cell. This property does not affect run-time behavior
                            of the table.


7992   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7992 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7993 ordinal=7993 -->
## Property and Method Reference

Property and Method Reference


Property         Description

              Number of visible columns in the table, including the row headers if visible. TheNumber of              number of columns might change if the vertical scroll bar is visible. This propertyColumns                 counts partially visible columns.

              Number of visible rows in the table. If the table uses column headers, this
              number includes one row for the column headers. The number of rows mightNumber of Rows               change if the horizontal scroll bar is visible. This property counts partially visible
                 rows.

Row Header              An array of the strings in the row headers.
Strings[]

Selection Color   Color used to draw the data selection.

                 Index of the row and column pair that specifies the number of rows and columnsSelection Size
                    in the selection.

             Row and column index that specifies the beginning of data selection.Selection Start
                 Coordinates begin at (0,0), which is top left, and do not include headers.

Size            The width and height in pixels of the table control.

Size:Height      The height of the table control in pixels.

Size:Width      The width of the table control in pixels.

                            If TRUE, the horizontal scrolling of the table is by pixels, such that the first
Smooth        column may be horizontally clipped. If FALSE, the table scrolls by whole column
Horizontal       widths such that the first column is never clipped. However, if a column is wider
Scrolling        than the width of the table, you cannot see the text that is hidden off the right
               edge of that column.

Value            Value of table control: 2D array of strings.

Value (Signaling)  Sets the value of the control and generates a Value Change event.

Visible
Items:Column       If TRUE, displays the column headers.
Headers Visible

Visible
Items:Horizontal   If TRUE, displays horizontal lines that separate rows in the table.
Lines Visible

Visible
Items:Horizontal   If TRUE, displays the horizontal scroll bar.
Scrollbar Visible


                                                    © National Instruments 7993

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7993 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7994 ordinal=7994 -->
## Property and Method Reference

Property and Method Reference


        Property         Description

          Visible
         Items:Index       Displays the row-column index of the top left visible cell in a table.
          Visible

          Visible
        Items:Row      Shows the row headers.
        Headers Visible

          Visible
          Items:Vertical       If TRUE, displays vertical lines that separate columns in the table.
         Lines Visible

          Visible
          Items:Vertical       If TRUE, displays the vertical scroll bar.
         Scrollbar Visible

   ActiveActive Cell:ActiveCell:Active CellCell
    ActiveActive Cell:ActiveCell:Active CellCell

       Sets the row and column of the active cell(s).

     Elements

      Name   Description
                  Sets the row(s) of the active cell(s). Possible values are 0…n, where nis the total number      Row
                   of rows - 1. Enter –2 to select all rows.
                  Sets the column(s) of the active cell(s). Possible values are 0…m, where mis the total
       Column number of columns - 1. Enter –2 to select all columns. Enter –1 to select the column
                  header.

      The following table lists example values for this property.


      Row  Column    Result

        –2    0           Selects all cells of the first column, including the column header.


7994   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7994 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7995 ordinal=7995 -->
## Property and Method Reference

Property and Method Reference


 Row  Column    Result

 –2    –2         Selects all rows and columns, including column headers.

 –1    0           Selects the header of the first column.

 –1    –2         Selects the headers of all columns.

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

ActiveActive Cell:CellCell:Cell BackgroundBackground ColorColor
ActiveActive Cell:CellCell:Cell BackgroundBackground ColorColor

The background color of active cell(s).

You can set the color of the front panel object by wiring a hexadecimal number with
the form RRGGBB or by wiring the color box constant to the property.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 7995

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7995 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7996 ordinal=7996 -->
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

   ActiveActive Cell:CellCell:Cell FontFont
    ActiveActive Cell:CellCell:Cell FontFont

      The font of the active cell in the table control.

      Use this property to change the size, style, or color of the cell font. You cannot use this
       property with a strict type definition.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No


7996   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7996 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7997 ordinal=7997 -->
## Property and Method Reference

Property and Method Reference


 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

ActiveActive Cell:CellCell:Cell Font:BoldFont:Bold
ActiveActive Cell:CellCell:Cell Font:BoldFont:Bold

Indicates whether the text in the active cell is bold.

This property is an element of the Active Cell:Cell Font property.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

ActiveActive Cell:CellCell:Cell Font:ColorFont:Color
ActiveActive Cell:CellCell:Cell Font:ColorFont:Color

The text font color in the active cell.


                                                    © National Instruments 7997

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7997 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7998 ordinal=7998 -->
## Property and Method Reference

Property and Method Reference

       This property is an element of the Active Cell:Cell Font property.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   ActiveActive Cell:CellCell:Cell Font:ItalicFont:Italic
    ActiveActive Cell:CellCell:Cell Font:ItalicFont:Italic

       Indicates whether the text in the active cell is italic.

       This property is an element of the Active Cell:Cell Font property.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes


7998   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7998 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7999 ordinal=7999 -->
## Property and Method Reference

Property and Method Reference


 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

ActiveActive Cell:CellCell:Cell Font:NameFont:Name
ActiveActive Cell:CellCell:Cell Font:NameFont:Name

The name of the font in the active cell. Predefined font names include App Font,
Sys Font, and Dlg Font.

This property is an element of the Active Cell:Cell Font property.

If you select an invalid font, this property returns an error.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

 Remote access allowed                                                  Yes

                                                    © National Instruments 7999

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:7999 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:8000 ordinal=8000 -->
## Property and Method Reference

Property and Method Reference

   ActiveActive Cell:CellCell:Cell Font:SizeFont:Size
    ActiveActive Cell:CellCell:Cell Font:SizeFont:Size

      The size of the font in the active cell.

       This property is an element of the Active Cell:Cell Font property.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

       Remote access allowed                                                  Yes

   ActiveActive Cell:CellCell:Cell Font:StrikeoutFont:Strikeout
    ActiveActive Cell:CellCell:Cell Font:StrikeoutFont:Strikeout

       Indicates whether to strike out the text in the active cell.

       This property is an element of the Active Cell:Cell Font property.


8000   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:8000 -->

