# JAVA OPENAPI: UPDMProfile.ServiceDescriptionStereotype (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/updm/utils/UPDMProfile.ServiceDescriptionStereotype.html
- source_path: `com/nomagic/updm/utils/UPDMProfile.ServiceDescriptionStereotype.html`
- source_sha256: `ad39ba4a82bd15b2b69e0ebd13bfa387b8fae55044a63aaf37c673a3ab730f99`
- captured_utc: `2026-07-14T16:46:47.317429+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.updm.utils](package-summary.html)

## Class UPDMProfile.ServiceDescriptionStereotype

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[com.nomagic.profiles.ProfileImplementation.StereotypeWrapper](../../profiles/ProfileImplementation.StereotypeWrapper.html)
com.nomagic.updm.utils.UPDMProfile.ServiceDescriptionStereotype

Enclosing class:
`[UPDMProfile](UPDMProfile.html)`

public static classUPDMProfile.ServiceDescriptionStereotype
extends [ProfileImplementation.StereotypeWrapper](../../profiles/ProfileImplementation.StereotypeWrapper.html)

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[ACTUALPROPERTYSET](#ACTUALPROPERTYSET)`
The actual measurements to which the element must conform.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[APPROVALAUTHORITY](#APPROVALAUTHORITY)`
References the actual organizational resource that has the authority to approve the architectural description.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[ARCHITECT](#ARCHITECT)`
The name of the architect responsible for the ArchitecturalDescription.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[ARCHITECTUREFRAMEWORK](#ARCHITECTUREFRAMEWORK)`
The architectureFramework tag identifies the subset of aliases to use within the context of the ArchitecturalDescription (i.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[ASSUMPTIONANDCONSTRAINT](#ASSUMPTIONANDCONSTRAINT)`
Any assumptions, constraints, and limitations contained in the ArchitecturalDescription, including those affecting deployment, communications performance, information assurance environments, etc.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[CONFORMSTO](#CONFORMSTO)`
Standard that this UPDM element is conforming to.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[CREATINGORGANIZATION](#CREATINGORGANIZATION)`
Describes the ActualOrganizationalResource creating the ArchitecturalDescription.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[DATECOMPLETED](#DATECOMPLETED)`
Date that the Architectural Description was completed.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[ENDBOUNDARYTYPE](#ENDBOUNDARYTYPE)`
End time of boundary.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[PROPERTYSET](#PROPERTYSET)`
Types of measurements corresponding to the actual measurements.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[PURPOSE](#PURPOSE)`
Explains the need for the Architecture, what it will demonstrate, the types of analyses that will be applied to it, who is expected to perform the analyses, what decisions are expected to be made on the basis of each form of analysis, who is expected to make those decisions, and what actions are expected to result.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[RECOMMENDATIONS](#RECOMMENDATIONS)`
States the recommendations that have been developed based on the architecture effort.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[STARTBOUNDARYTYPE](#STARTBOUNDARYTYPE)`
Start time of a boundary.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[STEREOTYPE_NAME](#STEREOTYPE_NAME)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[SUMMARYOFFINDINGS](#SUMMARYOFFINDINGS)`
Summarizes the findings that have been developed so far.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TOBE](#TOBE)`
Indicates whether the ArchitecturalDescription is existing or future.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TOOLSUSED](#TOOLSUSED)`
Identifies any tools used to develop the ArchitecturalDescription as well as file names and formats if appropriate.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[URI](#URI)`
Unique identifier for the element.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[VIEWPOINT](#VIEWPOINT)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[VIEWS](#VIEWS)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Modifier
Constructor
Description
`protected`
`[ServiceDescriptionStereotype](#%3Cinit%3E(com.nomagic.updm.utils.UPDMProfile))([UPDMProfile](UPDMProfile.html) profile)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[addActualPropertySet](#addActualPropertySet(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)`

`void`
`[addApprovalAuthority](#addApprovalAuthority(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)`

`void`
`[addArchitect](#addArchitect(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)`

`void`
`[addAssumptionAndConstraint](#addAssumptionAndConstraint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)`

`void`
`[addConformsTo](#addConformsTo(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)`

`void`
`[addCreatingOrganization](#addCreatingOrganization(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)`

`void`
`[addPropertySet](#addPropertySet(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)`

`void`
`[addPurpose](#addPurpose(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)`

`void`
`[addRecommendations](#addRecommendations(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)`

`void`
`[addSummaryOfFindings](#addSummaryOfFindings(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)`

`void`
`[addToolsUsed](#addToolsUsed(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)`

`void`
`[addViewpoint](#addViewpoint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)`

`void`
`[addViews](#addViews(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)`

`void`
`[clearActualPropertySet](#clearActualPropertySet(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearApprovalAuthority](#clearApprovalAuthority(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearArchitect](#clearArchitect(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearArchitectureFramework](#clearArchitectureFramework(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearAssumptionAndConstraint](#clearAssumptionAndConstraint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearConformsTo](#clearConformsTo(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearCreatingOrganization](#clearCreatingOrganization(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearDateCompleted](#clearDateCompleted(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearEndBoundaryType](#clearEndBoundaryType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearPropertySet](#clearPropertySet(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearPurpose](#clearPurpose(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearRecommendations](#clearRecommendations(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearStartBoundaryType](#clearStartBoundaryType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearSummaryOfFindings](#clearSummaryOfFindings(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearToBe](#clearToBe(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearToolsUsed](#clearToolsUsed(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearURI](#clearURI(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearViewpoint](#clearViewpoint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearViews](#clearViews(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getActualPropertySet](#getActualPropertySet(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getActualPropertySetProperty](#getActualPropertySetProperty())()`

`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[getApprovalAuthority](#getApprovalAuthority(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getApprovalAuthorityProperty](#getApprovalAuthorityProperty())()`

`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[getArchitect](#getArchitect(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getArchitectProperty](#getArchitectProperty())()`

`[UPDMProfile.ArchitectureFrameworkKindEnum](UPDMProfile.ArchitectureFrameworkKindEnum.html)`
`[getArchitectureFramework](#getArchitectureFramework(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getArchitectureFrameworkProperty](#getArchitectureFrameworkProperty())()`

`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[getAssumptionAndConstraint](#getAssumptionAndConstraint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getAssumptionAndConstraintProperty](#getAssumptionAndConstraintProperty())()`

`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getConformsTo](#getConformsTo(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getConformsToProperty](#getConformsToProperty())()`

`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[getCreatingOrganization](#getCreatingOrganization(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getCreatingOrganizationProperty](#getCreatingOrganizationProperty())()`

`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getDateCompleted](#getDateCompleted(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getDateCompletedProperty](#getDateCompletedProperty())()`

`[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[getEndBoundaryType](#getEndBoundaryType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getEndBoundaryTypeProperty](#getEndBoundaryTypeProperty())()`

`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getPropertySet](#getPropertySet(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getPropertySetProperty](#getPropertySetProperty())()`

`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[getPurpose](#getPurpose(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getPurposeProperty](#getPurposeProperty())()`

`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[getRecommendations](#getRecommendations(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getRecommendationsProperty](#getRecommendationsProperty())()`

`[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[getStartBoundaryType](#getStartBoundaryType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getStartBoundaryTypeProperty](#getStartBoundaryTypeProperty())()`

`[Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html)`
`[getStereotype](#getStereotype())()`
Returns stereotype for this wrapper.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[getSummaryOfFindings](#getSummaryOfFindings(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getSummaryOfFindingsProperty](#getSummaryOfFindingsProperty())()`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getToBeProperty](#getToBeProperty())()`

`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[getToolsUsed](#getToolsUsed(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getToolsUsedProperty](#getToolsUsedProperty())()`

`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getURI](#getURI(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getURIProperty](#getURIProperty())()`

`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[getViewpoint](#getViewpoint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getViewpointProperty](#getViewpointProperty())()`

`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getViews](#getViews(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getViewsProperty](#getViewsProperty())()`

`boolean`
`[is](#is(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`static boolean`
`[isInstance](#isInstance(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Boolean](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html)`
`[isToBe](#isToBe(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[removeActualPropertySet](#removeActualPropertySet(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)`

`void`
`[removeApprovalAuthority](#removeApprovalAuthority(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)`

`void`
`[removeArchitect](#removeArchitect(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)`

`void`
`[removeAssumptionAndConstraint](#removeAssumptionAndConstraint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)`

`void`
`[removeConformsTo](#removeConformsTo(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)`

`void`
`[removeCreatingOrganization](#removeCreatingOrganization(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)`

`void`
`[removePropertySet](#removePropertySet(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)`

`void`
`[removePurpose](#removePurpose(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)`

`void`
`[removeRecommendations](#removeRecommendations(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)`

`void`
`[removeSummaryOfFindings](#removeSummaryOfFindings(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)`

`void`
`[removeToolsUsed](#removeToolsUsed(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)`

`void`
`[removeViewpoint](#removeViewpoint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)`

`void`
`[removeViews](#removeViews(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)`

`void`
`[setActualPropertySet](#setActualPropertySet(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> value)`

`void`
`[setApprovalAuthority](#setApprovalAuthority(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> value)`

`void`
`[setArchitect](#setArchitect(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> value)`

`void`
`[setArchitectureFramework](#setArchitectureFramework(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.updm.utils.UPDMProfile.ArchitectureFrameworkKindEnum))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [UPDMProfile.ArchitectureFrameworkKindEnum](UPDMProfile.ArchitectureFrameworkKindEnum.html) value)`

`void`
`[setAssumptionAndConstraint](#setAssumptionAndConstraint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> value)`

`void`
`[setConformsTo](#setConformsTo(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> value)`

`void`
`[setCreatingOrganization](#setCreatingOrganization(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> value)`

`void`
`[setDateCompleted](#setDateCompleted(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)`

`void`
`[setEndBoundaryType](#setEndBoundaryType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)`

`void`
`[setPropertySet](#setPropertySet(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> value)`

`void`
`[setPurpose](#setPurpose(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> value)`

`void`
`[setRecommendations](#setRecommendations(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> value)`

`void`
`[setStartBoundaryType](#setStartBoundaryType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)`

`void`
`[setSummaryOfFindings](#setSummaryOfFindings(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> value)`

`void`
`[setToBe](#setToBe(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Boolean](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html) value)`

`void`
`[setToolsUsed](#setToolsUsed(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> value)`

`void`
`[setURI](#setURI(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)`

`void`
`[setViewpoint](#setViewpoint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> value)`

`void`
`[setViews](#setViews(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> value)`
Methods inherited from class com.nomagic.profiles.[ProfileImplementation.StereotypeWrapper](../../profiles/ProfileImplementation.StereotypeWrapper.html)
`[apply](../../profiles/ProfileImplementation.StereotypeWrapper.html#apply(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [isDerivedStereotype](../../profiles/ProfileImplementation.StereotypeWrapper.html#isDerivedStereotype(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)), [isSameOrDerivedStereotype](../../profiles/ProfileImplementation.StereotypeWrapper.html#isSameOrDerivedStereotype(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)), [unApply](../../profiles/ProfileImplementation.StereotypeWrapper.html#unApply(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
STEREOTYPE_NAME
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) STEREOTYPE_NAME
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.updm.utils.UPDMProfile.ServiceDescriptionStereotype.STEREOTYPE_NAME)
APPROVALAUTHORITY
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) APPROVALAUTHORITY
References the actual organizational resource that has the authority to approve the architectural description.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.updm.utils.UPDMProfile.ServiceDescriptionStereotype.APPROVALAUTHORITY)
ARCHITECT
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) ARCHITECT
The name of the architect responsible for the ArchitecturalDescription.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.updm.utils.UPDMProfile.ServiceDescriptionStereotype.ARCHITECT)
ARCHITECTUREFRAMEWORK
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) ARCHITECTUREFRAMEWORK
The architectureFramework tag identifies the subset of aliases to use within the context of the ArchitecturalDescription (i. e. DoDAF, MODAF or none)
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.updm.utils.UPDMProfile.ServiceDescriptionStereotype.ARCHITECTUREFRAMEWORK)
ASSUMPTIONANDCONSTRAINT
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) ASSUMPTIONANDCONSTRAINT
Any assumptions, constraints, and limitations contained in the ArchitecturalDescription, including those affecting deployment, communications performance, information assurance environments, etc.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.updm.utils.UPDMProfile.ServiceDescriptionStereotype.ASSUMPTIONANDCONSTRAINT)
CREATINGORGANIZATION
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) CREATINGORGANIZATION
Describes the ActualOrganizationalResource creating the ArchitecturalDescription.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.updm.utils.UPDMProfile.ServiceDescriptionStereotype.CREATINGORGANIZATION)
DATECOMPLETED
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) DATECOMPLETED
Date that the Architectural Description was completed.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.updm.utils.UPDMProfile.ServiceDescriptionStereotype.DATECOMPLETED)
PURPOSE
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) PURPOSE
Explains the need for the Architecture, what it will demonstrate, the types of analyses that will be applied to it, who is expected to perform the analyses, what decisions are expected to be made on the basis of each form of analysis, who is expected to make those decisions, and what actions are expected to result.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.updm.utils.UPDMProfile.ServiceDescriptionStereotype.PURPOSE)
RECOMMENDATIONS
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) RECOMMENDATIONS
States the recommendations that have been developed based on the architecture effort. Examples include recommended system implementations, and opportunities for technology insertion.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.updm.utils.UPDMProfile.ServiceDescriptionStereotype.RECOMMENDATIONS)
SUMMARYOFFINDINGS
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) SUMMARYOFFINDINGS
Summarizes the findings that have been developed so far. This may be updated several times during the development of the ArchitecturalDescription.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.updm.utils.UPDMProfile.ServiceDescriptionStereotype.SUMMARYOFFINDINGS)
TOBE
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TOBE
Indicates whether the ArchitecturalDescription is existing or future.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.updm.utils.UPDMProfile.ServiceDescriptionStereotype.TOBE)
TOOLSUSED
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TOOLSUSED
Identifies any tools used to develop the ArchitecturalDescription as well as file names and formats if appropriate.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.updm.utils.UPDMProfile.ServiceDescriptionStereotype.TOOLSUSED)
VIEWPOINT
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) VIEWPOINT
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.updm.utils.UPDMProfile.ServiceDescriptionStereotype.VIEWPOINT)
VIEWS
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) VIEWS
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.updm.utils.UPDMProfile.ServiceDescriptionStereotype.VIEWS)
URI
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) URI
Unique identifier for the element.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.updm.utils.UPDMProfile.ServiceDescriptionStereotype.URI)
ACTUALPROPERTYSET
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) ACTUALPROPERTYSET
The actual measurements to which the element must conform.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.updm.utils.UPDMProfile.ServiceDescriptionStereotype.ACTUALPROPERTYSET)
CONFORMSTO
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) CONFORMSTO
Standard that this UPDM element is conforming to.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.updm.utils.UPDMProfile.ServiceDescriptionStereotype.CONFORMSTO)
ENDBOUNDARYTYPE
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) ENDBOUNDARYTYPE
End time of boundary.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.updm.utils.UPDMProfile.ServiceDescriptionStereotype.ENDBOUNDARYTYPE)
PROPERTYSET
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) PROPERTYSET
Types of measurements corresponding to the actual measurements.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.updm.utils.UPDMProfile.ServiceDescriptionStereotype.PROPERTYSET)
STARTBOUNDARYTYPE
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) STARTBOUNDARYTYPE
Start time of a boundary.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.updm.utils.UPDMProfile.ServiceDescriptionStereotype.STARTBOUNDARYTYPE)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ServiceDescriptionStereotype
protected ServiceDescriptionStereotype([UPDMProfile](UPDMProfile.html) profile)
 ============ METHOD DETAIL ========== 
Method Details
getStereotype
public [Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) getStereotype()
Description copied from class: `[ProfileImplementation.StereotypeWrapper](../../profiles/ProfileImplementation.StereotypeWrapper.html#getStereotype())`
Returns stereotype for this wrapper.
Specified by:
`[getStereotype](../../profiles/ProfileImplementation.StereotypeWrapper.html#getStereotype())` in class `[ProfileImplementation.StereotypeWrapper](../../profiles/ProfileImplementation.StereotypeWrapper.html)`
Returns:
stereotype
getApprovalAuthorityProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getApprovalAuthorityProperty()
getArchitectProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getArchitectProperty()
getArchitectureFrameworkProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getArchitectureFrameworkProperty()
getAssumptionAndConstraintProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getAssumptionAndConstraintProperty()
getCreatingOrganizationProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getCreatingOrganizationProperty()
getDateCompletedProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getDateCompletedProperty()
getPurposeProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getPurposeProperty()
getRecommendationsProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getRecommendationsProperty()
getSummaryOfFindingsProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getSummaryOfFindingsProperty()
getToBeProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getToBeProperty()
getToolsUsedProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getToolsUsedProperty()
getViewpointProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getViewpointProperty()
getViewsProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getViewsProperty()
getURIProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getURIProperty()
getActualPropertySetProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getActualPropertySetProperty()
getConformsToProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getConformsToProperty()
getEndBoundaryTypeProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getEndBoundaryTypeProperty()
getPropertySetProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getPropertySetProperty()
getStartBoundaryTypeProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getStartBoundaryTypeProperty()
setApprovalAuthority
public void setApprovalAuthority([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> value)
clearApprovalAuthority
public void clearApprovalAuthority([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
addApprovalAuthority
public void addApprovalAuthority([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)
removeApprovalAuthority
public void removeApprovalAuthority([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)
getApprovalAuthority
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> getApprovalAuthority([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setArchitect
public void setArchitect([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> value)
clearArchitect
public void clearArchitect([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
addArchitect
public void addArchitect([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)
removeArchitect
public void removeArchitect([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)
getArchitect
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> getArchitect([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setArchitectureFramework
public void setArchitectureFramework([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [UPDMProfile.ArchitectureFrameworkKindEnum](UPDMProfile.ArchitectureFrameworkKindEnum.html) value)
clearArchitectureFramework
public void clearArchitectureFramework([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
getArchitectureFramework
@CheckForNullpublic [UPDMProfile.ArchitectureFrameworkKindEnum](UPDMProfile.ArchitectureFrameworkKindEnum.html) getArchitectureFramework([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setAssumptionAndConstraint
public void setAssumptionAndConstraint([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> value)
clearAssumptionAndConstraint
public void clearAssumptionAndConstraint([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
addAssumptionAndConstraint
public void addAssumptionAndConstraint([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)
removeAssumptionAndConstraint
public void removeAssumptionAndConstraint([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)
getAssumptionAndConstraint
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> getAssumptionAndConstraint([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setCreatingOrganization
public void setCreatingOrganization([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> value)
clearCreatingOrganization
public void clearCreatingOrganization([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
addCreatingOrganization
public void addCreatingOrganization([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)
removeCreatingOrganization
public void removeCreatingOrganization([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)
getCreatingOrganization
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> getCreatingOrganization([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setDateCompleted
public void setDateCompleted([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)
clearDateCompleted
public void clearDateCompleted([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
getDateCompleted
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getDateCompleted([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setPurpose
public void setPurpose([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> value)
clearPurpose
public void clearPurpose([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
addPurpose
public void addPurpose([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)
removePurpose
public void removePurpose([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)
getPurpose
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> getPurpose([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setRecommendations
public void setRecommendations([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> value)
clearRecommendations
public void clearRecommendations([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
addRecommendations
public void addRecommendations([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)
removeRecommendations
public void removeRecommendations([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)
getRecommendations
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> getRecommendations([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setSummaryOfFindings
public void setSummaryOfFindings([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> value)
clearSummaryOfFindings
public void clearSummaryOfFindings([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
addSummaryOfFindings
public void addSummaryOfFindings([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)
removeSummaryOfFindings
public void removeSummaryOfFindings([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)
getSummaryOfFindings
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> getSummaryOfFindings([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setToBe
public void setToBe([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Boolean](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html) value)
clearToBe
public void clearToBe([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
isToBe
@CheckForNullpublic [Boolean](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html) isToBe([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setToolsUsed
public void setToolsUsed([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> value)
clearToolsUsed
public void clearToolsUsed([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
addToolsUsed
public void addToolsUsed([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)
removeToolsUsed
public void removeToolsUsed([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)
getToolsUsed
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> getToolsUsed([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setViewpoint
public void setViewpoint([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> value)
clearViewpoint
public void clearViewpoint([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
addViewpoint
public void addViewpoint([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)
removeViewpoint
public void removeViewpoint([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)
getViewpoint
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> getViewpoint([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setViews
public void setViews([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> value)
clearViews
public void clearViews([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
addViews
public void addViews([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)
removeViews
public void removeViews([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)
getViews
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getViews([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setURI
public void setURI([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)
clearURI
public void clearURI([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
getURI
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getURI([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setActualPropertySet
public void setActualPropertySet([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> value)
clearActualPropertySet
public void clearActualPropertySet([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
addActualPropertySet
public void addActualPropertySet([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)
removeActualPropertySet
public void removeActualPropertySet([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)
getActualPropertySet
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getActualPropertySet([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setConformsTo
public void setConformsTo([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> value)
clearConformsTo
public void clearConformsTo([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
addConformsTo
public void addConformsTo([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)
removeConformsTo
public void removeConformsTo([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)
getConformsTo
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getConformsTo([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setEndBoundaryType
public void setEndBoundaryType([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)
clearEndBoundaryType
public void clearEndBoundaryType([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
getEndBoundaryType
@CheckForNullpublic [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) getEndBoundaryType([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setPropertySet
public void setPropertySet([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> value)
clearPropertySet
public void clearPropertySet([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
addPropertySet
public void addPropertySet([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)
removePropertySet
public void removePropertySet([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)
getPropertySet
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getPropertySet([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setStartBoundaryType
public void setStartBoundaryType([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)
clearStartBoundaryType
public void clearStartBoundaryType([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
getStartBoundaryType
@CheckForNullpublic [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) getStartBoundaryType([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
is
public boolean is(@CheckForNull
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
isInstance
public static boolean isInstance(@CheckForNull
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.updm.utils</a></div>
<h1 class="title" title="Class UPDMProfile.ServiceDescriptionStereotype">Class UPDMProfile.ServiceDescriptionStereotype</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="../../profiles/ProfileImplementation.StereotypeWrapper.html" title="class in com.nomagic.profiles">com.nomagic.profiles.ProfileImplementation.StereotypeWrapper</a>
<div class="inheritance">com.nomagic.updm.utils.UPDMProfile.ServiceDescriptionStereotype</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><code><a href="UPDMProfile.html" title="class in com.nomagic.updm.utils">UPDMProfile</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public static class </span><span class="element-name type-name-label">UPDMProfile.ServiceDescriptionStereotype</span>
<span class="extends-implements">extends <a href="../../profiles/ProfileImplementation.StereotypeWrapper.html" title="class in com.nomagic.profiles">ProfileImplementation.StereotypeWrapper</a></span></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ACTUALPROPERTYSET">ACTUALPROPERTYSET</a></code></div>
<div class="col-last even-row-color">
<div class="block">The actual measurements to which the element must conform.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#APPROVALAUTHORITY">APPROVALAUTHORITY</a></code></div>
<div class="col-last odd-row-color">
<div class="block">References the actual organizational resource that has the authority to approve the architectural description.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ARCHITECT">ARCHITECT</a></code></div>
<div class="col-last even-row-color">
<div class="block">The name of the architect responsible for the ArchitecturalDescription.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ARCHITECTUREFRAMEWORK">ARCHITECTUREFRAMEWORK</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The architectureFramework tag identifies the subset of aliases to use within the context of the ArchitecturalDescription (i.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ASSUMPTIONANDCONSTRAINT">ASSUMPTIONANDCONSTRAINT</a></code></div>
<div class="col-last even-row-color">
<div class="block">Any assumptions, constraints, and limitations contained in the ArchitecturalDescription, including those affecting deployment, communications performance, information assurance environments, etc.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#CONFORMSTO">CONFORMSTO</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Standard that this UPDM element is conforming to.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CREATINGORGANIZATION">CREATINGORGANIZATION</a></code></div>
<div class="col-last even-row-color">
<div class="block">Describes the ActualOrganizationalResource creating the ArchitecturalDescription.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DATECOMPLETED">DATECOMPLETED</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Date that the Architectural Description was completed.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ENDBOUNDARYTYPE">ENDBOUNDARYTYPE</a></code></div>
<div class="col-last even-row-color">
<div class="block">End time of boundary.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#PROPERTYSET">PROPERTYSET</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Types of measurements corresponding to the actual measurements.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#PURPOSE">PURPOSE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Explains the need for the Architecture, what it will demonstrate, the types of analyses that will be applied to it, who is expected to perform the analyses, what decisions are expected to be made on the basis of each form of analysis, who is expected to make those decisions, and what actions are expected to result.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#RECOMMENDATIONS">RECOMMENDATIONS</a></code></div>
<div class="col-last odd-row-color">
<div class="block">States the recommendations that have been developed based on the architecture effort.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#STARTBOUNDARYTYPE">STARTBOUNDARYTYPE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Start time of a boundary.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#STEREOTYPE_NAME">STEREOTYPE_NAME</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SUMMARYOFFINDINGS">SUMMARYOFFINDINGS</a></code></div>
<div class="col-last even-row-color">
<div class="block">Summarizes the findings that have been developed so far.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TOBE">TOBE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Indicates whether the ArchitecturalDescription is existing or future.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TOOLSUSED">TOOLSUSED</a></code></div>
<div class="col-last even-row-color">
<div class="block">Identifies any tools used to develop the ArchitecturalDescription as well as file names and formats if appropriate.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#URI">URI</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Unique identifier for the element.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#VIEWPOINT">VIEWPOINT</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#VIEWS">VIEWS</a></code></div>
<div class="col-last odd-row-color"> </div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier</div>
<div class="table-header col-second">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>protected </code></div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.updm.utils.UPDMProfile)">ServiceDescriptionStereotype</a><wbr/>(<a href="UPDMProfile.html" title="class in com.nomagic.updm.utils">UPDMProfile</a> profile)</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addActualPropertySet(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">addActualPropertySet</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addApprovalAuthority(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">addApprovalAuthority</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addArchitect(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">addArchitect</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addAssumptionAndConstraint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">addAssumptionAndConstraint</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addConformsTo(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">addConformsTo</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addCreatingOrganization(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">addCreatingOrganization</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addPropertySet(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">addPropertySet</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addPurpose(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">addPurpose</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addRecommendations(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">addRecommendations</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addSummaryOfFindings(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">addSummaryOfFindings</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addToolsUsed(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">addToolsUsed</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addViewpoint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">addViewpoint</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addViews(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">addViews</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearActualPropertySet(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearActualPropertySet</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearApprovalAuthority(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearApprovalAuthority</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearArchitect(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearArchitect</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearArchitectureFramework(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearArchitectureFramework</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearAssumptionAndConstraint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearAssumptionAndConstraint</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearConformsTo(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearConformsTo</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearCreatingOrganization(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearCreatingOrganization</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearDateCompleted(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearDateCompleted</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearEndBoundaryType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearEndBoundaryType</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearPropertySet(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearPropertySet</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearPurpose(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearPurpose</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearRecommendations(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearRecommendations</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearStartBoundaryType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearStartBoundaryType</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearSummaryOfFindings(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearSummaryOfFindings</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearToBe(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearToBe</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearToolsUsed(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearToolsUsed</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearURI(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearURI</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearViewpoint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearViewpoint</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearViews(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearViews</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getActualPropertySet(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getActualPropertySet</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getActualPropertySetProperty()">getActualPropertySetProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getApprovalAuthority(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getApprovalAuthority</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getApprovalAuthorityProperty()">getApprovalAuthorityProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getArchitect(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getArchitect</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getArchitectProperty()">getArchitectProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UPDMProfile.ArchitectureFrameworkKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.ArchitectureFrameworkKindEnum</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getArchitectureFramework(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getArchitectureFramework</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getArchitectureFrameworkProperty()">getArchitectureFrameworkProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAssumptionAndConstraint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getAssumptionAndConstraint</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAssumptionAndConstraintProperty()">getAssumptionAndConstraintProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getConformsTo(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getConformsTo</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getConformsToProperty()">getConformsToProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCreatingOrganization(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getCreatingOrganization</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCreatingOrganizationProperty()">getCreatingOrganizationProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDateCompleted(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getDateCompleted</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDateCompletedProperty()">getDateCompletedProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getEndBoundaryType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getEndBoundaryType</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getEndBoundaryTypeProperty()">getEndBoundaryTypeProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPropertySet(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getPropertySet</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPropertySetProperty()">getPropertySetProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPurpose(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getPurpose</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPurposeProperty()">getPurposeProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRecommendations(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getRecommendations</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRecommendationsProperty()">getRecommendationsProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStartBoundaryType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getStartBoundaryType</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStartBoundaryTypeProperty()">getStartBoundaryTypeProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStereotype()">getStereotype</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns stereotype for this wrapper.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSummaryOfFindings(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getSummaryOfFindings</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSummaryOfFindingsProperty()">getSummaryOfFindingsProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getToBeProperty()">getToBeProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getToolsUsed(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getToolsUsed</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getToolsUsedProperty()">getToolsUsedProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getURI(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getURI</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getURIProperty()">getURIProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getViewpoint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getViewpoint</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getViewpointProperty()">getViewpointProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getViews(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getViews</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getViewsProperty()">getViewsProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#is(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">is</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isInstance(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isInstance</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isToBe(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isToBe</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeActualPropertySet(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">removeActualPropertySet</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeApprovalAuthority(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">removeApprovalAuthority</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeArchitect(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">removeArchitect</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeAssumptionAndConstraint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">removeAssumptionAndConstraint</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeConformsTo(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">removeConformsTo</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeCreatingOrganization(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">removeCreatingOrganization</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removePropertySet(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">removePropertySet</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removePurpose(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">removePurpose</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeRecommendations(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">removeRecommendations</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeSummaryOfFindings(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">removeSummaryOfFindings</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeToolsUsed(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">removeToolsUsed</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeViewpoint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">removeViewpoint</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeViews(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">removeViews</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setActualPropertySet(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">setActualPropertySet</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setApprovalAuthority(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">setApprovalAuthority</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setArchitect(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">setArchitect</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setArchitectureFramework(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.updm.utils.UPDMProfile.ArchitectureFrameworkKindEnum)">setArchitectureFramework</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="UPDMProfile.ArchitectureFrameworkKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.ArchitectureFrameworkKindEnum</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAssumptionAndConstraint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">setAssumptionAndConstraint</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setConformsTo(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">setConformsTo</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCreatingOrganization(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">setCreatingOrganization</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDateCompleted(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">setDateCompleted</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setEndBoundaryType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setEndBoundaryType</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setPropertySet(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">setPropertySet</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setPurpose(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">setPurpose</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setRecommendations(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">setRecommendations</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setStartBoundaryType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setStartBoundaryType</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSummaryOfFindings(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">setSummaryOfFindings</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setToBe(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">setToBe</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setToolsUsed(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">setToolsUsed</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setURI(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">setURI</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setViewpoint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">setViewpoint</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setViews(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">setViews</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.profiles.ProfileImplementation.StereotypeWrapper">Methods inherited from class com.nomagic.profiles.<a href="../../profiles/ProfileImplementation.StereotypeWrapper.html" title="class in com.nomagic.profiles">ProfileImplementation.StereotypeWrapper</a></h3>
<code><a href="../../profiles/ProfileImplementation.StereotypeWrapper.html#apply(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">apply</a>, <a href="../../profiles/ProfileImplementation.StereotypeWrapper.html#isDerivedStereotype(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">isDerivedStereotype</a>, <a href="../../profiles/ProfileImplementation.StereotypeWrapper.html#isSameOrDerivedStereotype(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">isSameOrDerivedStereotype</a>, <a href="../../profiles/ProfileImplementation.StereotypeWrapper.html#unApply(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">unApply</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">
<h2>Field Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="STEREOTYPE_NAME">
<h3>STEREOTYPE_NAME</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">STEREOTYPE_NAME</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.updm.utils.UPDMProfile.ServiceDescriptionStereotype.STEREOTYPE_NAME">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="APPROVALAUTHORITY">
<h3>APPROVALAUTHORITY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">APPROVALAUTHORITY</span></div>
<div class="block">References the actual organizational resource that has the authority to approve the architectural description.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.updm.utils.UPDMProfile.ServiceDescriptionStereotype.APPROVALAUTHORITY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ARCHITECT">
<h3>ARCHITECT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ARCHITECT</span></div>
<div class="block">The name of the architect responsible for the ArchitecturalDescription.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.updm.utils.UPDMProfile.ServiceDescriptionStereotype.ARCHITECT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ARCHITECTUREFRAMEWORK">
<h3>ARCHITECTUREFRAMEWORK</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ARCHITECTUREFRAMEWORK</span></div>
<div class="block">The architectureFramework tag identifies the subset of aliases to use within the context of the ArchitecturalDescription (i. e. DoDAF, MODAF or none)</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.updm.utils.UPDMProfile.ServiceDescriptionStereotype.ARCHITECTUREFRAMEWORK">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ASSUMPTIONANDCONSTRAINT">
<h3>ASSUMPTIONANDCONSTRAINT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ASSUMPTIONANDCONSTRAINT</span></div>
<div class="block">Any assumptions, constraints, and limitations contained in the ArchitecturalDescription, including those affecting deployment, communications performance, information assurance environments, etc.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.updm.utils.UPDMProfile.ServiceDescriptionStereotype.ASSUMPTIONANDCONSTRAINT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CREATINGORGANIZATION">
<h3>CREATINGORGANIZATION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">CREATINGORGANIZATION</span></div>
<div class="block">Describes the ActualOrganizationalResource creating the ArchitecturalDescription.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.updm.utils.UPDMProfile.ServiceDescriptionStereotype.CREATINGORGANIZATION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DATECOMPLETED">
<h3>DATECOMPLETED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DATECOMPLETED</span></div>
<div class="block">Date that the Architectural Description was completed.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.updm.utils.UPDMProfile.ServiceDescriptionStereotype.DATECOMPLETED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PURPOSE">
<h3>PURPOSE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">PURPOSE</span></div>
<div class="block">Explains the need for the Architecture, what it will demonstrate, the types of analyses that will be applied to it, who is expected to perform the analyses, what decisions are expected to be made on the basis of each form of analysis, who is expected to make those decisions, and what actions are expected to result.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.updm.utils.UPDMProfile.ServiceDescriptionStereotype.PURPOSE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="RECOMMENDATIONS">
<h3>RECOMMENDATIONS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">RECOMMENDATIONS</span></div>
<div class="block">States the recommendations that have been developed based on the architecture effort. Examples include recommended system implementations, and opportunities for technology insertion.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.updm.utils.UPDMProfile.ServiceDescriptionStereotype.RECOMMENDATIONS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SUMMARYOFFINDINGS">
<h3>SUMMARYOFFINDINGS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SUMMARYOFFINDINGS</span></div>
<div class="block">Summarizes the findings that have been developed so far. This may be updated several times during the development of the ArchitecturalDescription.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.updm.utils.UPDMProfile.ServiceDescriptionStereotype.SUMMARYOFFINDINGS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TOBE">
<h3>TOBE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TOBE</span></div>
<div class="block">Indicates whether the ArchitecturalDescription is existing or future.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.updm.utils.UPDMProfile.ServiceDescriptionStereotype.TOBE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TOOLSUSED">
<h3>TOOLSUSED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TOOLSUSED</span></div>
<div class="block">Identifies any tools used to develop the ArchitecturalDescription as well as file names and formats if appropriate.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.updm.utils.UPDMProfile.ServiceDescriptionStereotype.TOOLSUSED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="VIEWPOINT">
<h3>VIEWPOINT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">VIEWPOINT</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.updm.utils.UPDMProfile.ServiceDescriptionStereotype.VIEWPOINT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="VIEWS">
<h3>VIEWS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">VIEWS</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.updm.utils.UPDMProfile.ServiceDescriptionStereotype.VIEWS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="URI">
<h3>URI</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">URI</span></div>
<div class="block">Unique identifier for the element.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.updm.utils.UPDMProfile.ServiceDescriptionStereotype.URI">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ACTUALPROPERTYSET">
<h3>ACTUALPROPERTYSET</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ACTUALPROPERTYSET</span></div>
<div class="block">The actual measurements to which the element must conform.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.updm.utils.UPDMProfile.ServiceDescriptionStereotype.ACTUALPROPERTYSET">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CONFORMSTO">
<h3>CONFORMSTO</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">CONFORMSTO</span></div>
<div class="block">Standard that this UPDM element is conforming to.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.updm.utils.UPDMProfile.ServiceDescriptionStereotype.CONFORMSTO">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ENDBOUNDARYTYPE">
<h3>ENDBOUNDARYTYPE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ENDBOUNDARYTYPE</span></div>
<div class="block">End time of boundary.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.updm.utils.UPDMProfile.ServiceDescriptionStereotype.ENDBOUNDARYTYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PROPERTYSET">
<h3>PROPERTYSET</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">PROPERTYSET</span></div>
<div class="block">Types of measurements corresponding to the actual measurements.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.updm.utils.UPDMProfile.ServiceDescriptionStereotype.PROPERTYSET">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="STARTBOUNDARYTYPE">
<h3>STARTBOUNDARYTYPE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">STARTBOUNDARYTYPE</span></div>
<div class="block">Start time of a boundary.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.updm.utils.UPDMProfile.ServiceDescriptionStereotype.STARTBOUNDARYTYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.updm.utils.UPDMProfile)">
<h3>ServiceDescriptionStereotype</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="element-name">ServiceDescriptionStereotype</span><wbr/><span class="parameters">(<a href="UPDMProfile.html" title="class in com.nomagic.updm.utils">UPDMProfile</a> profile)</span></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">
<h2>Method Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="getStereotype()">
<h3>getStereotype</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getStereotype</span>()</div>
<div class="block"><span class="description-from-type-label">Description copied from class: <code><a href="../../profiles/ProfileImplementation.StereotypeWrapper.html#getStereotype()">ProfileImplementation.StereotypeWrapper</a></code></span></div>
<div class="block">Returns stereotype for this wrapper.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../profiles/ProfileImplementation.StereotypeWrapper.html#getStereotype()">getStereotype</a></code> in class <code><a href="../../profiles/ProfileImplementation.StereotypeWrapper.html" title="class in com.nomagic.profiles">ProfileImplementation.StereotypeWrapper</a></code></dd>
<dt>Returns:</dt>
<dd>stereotype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getApprovalAuthorityProperty()">
<h3>getApprovalAuthorityProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getApprovalAuthorityProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getArchitectProperty()">
<h3>getArchitectProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getArchitectProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getArchitectureFrameworkProperty()">
<h3>getArchitectureFrameworkProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getArchitectureFrameworkProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getAssumptionAndConstraintProperty()">
<h3>getAssumptionAndConstraintProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getAssumptionAndConstraintProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getCreatingOrganizationProperty()">
<h3>getCreatingOrganizationProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getCreatingOrganizationProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getDateCompletedProperty()">
<h3>getDateCompletedProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getDateCompletedProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getPurposeProperty()">
<h3>getPurposeProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getPurposeProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getRecommendationsProperty()">
<h3>getRecommendationsProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getRecommendationsProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getSummaryOfFindingsProperty()">
<h3>getSummaryOfFindingsProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getSummaryOfFindingsProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getToBeProperty()">
<h3>getToBeProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getToBeProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getToolsUsedProperty()">
<h3>getToolsUsedProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getToolsUsedProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getViewpointProperty()">
<h3>getViewpointProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getViewpointProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getViewsProperty()">
<h3>getViewsProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getViewsProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getURIProperty()">
<h3>getURIProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getURIProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getActualPropertySetProperty()">
<h3>getActualPropertySetProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getActualPropertySetProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getConformsToProperty()">
<h3>getConformsToProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getConformsToProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getEndBoundaryTypeProperty()">
<h3>getEndBoundaryTypeProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getEndBoundaryTypeProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getPropertySetProperty()">
<h3>getPropertySetProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getPropertySetProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getStartBoundaryTypeProperty()">
<h3>getStartBoundaryTypeProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getStartBoundaryTypeProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setApprovalAuthority(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">
<h3>setApprovalAuthority</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setApprovalAuthority</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearApprovalAuthority(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearApprovalAuthority</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearApprovalAuthority</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="addApprovalAuthority(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>addApprovalAuthority</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addApprovalAuthority</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="removeApprovalAuthority(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>removeApprovalAuthority</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeApprovalAuthority</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="getApprovalAuthority(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getApprovalAuthority</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getApprovalAuthority</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setArchitect(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">
<h3>setArchitect</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setArchitect</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearArchitect(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearArchitect</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearArchitect</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="addArchitect(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>addArchitect</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addArchitect</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="removeArchitect(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>removeArchitect</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeArchitect</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="getArchitect(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getArchitect</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getArchitect</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setArchitectureFramework(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.updm.utils.UPDMProfile.ArchitectureFrameworkKindEnum)">
<h3>setArchitectureFramework</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setArchitectureFramework</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="UPDMProfile.ArchitectureFrameworkKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.ArchitectureFrameworkKindEnum</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearArchitectureFramework(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearArchitectureFramework</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearArchitectureFramework</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getArchitectureFramework(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getArchitectureFramework</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="UPDMProfile.ArchitectureFrameworkKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.ArchitectureFrameworkKindEnum</a></span> <span class="element-name">getArchitectureFramework</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setAssumptionAndConstraint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">
<h3>setAssumptionAndConstraint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAssumptionAndConstraint</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearAssumptionAndConstraint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearAssumptionAndConstraint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearAssumptionAndConstraint</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="addAssumptionAndConstraint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>addAssumptionAndConstraint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addAssumptionAndConstraint</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="removeAssumptionAndConstraint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>removeAssumptionAndConstraint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeAssumptionAndConstraint</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="getAssumptionAndConstraint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getAssumptionAndConstraint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getAssumptionAndConstraint</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setCreatingOrganization(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">
<h3>setCreatingOrganization</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCreatingOrganization</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearCreatingOrganization(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearCreatingOrganization</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearCreatingOrganization</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="addCreatingOrganization(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>addCreatingOrganization</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addCreatingOrganization</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="removeCreatingOrganization(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>removeCreatingOrganization</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeCreatingOrganization</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="getCreatingOrganization(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getCreatingOrganization</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getCreatingOrganization</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setDateCompleted(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>setDateCompleted</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDateCompleted</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearDateCompleted(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearDateCompleted</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearDateCompleted</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getDateCompleted(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getDateCompleted</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDateCompleted</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setPurpose(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">
<h3>setPurpose</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPurpose</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearPurpose(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearPurpose</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearPurpose</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="addPurpose(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>addPurpose</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addPurpose</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="removePurpose(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>removePurpose</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removePurpose</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="getPurpose(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getPurpose</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getPurpose</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setRecommendations(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">
<h3>setRecommendations</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRecommendations</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearRecommendations(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearRecommendations</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearRecommendations</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="addRecommendations(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>addRecommendations</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addRecommendations</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="removeRecommendations(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>removeRecommendations</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeRecommendations</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="getRecommendations(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getRecommendations</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getRecommendations</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setSummaryOfFindings(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">
<h3>setSummaryOfFindings</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSummaryOfFindings</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearSummaryOfFindings(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearSummaryOfFindings</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearSummaryOfFindings</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="addSummaryOfFindings(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>addSummaryOfFindings</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addSummaryOfFindings</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="removeSummaryOfFindings(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>removeSummaryOfFindings</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeSummaryOfFindings</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="getSummaryOfFindings(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getSummaryOfFindings</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getSummaryOfFindings</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setToBe(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">
<h3>setToBe</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setToBe</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearToBe(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearToBe</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearToBe</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="isToBe(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isToBe</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">isToBe</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setToolsUsed(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">
<h3>setToolsUsed</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setToolsUsed</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearToolsUsed(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearToolsUsed</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearToolsUsed</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="addToolsUsed(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>addToolsUsed</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addToolsUsed</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="removeToolsUsed(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>removeToolsUsed</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeToolsUsed</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="getToolsUsed(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getToolsUsed</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getToolsUsed</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setViewpoint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">
<h3>setViewpoint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setViewpoint</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearViewpoint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearViewpoint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearViewpoint</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="addViewpoint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>addViewpoint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addViewpoint</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="removeViewpoint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>removeViewpoint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeViewpoint</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="getViewpoint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getViewpoint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getViewpoint</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setViews(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">
<h3>setViews</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setViews</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearViews(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearViews</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearViews</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="addViews(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>addViews</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addViews</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="removeViews(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>removeViews</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeViews</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="getViews(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getViews</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getViews</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setURI(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>setURI</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setURI</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearURI(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearURI</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearURI</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getURI(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getURI</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getURI</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setActualPropertySet(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">
<h3>setActualPropertySet</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setActualPropertySet</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearActualPropertySet(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearActualPropertySet</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearActualPropertySet</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="addActualPropertySet(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>addActualPropertySet</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addActualPropertySet</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="removeActualPropertySet(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>removeActualPropertySet</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeActualPropertySet</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="getActualPropertySet(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getActualPropertySet</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getActualPropertySet</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setConformsTo(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">
<h3>setConformsTo</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setConformsTo</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearConformsTo(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearConformsTo</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearConformsTo</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="addConformsTo(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>addConformsTo</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addConformsTo</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="removeConformsTo(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>removeConformsTo</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeConformsTo</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="getConformsTo(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getConformsTo</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getConformsTo</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setEndBoundaryType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>setEndBoundaryType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setEndBoundaryType</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearEndBoundaryType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearEndBoundaryType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearEndBoundaryType</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getEndBoundaryType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getEndBoundaryType</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getEndBoundaryType</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setPropertySet(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">
<h3>setPropertySet</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPropertySet</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearPropertySet(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearPropertySet</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearPropertySet</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="addPropertySet(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>addPropertySet</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addPropertySet</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="removePropertySet(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>removePropertySet</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removePropertySet</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="getPropertySet(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getPropertySet</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getPropertySet</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setStartBoundaryType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>setStartBoundaryType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setStartBoundaryType</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearStartBoundaryType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearStartBoundaryType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearStartBoundaryType</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getStartBoundaryType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getStartBoundaryType</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getStartBoundaryType</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="is(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>is</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">is</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="isInstance(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isInstance</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isInstance</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>
````
