# NI_LABVIEW_PROGRAMMING_REFERENCE

<!--SYSTEM_CORPUS id=NI_LABVIEW_PROGRAMMING_REFERENCE format=markdown generated=2026-07-14T12:02:18+00:00 -->
- title: LabVIEW Programming Reference Manual
- source: https://docs-be.ni.com/bundle/labview-api-ref/preprocessedpdf/enus
- source_sha256: 7a54c389b4f3d78e2215f55c9f156124d3668ce61d0d5018094e356004d895ac
- versions: 2024 Q1|2024 Q3|2025 Q1|2025 Q3|2026 Q1
- fidelity: full-text-records

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11501 ordinal=11501 -->
## Error Codes and Messages

Error Codes and Messages


To correct this error, you must either remove the dynamic dispatch setting or replace
this control or indicator with another that is the type of the owning class.

PrivatePrivate datadata controlcontrol ofof thisthis classclass mustmust bebe aa clustercluster

Even if you only have zero or one element in the cluster, the private data control must
be a cluster type.


To correct this error, make sure that the elements of the private data control are in a
cluster even if you need only zero or one element for the private data.


                                                    © National Instruments 11501

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11501 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11502 ordinal=11502 -->
## Error Codes and Messages

Error Codes and Messages


       PrivatePrivate datadata controlcontrol ofof thisthis classclass usesuses anan illegalillegal valuevalue forfor itsits defaultdefault
      datadata

       The private data control defines the default value for a LabVIEW class. This error occurs
      when the private data control has values set as the defaults that are illegal. Illegal
         default values include the following values:

               • Any value of this class itself
               • Any value of any child class
               • Any class LabVIEW has not loaded into memory
               • Any class that uses this class as a member in its own private data control

            Note LabVIEW is a by-value language and does not have a "reference to
                 class" control. If you include a class control in the private data cluster,

11502   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11502 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11503 ordinal=11503 -->
## Error Codes and Messages

Error Codes and Messages


       LabVIEW includes the entire class value in the private data. Instantiating a
        class that contains itself would result in the data type definition recursing
         infinitely and allocating by value at every level until memory was full. Only a
        class that is fully defined without using itself as part of its definition can be
       used as fields of the private data control.

To correct this error, check for these illegal default values. Check class controls and
variant controls for illegal default values.

PrivatePrivate datadata controlcontrol ofof thisthis LabVIEWLabVIEW classclass hashas anan undefinedundefined typetype

This error occurs on controls and indicators of LabVIEW class types if the private data
control of the initial LabVIEW class includes an array without a subtype, or a nested
empty cluster. The top-level cluster of the private data control can have zero elements,
but nested clusters must have at least one element.

The following image displays all possible issues:

  • Empty nested cluster
  • Void array
  • Missing LabVIEW class
  • Missing type definition


To correct this error, verify that all nested clusters of the private data control have at
least one element.


                                                    © National Instruments 11503

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11503 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11504 ordinal=11504 -->
## Error Codes and Messages

Error Codes and Messages

       PrivatePrivate datadata controlcontrol ofof thisthis classclass isis notnot aa validvalid datadata typetype

       The private data control must be a cluster of zero or more valid elements.

       To correct this error, verify that the cluster contains valid elements. Click the Invalid
        Control button to open the Error list window and correct the errors the Error list
       window displays. The private data control might contain an array without a subtype, a
        nested cluster of zero elements, a missing or broken type definition, or a missing or
        broken LabVIEW class.

       RefersRefers toto aa brokenbroken LabVIEWLabVIEW classclass

        This control refers to a broken LabVIEW class.

       To correct this error, right-click the broken class and select Show Error Window to
        view the errors in the Error list window. Resolve the errors that the Error list window
         displays.

       RefersRefers toto aa missingmissing LabVIEWLabVIEW classclass

        This control is broken because LabVIEW cannot find the class to which this control
          refers.


        This reference control is broken because LabVIEW cannot find the class to which this
         control refers.


        This refnum control is broken because LabVIEW cannot find the class this control uses
         in its connector pane.


11504   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11504 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11505 ordinal=11505 -->
## Error Codes and Messages

Error Codes and Messages


To correct this error, load into memory the LabVIEW class to which the control refers.

ThisThis VIVI cannotcannot accessaccess thethe classclass controlcontrol

This VI cannot use the LabVIEW class control because the library access scope does not
allow access to the class. The LabVIEW class is a private library item and only VIs in the
same library or libraries contained in that library can access the class.

To correct this error, change the access scope of the class library.

MiscellaneousMiscellaneous FrontFront PanelPanel ErrorsErrors

This section contains reference information about miscellaneous front panel syntax
errors.

BooleanBoolean latchlatch actionaction isis incompatibleincompatible withwith locallocal variablesvariables

If a Boolean control has associated local variables, the Boolean control cannot use a
latch mechanical action.


The first local variable to read the Boolean control with latch action resets its value to
the default value.


                                                    © National Instruments 11505

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11505 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11506 ordinal=11506 -->
## Error Codes and Messages

Error Codes and Messages

      ChannelChannel controlscontrols oror indicatorsindicators cannotcannot bebe nestednested insideinside anotheranother
       controlcontrol oror indicatorindicator

       A channel control or indicator cannot be nested inside another control or indicator. To
         correct this error, replace the channel control or indicator with another type of control
        or indicator, or move the channel control or indicator out of the nesting counterparts.

      ChannelChannel controlscontrols oror indicatorsindicators mustmust bebe onon thethe connectorconnector panepane

       Channel controls or indicators cannot be independent endpoints. They must be
        connected to the connector pane. To correct this error, add the channel controls or
         indicators to the connector pane.

       ControlControl containscontains nono elementselements andand isis undefinedundefined

      Some controls require an inner control to work correctly. When such a control does not
        contain any elements, its type is undefined. In the following example, all of the
         controls would return this error.


       To correct this error, place the control you want inside the broken control.

       ControlControl hashas badbad unitunit syntaxsyntax

       The unit text in the unit label for this control is invalid.


         Right-click the unit label and select Build Unit String from the shortcut menu to
         display a list of valid units.

11506   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11506 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11507 ordinal=11507 -->
## Error Codes and Messages

Error Codes and Messages

ControlControl requiresrequires anan externalexternal librarylibrary

This error occurs if the required external library is not installed, is not installed in the
correct location, or is not loadable, or when the version of the library is not compatible
with the control. To correct this error, ensure the library is installed in the correct
location and check the version of the library.

CouldCould notnot determinedetermine datadata typestypes ofof allall wireswires inin thisthis VIVI

This error might occur if you do not wire an initial value to one of the shift registers on
the block diagram.

EmptyEmpty customcustom controlcontrol panelpanel

The custom control must contain one control to be valid.

To correct this error, add a control from the Controls palette to the custom control.

EnumerationEnumeration itemsitems mustmust bebe uniqueunique

All item names in an enumeration list must be unique. In the following example, the
enumeration list contains two items of the same name.


To correct this error, change the names of duplicate items.

ExternalExternal datadata valuevalue referencereference onon thethe frontfront panelpanel containscontains unsupportedunsupported
datadata typetype

LabVIEW does not support an external data value reference with a contained type
other than an array of integers, floating-point, fixed-point, or boolean data type. An
external data value reference control is for display only. A device driver must support
and provide the external data value reference.


                                                    © National Instruments 11507

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11507 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11508 ordinal=11508 -->
## Error Codes and Messages

Error Codes and Messages

       ExtraExtra controlscontrols onon customcustom control'scontrol's frontfront panelpanel

       The front panel contains extra controls that do not belong to the custom control. For
        example, the following custom control front panel contains both a cluster and a
       Boolean control.


       To correct this error, delete any controls on the front panel that do not belong to the
       custom control.

      RadioRadio buttonbutton hashas enumerationenumeration conflictconflict

       Each Boolean control in a radio buttons control must have a unique label. However,
        they do not have to have unique captions. The labels are used as the values of the
        enumeration type on the block diagram. In the following example, the second and
         third Boolean controls have the same label.


       To correct this error, create a unique and valid label for each Boolean control.

         In the following example, the Allow No Selection option is enabled for a radio buttons
         control. As a result, none of the Boolean controls can have a No Selection label.


11508   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11508 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11509 ordinal=11509 -->
## Error Codes and Messages

Error Codes and Messages


When Allow No Selection is enabled, the enumeration uses the text No Selection
to indicate when none of the radio buttons are checked.

To correct this error, change the value of the No Selection label or disable the Allow
No Selection option.

TheThe XControlXControl usedused inin thisthis VIVI isis brokenbroken

The XControl library is missing or one or more VIs required by the XControl might be
broken or missing.

TypeType doesdoes notnot coercecoerce

The control type does not coerce with the variable it is bound to.

To correct this error, the data type of the control and the variable must be the same, or
you must be able to coerce the data types.


                                                    © National Instruments 11509

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11509 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11510 ordinal=11510 -->
## Error Codes and Messages

Error Codes and Messages

      UnresolvedUnresolved linkagelinkage toto network-publishednetwork-published variablevariable

        This control is bound to a network-published variable, but the variable could not be
       found in the current project.

       XControlXControl isis disconnecteddisconnected

       The XControl library is currently disconnected from the XControl. The XControl is
        unlocked for editing. To correct this error, right-click the XControl library and select
        Apply Changes to Instances from the shortcut menu.

       XControlXControl notnot supportedsupported forfor currentcurrent targettarget

        XControls are not supported for the current target.

      TheThe VIVI cannotcannot accessaccess thethe XControlXControl

        This VI cannot use the XControl because the library access scope does not allow access
         to the XControl. The XControl is a private library item and only VIs in the same library
        or libraries contained in that library can access the XControl.

       Complete the following steps to correct this error by changing access to the XControl
       from Private to Public.

           1. In the Project Explorer window, right-click the XControl the VI cannot access and
             select Unlock Library for Editing.
           2. Right-click the XControl again and select Access Scope»Public.
           3. Right-click the XControl a third time and select Apply Changes to Instances. The
         Run button appears as a solid white arrow to indicate you can run the VI.

            Note You also can remove the XControl from the broken VI to correct this
                   error.

     TypeType DefinitionDefinition ErrorsErrors

        This section contains reference information about possible front panel syntax errors

11510   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11510 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11511 ordinal=11511 -->
## Error Codes and Messages

Error Codes and Messages

related to type definitions.

CannotCannot useuse anan XControlXControl inin aa privateprivate datadata controlcontrol

The private data control is using a type definition control that uses an XControl. You
cannot use an XControl in a private data control. The private data control is unable to
update to match the type definition.

ControlControl doesdoes notnot matchmatch itsits typetype definitiondefinition

This control is linked to a type definition. That type definition has been edited, but the
changes in the Control Editor window have not yet been applied. You must either
apply the changes or disconnect from the type definition. To apply the changes only
for this control, right-click the control and select Update from Type Def from the
shortcut menu. To apply changes for all instances of the type definition currently in
memory, open the type definition in the Control Editor window and select File»Apply
Changes. To disconnect this control from the type definition, right-click the control
and select Disconnect from Type Def from the shortcut menu.

ControlControl isis corruptcorrupt
Replace Paste Replace
FrontFront panelpanel controlcontrol containscontains aa datadata typetype withwith aa typetype definitiondefinition

The front panel control contains a data type with a type definition and you cannot
create a type definition from this control.

InvalidInvalid useuse ofof typetype definitiondefinition inin ControlControl EditorEditor

The Control Editor window contains a type definition as well as another control, as
shown in the following Control Editor window.


                                                    © National Instruments 11511

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11511 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11512 ordinal=11512 -->
## Error Codes and Messages

Error Codes and Messages


       To correct this error, use the type definition inside another control, such as a cluster or
       an array.

      LabVIEWLabVIEW cannotcannot updateupdate fromfrom typetype definitiondefinition withoutwithout incorrectlyincorrectly
       preservingpreserving defaultdefault valuesvalues

             If LabVIEW places a type definition instance in an unresolved state, you must manually
       update unresolved instances or remove the link between unresolved instances and the
        type definition before the application can run. To manually update the unresolved
         instances, right-click an unresolved instance and select Review and Update from Type
        Def from the shortcut menu to display the Review and Update from Type Def. dialog
        box. If you do not want to update an instance from the type definition, you can remove
        the link by right-clicking the instance and selecting Disconnect from Type Def.

         In most cases, LabVIEW correctly preserves the default values of each instance when
        updating from the type definition. However, if LabVIEW is unable to map the previous
         default values of the instance to the updated controls or constants, LabVIEW places
        those instances in an unresolved state. An unresolved instance appears dimmed, and
        the Run button of the VI in which the instance exists appears broken. To resolve the
        data mapping discrepancies, you must manually update the instances using the
       Review and Update from Type Def. dialog box.

       Related Information

        Manually Updating Type Definition Instances

       Review and Update from Type Def. Dialog Box


11512   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11512 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11513 ordinal=11513 -->
## Error Codes and Messages

Error Codes and Messages

RefersRefers toto aa brokenbroken typetype definitiondefinition

The control or indicator is a type definition. The type definition is broken because of a
dependency, such as another contained type definition or its owning library. Check the
type definition errors to find the broken dependency.

ThisThis typetype definitiondefinition hashas unappliedunapplied changeschanges

The control or constant refers to a type definition that has changes that have not yet
been applied. The control VI may not be broken. To correct this error, apply the
changes to the type definition.

TypeType definitiondefinition insideinside thatthat samesame typetype definitiondefinition

You cannot use a type definition recursively inside the same type definition. To correct
this error, delete the type definition.

TypeType definitiondefinition notnot foundfound oror containscontains errorserrors

To correct this error, locate and open the VI for the type definition. Correct any errors in
the type definition. You also can disconnect the type definition by right-clicking the
type definition and selecting Disconnect.

TypeType definitiondefinition cannotcannot havehave arrayarray ofof arraysarrays

The type definition for the control is an array, and the control is an element of an array.
You cannot create an array of arrays.

To correct this error, make sure you do not attempt to create an array of arrays in
LabVIEW. Instead, use a multidimensional array or create an array of clusters in which
each cluster contains one or more arrays.

For more information, refer to Grouping Data with Arrays and Clusters.

TypedefTypedef hashas unappliedunapplied changeschanges

A typedef that defines the shared variable data type has unapplied changes.

                                                    © National Instruments 11513

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11513 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11514 ordinal=11514 -->
## Error Codes and Messages

Error Codes and Messages

      TypedefTypedef isis brokenbroken

       A typedef that defines the shared variable data type is broken.

      TypedefTypedef mismatchmismatch

       The typedef in this application instance is different than the variable typedef.

      ProjectProject LibraryLibrary ErrorError MessagesMessages

        This section contains reference information about possible syntax errors related to
         project libraries.

      ThisThis librarylibrary claimsclaims toto bebe ownedowned byby anotheranother librarylibrary

        This library claims to be owned by another library that does not include this library.
       Open the owning library to correct the problem.

     AA subVIsubVI whichwhich claimsclaims toto bebe partpart ofof aa dependentdependent packedpacked librarylibrary
        isis missingmissing fromfrom thatthat packedpacked librarylibrary

       LabVIEW cannot find a subVI of this VI. The subVI claims to be owned by the packed
          library in memory, but the packed library does not contain the subVI.

       The packed library might have been rebuilt without the subVI, or the subVI might be a
      member of a different packed library with the same name. If you open a different
       packed library with the same name, all VIs link to the open packed library.

      ThisThis librarylibrary isis invalidlyinvalidly licensedlicensed

        This computer does not have the license required to access this library. Contact your
        National Instruments sales representative or refer to the National Instruments Web site
         for more information on upgrading your license.


11514   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11514 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11515 ordinal=11515 -->
## Error Codes and Messages

Error Codes and Messages

TheThe owningowning librarylibrary isis brokenbroken

The library that owns this VI is broken and prevents this VI from executing. Open the
library to see what errors the owning library reports.

LabVIEWLabVIEW ClassClass ErrorsErrors

This section contains reference information about possible syntax errors related to
LabVIEW Classes.

AncestorAncestor classesclasses areare reservedreserved forfor runrun

If you load this class into a reserved class hierarchy while the class is broken, the class
remains broken until LabVIEW no longer reserves the class hierarchy. To correct this
error, stop the application that is reserving this class hierarchy.

AtAt leastleast oneone dynamicdynamic membermember VIVI ofof thisthis LabVIEWLabVIEW classclass isis brokenbroken

A dynamic member VI is a member of a LabVIEW class. LabVIEW cannot execute any
part of the LabVIEW class because one or more of the member VIs are broken.

For a class to be executable, all member VIs and all ancestor classes must be error-free.

To correct this error, examine the Error list window of the member VIs and correct any
errors you find in each VI.

TheThe parentparent ofof thisthis LabVIEWLabVIEW classclass isis brokenbroken

This VI is a member of the LabVIEW class. LabVIEW cannot execute any part of the
LabVIEW class because the parent class is broken.

To correct this error, right-click the parent class and select Show Error Window to view
errors in the Error list window. Resolve the errors that the Error list window displays.

TheThe privateprivate datadata controlcontrol forfor thisthis classclass hashas unappliedunapplied changeschanges
Control Editor File»Apply Changes

                                                    © National Instruments 11515

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11515 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11516 ordinal=11516 -->
## Error Codes and Messages

Error Codes and Messages

      TheThe privateprivate datadata controlcontrol ofof thisthis LabVIEWLabVIEW classclass isis brokenbroken

       LabVIEW cannot execute any part of this LabVIEW class because the private data
         control is broken.

       To correct this error, click the Invalid Control button in the private data control and
         correct the errors in the Error list window.

       ThisThis LabVIEWLabVIEW classclass cannotcannot findfind itsits parentparent classclass

        This VI is a member of the LabVIEW class. LabVIEW cannot execute any part of the
       LabVIEW class because LabVIEW cannot find the parent class.

       To correct this error, load the class library file ( .lvclass) or you can change the
         inheritance of the class so the class inherits from another class which LabVIEW has
        loaded.

       ThisThis LabVIEWLabVIEW classclass definitiondefinition isis corruptcorrupt

       The .lvclass file that owns this VI is corrupt and LabVIEW might not be able load
        the file.

       To correct this error, you must rebuild the LabVIEW class.

       ThisThis LabVIEWLabVIEW classclass isis missingmissing atat leastleast oneone membermember VIVI

        This VI is a member of the LabVIEW class. LabVIEW cannot execute any part of the
       LabVIEW class because LabVIEW cannot find one or more member VIs of the class.
       LabVIEW displays missing VI in the Project Window next to any member VI that is
        missing from the library.

       To correct this error, find the missing member VIs on disk and load them into memory
        or delete the member VIs from the LabVIEW class definition in the Project Explorer
       window.

         Previously saving a member VI in a version of LabVIEW that is newer than the version
       you are currently running can result in this error.


11516   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11516 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11517 ordinal=11517 -->
## Error Codes and Messages

Error Codes and Messages

TheThe parentparent ofof thisthis LabVIEWLabVIEW classclass isis privateprivate andand isis notnot accessibleaccessible fromfrom
thisthis classclass

This LabVIEW class inherits from a class whose access scope is private. The inheriting
class cannot access the parent class from outside of the library to which the parent
class belongs.

To correct this error, make the inheriting class a part of the same library, or change the
access scope of the parent class to public.

TargetTarget ErrorError MessagesMessages

This section contains reference information about possible target specific syntax
errors.

VIVI mustmust bebe reentrantreentrant toto useuse aa controlcontrol ofof thisthis typetype

To correct this error, make the VI reentrant by selecting File»VI Properties, selecting
Execution in the VI Properties dialog box, and selecting one of the reentrant execution
options.

CannotCannot mixmix staticstatic andand dynamicdynamic datadata inin aa clustercluster

Clusters cannot include both static and dynamic data. For example, in the following
illustration, the cluster includes a constant that is static and an FPGA I/O constant that
is dynamic.


To correct this error, remove either the static or dynamic data from the cluster.


                                                    © National Instruments 11517

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11517 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11518 ordinal=11518 -->
## Error Codes and Messages

Error Codes and Messages

      ConstantConstant ofof thisthis typetype isis notnot supportedsupported onon thisthis targettarget

       To correct this error, remove the constant or open the VI in a different application
         instance.

       VIVI mustmust bebe reentrantreentrant ifif aa controlcontrol ofof thisthis typetype isis onon thethe
      connectorconnector panepane

       To correct this error, make the VI reentrant by selecting File»VI Properties, selecting
        Execution in the VI Properties dialog box, and selecting one of the reentrant execution
         options.

     AA controlcontrol ofof thisthis typetype mustmust bebe onon thethe connectorconnector panepane

       To correct this error, add the control to the connector pane.

      VIVI ErrorError MessagessMessagess

        This section contains reference information about possible syntax errors related to VIs.

     LabVIEWLabVIEW ClassClass ErrorsErrors

        This section contains reference information about possible VI syntax errors related to
       LabVIEW Classes.

      DynamicDynamic dispatchdispatch VIsVIs cannotcannot bebe inin communitycommunity scopescope

       You use a dynamic dispatch VI so that child classes can override that VI and provide
         different behavior with a VI of the same name. If the dynamic dispatch VI is in
       Community scope, it is hidden from any child class that is not a friend, creating a
         situation in which a child may get errors trying to match the connector pane of a VI
        they do not know their parent has defined. To correct this error, either make the VI
          static by changing the dynamic input terminal to Required or change the VI access
        scope to Protected or Public.


11518   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11518 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11519 ordinal=11519 -->
## Error Codes and Messages

Error Codes and Messages

DynamicDynamic dispatchdispatch VIsVIs cannotcannot bebe inin privateprivate scopescope

You use a dynamic dispatch VI so that child classes can override that VI and provide
different behavior with a VI of the same name. If the dynamic dispatch VI is private, it is
hidden from child classes. As a result, errors might occur when a child class attempts
to match the connector pane of the dynamic dispatch VI.


To correct this error, make the dynamic dispatch VI static by removing the dynamic
input terminal or change the access scope of the VI to Protected or Public.


                                                    © National Instruments 11519

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11519 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11520 ordinal=11520 -->
## Error Codes and Messages

Error Codes and Messages

      OnlyOnly VIsVIs ownedowned byby aa LabVIEWLabVIEW classclass maymay useuse dynamicdynamic terminalsterminals inin thethe
      connectorconnector panepane

       Dynamic dispatch terminals are allowed only on the connector pane of VIs that are
       members of LabVIEW classes.

       To correct this error, add this VI to a class or edit its connector pane to change the
       dynamic input terminal to a simple required terminal.

       PropertyProperty datadata terminalterminal isis assignedassigned toto thethe wrongwrong sideside ofof thethe connectorconnector
      panepane

        This accessor VI has an incorrect assignment to its data terminal.

        Accessor VIs for LabVIEW class properties require the following connector pane
         configuration for the data input or output terminal:

               • Read accessor VIs—An indicator must be assigned to the second-from-top- right
             terminal.
               • Write accessor VIs—A control must be assigned to the second-from-top- left
             terminal.

       To correct this error, ensure that the connector pane of the accessor VI meets these
        requirements.

      TheThe parentparent ofof thisthis LabVIEWLabVIEW classclass isis inin communitycommunity scopescope andand isis notnot
       accessibleaccessible fromfrom thisthis classclass

        This LabVIEW class is set to inherit from a class in community access scope and cannot
       be accessed from outside of the library to which it belongs unless you declare it a
         friend of that library. To correct this error, make this class a part of the same library,
        declare this class a friend of the library, or change the access scope of the parent to
         Public.


11520   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11520 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11521 ordinal=11521 -->
## Error Codes and Messages

Error Codes and Messages

ThisThis classclass cannotcannot inheritinherit fromfrom thethe communitycommunity scopedscoped itemitem inin aa lockedlocked
librarylibrary

This LabVIEW class cannot access the referenced item because of security restrictions.
The first time you establish access to a community-scoped item in a password-
protected library, you must enter the password for that library. This prevents users
from replacing a friended class on disk with another class of the same name. To
correct this error, enter the password for the locked library in the Library Properties
dialog box.

ThisThis VIVI attemptsattempts toto overrideoverride aa staticstatic VIVI inin anan ancestorancestor classclass

You only can override parent dynamic member VIs in child classes. A VI is a dynamic
dispatch VI when it contains at least one dynamic input terminal on the connector
pane.

To correct this error, change the name of this VI so that it does not match any ancestor
VI names or create a dynamic dispatch input terminal in the ancestor VI.

PolymorphicPolymorphic VIVI ErrorsErrors

This section contains reference information about possible syntax errors related to
polymorphic VIs.

DynamicDynamic dispatchdispatch VIsVIs cannotcannot bebe membersmembers ofof polymorphicpolymorphic VIsVIs

LabVIEW does not currently support dynamic dispatch VIs as members of polymorphic
VIs. If you need this functionality, create a non-dynamic VI that calls the dynamic VI
and add the non-dynamic VI to the polymorphic VI.

InvalidInvalid polymorphicpolymorphic subsystemsubsystem

A polymorphic VI can contain either all VI instances or all subsystem instances, but not
a mixture of both.


                                                    © National Instruments 11521

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11521 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11522 ordinal=11522 -->
## Error Codes and Messages

Error Codes and Messages

      PolymorphicPolymorphic instancesinstances havehave differentdifferent connectorconnector panepane terminalsterminals

      One or more polymorphic instances have a connector pane that is incompatible with
        the connector panes of other instances.

      PolymorphicPolymorphic instancesinstances havehave differentdifferent terminalterminal directionsdirections onon
      connectorconnector panespanes

      One or more polymorphic instances have a connector pane with terminals that have a
         different direction (input/output) than the terminals of other instances.

      PolymorphicPolymorphic VIsVIs cannotcannot containcontain instancesinstances thatthat alsoalso areare polymorphicpolymorphic
        VIsVIs

       LabVIEW does not support polymorphic VIs as instances of other polymorphic VIs.

       ThisThis polymorphicpolymorphic VIVI hashas nono subVIssubVIs oror hashas subVIssubVIs withwith differentdifferent
      connectorconnector patternspatterns

        This polymorphic VI contains no subVIs or contains subVIs with different connector
       pane patterns. To correct this error, modify the polymorphic VI to contain at least one
         subVI. If the polymorphic VI contains more than one subVI, make sure all subVIs have
        the same connector pane pattern.

      ControlControl VIVI hashas unappliedunapplied changeschanges

       The control VI is not broken but has changes that have not been applied. This can
        cause other VIs to break. To correct this error, close the Control Editor window, save
        the control, or select File»Apply Changes from the menu bar.

      ThisThis objectobject isis notnot allowedallowed inin aa VIVI onon whichwhich youyou enableenable inlininginlining

        This object is not allowed in a VI on which you enable inlining. Disable inlining or
       remove this object.


11522   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11522 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11523 ordinal=11523 -->
## Error Codes and Messages

Error Codes and Messages

ThisThis VIVI doesdoes notnot matchmatch otherother VIsVIs inin thethe method;method; connectorconnector
panepane patternspatterns areare differentdifferent

All VIs that implement a method must have the same connector pane pattern.

To correct this error, compare the connector pane patterns of both this VI and the VI of
an ancestor class that implements this method.

ThisThis VIVI doesdoes notnot matchmatch otherother VIsVIs inin thethe method;method; connectorconnector
panepane terminal(s)terminal(s) areare differentdifferent

All VIs that implement a method must have the same connector pane terminals.

To correct this error, compare the connector pane terminals of both this VI and the VI
of an ancestor class that implements this method.

ThisThis VIVI doesdoes notnot matchmatch otherother VIsVIs inin thethe method;method; executionexecution
prioritiespriorities areare differentdifferent

All VIs that implement a method must have the same priority.

To correct this error, select File»VI Properties and compare the value of the Priority
option on the Execution page for this VI and the VI of an ancestor class that
implements this method.

ThisThis VIVI doesdoes notnot matchmatch otherother VIsVIs inin thethe method;method; oneone isis
reentrant,reentrant, oneone isis notnot

If one VI that implements a method is reentrant, all VIs that implement the method
must be reentrant.

To correct this error, select File»VI Properties and compare the reentrancy settings on
the Execution page for this VI and the VI of an ancestor class that implements this
method.


                                                    © National Instruments 11523

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11523 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11524 ordinal=11524 -->
## Error Codes and Messages

Error Codes and Messages

      ThisThis VIVI doesdoes notnot matchmatch otherother VIsVIs inin thethe method;method; preferredpreferred
      executionexecution systemssystems areare differentdifferent

           All VIs that implement a method must use the same preferred execution system.

       To correct this error, select File»VI Properties and compare the value of the Preferred
        Execution System option on the Execution page for this VI and the VI of an ancestor
         class that implements this method.

      ThisThis VIVI doesdoes notnot matchmatch otherother VIsVIs inin thethe method;method; thethe scopescope isis
       differentdifferent

           All VIs that implement a method must have the same scope.

       To correct this error, compare the access scope of both this VI and the VI of an ancestor
         class that implements this method.

      ThisThis VIVI isis configuredconfigured withwith inlininginlining andand automaticautomatic errorerror
      handlinghandling enabledenabled

       You cannot inline a VI on which you enable automatic error handling. Disable inlining
        or automatic error handling on this VI.

      ThisThis VIVI isis configuredconfigured withwith inlininginlining andand debuggingdebugging enabledenabled

       You cannot inline a VI on which you enable debugging. Disable inlining or debugging
       on this VI.

      ThisThis recursiverecursive VIVI isis configuredconfigured withwith inlininginlining enabledenabled

       You cannot inline a VI in a recursive cycle. Disable inlining on this VI or break the
         recursive cycle.


11524   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11524 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11525 ordinal=11525 -->
## Error Codes and Messages

Error Codes and Messages

VIVI containingcontaining SharedShared VariableVariable nodenode needsneeds toto bebe loadedloaded inin aa
projectproject
Shared Variable
RangesRanges ofof LabVIEWLabVIEW ErrorError CodesCodes

VIs and functions in LabVIEW can return numeric error codes. This book includes tables
of numeric error codes and the descriptions for these errors. Each error code table
includes a range of error codes, such as mathematics error codes or security error
codes. The error code tables are arranged in ascending order, from negative to positive
values. You can define custom error codes in the range of –8999 through –8000, 5000
through 9999, or 500,000 through 599,999.

Some numeric error codes are used by more than one group of VIs and functions. For
example, error 65 is both a serial error code, indicating a serial port timeout, and a
networking error code, indicating that a network connection is already established.

Refer to the KnowledgeBase for more information about correcting errors in LabVIEW.

3D3D PicturePicture ControlControl ErrorError CodesCodes

The 3D Picture Control VIs return the following error codes. Refer to the
KnowledgeBase for more information about correcting errors in LabVIEW.


 Code  Description

        Light cannot accept specified index. The light index must be in the range: 0 <= index <
 1456
      MAX_LIGHT_INDEX, where MAX_LIGHT_INDEX is implementation dependent.

       Passed an invalid index to the clip plane. The clip plane index must be in the range: 0 ≤ index
 1457  < MAX_CLIP_PLANES, where MAX_CLIP_PLANES is implementation dependent, but must be
        at least 6.

 1458  Matrices must be arrays of 2 dimensions of size 4.

 1459  The scene contains a value that LabVIEW does not support.

       Color component not in accepted range. All components of a color (red, green, blue, alpha)
 1460
      must be in the range 0.0 to 1.0.


                                                    © National Instruments 11525

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11525 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11526 ordinal=11526 -->
## Error Codes and Messages

Error Codes and Messages


        Code  Description

              Bad value for the shininess of the material. The shininess value must be in the range of 0.0 to         1461                  128.0.

         1462  Cannot write this value. This value is inherited from this node's parent.

         1463  This scene is missing expected nodes or contains nodes that LabVIEW does not support.

         1464  Fog start and fog end cannot be the same.

         1465  Bad value for point size. You must pass a positive number for this value.

         1466  Bad value. You must pass a positive number for this value.

         1467  Bad value. Value must be 0 < Value ≤ 1.

              Bad value passed for spotlight cutoff. The cutoff value must be in the range of 0 to 90, or be         1471                the special value 180 (no cutoff).

              Bad value passed for the exponent of a spotlight. The exponent must be in the range 0 to         1472
                 128.

         1473  Bad value passed for light attenuation. Value must be greater than or equal to 0.

              Bad value or array configuration. You must pass either an empty 2D array or a 2D array that is         1474                  at least 2 elements in each dimension.

              Bad pixmap cluster. The pixmap cluster passed is inconsistent and does not describe a valid         1475                   picture.

               Cannot add the specified node. Adding this node to the scene would result in a cyclic graph.         1476                 This is not permitted.

         1477  An index in the mesh is greater than the number of elements in the element array.

              Bad texture index size. The mesh must have no texture indices or at least one texture index
         1478
                   for every vertex.

              The libraries that support 3D rendering and operations are missing. This property or method
         1481
                cannot function without these libraries.

         1482  The view direction either cannot be determined or is colinear with the up vector.

                Font not found. LabVIEW cannot find the font at the specified path, or the font is not a True
         1520
               Type (.ttf) font. Ensure that the path you wired to the Font Path property is correct.

         1539  Valid stipple factors are 1 - 256

         1540  Cannot pass a degenerate vector for the normal of an object.

         1541  This property or method is not valid because the object is not billboarded.


11526   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11526 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11527 ordinal=11527 -->
## Error Codes and Messages

Error Codes and Messages


 Code  Description

 1542  You must set the drawable of the object before you configure billboard parameters.

 1543  Cannot pass an empty position list for billboarding.

DeploymentDeployment ErrorError CodesCodes

Deploying or uploading I/O variables, scan engine settings, hardware configuration,
and similar item types can return the following error codes. Refer to the
KnowledgeBase for more information about correcting errors in LabVIEW.


 Code         Description

 −2132869120 The assembly you are deploying is bad.

 −2132869119 The assembly handler does not support the sent command.

 −2132869118 A file I/O error occurred.

 −2132869117 The resource you are deploying is bad.

 −2132869116 The item cannot read the assembly.

 −2132869115 The item cannot create the assembly handler.

 −2132869114 A module cannot load.

 −2132869113 The item encountered an invalid pointer argument.

 −2132869112 The item cannot be found.

 −2132869111 The item is out of memory.

 −2132869110 A communication error between the host and target occurred.

 −2132869109 The system is in a bad state.

 −2132869108 The deploy header is bad.

 −2132869107 An unknown error occurred during deployment.

 −2132869106 An XML parsing error occurred.

 −2132869105 The deployment command failed.

 −2132869104 The current deployment operation has a missing dependency.

 −2132869103 The item encountered an invalid argument.


                                                    © National Instruments 11527

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11527 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11528 ordinal=11528 -->
## Error Codes and Messages

Error Codes and Messages


        Code         Description

         −2132869102 The specified file cannot be found.

                     The deployment operation caused a rollback operation, and the rollback operation         −2132869101                             failed.

         −2132869100 Logging an entry to the rollback log causes an error.

         −2132869099 A deployment transaction is in progress.

         −2132869098 A deployment transaction has not started.

         −2132869096 The deployment operation causes a rollback operation.

         −2132869095 The deployment connection timed out.

         −2132869094 The current transaction has no items to process.

         −2132869093 The current state does not allow the deployment operation.

         −2132869092 No items are left to deploy.

         −2132869091 No items are left to undeploy.

                     The deployment plug-in for this item cannot be found. Verify the proper software is         −2132869090
                            installed.

         −2132869089 An instance of the target-side deployment endpoint already exists.

                         This item cannot upload because another item with the same name exists in the         −2132869088                           project.

     EPICSEPICS ErrorError CodesCodes

       The EPICS VIs can return the following error codes. Refer to the KnowledgeBase for
       more information about correcting errors in LabVIEW.


        Code         Description

                     The data type of a process variable in the EPICS Client I/O server does not match the
         −2067353911
                       data type of the corresponding process variable in the IOC.

         −2067353910 The connection to the IOC was lost due to a network failure or an IOC error.

                     The EPICS Server I/O Server cannot be deployed because one or more PV source
         −2067353909  variables do not exist. Open the configuration dialog to check and correct broken
                       source variables.


11528   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11528 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11529 ordinal=11529 -->
## Error Codes and Messages

Error Codes and Messages


Code         Description

               Failed to connect to the MAX database (MXS) when undeploying the EPICS Client I/O−311119               server.

               Failed to connect to the MAX database (MXS) when deploying the EPICS Client I/O−311118               server.

               Failed to connect to the MAX database (MXS) when creating the EPICS Client I/O−311117               server.

−311116     The specified access type is invalid for the EPICS Client I/O server.

−311115     The specified data type is invalid for the EPICS Client I/O server.

−311114     Unable to find the specified field name on the EPICS Client I/O server.

−311113     Unable to find the specified record name on the EPICS Client I/O server.

               Failed to locate a network interface. Make sure you have properly configured a−311111
            network interface. Then deploy the EPICS Server I/O server again.

               Failed to load EPICS Base libraries. Make sure you have properly installed EPICS Base−311110
                 libraries.

            The specified process variable (PV) name includes an invalid character. The valid−311109
              character set for a PV name is: a-z, A-Z, 0-9, _, -, :, ., [, ], <, >, ;.

−311108     Unable to locate the process variable (PV).

               Failed to connect to the MAX database (MXS) when removing an empty process or−311107                folder.

               Failed to connect to the MAX database (MXS) when undeploying the EPICS Server I/O−311106               server.

               Failed to connect to the MAX database (MXS) when deploying the EPICS Server I/O
−311105
               server.

−311104      Failed to connect to the MAX database (MXS) when creating a process or folder.

               Failed to connect to the MAX database (MXS) when creating the EPICS Server I/O
−311103
               server.

−311102     The specified process variable (PV) name conflicts with an existing PV name.

−311101     The variable path must be a valid absolute URL or a machine-relative URL.

            Not a URL or an invalid URL. The EPICS Client URL or EPICS Server URL must be an
−311100
              absolute URL or a machine-relative URL.

311100      Unable to get the host name from the variable path. The IP address is used to


                                                    © National Instruments 11529

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11529 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11530 ordinal=11530 -->
## Error Codes and Messages

Error Codes and Messages


        Code         Description

                        generate the default process variable (PV) name.

                     The EPICS Server I/O server cannot support the specified data type. LabVIEW created         311101                     a string type process variable.

                     The EPICS Server I/O server cannot support the data type of the shared variable.         311102
                     LabVIEW created a string type process variable.

                      Unable to get the data type of the shared variable. LabVIEW created a string type         311103                        process variable.

     FTPFTP ErrorError CodesCodes

       The FTP VIs can return the following error codes. Refer to the KnowledgeBase for more
        information about correcting errors in LabVIEW.


        Code    Description

         15110   110 Restart marker reply.

         15120   120 Service ready in nnn minutes.

         15125   125 Data connection is open already. Transfer is starting.

         15150   150 File status is okay. Data connection is about to open.

         15200   200 Command is okay.

         15202   202 Command was not implemented because it is superfluous at this site.

         15211   211 System status or system help reply.

         15212   212 Directory status.

         15213   213 File status.

         15214   214 Help message.

         15215   215 NAME system type.

         15220   220 Service ready for new user.

         15221   221 Service closing control connection.

         15225   225 Data connection open. No transfer in progress.

         15226   226 Closing data connection.


11530   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11530 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11531 ordinal=11531 -->
## Error Codes and Messages

Error Codes and Messages


 Code    Description

 15227   227 Entering passive mode (h1,h2,h3,h4,p1,p2).

 15230   230 User logged in. Proceed.

 15250   250 Requested file action is okay. Action completed.

 15257   257 PATHNAME created.

 15331   331 Username okay. Need password.

 15332   332 Need account for login.

 15350   350 Requested file action pending further information.

 15421   421 Service not available. Closing control connection.

 15425   425 Cannot open data connection.

 15426   426 Connection closed. Transfer aborted.

 15450   450 Requested file action not taken.

 15451   451 Requested action aborted: local error in processing.

 15452   452 Requested action not taken.

 15500   500 Syntax error. Command unrecognized.

 15501   501 Syntax error in parameters or arguments.

 15502   502 Command not implemented.

 15503   503 Bad sequence of commands.

 15504   504 Command not implemented for the parameter.

 15530   530 Not logged in.

 15532   532 Need account for storing files.

 15550   550 Requested action not taken.

 15551   551 Requested action aborted: page type unknown.

 15552   552 Requested file action aborted.

 15553   553 Requested action not taken.

GeneralGeneral LabVIEWLabVIEW ErrorError CodesCodes

LabVIEW VIs and functions and VI Server properties and methods can return the

                                                    © National Instruments 11531

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11531 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11532 ordinal=11532 -->
## Error Codes and Messages

Error Codes and Messages

         following error codes. Refer to the KnowledgeBase for more information about
         correcting errors in LabVIEW.


        Code         Description

         −2147467259  Unspecified error.

         −1967345152  Invalid refnum. A specified refnum was not valid.

         −1967345151  Invalid property code. The specified property code is not valid for this refnum.

         −1967345150  Invalid privilege ID. The specified privilege ID is out of range.

         −1967345149  Invalid access type. The specified access type is not valid.

         −1967345148  Invalid argument. One of the specified arguments is invalid.

         −1967345147  Entry not found. The requested entry could not be found.

         −375012     A JSON numeric value is out of the range of a LabVIEW numeric type.

                     LabVIEW failed to read or write a -Infinity or +Infinity floating-point value. You must         −375011                       enable LabVIEW JSON extensions to allow support for a value of Infinity.

                     LabVIEW failed to read or write a NaN floating-point value. You must enable LabVIEW         −375010                   JSON extensions to allow support for a value of NaN.

         −375009     The JSON string contains an invalid multi-dimensional array.

         −375008     The array has an invalid number of dimensions.

                     The cluster or JSON string contains an invalid number of elements. When strict
         −375007      validation is enabled, the number of elements in the JSON string must match the
                    number of elements in the input cluster.

         −375005     Type mismatch between JSON and LabVIEW.

         −375004     The path cannot be found in the JSON string.

                     The JSON string is invalid. JSON strings must be encoded in UTF-8 and must
         −375003
                     conform to the JSON grammar.

                     The cluster element name is invalid. Each element of the cluster must have either a
         −375002
                      unique name or no name, such as an empty string.

         −375001     The JSON root container must be an array or cluster.

                     The data type cannot be converted to or from JSON. Supported data types include
         −375000
                         arrays and clusters of booleans, numerics, strings, and other arrays and clusters.

         −120000      SignalExpress is required to open this Express VI. Install SignalExpress or visit


11532   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11532 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11533 ordinal=11533 -->
## Error Codes and Messages

Error Codes and Messages


Code         Description

             www.ni.com/signalexpress to download an evaluation version.

             Device driver not present or not supported. The device driver needed to execute the
−4850         In Port and Out Port VIs is not present. LabVIEW does not support this device driver
           on Windows Vista or later.

             Clipped Floating-point data to fit the range [-1.0, 1.0]. The floating point data was−4824              outside of the range [-1.0, 1.0]. The values were clipped to fit within this range.

           A buffer underflow has occurred. A buffer underflow has occurred because the−4820              application is not writing data quickly enough.

            The sound driver or card does not support the specified operation. The sound driver
−4803        or card cannot accommodate the specified configuration. Ensure that the
             parameters values are within the supported range for the hardware and drivers.

            LabVIEW cannot locate a palette item. LabVIEW cannot locate a palette item. Verify
             the path for each item in the items array. The file might have been moved or deleted,
−4407        or the path might be incorrectly formatted for the operating system. For example,
             use \ as path separators on Windows, : on OS X (32-bit), and / on Linux and OS X
                 (64-bit).

           A VI item in the palette data array is not supported in this version of LabVIEW. A VI
−4406        item in the palette data array is not supported in this version of LabVIEW. This error
            can occur if you use a VI that is not supported in the LabVIEW Run-Time Engine.

            The value for palette width is invalid. The value for palette width must be 0 or−4404                greater.

           A palette item is invalid. A palette item is invalid. Verify the path for each item in the−4403             items array. Paths to VIs and palette files (.mnu) must be valid.

            The palette view format is invalid. The palette view format must be Icons, Icons and
−4402         Text, or Text. Select Customize»View This Palette As from the Controls or Functions
               palette to change the palette view format.

            The specified file is not a valid palette file (.mnu). The specified file is not a valid
−4401         palette file (.mnu). Enter a path to an existing palette file to read data from the
               palette file. Enter a path to a valid palette file to write data to the file.

            The palette type is invalid. The palette type input is invalid. The palette type value
−4400        has enumeration values of Controls or Functions. The value provided was beyond
             the defined range.

           DIAdem could not be started. You must have DIAdem 9.1 Service Pack 2 or later
−2584
               installed to use the DIAdem Report Express VI.


                                                    © National Instruments 11533

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11533 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11534 ordinal=11534 -->
## Error Codes and Messages

Error Codes and Messages


        Code         Description

                     The Write to Measurement File Express VI cannot append new data to frequency
                    domain waveforms. Frequency domain waveforms are constructed with a base
                       frequency f0 and a delta frequency df. The frequency for a data point is then
         −2580        calculated as f0+N*df. This calculation leads to erroneous results if data is appended
                         to the waveform. This error can occur when you write a frequency domain waveform
                         to a file with Segment Headers set to One header only. Set Segment Headers to
                   One header per segment to correct this error.

                    An input parameter is invalid. For example if the input is a path, the path might
                        contain a character not allowed by the OS such as ? or @. If you receive this error         1                        while trying to run File I/O VIs, refer to the KnowledgeBase at ni.com for more
                         information.

                   Memory is full. If you receive this error while developing a large application or
         2              storing large sets of data in LabVIEW, refer to the KnowledgeBase at ni.com for more
                         information.

         4          End of file encountered.

         5               File already open.

                        Generic file I/O error. A possible cause for this error is the disk or hard drive to which
                     you are trying to save might be full. Try freeing up disk space or saving to a different
         6             disk or drive. Another possible cause for this error is there might be a bad network
                        connection. For example, the network connection is down or a network cable is
                       unplugged.

                             File not found. The file might be in a different location or deleted. Use the command
                     prompt or the file explorer to verify that the path is correct. Another possible cause
         7                            for this error is there might be a bad network connection. For example, the network
                       connection is down or a network cable is unplugged.

                             File permission error. You do not have the correct permissions for the file. To correct
                            this error, verify that the file is not in use by another application and that file
                       permissions are set correctly. On Windows, navigate to the file, right-click the file,
                          select Properties, and set the Read-only option in the dialog box. On Linux or Mac
         8         OS X use chmod to set file permissions. If you only need read access, you can use the
                       Open/Create/Replace File function with the access input set to Read-only. If you
                         receive this error while trying to build an executable in LabVIEW 8.5 or later with the
                       Report Generation toolkit 1.1.2 or later , refer to the KnowledgeBase at ni.com for
                    more information.

                        Disk full. The disk or hard drive does not have enough free space to complete the
         9
                         operation. Try freeing up disk space or saving to a different disk or drive.

         10            Duplicate path. If you receive this error while building an application in LabVIEW,

11534   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11534 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11535 ordinal=11535 -->
## Error Codes and Messages

Error Codes and Messages


Code         Description

                refer to the KnowledgeBase at ni.com for more information. If you receive this error
              while using a File I/O function or VI, you may be attempting to overwrite a file or
               folder that already exists. Refer to the specific function or VI reference topic in the
            LabVIEW Help for information about overwriting files or folders.

11          Too many files open.

12         Some system capacity necessary for operation is not enabled.

               Failed to load dynamic library because of missing external symbols or dependencies,13              or because of an invalid file format.

14          Cannot add resource.

             Resource not found. This error might occur if you remove the front panel of the VI15           when building a stand-alone application.

16          Image not found.

17          Not enough memory to manipulate image.

18          Pen does not exist.

19            Configuration type invalid.

20            Configuration token not found.

21            Error occurred parsing configuration string.

22            Configuration memory error.

23         Bad external code format.

24            External subroutine not supported.

25            External code not present.

26            Null window.

27           Destroy window error.

28            Null menu. If you reconnect a removable device, restart LabVIEW to use the device.

29             Print aborted.

30         Bad print record.

31             Print driver error.

32           Operating system error during print.

33         Memory error during print.

                                                    © National Instruments 11535

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11535 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11536 ordinal=11536 -->
## Error Codes and Messages

Error Codes and Messages


        Code         Description

         34             Print dialog error.

         35           Generic print error.

         36             Invalid device refnum.

         37           Device not found.

         38           Device parameter error.

         39           Device unit error.

         40          Cannot open device.

         41           Device call aborted.

         42           Generic error.

                       Operation cancelled by user. If the VI or function that throws this error has an error
                      out parameter, wire error out to the selector terminal of a case structure to avoid
                            this error message. If you are using the Open/Create/Replace File function or Open/
                        Create/Replace Datalog function, you can wire cancelled to the selector terminal of
         43           the case structure instead. If the VI or function does not have error out, you can edit
                        the error handling within the VI or function to avoid this error. Double-click the VI or
                         function and replace the general error handling with an error out indicator or some
                        other form of error handling. Save the new VI or function to a different directory than
                  vi.lib so you do not overwrite the original.

         44           Object ID too low.

         45           Object ID too high.

         46           Object not in heap.

         47         Unknown heap.

         48         Unknown object (invalid DefProc).

         49         Unknown object (DefProc not in table).

         50          Message out of range.

         51            Null method.

         52         Unknown message.

         67            Interapplication Manager initialization error.

         68         Bad occurrence.

         69           Handler does not know what occurrence to wait for.


11536   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11536 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11537 ordinal=11537 -->
## Error Codes and Messages

Error Codes and Messages


Code         Description

70           Occurrence queue overflow.

71              File datalog type conflict.

72          Semaphore not signaled.

73            Interapplication Manager unrecognized type error.

74         Memory or data structure corrupt.

75            Failed to make temporary DLL.

            Format specifier type mismatch. A format specifier does not match the data type of81                   its corresponding argument in a Format Into String or Scan From String function.

           Unknown format specifier. A bad format specifier was found in the Format String82              input to a Format Into String or Scan From String function.

            Too few format specifiers. There are not enough format specifiers to match all of the83
            arguments of a Format Into String or Scan From String function.

            Too many format specifiers. There are more format specifiers than the number of84
            arguments of a Format Into String or Scan From String function.

            Scan failed. The input string does not contain data in the expected format. The Scan
           From String function was unable to scan its input because the data was not in the
             expected format. Right-click the Scan From String function and select Edit Format
85              String to configure the format string to match the input data. You also can receive
                this error if the Scan From File or Scan From String functions reach the end of the
                    file. Refer to the KnowledgeBase at ni.com for more information about this use case.

               Error converting to variant. An error occurred converting from LabVIEW type to OLE
87               variant type.

88           Run-time menu error.

89           Another user tampered with the VI password.

90            Variant attribute not found.

            The data type of the variant is not compatible with the data type wired to the type
91
               input.

97         A null or previously deleted refnum was passed in as an input.

               Incorrect file type. Attempted to read from or write to a file of a type incompatible
98
             with the operation. This normally is a user data file.

               Incorrect file version. Attempted to read from or write to a file of a version
99
             incompatible with the write/read function version. This file normally is a user data

                                                    © National Instruments 11537

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11537 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11538 ordinal=11538 -->
## Error Codes and Messages

Error Codes and Messages


        Code         Description

                                   file.

         100             File contains erroneous data. This normally is a user data file.

                         Unflatten or byte stream read operation failed due to corrupt, unexpected, or         116                        truncated data.

                         Directory path supplied where a file path is required. A file path with the filename is         117                          required, but the supplied path is a path to a directory.

         118         The supplied folder path does not exist.

                     The resource you are attempting to open was created in a more recent version of         122
                     LabVIEW and is incompatible with this version.

         123         A timeout occurred.

         124         A string contained an unexpected null character.

                    A stack overflow occurred. To correct this error, restart LabVIEW and review your         125                     code for recursive data structures.

                     The VI is not in a state compatible with this operation. This error can occur for
                          several reasons. This error can occur if you attempt to edit a VI that is running or
                        reserved for running. This error also can occur if you attempt to open a reference to a
                            VI that is running or reserved for running. A VI is reserved for running when you open
                     a reference to the VI by wiring a type specifier VI Refnum to the Open VI Reference
                          function, or when you have a Static VI Reference linked to the VI within a running VI.
                         This error also can occur if you try to run a VI using the run method while the target         1000                            VI is running or reserved for running. To correct this error, ensure the target VI is idle
                        or reentrant. If it is reentrant, use the Open VI Reference function with the options
                        input set to 0x08 to prepare the VI for reentrant run or use the Open VI Reference
                         function with the type specifier VI Refnum wired to a strictly typed VI reference. This
                          error also can occur if you attempt to obtain a VI's image while the VI is being
                       modified programmatically. Wait until the VI is not being modified to get the image
                          of a panel or diagram.

                     The VI front panel is not open. Use the Window Appearance page to configure if the
         1001          front panel is shown when the VI is run or loaded. You also can use the Front
                      Panel:Open method to open the front panel programmatically.

         1002        The VI cannot run because it has a front panel control in an error state.

                     The VI is not executable. This error may occur because the VI is either broken or
                        contains a subVI that LabVIEW cannot locate. Select File»Open to open the VI and
         1003
                            verify that you can run it. Refer to the KnowledgeBase at ni.com if you receive this
                          error in one of the following situations: while using the VI Server to call a VI

11538   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11538 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11539 ordinal=11539 -->
## Error Codes and Messages

Error Codes and Messages


Code         Description

             dynamically or while building an application.

1004        The VI is not in memory.

                VI execution has been disabled in the VI Properties dialog box. Open the Execution1005            page of the VI Properties dialog box to change the settings for the VI execution.

1006       FPDCO on connector pane thinks it is constant.

1007       No IP record in summary.

1008        Cannot load connector pane.

1009          Variant tag out of range.

1010       No default or operate data.

1011           VI Creation failed.

1012        Cannot load block diagram.

            Cannot load front panel. Make sure you include the front panel of the VI when1013              building a stand-alone application.

1014          Linker error.

1015          Printer is not responding. Check printer configuration.

1016        Cannot load History.

1017           VI has been modified on disk since it was last loaded or saved.

1018         Unspecified error occurred.

           One or more untitled subVIs exist. This file cannot be saved until all dependent files
1019            have been named.

1022         Wizard Template not found.

1023         Wizard template does not have a diagram.

1024           Call Instrument aborted.

1025          Application Reference is invalid.

1026           VI Reference is invalid.

             For the requested operation, the reference cannot be reserved as requested, is in an
1027         improper reservation mode, or the execution state must be set to running or
              reserved.

1028          Attribute selector is invalid.

                                                    © National Instruments 11539

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11539 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11540 ordinal=11540 -->
## Error Codes and Messages

Error Codes and Messages


        Code         Description

         1029           VI Server property is read-only.

         1030           VI Reference is already reserved for editing.

         1031           VI Reference type does not match VI connector pane.

                            VI Server access denied. If this error is returned from the Open VI Reference function
                    on a remote connection, use the VI Server page of the Options dialog box to ensure
                         that the VI is exported. If this error is returned from a Property or Invoke Node, the
         1032         property or method might not be allowed for remote VI Server connections. For
                       example, the Application:All VIs In Memory property is allowed locally, but remotely
                     you should use the Application:Exported VIs In Memory property instead. Refer to
                        the help for the property or method to determine if it is allowed remotely.

         1033        Bad run-time menu file version.

         1034        Bad run-time menu file.

         1035         Operation is invalid for this type of VI.

         1036        Method selector is invalid.

         1037         Incompatible VI Server protocol version.

         1038         Required parameter missing.

         1039           VI was aborted.

         1040           VI is password protected.

         1041          Incorrect password.

         1042         Attempted recursive call.

                     The property or method is not supported in this version of LabVIEW. This error can
         1043         occur if you use a property or method that is not supported in the LabVIEW Run-
                     Time Engine.

         1044           VI is locked.

         1045          Null Refnum passed to Close Reference.

                    A LabVIEW file of that name already exists in memory, or exists within a project
         1051           library already in memory. To resolve this error, give the file a unique name that does
                       not already exist in the application instance.

         1052        The LabVIEW filename is invalid.

         1054        The specified object was not found.

         1055         Object reference is invalid.

11540   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11540 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11541 ordinal=11541 -->
## Error Codes and Messages

Error Codes and Messages


Code         Description

1056          Specified object is not scriptable in this version.

1057        Type mismatch: Object cannot be cast to the specified type.

1058          Specified property not found.

1059        Unexpected file type.

1060         Object cannot contain (own) the specified object.

1061        Unable to create new object.

1062          Specified objects cannot be wired together.

1063          Specified terminal not found in the object.

1066        Hardware open error.

1067        Hardware close error.

1068        Hardware transact error.

1069        Hardware DLL missing.

1070        Hardware no session error.

1071        LabVIEW cannot locate the specified method.

1072          This property or method is not yet implemented.

              This property is writable only when the VI is in edit mode, or this method is available
1073         only when the VI is in edit mode. Refer to the KnowledgeBase for more information
            about this error.

1074        Cannot create a control/indicator for the specified terminal.

1075        Cannot create a constant for the specified terminal.

1076           VI is not debuggable.

1077          Invalid property value.

1082         Operation not valid for strict type definition instance.

           Wrong control type. The operation is not allowed on this kind of control or a control
1086
               at this level.

1087         There is no DataSocket information available for the object.

1088        Bad value for parameter.

1089          Error occurred while executing script. Error message from server: %s.


                                                    © National Instruments 11541

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11541 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11542 ordinal=11542 -->
## Error Codes and Messages

Error Codes and Messages


        Code         Description

         1090          Specified object cannot be moved.

         1091        The VI Server or client received an unrecognized message.

                    Queue and notifier references of the same name must be obtained using the same
                       data type. When you obtain a reference to a queue or notifier, you can specify which
                       data type the mechanism stores. You can receive this error when future requests to
                        obtain a reference to the same mechanism do not wire the same data type as the         1094                           original specified data type. Unnamed mechanisms do not have this restriction,
                      because each request to obtain an unnamed mechanism creates a new mechanism.
                         Refer to the KnowledgeBase at ni.com for more information about avoiding this
                             error.

                         This container cannot be left without a subtype. Right-click the container border and         1095
                          select Replace or drag new subtype.

                     The Open VI Reference function cannot prepare a non-reentrant VI for reentrant run.         1096
                            Verify the values you wired to the Open VI Reference function.

                    An exception occurred within the external code called by a Call Library Function
                      Node. The exception might have corrupted the LabVIEW memory. Save any work to a         1097                  new location and restart LabVIEW. Verify the values you wired to theCall Library
                       Function Node.

                     Cannot disconnect type definitions or polymorphic VIs if the block diagram is not
         1098                           available.

                  No object of that name was found. No reference could be returned. You can use the
                       Obtain Queue or Obtain Notifier function to look up a queue or notifier by name. If         1100                        create if not found? is FALSE and a queue or notifier with that name was not found,
                     LabVIEW returns this error.

         1102        The string wired to the xml string input is empty.

         1103        The XML tag describing the type of data is not recognized.

         1104       No end tag was found for an XML start/end tag pair.

         1105        An unknown or unexpected XML tag was discovered.

         1106        The XML tag describing the type of data does not match the wired type.

         1107        The XML enumerated type choice(s) does not match the wired type.

         1108       XML value text is illegal or out of range for type and/or format.

         1109        Unsupported data type.

         1110       No longer used.

11542   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11542 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11543 ordinal=11543 -->
## Error Codes and Messages

Error Codes and Messages


Code         Description

1111         Release Semaphore called on a semaphore that was not currently acquired.

1122        Refnum became invalid while node waited for it.

            You cannot create an object (such as control caption) in built applications. You must1123              create these objects in the LabVIEW development system.

                VI is not loadable.In a built application, this error might occur because the VI being
             loaded was last compiled for a different OS or with CPU features, such as SSE, that
                this target does not support. In this case you must rebuild the application for the
1124          target OS and make sure SSE compiler settings in the build specifications match the
               target platform. This error also might occur if the VI is a polymorphic VI, which
             cannot be loaded in the LabVIEW Run-Time Engine. You must load an instance of the
             polymorphic VI instead of the polymorphic VI itself.

1125           File version is later than the current LabVIEW version.

                VI version is too early to convert to the current LabVIEW version. Refer to the
1126         Converting VIs topic in the LabVIEW Help for more information about converting VIs
              to the current LabVIEW version.

1127        Cannot instantiate template VI because it is already in memory.

1128         Input unit is not compatible with the current unit.

            You cannot assign the same numeric value to two or more strings in a ring control.
            You also cannot assign the same string value to two or more strings in a combo box
1129               control. If you receive this error while trying to write to the Strings and Values []
              property of a control, refer to the KnowledgeBase at ni.com for more information.

            The VI Server connection peer is unresponsive. Refer to the Connection
1130         Responsiveness: Check Method topic in the LabVIEW Help for more information
            about connection polling.

1131        You cannot use this property with this system control.

1135        The tree control's active item is not valid for this property.

1136        You wired an invalid item tag to a tree control property or method.

1137         Tree control's internal data is corrupt.

           An exception occurred within external code called by LabVIEW. This might have
1138         corrupted the LabVIEW memory. Save any work to a new location and restart
             LabVIEW.

1144        Cannot insert VI in a subpanel control because VI is already open.

1145        Cannot open VI because it is already in a subpanel control.

                                                    © National Instruments 11543

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11543 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11544 ordinal=11544 -->
## Error Codes and Messages

Error Codes and Messages


        Code         Description

         1146        You attempted an operation that would change a child-only item into a parent item.

         1147        Cannot insert a remote VI in a subpanel control.

         1148          This property is read only while the VI is in a subpanel.

                     Cannot close or set the state of a closed front panel. The front panel must already be         1149
                    open before you close it or set its state.

                     Cannot open a front panel that is already open. To set the state of the open front         1150                         panel, use the Front Panel Window:State property.

         1151          Invalid input for front panel state.

                   Memory full error, possibly due to a data format not matching expected data type.
                         This is caused by trying to allocate a buffer that is too large for memory. Although
                     normal allocation might run the system out of memory, frequently an out of
         1156       memory error is caused by interpreting the data incorrectly and treating something
                         that is data as the size of the data. Before assuming that the system needs more
                  memory to complete the operation, make sure the read format you are requesting is
                           valid for the data being read.

         1157        You cannot use this property with a numeric indicator.

                           Invalid return parameter for Call Library Function Node. The return type must be
         1174          Void, Numeric, or String. Numeric return types are passed by value. Strings return
                        types are passed as a C String Pointer or a Pascal String Pointer.

                           Invalid array dimension in Call Library Function Node configuration. An array must         1175                      have 1 or more dimensions.

                           Invalid waveform dimension in Call Library Function Node configuration. A         1176                     waveform must have 0 or 1 dimensions.

                           Invalid data type for Call Library Function Node parameter. Void can be used only as
         1177
                         return type of function.

                     Cannot show or hide the label on its own. Label visibility is controlled by the label
         1186
                       owner.

         1187          Internet Explorer is required for this operation but it is not installed.

                     The static VI reference is not configured. Right-click the Static VI Reference function
         1188        on the block diagram and select Browse for Path. Navigate to the VI for the reference
                    and click the Open button to configure the reference.

         1190        The operation is not allowed when the control has key focus.

         1191        The wire already has a probe on it.

11544   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11544 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11545 ordinal=11545 -->
## Error Codes and Messages

Error Codes and Messages


Code         Description

1192       No data range set for digital displays.

          When a Boolean control has a latch mechanical action, you cannot use the Value
              property to read or write its value. When a Boolean control is configured with a
               latching mechanical action, the Value property always returns an error. Due to race1193
              conditions that can occur when you have a Boolean value with latching mechanical
               action, you cannot programmatically read Boolean values that are set with a
               latching mechanical action.

              This Express VI requires DIAdem 8.1 or later and the LabVIEW DIAdem Connectivity
1194          VIs version 2.1 or later. The Connectivity VIs are available for free download from
              ni.com. Refer to the National Instruments Web site to download the VIs.

            Cannot list the same terminal more than once in the grown region of the expandable1196
               subVI.

              This operation is not valid for static VI references. To run a VI using a static VI
1197          reference, use an Invoke Node to call the Run VI method. Set the Invoke Node class
              to VI and select the Run VI method.

            The VI is not in a state compatible with this operation. Change the execution mode of1198             the referenced VI to reentrant for this operation.

            The dimension of the array passed in does not match the expected dimension for the1301              operation.

1303        The elements of the array are not unique. There are duplicated items in the array.

1304        The array index is outside of the array bounds.

1305        The required page cannot be found.

1306        Unable to load new code resource to the node. Code resource already loaded.

            Subpanel control could not open the VI window. You tried to insert a VI into a
1307         subpanel control, but the front panel or block diagram window you want to insert
            does not exist.

1308        The Property or Invoke Node is not linked to a front panel control.

1309        The Property or Invoke Node reference input terminal is already wired.

            The object is not in the same VI as the Property or Invoke Node. The control
1310          reference of the control does not belong to the VI that owns the Property or Invoke
            Node.

            The input for class name is not correct or is in the wrong format. The input for class
1311
          name is not correct or is in the wrong format. The correct format should begin with


                                                    © National Instruments 11545

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11545 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11546 ordinal=11546 -->
## Error Codes and Messages

Error Codes and Messages


        Code         Description

                        the class type followed by the path to the object using the long names. For example,
                            VI Server:Generic:GObject

                         Structure frame index is out of range. This error occurs when you use an index value
         1312          that is out of range to access a frame in a Case, Stacked Sequence, or Event
                           structure.

         1313        You cannot use this property on a control in a radio buttons control.

                     You cannot use this property on an instance of a type definition set to update         1314                        automatically from the master copy of the type definition.

         1315        You have attempted to create a data type with a descriptor that is too large.

         1319        Cannot insert a VI into a subpanel that is not in a running state.

                           In run mode, LabVIEW cannot get or set a property for a control part that has not         1320
                     been created.

                        NI License Manager is not initialized. Verify that NI License Manager is installed on
         1321         the computer by selecting Start>>All Programs>>National Instruments>>NI License
                      Manager.

         1322          Invalid project build reference.

                    A LabVIEW file from that path already exists in memory, or exists within a project
         1357           library already in memory. To resolve this error, give the file a path that does not
                        already contain a LabVIEW file in any open application instance.

                     The splitter bar cannot be moved to this position because it violates the minimum or
                  maximum size of a descendant pane. When LabVIEW tries to move the splitter bar to
                        the specified position, at least one pane shrinks smaller than its set minimum size.
                        For example, if you have a VI with one vertical splitter bar, and the minimum size of         1358                        the left pane is 50, wiring 10 to the Splitter Position property will return this error. To
                          correct this error, set the minimum size of the pane to a smaller value, or wire a value
                         to the Splitter Position property that does not shrink the pane beyond its minimum
                              size.

         1359        A drag cannot start because a previous drag transaction is still pending.

                     Cannot provide the type of data requested for this drag and drop operation. To
                          correct this error, ensure that a drag and drop operation is in progress when you call
         1360
                            this function and that the data type and drag data name match what is currently
                          available during the drag and drop operation.

                     The name or data type of a drag data element conflicts with the built-in LabVIEW
         1361                       drag data types. You cannot use the prefix LV_ on a data name.


11546   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11546 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11547 ordinal=11547 -->
## Error Codes and Messages

Error Codes and Messages


Code         Description

            Cannot use this property with this string display mode or if word wrapping is
1362         enabled. Change the display mode to 0 (normal) and/or disable word wrapping to
             use this property.

1363        The specified name or GUID is invalid.

1364        The provider plug-in is not installed or somehow corrupt.

1365          Failed to generate a valid GUID.

            You cannot hide or show the scroll bars of a subpanel control when a VI containing1366              multiple panels is inserted.

1370        The selected build failed to complete.

           A Diagram Disable structure cannot have a default frame. This error occurs when you
1376           try to use the Default Frame property with a Diagram Disable structure. You can use
                this property only with the Conditional Disable structure.

           A Diagram Disable structure cannot have conditions. You can use the Conditions
1377         property and the Get Frame Index method only with the Conditional Disable
               structure.

            Cannot set the Active Frame property on a Conditional Disable structure. This error
             occurs when you try to use the Active Frame property with a Conditional Disable
1378          structure. You cannot use this property with a Conditional Disable structure because
              conditions determine the active frame. You can use this property only with a
            Diagram Disable structure.

              License checkout failure. Unable to checkout the requested license feature because
1380             the license is invalid or does not exist.

1381        Cannot create semaphores with a size less than one.

            Cannot start dragging because duplicate names for drag data types were passed to
             the Start Drag method or Drag Starting? event. To correct this error, ensure that the
1384
           names you use for drag data are unique in each element of the data array for the
           method or event.

            Cannot start a drag and drop operation because the data provided is invalid. To
1385          correct this error, verify that the drag data array is not NULL and that all elements
            have names and data fields.

            The block diagram you are attempting to access belongs to a VI that is either in
1388         evaluation mode or has an invalid license. To correct this error, you must obtain a
               valid license for the VI and its containing library.

1389        You are attempting to save or copy a VI that is either in evaluation mode or has an

                                                    © National Instruments 11547

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11547 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11548 ordinal=11548 -->
## Error Codes and Messages

Error Codes and Messages


        Code         Description

                           invalid license. To correct this error, you must obtain a valid license for the VI and its
                        containing library.

                     You attempted to open a VI Server reference to an out-of-scope VI. A VI can open VI
                        Server references only to other VIs that it could call as subVIs. After the reference is         1390
                      opened, that VI can return the reference to other VIs that could not normally open
                        the reference.

         1396        Cannot convert text from the source character set to the destination character set.

                     You have not wired a required input on this subVI. To correct this error, wire the         1397
                        required input.

         1398        The subVI cannot be inlined because there is a local variable in the block diagram.

                     The subVI cannot be inlined because a front panel terminal is not on the root
         1399         diagram. For example, this error might occur when a front panel terminal is inside a
                           structure.

         1430        The path is empty or relative. You must use an absolute path.

                     The specified format cannot be used with floating point data. For example,         1432
                      hexadecimal notation is not a valid format for floating point numbers.

         1434        The precision is greater than the maximum allowed value for this format.

         1436        Numeric precision cannot be negative.

         1438         Archive version is later than the current LabVIEW version.

                    A project library cannot be copied to the same folder as the original library because
         1439         the new library files would conflict with the original library files on disk. You must
                          specify a different location on disk when copying a project library.

                     The filename does not match the expected name. The file specified must have the
         1440
                   same filename as the original file.

                    Debug connection refused by specified server. Only one debug connection is allowed
         1443
                       per application or shared library.

         1444       No VIs to download from application, connection closed.

                   Open VI Reference no longer matches VIs in memory by filename. A filename is no
                        longer sufficient because the full name of a VI now includes any owning libraries. You
         1445
                      can use the Strip Path function to wire the filename as a string, but this will not work
                            for VIs in libraries.

                      There was a name conflict while saving for previous. VIs in libraries are saved in the
         1447
                      form LIBRARYNAME_VINAME. There is already a VI in this hierarchy with this name.

11548   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11548 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11549 ordinal=11549 -->
## Error Codes and Messages

Error Codes and Messages


Code         Description

1449          Arrays must have at least one dimension and a maximum of 63 dimensions.

           One or more untitled library dependencies exist. This file cannot be saved until all1450            dependent files have been named.

           One or more untitled dependencies exist. This file cannot be saved until all1451
            dependent files have been named.

              This library was saved in an earlier version of LabVIEW. It must be loaded and saved1452                in the current version of LabVIEW.

1453        You may only set the vertical arrangement on a label, caption or free label.

1454        LabVIEW classes cannot be flattened as XML in this version of LabVIEW.

              Revert failed. This item has been edited in another context on this machine. Only1455              that instance can be reverted.

              Specified ability not supported by the library. Verify the ability name does not1468              contain spaces.

1469          Specified ability already exists. You cannot add an ability multiple times.

              Specified folder is outside the library. You cannot add library items to folders that do1470
             not belong to the library.

            Cannot change width of the plot legend when you configure the plot legend to
              automatically resize, or if the legend has more than one entry and you arrange the
1483          plot legend horizontally. Right-click the graph or chart and deselect Autosize Plot
            Legend in the shortcut menu to disable automatic resizing and make sureyou
             arrange the plot legend vertically.

            LabVIEW cannot inline the subVI into its calling VIs because the block diagram of the
1484         subVI contains an implicit control reference. To correct this error and inline the
               subVI, remove the implicit control reference.

            LabVIEW cannot inline the subVI into its calling VIs because the block diagram of the
1485         subVI contains an implicit Property Node or Invoke Node. To correct this error and
                inline the subVI, remove the implicit Property Node or Invoke Node.

1488        The migration file cannot load because it is no longer supported.

1489        The migration file cannot load because its content is not valid or is corrupt.

            The migration file cannot load because it makes references to data that does not
1490
                exist or is invalid.

                      If you obtain a queue reference in one application instance, you cannot use that
1491
            queue reference in another application instance. You cannot use queues for

                                                    © National Instruments 11549

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11549 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11550 ordinal=11550 -->
## Error Codes and Messages

Error Codes and Messages


        Code         Description

                     communication between LabVIEW application instances.

                                       If you obtain a notifier reference in one application instance, you cannot use that
         1492           notifier reference in another application instance. You cannot use notifiers for
                     communication between LabVIEW application instances.

                     The save operation failed because multiple files of the same name cannot be saved         1493                          into a single LLB. To correct this error, save to a folder instead of an LLB.

         1497        Cannot unlock a library for edit when instances in running VIs exist.

         1498          Library has errors. Fix the errors before attempting this operation.

                          Library has edits in another context. Sync up changes before attempting this         1499                         operation.

                                       If you obtain a user event reference in one application instance, you cannot use that
         1500         user event reference in another application instance. You cannot use user events for
                     communication between LabVIEW application instances.

         1502        Cannot save a bad VI without its block diagram.

         1503        Cannot save a clone of a reentrant VI.

         1504        Cannot save a remote panel.

                    An error occurred in the Call Library Node processing. This error was most likely a
         1517          configuration mismatch between the calling conventions of the Call Library Node
                    and the function being called in the DLL.

                      Passed an invalid number of strings to the Strings [ ] property. You must pass either 1         1523                           string or 6 strings.

                     The target version for save is not formatted correctly. The target version for save
         1524        must be a valid LabVIEW version in the form x.xor xx.x, where xis a number. Refer
                         to the LabVIEWHelpfor a list of valid versions.

         1526          This property does not apply when the plot legend of a graph or chart is in tree view.

                      There are too many nested VI calls. This typically results from recursion without a
         1529
                       proper termination condition to stop the recursion.

                     The target application instance is currently being destroyed. You cannot get a new
         1532
                         reference to the application instance or load a VI in the application instance.

         1533        A shared variable node cannot be created from the specified terminal.

                     The semaphore you specified does not exist. LabVIEW cannot return a reference to
         1534
                        the semaphore. This error might occur if the create if not found input of the Obtain

11550   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11550 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11551 ordinal=11551 -->
## Error Codes and Messages

Error Codes and Messages


Code         Description

           Semaphore Reference VI is FALSE and LabVIEW cannot find a semaphore with the
          name you specify.

            The semaphore reference you specified is invalid. To correct this error, make sure the1535              reference to the semaphore is valid.

            LabVIEW attempted a read, write, or seek on a file opened in unbuffered mode, and
             the data size is not a multiple of the disk sector size. Use the Get Volume Info
1544          function to return the proper sector size. If you do not have the right amount of data
              to align to a sector size, you must pad the data with filler data and delete the filler
             data before LabVIEW reads back the file.

            LabVIEW attempted to read or write data to a file opened in unbuffered mode, and
             the data is not aligned properly. LabVIEW determines how data is aligned and you1545
             cannot alter that alignment. If this error occurs, you must enable buffering and
            reopen the file.

1546        The VI must be in a project to use this property.

           Queue refnum cannot be obtained with a size of zero. Size input must be a positive1548
           number or -1 for unlimited size.

1550        The license for the I/O server type is invalid.

            The LabVIEW Run-Time Engine cannot load the polymorphic VI. This error occurs in
1553         stand-alone applications when the VI is polymorphic. To correct this error, load an
              instance of the polymorphic VI rather than the polymorphic VI itself.

1554        The current LabVIEW target cannot load control VIs.

            The reference is invalid. This error might occur because the reference has been1556              deleted.

1557        LabVIEW tried to access duplicate references at the same time.

             There is a type mismatch between the wire type and the internal data type of the
1558
               reference. This problem might occur due to a type cast error.

              Project file cannot be saved at this time. The project has a locked untitled
1564         dependency. The lock prevents giving the untitled item a name so it cannot be
              saved.

            You cannot open a packed library saved in a version earlier than the current version
1571
               of LabVIEW.

            You cannot load a packed library built for a target or operating system different than
1573
             the current target or operating system.


                                                    © National Instruments 11551

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11551 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11552 ordinal=11552 -->
## Error Codes and Messages

Error Codes and Messages


        Code         Description

                     Cannot open a file with separated compiled code in the LabVIEW Run-Time Engine.
         1574         Contact the distributor of the file. The distributor must include compiled code in the
                                  file for it to run in the LabVIEW Run-Time Engine.

                         Specified paths do not share a common directory. The paths must share a directory.         1579
                       Consider building caches for each set of paths that share a common directory.

                     Cannot find the compiled code in the compiled object cache. Verify that the VI is
         1580        marked to save its compiled code separately and that it is not broken. Then compile
                        the VI.

         1581        Cannot use this property on either .NET or ActiveX Container.

                     The data in the reference cannot be resized. There is a size mismatch between the
         1584         data in the reference and the data wired to the Data Value Reference Write Element
                       border node.

         1586        Compiled code is out of date.

         1587           VI is not marked to separate compiled code from source file.

         1588        Compiled object cache is corrupt.

                     The qualified name of one of the dependencies of the specified file is not what
         1590        LabVIEW expected. This mismatch implies that the dependency report is unreliable,
                      so the ReadLinkInfo operation was aborted.

         1595        The RT target does not have enough memory to load the startup application.

                     Cannot use SSL on this operating system because SSL is either not configured, not         1596                            installed, or not supported.

                     The Paste Data operation attempted to paste data into a destination that would have         1597                    had a dimmed 'paste' option in the shortcut menu.

         1599        An empty string is not a valid method name.

                     The Open VI Reference function does not support using an asynchronous call by
                         reference option with the Prepare for reentrant run option. Both the 0x80 and 0x100
                        option flags conflict with the 0x08 option flag. The 0x08 flag is useful when running
         1603
                           VIs with the Run VI method. The 0x08 flag is not useful when performing
                      asynchronous calls. To correct this error, remove either the 0x08 option or the 0x80
                    and 0x100 options.

                     The Open VI Reference function does not support using the option 0x08 (Prepare for
         1604         reentrant run) with the asynchronous call by reference options 0x80 (Prepare to call
                    and forget) or 0x100 (Prepare to call and collect).


11552   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11552 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11553 ordinal=11553 -->
## Error Codes and Messages

Error Codes and Messages


Code         Description

           An internal error occurred because a front panel item has no execute data.1611             Recompiling the VI may fix this issue.

            The path to save the report is not valid. A valid path cannot contain any of the1616              following characters: (Windows) < > / | : " * ? or (OS X/Linux) < > \ | : " * ?.

            LabVIEW is unable to generate a VI comparison report. Make sure you have write1617             permission to the path you specified and generate the report again.

            LabVIEW is unable to find the Microsoft Word components. Make sure you installed1619              Microsoft Word correctly.

            LabVIEW is unable to create the Microsoft Word report. Try generating the report1620               again. If the problem persists, contact National Instruments technical support.

            LabVIEW is unable to create the Microsoft Word report. Try generating the report1621
               again. If the problem persists, contact National Instruments technical support.

            LabVIEW is unable to create the Microsoft Word report. Make sure you installed1622
              Microsoft Word correctly and create the report again.

            LabVIEW is unable to find the Microsoft Word components. Make sure you installed1623
              Microsoft Word correctly.

1624        You can only generate web page or plain text reports on OS X and Linux.

1627        The control index at position %d is invalid.

1628        LabVIEW cannot convert the input data type at position %d to the control data type.

1629        The control must have a terminal on the block diagram..

                      If you wire a variant or a LabVIEW class library file (.lvclass) to this function, you must
1630                 call the function on a VI in the same application instance.

            You cannot insert a custom control directly into a subpanel. Use a VI with the custom
1632
              control on its front panel instead.

             Channels are incompatible with asynchronous call by reference options 0x80
             (Prepare for call-and-forget) and 0x100 (Prepare for call-and-collect). Channels
               currently express only intraprocess communication. Channels cannot maintain their
1640
               state properly if one endpoint or the other shuts down independently. Both of the
             asynchronous call modes Prepare for call-and-forget and Prepare for call-and-
               collect allow the called VI to have a different run lifetime from its direct caller.

              Selected Device is Invalid The currently selected device index is invalid. This could be
4800
            caused by an invalid sound driver.

4801          Invalid sound task refnum. No sound driver is available for use, or the given GUID is

                                                    © National Instruments 11553

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11553 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11554 ordinal=11554 -->
## Error Codes and Messages

Error Codes and Messages


        Code         Description

                       not a valid DirectSound device ID.

                     The sound device is busy. Another application is currently using the device. Raising         4802                            this application's priority level could resolve this issue.

                     The sound driver or card cannot accommodate the specified configuration. Check
                         that the parameters entered are within the supported range for the hardware and         4803                            drivers. If you receive this error while using the Sound Output Configure VI, refer to
                        the KnowledgeBase at ni.com for more information.

                     Cannot write in file playback. The application attempted to write to the file while it         4804
                    was being played. This error code is not currently reported by the LVSound library.

         4805        Could not find the sound file. The specified sound file could not be found.

                         DirectX 8.0 or higher is required to run. To correct this error, install the latest version         4806
                          of DirectX from http://www.microsoft.com/downloads.

                     Cannot recognize sound format. The sound format of this file is not recognizable.         4810
                     The file may be corrupt.

                     Cannot support sound format. The specified wave format is not supported. This         4811
                       could be a limitation of the hardware, driver, or both.

                    A buffer underflow has occurred. A buffer underflow has occurred because the
         4820                         application is not writing data quickly enough.

                        Overwrite error. An overwrite error has occurred because the application is not
         4821                        reading data quickly enough from the buffer.

                    A timeout occurred before the operation finished. A timeout error occurred because
         4822                        the application was unable to successfully acquire a mutex.

                     You cannot perform this operation without an active task. Ensure that a task is active
         4823        and try again. An input task might stop running if the input buffer overflows.
                       Overflow occurs when the data is not read fast enough.

         56000        Generic project error.

         56001       An item with this name already exists in the project.

         56002       An item with this path already exists in the project.

         56003       Adding this item would cause a conflict with another item.

         56004       The project item could not be found.

         56005       The item type is not compatible with the target type.

         56006       You cannot add a packed library to a project library.

11554   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11554 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11555 ordinal=11555 -->
## Error Codes and Messages

Error Codes and Messages


 Code         Description

            The global time on the controller was altered, which might affect the period of an
                iteration of the NI Scan Engine. A timing source such as IEEE-1588 or GPS modified 66464              the global time value on the controller. This can result in a temporary phase shift,
             which would alter the update period for NI Scan Engine variables for one iteration.

GPIBGPIB ErrorError CodesCodes

The GPIB functions and VI Server properties and methods can return the following
error codes. Refer to the KnowledgeBase for more information about correcting errors
in LabVIEW.


 Code  Description

        Error connecting to driver or device. The NI-488.2 driver may not be installed. This error 0
       might be caused by a failure to find or properly open the GPIB device driver.

     Command requires GPIB Controller to be Controller-In-Charge. This error occurs when the
       board is not the Controller-In-Charge and any board-level function requiring controller 1        capability is called or when any device-level function that affects the GPIB is called and the
        driver cannot make the board the Controller-In-Charge.

     No Listeners on the GPIB. This error occurs when a data-byte write operation, such as
 2    ibwrt, is attempted with no addressed listeners on the bus or if a command-byte
       operation, such as ibcmd or SendCmds, is attempted and no devices are present.

      GPIB Controller not addressed correctly. This error occurs when the board is the Controller-
       In-Charge and is not properly addressed before starting a transfer. For example, ibrd
 3
       returns EADR if the interface is not addressed as a listener. ibgts also can return this error
            if the board is not properly addressed for shadow handshaking.

        Invalid argument or arguments to function call. This error occurs when a driver function is
 4
        called with an invalid parameter.

     Command requires GPIB Controller to be System Controller. This error occurs when the
 5
       board is not the System Controller but needs to be to perform the requested operation.

        I/O operation aborted. This error occurs when the I/O operation is aborted due to timeout,
 6      ibstop, or Device Clear.

       Nonexistent GPIB interface. Board-level functions return ENEB when the specified interface
 7       is configured in ibconf but cannot be found in the system. Device-level functions return
     ENEB when the specified access board of a device cannot be found in the system, even if the


                                                    © National Instruments 11555

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11555 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11556 ordinal=11556 -->
## Error Codes and Messages

Error Codes and Messages


        Code  Description

                 access board is configured in ibconf.

            DMA hardware error detected. This error occurs when the driver has DMA enabled but
                cannot use DMA to transfer a buffer. The error can be due to an operating system error, such
         8     as when the operating system is unable to provide a physical address to the driver. The error
                  also can be due to a hardware limitation, such as when the DMA controller cannot address
                your buffer and the driver cannot remap the buffer.

         9    DMA hardware uP bus timeout.

               Asynchronous I/O operation in progress. This error occurs when a thread starts
         10    asynchronous I/O and then attempts to access the interface while the interface is still in an
                unsynchronized state.

             No capability for operation. This error occurs when you try to take advantage of a driver
                  feature that is either not implemented in the driver or is not currently usable. For example, if
         11               you disabled hardware DMA by removing the DRQ/DACK jumpers on her legacy AT-GPIB/TNT,
               a call to ibconfigIbcDMA with a value of 1 to enable DMA would return this error.

                    File system operation error. This error occurs when an ibrdf or ibwrtf call encounters a         12
               problem accessing the specified file.

         13    Shareable board exclusively owned.

               GPIB bus error. This error occurs while sending out GPIB command bytes. This error is only
         14    returned by functions that indirectly send out command bytes. For example, a device-level
             ibwrt returns EBUS if it is unable to send the addressing command bytes.

         15     Serial poll byte queue overflow.

             SRQ stuck in ON position. This error occurs when the driver is unable to wait for the RQS bit
         16                 to set during a device-level ibwait.

         17    Unrecognized command.

         19    Board not present.

                 Table error. This error occurs when there is a problem with a table used by a driver function.
             FindLstn returns ETAB when it finds more listeners on the bus than will fit in the table you
         20
                 provided. FindRQS and AllSpoll return ETAB if the list of addresses to serial poll is
              empty or none of the devices in the list are asserting SRQ.

         30   No GPIB address input.

         31   No string input (write).

         32   No count input (read).


11556   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11556 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11557 ordinal=11557 -->
## Error Codes and Messages

Error Codes and Messages

InputInput DeviceDevice ControlControl VIVI ErrorError CodesCodes

The Input Device Control VIs can return the following error codes. This includes the
Acquire Input Data, Close Input Device, Initialize Joystick, Initialize Keyboard, Initialize
Mouse, and Query Input Devices VIs. Refer to the KnowledgeBase for more information
about correcting errors in LabVIEW.


 Code         Description

              Input Sprockets FailureThe Mac Input Sprockets tool kit is not properly installed on –2000000013              the machine.

 –2000000012  Close failure.Make sure the device is currently open.

 –2000000011 Read failure. Fails to read the device.

            The deviceCount being passed in is incorrect. Please connect the deviceCount –2000000010             parameter from initializeVI to the input parameter of closeDeviceVI.

 –2000000009 The operation cannot be performed while the device is acquired.

              Please check to see if the device is attached correctly. Please make sure the
 –2000000008              deviceIndex you passed in to initDevice.vi is correct.

 –2000000007 Data is not yet available.

 –2000000006 The operation cannot be performed unless the device is acquired.

 –2000000005  Access to the input device has been lost. It must be reacquired.

 –2000000004  This object has not been initialized.

            The DirectInput subsystem could not allocate sufficient memory to complete the
 –2000000003                   call. This value is equal to the E_OUTOFMEMORY standard COM return value.

 –2000000002 The application requires a newer version of DirectInput.

            An invalid parameter was passed to the returning function, or the object was not in a
 –2000000001  state that permitted the function to be called. This value is equal to the
             E_INVALIDARG standard COM return value.

 –2000000000 The application was written for an unsupported prerelease version of DirectInput.

             Check to see if proper initialization VI has been called. Also, please check the
 –1
               Microsoft web page for additional information about directInput.


                                                    © National Instruments 11557

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11557 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11558 ordinal=11558 -->
## Error Codes and Messages

Error Codes and Messages

      InstrumentInstrument DriverDriver ErrorError CodesCodes

       The Instrument Driver VIs and VI Server properties and methods can return the
         following error codes, as well as GPIB and VISA error codes. Refer to the
       KnowledgeBase for more information about correcting errors in LabVIEW.


        Code         Description

         −1074003967 Parameter 1 is out of range.

         −1074003966 Parameter 2 is out of range.

         −1074003965 Parameter 3 is out of range.

         −1074003964 Parameter 4 is out of range.

         −1074003963 Parameter 5 is out of range.

         −1074003962 Parameter 6 is out of range.

         −1074003961 Parameter 7 is out of range.

         −1074003960 Parameter 8 is out of range.

                           Identification query failed. Instrument identification failed. This error can occur if
                     you selected the wrong instrument or your instrument did not respond. This error
         −1074003951  also can occur if you used a model that is not officially supported by this driver. If
                     you are sure that you have selected the correct instrument and it is responding, try
                         disabling ID Query in the instrument driver's initialize VI.

         −1074003950  Error interpreting the instrument's response.

                       Instrument self-test failure. The instrument you are communicating with reported a         −1074000001                             self-test failure.

                       Instrument error query failure. The instrument you are communicating with
         −1074000000
                        reported an error.

         −1300         Instrument-specific error.

         −1236         Error interpreting instrument response.

         −1223        Instrument identification query failed.

         −1210        Parameter out of range. The Set Cursor VI also can return this error.

                               IVI invalid downcast. Driver is different from the specific driver associated with
         102
                         Logical Name.

         103        No IVI class session opened. You must call the class driver Initialize VI before you can

11558   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11558 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11559 ordinal=11559 -->
## Error Codes and Messages

Error Codes and Messages


 Code         Description

                  call a specific driver VI. This error also can occur if the IVI Logical Name control is set
               to the wrong IVI Class.

 1073479937   ID Query not supported.

 1073479938   Reset not supported.

 1073479939   Self-test not supported.

 1073479940   Error Query not supported.

LabVIEWLabVIEW Object-OrientedObject-Oriented ProgrammingProgramming ErrorError CodesCodes

VIs related to LabVIEW object-oriented programming return the following error codes.
Refer to the KnowledgeBase for more information about correcting errors in LabVIEW.


 Code  Description

 1371  Class library could not be loaded.

 1373  Class could not be loaded.

      LabVIEW classes do not support Revert if the library version has been bumped. There is
        insufficient information to undo a change to the live data in controls and indicators. To
 1392        revert current changes, you must unload the class and all VIs that reference the class without
       saving any changes and then reload from disk.

 1393  The LabVIEW class is not in memory. This dynamic subVI cannot execute.

       This dynamic subVI cannot execute because the needed member VI cannot be found. Probe
 1394  the wire going into the dynamic terminal to see the data type. Then open that LabVIEW class.
      Open the member VI of the class that has the same name as the dynamic subVI.

       Attempted to read flattened data of a LabVIEW class. The flat data could not be converted to
 1400  the requested type because the flat data is not the same as the requested type nor is it the
      same as any child class of the requested type.

       Attempted to read flattened data of a LabVIEW class. The version of the class currently in
 1401  memory is older than the version of the data. You must find a newer version of the class to
       load this data.

       Attempted to read flattened data of a LabVIEW class. The data was written by an old version
 1402  of the class and the class in memory no longer supports loading and mutating data from
        that older version.


                                                    © National Instruments 11559

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11559 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11560 ordinal=11560 -->
## Error Codes and Messages

Error Codes and Messages


        Code  Description

               Attempted to read flattened data of a LabVIEW class. The data is corrupt. LabVIEW could not         1403                  interpret the data as any valid flattened LabVIEW class.

         1446  The class of object in did not match the class of target object at run-time.

              Bad type cast. LabVIEW cannot treat the run-time value of this LabVIEW class as an instance         1448
                  of the given LabVIEW class.

                 This property or method cannot be executed on a reference that refers to a LabVIEW class         1486                loaded in a different application instance.

         1521  Cannot read the value of a control that contains placeholder data.

               You cannot read the value of a control when the class that defines the data is not available.         1525               You must load a missing LabVIEW class file to make this data readable.

               Attempted to read flattened data of a LabVIEW class that is not currently loaded into         1527
                LabVIEW. Load the missing class to be able to unflatten this data.

              The running VI attempted to make a subVI call into a top-level VI. LabVIEW does not allow         1530
                    calls into top-level VIs.

              The LabVIEW class data cannot be unflattened because the class is broken. You must fix         1531
               problems with the class before LabVIEW can unflatten data of this class.

              The long name of the property is not unique. LabVIEW class properties must have unique
         1572                long names. The long name you specified already exists for another LabVIEW class property.

         1598  The requested path does not match a LabVIEW class in memory.

         1600  The specified method was not found on the specified LabVIEW class.

                Although the requested class (or one of its ancestors) does have a member VI of the
         1601  requested name, that VI is not actually a method. Either it has no input terminal of the class
                type or it is a non-runnable kind of VI, like a global VI, control VI, or poly VI.

         1602  The value supplied for the enum input is not supported on this method or property.

                 This class cannot load into this application instance. Classes cannot have edits when loaded
                   in multiple application instances. This class attempted to load into a new application
         1609  instance where some dependency of the class, such as a type definition or nested class, is
                loaded from a different path than the application instance in which the class is already
                 loaded.

               You attempted to invoke a dynamic dispatch VI statically. The object you supplied for the
               dynamic dispatch terminal has an override VI for the chosen method that is not the same as
         1612
                the VI you specified. LabVIEW does not allow callers to directly invoke ancestor versions of
                the object's method.


11560   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11560 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11561 ordinal=11561 -->
## Error Codes and Messages

Error Codes and Messages


 Code  Description

 1613  Calls to remote application instances are not supported for dynamic dispatch VIs.

MathematicsMathematics ErrorError CodesCodes

The Mathematics VIs and VI Server properties and methods can return the following
error codes. Refer to the KnowledgeBase for more information about correcting errors
in LabVIEW.


 Code   Description

 0     No error.

 −23096 Too many decimal points. For example, 1.23.45.

 −23095 Not a valid function. For example, sins(x).

 −23094 Incomplete function expression. For example, sin(x)+.

 −23093 Incomplete expression. For example, x+.

 −23092  Variables output problem. Depends on application.

 −23091  Inconsistency in variables or numbers. Depends on application.

 −23090 Contains more than one variable. For example, 1+x+y4.

 −23089 Contains variables. Depends on application.

 −23088 Wrong variable name. For example, a11.

 −23086 Wrong function call. For example, sin().

 −23085 Wrong number format. For example, 1e-3 instead of 1E-3.

 −23084 Wrong decimal point. For example, 1,2 for United States.

 −23083  Bracket problem at the end. For example, (1+x.

 −23082  Bracket problem at the beginning. For example, 1+x).

 −23081  Bracket problem. For example, ().

 −23055 Argument out of range [0,1).

 −23054 Non-unique variables.

 −23053  Signal length not a power of two and ≥ 4.


                                                    © National Instruments 11561

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11561 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11562 ordinal=11562 -->
## Error Codes and Messages

Error Codes and Messages


        Code   Description

         −23052  Signal length not a prime and ≥ 5.

         −23051  Signal length not a power of two.

         −23050  Signal length not a multiple of number.

         −23049  Invalid window length.

         −23048  Invalid time increment.

         −23046 Empty array.

         −23045 n < k

         −23044 Argument out of range [0,1].

         −23043 Argument out of range (0,1].

         −23042  Negative argument.

         −23041 Not exactly two variables.

         −23040  Derivative out of range.

         −23039 Parameter problem.

         −23038 No variables in expression.

         −23037 Not exactly two functions.

         −23036  Different parameters.

         −23035  Nonpositive number.

         −23034   Ill conditioned system

         −23033  Vectors have different dimensions or empty vectors.

         −23032 Maximum does not exist.

         −23031 No valid point.

         −23030 m ≥ n ≥ 0 is violated or the matrix of derivatives has the wrong dimension.

         −23028 Wrong model equation.

         −23027 Not exactly one variable.

         −23026 No optimum found.

         −23025  Invalid triplet (a,b,c).

         −23024 No root found.


11562   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11562 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11563 ordinal=11563 -->
## Error Codes and Messages

Error Codes and Messages


Code   Description

−23023 Wrong dimension of start.

−23022  Nonpositive accuracy or nonpositive delta x(h).

−23021 Both function values have the same sign.

−23020  Left point greater than right point.

−23019  Right point is a root.

−23018  Left point is a root.

−23017  Multiple roots.

−23016  Singular eigenvector matrix.

−23015 Empty X0.

−23014 A and X0 have different dimensions.

−23013  Matrix vector conflict.

−23012  Nonpositive accuracy.

−23011  Nonpositive step rate.

       Wrong input, Cash Karp method. Verify the values you wired to the ODE Cash Karp 5th−23010        Order VI.

       Wrong input, Runge Kutta method. Verify the values you wired to the ODE Runge Kutta 4th−23009        Order VI.

−23008 Wrong input, Euler method. Verify the values you wired to the ODE Euler Method VI.

−23007 Not a graphs file.

−23006 Not a valid path.

−23005  Negative distance.

−23004 Number of color palettes out of range.

−23003 Number of contours out of range.

−23002 Discrepancy between function, variables and coordinates.

−23001 Syntax error of parser.

−23000 The starting error codes of engineering math.

−20165 The initial condition conflicts with the PDE class input.

−20164 The boundary condition conflicts with the PDE class input.

                                                    © National Instruments 11563

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11563 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11564 ordinal=11564 -->
## Error Codes and Messages

Error Codes and Messages


        Code   Description

         −20163 The domain conflicts with the PDE class input.

         −20162 The right side of the PDE conflicts with the PDE class input.

         −20161 The equation conflicts with the PDE class input.

                The size of the initial condition of the PDE is incompatible with the size of the grid on the         −20158
                 domain.

                The size of the boundary condition of the PDE is incompatible with the size of the grid on         −20157                  the domain.

         −20156 The size of the right side of the PDE is incompatible with the size of the grid on the domain.

                The number of boundary points must be greater than or equal to 3 on the polygonal         −20155                 domain.

         −20154 The number of grid points is 0 on the polygonal domain.

         −20153 The number of spatial points must be greater than or equal to 3.

         −20152 The number of time points must be greater than or equal to 2.

         −20151 The final or end point must be greater than the initial or start point.

         −20144 The interpolation size must be greater than or equal to the data size.

         −20143 An input value is outside its acceptable domain.

         −20141 The input must be non-zero.

         −20140 The input must be greater than zero.

         −20127 The number of samples is less than the number of unknown parameters.

         20005  LabVIEW cannot reorder the generalized eigenvalues.

      MathscriptMathscript ErrorError codescodes

       The Mathscript node can return the following error codes.


        Code   Description

         0     No error.

         −90142 The MathScript Module is not supported from LabVIEW 2023 Q1 release. Visit for detailed


11564   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11564 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11565 ordinal=11565 -->
## Error Codes and Messages

Error Codes and Messages


 Code   Description

         information and recommended alternatives.

ModbusModbus ErrorError CodesCodes

The Modbus VIs can return the following error codes. Refer to the KnowledgeBase for
more information about correcting errors in LabVIEW.


 Code    Description

         The target device does not have any response. Possible reason: the target device is not −389122
          present on the network. This error description is defined by the Modbus Organization.

         The gateway is unable to allocate an internal communication path from the input port to
          the output port for processing the request. Possible reason: the gateway is either −389121          misconfigured or overloaded. This error description is defined by the Modbus
          Organization.

        An extended file area failed to pass a consistency check. You can use the Modbus master
 −389118  to retry the connection, but the Modbus slave may require certain service. This error
          description is defined by the Modbus Organization.

         The Modbus slave is busy. Use the Modbus master to retransmit data at a later time. This −389116           error description is defined by the Modbus Organization.

         The Modbus slave is processing the request and may spend a long time processing this −389115           request. This error description is defined by the Modbus Organization.

        An unrecoverable error occurred while the server was attempting to perform the
 −389114
          requested action. This error description is defined by the Modbus Organization.

        A value contained in the query data field is invalid for the Modbus slave. This error
 −389113
          description is defined by the Modbus Organization.

         The Modbus slave does not accept the data address contained in the query. This error
 −389112
          description is defined by the Modbus Organization.

         The Modbus slave does not accept the function code contained in the query. This error
 −389111
          description is defined by the Modbus Organization.

         The Modbus master does not use a serial protocol and cannot perform the action that
 −389107
         you requested. Ensure that you use a serial Modbus master to perform this action.


                                                    © National Instruments 11565

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11565 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11566 ordinal=11566 -->
## Error Codes and Messages

Error Codes and Messages


        Code    Description

                 The current Modbus slave cannot perform the operation you wanted to perform, because         −389106                       this slave is not a TCP Modbus slave.

                 The Modbus slave daemon, also known as background process, failed to launch. Contact         −389105                    National Instruments for technical support.

         −389104 The object that you write exceeds 244 bytes in length.

                 The object that you specified does not exist in the Modbus slave. Ensure that you specify
         −389103 an object that exists in the Modbus slave. Contact National Instruments for technical
                    support.

                 The data that the Modbus slave returned did not match the data that the Modbus master
         −389102  sent for the operation you want to perform. Contact National Instruments for technical
                    support.

                 The returned Modbus Encapsulated Interface type was not 0x0E (14). This type is required
                       for the operation you want to perform. Possible reasons: the Modbus slave does not have         −389101
                  a device identification; the Modbus slave does not support read operations on its device
                       identification.

                 The returned function code does not match the function code in the requested data.         −389100                   Contact National Instruments for technical support.

                 The operation you want to perform is not implemented. Possible reasons: the
                  descendant class does not implement one of the required member VIs in the ancestor
         389298  Modbus class; the descendant class data is lost and LabVIEW executes a member VI in the
                    ancestor Modbus class that does not provide an implementation. Contact National
                   Instruments for technical support.

                 You configured this serial request as a broadcast. The Modbus slave does not respond to
         389299                    broadcasts. Contact National Instruments for technical support.

     NetworkNetwork StreamsStreams ErrorError CodesCodes

       Network streams can return the following error codes. Refer to the KnowledgeBase for
       more information about correcting errors in LabVIEW.


        Code    Description

                 You cannot read data from a writer endpoint or write data to a reader endpoint. Ensure
         −314352  that you have not wired a Write Single Element to Stream, Write Multiple Elements to
                   Stream, or Flush Stream function to a Create Network Stream Reader Endpoint function.


11566   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11566 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11567 ordinal=11567 -->
## Error Codes and Messages

Error Codes and Messages


Code    Description

          Conversely, ensure that you have not wired a Read Single Element from Stream or Read
          Multiple Elements from Stream function to a Create Network Stream Writer Endpoint
          function.

        You must read or write elements of the same data type that you wired to the data type
−314351  terminal of the Create Network Stream Reader Endpoint or Create Network Stream Writer
         Endpoint function.

         Another application is already streaming data to an endpoint in the context you specified.
               If you specified a context name in the reader name or writer name terminal of the
−314350  endpoint, you must specify an unused context name. If you did not specify a context
        name, you must specify an unused context name by entering an endpoint URL in the
         reader name or writer name terminal.

        The local endpoint found the remote endpoint at the URL you specified, but the remote
         endpoint was trying to connect to a third endpoint. Ensure that corresponding endpoints
−314340 each specify the URL of the other endpoint, or specify a URL with only one of the
         endpoints so the other endpoint accepts a connection from the first endpoint that
         connects to it.

        The local endpoint was restarted because the computer that hosts the remote endpoint
−314335         crashed, was rebooted, or experienced a hang.

        LabVIEW could not create the remote endpoint because the computer that hosts the
−314320         endpoint ran out of memory.

−314310 The remote endpoint has been destroyed.

        The protocol version of the writer endpoint is not compatible with the protocol version of
−314305 the reader endpoint. To transfer data between these endpoints, you must upgrade the
          version of LabVIEW that the older endpoint uses.

        The remote endpoint is already connected to another endpoint. Each endpoint can
−314302
         connect to only one other endpoint at a time.

        The remote and local endpoints are either both reader endpoints or both writer
−314246
         endpoints. You can prompt a connection between a reader and writer endpoint only .

        The data type of the remote endpoint does not match the data type of the local endpoint.
−314245
        The data types of the endpoints must match.

        The stream detected an unrecoverable loss of data. Contact National Instruments for
−314240
         support.

        The remote endpoint was restarted because the computer that hosts the endpoint
−314235
         crashed, was rebooted, or experienced a hang.


                                                    © National Instruments 11567

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11567 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11568 ordinal=11568 -->
## Error Codes and Messages

Error Codes and Messages


        Code    Description

                 LabVIEW could not create the local endpoint because the computer that hosts the         −314230                  endpoint ran out of memory.

                 The URL you specified with the reader url or writer url terminal does not include the
         −314227 name of the remote endpoint. You must specify a valid endpoint URL in one of these
                    terminals to connect two endpoints together.

         −314226 Incompatible format.

         −314220 The remote endpoint has been destroyed.

                 You cannot read or write a number of elements that is larger than the size of the endpoint         −314215
                       buffer.

                 You cannot flush a network stream from the reader endpoint. Call the Flush Stream         −314202                    function from the writer endpoint only.

                 The local endpoint lost connection and reconnected with the remote endpoint, but some         −314201                   data was lost.

                 The name of one endpoint cannot be the partial name of another endpoint within the
         −314109 same application. Change the name of this endpoint so that it does not overlap with an
                      existing name, or destroy the other endpoint before creating this endpoint.

                 The name of one endpoint cannot be the partial name of another endpoint within the
         −314108 same application. Change the name of this endpoint so that it does not overlap with an
                      existing name, or destroy the other endpoint before creating this endpoint.

                 The local endpoint is already connected to another endpoint. Each endpoint can connect         −314107                    to only one other endpoint at a time.

                 The local endpoint is not connected to a remote endpoint. Specify the URL of a remote
                  endpoint in the writer url terminal of the Create Network Stream Reader Endpoint         −314106                    function or the reader url terminal of the Create Network Stream Writer Endpoint
                    function to prompt a connection between two endpoints.

                 You can call the Write Single Element to Stream and Write Multiple Elements to Stream
         −314105
                    functions from the writer endpoint only.

                 You can call the Read Single Element from Stream and Read Multiple Elements from
         −314104
                  Stream functions from the reader endpoint only.

                 You did not specify an endpoint name. Specify a valid name or endpoint URL with the
         −314103  reader name terminal of the Create Network Stream Reader Endpoint function or the
                     writer name terminal of the Create Network Stream Writer Endpoint function.

         −314102 The buffer size of the endpoint must be greater than zero elements.


11568   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11568 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11569 ordinal=11569 -->
## Error Codes and Messages

Error Codes and Messages


Code    Description

−314101 An endpoint with the same name already exists.

−314100 The specified endpoint does not exist.

−314054 The Network Streams Engine cannot be uninitialized.

−314053 The Network Streams Engine failed to initialize.

−314052 The Network Streams Engine is not initialized.

−314051 The Network Streams Engine was already initialized.

−314050 The Network Streams Engine does not exist.

        The value wired to the Wait Condition input is invalid. Refer to the LabVIEW Help for valid−314009
          values.

        The value wired to the Element Allocation Mode input is invalid. Refer to the LabVIEW−314008         Help for valid values.

        You cannot read multiple array elements of different dimensions. You can read multiple−314007          array elements of the same dimension only.

        You cannot specify a relative URL with the reader url and writer url terminals. You must
         use an absolute URL instead. For example, if you are connecting to an endpoint with the−314006
       name Endpoint1 on a computer with the IP address 10.0.0.62, use the URL //10.0.0.62/
         stream1.

−314005 The ni_nwstreams library contains invalid parameters.

        LabVIEW could not create the endpoint within the timeout period. Ensure that you specify
         the URL of a remote endpoint with the reader url terminal of the Create Network Stream−314004          Writer Endpoint function or the writer url terminal of the Create Network Stream Reader
         Endpoint function.

        LabVIEW could not create a network stream. You must specify the URL of a remote
         endpoint with either the reader url terminal of the Create Network Stream Writer
−314003
         Endpoint function or the writer url terminal of the Create Network Stream Reader
         Endpoint function.

        You cannot call this property from the reader endpoint. You can call this property from
−314002
         the writer endpoint only.

        You cannot call this property from the writer endpoint. You can call this property from the
−314001
         reader endpoint only.

        LabVIEW cannot load the ni_nwstreams library. If you are using a desktop computer, you
−314000 might need to repair your LabVIEW installation or reinstall LabVIEW or the LabVIEW Run-
        Time Engine. If you are using an RT target, verify that you installed the network streams

                                                    © National Instruments 11569

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11569 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11570 ordinal=11570 -->
## Error Codes and Messages

Error Codes and Messages


        Code    Description

                     feature with Measurement and Automation Explorer (MAX).

         314000  Not enough elements to read.

         314001  Not enough free space to write.

                 The writer endpoint was destroyed before it received an acknowledgement from the
         314010   reader endpoint that all data was received. The reader endpoint might not have received
               some data.

         314050  You specified the URL of a remote endpoint that does not exist.

                 The remote endpoint did not prompt a connection with the local endpoint. Make sure         314051
                 you specify the correct URL with the URL terminal of the remote endpoint.

                 The local endpoint did not receive a response from the remote endpoint before the         314205                   timeout expired.

         314210  The endpoint timed out before another endpoint prompted a connection with it.

      NetworkingNetworking ErrorError CodesCodes

         VIs and functions that use TCP connections in LabVIEW and VI Server properties and
       methods can return the following error codes. This includes TCP, UDP, DataSocket,
        Bluetooth, and IrDA VIs and functions, remote front panel connections, and VI Server
         applications. Remote front panels also can return additional error messages. Refer to
        the KnowledgeBase for more information about correcting errors in LabVIEW.


        Code         Description

         −2147467263 Not implemented.

         −2147024809 One or more arguments are invalid.

         −1967390712 Cannot resolve name to a network address.

         −1967390711 Network operation timed out.

         −1967390703 Could not resolve service to a port address.

         −1967390702 Timed out while trying to connect to peer.

         −1967390686 Computer name is not present in the URL.

         −1967390685 Computer name starts with a non-alphabetic character.


11570   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11570 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11571 ordinal=11571 -->
## Error Codes and Messages

Error Codes and Messages


Code         Description

−1967390684 Computer name contains an invalid character.

−1967390683 Process name is not present in the URL.

−1967390682 Process name contains an invalid character.

−1967390681  Point or tag name is not present in the URL.

−1967390680  Point or tag name contains an invalid character.

−1967390672 Empty component in point or tag name.

−1967390668 Thread initiation failed.

−1967390464 URL does not start with two slashes.

−1967390463 URL starts with more than two slashes.

−1967390462 URL contains two consecutive delimiters.

−1967390460 Unbalanced quotation marks in URL.

53          Manager call not supported.

            The network address is ill-formed. Make sure the address is in a valid format. For
               TCP/IP, the address can be either a machine name or an IP address in the form
                xxx.xxx.xxx.xxx. If this error occurs when specifying a machine name, make sure the54
            machine name is valid. Try to ping the machine name. Check that you have a DNS
              server properly configured. If you are using the TCP Open Connection function,
             ensure that the value of the remote port or service name is not 0.

            The network operation is in progress. If you receive this error while using the UDP
55              Write function, refer to the KnowledgeBase at ni.com for more information.

56          The network operation exceeded the user-specified or system time limit.

57          The network connection is busy.

58          The network function is not supported by the system.

59          The network is down, unreachable, or has been reset.

            The specified port or network address is currently in use. Select an available port or
60
            network address.

61          The system could not allocate the necessary memory.

62          The system caused the network connection to be aborted.

            The network connection was refused by the server. For TCP/IP, make sure the server
63
                   is running and listening on the port you want to use. Firewalls also can cause a


                                                    © National Instruments 11571

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11571 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11572 ordinal=11572 -->
## Error Codes and Messages

Error Codes and Messages


        Code         Description

                         server to refuse a connection. For VI Server, make sure the VI Server is enabled on
                        the VI Server page of the Options dialog box.

         64          The network connection is not yet established.

         65          The network connection is already established.

                     The network connection was closed by the peer. If you are using the Open VI
         66           Reference function on a remote VI Server connection, verify that the machine is
                       allowed access by selecting Tools»Options»VI Server on the server side.

         108           Singlecast connections cannot send to multicast addresses.

         109           Multicast connections cannot send to singlecast addresses.

         110           Specified IP address is not in multicast address range.

         111         Cannot write to read-only multicast connection.

         112         Cannot read from write-only multicast connection.

                    A message sent on a datagram socket was larger than the internal message buffer or
         113        some other network limit, or the buffer used to receive a datagram was smaller than
                        the datagram itself.

                      Could not create TCP listener port because the port, service name, or net address         114                            conflict with a TCP listener that already exists.

                              Illegal combination of Bluetooth discoverable and non-connectable modes. A
                         discoverable Bluetooth system is connectable, and non-connectable Bluetooth
         119                      system is non-discoverable. The combination of discoverable and non-connectable
                                 is illegal.

                          Error setting Bluetooth mode. Unknown internal error encountered while setting         120
                       Bluetooth mode.

                           Invalid GUID string. The GUID string has an invalid format. An example of the correct
         121
                       format is: B62C4E8D-62CC-404b-BBBF-BF3E3BBB1374.

                      Could not query socket state. Either the socket is in a bad state (e.g. an error state,
         126          not connected, and so on) and the requested information is not available, or the
                        socket is unable to answer the query.

         127         The specified socket is not an IPv4 socket.

                   Open connection limit exceeded. The application has exceeded the maximum
         128
                    number of open sockets allowed by the “Max_Sockets” INI token.

         1101           Insufficient privileges to read, write, or create an item in the DataSocket Server. Use


11572   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11572 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11573 ordinal=11573 -->
## Error Codes and Messages

Error Codes and Messages


Code         Description

             the DataSocket Server Manager to configure these privileges.

1114          This item is read-only. You must connect in read mode.

1115          This item is write-only. You must connect in write mode.

1132        Busy with another operation.

1133        LabVIEW is busy connecting.

1134        A different read operation is in progress.

           A DataSocket item name cannot contain certain characters. This error occurs if the1139             DataSocket item name contains "/", "\", "?", "=", or "&".

            Exceeded maximum DataSocket item count. Use the DataSocket Server Manager to
1140        change the maximum number of dynamically created items the data server will
               allow.

            Exceeded maximum data item connection count. Use the DataSocket Server1141            Manager to change the maximum number of connections the data server will allow.

              Multiple writers are not allowed. You can use the Shared Variable Properties dialog1142            box to configure shared variables to accept multiple writers.

1143        Cannot load dataskt.llb.

1178        LabVIEW reached end of file.

1179         Access mode not supported for operation.

1180        Pending operation in progress.

              Protocol not recognized by LabVIEW. You must use a valid URL to establish a data1181              connection.

1182          Error parsing URL.

            Synchronous operation not supported for connection. Append "?sync=true" to URL
1183          to enable synchronous operations with the PSP protocol. LabVIEW 8.0.1 and later
             support synchronous operations.

1184         Path not found, FTP login incorrect, or no FTP write permission.

1185       OPC item not found.

1337        Not enough memory to complete this remote panel operation.

1338        Network type not supported by remote panel protocol.

1339        Remote panel connection is closed.


                                                    © National Instruments 11573

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11573 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11574 ordinal=11574 -->
## Error Codes and Messages

Error Codes and Messages


        Code         Description

                           Invalid server IP address. Contact the server administrator to get the correct IP         1340                       address or name of the computer to which you want to connect.

                    Remote panel connection refused by the specified server. The server administrator
         1341        must enable the LabVIEW Web Server. Verify that the Server IP Address and Port you
                       entered in the Connect to Remote Panel dialog box are correct.

         1343          Client does not have access to remote panel server.

                     The remote panel protocol version is incompatible. The client and server computers
                    must be running the same version of LabVIEW. If you are using a browser to view and
                         control a remote front panel, you must use a version of the LabVIEW Run-Time         1344                       Engine compatible with the version of LabVIEW on the server computer. Also, be sure
                    and contact the server administrator and have them make sure that the HTML
                    document specifies the correct version of the LabVIEW Run-Time Engine.

                     The LabVIEW client version is incompatible with the LabVIEW server version. Make         1345
                        sure you entered the IP address or computer name of the server correctly.

         1346         Server does not support remote panels.

         1347        You cannot connect to the local LabVIEW application.

                    Remote panel server failed to send the requested VI. A memory or network problem
                         occurred. This error might occur if you try to connect to a large front panel. Try to         1348                       connect to the front panel again, or request that the server administrator modify the
                          front panel so it uses less memory.

                          Client does not have access to specified VI. The server administrator must specify the
         1349                           VIs that clients can view or control.

         1350        Requested VI is broken and cannot be viewed or controlled.

                      Requested VI is not a standard VI. You cannot view or control a polymorphic VI,
         1351
                     custom control, or global variable VI remotely.

         1352        Requested VI is not loaded into memory on the server computer.

         1353        Requested VI is not in run mode.

         1354           VI name required.

         1355          Fatal error occurred during operation, closing connection.

         1356        A remote panel connection does not exist for the specified VI.

         1369        Removing data connection from this control.

         1383        The data type of the data read does not match the data type of the type input.


11574   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11574 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11575 ordinal=11575 -->
## Error Codes and Messages

Error Codes and Messages


 Code         Description

 1509        The response from the NI Service Locator is not a valid HTTP response.

            The requested service was not found as a registered service with the NI Service
               Locator. To correct this error, check that the desired service name is correct. If the 1510                service name is correct, check that either the TCP Create Listener, or the UDP Open
               functions are registering the service.

            The requested service is a registered service with the NI Service Locator but it did not 1511              contain a port mapping. The port number is missing or is registered incorrectly.

            The control is not located in the same VI as the control reference. You can link a 1567
               control reference only to controls or indicators in the same VI.

             LabVIEW Real-Time target is already connected to a host VI. You cannot initiate a
 1583        remote panel connection to a Real-Time target while also using a host VI to connect
               to the target. Choose only one method to connect to the target.

 2308        Found no configured network adapters.

 363515      The file exceeds the size limit on the server.

 363516        Client does not have access to the specified resource (access is forbidden).

 363517      Cannot find the remote file.

 363518      The remote file already exists.

 363519       Storage space limits on the server exceeded.

 363520      The server does not recognize the transfer encoding.

 363521      Number of redirects to other resources exceeded.

 363522      The network communication socket is not ready.

 363523      An unknown error occurred in the curl libraries.

 363524      The specified protocol is invalid or unsupported.

OPCOPC UAUA ErrorError CodesCodes

The OPC UA VIs can return the following error codes. Refer to the KnowledgeBase for
more information about correcting errors in LabVIEW.


                                                    © National Instruments 11575

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11575 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11576 ordinal=11576 -->
## Error Codes and Messages

Error Codes and Messages


        Code    Description

         −356702 The OPC UA server has reached the maximum number of subscriptions allowed.

         −356701 The port you specified for creating the server is occupied.

                 LabVIEW cannot find the certificate or private key file. Ensure the file exists and the         −356699                     specified file path is valid.

         −356698 Unable to locate the host. Ensure the hostname is valid or use the IP address.

                 The OPC UA client failed to establish a secure connection to the OPC UA server. Either the
               OPC UA server does not trust the certificate file that the OPC UA client uses or the system
                  time of the server machine is out of the valid time range of the certificate file that the OPC
               UA client uses. You must ensure that the OPC UA server trusts the certificate file that the
         −356697 OPC UA client uses. If you do not specify a certificate file for the OPC UA client to use,
                   ensure that the OPC UA server trusts the default certificate file of the OPC UA client. You
                 must also ensure that the system time of the server machine is within the valid time
                   range of the certificate file. You can find the valid time range by opening the certificate
                             file.

         −356696 Value in the OPC UA server contains a syntax error.

         −356695 The OPC UA server does not support the specified security policy .

         −356694 The OPC UA server does not support the specified message mode.

                 The requested operation is not supported or one or more parameter specified in the         −356683                   requested operation are not supported.

         −356677 The node path refers to a node that does not exist in the server address space.

         −356676 The OPC UA server cannot recognize the node in the request of the OPC UA client.

         −356653 The status of the OPC UA server is uncertain.

         −356650 The view version is not available or is not supported.

         −356648 The view timestamp is not available or is not supported.

         −356647 The view ID does not refer to a valid view node.

         −356646 The user does not have permission to perform the requested operation.

         −356645 The OPC UA client cannot recognize the response from the OPC UA server.

         −356644 An unexpected error occurred.

         −356643 The request cannot be processed because the request specified too many operations.

         −356641 The operation timed out.


11576   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11576 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11577 ordinal=11577 -->
## Error Codes and Messages

Error Codes and Messages


Code    Description

        The subscription ID is not valid. Ensure the ID refers to a subscription that you have−356640         already created.

−356639 The operation was cancelled because the application is shutting down.

−356638 The session cannot be used because you have not activated this session.

−356637 The session has been closed by the OPC UA client.

−356636 The OPC UA client failed to close a session. Verify that the session is active.

−356635 The OPC UA server does not support the requested service.

−356634 The server URI is not valid.

        You cannot complete the operation before you connect the OPC UA client to the OPC UA−356633          server.

−356632 The OPC UA server has stopped and cannot process any requests.

−356631 An error occurred when the OPC UA server was verifying the security policy.

−356630 The secure channel you specified is no longer valid.

−356629 An operating system resource is not available.

−356628 The header for the request is missing or invalid.

        The OPC UA client cannot read the response message from the OPC UA server, because−356627         the message size exceeds the specified limits.

        The OPC UA server cannot read the request message from the OPC UA client, because the−356626        message size exceeds the specified limits.

−356625 The OPC UA client has cancelled the request.

−356624 Not enough memory to complete this operation.

       No operation executed because the OPC UA client passed a list of operations with no
−356623
         elements.

−356622 The nonce does not appear to be a random value or is not correct in length.

−356621 The timestamp is out of the range the OPC UA server allows.

−356620 The operation cannot complete. Possible reason is that the OPC UA server is shut down.

        The OPC UA server failed to validate one or more parameters in the OPC UA client
−356619
          request.

−356618 The OPC UA client cannot connect to the OPC UA server because the OPC UA server


                                                    © National Instruments 11577

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11577 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11578 ordinal=11578 -->
## Error Codes and Messages

Error Codes and Messages


        Code    Description

                     rejected the security policy, username, or password.

                 The OPC UA client cannot connect to the OPC UA server because the security policy,         −356617                  username, or password is invalid.

         −356616 The message encoding and decoding limits imposed by the stack have been exceeded.

         −356615 Encoding halted because of invalid data in the serialized objects.

         −356614 Decoding halted because of invalid data in the stream.

                 The extension object cannot be serialized or deserialized because the data type ID is not         −356613                    recognized.

         −356611 You cannot use the certificate for the requested operation.

         −356610 The certificate is not trusted.

                 The certificate URI in the OPC UA client request does not match the certificate URI that         −356609
                   the OPC UA server expects.

         −356608 The certificate has expired or is not yet valid.

         −356607 The certificate has been revoked.

         −356606 Unable to determine if the certificate has been revoked.

                 The certificate provided by OPC UA server is not valid. Ensure the OPC UA client trusts the         −356605               OPC UA server certificate.

         −356603 An issuer certificate has expired or is not yet valid.

         −356602 You cannot use the issuer certificate for the requested operation.

         −356601 Unable to determine if the issuer certificate has been revoked.

                 The host name that you use to connect to an OPC UA server does not match a host name
         −356600
                      in the certificate.

         −356530 The syntax of node path is incorrect.

         −356529 You must select at least one security policy.

         −356528 You cannot remove a certificate when the OPC UA server is running.

         −356527 You cannot add a certificate when the OPC UA server is running.

         −356526 The initial value of a node in the OPC UA server address space is uncertain.

         −356525 The sensor from which the value is derived by the device or data source failed.

         −356524 The device or data source that generates the value failed.

11578   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11578 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11579 ordinal=11579 -->
## Error Codes and Messages

Error Codes and Messages


 Code    Description

 −356523 The node you want to delete does not exist in the address space.

 −356522 You cannot add a node when the OPC UA server is running.

 −356521 You cannot delete a node when the OPC UA server is running.

 −356520 Unable to remove one or more certificate files.

 −356519 Unable to add one or more certificate files.

 −356517 The client refnum input is not valid.

 −356516 The server refnum input is not valid.

 −356515 The data type of the node does not match the data type of the value to write.

 −356514 The data type of the node does not match the expected data type.

 −356512 An error occurred when writing to the node.

 −356511 An error occurred when reading the node.

 −356510 The OPC UA server does not support this feature.

 −356509 The node you want to add already exists in the address space.

 −356508 Unable to add a node to the address space.

 −356507 Unable to add a property to the address space.

 −356506 Unable to add an item to the address space.

 −356505 Unable to add a folder to the address space.

 −356504 Unable to find a node in the address space.

 −356503  This node does not support read and write operations.

 −356502 Not enough memory to complete this operation.

 −356500 An internal error occurred as a result of a programming or configuration error.

PointPoint ByBy PointPoint ErrorError CodesCodes

The Point By Point VIs and VI Server properties and methods can return the following
error codes. Linking to the Error Cluster From Error Code VI builds an error cluster
compatible with error chaining. Refer to the KnowledgeBase for more information
about correcting errors in LabVIEW.


                                                    © National Instruments 11579

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11579 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11580 ordinal=11580 -->
## Error Codes and Messages

Error Codes and Messages


        Code         Description

         −20207      The upper limit is less than the lower limit.

         −20206         Shifts: n is negative.

         −20205      The sample length is less than the window length.

         −20204      The window length is not positive.

         −20203      The time increment is not positive.

         −20202      The sample length is negative.

         −20201      The sample length is not positive.

      RegularRegular ExpressionExpression ErrorError CodesCodes

       The Match Regular Expression function returns these errors. Refer to the
       KnowledgeBase for more information about correcting errors in LabVIEW.


        Code  Description

              One of the string parameters contains a null character. LabVIEW does not support null
         −4702                  characters for regular expression matching.

               The maximum recursion limit was reached while attempting the regular expression match
         −4701  This error is typically due to an inefficient regular expression being used in a long input
                     string.

         −4644 An invalid UTF-8 string was used in a regular expression or input string.

             Two named groups have the same name. Two named groups (using "(?P<name>)") have the
         −4643
              same name.

                There is a syntax error after (?P. An invalid "(?P" (named parentheses expression) was found
         −4642
                    in a regular expression.

              An unrecognized character was encountered after (?P. An unrecognized character was
         −4641
                encountered after a "(?P" expression. Acceptable characters are "<", ">", or "=".

              A recursive call could loop indefinitely. A recursive call was used in a regular expression that
         −4640
                 could loop indefinitely. A recursion call on an empty match cause an infinite loop.

                UTF-8 is not supported. The Match Regular Expression function does not support UTF-8
         −4632
                  character encoding.

         −4631 POSIX collating elements are not supported. Also, POSIX classes are allowed only within

11580   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11580 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11581 ordinal=11581 -->
## Error Codes and Messages

Error Codes and Messages


Code  Description

       character classes. Ex: "[0-9]" or "[[:digit:]]" are valid while "[[.ch.]]", "[[=e=]]", and "[:digit:]"
       are not.

      Unknown POSIX class name. An unrecognized POSIX class name appeared in a regular−4630       expression.

      A (?R or (?digits expression must be followed by ). A recursion or subroutine did not have a−4629        right parenthesis in the proper place. Ex: "(?1)" or "(?R)" is valid while "(?1" or "(?R" is not.

      An assertion is expected after (?(. A conditional must either refer to a partial match (ex:−4628         "(?(1)a)"), a recursion (ex: "(?(R)a)"), or an assertion (ex: "(?(?<a)b)").

      A conditional group contains more than two branches. A conditional group may only−4627       contain one or two branches. Ex: "(a)(?(1)b|12)" is valid, while "(a)(?(1)b|12|cd)" is not.

       There is a malformed number after (?(. A malformed number was used for a subroutine call−4626
        in a regular expression.

−4625 A lookbehind assertion is not a fixed length. Lookbehind assertions may not use quantifiers.

      The regular expression contains an unrecognized character after (?<. You must follow (?<−4624       with the character = (ex: "(?<=a)") or ! (ex: "(?<!a)").

−4622 There is an unmatched parenthesis in a regular expression.

−4621  Failed to get the memory for regular expression matching.

−4620 The regular expression is too large. The limit is 65536 characters.

       Parentheses are nested too deeply. A regular expression has parentheses that are nested
−4619       too deeply. The limit is 200.

      A ) is missing after a comment. A comment (ex: "(?# comment )") is missing a right
−4618       parenthesis.

       There is a reference to non-existent subpattern. A back reference (ex: "\1") in a regular
−4615
       expression refers to a non-existent subpattern.

−4614 A ) is missing. A regular expression is missing a right parenthesis.

      POSIX named classes are supported only within a class. A POSIX named class (ex: "[:digit:]")
−4613
      can only appear within a character class ("[[:digit:]]").

       There is an unrecognized character after (?. An unrecognized character appeared after a '(?'
−4612
      sequence in a regular expression.

       There is nothing to repeat. A quantifier was used in a place that does not allow repetition.
−4609
       For example, a quantifier may not appear at the beginning of a regular expression.

−4608 A range is out of order in a character class. Ranges in character classes must have the lowest

                                                    © National Instruments 11581

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11581 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11582 ordinal=11582 -->
## Error Codes and Messages

Error Codes and Messages


        Code  Description

                  character first. For example, [a-z] is valid while [z-a] is not.

         −4607 A character class contains an invalid escape sequence.

              A character class is missing a ']' terminator. If you meant to match a literal '[', escape it with         −4606                a backslash (i.e., "\[").

              A number in the {} quantifier is too large. The number in a {} quantifier must be less than         −4605                 65536.

                   In the regular expression, the numbers within the quantifier {} are out of order. In a {}         −4604                    quantifier, the first number must be less than or equal to the second.

              An unrecognized character follows a '\'. A regular expression contains an unrecognized         −4603                escape sequence.

              A regular expression must not end with '\c'. You must follow a '\c' in a regular expression by         −4602
                 another character to denote a control character.

              A regular expression must not end with '\'. Use the backslash ('\') character to mark special
         −4601  characters or to mark a special character to remove its special meaning. To match a literal
                  backslash, use a double backslash ("\\").

              An unknown error occurred during the regular expression match. An unknown error         −4600                 occurred during the regular expression match.

      ReportReport GenerationGeneration ErrorError CodesCodes

       The Report Generation VIs and VI Server properties and methods can return the
         following error codes. Refer to the KnowledgeBase for more information about
         correcting errors in LabVIEW.


        Code   Description

                You must have the LabVIEW Report Generation Toolkit for Microsoft Office installed to
         −41007  create this type of report. The toolkit must also have an activated license or be in
                   evaluation mode.

                     Invalid margins. One or more of the specified margin values do not exceed the minimum
         −41005
                 margins of the printer.

         −41003  File open error. Unable to open or read from the specified file.

         −41001 Out of memory. Insufficient memory for requested operation. Try closing open


11582   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11582 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11583 ordinal=11583 -->
## Error Codes and Messages

Error Codes and Messages


 Code   Description

         applications to create more memory.

 −41000 An unknown error has occurred.

 41000  You attempted to use a function that has no effect with the current report type.

Run-TimeRun-Time MenuMenu ErrorError CodesCodes

The Menu functions and VI Server properties and methods can return the following
error codes. Refer to the KnowledgeBase for more information about correcting errors
in LabVIEW.


 Code  Description

 1158  One or more application items already exist.

 1159  Cannot find one or more application items.

 1160   Illegal menu.

 1161  Cannot find the menu because the front panel is not open.

 1162  Cannot find one or more tags.

 1163   Illegal shortcut.

 1164  Cannot modify an application menu item.

 1165  Cannot find the menu.

 1166  One or more illegal menu item indexes.

 1167  Cannot insert a group item as a menu bar item.

       Exceeded the maximum number of menus for this platform. The VI will use the default run-
 1168
       time menu.

 1169  Cannot select the menu item because it is disabled or has a submenu attached to it.

 1318  Run-time menu shortcuts are not supported for this type of menu.

      Cannot insert or delete menu items while LabVIEW is tracking this menu. This error occurs
      when you use the Insert Menu Items or Delete Menu Items function to add or remove a menu
 1404  item while a user is interacting with the menu. After LabVIEW processes a menu activation
       event, LabVIEW begins to track that menu. For example when you navigate through menus
       with the mouse or the keyboard, LabVIEW tracks that menu. While LabVIEW is tracking a


                                                    © National Instruments 11583

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11583 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11584 ordinal=11584 -->
## Error Codes and Messages

Error Codes and Messages


        Code  Description

              menu, LabVIEW cannot insert or delete items from that menu.

                 This application menu item has been removed. Menu item tags that existed in previous         1437                 versions of LabVIEW as LabVIEW application item tags cannot be used.

               LabVIEW cannot build a path to an .rtm file from the VI being saved. If you save the VI on
         1615  disk, make sure that the .rtm file is saved on the same machine. If you save the VI to a
               network location, make sure that the .rtm file is on the same network.

       ScriptScript NodeNode ErrorError CodesCodes

       Use script nodes to execute math scripts in LabVIEW. LabVIEW provides script nodes
         for the MATLAB® language syntax. Script nodes, including the MATLAB script node, can
         return the following errors. Refer to the KnowledgeBase for more information about
         correcting errors in LabVIEW.


        Code  Description

         1046  LabVIEW cannot initialize the script server. Ensure the server software is installed.

         1047  LabVIEW failed to send variable to the script server.

         1048  LabVIEW failed to get variable from the script server.

         1049  LabVIEW failed to send script text to the script server.

         1050   Error occurred while executing script.

         1053   At run time, LabVIEW cannot find script support DLL.

      SecuritySecurity ErrorError CodesCodes

       The NI Security-related tools and VI Server properties and methods can return the
         following error codes. Refer to the KnowledgeBase for more information about
         correcting errors in LabVIEW.


        Code  Description

               Unable to authenticate because the NI Security library failed to load. Ensure that LabVIEW is
         1367
                   installed properly.


11584   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11584 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11585 ordinal=11585 -->
## Error Codes and Messages

Error Codes and Messages


 Code  Description

      Unable to authenticate because LabVIEW failed to load an NI Security library that is required 1368       to authenticate access.

 1379  The user failed a security authentication check.

SerialSerial ErrorError CodesCodes

The Serial VIs and functions, the Report Generation VIs, and VI Server properties and
methods can return the following error codes. Refer to the KnowledgeBase for more
information about correcting errors in LabVIEW.


 Code      Description

 61          Serial port parity error.

 62          Serial port overrun error.

 63          Serial port receive buffer overflow.

 64          Serial port framing error.

 65          Serial port timeout; bytes not received at serial port.

SharedShared VariableVariable ErrorError CodesCodes

Shared variables can return the following error codes. Shared variables also can return
Real-Time Shared Variable error codes. Refer to the KnowledgeBase for more
information about correcting errors in LabVIEW.


 Code         Description

            The prototype of a shared variable whose data type is custom cannot be an empty
 −1950679041
                variant.

            The value from this shared variable might not be the most current value from the
 −1950679040
              data source.

 −1950679039 Sensor failure

 −1950679038 General device error response.

 −1950679037 The shared variable specified in the binding URL does not exist in the process.

                                                    © National Instruments 11585

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11585 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11586 ordinal=11586 -->
## Error Codes and Messages

Error Codes and Messages


        Code         Description

                       Ensure that all shared variables are deployed and the variable identifier URL is
                           correct.

         −1950679036 General communications failure.

                      Unable to locate the shared variable in the Shared Variable Engine (SVE).
         −1950679035 Deployment of this shared variable may have failed, the SVE has not started, or the
                     SVE is too busy to respond to this request.

                     The shared variable has no value. If you receive this error while trying to read a         −1950679034                       shared variable, refer to the KnowledgeBase at ni.com for more information.

         −1950679033 The shared variable is inactive.

         −1950679032 Sensor inaccurate

         −1950679031  Engineering unit limits exceeded.

         −1950679030  Unspecified error

         −1950679029 Math error

         −1950679028 Communications link failure

         −1950679027 NI-PSP has not connected to the server yet

         −1950679026 DNS lookup failed for the server.

         −1950679025 The server is not reachable.

         −1950679024  Service lookup failed for the server.

                     The process specified in the binding URL does not exist. Ensure that all shared
         −1950679023                          variables are deployed and the variable identifier URL is correct.

                     The process was not found or is not responding. If you receive this error while trying
         −1950679022  to programmatically deploy a library that contains shared variables , refer to the
                     KnowledgeBase at ni.com for more information.

         −1950679021  Failed to resolve URL for this shared variable.

                      Unable to access the shared variable. This error can occur if you attempt to read
         −1950679020 from a write-only variable or write to a read-only variable, or if you do not have
                       permission to access the variable.

                       Subscribe failed. This error can occur when a client attempts to connect to a host
         −1950679019
                        using Logos, when the host only supports LogosXT.

         −1950679018  Invalid URL for this shared variable.

         −1950679016  Invalid float value.

11586   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11586 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11587 ordinal=11587 -->
## Error Codes and Messages

Error Codes and Messages


Code         Description

−1950679015  Invalid Boolean value.

−1950679014 Value attribute not found.

−1950679013  Invalid access type.

−1950679012  Missing access type.

−1950679011  Invalid URL syntax.

−1950679010 Shared variable is bound but the path or URL is not specified.

−1950679009 A path and URL are both specified.

               Invalid value for the Enable Aliasing option. On the Variable page of the Shared
−1950679008  Variable Properties dialog box, verify the values of the options that are enabled
           when you place a checkmark in the Enable Aliasing checkbox.

           A value is missing for the Enable Aliasing option. On the Variable page of the Shared
−1950679007  Variable Properties dialog box, verify the values of the options that are enabled
           when you place a checkmark in the Enable Aliasing checkbox.

               Invalid value for Single Writer option. This option is available only for network-−1950679006             published shared variables.

−1950679005 You must select a name for the shared variable.

−1950679001  Buffer size must be greater than 1.

−1950679000  Array length must be greater than or equal to 2.

−1950678999 Data points in waveform must be greater than or equal to 1.

−1950678998  Global variables can only be accessed from the local machine.

−1950678997 You cannot use a Variable Node of this type on this target.

            The variable configuration is invalid. Edit the variable properties to correct the
−1950678996
               configuration.

−1950678995  Variable has undefined data type.

−1950678994  Variable has invalid data type.

−1950678993 The Raw Full Scale value must be greater than the Raw Zero Scale value.

−1950678992 The Raw Scale and/or Engineering Scale is invalid.

            The Engineering Full Scale value should not be equal to Engineering Zero Scale
−1950678991
               value.


                                                    © National Instruments 11587

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11587 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11588 ordinal=11588 -->
## Error Codes and Messages

Error Codes and Messages


        Code         Description

         −1950678990  Scaling type attribute not specified.

         −1950678989  Scaling ranges not fully specified.

                     The number of arrays, elements, and points per waveform must be greater than or         −1950678988                       equal to 1.

         −1950678987  This piece of configuration does not exist for this type of variable.

         −1950678986  Unspecified shared variable error.

                           Invalid variable name. The name of a variable cannot start with a single quote ('),
         −1950678985  start or end with a space, or contain a backslash, forward slash, or any of the
                         following backslash '\' codes: \r \n \t \b \s.

         −1950678984  Variable names can have a maximum of 255 characters.

                     The array sizes in the network buffer must be greater than or equal to the array sizes
                           in the real-time FIFO buffer. The waveform sizes in the network buffer must be
                         greater than or equal to the waveform sizes in the real-time FIFO buffer. To correct
         −1950678983  this error, ensure that the values of the Array Size and Waveform Size options on the
                         Variable page of the Shared Variable Properties dialog box are greater than or equal
                         to the corresponding values of the Array Size and Waveform Size options on the
                      Real-Time FIFO page of the Shared Variable Properties dialog box.

         −1950678982 The shared variable client-side read buffer is full.

         −1950678981 The shared variable client-side read buffer overflowed.

         −1950678980 The shared variable server-side write buffer is full.

         −1950678979 The shared variable server-side write buffer overflowed.

                     The project that contains the project library you want to add a shared variable to         −1950678978
                    must be open.

                      Unable to deploy the library because the name is reserved. You cannot deploy a
         −1950678977  library named "System", "LV", or "FP". You also cannot deploy a library with a name
                         that starts with "NI_".

                     The specified I/O Variable is configured with a timeout, but timeouts are not
         −1950678959
                      supported when accessing an I/O variable locally.

                     The string for the Variable Engine or protocol portion of the URL is invalid. You
                      cannot use the characters _~!$&'()*,;=:/?#[]@ in their decoded form. To         −1950678954
                          specify one of these characters in a URL, you must replace these characters with
                           their percent-encoded UTF-8 equivalents.

         −1950678953 The URL is invalid. The URL uses the general form [Variable Engine]:// or

11588   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11588 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11589 ordinal=11589 -->
## Error Codes and Messages

Error Codes and Messages


 Code         Description

            ni.dex://, which indicates a host name should follow, but the URL does not
                specify a host name. To correct the problem, specify the host name of the computer
               that hosts the resource. If the resource hosts on the same computer where the VI is
               running, you can use the host name localhost or you can omit the host name. For
                variables, use URL format [Variable Engine]:/[Container
           Name]/[Variable Name]. For network stream endpoints use URL format
           ni.dex:/[Endpoint Name].

            The path in the URL is invalid. The path contains one or more of the reserved
               characters /?#[]!$&*+;=, which you cannot use in their decoded form. To
                identify resources that contain these characters as part of their name, replace the
 −1950678948  reserved character with its percent-encoded UTF-8 equivalent form. For example,
           ni.var.psp://localhost/PathSegment1/channel#1 becomes
           ni.var.psp://localhost/PathSegment1/channel%231 where %23 is
              the percent encoded UTF-8 equivalent form for the # character.

            The host name specified in the variable identifier URL does not correspond to the
                local host, but the specified variable engine URL only supports an operation on the
 −1950678945  local host. You cannot perform the specified operation on a remotely hosted variable
               or stream endpoint. Use the PSP Variable Engine URL (ni.var.psp) to read or write a
              network-published I/O variable or I/O alias remotely.

            The Class Identifier property of the variable object specified in the variable identifier
           URL is incompatible with the refnum configuration. The class of the variable object is
 −1950678944 not equivalent to or does not derive from the class you configured for the refnum.
               This error might occur if you try to reference a Variable object, but the specified
                variable identifier URL does not reference a Variable.

 −1950678943 Timed out while attempting to open a connection to the variable.

 −1950678942  Scaling coerce attribute not specified.

            An empty string is not a valid URL. If you want to reference the root container within
 −1950678941 a variable engine, you need to specify the path explicitly using one of the following
           URL formats: "[Variable Engine]://[Host Name]", "[Variable Engine]:", or "/".

 −1950678934  Requires an open variable connection to read or write the specified property.

SignalSignal ProcessingProcessing ErrorError CodesCodes

The Signal Processing VIs and VI Server properties and methods can return the
following error codes. Refer to the KnowledgeBase for more information about
correcting errors in LabVIEW.

                                                    © National Instruments 11589

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11589 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11590 ordinal=11590 -->
## Error Codes and Messages

Error Codes and Messages


        Code   Description

         −20337 The specified time stamp occurs after the end of the limit.

                Waveforms are not contiguous. You can concatenate two waveforms (A, B) with same dt
         −20335  only if they are contiguous, that is if t0_B = t0_A + N * dt, where N is the number of samples
                    of waveform A.

                Cannot align waveforms because their time stamps are separated by more than 10 times         −20334                  the duration of the longest waveform.

                Cannot align two waveforms with same dt if their samples are not clocked in-phase.
         −20333 Alignment of two waveforms is possible only if the samples share the same dt and are in-
                  phase, that is the difference between their t0s is a integer multiple of dt.

                    Internal error: The number of threads attribute is less than zero. If the problem persists,         −20332                   contact National Instruments technical support.

                    Internal error: The parameter struct pointer is Null, possibly because of changes to the
         −20331  calling VI block diagram. If the problem persists, contact National Instruments technical
                   support.

                    Internal error: The result pointer is Null, possibly because of changes to the calling VI block         −20330
                  diagram. If the problem persists, contact National Instruments technical support.

                    Internal error: The cursor struct pointer is Null, possibly because of a change to the calling
         −20329                     VI block diagram. If the problem persists, contact National Instruments technical support.

                     Failure initializing a critical section in measurement code, possibly due to low memory. If
         −20328                  the problem persists, contact National Instruments technical support.

               An exception occurred in the measurement code, possibly due to low memory. If the
         −20327                problem persists, contact National Instruments technical support.

         −20326 The slew rate is infinite because the rise or fall time is zero.

                    Internal error: Two measurements share the same ID number. If the problem persists,
         −20324
                   contact National Instruments technical support.

         −20323 The edge number, pulse number, or cycle parameter value must be greater than zero.

                    Internal error: The attribute number does not refer to a valid parameter. Check the
         −20322
                  reference levels, percent level settings, and state settings inputs.

                    Internal Error: The measurement session handle is invalid. If the problem persists, contact
         −20321
                   National Instruments technical support.

                    Internal error: The requested measurement is not available. If the problem persists,
         −20320
                   contact National Instruments technical support.


11590   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11590 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11591 ordinal=11591 -->
## Error Codes and Messages

Error Codes and Messages


Code   Description

−20319 The period of the waveform is too short to perform the measurement.

−20318 The result is not a number (NaN) or infinite.

−20317 The histogram size parameter value is less than or equal to zero.

−20316  Illegal percent method parameter. Check the method enumerated type input.

−20315 The waveform dt parameter is ≤ 0.

−20314  Illegal reference level units parameter. Check the ref units input.

        Reference levels do not satisfy requirements. The low ref must be less than or equal to the−20313       mid ref, which must be less than or equal to the high ref.

−20312 The input waveform size is zero.

−20311  Insufficient memory available for waveform measurement.

       The waveform did not have enough edges to perform this measurement. An edge is
−20310  defined as a crossing of both the low and high reference levels. Check the signal length,
        reference levels, and ref level units.

−20309 The amplitude of the waveform is zero, so the histogram method cannot be used.

       The waveform did not cross the mid reference level enough times to perform this−20308
       measurement. Check the signal length, reference levels, and ref level units.

−20307 Frequency not a multiple of (Sampling Rate)/Samples.

−20306 The two time signal waveforms contain different dt.

−20305 The two time signal waveforms contain different number of data points.

        At least one of the time signal waveforms does not contain the correct dt to continue the−20304
        averaging process.

        At least one of the time signal waveforms does not contain the correct number of data
−20303
        points to continue the averaging process.

       The time signal waveform does not contain the correct dt to continue the averaging
−20302
         process.

       The time signal waveform does not contain the correct number of data points to continue
−20301
        the averaging process.

−20131 The order must be less than or equal to the degree.

−20130 The input is not a prime number.

−20129 The size of the input array is not a power of the radix.


                                                    © National Instruments 11591

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11591 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11592 ordinal=11592 -->
## Error Codes and Messages

Error Codes and Messages


        Code   Description

                The size of the Hadamard matrix does not meet size requirements. The valid size is 2^k,         −20128                  12*2^k, or 20*2^k where k > 0.

         −20119 The number of samples is not equal to three.

         −20118 The input is greater than 1 or less than -1.

         −20117  Significance has been lost. Computation failed due to loss of significance.

         −20116  Feasible solution not found.

         −20115 The FFT size must be greater than zero.

                The start value wired to the Polynomial Real Zeros Counter VI is greater than the end value.         −20114
                     Verify the values you wired to the Polynomial Real Zeros Counter VI.

         −20113 The end value wired to the Polynomial Real Zeros Counter VI is a root.

         −20112 The start value wired to the Polynomial Real Zeros Counter VI is a root.

         −20111 The input polynomial coefficients are all zeros.

         −20107 The number is out of range. The valid range is [0, pi].

         −20106 The number is out of range. The valid range is [0, pi/2].

         −20104  Input parameters have at least one NaN element.

         −20103 The order must be greater than or equal to zero.

         −20102 The shifts must meet: |shifts| < samples.

                The maximum value of the parameter must be greater than the minimum value of the         −20101                  parameter.

         −20078  This functionality is not supported on this platform.

         −20077 The time points are not in ascending order.

         −20076 The resample point cannot be calculated with the signal behind that of the input.

         −20075 The filter buffer overflows.

         −20074 Reordering eigenvalues changed some complex ones.

         −20073 The eigenvalues cannot be reordered because some of them are too close.

         −20072 The logarithm of the input matrix cannot be computed.

         −20071 The input matrix is not positive definite.

         −20070  Matrices must have the same size.


11592   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11592 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11593 ordinal=11593 -->
## Error Codes and Messages

Error Codes and Messages


Code   Description

−20069 The number of samples must be greater than or equal to four.

−20068  Input parameters has at least one element that is Inf, NaN, DBL_MAX, or DBL_MIN

−20067 The input fundamental frequency or sampling rate is equal to zero.

−20066 The information in IIR filter structure is not correct.

−20065 The elements in the vector can not be all zero.

−20064 The internal memory state of this function was not initialized correctly.

−20063 The coefficients of the polynomial are invalid.

−20062 The maximum number of iterations was exceeded.

−20061 The selection is invalid.

−20060  Divide by zero error.

−20059  Negative number error

−20058  Invalid number of dimensions or dependent variables

−20057 The parameter to the beta function should be 0 < p < 1

−20056 The contingency table has a negative number.

−20055 The number of categories or samples must be greater than one.

−20054 The probability must be greater than or equal to zero and less than one.

−20053 The number must be between zero and one.

       The degree of freedom must be greater than zero and less than the length of the input−20052        sequence.

−20051  All values in the first column of X matrix must be one.

−20050 The interpolating function has a pole at the requested value.

−20049 The x-values must be distinct.

−20048 The Random Effect model was requested when the Fixed Effect model is required.

−20047 The data is unbalanced. All cells must contain the same number of observations.

−20046 There is an overflow in the calculation.

       The total number of data points must be equal to the result of multiplying each level and
−20045
        the number of observations per cell.

−20044 Zero observations were made at some level of a factor.

                                                    © National Instruments 11593

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11593 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11594 ordinal=11594 -->
## Error Codes and Messages

Error Codes and Messages


        Code   Description

         −20043 The level of factors is outside the allowable range of some data.

         −20042 The number of levels is out of range.

         −20041 The system of equations cannot be solved because the input matrix is singular.

         −20040 The input matrix must be a square matrix.

                The number of columns in the first matrix is not equal to the number of rows in the second         −20039                   matrix or vector.

         −20038 The number of intervals must be > 0.

         −20037 The number of data points in the Y value array must be greater than the order value.

         −20036 The elements of the Y Values array must be nonzero and either all positive or all negative.

         −20035 The standard deviation must be greater than zero for normalization.

         −20034 The number of coefficients must be even for this filter.

         −20033 The number of coefficients must be odd for this filter.

                The left rank of the filter must meet: left rank ≥ 0. The right rank of the filter must meet:         −20032
                     right rank < size.

         −20031 The filter cannot be designed with the specified input values.

         −20030 The leakage coefficient, leak, and step-size parameter, u, must meet: 0 ≤ leak ≤ u.

         −20029 The step-size, u, must meet: 0 ≤ u ≤ 0.1.

         −20028 The attenuation value must be greater than the ripple amplitude.

         −20027 The final value must be > 0.

         −20026 The width must be > 0.

         −20025 The attenuation must be > 0.

         −20024 The ripple amplitude must be > 0.

         −20023 The following conditions must be met: 0 < f_low ≤ f_high ≤ fs/2.

         −20022 The decimating factor must meet: 0 < decimating factor ≤ samples.

         −20021 The order must be greater than 0.

         −20020 The cut-off frequency, fc, must meet: 0 ≤ fc ≤ fs/2.

         −20019 The upper value must be ≥ the lower value.

         −20018 The following condition must be met: 0 ≤ (index + length) < samples.

11594   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11594 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11595 ordinal=11595 -->
## Error Codes and Messages

Error Codes and Messages


Code   Description

−20017 The following condition must be met: 0 ≤ index < samples.

−20016  dt must be > 0.

−20015  dt must be ≥ 0.

−20014 The following conditions must be met: 0 ≤ (delay + width) < samples.

−20013 The width must meet: 0 < width < samples.

−20012 The number of cycles must be > 0 and ≤ the number of samples.

−20011 The duty cycle must be equal to or fall between 0 and 100: 0 ≤ duty cycle ≤ 100.

−20010 The maximum allowable transform size has been exceeded.

−20009 The size of the input array must be a power of two: size = 2^m, 0 < m < 23.

−20008 The input arrays do not contain the correct number of data values for this function.

−20007 The number of samples must be greater than or equal to 3.

−20006 The number of samples must be ≥ 2.

−20005 The number of samples must be greater than or equal to 1.

−20004 The number of samples must be ≥ 0.

−20003 The number of samples must be > 0.

−20002 The input sequences must be the same size.

−20001 There is not enough memory to perform the specified routine.

20001  The matrix is rank deficient.

20002  The number of samples must be greater than zero.

20003  The matrix is singular.

20004   Matrices or vectors do not have the same size.

20006  The computation result might be inaccurate.

20007  The input is an invalid Cholesky factorization.

20008  The matrix is not positive-definite.

20010  The sizes of the input arrays do not meet the specified conditions.

20011  The input standard deviation is invalid.

20012  The input polynomial is empty.


                                                    © National Instruments 11595

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11595 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11596 ordinal=11596 -->
## Error Codes and Messages

Error Codes and Messages


        Code   Description

         20020  Some frequencies violate Nyquist criteria.

         20030  The input matrix has at least one element with a value of Inf or NaN.

         20307  Frequency was coerced to the nearest multiple of (sampling rate)/samples.

                Waveforms are not overlapping. The time stamp of one waveform is not contained within         20334
                  the duration of a second waveform.

                The averaging process was automatically restarted to respond to a change in the averaging         20351                  parameters.

         20352   Current and previous waveforms are not contiguous.

         20353   Current and previous dt not equal.

    SMTPSMTP EmailEmail ReplyReply CodesCodes

       The SMTP Email VIs can return the following error codes. Refer to the KnowledgeBase
         for more information about correcting errors in LabVIEW.


        Code  Description

         16211 211 System status or system help reply.

                214 Help message. Information about how to use the receiver or the meaning of a particular         16214                 non-standard command; this reply is useful only to the human user.

         16220 220 "domain" Service ready.

         16221 221 domain service closing transmission channel.

         16250 250 Requested mail action okay, completed.

         16251 251 User not local; will forward to "forward-path."

         16354 354 Start mail input; end with two carriage-return/line-feed characters.

                421 "domain" service not available, closing transmission channel. This might be a reply to
         16421
               any command if the service knows it must shut down.

                450 Requested mail action not taken: mailbox unavailable. For example, the mailbox might
         16450
               be busy.

         16451 451 Requested action aborted: local error in processing.

         16452 452 Requested action not taken: insufficient system storage.

11596   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11596 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11597 ordinal=11597 -->
## Error Codes and Messages

Error Codes and Messages


 Code  Description

       500 Syntax error, command unrecognized. For example, the command line might be too 16500        long.

 16501 501 Syntax error in parameters or arguments.

 16502 502 Command not implemented.

 16503 503 Bad sequence of commands.

 16504 504 Command parameter not implemented.

       550 Requested action not taken: mailbox unavailable. For example, the mailbox was not 16550       found or there is no access.

 16551 551 User not local; try "forward-path."

 16552 552 Requested mail action aborted: exceeded storage allocation.

       553 Requested action not taken: mailbox name not allowed. For example, the mailbox 16553
        syntax might be incorrect.

 16554 554 Transaction failed.

SourceSource ControlControl ErrorError CodesCodes

The Source Control VIs and VI Server properties and methods can return the following
error codes. Refer to the KnowledgeBase for more information about correcting errors
in LabVIEW.


 Code  Description

       The LabVIEW project is configured not to use source control. You must enable source control
 −2985  in order to perform source control operations. Select Project>>Properties to configure
        source control settings for the LabVIEW project.

       The source control settings for the LabVIEW project require a different source control
        provider than what is configured for the LabVIEW environment. Select Tools»Source
 −2984
        Control»Configure Source Control to change the source control provider for the LabVIEW
       environment.

       LabVIEW could not access the source control provider. The LabVIEW source control
        configuration settings are not valid for this session or a timeout occurred. Select
 −2983
       Tools»Source Control»Configure Source Control to reconfigure source control. If you
        receive this error while running an application that uses Source Control VIs, refer to the


                                                    © National Instruments 11597

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11597 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11598 ordinal=11598 -->
## Error Codes and Messages

Error Codes and Messages


        Code  Description

               KnowledgeBase at ni.com for more information.

               The specified file is not a valid LabVIEW file type. Enter a path to an existing LabVIEW file,         −2982                such as a VI or control.

              An error occurred while comparing the specified file. The local file is not the latest version in
         −2981 source control. Select Tools>>Source Control>>Get Latest Version to copy the latest
                  version to the local directory if you want to perform a comparison.

         −2980 The value of an input parameter is out of range.

               The source control configuration data is invalid, corrupted, or missing. Verify that the data is         −2979
                    valid for the source control provider you selected during configuration.

               The number of files input does not match the version information input. Make sure the two         −2978                  inputs contain the same number of elements.

         −2977 The input file type is not compatible with the file retrieval method.

         −2976  Invalid source control reference.

         −2975 No valid file paths were specified. You must enter at least one valid file path.

         −2974 An error occurred while uninitializing the source control provider.

              An error occurred while loading the source control DLL. The source control provider might
         −2973 have been moved or removed without a registry update. You might need to reinstall the
                 source control provider.

         −2972 An internal error occurred during the source control operation.

              An error occurred while accessing the source control provider. The specified provider was         −2971                 not found.

               You cannot perform source control operations until you configure source control in
         −2970 LabVIEW. Select Tools»Source Control»Configure Source Control to configure source
                   control.

               You cannot perform the specified source control operation on files marked as Open for Add
         −2964  or Open for Delete. Submit these files to the source control provider before you attempt the
                  operation.

               The changelist does not include a valid description. Verify that the description is not empty
         −2963
               and does not contain the default text.

         −2962 Unable to locate or run the administration tool from the source control provider.

                      All files in a single submit operation must be the latest version, checked out to the user, not
         −2961
                 locked by another user, and under source control.


11598   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11598 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11599 ordinal=11599 -->
## Error Codes and Messages

Error Codes and Messages


Code  Description

      The specified files are not in the same changelist. All files in a single submit operation must−2960      be in the same changelist.

−2955 An error occurred during the specified source control operation.

      A connection with the source control provider already exists. Disconnect from the current−2954
       source control provider before you open a new connection.

      The specified source control provider is not compatible with LabVIEW. The source control
       provider does not support required LabVIEW functionality. On Windows, LabVIEW integrates
−2953 with any source control provider that supports the Microsoft Source Code Control interface.
     On non-Windows platforms, LabVIEW integrates with Perforce using a command line
        interface.

−2952 The length of an input parameter exceeds the maximum allowed value.

      The specified source control operation cannot run because the source control provider is−2951       not initialized.

−2950 The specified option is invalid.

−2929 A failure occurred in the connection with the source control provider.

−2928 Unable to locate the local copy of the specified file.

      An error occurred while opening a source control project or accessing a file. An input value
−2927       uses invalid file syntax.

−2926 The user is not allowed to perform this operation.

      An error occurred while performing the specified operation. No source control project is−2925       open.

      An error occurred while opening a source control project or accessing a file. The specified−2924
       path is invalid.

      An error occurred while opening the specified source control project. An input value uses
−2923
        invalid syntax for the source control project syntax.

−2922 The specified source control project is already open.

      An error occurred while logging into the source code provider. The specified user login is
−2921
        invalid. Verify the login information you entered.

−2920 An error occurred within the source control provider program, such as shell failure.

      An error occurred during file check-in. The specified file was automatically merged but was
−2919
       not checked in because you must resolve a merge conflict manually.

−2918 An error occurred during file check-in. The specified file was automatically merged but was

                                                    © National Instruments 11599

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11599 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11600 ordinal=11600 -->
## Error Codes and Messages

Error Codes and Messages


        Code  Description

                 not checked in, pending user verification.

              An error occurred while adding a file to source control. The source control provider does not         −2917                 support the file type (binary or text).

         −2916 The source control provider did not perform the specified operation.

               The source control provider returned a non-specific error. The specified operation was not         −2915                 performed.

         −2914 The source control provider does not support the specified operation.

               The version of the file you specified does not exist or was not specified correctly. Specify a         −2913
                    valid version or date and time.

              An error occurred while retrieving or removing the specified file. The file is currently         −2912                checked out, so the provider is unable to retrieve or remove it.

         −2911 The specified file is not under source control.

              An error occurred while adding a file to source control. The specified file is in source control         −2910
                   already.

         −2909  File check-in did not occur because of a conflict error. Another user has checked in the file.

              An error occurred while accessing source control. Check for network or contention         −2908                 problems.

              An error occurred while checking out a file. The specified file is exclusively checked out by         −2907                 another user.

         −2906 An error occurred while checking out a file. The specified file is locked.

         −2905 An error occurred while checking out a file. The specified file already is checked out.

              An error occurred while checking in or undoing the check out of a file. The specified file is
         −2904
                 not checked out to the current user.

              An error occurred while opening the specified source control project. The source control
         −2903
                  provider could not create the source control project.

              An error occurred while opening the specified source control project. The source control
         −2902  provider does not recognize the project name. Verify that the project name and location are
                    correct.

         −2901 An error occurred during source control provider initialization.


11600   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11600 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11601 ordinal=11601 -->
## Error Codes and Messages

Error Codes and Messages

Storage/DataPluginStorage/DataPlugin andand TDMTDM StreamingStreaming ErrorError CodesCodes

The Storage/DataPlugin VIs and the TDM Streaming VIs and functions can return the
following error codes. Refer to the KnowledgeBase for more information about
correcting errors in LabVIEW.


 Code   Description

        The TDMS Defragment, TDMS Convert Format, and TDMS Delete Data functions cannot
 −68027  process a file that has a TDMS segment containing data from multiple groups with
         interleaved channels. Data can be read from the file using the TDMS Read function.

 −68026  Failed to delete data from the .tdms file, because channel names contains digital data.

          Failed to delete the index file after writing data to the TDMS file. National Instruments −68025       recommends that you delete the index file manually.

        The TDM Streaming VIs and Functions do not support extended-precision floating-point −68024        numbers on Linux, OS X, and VxWorks.

          Failed to update the .tdms file. This file might be incomplete due to an application crash
         during the logging process. You can still read the existing data from this file, but you −68018
        cannot append new data to this file. Consider creating a new .tdms file for your
          application.

        The hierarchy of certain channels or groups in the file is not supported by the current
 −68017  version of LabVIEW. Upgrade LabVIEW to the latest version to fix this error. Contact
         National Instruments if this error persists.

        The data in certain channels or groups of the file is not supported. LabVIEW skips these
 −68016 channels or groups when listing content of the file. Upgrade LabVIEW to the latest version
         to fix this error. Contact National Instruments if this error persists.

         This channel contains multi-dimension data that is not recognized by the current version
 −68015  of LabVIEW. Upgrade LabVIEW to the latest version to fix this error. Contact National
         Instruments if this error persists.

          Failed to append data to the specified channel because the dimension of the new data
 −68014
        does not match that of the existing data.

          Failed to access the specified channel because this channel is protected by LabVIEW. You
        cannot rename the group that contains the protected channel because renaming a group
 −68013
          affects all channel names under that group. If you are creating a new channel or renaming
        an existing channel, use another channel name.

 −68010  File is still in use. Close all other references to this file before truncating the file.


                                                    © National Instruments 11601

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11601 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11602 ordinal=11602 -->
## Error Codes and Messages

Error Codes and Messages


        Code   Description

              TDMS asynchronous mode is not initialized properly. Make sure the enable asynchronous?
                   input of the TDMS Advanced Open function is TRUE. If you are writing data to a file, also
         −68009 make sure the TDMS Configure Asynchronous Writes (Data Ref) function exists. If you are
                  reading data from a file, also make sure the TDMS Configure Asynchronous Reads (Data
                    Ref) function exists.

                The data type input of the TDMS Configure Asynchronous Writes function is not wired. If
                  the pre-allocate? input of this function is TRUE, you must wire a supported data type to
         −68008  this function. LabVIEW uses the data type information to determine the size of each pre-
                   allocated buffer. The data type input accepts integers, floating-point numbers, Booleans,
                and timestamps.

                   This channel or property value contains a data type that is not recognized by this version         −68007                    of LabVIEW.

                    Failed to perform this operation. You cannot use the TDMS Advanced Asynchronous I/O         −68006
                   functions and the TDMS Advanced Data Reference I/O functions jointly.

                    Failed to manipulate the .tdms file when the file is opened with the TDMS Advanced Open
         −68004  function. You must either use the TDMS Open function to open the .tdms file or use the
                Advanced TDMS VIs and functions to manipulate the .tdms file.

                      File is opened in asynchronous mode. You must either set the enable asynchronous input
         −68003  of the TDMS Advanced Open function to FALSE or use the TDMS Advanced Asynchronous
                   Write or TDMS Advanced Asynchronous Read function to perform the operation.

                    Failed to reserve file size. If you are running the TDMS Reserve File Size function on
               Windows with User Account Control enabled, you must run LabVIEW or the application         −68002                  with administrator privileges. Refer to the KnowledgeBase for more information about
                  using User Account Control.

                    Failed to perform the operation. You must use the TDMS Advanced Open function to open
         −68001
                  the .tdms file.

                  Concurrent references to the same .tdms file cannot be opened with different values for
         −68000 the disable buffering? or enable asynchronous? input of the TDMS Advanced Open
                    function.

         −2595   Failed to get the version information about the DataPlugin.

               An error occurred while connecting to the DataPlugin server. Possible reasons include a
         −2594
                     failed network connection or a server connection problem.

               An error occurred while installing the DataPlugin. Possible reasons include an invalid
         −2593
                  DataPlugin name or a failed network connection.

         −2592  TDMS does not support replacing channel values.

11602   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11602 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11603 ordinal=11603 -->
## Error Codes and Messages

Error Codes and Messages


Code   Description

       You must install NI-DAQmx on the computer to store NI-DAQmx properties by using the−2591        Storage/DataPlugin VIs.

         Failed to export the DataPlugin. You can export only DataPlugins with a type of VBS or−2590        VBCrypt. Use the List DataPlugins VI to view the type of a DataPlugin.

         Failed to unregister the DataPlugin. You cannot unregister the DataPlugins that LabVIEW−2589          installs by default.

         Failed to register the DataPlugin. The DataPlugin .uri file might contain invalid DataPlugin−2588        information.

       LabVIEW failed to write data to the .tdms file. Ensure that the file format version you
         specified for the TDMS Open function supports the data you want to write. For example, to
−2587   write interleaved data or data you acquire from an NI-DAQmx device, you must select 2.0
         for the file format version input. To write data in big-endian format, you also must select
        2.0 for the file format version input.

        Support for the TDMS file format is not currently installed on your machine. You can−2586       download it from the DataPlugins Web site at ni.com.

−2585  The .tdm file format is not currently supported on this operating system.

       Cannot append data to the existing file because the value of the X Value Columns option of
        the Write to Measurement File Express VI changed. This error occurs when the value of the
−2583  X Value Columns option changes from the value specified when the file was first created.
       To correct this error, use the same X Value Columns value when you use this Express VI to
       append data to an existing file.

       The Write to Measurement File Express VI cannot append new data to the file because the
        time information of the signals stored in the file does not match the signals you are trying
−2582   to append. You can append waveforms only if their dt values match and the t0 value of the
      new data matches the next time increment after the last saved value. To correct this error,
         set the Segment Headers option to One header per segment.

       The Write to Measurement File Express VI cannot append new data to the file because the
−2581   signals stored in the file don't match the signals you are trying to append. To correct this
          error, set the Segment Headers option to One header per segment.

         After deleting data from a file, you must close the file and reopen it before you can perform
−2578
       a read operation.

        Storage VIs version conflict. This version of LabVIEW cannot interpret the parameters of the
−2575
        Storage VI. The VI was created in a more recent LabVIEW version.

       The string you wired to this VI contains binary characters that are not valid entries for
−2574
         string values in a .tdm file. To store binary data, use data channels with a data type of 8-bit

                                                    © National Instruments 11603

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11603 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11604 ordinal=11604 -->
## Error Codes and Messages

Error Codes and Messages


        Code   Description

                 unsigned integer.

         −2572   This property is not part of the Storage VI data structure.

         −2571   This object type is not part of the Storage VI data structure.

                LabVIEW could not write the file back to disk. The file might be write protected by the
                   operating system. To open the file for a read-only operation, select open (read only) in the         −2570                 Overwrite options (if not wired) pull-down menu in the Configure Open Data Storage
                   dialog box.

                LabVIEW cannot convert the object ID into a valid refnum. An object with this ID does not         −2569
                      exist in the data storage file.

         −2568  LabVIEW failed to allocate memory from the operating system of your computer.

         −2566  An input parameter to this VI is invalid.

                LabVIEW could not load the data channel you specified from the data storage file. The
                 channel either is empty or the properties that describe the channel, such as length or data
                    type, are incomplete. You might be trying to read data in a format that is not compatible
         −2565   with the format in which it was written. If you are using the Read Data VI, which reads
                   multiple channels, consider using a query condition to exclude some of the channels from
                  being loaded. You can determine the data type of a channel by reading the Data type
                   property.

                The software installed on this computer does not support the file format you requested.
         −2564  The Storage/DataPlugin VIs access files through plug-in libraries LabVIEW and DIAdem
                        install. Refer to the National Instruments Web site to download the library you need.

                The data type of a property or channel could not automatically be coerced when writing to         −2562                   or reading from a data storage file.

                 Data storage is write-protected. LabVIEW cannot write data to this data storage file
                 because it is write-protected. The file might be write protected by the operating system. To
         −2561
                open the file for a read-only operation, select open (read only) in the Overwrite options (if
                 not wired) pull-down menu in the Configure Open Data Storage dialog box.

                LabVIEW cannot load the USI components the Storage/DataPlugin VIs require. These
         −2560  components are installed by LabVIEW and DIAdem. Refer to the National Instruments Web
                      site to download the components you need. You may need to reinstall LabVIEW or DIAdem.

         −2559  The data storage file is already open.

                LabVIEW cannot open the data storage file. Ensure that you chose a correct DataPlugin for
         −2558
                      this file format.

         −2557  There is an error in the query expression.

11604   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11604 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11605 ordinal=11605 -->
## Error Codes and Messages

Error Codes and Messages


Code   Description

−2556  LabVIEW cannot find the object type.

−2555  LabVIEW cannot write to a read-only data storage file.

−2554  LabVIEW does not support the data type of this property.

       The object refnum is invalid. The node that returned this refnum might have encountered
       an error and did not return a valid refnum. The storage this refnum refers to might have
−2553   closed before the call executed. This error usually is the result of an error being
        encountered, such as failing to open a storage or looking for a channel that does not exist.
         Valid refnums become invalid when the storage they refer to is closed.

−2551  The property data type does not match.

−2550   This property does not exist.

       Asynchronous reads from an earlier operation are still in progress. You cannot configure or
−2549   start an asynchronous read unless the previous operation has been completed or stopped.
       You can stop asynchronous reads by using the TDMS Stop Asynchronous Reads function.

         Failed to write raw data to the .tdms file without channel information. Use the TDMS Set
       Channel Information function to specify the channel information for the raw data. The
−2548   error may be caused by incorrect calling of TDMS Create Scaling Information VI. To call this
         VI with TDMS Advanced functions, only call the TDMS Set Channel Information function
          after any calls to the TDMS Create Scaling Information VI.

       LabVIEW failed to complete this operation. Verify that the values of both the max
       asynchronous writes input of the TDMS Configure Asynchronous Writes function and the
      number of buffers input of the TDMS Configure Asynchronous Reads function are less than
−2547         64. Also verify the array size of the data input of the TDMS Advanced Write function is
       below the maximum value. Refer to the LabVIEW Help for more information about using
        the TDMS Advanced Write function.

       Asynchronous reads or writes failed due to timeout. Increase the timeout value for the
−2546
        corresponding function.

      TDMS asynchronous mode is not initialized properly. Make sure the enable asynchronous?
        input of the TDMS Advanced Open function is TRUE. If you are writing data to a file, also
−2545  make sure the TDMS Configure Asynchronous Writes function exists. If you are reading
        data from a file, also make sure that both the TDMS Configure Asynchronous Reads and
        the TDMS Start Asynchronous Reads functions exist.

        With operating system buffering disabled, array sizes and file positions for the Advanced
−2544  TDMS VIs and functions must be integer multiples of the hard disk sector size. Use the
      TDMS Advanced Open function to retrieve the sector size.

−2543  LabVIEW failed to open the .tdms file for raw data access. This error occurs if the file format

                                                    © National Instruments 11605

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11605 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11606 ordinal=11606 -->
## Error Codes and Messages

Error Codes and Messages


        Code   Description

                   version is 1.0 or if the file contains raw data that is not encoded in native-endian. Use the
              TDMS Defragment function and the TDMS Convert Format VI to convert the file to native-
                 endian and version 2.0.

                      Files that contain DAQmx data samples cannot be processed by the TDMS Convert Format,         −2542
              TDMS Defragment, and TDMS Delete Data functions.

                    Failed to scale the data in the .tdms file. The NI TDMS component on your computer does
                  not support the scale type. Upgrade the NI TDMS component to the latest version before         −2541                  reading the .tdms file. Refer to the National Instruments Web site for information about
                      installing the latest version of the NI TDMS component.

                 Reading data that was streamed to a .tdms file by NI-DAQmx and data that was added to         −2540                  the file using a different application requires separate TDMS Read functions.

                   This file cannot be written to, because it is opened and locked by another thread or
         −2539   process. This typically happens when a file is written by a hardware driver, for example NI-
               DAQmx.

                    Failed to add scaling information to the TDMS object. This object contains scaling         −2538
                  information that has already been applied.

                    Failed to convert the "name" property to TDMS file format version 2.0. In file format
                   version 2.0, "name" must be a string. To correct this error, you can use the new property         −2537              name input of the TDMS Convert Format VI to specify a new name for the "name"
                   property.

                LabVIEW failed to scale the data in the .tdms file. Ensure that this function supports the
         −2536                  data type that you specify.

         −2535  LabVIEW failed to create a scale for the .tdms file.

         −2534  The type of interleaved data is not supported by TDMS.

                LabVIEW failed to save the data in interleaved format because the data is either an analog
         −2533  waveform, a compressed digital table or waveform, or a 1D or 2D string array. LabVIEW
                 saved the data in decimated format.

         −2532   Invalid group name and/or channel name.

         −2531  LabVIEW could not unload the TDMS file component.

                    Failed to perform the operation on this .tdms file because pending data for this file exists.
         −2530
                Use the TDMS Flush function to flush the data to disk.

                     In TDMS files, channels in the same channel group must have unique names. You can
         −2529   provide unique channel names by using the "channel name(s)" input of the specified TDM
                 Streaming Function. If you are using waveforms or the LabVIEW Express Dynamic Data

11606   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11606 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11607 ordinal=11607 -->
## Error Codes and Messages

Error Codes and Messages


Code   Description

        Type, use the waveform attribute "NI_UpdateChannelName" to set a channel name.

       LabVIEW dynamically calculates the value of this property. You cannot write any values to
−2526   this property. This typically applies to properties like "NI_ChannelLength" or
        "NI_DataType".

−2525  TDMS file data could not be converted into the specified data type.

       You have attempted to open a TDM file. Use the Read From Measurement File Express VI or−2524        the Storage/DataPlugin VIs to open this file.

−2522   This TDMS file is open as a read-only file. Close the file before you open it for writing.

       LabVIEW could not load the TDMS file component. The component is expected in the
−2519  National Instruments\shared\TDMS directory. You might need to reinstall
       LabVIEW to fix this problem.

       The specified array dimension is not supported. The TDMS functions support only 1D or 2D−2518
         arrays.

       LabVIEW could not create an index file for this TDMS file. The disk might be write−2516
         protected. Without an index file, LabVIEW will not be able to open the TDMS file.

      When appending data to an existing data channel, the data types of the existing data and
−2515        the new data did not match.

−2514   This function does not accept the specified data type.

−2513  LabVIEW does not support properties of the specified data type.

−2511  The specified TDMS file is corrupt.

        This TDMS file complies with a new version of the TDMS format that is not supported by
−2510   this version of LabVIEW. Refer to the DataPlugins Web site at ni.com for more information
       about the TDMS file format.

−2509  LabVIEW no longer supports this version of the TDMS file format.

−2508   Invalid property.

−2507   Invalid group name and/or channel name.

−2506  LabVIEW failed to read data from the TDMS file.

−2505  LabVIEW failed to write data to the TDMS file.

−2504  LabVIEW failed to close the TDMS file.

−2503   Specified file does not comply with TDMS file format standards.

−2502   String values are stored in TDMS files in utf8 unicode format. LabVIEW uses operating

                                                    © National Instruments 11607

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11607 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11608 ordinal=11608 -->
## Error Codes and Messages

Error Codes and Messages


        Code   Description

                 system functions to convert the unicode data, and one of these operating system functions
                 has returned an error. This error may indicate that you are using characters that are not
                 supported within the language settings on your machine.

         −2501   Invalid TDMS file reference.

         2552    This property does not contain data.

     TimedTimed LoopLoop ErrorError CodesCodes

       The Timed Loop structure and VIs and VI Server properties and methods can return the
         following error codes. Refer to the KnowledgeBase for more information about
         correcting errors in LabVIEW.


        Code  Description

              The timed structure failed to unreserve the NI Scan Engine. An error occurred while trying to         −842                 close a transaction with the NI Scan Engine.

              The timed structure failed to retrieve the NI Scan Engine mode. Terminals bound to CE state         −841                    will be undefined

              The timed structure failed to reserve the NI Scan Engine. An error occurred while trying to         −840              open a transaction with the NI Scan Engine.

              The Priority Mapper Table is full. Timed structures must use one of the existing priorities         −832                 already in the Priority Mapper Table.

                Timing Source Fire Count Overflow The timing source has been triggered MAX_U64_VALUE         −831                  times, and cannot fire again. You must clear and recreate the timing source.

         −830  Invalid Trigger ID The trigger ID cannot be less than 0 or greater than 128.

              A time-critical VI contains a timed structure. You cannot place a timed structure in a time-
         −826   critical VI. The priority schemes would conflict and cause the timed structure to operate
                   unreliably.

                   Invalid CPU Specified for timed structure. Invalid CPU specified for timed structure. The CPU
         −825  must fall within the range of 0...N-1, where N is the number of CPUs in the system. Additional
                   valid entries include -2 (automatic assignment) and -1 (no change).

         −823  Cannot load Timed Loop Scheduler Dynamic Library.

         −822  The timed structure feature or type is not supported on the current platform for the


11608   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11608 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11609 ordinal=11609 -->
## Error Codes and Messages

Error Codes and Messages


Code  Description

       following timing source.

     The following timed structures timed out while waiting for the synchronization group to−821      synchronize all timed structures in the group.

−820  The following timed structure has been initialized with illegal parameters.

−819  An illegal mode has been specified for the following given Timed Loop.

     An illegal period, priority, deadline, offset, or start has been specified for the following timed−818       structure.

      Timing Source error or attempted to execute another iteration of a Timed Loop that was−817
       already aborted due to an error of the following timing source.

     Timed structure aborted or attempted to execute another iteration of the following aborted−816     Timed Loop.

−815  Cannot add timing source to the following active timing source hierarchy.

−814  Cannot add timed structure to the active timed structure synchronization group.

−813  The following timing source can be assigned to only one timing source hierarchy at a time.

     The following timed structure can only be assigned to one timed structure synchronization−812
      group at a time.

−811  The given name is already being used by another timing source hierarchy:

−810  The given name is already being used by another timed structure synchronization group:

−809  The given name is already being used by the following timing source.

−808  The given name is already being used by the following timed structure.

     The following timing source hierarchy does not exist possibly because the timing source
−807
       hierarchy has never been created, has been cleared, or an illegal action was attempted.

     The following synchronization group does not exist possibly because the synchronization
−806
      group has never been created, has been cleared, or an illegal action was attempted.

     The following timing source does not exist. This error might occur because the timing source
−805  was never created, has been cleared, or an illegal action was attempted. Use the Create
      Timing Source VI to create a Timed Loop timing source.

     The timed structure does not exist, possibly because the timed structure has not been
−804
       created, the timed structure has been cleared, or an illegal operation was attempted.

       Creating a new timing source hierarchy exceeds the maximum allowed number of
−803
      simultaneously active timing source hierarchies.


                                                    © National Instruments 11609

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11609 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11610 ordinal=11610 -->
## Error Codes and Messages

Error Codes and Messages


        Code  Description

                 Creating another timed structure synchronization group exceeds the maximum allowed         −802              number of simultaneously active synchronization groups.

                 Creating another timing source exceeds the maximum allowed number of simultaneously         −801                  active timing sources.

                 Creating another timed structure exceeds the maximum allowed number of simultaneously         −800                  active timed structures.

         824   You must supply a mode to change the offset of the Timed Loop.

      VISAVISA ErrorError CodesCodes

       The VISA functions and VI Server properties and methods can return the following
         error codes. Refer to the KnowledgeBase for more information about correcting errors
         in LabVIEW.


        Code         Description

         −1073807360 Unknown system error (miscellaneous error).

         −1073807346 The given session or object reference is invalid.

                         Specified type of lock cannot be obtained, or specified operation cannot be         −1073807345                       performed, because the resource is locked.

         −1073807344  Invalid expression specified for search.

                            Insufficient location information or the device or resource is not present in the         −1073807343
                        system.

         −1073807342  Invalid resource reference specified. Parsing error.

         −1073807341  Invalid access mode.

         −1073807339 Timeout expired before operation completed.

                     The VISA driver failed to properly close the session or object reference. This might be
         −1073807338 due to an error freeing internal or OS resources, a failed network connection, or a
                       lower level driver or OS error.

         −1073807333  Specified degree is invalid.

         −1073807332  Specified job identifier is invalid.

         −1073807331 The specified attribute is not defined or supported by the referenced resource.

11610   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11610 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11611 ordinal=11611 -->
## Error Codes and Messages

Error Codes and Messages


Code         Description

            The specified state of the attribute is not valid, or is not supported as defined by the−1073807330              resource.

−1073807329 The specified attribute is read-only.

−1073807328 The specified type of lock is not supported by this resource.

−1073807327 The access key to the specified resource is invalid.

−1073807322  Specified event type is not supported by the resource.

−1073807321  Invalid mechanism specified.

−1073807320 A handler was not installed.

−1073807319 The given handler reference is invalid.

−1073807318  Specified event context is invalid.

            The event queue for the specified type has overflowed. This is usually due to−1073807315
              previous events not having been closed.

−1073807313 You must be enabled for events of the specified type in order to receive them.

−1073807312 User abort occurred during transfer.

−1073807308  Violation of raw write protocol occurred during transfer.

−1073807307  Violation of raw read protocol occurred during transfer.

−1073807306 Device reported an output protocol error during transfer.

−1073807305 Device reported an input protocol error during transfer.

−1073807304 Bus error occurred during transfer.

            Unable to queue the asynchronous operation because there is already an operation
−1073807303
                in progress.

            Unable to start operation because setup is invalid (due to attributes being set to an
−1073807302
               inconsistent state).

            Unable to queue the asynchronous operation (usually due to the I/O completion
−1073807301
             event not being enabled or insufficient space in the session's queue).

−1073807300  Insufficient system resources to perform necessary memory allocation.

−1073807299  Invalid buffer mask specified.

−1073807298 Could not perform operation because of I/O error.

−1073807297 A format specifier in the format string is invalid.

                                                    © National Instruments 11611

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11611 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11612 ordinal=11612 -->
## Error Codes and Messages

Error Codes and Messages


        Code         Description

         −1073807295 A format specifier in the format string is not supported.

         −1073807294 The specified trigger line is currently in use.

         −1073807290 The specified mode is not supported by this VISA implementation.

         −1073807286  Service request has not been received for the session.

         −1073807282  Invalid address space specified.

         −1073807279  Invalid offset specified.

         −1073807278  Invalid access width specified.

         −1073807276  Specified offset is not accessible from this hardware.

         −1073807275 Cannot support source and destination widths that are different.

         −1073807273 The specified session is not currently mapped.

         −1073807271 A previous response is still pending, causing a multiple query error.

         −1073807265 No listeners condition is detected (both NRFD and NDAC are deasserted).

         −1073807264 The interface associated with this session is not currently the controller in charge.

         −1073807263 The interface associated with this session is not the system controller.

         −1073807257 The given session or object reference does not support this operation.

         −1073807256 An interrupt is still pending from a previous call.

         −1073807254 A parity error occurred during transfer.

                    A framing error occurred during transfer. If you receive this error while using a VISA         −1073807253                         read, refer to the KnowledgeBase at ni.com for more information.

                    An overrun error occurred during transfer. A character was not read from the
         −1073807252
                      hardware before the next character arrived.

         −1073807250 The path from trigSrc to trigDest is not currently mapped.

         −1073807248 The specified offset is not properly aligned for the access width of the operation.

         −1073807247 A specified user buffer is not valid or cannot be accessed for the required size.

         −1073807246 The resource is valid, but VISA cannot currently access it.

         −1073807242  Specified width is not supported by this hardware.

         −1073807240 The value of some parameter (which parameter is not known) is invalid.

         −1073807239 The protocol specified is invalid.

11612   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11612 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11613 ordinal=11613 -->
## Error Codes and Messages

Error Codes and Messages


Code         Description

−1073807237  Invalid size of window specified.

−1073807232 The specified session currently contains a mapped window.

−1073807231 The given operation is not implemented.

−1073807229  Invalid length specified.

−1073807215  Invalid mode specified.

−1073807204 The current session did not have a lock on the resource.

             VISA or a code library required by VISA could not be located or loaded. This is usually−1073807202            due to a required driver not being installed on the system.

            The interface cannot generate an interrupt on the requested level or with the−1073807201             requested statusID value.

−1073807200 The value specified by the line parameter is invalid.

           An error occurred while trying to open the specified file. Possible reasons include an−1073807199               invalid path or lack of access rights.

−1073807198 An error occurred while performing I/O on the specified file.

           One of the specified lines, trigSrc or trigDest, is not supported by this VISA−1073807197
             implementation, or the combination of lines is not a valid mapping.

−1073807196 The specified mechanism is not supported for the given event type.

−1073807195 The interface type is valid, but the specified interface number is not configured.

−1073807194 The connection for the given session has been lost.

            The remote machine does not exist or is not accepting any connections. If the NI-
−1073807193 VISA server is installed and running on the remote machine, it might have an
             incompatible version or might be listening on a different port.

             Access to the resource or remote machine is denied. This is due to lack of sufficient
−1073807192
               privileges for the current user or machine.

0            Operation completed successfully.

1073676290   Specified event is already enabled for at least one of the specified mechanisms.

1073676291   Specified event is already disabled for at least one of the specified mechanisms.

1073676292   Operation completed successfully, but queue was already empty.

1073676293  The specified termination character was read.


                                                    © National Instruments 11613

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11613 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11614 ordinal=11614 -->
## Error Codes and Messages

Error Codes and Messages


        Code         Description

                     The number of bytes transferred is equal to the requested input count. More data         1073676294                      might be available.

                       VISA received more event information of the specified type than the configured         1073676300                     queue size could hold.

                     The specified configuration either does not exist or could not be loaded. VISA-         1073676407                          specified defaults will be used.

                        Session opened successfully, but the device at the specified address is not         1073676413                        responding.

         1073676414  The path from trigSrc to trigDest is already mapped.

                       Wait terminated successfully on receipt of an event notification. There is at least one
         1073676416  more event occurrence of the type specified by inEventType available for this
                          session.

         1073676418  The specified object reference is uninitialized.

                       Although the specified state of the attribute is valid, it is not supported by this         1073676420                        resource implementation.

         1073676421  The status code passed to the operation could not be interpreted.

         1073676424  The specified I/O buffer is not supported.

                       Event handled successfully. Do not invoke any other handlers on this session for this         1073676440                         event.

         1073676441   Operation completed successfully, and this session has nested shared locks.

         1073676442   Operation completed successfully, and this session has nested exclusive locks.

                       Operation completed successfully, but the operation was actually synchronous
         1073676443
                          rather than asynchronous.

                     The operation succeeded, but a lower level driver did not implement the extended
         1073676457
                           functionality.

     WaveformWaveform ErrorError CodesCodes

       The Waveform VIs and functions and VI Server properties and methods can return the
         following error codes. Refer to the KnowledgeBase for more information about
         correcting errors in LabVIEW.


11614   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11614 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11615 ordinal=11615 -->
## Error Codes and Messages

Error Codes and Messages


Code  Description

      Waveform data type file datalog type conflict. Refer to the KnowledgeBase for more−1821       information about migrating waveform data from LabVIEW 6.x to LabVIEW 7.x.

      The t0 does not align with the end of the previous signal. Appending two waveforms may
−1820  require that the t0 of the second waveform match the value of the last point in the first
      waveform. This error is returned when this is required, but the requirement is not met.

−1817  Specified start position or signal index is out of range.

−1816  Full Scale Range cannot be less than or equal to zero.

−1815 An invalid character was present in the spreadsheet string. Use only 0, 1, L, H, X, Z, V, or T.

−1813 Too many signals to convert into the specified data type.

−1812  Specified start position or duration is out of range.

−1811 Both waveforms must contain the same number of signals.

−1810 The number of samples to compare exceeds the number of samples after the start sample.

−1809  Highest resolution supported for conversion is 52.

−1808  Values other than 0, 1, L, H are present in the digital data.

−1807 Appending data with mismatched numbers of digital samples or signals.

−1806  Signal value input is outside the range of the digital data.

−1805  Start index out of range

−1804  Start index, value, or tolerance is NaN

−1803 Waveform x-axis value requested is out of range.

−1802 Waveforms have different dt values.

       Duration input is not an integer multiple of dt. Value was coerced to nearest integer multiple
−1801
        of dt.

        Start time input is not an integer multiple of dt. Value was coerced to nearest integer
−1800
       multiple of dt.

        Start time input is not an integer multiple of dt. Value was coerced to nearest integer
1800
       multiple of dt.

       Duration input is not an integer multiple of dt. Value was coerced to nearest integer multiple
1801
        of dt.

1802  Waveforms have different dt values.


                                                    © National Instruments 11615

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11615 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11616 ordinal=11616 -->
## Error Codes and Messages

Error Codes and Messages


        Code  Description

         1803  Waveform x-axis value requested is out of range.

         1804   Start index, value, or tolerance is NaN.

         1805   Start index is out of range.

         1806   Signal value input is outside the range of the digital data.

         1807  Appending data with mismatched numbers of digital samples or signals.

         1808   Values other than 0, 1, L, H are present in the digital data.

         1809   Highest resolution supported for conversion is 52.

         1814   Values other than 0, 1, L, and H are present in the digital data and were coerced to 0.

     WindowsWindows ConnectivityConnectivity ErrorError CodesCodes

       The ActiveX functions, the .NET Constructor Node, and VI Server properties and
       methods can return the following error codes. Refer to the KnowledgeBase for more
        information about correcting errors in LabVIEW.


        Code  Description

         92    The ActiveX event data was not available on the queue.

         93    ActiveX event information was not available.

         94    The occurrence associated with the ActiveX event was not found.

         95    The ActiveX event queue could not be created.

         96    ActiveX event information was not available in the type library.

              A .NET exception occurred in an external assembly. For information about correcting this
         1172  error, copy the following exception (in bold), and search the Microsoft Developer Network
              (MSDN) Web site or the Web for a possible explanation.

         1173  LabVIEW data type does not match the .NET type.

         1189  You cannot register the same event on an object multiple times.

         1195  You must install the .NET Framework 4.0 for this operation.

               Cannot convert the specified LabVIEW type to .NET object. Valid types include all numeric
         1199  data types except extended and complex precision, string, Boolean, path, time stamp, .NET
                refnum, and arrays of these data types.

11616   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11616 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11617 ordinal=11617 -->
## Error Codes and Messages

Error Codes and Messages


 Code  Description

 1325  LabVIEW cannot find the specified event.

 1375  The .NET Framework 4.0 is not installed on this machine.

 1386  The specified .NET class is not available in LabVIEW.

 1387  The specified .NET assembly is not available in LabVIEW.

       Property or invoke node is corrupt. To correct this error, delete the node and re-add it to the 1555       block diagram.

      The loaded .NET assembly was not found in its original directory. The loaded .NET assembly
      was not found in its original directory. You might have moved or deleted the assembly while 1589
      LabVIEW was still using it. To fix this error, move the .NET assembly back to its original
        location.

WebWeb ServicesServices ErrorError CodesCodes

The Web Services VIs and functions can return the following error codes. Refer to the
KnowledgeBase for more information about correcting errors in LabVIEW.


 Code    Description

         LabVIEW Web Services: An unexpected communication error has occurred with the
         remote target. This error typically occurs when the LabVIEW application on the remote
 −356060  target has crashed or restarted unexpectedly. Subsequent calls to this Web service will
         attempt to repair the communication error. However, the application may no longer be in
         a known good state.

         LabVIEW Web Services: The specified property or method cannot be used over a network.
 −356010
          Execute this property or method only on the local host.

 −67750  LabVIEW Web Services: Memory Allocation failed.

         LabVIEW Web Services: An error occurred when extracting the deployed Web service. The
 −67508    file path might be too long. Reduce the length of VI filenames, directory names, or the
       Web service itself.

 −67506  LabVIEW Web Services: An operating system exception encountered.

         LabVIEW Web Services: Message received is invalid for the current state of the File
 −67505
           Receiver.

 −67504  LabVIEW Web Services: Error creating a temporary file.


                                                    © National Instruments 11617

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11617 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11618 ordinal=11618 -->
## Error Codes and Messages

Error Codes and Messages


        Code    Description

                 LabVIEW Web Services: Invalid message received. An unknown type of message was         −67503                     received.

         −67502  LabVIEW Web Services: Copying data to or from a LabVIEW terminal failed.

                 LabVIEW Web Services: Parse failed. Error encountered while parsing a default string or a         −67501
                    routing template.

         −67500  LabVIEW Web Services: Memory allocation failed.

                 LabVIEW Web Services: Web service deployment failed. The Web service installer received         −67404                 an error when attempting to deploy. The Web service has not been installed.

                 LabVIEW Web Services: Unexpected response from the server. The Web service installer
         −67403   received an unexpected response from the server. The Web service has not been
                       installed.

                 LabVIEW Web Services: Authentication failed. Either the Web service installer did not
         −67402   receive the correct credentials or authentication was cancelled. The Web service has not
                 been installed.

                 LabVIEW Web Services: Unable to detect Application Web Server port. The Web service
         −67401   installer was unable to detect the port of the Application Web Server. The Web service has
                   not been installed.

                 LabVIEW Web Services: Failed to start the Application Web Server. The Web service
         −67400   installer was unable to start the correct version of the Application Web Server. The Web
                     service has not been installed.

         −67306  LabVIEW Web Services: Invalid session ID specified.

                 LabVIEW Web Services: Function not available for service VIs configured for headerless
         −67305  mode. The function attempted by the Web service method is not available for Web
                     service methods configured for headerless mode.

                 LabVIEW Web Services: Function not available for service VIs configured for output
         −67304   terminal mode. The function attempted by the Web service method is not available for
                     services configured for the output terminal mode.

                 LabVIEW Web Services: Variable not defined for current session. The variable being
         −67303
                   accessed has not been defined for the session associated with the current request.

         −67302  LabVIEW Web Services: Input Request ID has no associated session.

                 LabVIEW Web Services: Invalid Request ID. The value wired into the httpRequestID
         −67301
                    terminal of the VI is invalid.

         −67300  LabVIEW Web Services: Internal error in LabVIEW Web services runtime. This could be a


11618   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11618 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11619 ordinal=11619 -->
## Error Codes and Messages

Error Codes and Messages


Code    Description

       memory error or a file error.

        LabVIEW Web Services: A non-printable ASCII character was encountered. Only printable−67164          ASCII characters are allowed in terminal labels, service names, and VI names.

−67163  LabVIEW Web Services: Error encountered while writing data to the socket.

−67162  LabVIEW Web Services: LabVIEW string conversion error.

−67161  LabVIEW Web Services: LabVIEW C Interface memory management error.

−67160  LabVIEW Web Services: LabVIEW C Interface table not found.

−67159  LabVIEW Web Services: LabVIEW application not found.

−67158  LabVIEW Web Services: Error encountered while writing session variable.

−67157  LabVIEW Web Services: Error encountered while flushing data into the socket.

−67156  LabVIEW Web Services: Unknown map error.

−67155  LabVIEW Web Services: Request variables associated with the current request not found.

−67154  LabVIEW Web Services: Invalid LabVIEW array handle encountered.

−67153  LabVIEW Web Services: Session variables defined for the current session not found.

−67152  LabVIEW Web Services: The current request not found.

−67151  LabVIEW Web Services: Web service active request map not found.

−67150  LabVIEW Web Services: Web Service session manager not found.

        LabVIEW Web Services: The Web service is currently unavailable because it is still loading,
         has crashed, or is disabled. Try accessing the service again later or restarting the Web
−67043          server. This error corresponds to HTTP status code 503 and is usually a temporary
          condition.

−67041  LabVIEW Web Services: Invalid value for input parameter.

−67040  LabVIEW Web Services: An invalid HTTP method was encountered.

        LabVIEW Web Services: Invalid character encountered in terminal name. An invalid
−67039   character, such as an open or close bracket, is present in a terminal name of an HTTP
        method VI.

        LabVIEW Web Services: Duplicate terminal name encountered. Multiple terminals with
−67038
         the same name exist on the connector pane of an HTTP method VI.

−67037  LabVIEW Web Services: An invalid content header was encountered.


                                                    © National Instruments 11619

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11619 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11620 ordinal=11620 -->
## Error Codes and Messages

Error Codes and Messages


        Code    Description

                 LabVIEW Web Services: ESP Error. An error was encountered while rendering an ESP
         −67035   script or setting an ESP variable. This may occur because scripting was not enabled on
                   the server or due to an error in the ESP script.

         −67034  LabVIEW Web Services: Object not found in the object map.

         −67033  LabVIEW Web Services: A Web service already exists with the input name.

         −67032  LabVIEW Web Services: This type of Web service is not supported.

         −67030  LabVIEW Web Services: Unable to load shared library.

                 LabVIEW Web Services: SetSysAdminMgr function not found in shared library published         −67029
                   as a Web service.

                 LabVIEW Web Services: Finalize method not found in Web services shared library. A         −67028                   shared library published as a Web service did not define Finalize method.

                 LabVIEW Web Services: Resume method not found in Web services shared library. A         −67027                   shared library published as a Web service did not define Resume method.

                 LabVIEW Web Services: Pause method not found in Web services shared library. A shared         −67026                       library published as a Web service did not define Pause method.

                 LabVIEW Web Services: Init not found in Web services shared library. A shared library         −67025                   published as a Web service did not define Init method.

                 LabVIEW Web Services: Run not found in Web services shared library. A shared library         −67024                   published as a Web service did not define Run method.

         −67023  LabVIEW Web Services: An operating system exception encountered.

                 LabVIEW Web Services: The current service command is not defined for the variable type
         −67022                   encountered.

         −67021  LabVIEW Web Services: Error while creating directory.

         −67020  LabVIEW Web Services: Invalid service directory name encountered.

         −67019  LabVIEW Web Services: VI checksum mismatch.

         −67018  LabVIEW Web Services: Shared Variable engine failure.

         −67017  LabVIEW Web Services: No INI file found in service directory.

         −67016  LabVIEW Web Services: File I/O error.

         −67015  LabVIEW Web Services: System is currently in an invalid state for the current message.

         −67014  LabVIEW Web Services: Invalid message received.


11620   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11620 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11621 ordinal=11621 -->
## Error Codes and Messages

Error Codes and Messages


 Code    Description

 −67013  LabVIEW Web Services: More than one INI file encountered in a service directory.

 −67012  LabVIEW Web Services: Error encountered while parsing INI file.

 −67011  LabVIEW Web Services: Copying data to the VI terminal(s) failed.

 −67010  LabVIEW Web Services: An unsupported LabVIEW data type encountered.

 −67009  LabVIEW Web Services: Call to run a VI failed.

 −67008  LabVIEW Web Services: The VI has not been cached.

 −67007  LabVIEW Web Services: The service has already been registered.

 −67006  LabVIEW Web Services: The VI has already been cached.

 −67005  LabVIEW Web Services: Unknown VI name. Unable to locate the named VI.

 −67004  LabVIEW Web Services: Memory allocation failure.

         LabVIEW Web Services: Call to create a VI reference failed. The target might not support
 −67003  SSE2 optimization. Disable SSE2 optimization on the Advanced page of the Web Service
          Properties dialog box before proceeding.

 −67002  LabVIEW Web Services: Call to create a reference to the LabVIEW application failed.

 −67001  LabVIEW Web Services: The Web service is undefined.

 −67000  LabVIEW Web Services: A LabVIEW internal error occurred.

         LabVIEW Web Services: Cannot modify http header or response after written to socket.
 67200   HTTP headers and/or response have already been written to the client for the current
           request. They cannot be modified.

 67201   LabVIEW Web Services: Required input string is empty.

         LabVIEW Web Services: No POST data available for input Request ID. The current request
 67202
         does not contain postdata.

WindowsWindows RegistryRegistry AccessAccess ErrorError CodesCodes

The Windows Registry Access VIs and VI Server properties and methods can return the
following error codes. Refer to the KnowledgeBase for more information about
correcting errors in LabVIEW.


                                                    © National Instruments 11621

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11621 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11622 ordinal=11622 -->
## Error Codes and Messages

Error Codes and Messages


        Code  Description

         −620  Networked machine was not found.

         −619  Remote registry services not available or remote administration not enabled.

         −618  Cannot create a stable subkey under a volatile parent key.

         −617  Cannot create a symbolic link in a registry key that already has subkeys or values.

         −616  System could not allocate the required space in a registry log.

         −615   Illegal operation attempted on a registry key that has been marked for deletion.

              The system has attempted to load or restore a file into the registry, but the specified file is         −614                not in a registry file format.

              An I/O operation initiated by the registry failed irrecoverably. The registry could not read in,         −613
                 or write out, or flush, one of the files that contain the system's image of the registry.

              The registry is corrupted. The structure of one of the files that contains registry data is
         −612  corrupted, the system's image of the file in memory is corrupted, or the file could not be
                recovered because the alternate copy or log was absent or corrupted.

             One of the files in the registry database had to be recovered by use of a log or alternate copy.         −611              The recovery was successful.

         −610  The configuration registry key could not be written.

         −609  The configuration registry key could not be read.

         −608  The configuration registry key could not be opened.

         −607  The configuration registry key is invalid.

         −606  The configuration registry database is corrupt.

         −605  Attempted to read beyond last key or value.

              Remote registry access denied. If you receive this error while using the Delete Registry Key VI,
         −604
                   refer to the KnowledgeBase at ni.com for more information.

         −603  Specified key or value does not exist.

         −602  Invalid registry refnum.

         −601  Incorrect data type specified.

         −600  Undetermined Windows registry error.


11622   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11622 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11623 ordinal=11623 -->
## Error Codes and Messages

Error Codes and Messages

XMLXML ParserParser ErrorError CodesCodes

The XML Parser VIs and XML Parser properties and methods can return the following
error codes. Refer to the KnowledgeBase for more information about correcting errors
in LabVIEW.


 Code  Description

       The XPath expression must be a location path. Refer to the W3C XPath Website at −2769        http://www.w3.org/TR/xpath for more information about XPathsyntax and location paths.

       The XPath expression does not conform to XPath syntax. Refer to the W3CXPath Web site at −2768        http://www.w3.org/TR/xpath for more informationabout XPath syntax.

      An error occurred while performing an XPath query. Refer to the W3C XPathWeb site at −2767        http://www.w3.org/TR/xpath for more information aboutXPath syntax.

 −2766 Attempted to perform an XPath query with an invalid node refnum.

 −2765  File already exists at the specified path.

 −2764 Attempted to call Create Document with invalid document type.

 −2763 Attempted to set the Loading External DTD flag on invalid document.

 −2762 Attempted to get the Loading External DTD flag on invalid document.

 −2761 Attempted to set Validate Schema Full Checking on invalid document.

 −2760 Attempted to get Validate Schema Full Checking on invalid document.

 −2759 Attempted to get System ID on invalid notation.

 −2758 Attempted to get Public ID on invalid notation.

 −2757 Attempted to call Replace Data on invalid character data.

 −2756 Attempted to call Delete Data on invalid character data.

 −2755 Attempted to call Insert Data on invalid character data.

 −2754 Attempted to call Append Data on invalid character data.

 −2753 Attempted to get Substring Data on invalid character data.

 −2752 Attempted to get Length on invalid character data.

 −2751 Attempted to set Data on invalid character data.

 −2750 Attempted to get Data on invalid character data.


                                                    © National Instruments 11623

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11623 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11624 ordinal=11624 -->
## Error Codes and Messages

Error Codes and Messages


        Code  Description

         −2749 Attempted to call Has Attribute Namespace on invalid element.

         −2748 Attempted to call Has Attribute on invalid element.

         −2747 Attempted to call Get Element By Tag Name Namespace on invalid element.

         −2746 Attempted to call Set Attribute Node Namespace with invalid parameter on element.

         −2745 Attempted to call Set Attribute Node Namespace on invalid element.

         −2744 Attempted to call Get Attribute Node Namespace on invalid element.

         −2743 Attempted to call Remove Attribute Namespace on invalid element.

         −2742 Attempted to call Set Attribute Namespace on invalid element.

         −2741 Attempted to call Get Attribute Namespace on invalid element.

         −2740 Attempted to call Remove Attribute Node with invalid parameter on element.

         −2739 Attempted to call Remove Attribute Node on invalid element.

         −2738 Attempted to call Remove Attribute on invalid element.

         −2737 Attempted to call Set Attribute Node with invalid parameter on element.

         −2736 Attempted to call Set Attribute Node on invalid element.

         −2735 Attempted to call Set Attribute on invalid element.

         −2734 Attempted to call Get Attribute Node on invalid element.

         −2733 Attempted to get Attribute on invalid element.

         −2732 Attempted to get Tag Name on invalid element.

         −2731 Attempted to call Get Element By Tag Name on invalid element.

         −2730 Attempted to get Item on invalid node list.

         −2729 Attempted to get Length on invalid node list.

         −2728 Attempted to get Length on invalid named node map.

         −2727 Attempted to get Item on invalid named node map.

         −2726 Attempted to set Named Item Namespace with invalid parameter on named node map.

         −2725 Attempted to set Named Item Namespace on invalid named node map.

         −2724 Attempted to get Named Item Namespace on invalid named node map.

         −2723 Attempted to set Named Item with invalid parameter on named node map.


11624   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11624 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11625 ordinal=11625 -->
## Error Codes and Messages

Error Codes and Messages


Code  Description

−2722 Attempted to set Named Item on invalid named node map.

−2721 Attempted to call Remove Named Item Namespace on invalid named node map.

−2720 Attempted to call Get Elements By ID on invalid document.

−2719 Attempted to call Get Elements By Tag Name Namespace on invalid document.

−2718 Attempted to call Create Attribute Namespace on invalid document.

−2717 Attempted to call Create Attribute Namespace with empty name string.

−2716 Attempted to call Create Element Namespace on invalid document.

−2715 Attempted to call Create Element Namespace with empty name string.

−2714 Attempted to set Do Schema on invalid document.

−2713 Attempted to get Do Schema on invalid document.

−2712  Error occurred while saving file because path is invalid.

−2711  Error occurred while loading file because path is invalid.

−2710  Error occurred while loading file.

−2709 Attempted to get Internal Subset on invalid DTD.

−2708 Attempted to get System ID on invalid DTD.

−2707 Attempted to get Public ID on invalid DTD.

−2706 Attempted to call Create Document on invalid implementation.

−2705 Attempted to call Create Document Type on invalid implementation.

−2704 Attempted to get Owner Element on invalid attribute.

−2703 Attempted to set Value on invalid attribute.

−2702 Attempted to get Value on invalid attribute.

−2701 Attempted to get Name on invalid attribute.

−2700 Attempted to call Is Supported on invalid node refnum.

−2699 Attempted to set Prefix on invalid node refnum.

−2698  Access to the XML parser must go through an initialized document.

−2697 Attempted to get Attributes with invalid parameter New Node.

−2696 Attempted to get Attributes on invalid named node map refnum.


                                                    © National Instruments 11625

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11625 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11626 ordinal=11626 -->
## Error Codes and Messages

Error Codes and Messages


        Code  Description

         −2695 Attempted to call Remove Named Item on invalid named node map.

         −2694 Attempted to get Named Item on invalid named node map.

         −2693 Attempted to get array on invalid named node map.

         −2692 Attempted to set Preserve Whitespace on invalid document.

         −2691 Attempted to get Preserve Whitespace on invalid document.

         −2690 Attempted to call Implementation on invalid document.

         −2689 Attempted to set Validate On Load on invalid document.

         −2688 Attempted to get Validate On Load on invalid document.

         −2687 Attempted to call Get Elements By Tag Name on invalid document.

         −2686 Attempted to get DocType on invalid document.

         −2685 Attempted to call Create Text Node on invalid document.

         −2684 Attempted to call Create Document Fragment on invalid document.

         −2683 Attempted to call Create Processing Instruction on invalid document.

         −2682 Attempted to call Create Processing Instruction with empty target string.

         −2681 Attempted to call Create Attribute on invalid document.

         −2680 Attempted to call Create Attribute with empty name string.

         −2679 Attempted to call Create CDATA Section on invalid document.

         −2678 Attempted to call Create Element on invalid document.

         −2677 Attempted to call Create Element with empty name string.

         −2676 Attempted to call Create Comment on invalid document.

         −2675 Attempted to get Document Element on invalid document.

         −2674 Attempted to call Save File on invalid document.

         −2673 Attempted to call Load File on invalid document.

         −2672 Attempted to get Notations on invalid DTD.

         −2671 Attempted to get Entities on invalid DTD.

         −2670 Attempted to get Name on invalid DTD.

         −2669 Attempted to call Has Feature on invalid implementation.


11626   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11626 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11627 ordinal=11627 -->
## Error Codes and Messages

Error Codes and Messages


Code  Description

−2668 Attempted to get Notation Name on invalid entity.

−2667 Attempted to get System ID on invalid entity.

−2666 Attempted to get Public ID on invalid entity.

−2665 Attempted to set Data on invalid processing instruction.

−2664 Attempted to get Data on invalid processing instruction.

−2663 Attempted to get Target on invalid processing instruction.

−2662 Attempted to call Split Text on invalid text node.

−2661 Attempted to get Specified on invalid attribute.

−2660 Attempted to call Replace Child with invalid node refnum parameter Old Child.

−2659 Attempted to call Replace Child with invalid node refnum parameter New Child.

−2658 Attempted to call Replace Child on invalid node refnum.

−2657 Attempted to call Insert Before with invalid node refnum parameter New Child.

−2656 Attempted to call Insert Before on invalid node refnum.

−2655 Attempted to call Normalize on invalid node refnum.

−2654 Cannot call Normalize on node that is not of element type.

−2653 Attempted to call Get XML on invalid node refnum.

−2652 Attempted to call Has Child Nodes on invalid node refnum.

−2651 Attempted to call Clone Node on invalid node refnum.

−2648 Attempted to call Append Child with invalid refnum parameter New Child.

−2647 Attempted to call Append Child on invalid refnum.

−2646 Attempted to call Remove Child with invalid refnum parameter Old Child.

−2645 Attempted to call Remove Child on invalid node refnum.

−2644 Attempted to set Node Value on invalid node refnum.

−2643 Attempted to get Attributes on invalid node refnum.

−2642 Attempted to get Namespace Name on invalid node refnum.

−2641 Attempted to get Prefix Name on invalid node refnum.

−2640 Attempted to get Local Name on invalid node refnum.


                                                    © National Instruments 11627

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11627 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11628 ordinal=11628 -->
## Error Codes and Messages

Error Codes and Messages


        Code  Description

         −2639 Attempted to get Owner Document on invalid node refnum.

         −2638 Attempted to get Previous Sibling on invalid node refnum.

         −2637 Attempted to get Next Sibling on invalid node refnum.

         −2636 Attempted to get Parent Node on invalid node refnum.

         −2635 Attempted to get Last Child on invalid node refnum.

         −2634 Attempted to get First Child on invalid node refnum.

         −2633 Attempted to get Child Nodes on invalid node refnum.

         −2632 Attempted to get Node Value on invalid node refnum.

         −2631 Attempted to get Node Name on invalid node refnum.

         −2629 An unknown error occurred.

         −2628 An error occurred while parsing the document.

         −2627 An unknown user error occurred.

         −2626  Invalid refnum.

         −2625 An error occurred while saving the document.

         −2616 A system error occurred.

                 Operation not performed. Validation error. You used a method that would invalidate the         −2615                node.

         −2614 A parameter or operation was not supported by the underlying object.

                Attempted to create or change an object in a way that was incorrect with regard to
         −2613                namespaces.

         −2612 Attempted to modify the type of an underlying object.

         −2611  Specified an invalid or illegal string.

         −2610 Attempted to use an object that is no longer usable.

         −2609 Attempted to add an attribute already in use.

         −2608 Requested a type of object or operation that implementation does not support.

         −2607 Attempted to reference a node in a context where it does not exist.

         −2606 Attempted to modify an object where modifications are not allowed.

         −2605  Specified data for a node that does not support data.

11628   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11628 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11629 ordinal=11629 -->
## Error Codes and Messages

Error Codes and Messages


 Code  Description

 −2604  Specified an invalid or illegal character, possibly in a name.

       Used a node in a document other than the one that created the node, and which does not −2603       support the node.

 −2602  Inserted node in the wrong location.

 −2601  Specified a range of text that does not fit into a string.

 −2600 Index or size is negative or is greater than the allowed value.

WindowsWindows EmbeddedEmbedded StandardStandard ErrorError CodesCodes

The >Write Filters VIs can return the following error codes. Refer to the KnowledgeBase
for more information about correcting errors in LabVIEW.


 Code    Description

         Unable to run the built application on the target. A user must log into a Windows session −311071        on the target.

 −311070 Unable to run the built application on the target. The target returns an unexpected error.

 −311052 Cannot commit all files.

 −311051 FBWF returned an unknown error.

 −311050 Cannot find the FBWF cache entry.

 −311049 The system does not have enough memory to list all the FBWF cache entries.

 −311048 The file path to remove does not exist in the exclusion list for the next session.

 −311047 The file to restore does not exist in the FBWF cache.

 −311046 Cannot restore a read-only file.

         Cannot restore the file, because the file is in the exclusion path, renamed, or does not
 −311045
            exist on the physical media.

         Cannot commit changes, because the file is write-protected. For example, the file is in the
 −311044
         CD-ROM.

         Cannot commit changes, because the file is in the exclusion path, renamed, or does not
 −311043
            exist on the physical media.

 −311042 The file is not valid or not in the FBWF cache.

                                                    © National Instruments 11629

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11629 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11630 ordinal=11630 -->
## Error Codes and Messages

Error Codes and Messages


        Code    Description

         −311041 The volume name is not valid or the volume is not protected by FBWF.

               FBWF is currently disabled, not enabled for the next session, or the volume is not         −311040                    protected by FBWF.

         −311026  Failed to set a checkpoint level on the EWF protected volume.

         −311025  Failed to free the memory that the EWF uses.

         −311024  Failed to get the configuration information of the EWF protected volume.

         −311023  Failed to get the configuration information of the EWF storage volume.

         −311022  Failed to open the EWF overlay storage volume.

         −311021  Failed to restore an EWF protected volume.

         −311020  Failed to create a new checkpoint on the EWF protected volume.

         −311019  Failed to disable HORM on the EWF protected volume.

         −311018  Failed to enable HORM on the EWF protected volume.

         −311017  Failed to get the list of EWF protected volumes.

         −311016  Failed to clear the EWF command on the EWF protected volume.

         −311015  Failed to live commit changes and disable EWF on the EWF protected volume.

         −311014  Failed to commit changes to the EWF protected volume.

         −311013  Failed to disable EWF on the volume.

         −311012  Failed to enable EWF on the volume.

         −311011  Failed to close the EWF protected volume handle or the EWF storage volume handle.

         −311010  Failed to open the EWF protected volume.

         −311001  Failed to get the Write Filters VIs library function.

         −311000  Failed to load the Write Filters VIs library.


11630   ni.com                     © 2024 National Instruments Corporation.

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:11630 -->

