# JAVA OPENAPI: ProjectOptions (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/core/options/ProjectOptions.html
- source_path: `com/nomagic/magicdraw/core/options/ProjectOptions.html`
- source_sha256: `d4c72ac8cf20a548d4d80ee7f5ca97ae8b24808ee743624e9d3102aeaa590e21`
- captured_utc: `2026-07-14T16:51:17.341150+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.core.options](package-summary.html)

## Class ProjectOptions

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml.MDElementImpl
com.nomagic.magicdraw.core.options.ProjectOptions

All Implemented Interfaces:
`[BaseElement](../../uml/BaseElement.html)`, `[MDElement](../../uml/MDElement.html)`, `[PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html)`, `[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`, `[EventListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html)`

@OpenApiAllpublic classProjectOptions
extends com.nomagic.magicdraw.uml.MDElementImpl
implements [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html), [PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html)

This class provides access and storage of project options.
 Most of the project options have convenience setters/getters.

See Also:
[Serialized Form](../../../../../serialized-form.html#com.nomagic.magicdraw.core.options.ProjectOptions)

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`static enum`
`[ProjectOptions.ApplyPropertyImageChoice](ProjectOptions.ApplyPropertyImageChoice.html)`

`static enum`
`[ProjectOptions.ExportPreferenceWhenLimitsExceeded](ProjectOptions.ExportPreferenceWhenLimitsExceeded.html)`

`static enum`
`[ProjectOptions.TooltipsStyleChoice](ProjectOptions.TooltipsStyleChoice.html)`
 =========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ACTIVE_VALIDATION_GROUP](#ACTIVE_VALIDATION_GROUP)`
Real time validation group name
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[BROWSER_GROUP](#BROWSER_GROUP)`
Browser group
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[COLLABORATION_GROUP](#COLLABORATION_GROUP)`
Collaboration group name
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[COMPLETE_DIAGRAMS](#COMPLETE_DIAGRAMS)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[COMPOSITION_INSPECTION_GROUP](#COMPOSITION_INSPECTION_GROUP)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[COMPOSITION_INSPECTION_SEVERITY_ADVANCED](#COMPOSITION_INSPECTION_SEVERITY_ADVANCED)`

`static final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[COMPOSITION_INSPECTION_SEVERITY_CHOICE](#COMPOSITION_INSPECTION_SEVERITY_CHOICE)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[COMPOSITION_INSPECTION_SEVERITY_STANDARD](#COMPOSITION_INSPECTION_SEVERITY_STANDARD)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[CREATE_AUTOMATICALLY](#CREATE_AUTOMATICALLY)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DEPENDENCY_CHECKER_GROUP](#DEPENDENCY_CHECKER_GROUP)`
Dependency checker group name.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DIAGRAM_ASPECTS_GROUP](#DIAGRAM_ASPECTS_GROUP)`

`static final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`
`[DIAGRAM_CONTEXT_MODES](#DIAGRAM_CONTEXT_MODES)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DIAGRAMS_GROUP](#DIAGRAMS_GROUP)`
Diagrams group name
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DO_NOT_CREATE](#DO_NOT_CREATE)`

`static final int`
`[DOC_TIPS](#DOC_TIPS)`
Deprecated.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ELEMENT_HIDING_GROUP](#ELEMENT_HIDING_GROUP)`
Element hiding group name
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[EXPORT](#EXPORT)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[GENERAL_GROUP](#GENERAL_GROUP)`
General group name
`static final int`
`[INDEX_COMMON](#INDEX_COMMON)`

`static final int`
`[INDEX_CUSTOM](#INDEX_CUSTOM)`

`static final int`
`[INDEX_NONE](#INDEX_NONE)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[LAYOUT_TEMPLATE_CREATION_MODE_DEFINITION](#LAYOUT_TEMPLATE_CREATION_MODE_DEFINITION)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[LAYOUT_TEMPLATE_CREATION_MODE_USAGE](#LAYOUT_TEMPLATE_CREATION_MODE_USAGE)`

`static final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`
`[LAYOUT_TEMPLATE_CREATION_MODES](#LAYOUT_TEMPLATE_CREATION_MODES)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[LOCKING_GROUP](#LOCKING_GROUP)`
Locking group name
`static final int`
`[NAME_TIPS](#NAME_TIPS)`
Deprecated.
`static final int`
`[NO_TIPS](#NO_TIPS)`
Deprecated.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[NUMBERING_GROUP](#NUMBERING_GROUP)`
Numbering group name.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[OPTIONS_LOCK](#OPTIONS_LOCK)`
Options lock event property name.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[PERSONAL_INVISIBLE_PROPERTIES](#PERSONAL_INVISIBLE_PROPERTIES)`
The name of the manager of not visible properties that affect only one
 user in multi-user environment.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[PERSONAL_VISIBLE_PROPERTIES](#PERSONAL_VISIBLE_PROPERTIES)`
The name of the manager of visible properties that affect only one
 user in multi-user environment
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[PRE_COMMIT_VALIDATION_GROUP](#PRE_COMMIT_VALIDATION_GROUP)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[PROJECT_GENERAL_PROPERTIES](#PROJECT_GENERAL_PROPERTIES)`
The name of the manager that contains user editable properties in Project options dialog.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[PROJECT_INVISIBLE_PROPERTIES](#PROJECT_INVISIBLE_PROPERTIES)`
The name of the manager of not visible properties in Project options dialog.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[QNAME_DISPLAY_STYLE_ABSOLUTE](#QNAME_DISPLAY_STYLE_ABSOLUTE)`
Qualified is calculated using named elements up to the project root - "Data"
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[QNAME_DISPLAY_STYLE_MODEL_OR_LIBRARY_RELATIVE](#QNAME_DISPLAY_STYLE_MODEL_OR_LIBRARY_RELATIVE)`
Qualified is calculated using named elements up to the nearest "Model" element or package with applied stereotype
 "ModelLibrary"
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[QNAME_DISPLAY_STYLE_MODEL_RELATIVE](#QNAME_DISPLAY_STYLE_MODEL_RELATIVE)`
Qualified is calculated using named elements up to the nearest "Model" element
`static final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`
`[QNAME_DISPLAY_STYLE_OPTIONS](#QNAME_DISPLAY_STYLE_OPTIONS)`
Collection of all possible qualified name display style modes.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[QNAME_DISPLAY_STYLE_RELATIVE](#QNAME_DISPLAY_STYLE_RELATIVE)`
Qualified is calculated using named elements up to the nearest package with applied stereotype "ModelLibrary"
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[STYLE_DIAGRAM_PROPERTIES](#STYLE_DIAGRAM_PROPERTIES)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[STYLE_MODEL_ELEMENT_DEFAULTS](#STYLE_MODEL_ELEMENT_DEFAULTS)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[STYLE_PERSONAL_PROPERTIES](#STYLE_PERSONAL_PROPERTIES)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[STYLE_USER_PROPERTIES](#STYLE_USER_PROPERTIES)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[UNIQUE_ELEMENT_NUMBER_PACKAGE_SCOPE](#UNIQUE_ELEMENT_NUMBER_PACKAGE_SCOPE)`
Deprecated.
option no longer exists
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[UNIQUE_ELEMENT_NUMBER_PROJECT_SCOPE](#UNIQUE_ELEMENT_NUMBER_PROJECT_SCOPE)`
Deprecated.
option no longer exists
`static final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`
`[UNIQUE_ELEMENT_NUMBER_SCOPE_OPTIONS](#UNIQUE_ELEMENT_NUMBER_SCOPE_OPTIONS)`
Deprecated.
options no longer exists
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[VALIDATION_GROUP](#VALIDATION_GROUP)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ProjectOptions](#%3Cinit%3E())()`
Constructor.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`void`
`[accept](#accept(com.nomagic.magicdraw.uml.Visitor))([Visitor](../../uml/Visitor.html) v)`
Method accepts visitor, and calls method visit<class name>(this) of visitor .
`static void`
`[addConfigurator](#addConfigurator(com.nomagic.magicdraw.core.options.ProjectOptionsConfigurator))([ProjectOptionsConfigurator](ProjectOptionsConfigurator.html) configurator)`
Add project options configurator
`void`
`[addHiddenBrowserTree](#addHiddenBrowserTree(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) treeID)`

`void`
`[addInvisibleProperty](#addInvisibleProperty(com.nomagic.magicdraw.properties.Property))([Property](../../properties/Property.html) property)`
Adds invisible property that affects all users in multi user environment.
`void`
`[addModuleDirectory](#addModuleDirectory(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) directory)`
Adds directory to project module directories.
`void`
`[addPersonalVisibleProperty](#addPersonalVisibleProperty(com.nomagic.magicdraw.properties.Property))([Property](../../properties/Property.html) property)`
Adds personal visible property that affects one user in multi user environment
`void`
`[addProperty](#addProperty(java.lang.String,com.nomagic.magicdraw.properties.Property))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) manager,
 [Property](../../properties/Property.html) p)`
Adds property
`void`
`[addToProjectSpellingIgnoreList](#addToProjectSpellingIgnoreList(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) newTextToBeIgnored)`

`void`
`[afterLoad](#afterLoad())()`

`void`
`[applyModifiedModelElementStyle](#applyModifiedModelElementStyle(com.nomagic.magicdraw.properties.Style))([Style](../../properties/Style.html) modelElementStyle)`
Applies user modified values to model element style
`boolean`
`[changeOwnershipForNavigability](#changeOwnershipForNavigability())()`
Gets the CHANGE_OWNERSHIP_FOR_NAVIGABILITY property value
`void`
`[checkAndAddModuleDirectory](#checkAndAddModuleDirectory(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) directory)`
Adds directory to project module directories if it was not added yet
`static void`
`[configureLoadedOptions](#configureLoadedOptions(com.nomagic.magicdraw.core.options.ProjectOptions))([ProjectOptions](ProjectOptions.html) options)`

`[Style](../../properties/Style.html)`
`[createDefaultModelElementStyle](#createDefaultModelElementStyle())()`
Returns default model element values.
`static [ProjectOptions](ProjectOptions.html)`
`[createDefaultProjectOptions](#createDefaultProjectOptions(com.nomagic.magicdraw.core.Project))([Project](../Project.html) project)`
Create default options for a given project
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getActiveValidationScope](#getActiveValidationScope())()`

`[EnumerationLiteral](../../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html)`
`[getActiveValidationSeverity](#getActiveValidationSeverity())()`

`[Style](../../properties/Style.html)`
`[getActualModelElementStyle](#getActualModelElementStyle())()`
Fast method.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getAdditionalBrowserTrees](#getAdditionalBrowserTrees())()`

`[ProjectOptions.ApplyPropertyImageChoice](ProjectOptions.ApplyPropertyImageChoice.html)`
`[getApplyPropertyImageProperty](#getApplyPropertyImageProperty())()`
Returns Apply Property Image property
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)`
`[getBrowserItemsTypes](#getBrowserItemsTypes())()`
Gets types that are filtered (not shown) in browser.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getBrowserLayout](#getBrowserLayout())()`

`[Package](../../../uml2/ext/magicdraw/classes/mdkernel/Package.html)`
`[getChoosePackageLastSelection](#getChoosePackageLastSelection())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getCompositionInspectionSeverity](#getCompositionInspectionSeverity())()`

`[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)`
`[getDecimalPlaces](#getDecimalPlaces())()`
Decimal places property to render the number (double/float) property in table and specification
`[DependencySeverityLevel](DependencySeverityLevel.html)`
`[getDependencySeverityLevel](#getDependencySeverityLevel())()`
Returns dependency checker severity level.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getDiagramContextMode](#getDiagramContextMode())()`
Returns diagram context mode for project
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getDiagramInfoCustomHTML](#getDiagramInfoCustomHTML())()`

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getDiagramInfoKeywords](#getDiagramInfoKeywords())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getDiagramsLayout](#getDiagramsLayout())()`
Deprecated.
use [`getEditorWindowsLayout()`](#getEditorWindowsLayout())
`[Style](../../properties/Style.html)`
`[getDiagramViewStyle](#getDiagramViewStyle())()`
Gets diagramViewStyle from the ProjectOptions.
`[Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[BaseElement](../../uml/BaseElement.html)>`
`[getDisableHighlightSuspended](#getDisableHighlightSuspended())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getEditorWindowsLayout](#getEditorWindowsLayout())()`

`[Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html)`
`[getExitFullScreenToolbarBounds](#getExitFullScreenToolbarBounds())()`
Getter for browser bounds.
`[ProjectOptions.ExportPreferenceWhenLimitsExceeded](ProjectOptions.ExportPreferenceWhenLimitsExceeded.html)`
`[getExportPrefWhenLimitsExceeded](#getExportPrefWhenLimitsExceeded())()`

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getFavoriteElements](#getFavoriteElements())()`

`[ElementListProperty](../../properties/ElementListProperty.html)`
`[getFavoriteElementsProperty](#getFavoriteElementsProperty())()`

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getFavoriteHyperlinks](#getFavoriteHyperlinks())()`
Get favorite hyperlinks.
`[Style](../../properties/Style.html)`
`[getFullModelElementStyle](#getFullModelElementStyle())()`
Returns default model element values with modified values.
`static [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>,[Group](Group.html)>`
`[getGroupRemap](#getGroupRemap())()`

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getHiddenBrowserTrees](#getHiddenBrowserTrees())()`

`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Package](../../../uml2/ext/magicdraw/classes/mdkernel/Package.html)>`
`[getIgnoredActiveSuites](#getIgnoredActiveSuites())()`

`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html)>`
`[getIgnoredDiagramAspects](#getIgnoredDiagramAspects())()`
Gets ignored diagram aspects
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getIgnoredDuplicatedModules](#getIgnoredDuplicatedModules())()`

`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Constraint](../../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html)>`
`[getIgnoredPassiveValidationRules](#getIgnoredPassiveValidationRules())()`
Gets ignored passive validation rules
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Package](../../../uml2/ext/magicdraw/classes/mdkernel/Package.html)>`
`[getIgnoredPassiveValidationSuites](#getIgnoredPassiveValidationSuites())()`

`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Constraint](../../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html)>`
`[getIgnoredValidationRules](#getIgnoredValidationRules())()`
Return collection of ignored constraints.
`[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)`
`[getImageHeightLimit](#getImageHeightLimit())()`

`[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)`
`[getImageWidthLimit](#getImageWidthLimit())()`

`int`
`[getIndexMode](#getIndexMode())()`

`[Package](../../../uml2/ext/magicdraw/classes/mdkernel/Package.html)[]`
`[getIndexScope](#getIndexScope())()`

`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)`
`[getIndexTypes](#getIndexTypes())()`

`[Property](../../properties/Property.html)`
`[getInvisibleProperty](#getInvisibleProperty(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)`
Gets invisible property that affects all users in multi user environment.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getLastDirectory](#getLastDirectory())()`
Deprecated.
use [`ProjectSpecificLocationRegister`](../ProjectSpecificLocationRegister.html) to store and retrieve this information
`[BaseElement](../../uml/BaseElement.html)`
`[getLastSelectedElement](#getLastSelectedElement())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getLastSelectedModulePath](#getLastSelectedModulePath())()`
Get last selected module path.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getLastSelectedTransformationName](#getLastSelectedTransformationName())()`

`boolean`
`[getLastSelectedTypeMapProfileDirection](#getLastSelectedTypeMapProfileDirection())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getLastSelectedTypeMapProfileName](#getLastSelectedTypeMapProfileName())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getLastSelectedXpdlImportLocation](#getLastSelectedXpdlImportLocation())()`
The directory last accessed for XPDL import
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getLayoutBeforeExitFullScreen](#getLayoutBeforeExitFullScreen())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getLayoutBeforeFullScreen](#getLayoutBeforeFullScreen())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getLayoutTemplateCreationMode](#getLayoutTemplateCreationMode())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getLocksFilterUsername](#getLocksFilterUsername())()`
Returns user name of lock view filter.
`[PropertyManager](../../properties/PropertyManager.html)`
`[getManager](#getManager(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)`
Returns the manager for properties.
`[EnumerationLiteral](../../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html)`
`[getMinimalSeverityProducingPreCommitWarning](#getMinimalSeverityProducingPreCommitWarning())()`
Gets minimal severity which produces warning after pre-commit validation.
`[EnumerationLiteral](../../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html)`
`[getMinimalSeverityProhibitingCommit](#getMinimalSeverityProhibitingCommit())()`
Get minimal severity which prohibits commit after pre-commit validation.
`[Style](../../properties/Style.html)`
`[getModifiedModelElementsStyle](#getModifiedModelElementsStyle())()`
Returns default model element values.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getModulesDirectories](#getModulesDirectories(boolean))(boolean resolvePathVariables)`
Returns modules paths.
`[EnumerationLiteral](../../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html)`
`[getPassiveValidationSeverity](#getPassiveValidationSeverity())()`

`[Style](../../properties/Style.html)`
`[getPersonalOptionsStyle](#getPersonalOptionsStyle())()`
Gets personalOptionsStyle from the ProjectOptions.
`[Property](../../properties/Property.html)`
`[getPersonalVisibleProperty](#getPersonalVisibleProperty(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)`
Gets personal visible property that affects one user in multi user environment
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getPreCommitValidationExcludedScope](#getPreCommitValidationExcludedScope())()`
Get elements, excluded from pre-commit validation.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Package](../../../uml2/ext/magicdraw/classes/mdkernel/Package.html)>`
`[getPreCommitValidationSuites](#getPreCommitValidationSuites())()`
Gets pre-commit validation suites.
`[Project](../Project.html)`
`[getProjectImpl](#getProjectImpl())()`

`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getProjectNotificationsByConditions](#getProjectNotificationsByConditions())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[]`
`[getProjectSpellingIgnoreList](#getProjectSpellingIgnoreList())()`

`[Property](../../properties/Property.html)`
`[getProperty](#getProperty(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) manager,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)`
Returns property
`[SyncMode](SyncMode.html)`
`[getPublicBranchSyncMode](#getPublicBranchSyncMode())()`
Method to get element hiding feature public branch synchronization mode.
`boolean`
`[getQNameDisplayAbsolute](#getQNameDisplayAbsolute())()`
Deprecated.
use [`getQNameDisplayStyle()`](#getQNameDisplayStyle()) instead.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getQNameDisplayStyle](#getQNameDisplayStyle())()`
Gets the QNAME_DISPLAY_STYLE property value.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getRecentlyOpenedWindowsIDs](#getRecentlyOpenedWindowsIDs())()`

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Classifier](../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)>`
`[getRecentTypes](#getRecentTypes())()`
Returns recent metaclasses for created types
`int`
`[getReportExtensionIndex](#getReportExtensionIndex())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getSecretProperty](#getSecretProperty(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) key)`
Retrieves secret property value according given key.
`[Style](../../properties/Style.html)`
`[getStyle](#getStyle())()`
Gets style that holds two properties manager - one for visible and user editable properties, other for
 invisible project properties.
`[StyleManager](../../properties/StyleManager.html)`
`[getSymbolStyles](#getSymbolStyles())()`
Gets symbol style manager.
`[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)`
`[getTimeLimitToBuild](#getTimeLimitToBuild())()`

`int`
`[getTipsStyle](#getTipsStyle())()`
Deprecated.
use [`getTooltipsStyle()`](#getTooltipsStyle())
`[ProjectOptions.TooltipsStyleChoice](ProjectOptions.TooltipsStyleChoice.html)`
`[getTooltipsStyle](#getTooltipsStyle())()`
Returns Tooltips Style property
`[Package](../../../uml2/ext/magicdraw/classes/mdkernel/Package.html)`
`[getTransformationDestination](#getTransformationDestination())()`

`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getUniqueElementNumberScope](#getUniqueElementNumberScope())()`
Get the Packages where autoIds are to be unique
`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getUnlockedElementRemovalInfo](#getUnlockedElementRemovalInfo())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getValidationIgnoredOption](#getValidationIgnoredOption())()`

`boolean`
`[isAutomaticBehaviorCreationMode](#isAutomaticBehaviorCreationMode())()`
Gets automatic behavior creation property value.
`boolean`
`[isAutomaticTypeCreationMode](#isAutomaticTypeCreationMode())()`
Gets automatic type creation property value.
`boolean`
`[isAutoNumbering](#isAutoNumbering())()`
Get the state of the autoNumber Option
`boolean`
`[isAutoSynchronizeParametersAndArguments](#isAutoSynchronizeParametersAndArguments())()`

`boolean`
`[isBrowserVisible](#isBrowserVisible())()`
Gets browser visibility flag
`boolean`
`[isCheckElementNumberUniques](#isCheckElementNumberUniques())()`
Get the value to check element id uniques in all id properties
`boolean`
`[isCheckForCyclicDependencies](#isCheckForCyclicDependencies())()`
Returns whether check for cyclic dependencies must be performed.
`boolean`
`[isCheckIdUniques](#isCheckIdUniques())()`
Get the value to check element id uniques in all id properties
`boolean`
`[isDetectIllegalModelReferences](#isDetectIllegalModelReferences())()`

`boolean`
`[isDisplayAllActivityParameterNodesInDiagrams](#isDisplayAllActivityParameterNodesInDiagrams())()`
Indicates if activity parameter nodes should be displayed in diagrams.
`boolean`
`[isDisplayAllPinsInDiagrams](#isDisplayAllPinsInDiagrams())()`

`boolean`
`[isDisplayElementNumberInBrowser](#isDisplayElementNumberInBrowser())()`
Get the value of display/hide autoId in the Browser
`boolean`
`[isDisplayNestedInstances](#isDisplayNestedInstances())()`
Get the state of the display nested instances property
`boolean`
`[isExcludeElementsFromReadOnlyModules](#isExcludeElementsFromReadOnlyModules())()`

`boolean`
`[isExcludeElementsFromReadOnlyModulesPreCommit](#isExcludeElementsFromReadOnlyModulesPreCommit())()`
Gets value of the Exclude Elements from Used Read-Only Project property in the pre-commit validation group.
`boolean`
`[isExportedVersionChanged](#isExportedVersionChanged())()`

`boolean`
`[isFilterEnabled](#isFilterEnabled())()`

`boolean`
`[isFilterExcludesAuxiliaryResources](#isFilterExcludesAuxiliaryResources())()`

`boolean`
`[isFilterHidesIrrelevantElements](#isFilterHidesIrrelevantElements())()`

`boolean`
`[isFilterShowsImportedElements](#isFilterShowsImportedElements())()`

`boolean`
`[isGlobalEditingEnabled](#isGlobalEditingEnabled())()`
Determines if global package permission is set to Read-Write or Read-Only
`boolean`
`[isHideInformationFlowVisibility](#isHideInformationFlowVisibility())()`

`boolean`
`[isHighlightSuspended](#isHighlightSuspended())()`

`boolean`
`[isIgnoreStandardProfiles](#isIgnoreStandardProfiles())()`
Returns indication that standard profiles must be ignored in dependency checking.
`boolean`
`[isIndexScopeAll](#isIndexScopeAll())()`

`boolean`
`[isLayoutScenarioDiagram](#isLayoutScenarioDiagram())()`

`boolean`
`[isLockedElementNumber](#isLockedElementNumber())()`
Get the value of number lock.
`boolean`
`[isLockFreeEditingEnabled](#isLockFreeEditingEnabled())()`
Determines if lock free editing is enabled in the project
`boolean`
`[isMarkInTreeAndDiagrams](#isMarkInTreeAndDiagrams())()`

`boolean`
`[isSeparateDecisionMergeAndJoinForkNotation](#isSeparateDecisionMergeAndJoinForkNotation())()`

`boolean`
`[isShowDiagramAbbreviation](#isShowDiagramAbbreviation())()`
Get the state of the show diagram abbreviation property
`boolean`
`[isSuspendAutoDisplayingOfLabels](#isSuspendAutoDisplayingOfLabels())()`

`boolean`
`[isSuspendAutoResizingOfShapes](#isSuspendAutoResizingOfShapes())()`

`boolean`
`[isTransformationInPlace](#isTransformationInPlace())()`

`boolean`
`[isUseDiagramInfoCustomMode](#isUseDiagramInfoCustomMode())()`

`boolean`
`[isUseDiagramsAspects](#isUseDiagramsAspects())()`

`boolean`
`[isUseI18NTextInDiagrams](#isUseI18NTextInDiagrams())()`

`boolean`
`[isValidateOnlyActiveDiagrams](#isValidateOnlyActiveDiagrams())()`

`boolean`
`[isValidateOnlyLocallyChangedElementsPreCommit](#isValidateOnlyLocallyChangedElementsPreCommit())()`
Gets value of the Validate Only Locally Changed Elements property in the pre-commit validation group.
`void`
`[propertyChange](#propertyChange(java.beans.PropertyChangeEvent))([PropertyChangeEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html) evt)`
Listens for property change event.
`static void`
`[remapGroupInUI](#remapGroupInUI(java.util.Collection,com.nomagic.magicdraw.core.options.Group))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> groupsToRemap,
 [Group](Group.html) newGroup)`
Remap properties group to a some other group in options UI
`static void`
`[removeConfigurator](#removeConfigurator(com.nomagic.magicdraw.core.options.ProjectOptionsConfigurator))([ProjectOptionsConfigurator](ProjectOptionsConfigurator.html) configurator)`
Remove project options configurator
`void`
`[removeHiddenBrowserTree](#removeHiddenBrowserTree(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) treeID)`

`void`
`[setActiveValidationScope](#setActiveValidationScope(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element%5B%5D))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)[] elements)`

`void`
`[setActiveValidationSeverity](#setActiveValidationSeverity(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral))([EnumerationLiteral](../../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) literal)`

`void`
`[setAdditionalBrowserTrees](#setAdditionalBrowserTrees(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> trees)`

`void`
`[setApplyPropertyImageProperty](#setApplyPropertyImageProperty(com.nomagic.magicdraw.core.options.ProjectOptions.ApplyPropertyImageChoice))([ProjectOptions.ApplyPropertyImageChoice](ProjectOptions.ApplyPropertyImageChoice.html) value)`
Sets Apply Property Image property
`void`
`[setAutomaticBehaviorCreationMode](#setAutomaticBehaviorCreationMode(boolean))(boolean val)`
Sets automatic behavior creation property value.
`void`
`[setAutomaticTypeCreationMode](#setAutomaticTypeCreationMode(boolean))(boolean val)`
Sets automatic type creation property value.
`void`
`[setAutoNumbering](#setAutoNumbering(boolean))(boolean value)`
Set AutoNumbering option
`void`
`[setAutoSynchronizeParametersAndArguments](#setAutoSynchronizeParametersAndArguments(boolean))(boolean value)`
Sets auto synchronize parameters and arguments property value.
`void`
`[setBooleanProperty](#setBooleanProperty(boolean,java.lang.String,java.lang.String,java.lang.String))(boolean value,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) manager,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) group)`

`void`
`[setBrowserItemsTypes](#setBrowserItemsTypes(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) v)`
Set types that are filtered (not shown) in browser.
`void`
`[setBrowserLayout](#setBrowserLayout(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) rez)`

`void`
`[setBrowserVisible](#setBrowserVisible(boolean))(boolean v)`
Set browser visibility flag
`void`
`[setChangeOwnershipForNavigability](#setChangeOwnershipForNavigability(boolean))(boolean value)`
Sets the HOW_DOT_NOTATION_FOR_ASSOCIATIONS property value.
`void`
`[setCheckElementNumberUniques](#setCheckElementNumberUniques(boolean))(boolean value)`
Set the value to check element number uniques
`void`
`[setCheckForCyclicDependencies](#setCheckForCyclicDependencies(boolean))(boolean value)`
Sets check for cyclic dependencies property value.
`void`
`[setCheckIdUniques](#setCheckIdUniques(boolean))(boolean value)`
Set the value to check element id uniques in all id properties
`void`
`[setChoosePackageLastSelection](#setChoosePackageLastSelection(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package))([Package](../../../uml2/ext/magicdraw/classes/mdkernel/Package.html) pck)`

`void`
`[setCompositionInspectionSeverity](#setCompositionInspectionSeverity(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) severity)`

`void`
`[setDecimalPlaces](#setDecimalPlaces(java.lang.Integer))([Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) decimalPlaces)`
Sets decimal places option value
`void`
`[setDefaults](#setDefaults())()`
Sets default project options.
`void`
`[setDependencySeverityLevel](#setDependencySeverityLevel(com.nomagic.magicdraw.core.options.DependencySeverityLevel))([DependencySeverityLevel](DependencySeverityLevel.html) value)`
Sets check for cyclic dependencies property value.
`void`
`[setDetectIllegalModelReferences](#setDetectIllegalModelReferences(boolean))(boolean isDetectIllegalReferences)`

`void`
`[setDiagramContextMode](#setDiagramContextMode(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) newValue)`
Sets diagram context mode for project
`void`
`[setDiagramInfoCustomHTML](#setDiagramInfoCustomHTML(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)`

`void`
`[setDiagramInfoKeywords](#setDiagramInfoKeywords(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> keywords)`

`void`
`[setDiagramsLayout](#setDiagramsLayout(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) rez)`
Deprecated.
use [`setEditorWindowsLayout(String)`](#setEditorWindowsLayout(java.lang.String))
`void`
`[setDisableHighlightSuspended](#setDisableHighlightSuspended(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [BaseElement](../../uml/BaseElement.html)> elements)`

`void`
`[setDisplayAllActivityParameterNodesInDiagrams](#setDisplayAllActivityParameterNodesInDiagrams(boolean))(boolean displayAllActivityParameterNodesInDiagrams)`
Sets whether to display activity parameter nodes in diagrams.
`void`
`[setDisplayAllPinsInDiagrams](#setDisplayAllPinsInDiagrams(boolean))(boolean displayAllPinsInDiagrams)`

`void`
`[setDisplayElementNumberInBrowser](#setDisplayElementNumberInBrowser(boolean))(boolean value)`
Set the value to display/hide autoIds in the Browser
`void`
`[setDisplayNestedInstances](#setDisplayNestedInstances(boolean))(boolean value)`
Set Display Nested instances option
`void`
`[setEditorWindowsLayout](#setEditorWindowsLayout(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) rez)`

`void`
`[setExcludeElementsFromReadOnlyModulesPreCommit](#setExcludeElementsFromReadOnlyModulesPreCommit(boolean))(boolean excludeFromUsedReadOnly)`
Sets value for the Exclude Elements from Used Read-Only Project property in the pre-commit validation group.
`void`
`[setExcludeReadonlyElements](#setExcludeReadonlyElements(boolean))(boolean exclude)`

`void`
`[setExitFullScreenToolbarBounds](#setExitFullScreenToolbarBounds(java.awt.Rectangle))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) bounds)`
Sets full screen toolbar bounds.
`void`
`[setExportedVersionChanged](#setExportedVersionChanged(boolean))(boolean value)`

`void`
`[setExportPrefWhenLimitsExceeded](#setExportPrefWhenLimitsExceeded(com.nomagic.magicdraw.core.options.ProjectOptions.ExportPreferenceWhenLimitsExceeded))([ProjectOptions.ExportPreferenceWhenLimitsExceeded](ProjectOptions.ExportPreferenceWhenLimitsExceeded.html) value)`

`void`
`[setFavoriteElements](#setFavoriteElements(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements)`

`void`
`[setFavoriteHyperlinks](#setFavoriteHyperlinks(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> urls)`
Set favorite hyperlinks.
`void`
`[setFilterEnabled](#setFilterEnabled(boolean))(boolean value)`

`void`
`[setFilterExcludesAuxiliaryResources](#setFilterExcludesAuxiliaryResources(boolean))(boolean value)`

`void`
`[setFilterHidesIrrelevantElements](#setFilterHidesIrrelevantElements(boolean))(boolean value)`

`void`
`[setFilterShowsImportedElements](#setFilterShowsImportedElements(boolean))(boolean value)`

`void`
`[setGlobalPermission](#setGlobalPermission(boolean))(boolean value)`
Sets package permission global property value.
`void`
`[setHiddenBrowserTrees](#setHiddenBrowserTrees(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> trees)`

`void`
`[setHideInformationFlowVisibility](#setHideInformationFlowVisibility(boolean))(boolean hideInformationFlowVisibility)`

`void`
`[setHighlightSuspended](#setHighlightSuspended(boolean))(boolean highlight)`

`void`
`[setIgnoredActiveSuites](#setIgnoredActiveSuites(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package%5B%5D))([Package](../../../uml2/ext/magicdraw/classes/mdkernel/Package.html)[] elements)`

`void`
`[setIgnoredDiagramAspects](#setIgnoredDiagramAspects(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype%5B%5D))([Stereotype](../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html)[] aspects)`

`void`
`[setIgnoredDuplicatedModules](#setIgnoredDuplicatedModules(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> value)`

`void`
`[setIgnoredPassiveValidationRules](#setIgnoredPassiveValidationRules(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint%5B%5D))([Constraint](../../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html)[] elements)`

`void`
`[setIgnoredPassiveValidationSuites](#setIgnoredPassiveValidationSuites(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package%5B%5D))([Package](../../../uml2/ext/magicdraw/classes/mdkernel/Package.html)[] elements)`

`void`
`[setIgnoredValidationResults](#setIgnoredValidationResults(java.lang.String%5B%5D))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] ignoredPairs)`

`void`
`[setIgnoredValidationRules](#setIgnoredValidationRules(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint%5B%5D))([Constraint](../../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html)[] elements)`

`void`
`[setIgnoreStandardProfiles](#setIgnoreStandardProfiles(boolean))(boolean value)`
Sets ignore standard profiles in dependency checking property.
`void`
`[setImageHeightLimit](#setImageHeightLimit(java.lang.Integer))([Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) imageHeightLimit)`

`void`
`[setImageWidthLimit](#setImageWidthLimit(java.lang.Integer))([Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) imageWidthLimit)`

`void`
`[setIndexMode](#setIndexMode(int))(int status)`

`void`
`[setIndexScope](#setIndexScope(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package%5B%5D))([Package](../../../uml2/ext/magicdraw/classes/mdkernel/Package.html)[] scope)`

`void`
`[setIndexScopeAll](#setIndexScopeAll(boolean))(boolean all)`

`void`
`[setIndexTypes](#setIndexTypes(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) types)`

`void`
`[setInvisibleProperties](#setInvisibleProperties(com.nomagic.magicdraw.properties.PropertyManager))([PropertyManager](../../properties/PropertyManager.html) newManager)`

`void`
`[setLastDirectory](#setLastDirectory(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) path)`
Deprecated.
use [`ProjectSpecificLocationRegister`](../ProjectSpecificLocationRegister.html) to store and retrieve this information
`void`
`[setLastSelectedElement](#setLastSelectedElement(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../../uml/BaseElement.html) element)`

`void`
`[setLastSelectedModulePath](#setLastSelectedModulePath(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) path)`
Set last selected module path.
`void`
`[setLastSelectedTransformationName](#setLastSelectedTransformationName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)`

`void`
`[setLastSelectedTypeMapProfileDirection](#setLastSelectedTypeMapProfileDirection(boolean))(boolean forward)`

`void`
`[setLastSelectedTypeMapProfileName](#setLastSelectedTypeMapProfileName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)`

`void`
`[setLayoutBeforeExitFullScreen](#setLayoutBeforeExitFullScreen(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) rez)`

`void`
`[setLayoutBeforeFullScreen](#setLayoutBeforeFullScreen(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) rez)`

`void`
`[setLayoutScenarioDiagram](#setLayoutScenarioDiagram(boolean))(boolean value)`
Sets to layout scenario diagram.
`void`
`[setLayoutTemplateCreationMode](#setLayoutTemplateCreationMode(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) newValue)`

`void`
`[setLockElementNumber](#setLockElementNumber(boolean))(boolean value)`
Set the value to lock element number
`void`
`[setLockFreeEditingEnabled](#setLockFreeEditingEnabled(boolean))(boolean enabled)`
Enables or disables lock free editing
`void`
`[setLocksFilterUsername](#setLocksFilterUsername(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) userName)`
Sets Lock view filter user name
`void`
`[setMarkInTreeAndDiagrams](#setMarkInTreeAndDiagrams(boolean))(boolean mark)`

`void`
`[setMinimalSeverityProducingPreCommitWarning](#setMinimalSeverityProducingPreCommitWarning(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral))([EnumerationLiteral](../../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) literal)`
Sets minimal severity which produces warning after pre-commit validation.
`void`
`[setMinimalSeverityProhibitingCommit](#setMinimalSeverityProhibitingCommit(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral))([EnumerationLiteral](../../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) literal)`
Set minimal severity which prohibits commit after pre-commit validation.
`void`
`[setModelElementStyle](#setModelElementStyle(com.nomagic.magicdraw.properties.Style))([Style](../../properties/Style.html) modelElementStyle)`
Sets style for default property values for all uml entities.
`void`
`[setModulesDirectories](#setModulesDirectories(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> collection)`
Sets project modules paths.
`void`
`[setPassiveValidationSeverity](#setPassiveValidationSeverity(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral))([EnumerationLiteral](../../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) literal)`

`void`
`[setPreCommitValidationExcludedScope](#setPreCommitValidationExcludedScope(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element%5B%5D))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)[] elements)`
Sets elements, excluded from pre-commit validation.
`void`
`[setPreCommitValidationSuites](#setPreCommitValidationSuites(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package%5B%5D))([Package](../../../uml2/ext/magicdraw/classes/mdkernel/Package.html)[] elements)`
Sets validation suites for pre-commit validation.
`void`
`[setProject](#setProject(com.nomagic.magicdraw.core.Project))([Project](../Project.html) project)`
Set project for the options.
`void`
`[setProjectNotificationByConditions](#setProjectNotificationByConditions(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) pluginID,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) notification)`

`void`
`[setPublicBranchSyncMode](#setPublicBranchSyncMode(com.nomagic.magicdraw.core.options.SyncMode))([SyncMode](SyncMode.html) syncMode)`
Element hiding public branch synchronization mode.
`void`
`[setQNameDisplayAbsolute](#setQNameDisplayAbsolute(boolean))(boolean value)`
Deprecated.
use [`setQNameDisplayStyle(String)`](#setQNameDisplayStyle(java.lang.String)) instead.
`void`
`[setQNameDisplayStyle](#setQNameDisplayStyle(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) newValue)`
Sets the QNAME_DISPLAY_STYLE property value.
`void`
`[setRecentlyOpenedWindowsIDs](#setRecentlyOpenedWindowsIDs(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> ids)`

`void`
`[setRecentTypes](#setRecentTypes(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Classifier](../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)> recentMetaclasses)`
Sets last selected metaclass for type creation
`void`
`[setReportExtensionIndex](#setReportExtensionIndex(int))(int index)`

`void`
`[setSecretProperty](#setSecretProperty(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) key,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)`
Sets secret property (maps given key to given value) Secret properties are encrypted properties that are not
 available as plain text when project options are persisted to xml.
`void`
`[setSeparateDecisionMergeAndJoinForkNotation](#setSeparateDecisionMergeAndJoinForkNotation(boolean))(boolean separateDecisionMergeAndJoinForkNotation)`

`void`
`[setShowDiagramAbbreviation](#setShowDiagramAbbreviation(boolean))(boolean showDiagramAbbreviation)`
Set show diagram abbreviation option
`void`
`[setShowDotNotationForAssociations](#setShowDotNotationForAssociations(boolean))(boolean value)`
Sets the SHOW_DOT_NOTATION_FOR_ASSOCIATIONS property value.
`void`
`[setStyle](#setStyle(com.nomagic.magicdraw.properties.Style))([Style](../../properties/Style.html) style)`
Sets style that holds two properties manager - one for visible and user editable properties, other for
 invisible project properties.
`void`
`[setSuspendAutoDisplayingOfLabels](#setSuspendAutoDisplayingOfLabels(boolean))(boolean suspend)`

`void`
`[setSuspendAutoResizingOfShapes](#setSuspendAutoResizingOfShapes(boolean))(boolean suspend)`

`void`
`[setTimeLimitToBuild](#setTimeLimitToBuild(java.lang.Integer))([Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) timeLimitToBuild)`

`void`
`[setTipsStyle](#setTipsStyle(int))(int st)`
Deprecated.
use [`setTooltipsStyle(TooltipsStyleChoice)`](#setTooltipsStyle(com.nomagic.magicdraw.core.options.ProjectOptions.TooltipsStyleChoice))
`void`
`[setTooltipsStyle](#setTooltipsStyle(com.nomagic.magicdraw.core.options.ProjectOptions.TooltipsStyleChoice))([ProjectOptions.TooltipsStyleChoice](ProjectOptions.TooltipsStyleChoice.html) value)`
Sets Tooltips Style property
`void`
`[setTransformationDestination](#setTransformationDestination(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package))([Package](../../../uml2/ext/magicdraw/classes/mdkernel/Package.html) destination)`

`void`
`[setTransformationInPlace](#setTransformationInPlace(boolean))(boolean inPlace)`

`void`
`[setUniqueElementNumberScope](#setUniqueElementNumberScope(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element%5B%5D))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)[] elements)`
Set the Packages where AutoIds are to be unique
`void`
`[setUnlockedElementRemovalInfo](#setUnlockedElementRemovalInfo(java.util.Map))([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> unlockedElementRemovalInfo)`

`void`
`[setUseDiagramInfoCustomMode](#setUseDiagramInfoCustomMode(boolean))(boolean value)`

`void`
`[setUseDiagramsAspects](#setUseDiagramsAspects(boolean))(boolean use)`

`void`
`[setUseI18NTextInDiagrams](#setUseI18NTextInDiagrams(boolean))(boolean value)`
Set useI18N property for painting a text in diagrams
`void`
`[setValidateOnlyActiveDiagrams](#setValidateOnlyActiveDiagrams(boolean))(boolean validateOnlyActiveDiagrams)`

`void`
`[setValidateOnlyLocallyChangedElementsPreCommit](#setValidateOnlyLocallyChangedElementsPreCommit(boolean))(boolean validateOnlyLocallyChangedElements)`
Sets value for the Validate Only Locally Changed Elements property in the pre-commit validation group.
`void`
`[setValidationIgnoredOption](#setValidationIgnoredOption(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)`

`void`
`[setXpdlImportLocation](#setXpdlImportLocation(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) importLocation)`

`boolean`
`[showDotNotationForAssociations](#showDotNotationForAssociations())()`
Gets the SHOW_DOT_NOTATION_FOR_ASSOCIATIONS property value
`static void`
`[updateBrowserAfterFilterChange](#updateBrowserAfterFilterChange())()`
Updates a [`Browser`](../../ui/browser/Browser.html) after the filtering was done through
 the *GUI* element.
`static void`
`[updateBrowserAfterFilterChange](#updateBrowserAfterFilterChange(java.util.function.Consumer))([Consumer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html)<[Browser](../../ui/browser/Browser.html)> savedStateBrowserConsumer)`
Updates a [`Browser`](../../ui/browser/Browser.html) after the filtering was done through
 the *GUI* element.
Methods inherited from class com.nomagic.magicdraw.uml.MDElementImpl
`accept, addPropertyChangeListener, atInsert, canAdd, canAddChild, canAddChild, canAddInstance, canBeDeleted, canChangeParent, canDeleteChild, clone, compareTo, createSortKeys, dispose, firePropertyChange, generateID, getClassType, getCommandForAppending, getHumanName, getHumanType, getID, getName, getObjectParent, getProject, getProjectProvider, getResourceID, getSortKeys, hasListeners, isEditable, isParentOf, removeAllParents, removeAllPropertyChangeListeners, removePropertyChangeListener, setID, setProjectProvider, sGetID, toString`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../uml/BaseElement.html)
`[canAdd](../../uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement))`

============ FIELD DETAIL =========== 
Field Details
OPTIONS_LOCK
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) OPTIONS_LOCK
Options lock event property name.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.OPTIONS_LOCK)
PROJECT_GENERAL_PROPERTIES
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) PROJECT_GENERAL_PROPERTIES
The name of the manager that contains user editable properties in Project options dialog.
See Also:
[`getManager(String)`](#getManager(java.lang.String))
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.PROJECT_GENERAL_PROPERTIES)
PROJECT_INVISIBLE_PROPERTIES
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) PROJECT_INVISIBLE_PROPERTIES
The name of the manager of not visible properties in Project options dialog.
See Also:
[`getManager(String)`](#getManager(java.lang.String))
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.PROJECT_INVISIBLE_PROPERTIES)
PERSONAL_INVISIBLE_PROPERTIES
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) PERSONAL_INVISIBLE_PROPERTIES
The name of the manager of not visible properties that affect only one
 user in multi-user environment.
See Also:
[`getManager(String)`](#getManager(java.lang.String))
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.PERSONAL_INVISIBLE_PROPERTIES)
PERSONAL_VISIBLE_PROPERTIES
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) PERSONAL_VISIBLE_PROPERTIES
The name of the manager of visible properties that affect only one
 user in multi-user environment
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.PERSONAL_VISIBLE_PROPERTIES)
STYLE_USER_PROPERTIES
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) STYLE_USER_PROPERTIES
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.STYLE_USER_PROPERTIES)
STYLE_PERSONAL_PROPERTIES
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) STYLE_PERSONAL_PROPERTIES
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.STYLE_PERSONAL_PROPERTIES)
STYLE_DIAGRAM_PROPERTIES
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) STYLE_DIAGRAM_PROPERTIES
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.STYLE_DIAGRAM_PROPERTIES)
STYLE_MODEL_ELEMENT_DEFAULTS
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) STYLE_MODEL_ELEMENT_DEFAULTS
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.STYLE_MODEL_ELEMENT_DEFAULTS)
ACTIVE_VALIDATION_GROUP
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ACTIVE_VALIDATION_GROUP
Real time validation group name
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.ACTIVE_VALIDATION_GROUP)
VALIDATION_GROUP
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) VALIDATION_GROUP
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.VALIDATION_GROUP)
PRE_COMMIT_VALIDATION_GROUP
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) PRE_COMMIT_VALIDATION_GROUP
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.PRE_COMMIT_VALIDATION_GROUP)
COMPOSITION_INSPECTION_GROUP
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) COMPOSITION_INSPECTION_GROUP
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.COMPOSITION_INSPECTION_GROUP)
DIAGRAM_ASPECTS_GROUP
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DIAGRAM_ASPECTS_GROUP
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.DIAGRAM_ASPECTS_GROUP)
COMPLETE_DIAGRAMS
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) COMPLETE_DIAGRAMS
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.COMPLETE_DIAGRAMS)
EXPORT
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) EXPORT
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.EXPORT)
CREATE_AUTOMATICALLY
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) CREATE_AUTOMATICALLY
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.CREATE_AUTOMATICALLY)
DO_NOT_CREATE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DO_NOT_CREATE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.DO_NOT_CREATE)
DIAGRAM_CONTEXT_MODES
public static final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) DIAGRAM_CONTEXT_MODES
COLLABORATION_GROUP
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) COLLABORATION_GROUP
Collaboration group name
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.COLLABORATION_GROUP)
ELEMENT_HIDING_GROUP
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ELEMENT_HIDING_GROUP
Element hiding group name
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.ELEMENT_HIDING_GROUP)
LOCKING_GROUP
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) LOCKING_GROUP
Locking group name
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.LOCKING_GROUP)
DEPENDENCY_CHECKER_GROUP
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DEPENDENCY_CHECKER_GROUP
Dependency checker group name.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.DEPENDENCY_CHECKER_GROUP)
QNAME_DISPLAY_STYLE_ABSOLUTE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) QNAME_DISPLAY_STYLE_ABSOLUTE
Qualified is calculated using named elements up to the project root - "Data"
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.QNAME_DISPLAY_STYLE_ABSOLUTE)
QNAME_DISPLAY_STYLE_RELATIVE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) QNAME_DISPLAY_STYLE_RELATIVE
Qualified is calculated using named elements up to the nearest package with applied stereotype "ModelLibrary"
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.QNAME_DISPLAY_STYLE_RELATIVE)
QNAME_DISPLAY_STYLE_MODEL_RELATIVE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) QNAME_DISPLAY_STYLE_MODEL_RELATIVE
Qualified is calculated using named elements up to the nearest "Model" element
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.QNAME_DISPLAY_STYLE_MODEL_RELATIVE)
QNAME_DISPLAY_STYLE_MODEL_OR_LIBRARY_RELATIVE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) QNAME_DISPLAY_STYLE_MODEL_OR_LIBRARY_RELATIVE
Qualified is calculated using named elements up to the nearest "Model" element or package with applied stereotype
 "ModelLibrary"
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.QNAME_DISPLAY_STYLE_MODEL_OR_LIBRARY_RELATIVE)
QNAME_DISPLAY_STYLE_OPTIONS
public static final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) QNAME_DISPLAY_STYLE_OPTIONS
Collection of all possible qualified name display style modes.
LAYOUT_TEMPLATE_CREATION_MODE_USAGE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) LAYOUT_TEMPLATE_CREATION_MODE_USAGE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.LAYOUT_TEMPLATE_CREATION_MODE_USAGE)
LAYOUT_TEMPLATE_CREATION_MODE_DEFINITION
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) LAYOUT_TEMPLATE_CREATION_MODE_DEFINITION
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.LAYOUT_TEMPLATE_CREATION_MODE_DEFINITION)
LAYOUT_TEMPLATE_CREATION_MODES
public static final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) LAYOUT_TEMPLATE_CREATION_MODES
NUMBERING_GROUP
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) NUMBERING_GROUP
Numbering group name.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.NUMBERING_GROUP)
BROWSER_GROUP
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) BROWSER_GROUP
Browser group
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.BROWSER_GROUP)
DIAGRAMS_GROUP
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DIAGRAMS_GROUP
Diagrams group name
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.DIAGRAMS_GROUP)
GENERAL_GROUP
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) GENERAL_GROUP
General group name
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.GENERAL_GROUP)
UNIQUE_ELEMENT_NUMBER_PROJECT_SCOPE
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) UNIQUE_ELEMENT_NUMBER_PROJECT_SCOPE
Deprecated.
option no longer exists
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.UNIQUE_ELEMENT_NUMBER_PROJECT_SCOPE)
UNIQUE_ELEMENT_NUMBER_PACKAGE_SCOPE
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) UNIQUE_ELEMENT_NUMBER_PACKAGE_SCOPE
Deprecated.
option no longer exists
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.UNIQUE_ELEMENT_NUMBER_PACKAGE_SCOPE)
UNIQUE_ELEMENT_NUMBER_SCOPE_OPTIONS
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) UNIQUE_ELEMENT_NUMBER_SCOPE_OPTIONS
Deprecated.
options no longer exists
NO_TIPS
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final int NO_TIPS
Deprecated.
Tool tips style constant. No tooltip is displayed if mouse cursor is over PresentationElement in diagram.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.NO_TIPS)
NAME_TIPS
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final int NAME_TIPS
Deprecated.
Tool tips style constant. Name as tooltip is displayed if mouse cursor is over PresentationElement in diagram.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.NAME_TIPS)
DOC_TIPS
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final int DOC_TIPS
Deprecated.
Tool tips style constant. Model element documentation as tooltip is displayed if mouse cursor is over
 PresentationElement in diagram.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.DOC_TIPS)
INDEX_NONE
public static final int INDEX_NONE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.INDEX_NONE)
INDEX_COMMON
public static final int INDEX_COMMON
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.INDEX_COMMON)
INDEX_CUSTOM
public static final int INDEX_CUSTOM
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.INDEX_CUSTOM)
COMPOSITION_INSPECTION_SEVERITY_STANDARD
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) COMPOSITION_INSPECTION_SEVERITY_STANDARD
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.COMPOSITION_INSPECTION_SEVERITY_STANDARD)
COMPOSITION_INSPECTION_SEVERITY_ADVANCED
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) COMPOSITION_INSPECTION_SEVERITY_ADVANCED
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.COMPOSITION_INSPECTION_SEVERITY_ADVANCED)
COMPOSITION_INSPECTION_SEVERITY_CHOICE
public static final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> COMPOSITION_INSPECTION_SEVERITY_CHOICE
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ProjectOptions
public ProjectOptions()
Constructor. Creates project options with initialized defaults.
 Use this constructor when compatibility properties converting should be performed.
 ============ METHOD DETAIL ========== 
Method Details
remapGroupInUI
public static void remapGroupInUI([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> groupsToRemap,
 [Group](Group.html) newGroup)
Remap properties group to a some other group in options UI
Parameters:
`groupsToRemap` - groups to remap
`newGroup` - new group
getGroupRemap
public static [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>,[Group](Group.html)> getGroupRemap()
createDefaultProjectOptions
public static [ProjectOptions](ProjectOptions.html) createDefaultProjectOptions([Project](../Project.html) project)
Create default options for a given project
Parameters:
`project` - project
Returns:
options with default settings
setProject
public void setProject([Project](../Project.html) project)
Set project for the options.
Parameters:
`project` - project
setDefaults
public void setDefaults()
Sets default project options.
getStyle
public [Style](../../properties/Style.html) getStyle()
Gets style that holds two properties manager - one for visible and user editable properties, other for
 invisible project properties.
Returns:
project properties
setStyle
public void setStyle([Style](../../properties/Style.html) style)
Sets style that holds two properties manager - one for visible and user editable properties, other for
 invisible project properties.
Parameters:
`style` - project properties
getPersonalOptionsStyle
public [Style](../../properties/Style.html) getPersonalOptionsStyle()
Gets personalOptionsStyle from the ProjectOptions. Personal options are GUI setting that
 are user specific in multiple user env.
Returns:
Style object
getDiagramViewStyle
public [Style](../../properties/Style.html) getDiagramViewStyle()
Gets diagramViewStyle from the ProjectOptions. Personal options are GUI setting that
 are user specific in multiple user env.
Returns:
Style object
getSymbolStyles
public [StyleManager](../../properties/StyleManager.html) getSymbolStyles()
Gets symbol style manager.
Returns:
symbol style manager.
configureLoadedOptions
public static void configureLoadedOptions([ProjectOptions](ProjectOptions.html) options)
addModuleDirectory
public void addModuleDirectory([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) directory)
Adds directory to project module directories.
Parameters:
`directory` - directory to add.
checkAndAddModuleDirectory
public void checkAndAddModuleDirectory([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) directory)
Adds directory to project module directories if it was not added yet
Parameters:
`directory` - directory to add.
setModulesDirectories
public void setModulesDirectories([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> collection)
Sets project modules paths.
Parameters:
`collection` - collections of String objects specifying paths to module directories.
getModulesDirectories
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getModulesDirectories(boolean resolvePathVariables)
Returns modules paths.
Parameters:
`resolvePathVariables` - true if path variables must be resolved (real paths returned)
Returns:
list of String objects file paths to module dirs.
setTipsStyle
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public void setTipsStyle(int st)
Deprecated.
use [`setTooltipsStyle(TooltipsStyleChoice)`](#setTooltipsStyle(com.nomagic.magicdraw.core.options.ProjectOptions.TooltipsStyleChoice))
Set tooltips style.
Parameters:
`st` - tips style constant.
getTipsStyle
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public int getTipsStyle()
Deprecated.
use [`getTooltipsStyle()`](#getTooltipsStyle())
Get tooltips style.
Returns:
tooltip style constant.
accept
public void accept([Visitor](../../uml/Visitor.html) v)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Description copied from interface: `[MDElement](../../uml/MDElement.html#accept(com.nomagic.magicdraw.uml.Visitor))`
Method accepts visitor, and calls method visit<class name>(this) of visitor .
 See Visitor pattern for more details.
Specified by:
`[accept](../../uml/MDElement.html#accept(com.nomagic.magicdraw.uml.Visitor))` in interface `[MDElement](../../uml/MDElement.html)`
Overrides:
`accept` in class `com.nomagic.magicdraw.uml.MDElementImpl`
Parameters:
`v` - which visits this element.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
propertyChange
public void propertyChange([PropertyChangeEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html) evt)
Listens for property change event.
Specified by:
`[propertyChange](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html#propertyChange(java.beans.PropertyChangeEvent))` in interface `[PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html)`
updateBrowserAfterFilterChange
public static void updateBrowserAfterFilterChange()
Updates a [`Browser`](../../ui/browser/Browser.html) after the filtering was done through
 the *GUI* element.
 Method does save the state of [`trees`](../../ui/browser/BrowserTabTree.html)
 and restores it before returning from a call.
updateBrowserAfterFilterChange
public static void updateBrowserAfterFilterChange([Consumer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html)<[Browser](../../ui/browser/Browser.html)> savedStateBrowserConsumer)
Updates a [`Browser`](../../ui/browser/Browser.html) after the filtering was done through
 the *GUI* element.
 Method does save the state of [`trees`](../../ui/browser/BrowserTabTree.html)
 and restores it before returning from a call.
Parameters:
`savedStateBrowserConsumer` - an implementation of [`Consumer`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html)
 that accepts a [`Browser`](../../ui/browser/Browser.html) whose state
 was already saved.
setBrowserItemsTypes
public void setBrowserItemsTypes(@CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) v)
Set types that are filtered (not shown) in browser.
Parameters:
`v` - collection of String objects short name of class type (something like `ClassTypes.getShortName(Actor.class)`).
getBrowserItemsTypes
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) getBrowserItemsTypes()
Gets types that are filtered (not shown) in browser.
Returns:
collection of String objects short name of class type (something like `ClassTypes.getShortName(Actor.class)`).
setBrowserVisible
public void setBrowserVisible(boolean v)
Set browser visibility flag
isBrowserVisible
public boolean isBrowserVisible()
Gets browser visibility flag
setChoosePackageLastSelection
public void setChoosePackageLastSelection([Package](../../../uml2/ext/magicdraw/classes/mdkernel/Package.html) pck)
getChoosePackageLastSelection
@CheckForNullpublic [Package](../../../uml2/ext/magicdraw/classes/mdkernel/Package.html) getChoosePackageLastSelection()
setDisableHighlightSuspended
public void setDisableHighlightSuspended([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [BaseElement](../../uml/BaseElement.html)> elements)
getDisableHighlightSuspended
public [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[BaseElement](../../uml/BaseElement.html)> getDisableHighlightSuspended()
getManager
@CheckForNullpublic [PropertyManager](../../properties/PropertyManager.html) getManager([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)
Returns the manager for properties.
Returns:
property manager name.
See Also:
[`PROJECT_GENERAL_PROPERTIES`](#PROJECT_GENERAL_PROPERTIES)
[`PROJECT_INVISIBLE_PROPERTIES`](#PROJECT_INVISIBLE_PROPERTIES)
[`PERSONAL_INVISIBLE_PROPERTIES`](#PERSONAL_INVISIBLE_PROPERTIES)
[`PERSONAL_VISIBLE_PROPERTIES`](#PERSONAL_VISIBLE_PROPERTIES)
getProperty
@CheckForNullpublic [Property](../../properties/Property.html) getProperty([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) manager,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)
Returns property
addProperty
public void addProperty([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) manager,
 [Property](../../properties/Property.html) p)
Adds property
getRecentlyOpenedWindowsIDs
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getRecentlyOpenedWindowsIDs()
setRecentlyOpenedWindowsIDs
public void setRecentlyOpenedWindowsIDs([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> ids)
setBrowserLayout
public void setBrowserLayout(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) rez)
Parameters:
`rez` - browser layout value
getBrowserLayout
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getBrowserLayout()
setDiagramsLayout
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public void setDiagramsLayout(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) rez)
Deprecated.
use [`setEditorWindowsLayout(String)`](#setEditorWindowsLayout(java.lang.String))
setEditorWindowsLayout
public void setEditorWindowsLayout(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) rez)
getDiagramsLayout
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getDiagramsLayout()
Deprecated.
use [`getEditorWindowsLayout()`](#getEditorWindowsLayout())
getEditorWindowsLayout
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getEditorWindowsLayout()
setProjectNotificationByConditions
public void setProjectNotificationByConditions(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) pluginID,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) notification)
getProjectNotificationsByConditions
@CheckForNullpublic [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getProjectNotificationsByConditions()
setRecentTypes
public void setRecentTypes(@CheckForNull
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Classifier](../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)> recentMetaclasses)
Sets last selected metaclass for type creation
Parameters:
`recentMetaclasses` - recent metaclasses
getRecentTypes
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Classifier](../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)> getRecentTypes()
Returns recent metaclasses for created types
Returns:
recent metaclass list
setLayoutBeforeFullScreen
public void setLayoutBeforeFullScreen(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) rez)
setLayoutBeforeExitFullScreen
public void setLayoutBeforeExitFullScreen(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) rez)
getLayoutBeforeFullScreen
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getLayoutBeforeFullScreen()
getLayoutBeforeExitFullScreen
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getLayoutBeforeExitFullScreen()
setExitFullScreenToolbarBounds
public void setExitFullScreenToolbarBounds(@CheckForNull
 [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) bounds)
Sets full screen toolbar bounds.
Parameters:
`bounds` - new bounds.
getExitFullScreenToolbarBounds
@CheckForNullpublic [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) getExitFullScreenToolbarBounds()
Getter for browser bounds.
Returns:
browser bounds.
getAdditionalBrowserTrees
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getAdditionalBrowserTrees()
setAdditionalBrowserTrees
public void setAdditionalBrowserTrees([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> trees)
getHiddenBrowserTrees
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getHiddenBrowserTrees()
setHiddenBrowserTrees
public void setHiddenBrowserTrees([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> trees)
addHiddenBrowserTree
public void addHiddenBrowserTree([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) treeID)
removeHiddenBrowserTree
public void removeHiddenBrowserTree([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) treeID)
setUseDiagramInfoCustomMode
public void setUseDiagramInfoCustomMode(boolean value)
isUseDiagramInfoCustomMode
public boolean isUseDiagramInfoCustomMode()
setExportedVersionChanged
public void setExportedVersionChanged(boolean value)
isExportedVersionChanged
public boolean isExportedVersionChanged()
setDiagramInfoCustomHTML
public void setDiagramInfoCustomHTML([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)
getDiagramInfoCustomHTML
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getDiagramInfoCustomHTML()
setDiagramInfoKeywords
public void setDiagramInfoKeywords([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> keywords)
getDiagramInfoKeywords
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getDiagramInfoKeywords()
setSecretProperty
public void setSecretProperty([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) key,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)
Sets secret property (maps given key to given value) Secret properties are encrypted properties that are not
 available as plain text when project options are persisted to xml.
Parameters:
`key` - key for the property.
`value` - value of the property.
getSecretProperty
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getSecretProperty([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) key)
Retrieves secret property value according given key. Secret properties are encrypted properties that are not
 available as plain text when project options are persisted to xml.
Parameters:
`key` - key of the property.
Returns:
property value.
setInvisibleProperties
public void setInvisibleProperties([PropertyManager](../../properties/PropertyManager.html) newManager)
setLastSelectedTransformationName
public void setLastSelectedTransformationName(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)
getLastSelectedTransformationName
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getLastSelectedTransformationName()
setTransformationDestination
public void setTransformationDestination(@CheckForNull
 [Package](../../../uml2/ext/magicdraw/classes/mdkernel/Package.html) destination)
getTransformationDestination
@CheckForNullpublic [Package](../../../uml2/ext/magicdraw/classes/mdkernel/Package.html) getTransformationDestination()
setLastSelectedTypeMapProfileName
public void setLastSelectedTypeMapProfileName(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)
getLastSelectedTypeMapProfileName
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getLastSelectedTypeMapProfileName()
setLastSelectedTypeMapProfileDirection
public void setLastSelectedTypeMapProfileDirection(boolean forward)
getLastSelectedTypeMapProfileDirection
public boolean getLastSelectedTypeMapProfileDirection()
setTransformationInPlace
public void setTransformationInPlace(boolean inPlace)
isTransformationInPlace
public boolean isTransformationInPlace()
setLastSelectedElement
public void setLastSelectedElement([BaseElement](../../uml/BaseElement.html) element)
getLastSelectedElement
@CheckForNullpublic [BaseElement](../../uml/BaseElement.html) getLastSelectedElement()
setIndexMode
public void setIndexMode(int status)
getIndexMode
public int getIndexMode()
setIndexScopeAll
public void setIndexScopeAll(boolean all)
isIndexScopeAll
public boolean isIndexScopeAll()
setIndexScope
public void setIndexScope([Package](../../../uml2/ext/magicdraw/classes/mdkernel/Package.html)[] scope)
getIndexScope
@CheckForNullpublic [Package](../../../uml2/ext/magicdraw/classes/mdkernel/Package.html)[] getIndexScope()
setIndexTypes
public void setIndexTypes([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) types)
getIndexTypes
@CheckForNullpublic [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) getIndexTypes()
setLastDirectory
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public void setLastDirectory([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) path)
Deprecated.
use [`ProjectSpecificLocationRegister`](../ProjectSpecificLocationRegister.html) to store and retrieve this information
Sets the last used project related directory.
Parameters:
`path` - last dir path.
getReportExtensionIndex
public int getReportExtensionIndex()
setReportExtensionIndex
public void setReportExtensionIndex(int index)
getLastDirectory
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getLastDirectory()
Deprecated.
use [`ProjectSpecificLocationRegister`](../ProjectSpecificLocationRegister.html) to store and retrieve this information
Returns the last used project related directory.
Returns:
the path
addInvisibleProperty
public void addInvisibleProperty([Property](../../properties/Property.html) property)
Adds invisible property that affects all users in multi user environment.
Parameters:
`property` - property
getInvisibleProperty
@CheckForNullpublic [Property](../../properties/Property.html) getInvisibleProperty([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)
Gets invisible property that affects all users in multi user environment.
Parameters:
`id` - property identifier
Returns:
invisible property
addPersonalVisibleProperty
public void addPersonalVisibleProperty([Property](../../properties/Property.html) property)
Adds personal visible property that affects one user in multi user environment
Parameters:
`property` - property
getPersonalVisibleProperty
@CheckForNullpublic [Property](../../properties/Property.html) getPersonalVisibleProperty([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)
Gets personal visible property that affects one user in multi user environment
Parameters:
`id` - property identifier
Returns:
personal visible property
addConfigurator
public static void addConfigurator([ProjectOptionsConfigurator](ProjectOptionsConfigurator.html) configurator)
Add project options configurator
Parameters:
`configurator` - options configurator.
removeConfigurator
public static void removeConfigurator([ProjectOptionsConfigurator](ProjectOptionsConfigurator.html) configurator)
Remove project options configurator
Parameters:
`configurator` - options configurator.
setModelElementStyle
public void setModelElementStyle([Style](../../properties/Style.html) modelElementStyle)
Sets style for default property values for all uml entities.
Parameters:
`modelElementStyle` - style
applyModifiedModelElementStyle
public void applyModifiedModelElementStyle([Style](../../properties/Style.html) modelElementStyle)
Applies user modified values to model element style
Parameters:
`modelElementStyle` - style to retrieve modified values from
getFullModelElementStyle
public [Style](../../properties/Style.html) getFullModelElementStyle()
Returns default model element values with modified values. Method is useful for full review of values.
 Does not return actual project model element style, used for review purposes.
Returns:
all modified values and all unchanged
getActualModelElementStyle
public [Style](../../properties/Style.html) getActualModelElementStyle()
Fast method. Returns default model element values.
Returns:
all modified values and some unmodified (unmodified values are not filtered)
getModifiedModelElementsStyle
public [Style](../../properties/Style.html) getModifiedModelElementsStyle()
Returns default model element values.
Returns:
all modified values, unchanged values are filtered
createDefaultModelElementStyle
public [Style](../../properties/Style.html) createDefaultModelElementStyle()
Returns default model element values.
Returns:
all default values, none of them are modified
showDotNotationForAssociations
public boolean showDotNotationForAssociations()
Gets the SHOW_DOT_NOTATION_FOR_ASSOCIATIONS property value
Returns:
value of SHOW_DOT_NOTATION_FOR_ASSOCIATIONS property or false if such property wasn't set.
setShowDotNotationForAssociations
public void setShowDotNotationForAssociations(boolean value)
Sets the SHOW_DOT_NOTATION_FOR_ASSOCIATIONS property value. If such property wasn't yet created, then creates one.
Parameters:
`value` - boolean property value
changeOwnershipForNavigability
public boolean changeOwnershipForNavigability()
Gets the CHANGE_OWNERSHIP_FOR_NAVIGABILITY property value
Returns:
value of CHANGE_OWNERSHIP_FOR_NAVIGABILITY property or false if such property wasn't set.
setChangeOwnershipForNavigability
public void setChangeOwnershipForNavigability(boolean value)
Sets the HOW_DOT_NOTATION_FOR_ASSOCIATIONS property value. If such property wasn't yet created, then creates one.
Parameters:
`value` - boolean property value
setBooleanProperty
public void setBooleanProperty(boolean value,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) manager,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) group)
isDisplayAllActivityParameterNodesInDiagrams
public boolean isDisplayAllActivityParameterNodesInDiagrams()
Indicates if activity parameter nodes should be displayed in diagrams.
Returns:
true if activity parameter nodes should be displayed, false otherwise.
setDisplayAllActivityParameterNodesInDiagrams
public void setDisplayAllActivityParameterNodesInDiagrams(boolean displayAllActivityParameterNodesInDiagrams)
Sets whether to display activity parameter nodes in diagrams.
Parameters:
`displayAllActivityParameterNodesInDiagrams` - property value to set.
isDisplayAllPinsInDiagrams
public boolean isDisplayAllPinsInDiagrams()
setDisplayAllPinsInDiagrams
public void setDisplayAllPinsInDiagrams(boolean displayAllPinsInDiagrams)
isSeparateDecisionMergeAndJoinForkNotation
public boolean isSeparateDecisionMergeAndJoinForkNotation()
isHideInformationFlowVisibility
public boolean isHideInformationFlowVisibility()
setHideInformationFlowVisibility
public void setHideInformationFlowVisibility(boolean hideInformationFlowVisibility)
setSeparateDecisionMergeAndJoinForkNotation
public void setSeparateDecisionMergeAndJoinForkNotation(boolean separateDecisionMergeAndJoinForkNotation)
isAutoSynchronizeParametersAndArguments
public boolean isAutoSynchronizeParametersAndArguments()
Returns:
true if parameters and arguments should be auto-synchronized.
isLayoutScenarioDiagram
public boolean isLayoutScenarioDiagram()
Returns:
true if scenario diagram should be layouted each time it is opened.
setLayoutScenarioDiagram
public void setLayoutScenarioDiagram(boolean value)
Sets to layout scenario diagram.
Parameters:
`value` - value of the property.
setAutoSynchronizeParametersAndArguments
public void setAutoSynchronizeParametersAndArguments(boolean value)
Sets auto synchronize parameters and arguments property value.
Parameters:
`value` - - value of the property.
setGlobalPermission
public void setGlobalPermission(boolean value)
Sets package permission global property value.
Parameters:
`value` - - value of the property.
getQNameDisplayAbsolute
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public boolean getQNameDisplayAbsolute()
Deprecated.
use [`getQNameDisplayStyle()`](#getQNameDisplayStyle()) instead.
Gets the QNAME_DISPLAY_STYLE property value.
Returns:
true if qualified name should be calculated starting from the project root, or false when qualified name
 should be calculated starting from the model library element.
getQNameDisplayStyle
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getQNameDisplayStyle()
Gets the QNAME_DISPLAY_STYLE property value.
Returns:
string that is one of the #QNAME_DISPLAY_STYLE_OPTIONS collection elements item.
setQNameDisplayAbsolute
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public void setQNameDisplayAbsolute(boolean value)
Deprecated.
use [`setQNameDisplayStyle(String)`](#setQNameDisplayStyle(java.lang.String)) instead.
Sets the QNAME_DISPLAY_STYLE property value.
Parameters:
`value` - true if qualified name should be calculated starting from the project root, or false when qualified
 name should be calculated starting from the model library element.
setQNameDisplayStyle
public void setQNameDisplayStyle([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) newValue)
Sets the QNAME_DISPLAY_STYLE property value.
Parameters:
`newValue` - one of the #QNAME_DISPLAY_STYLE_OPTIONS collection elements item, otherwise nothing happens -
 property remains unchanged.
getLayoutTemplateCreationMode
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getLayoutTemplateCreationMode()
setLayoutTemplateCreationMode
public void setLayoutTemplateCreationMode([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) newValue)
getTooltipsStyle
public [ProjectOptions.TooltipsStyleChoice](ProjectOptions.TooltipsStyleChoice.html) getTooltipsStyle()
Returns Tooltips Style property
Returns:
selected value
setTooltipsStyle
public void setTooltipsStyle([ProjectOptions.TooltipsStyleChoice](ProjectOptions.TooltipsStyleChoice.html) value)
Sets Tooltips Style property
Parameters:
`value` - new value.
setIgnoredValidationResults
public void setIgnoredValidationResults(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] ignoredPairs)
getIgnoredActiveSuites
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Package](../../../uml2/ext/magicdraw/classes/mdkernel/Package.html)> getIgnoredActiveSuites()
getIgnoredPassiveValidationSuites
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Package](../../../uml2/ext/magicdraw/classes/mdkernel/Package.html)> getIgnoredPassiveValidationSuites()
getIgnoredValidationRules
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Constraint](../../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html)> getIgnoredValidationRules()
Return collection of ignored constraints.
Returns:
collection of ignored constraints.
getIgnoredPassiveValidationRules
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Constraint](../../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html)> getIgnoredPassiveValidationRules()
Gets ignored passive validation rules
Returns:
ignored passive validation rules.
getIgnoredDuplicatedModules
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getIgnoredDuplicatedModules()
Returns:
modules for which warning that they found in duplicated path is not shown.
setIgnoredDuplicatedModules
public void setIgnoredDuplicatedModules([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> value)
Parameters:
`value` - modules for which warning that they found in duplicated path is not shown.
setIgnoredActiveSuites
public void setIgnoredActiveSuites(@CheckForNull
 [Package](../../../uml2/ext/magicdraw/classes/mdkernel/Package.html)[] elements)
setIgnoredPassiveValidationSuites
public void setIgnoredPassiveValidationSuites(@CheckForNull
 [Package](../../../uml2/ext/magicdraw/classes/mdkernel/Package.html)[] elements)
setIgnoredValidationRules
public void setIgnoredValidationRules(@CheckForNull
 [Constraint](../../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html)[] elements)
setIgnoredPassiveValidationRules
public void setIgnoredPassiveValidationRules(@CheckForNull
 [Constraint](../../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html)[] elements)
setPublicBranchSyncMode
public void setPublicBranchSyncMode([SyncMode](SyncMode.html) syncMode)
Element hiding public branch synchronization mode.
 Project and user specific option.
Parameters:
`syncMode` - sync mode to set
getPublicBranchSyncMode
@CheckForNullpublic [SyncMode](SyncMode.html) getPublicBranchSyncMode()
Method to get element hiding feature public branch synchronization mode.
Returns:
returns current synchronization mode or null if mode is not applicable for this project
isLockFreeEditingEnabled
public boolean isLockFreeEditingEnabled()
Determines if lock free editing is enabled in the project
Returns:
`true` if enabled, `false` otherwise
isGlobalEditingEnabled
public boolean isGlobalEditingEnabled()
Determines if global package permission is set to Read-Write or Read-Only
Returns:
`true` if Read-Write, `false` if Read-Only
setLockFreeEditingEnabled
public void setLockFreeEditingEnabled(boolean enabled)
Enables or disables lock free editing
Parameters:
`enabled` - `true` to enable, `false` to disable
getActiveValidationScope
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getActiveValidationScope()
setActiveValidationScope
public void setActiveValidationScope(@CheckForNull
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)[] elements)
isFilterExcludesAuxiliaryResources
public boolean isFilterExcludesAuxiliaryResources()
setFilterExcludesAuxiliaryResources
public void setFilterExcludesAuxiliaryResources(boolean value)
setFilterHidesIrrelevantElements
public void setFilterHidesIrrelevantElements(boolean value)
isFilterHidesIrrelevantElements
public boolean isFilterHidesIrrelevantElements()
setFilterShowsImportedElements
public void setFilterShowsImportedElements(boolean value)
isFilterShowsImportedElements
public boolean isFilterShowsImportedElements()
setFilterEnabled
public void setFilterEnabled(boolean value)
isFilterEnabled
public boolean isFilterEnabled()
getFavoriteElements
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getFavoriteElements()
setFavoriteElements
public void setFavoriteElements([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements)
getFavoriteElementsProperty
@CheckForNullpublic [ElementListProperty](../../properties/ElementListProperty.html) getFavoriteElementsProperty()
setActiveValidationSeverity
public void setActiveValidationSeverity(@CheckForNull
 [EnumerationLiteral](../../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) literal)
setPassiveValidationSeverity
public void setPassiveValidationSeverity(@CheckForNull
 [EnumerationLiteral](../../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) literal)
getActiveValidationSeverity
@CheckForNullpublic [EnumerationLiteral](../../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) getActiveValidationSeverity()
getPassiveValidationSeverity
@CheckForNullpublic [EnumerationLiteral](../../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) getPassiveValidationSeverity()
setCompositionInspectionSeverity
public void setCompositionInspectionSeverity([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) severity)
getCompositionInspectionSeverity
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getCompositionInspectionSeverity()
setDetectIllegalModelReferences
public void setDetectIllegalModelReferences(boolean isDetectIllegalReferences)
isDetectIllegalModelReferences
public boolean isDetectIllegalModelReferences()
setValidationIgnoredOption
public void setValidationIgnoredOption(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)
getValidationIgnoredOption
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getValidationIgnoredOption()
setMarkInTreeAndDiagrams
public void setMarkInTreeAndDiagrams(boolean mark)
isMarkInTreeAndDiagrams
public boolean isMarkInTreeAndDiagrams()
setExcludeReadonlyElements
public void setExcludeReadonlyElements(boolean exclude)
isExcludeElementsFromReadOnlyModules
public boolean isExcludeElementsFromReadOnlyModules()
setValidateOnlyActiveDiagrams
public void setValidateOnlyActiveDiagrams(boolean validateOnlyActiveDiagrams)
isValidateOnlyActiveDiagrams
public boolean isValidateOnlyActiveDiagrams()
setValidateOnlyLocallyChangedElementsPreCommit
public void setValidateOnlyLocallyChangedElementsPreCommit(boolean validateOnlyLocallyChangedElements)
Sets value for the Validate Only Locally Changed Elements property in the pre-commit validation group.
Parameters:
`validateOnlyLocallyChangedElements` - new value
setExcludeElementsFromReadOnlyModulesPreCommit
public void setExcludeElementsFromReadOnlyModulesPreCommit(boolean excludeFromUsedReadOnly)
Sets value for the Exclude Elements from Used Read-Only Project property in the pre-commit validation group.
Parameters:
`excludeFromUsedReadOnly` - new value
isValidateOnlyLocallyChangedElementsPreCommit
public boolean isValidateOnlyLocallyChangedElementsPreCommit()
Gets value of the Validate Only Locally Changed Elements property in the pre-commit validation group.
Returns:
true if property exists and is set to true
isExcludeElementsFromReadOnlyModulesPreCommit
public boolean isExcludeElementsFromReadOnlyModulesPreCommit()
Gets value of the Exclude Elements from Used Read-Only Project property in the pre-commit validation group.
Returns:
true if property exists and is set to true
setPreCommitValidationSuites
public void setPreCommitValidationSuites(@CheckForNull
 [Package](../../../uml2/ext/magicdraw/classes/mdkernel/Package.html)[] elements)
Sets validation suites for pre-commit validation.
Parameters:
`elements` - suites
getPreCommitValidationSuites
@CheckForNullpublic [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Package](../../../uml2/ext/magicdraw/classes/mdkernel/Package.html)> getPreCommitValidationSuites()
Gets pre-commit validation suites.
Returns:
suites or null, if the property does not exist
setPreCommitValidationExcludedScope
public void setPreCommitValidationExcludedScope(@CheckForNull
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)[] elements)
Sets elements, excluded from pre-commit validation. Creates the property, if it does not yet exist.
Parameters:
`elements` - excluded elements
getPreCommitValidationExcludedScope
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getPreCommitValidationExcludedScope()
Get elements, excluded from pre-commit validation.
Returns:
excluded scope
setMinimalSeverityProhibitingCommit
public void setMinimalSeverityProhibitingCommit(@CheckForNull
 [EnumerationLiteral](../../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) literal)
Set minimal severity which prohibits commit after pre-commit validation.
Parameters:
`literal` - new severity. Null value sets the highest level - None
getMinimalSeverityProhibitingCommit
@CheckForNullpublic [EnumerationLiteral](../../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) getMinimalSeverityProhibitingCommit()
Get minimal severity which prohibits commit after pre-commit validation.
Returns:
minimal severity or null, if such property does not exist
setMinimalSeverityProducingPreCommitWarning
public void setMinimalSeverityProducingPreCommitWarning(@CheckForNull
 [EnumerationLiteral](../../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) literal)
Sets minimal severity which produces warning after pre-commit validation.
Parameters:
`literal` - new severity. Null value sets the highest level - None
getMinimalSeverityProducingPreCommitWarning
@CheckForNullpublic [EnumerationLiteral](../../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) getMinimalSeverityProducingPreCommitWarning()
Gets minimal severity which produces warning after pre-commit validation.
Returns:
minimal severity or null, if such property does not exist
setLastSelectedModulePath
public void setLastSelectedModulePath(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) path)
Set last selected module path.
Parameters:
`path` - module path.
getLastSelectedModulePath
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getLastSelectedModulePath()
Get last selected module path.
Returns:
last module path.
setLocksFilterUsername
public void setLocksFilterUsername([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) userName)
Sets Lock view filter user name
Parameters:
`userName` - name of user which was filtered in locks view.
getLocksFilterUsername
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getLocksFilterUsername()
Returns user name of lock view filter.
Returns:
name of user which was filtered in locks view.
afterLoad
public void afterLoad()
addToProjectSpellingIgnoreList
public void addToProjectSpellingIgnoreList([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) newTextToBeIgnored)
getProjectSpellingIgnoreList
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] getProjectSpellingIgnoreList()
isCheckForCyclicDependencies
public boolean isCheckForCyclicDependencies()
Returns whether check for cyclic dependencies must be performed.
Returns:
true if checking for cyclic properties must be performed, otherwise - false.
setCheckForCyclicDependencies
public void setCheckForCyclicDependencies(boolean value)
Sets check for cyclic dependencies property value.
Parameters:
`value` - new value.
getDependencySeverityLevel
public [DependencySeverityLevel](DependencySeverityLevel.html) getDependencySeverityLevel()
Returns dependency checker severity level.
Returns:
true if checking for cyclic properties must be performed, otherwise - false.
setDependencySeverityLevel
public void setDependencySeverityLevel([DependencySeverityLevel](DependencySeverityLevel.html) value)
Sets check for cyclic dependencies property value.
Parameters:
`value` - new value.
getApplyPropertyImageProperty
public [ProjectOptions.ApplyPropertyImageChoice](ProjectOptions.ApplyPropertyImageChoice.html) getApplyPropertyImageProperty()
Returns Apply Property Image property
Returns:
selected value
setApplyPropertyImageProperty
public void setApplyPropertyImageProperty([ProjectOptions.ApplyPropertyImageChoice](ProjectOptions.ApplyPropertyImageChoice.html) value)
Sets Apply Property Image property
Parameters:
`value` - new value.
getDiagramContextMode
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getDiagramContextMode()
Returns diagram context mode for project
Returns:
diagram context mode
setDiagramContextMode
public void setDiagramContextMode([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) newValue)
Sets diagram context mode for project
Parameters:
`newValue` - context mode
isIgnoreStandardProfiles
public boolean isIgnoreStandardProfiles()
Returns indication that standard profiles must be ignored in dependency checking.
Returns:
true if checking for cyclic properties must be performed, otherwise - false.
setIgnoreStandardProfiles
public void setIgnoreStandardProfiles(boolean value)
Sets ignore standard profiles in dependency checking property.
Parameters:
`value` - new value.
getProjectImpl
public [Project](../Project.html) getProjectImpl()
Overrides:
`getProjectImpl` in class `com.nomagic.magicdraw.uml.MDElementImpl`
setAutoNumbering
public void setAutoNumbering(boolean value)
Set AutoNumbering option
Parameters:
`value` - true of autoNumber option is on
isAutoNumbering
public boolean isAutoNumbering()
Get the state of the autoNumber Option
Returns:
true if it is on
setDisplayNestedInstances
public void setDisplayNestedInstances(boolean value)
Set Display Nested instances option
Parameters:
`value` - true if to display nested instances, else false
isDisplayNestedInstances
public boolean isDisplayNestedInstances()
Get the state of the display nested instances property
Returns:
true if it is on
setShowDiagramAbbreviation
public void setShowDiagramAbbreviation(boolean showDiagramAbbreviation)
Set show diagram abbreviation option
Parameters:
`showDiagramAbbreviation` - true if to show diagram abbreviations, else false
isShowDiagramAbbreviation
public boolean isShowDiagramAbbreviation()
Get the state of the show diagram abbreviation property
Returns:
true if it is on
setDisplayElementNumberInBrowser
public void setDisplayElementNumberInBrowser(boolean value)
Set the value to display/hide autoIds in the Browser
Parameters:
`value` - true if autoIds are to be shown
setLockElementNumber
public void setLockElementNumber(boolean value)
Set the value to lock element number
Parameters:
`value` - true if lock numbers, else false
setCheckIdUniques
public void setCheckIdUniques(boolean value)
Set the value to check element id uniques in all id properties
Parameters:
`value` - true if to check id uniques, else false
setCheckElementNumberUniques
public void setCheckElementNumberUniques(boolean value)
Set the value to check element number uniques
Parameters:
`value` - true if to check id uniques, else false
isDisplayElementNumberInBrowser
public boolean isDisplayElementNumberInBrowser()
Get the value of display/hide autoId in the Browser
Returns:
true if the autoId is shown
isLockedElementNumber
public boolean isLockedElementNumber()
Get the value of number lock.
Returns:
true if locked, else false
isCheckIdUniques
public boolean isCheckIdUniques()
Get the value to check element id uniques in all id properties
Returns:
true if to check uniques, else false
isCheckElementNumberUniques
public boolean isCheckElementNumberUniques()
Get the value to check element id uniques in all id properties
Returns:
true if to check uniques, else false
getUniqueElementNumberScope
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getUniqueElementNumberScope()
Get the Packages where autoIds are to be unique
Returns:
a list of Packages
setUniqueElementNumberScope
public void setUniqueElementNumberScope(@CheckForNull
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)[] elements)
Set the Packages where AutoIds are to be unique
Parameters:
`elements` - the Packages
setUseI18NTextInDiagrams
public void setUseI18NTextInDiagrams(boolean value)
Set useI18N property for painting a text in diagrams
Parameters:
`value` - value
isUseI18NTextInDiagrams
public boolean isUseI18NTextInDiagrams()
Returns:
use useI18N property for painting a text in diagrams
getLastSelectedXpdlImportLocation
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getLastSelectedXpdlImportLocation()
The directory last accessed for XPDL import
Returns:
location
setXpdlImportLocation
public void setXpdlImportLocation([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) importLocation)
getFavoriteHyperlinks
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getFavoriteHyperlinks()
Get favorite hyperlinks.
Returns:
URLs of hyperlinks.
setFavoriteHyperlinks
public void setFavoriteHyperlinks([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> urls)
Set favorite hyperlinks.
Parameters:
`urls` - URLs of hyperlinks.
setUnlockedElementRemovalInfo
public void setUnlockedElementRemovalInfo(@CheckForNull
 [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> unlockedElementRemovalInfo)
getUnlockedElementRemovalInfo
@CheckForNullpublic [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getUnlockedElementRemovalInfo()
isUseDiagramsAspects
public boolean isUseDiagramsAspects()
setUseDiagramsAspects
public void setUseDiagramsAspects(boolean use)
isSuspendAutoResizingOfShapes
public boolean isSuspendAutoResizingOfShapes()
setSuspendAutoResizingOfShapes
public void setSuspendAutoResizingOfShapes(boolean suspend)
isSuspendAutoDisplayingOfLabels
public boolean isSuspendAutoDisplayingOfLabels()
setSuspendAutoDisplayingOfLabels
public void setSuspendAutoDisplayingOfLabels(boolean suspend)
isHighlightSuspended
public boolean isHighlightSuspended()
setHighlightSuspended
public void setHighlightSuspended(boolean highlight)
getTimeLimitToBuild
@CheckForNullpublic [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) getTimeLimitToBuild()
setTimeLimitToBuild
public void setTimeLimitToBuild(@CheckForNull
 [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) timeLimitToBuild)
getImageHeightLimit
@CheckForNullpublic [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) getImageHeightLimit()
setImageHeightLimit
public void setImageHeightLimit(@CheckForNull
 [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) imageHeightLimit)
getImageWidthLimit
@CheckForNullpublic [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) getImageWidthLimit()
setImageWidthLimit
public void setImageWidthLimit(@CheckForNull
 [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) imageWidthLimit)
getExportPrefWhenLimitsExceeded
public [ProjectOptions.ExportPreferenceWhenLimitsExceeded](ProjectOptions.ExportPreferenceWhenLimitsExceeded.html) getExportPrefWhenLimitsExceeded()
setExportPrefWhenLimitsExceeded
public void setExportPrefWhenLimitsExceeded([ProjectOptions.ExportPreferenceWhenLimitsExceeded](ProjectOptions.ExportPreferenceWhenLimitsExceeded.html) value)
getIgnoredDiagramAspects
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html)> getIgnoredDiagramAspects()
Gets ignored diagram aspects
Returns:
ignored diagram aspects
setIgnoredDiagramAspects
public void setIgnoredDiagramAspects(@CheckForNull
 [Stereotype](../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html)[] aspects)
setAutomaticTypeCreationMode
public void setAutomaticTypeCreationMode(boolean val)
Sets automatic type creation property value.
Parameters:
`val` - - automatic type creation property value
isAutomaticTypeCreationMode
public boolean isAutomaticTypeCreationMode()
Gets automatic type creation property value.
Returns:
automatic type creation layout property value.
setAutomaticBehaviorCreationMode
public void setAutomaticBehaviorCreationMode(boolean val)
Sets automatic behavior creation property value.
Parameters:
`val` - - automatic behavior creation property value
isAutomaticBehaviorCreationMode
public boolean isAutomaticBehaviorCreationMode()
Gets automatic behavior creation property value.
Returns:
automatic behavior creation layout property value.
getDecimalPlaces
@CheckForNullpublic [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) getDecimalPlaces()
Decimal places property to render the number (double/float) property in table and specification
Returns:
decimal places or null if decimal places rendering is off
setDecimalPlaces
public void setDecimalPlaces(@CheckForNull
 [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) decimalPlaces)
Sets decimal places option value
Parameters:
`decimalPlaces` - option, null indicates option off

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.core.options</a></div>
<h1 class="title" title="Class ProjectOptions">Class ProjectOptions</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml.MDElementImpl
<div class="inheritance">com.nomagic.magicdraw.core.options.ProjectOptions</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a href="../../uml/MDElement.html" title="interface in com.nomagic.magicdraw.uml">MDElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html" title="class or interface in java.util">EventListener</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ProjectOptions</span>
<span class="extends-implements">extends com.nomagic.magicdraw.uml.MDElementImpl
implements <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a></span></div>
<div class="block">This class provides access and storage of project options.
 Most of the project options have convenience setters/getters.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../serialized-form.html#com.nomagic.magicdraw.core.options.ProjectOptions">Serialized Form</a></li>
</ul>
</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">
<h2>Nested Class Summary</h2>
<div class="caption"><span>Nested Classes</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Class</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static enum </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="ProjectOptions.ApplyPropertyImageChoice.html" title="enum class in com.nomagic.magicdraw.core.options">ProjectOptions.ApplyPropertyImageChoice</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static enum </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="ProjectOptions.ExportPreferenceWhenLimitsExceeded.html" title="enum class in com.nomagic.magicdraw.core.options">ProjectOptions.ExportPreferenceWhenLimitsExceeded</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static enum </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="ProjectOptions.TooltipsStyleChoice.html" title="enum class in com.nomagic.magicdraw.core.options">ProjectOptions.TooltipsStyleChoice</a></code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ACTIVE_VALIDATION_GROUP">ACTIVE_VALIDATION_GROUP</a></code></div>
<div class="col-last even-row-color">
<div class="block">Real time validation group name</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#BROWSER_GROUP">BROWSER_GROUP</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Browser group</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#COLLABORATION_GROUP">COLLABORATION_GROUP</a></code></div>
<div class="col-last even-row-color">
<div class="block">Collaboration group name</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#COMPLETE_DIAGRAMS">COMPLETE_DIAGRAMS</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#COMPOSITION_INSPECTION_GROUP">COMPOSITION_INSPECTION_GROUP</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#COMPOSITION_INSPECTION_SEVERITY_ADVANCED">COMPOSITION_INSPECTION_SEVERITY_ADVANCED</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#COMPOSITION_INSPECTION_SEVERITY_CHOICE">COMPOSITION_INSPECTION_SEVERITY_CHOICE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#COMPOSITION_INSPECTION_SEVERITY_STANDARD">COMPOSITION_INSPECTION_SEVERITY_STANDARD</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CREATE_AUTOMATICALLY">CREATE_AUTOMATICALLY</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DEPENDENCY_CHECKER_GROUP">DEPENDENCY_CHECKER_GROUP</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Dependency checker group name.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DIAGRAM_ASPECTS_GROUP">DIAGRAM_ASPECTS_GROUP</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DIAGRAM_CONTEXT_MODES">DIAGRAM_CONTEXT_MODES</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DIAGRAMS_GROUP">DIAGRAMS_GROUP</a></code></div>
<div class="col-last even-row-color">
<div class="block">Diagrams group name</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DO_NOT_CREATE">DO_NOT_CREATE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DOC_TIPS">DOC_TIPS</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ELEMENT_HIDING_GROUP">ELEMENT_HIDING_GROUP</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Element hiding group name</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#EXPORT">EXPORT</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#GENERAL_GROUP">GENERAL_GROUP</a></code></div>
<div class="col-last odd-row-color">
<div class="block">General group name</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#INDEX_COMMON">INDEX_COMMON</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#INDEX_CUSTOM">INDEX_CUSTOM</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#INDEX_NONE">INDEX_NONE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#LAYOUT_TEMPLATE_CREATION_MODE_DEFINITION">LAYOUT_TEMPLATE_CREATION_MODE_DEFINITION</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#LAYOUT_TEMPLATE_CREATION_MODE_USAGE">LAYOUT_TEMPLATE_CREATION_MODE_USAGE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#LAYOUT_TEMPLATE_CREATION_MODES">LAYOUT_TEMPLATE_CREATION_MODES</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#LOCKING_GROUP">LOCKING_GROUP</a></code></div>
<div class="col-last even-row-color">
<div class="block">Locking group name</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#NAME_TIPS">NAME_TIPS</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#NO_TIPS">NO_TIPS</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#NUMBERING_GROUP">NUMBERING_GROUP</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Numbering group name.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#OPTIONS_LOCK">OPTIONS_LOCK</a></code></div>
<div class="col-last even-row-color">
<div class="block">Options lock event property name.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#PERSONAL_INVISIBLE_PROPERTIES">PERSONAL_INVISIBLE_PROPERTIES</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The name of the manager of not visible properties that affect only one
 user in multi-user environment.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#PERSONAL_VISIBLE_PROPERTIES">PERSONAL_VISIBLE_PROPERTIES</a></code></div>
<div class="col-last even-row-color">
<div class="block">The name of the manager of visible properties that affect only one
 user in multi-user environment</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#PRE_COMMIT_VALIDATION_GROUP">PRE_COMMIT_VALIDATION_GROUP</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#PROJECT_GENERAL_PROPERTIES">PROJECT_GENERAL_PROPERTIES</a></code></div>
<div class="col-last even-row-color">
<div class="block">The name of the manager that contains user editable properties in Project options dialog.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#PROJECT_INVISIBLE_PROPERTIES">PROJECT_INVISIBLE_PROPERTIES</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The name of the manager of not visible properties in Project options dialog.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#QNAME_DISPLAY_STYLE_ABSOLUTE">QNAME_DISPLAY_STYLE_ABSOLUTE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Qualified is calculated using named elements up to the project root - "Data"</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#QNAME_DISPLAY_STYLE_MODEL_OR_LIBRARY_RELATIVE">QNAME_DISPLAY_STYLE_MODEL_OR_LIBRARY_RELATIVE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Qualified is calculated using named elements up to the nearest "Model" element or package with applied stereotype
 "ModelLibrary"</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#QNAME_DISPLAY_STYLE_MODEL_RELATIVE">QNAME_DISPLAY_STYLE_MODEL_RELATIVE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Qualified is calculated using named elements up to the nearest "Model" element</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#QNAME_DISPLAY_STYLE_OPTIONS">QNAME_DISPLAY_STYLE_OPTIONS</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Collection of all possible qualified name display style modes.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#QNAME_DISPLAY_STYLE_RELATIVE">QNAME_DISPLAY_STYLE_RELATIVE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Qualified is calculated using named elements up to the nearest package with applied stereotype "ModelLibrary"</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#STYLE_DIAGRAM_PROPERTIES">STYLE_DIAGRAM_PROPERTIES</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#STYLE_MODEL_ELEMENT_DEFAULTS">STYLE_MODEL_ELEMENT_DEFAULTS</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#STYLE_PERSONAL_PROPERTIES">STYLE_PERSONAL_PROPERTIES</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#STYLE_USER_PROPERTIES">STYLE_USER_PROPERTIES</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#UNIQUE_ELEMENT_NUMBER_PACKAGE_SCOPE">UNIQUE_ELEMENT_NUMBER_PACKAGE_SCOPE</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">option no longer exists</div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#UNIQUE_ELEMENT_NUMBER_PROJECT_SCOPE">UNIQUE_ELEMENT_NUMBER_PROJECT_SCOPE</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">option no longer exists</div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#UNIQUE_ELEMENT_NUMBER_SCOPE_OPTIONS">UNIQUE_ELEMENT_NUMBER_SCOPE_OPTIONS</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">options no longer exists</div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#VALIDATION_GROUP">VALIDATION_GROUP</a></code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ProjectOptions</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Constructor.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#accept(com.nomagic.magicdraw.uml.Visitor)">accept</a><wbr/>(<a href="../../uml/Visitor.html" title="class in com.nomagic.magicdraw.uml">Visitor</a> v)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method accepts visitor, and calls method visit&lt;class name&gt;(this) of visitor .</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#addConfigurator(com.nomagic.magicdraw.core.options.ProjectOptionsConfigurator)">addConfigurator</a><wbr/>(<a href="ProjectOptionsConfigurator.html" title="interface in com.nomagic.magicdraw.core.options">ProjectOptionsConfigurator</a> configurator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Add project options configurator</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addHiddenBrowserTree(java.lang.String)">addHiddenBrowserTree</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> treeID)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addInvisibleProperty(com.nomagic.magicdraw.properties.Property)">addInvisibleProperty</a><wbr/>(<a href="../../properties/Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> property)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds invisible property that affects all users in multi user environment.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addModuleDirectory(java.lang.String)">addModuleDirectory</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> directory)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds directory to project module directories.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addPersonalVisibleProperty(com.nomagic.magicdraw.properties.Property)">addPersonalVisibleProperty</a><wbr/>(<a href="../../properties/Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> property)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds personal visible property that affects one user in multi user environment</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addProperty(java.lang.String,com.nomagic.magicdraw.properties.Property)">addProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> manager,
 <a href="../../properties/Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> p)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds property</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addToProjectSpellingIgnoreList(java.lang.String)">addToProjectSpellingIgnoreList</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> newTextToBeIgnored)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#afterLoad()">afterLoad</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#applyModifiedModelElementStyle(com.nomagic.magicdraw.properties.Style)">applyModifiedModelElementStyle</a><wbr/>(<a href="../../properties/Style.html" title="class in com.nomagic.magicdraw.properties">Style</a> modelElementStyle)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Applies user modified values to model element style</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#changeOwnershipForNavigability()">changeOwnershipForNavigability</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the CHANGE_OWNERSHIP_FOR_NAVIGABILITY property value</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#checkAndAddModuleDirectory(java.lang.String)">checkAndAddModuleDirectory</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> directory)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds directory to project module directories if it was not added yet</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#configureLoadedOptions(com.nomagic.magicdraw.core.options.ProjectOptions)">configureLoadedOptions</a><wbr/>(<a href="ProjectOptions.html" title="class in com.nomagic.magicdraw.core.options">ProjectOptions</a> options)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../properties/Style.html" title="class in com.nomagic.magicdraw.properties">Style</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createDefaultModelElementStyle()">createDefaultModelElementStyle</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns default model element values.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ProjectOptions.html" title="class in com.nomagic.magicdraw.core.options">ProjectOptions</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createDefaultProjectOptions(com.nomagic.magicdraw.core.Project)">createDefaultProjectOptions</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create default options for a given project</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getActiveValidationScope()">getActiveValidationScope</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getActiveValidationSeverity()">getActiveValidationSeverity</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../properties/Style.html" title="class in com.nomagic.magicdraw.properties">Style</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getActualModelElementStyle()">getActualModelElementStyle</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Fast method.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAdditionalBrowserTrees()">getAdditionalBrowserTrees</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ProjectOptions.ApplyPropertyImageChoice.html" title="enum class in com.nomagic.magicdraw.core.options">ProjectOptions.ApplyPropertyImageChoice</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getApplyPropertyImageProperty()">getApplyPropertyImageProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns Apply Property Image property</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBrowserItemsTypes()">getBrowserItemsTypes</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets types that are filtered (not shown) in browser.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBrowserLayout()">getBrowserLayout</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getChoosePackageLastSelection()">getChoosePackageLastSelection</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCompositionInspectionSeverity()">getCompositionInspectionSeverity</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDecimalPlaces()">getDecimalPlaces</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Decimal places property to render the number (double/float) property in table and specification</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="DependencySeverityLevel.html" title="enum class in com.nomagic.magicdraw.core.options">DependencySeverityLevel</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDependencySeverityLevel()">getDependencySeverityLevel</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns dependency checker severity level.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDiagramContextMode()">getDiagramContextMode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns diagram context mode for project</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDiagramInfoCustomHTML()">getDiagramInfoCustomHTML</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDiagramInfoKeywords()">getDiagramInfoKeywords</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getDiagramsLayout()">getDiagramsLayout</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#getEditorWindowsLayout()"><code>getEditorWindowsLayout()</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../properties/Style.html" title="class in com.nomagic.magicdraw.properties">Style</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDiagramViewStyle()">getDiagramViewStyle</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets diagramViewStyle from the ProjectOptions.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDisableHighlightSuspended()">getDisableHighlightSuspended</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getEditorWindowsLayout()">getEditorWindowsLayout</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getExitFullScreenToolbarBounds()">getExitFullScreenToolbarBounds</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Getter for browser bounds.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ProjectOptions.ExportPreferenceWhenLimitsExceeded.html" title="enum class in com.nomagic.magicdraw.core.options">ProjectOptions.ExportPreferenceWhenLimitsExceeded</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getExportPrefWhenLimitsExceeded()">getExportPrefWhenLimitsExceeded</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFavoriteElements()">getFavoriteElements</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../properties/ElementListProperty.html" title="class in com.nomagic.magicdraw.properties">ElementListProperty</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFavoriteElementsProperty()">getFavoriteElementsProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFavoriteHyperlinks()">getFavoriteHyperlinks</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get favorite hyperlinks.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../properties/Style.html" title="class in com.nomagic.magicdraw.properties">Style</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFullModelElementStyle()">getFullModelElementStyle</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns default model element values with modified values.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;,<wbr/><a href="Group.html" title="class in com.nomagic.magicdraw.core.options">Group</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getGroupRemap()">getGroupRemap</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getHiddenBrowserTrees()">getHiddenBrowserTrees</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIgnoredActiveSuites()">getIgnoredActiveSuites</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIgnoredDiagramAspects()">getIgnoredDiagramAspects</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets ignored diagram aspects</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIgnoredDuplicatedModules()">getIgnoredDuplicatedModules</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIgnoredPassiveValidationRules()">getIgnoredPassiveValidationRules</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets ignored passive validation rules</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIgnoredPassiveValidationSuites()">getIgnoredPassiveValidationSuites</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIgnoredValidationRules()">getIgnoredValidationRules</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return collection of ignored constraints.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getImageHeightLimit()">getImageHeightLimit</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getImageWidthLimit()">getImageWidthLimit</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIndexMode()">getIndexMode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a>[]</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIndexScope()">getIndexScope</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIndexTypes()">getIndexTypes</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../properties/Property.html" title="class in com.nomagic.magicdraw.properties">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getInvisibleProperty(java.lang.String)">getInvisibleProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets invisible property that affects all users in multi user environment.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getLastDirectory()">getLastDirectory</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../ProjectSpecificLocationRegister.html" title="class in com.nomagic.magicdraw.core"><code>ProjectSpecificLocationRegister</code></a> to store and retrieve this information</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLastSelectedElement()">getLastSelectedElement</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLastSelectedModulePath()">getLastSelectedModulePath</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get last selected module path.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLastSelectedTransformationName()">getLastSelectedTransformationName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLastSelectedTypeMapProfileDirection()">getLastSelectedTypeMapProfileDirection</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLastSelectedTypeMapProfileName()">getLastSelectedTypeMapProfileName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLastSelectedXpdlImportLocation()">getLastSelectedXpdlImportLocation</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The directory last accessed for XPDL import</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLayoutBeforeExitFullScreen()">getLayoutBeforeExitFullScreen</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLayoutBeforeFullScreen()">getLayoutBeforeFullScreen</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLayoutTemplateCreationMode()">getLayoutTemplateCreationMode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLocksFilterUsername()">getLocksFilterUsername</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns user name of lock view filter.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getManager(java.lang.String)">getManager</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the manager for properties.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMinimalSeverityProducingPreCommitWarning()">getMinimalSeverityProducingPreCommitWarning</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets minimal severity which produces warning after pre-commit validation.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMinimalSeverityProhibitingCommit()">getMinimalSeverityProhibitingCommit</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get minimal severity which prohibits commit after pre-commit validation.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../properties/Style.html" title="class in com.nomagic.magicdraw.properties">Style</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getModifiedModelElementsStyle()">getModifiedModelElementsStyle</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns default model element values.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getModulesDirectories(boolean)">getModulesDirectories</a><wbr/>(boolean resolvePathVariables)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns modules paths.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPassiveValidationSeverity()">getPassiveValidationSeverity</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../properties/Style.html" title="class in com.nomagic.magicdraw.properties">Style</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPersonalOptionsStyle()">getPersonalOptionsStyle</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets personalOptionsStyle from the ProjectOptions.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../properties/Property.html" title="class in com.nomagic.magicdraw.properties">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPersonalVisibleProperty(java.lang.String)">getPersonalVisibleProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets personal visible property that affects one user in multi user environment</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPreCommitValidationExcludedScope()">getPreCommitValidationExcludedScope</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get elements, excluded from pre-commit validation.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPreCommitValidationSuites()">getPreCommitValidationSuites</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets pre-commit validation suites.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProjectImpl()">getProjectImpl</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProjectNotificationsByConditions()">getProjectNotificationsByConditions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[]</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProjectSpellingIgnoreList()">getProjectSpellingIgnoreList</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../properties/Property.html" title="class in com.nomagic.magicdraw.properties">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProperty(java.lang.String,java.lang.String)">getProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> manager,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns property</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SyncMode.html" title="enum class in com.nomagic.magicdraw.core.options">SyncMode</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPublicBranchSyncMode()">getPublicBranchSyncMode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method to get element hiding feature public branch synchronization mode.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getQNameDisplayAbsolute()">getQNameDisplayAbsolute</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#getQNameDisplayStyle()"><code>getQNameDisplayStyle()</code></a> instead.</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getQNameDisplayStyle()">getQNameDisplayStyle</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the QNAME_DISPLAY_STYLE property value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRecentlyOpenedWindowsIDs()">getRecentlyOpenedWindowsIDs</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRecentTypes()">getRecentTypes</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns recent metaclasses for created types</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getReportExtensionIndex()">getReportExtensionIndex</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSecretProperty(java.lang.String)">getSecretProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Retrieves secret property value according given key.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../properties/Style.html" title="class in com.nomagic.magicdraw.properties">Style</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStyle()">getStyle</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets style that holds two properties manager - one for visible and user editable properties, other for
 invisible project properties.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../properties/StyleManager.html" title="class in com.nomagic.magicdraw.properties">StyleManager</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSymbolStyles()">getSymbolStyles</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets symbol style manager.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTimeLimitToBuild()">getTimeLimitToBuild</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getTipsStyle()">getTipsStyle</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#getTooltipsStyle()"><code>getTooltipsStyle()</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ProjectOptions.TooltipsStyleChoice.html" title="enum class in com.nomagic.magicdraw.core.options">ProjectOptions.TooltipsStyleChoice</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTooltipsStyle()">getTooltipsStyle</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns Tooltips Style property</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTransformationDestination()">getTransformationDestination</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getUniqueElementNumberScope()">getUniqueElementNumberScope</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get the Packages where autoIds are to be unique</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getUnlockedElementRemovalInfo()">getUnlockedElementRemovalInfo</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getValidationIgnoredOption()">getValidationIgnoredOption</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isAutomaticBehaviorCreationMode()">isAutomaticBehaviorCreationMode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets automatic behavior creation property value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isAutomaticTypeCreationMode()">isAutomaticTypeCreationMode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets automatic type creation property value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isAutoNumbering()">isAutoNumbering</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get the state of the  autoNumber Option</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isAutoSynchronizeParametersAndArguments()">isAutoSynchronizeParametersAndArguments</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isBrowserVisible()">isBrowserVisible</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets browser visibility flag</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isCheckElementNumberUniques()">isCheckElementNumberUniques</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get the value to check element id uniques in all id properties</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isCheckForCyclicDependencies()">isCheckForCyclicDependencies</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns whether check for cyclic dependencies must be performed.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isCheckIdUniques()">isCheckIdUniques</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get the value to check element id uniques in all id properties</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isDetectIllegalModelReferences()">isDetectIllegalModelReferences</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isDisplayAllActivityParameterNodesInDiagrams()">isDisplayAllActivityParameterNodesInDiagrams</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Indicates if activity parameter nodes should be displayed in diagrams.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isDisplayAllPinsInDiagrams()">isDisplayAllPinsInDiagrams</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isDisplayElementNumberInBrowser()">isDisplayElementNumberInBrowser</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get the value of display/hide autoId in the Browser</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isDisplayNestedInstances()">isDisplayNestedInstances</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get the state of the display nested instances property</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isExcludeElementsFromReadOnlyModules()">isExcludeElementsFromReadOnlyModules</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isExcludeElementsFromReadOnlyModulesPreCommit()">isExcludeElementsFromReadOnlyModulesPreCommit</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets value of the Exclude Elements from Used Read-Only Project property in the pre-commit validation group.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isExportedVersionChanged()">isExportedVersionChanged</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isFilterEnabled()">isFilterEnabled</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isFilterExcludesAuxiliaryResources()">isFilterExcludesAuxiliaryResources</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isFilterHidesIrrelevantElements()">isFilterHidesIrrelevantElements</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isFilterShowsImportedElements()">isFilterShowsImportedElements</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isGlobalEditingEnabled()">isGlobalEditingEnabled</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Determines if global package permission is set to Read-Write or Read-Only</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isHideInformationFlowVisibility()">isHideInformationFlowVisibility</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isHighlightSuspended()">isHighlightSuspended</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isIgnoreStandardProfiles()">isIgnoreStandardProfiles</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns indication that standard profiles must be ignored in dependency checking.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isIndexScopeAll()">isIndexScopeAll</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isLayoutScenarioDiagram()">isLayoutScenarioDiagram</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isLockedElementNumber()">isLockedElementNumber</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get the value of number lock.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isLockFreeEditingEnabled()">isLockFreeEditingEnabled</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Determines if lock free editing is enabled in the project</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isMarkInTreeAndDiagrams()">isMarkInTreeAndDiagrams</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isSeparateDecisionMergeAndJoinForkNotation()">isSeparateDecisionMergeAndJoinForkNotation</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowDiagramAbbreviation()">isShowDiagramAbbreviation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get the state of the show diagram abbreviation property</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isSuspendAutoDisplayingOfLabels()">isSuspendAutoDisplayingOfLabels</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isSuspendAutoResizingOfShapes()">isSuspendAutoResizingOfShapes</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isTransformationInPlace()">isTransformationInPlace</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isUseDiagramInfoCustomMode()">isUseDiagramInfoCustomMode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isUseDiagramsAspects()">isUseDiagramsAspects</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isUseI18NTextInDiagrams()">isUseI18NTextInDiagrams</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isValidateOnlyActiveDiagrams()">isValidateOnlyActiveDiagrams</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isValidateOnlyLocallyChangedElementsPreCommit()">isValidateOnlyLocallyChangedElementsPreCommit</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets value of the Validate Only Locally Changed Elements property in the pre-commit validation group.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#propertyChange(java.beans.PropertyChangeEvent)">propertyChange</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans">PropertyChangeEvent</a> evt)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Listens for property change event.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#remapGroupInUI(java.util.Collection,com.nomagic.magicdraw.core.options.Group)">remapGroupInUI</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; groupsToRemap,
 <a href="Group.html" title="class in com.nomagic.magicdraw.core.options">Group</a> newGroup)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Remap properties group to a some other group in options UI</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#removeConfigurator(com.nomagic.magicdraw.core.options.ProjectOptionsConfigurator)">removeConfigurator</a><wbr/>(<a href="ProjectOptionsConfigurator.html" title="interface in com.nomagic.magicdraw.core.options">ProjectOptionsConfigurator</a> configurator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Remove project options configurator</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeHiddenBrowserTree(java.lang.String)">removeHiddenBrowserTree</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> treeID)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setActiveValidationScope(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element%5B%5D)">setActiveValidationScope</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>[] elements)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setActiveValidationSeverity(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral)">setActiveValidationSeverity</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> literal)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAdditionalBrowserTrees(java.util.Collection)">setAdditionalBrowserTrees</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; trees)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setApplyPropertyImageProperty(com.nomagic.magicdraw.core.options.ProjectOptions.ApplyPropertyImageChoice)">setApplyPropertyImageProperty</a><wbr/>(<a href="ProjectOptions.ApplyPropertyImageChoice.html" title="enum class in com.nomagic.magicdraw.core.options">ProjectOptions.ApplyPropertyImageChoice</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets Apply Property Image property</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAutomaticBehaviorCreationMode(boolean)">setAutomaticBehaviorCreationMode</a><wbr/>(boolean val)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets automatic behavior creation property value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAutomaticTypeCreationMode(boolean)">setAutomaticTypeCreationMode</a><wbr/>(boolean val)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets automatic type creation property value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAutoNumbering(boolean)">setAutoNumbering</a><wbr/>(boolean value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set AutoNumbering option</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAutoSynchronizeParametersAndArguments(boolean)">setAutoSynchronizeParametersAndArguments</a><wbr/>(boolean value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets auto synchronize parameters and arguments property value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setBooleanProperty(boolean,java.lang.String,java.lang.String,java.lang.String)">setBooleanProperty</a><wbr/>(boolean value,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> manager,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setBrowserItemsTypes(java.util.Collection)">setBrowserItemsTypes</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> v)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set types that are filtered (not shown) in browser.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setBrowserLayout(java.lang.String)">setBrowserLayout</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> rez)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setBrowserVisible(boolean)">setBrowserVisible</a><wbr/>(boolean v)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set browser visibility flag</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setChangeOwnershipForNavigability(boolean)">setChangeOwnershipForNavigability</a><wbr/>(boolean value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the HOW_DOT_NOTATION_FOR_ASSOCIATIONS property value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCheckElementNumberUniques(boolean)">setCheckElementNumberUniques</a><wbr/>(boolean value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set the value to check element number uniques</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCheckForCyclicDependencies(boolean)">setCheckForCyclicDependencies</a><wbr/>(boolean value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets check for cyclic dependencies property value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCheckIdUniques(boolean)">setCheckIdUniques</a><wbr/>(boolean value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set the value to check element id uniques in all id properties</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setChoosePackageLastSelection(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)">setChoosePackageLastSelection</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> pck)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCompositionInspectionSeverity(java.lang.String)">setCompositionInspectionSeverity</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> severity)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDecimalPlaces(java.lang.Integer)">setDecimalPlaces</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> decimalPlaces)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets decimal places option value</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDefaults()">setDefaults</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets default project options.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDependencySeverityLevel(com.nomagic.magicdraw.core.options.DependencySeverityLevel)">setDependencySeverityLevel</a><wbr/>(<a href="DependencySeverityLevel.html" title="enum class in com.nomagic.magicdraw.core.options">DependencySeverityLevel</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets check for cyclic dependencies property value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDetectIllegalModelReferences(boolean)">setDetectIllegalModelReferences</a><wbr/>(boolean isDetectIllegalReferences)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDiagramContextMode(java.lang.String)">setDiagramContextMode</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> newValue)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets diagram context mode for project</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDiagramInfoCustomHTML(java.lang.String)">setDiagramInfoCustomHTML</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDiagramInfoKeywords(java.util.Collection)">setDiagramInfoKeywords</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; keywords)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#setDiagramsLayout(java.lang.String)">setDiagramsLayout</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> rez)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#setEditorWindowsLayout(java.lang.String)"><code>setEditorWindowsLayout(String)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDisableHighlightSuspended(java.util.Collection)">setDisableHighlightSuspended</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt; elements)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDisplayAllActivityParameterNodesInDiagrams(boolean)">setDisplayAllActivityParameterNodesInDiagrams</a><wbr/>(boolean displayAllActivityParameterNodesInDiagrams)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets whether to display activity parameter nodes in diagrams.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDisplayAllPinsInDiagrams(boolean)">setDisplayAllPinsInDiagrams</a><wbr/>(boolean displayAllPinsInDiagrams)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDisplayElementNumberInBrowser(boolean)">setDisplayElementNumberInBrowser</a><wbr/>(boolean value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set the value to display/hide autoIds in the Browser</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDisplayNestedInstances(boolean)">setDisplayNestedInstances</a><wbr/>(boolean value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set Display Nested instances option</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setEditorWindowsLayout(java.lang.String)">setEditorWindowsLayout</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> rez)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setExcludeElementsFromReadOnlyModulesPreCommit(boolean)">setExcludeElementsFromReadOnlyModulesPreCommit</a><wbr/>(boolean excludeFromUsedReadOnly)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets value for the Exclude Elements from Used Read-Only Project property in the pre-commit validation group.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setExcludeReadonlyElements(boolean)">setExcludeReadonlyElements</a><wbr/>(boolean exclude)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setExitFullScreenToolbarBounds(java.awt.Rectangle)">setExitFullScreenToolbarBounds</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> bounds)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets full screen toolbar bounds.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setExportedVersionChanged(boolean)">setExportedVersionChanged</a><wbr/>(boolean value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setExportPrefWhenLimitsExceeded(com.nomagic.magicdraw.core.options.ProjectOptions.ExportPreferenceWhenLimitsExceeded)">setExportPrefWhenLimitsExceeded</a><wbr/>(<a href="ProjectOptions.ExportPreferenceWhenLimitsExceeded.html" title="enum class in com.nomagic.magicdraw.core.options">ProjectOptions.ExportPreferenceWhenLimitsExceeded</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setFavoriteElements(java.util.List)">setFavoriteElements</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setFavoriteHyperlinks(java.util.List)">setFavoriteHyperlinks</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; urls)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set favorite hyperlinks.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setFilterEnabled(boolean)">setFilterEnabled</a><wbr/>(boolean value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setFilterExcludesAuxiliaryResources(boolean)">setFilterExcludesAuxiliaryResources</a><wbr/>(boolean value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setFilterHidesIrrelevantElements(boolean)">setFilterHidesIrrelevantElements</a><wbr/>(boolean value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setFilterShowsImportedElements(boolean)">setFilterShowsImportedElements</a><wbr/>(boolean value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setGlobalPermission(boolean)">setGlobalPermission</a><wbr/>(boolean value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets package permission global property value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setHiddenBrowserTrees(java.util.Collection)">setHiddenBrowserTrees</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; trees)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setHideInformationFlowVisibility(boolean)">setHideInformationFlowVisibility</a><wbr/>(boolean hideInformationFlowVisibility)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setHighlightSuspended(boolean)">setHighlightSuspended</a><wbr/>(boolean highlight)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setIgnoredActiveSuites(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package%5B%5D)">setIgnoredActiveSuites</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a>[] elements)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setIgnoredDiagramAspects(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype%5B%5D)">setIgnoredDiagramAspects</a><wbr/>(<a href="../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>[] aspects)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setIgnoredDuplicatedModules(java.util.Collection)">setIgnoredDuplicatedModules</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setIgnoredPassiveValidationRules(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint%5B%5D)">setIgnoredPassiveValidationRules</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a>[] elements)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setIgnoredPassiveValidationSuites(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package%5B%5D)">setIgnoredPassiveValidationSuites</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a>[] elements)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setIgnoredValidationResults(java.lang.String%5B%5D)">setIgnoredValidationResults</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] ignoredPairs)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setIgnoredValidationRules(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint%5B%5D)">setIgnoredValidationRules</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a>[] elements)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setIgnoreStandardProfiles(boolean)">setIgnoreStandardProfiles</a><wbr/>(boolean value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets ignore standard profiles in dependency checking property.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setImageHeightLimit(java.lang.Integer)">setImageHeightLimit</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> imageHeightLimit)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setImageWidthLimit(java.lang.Integer)">setImageWidthLimit</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> imageWidthLimit)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setIndexMode(int)">setIndexMode</a><wbr/>(int status)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setIndexScope(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package%5B%5D)">setIndexScope</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a>[] scope)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setIndexScopeAll(boolean)">setIndexScopeAll</a><wbr/>(boolean all)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setIndexTypes(java.util.Collection)">setIndexTypes</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> types)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setInvisibleProperties(com.nomagic.magicdraw.properties.PropertyManager)">setInvisibleProperties</a><wbr/>(<a href="../../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> newManager)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#setLastDirectory(java.lang.String)">setLastDirectory</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> path)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../ProjectSpecificLocationRegister.html" title="class in com.nomagic.magicdraw.core"><code>ProjectSpecificLocationRegister</code></a> to store and retrieve this information</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLastSelectedElement(com.nomagic.magicdraw.uml.BaseElement)">setLastSelectedElement</a><wbr/>(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLastSelectedModulePath(java.lang.String)">setLastSelectedModulePath</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> path)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set last selected module path.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLastSelectedTransformationName(java.lang.String)">setLastSelectedTransformationName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLastSelectedTypeMapProfileDirection(boolean)">setLastSelectedTypeMapProfileDirection</a><wbr/>(boolean forward)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLastSelectedTypeMapProfileName(java.lang.String)">setLastSelectedTypeMapProfileName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLayoutBeforeExitFullScreen(java.lang.String)">setLayoutBeforeExitFullScreen</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> rez)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLayoutBeforeFullScreen(java.lang.String)">setLayoutBeforeFullScreen</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> rez)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLayoutScenarioDiagram(boolean)">setLayoutScenarioDiagram</a><wbr/>(boolean value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets to layout scenario diagram.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLayoutTemplateCreationMode(java.lang.String)">setLayoutTemplateCreationMode</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> newValue)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLockElementNumber(boolean)">setLockElementNumber</a><wbr/>(boolean value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set the value to lock element number</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLockFreeEditingEnabled(boolean)">setLockFreeEditingEnabled</a><wbr/>(boolean enabled)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Enables or disables lock free editing</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLocksFilterUsername(java.lang.String)">setLocksFilterUsername</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> userName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets Lock view filter user name</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setMarkInTreeAndDiagrams(boolean)">setMarkInTreeAndDiagrams</a><wbr/>(boolean mark)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setMinimalSeverityProducingPreCommitWarning(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral)">setMinimalSeverityProducingPreCommitWarning</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> literal)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets minimal severity which produces warning after pre-commit validation.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setMinimalSeverityProhibitingCommit(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral)">setMinimalSeverityProhibitingCommit</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> literal)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set minimal severity which prohibits commit after pre-commit validation.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setModelElementStyle(com.nomagic.magicdraw.properties.Style)">setModelElementStyle</a><wbr/>(<a href="../../properties/Style.html" title="class in com.nomagic.magicdraw.properties">Style</a> modelElementStyle)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets style for default property values for all uml entities.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setModulesDirectories(java.util.Collection)">setModulesDirectories</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; collection)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets project modules paths.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setPassiveValidationSeverity(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral)">setPassiveValidationSeverity</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> literal)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setPreCommitValidationExcludedScope(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element%5B%5D)">setPreCommitValidationExcludedScope</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>[] elements)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets elements, excluded from pre-commit validation.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setPreCommitValidationSuites(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package%5B%5D)">setPreCommitValidationSuites</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a>[] elements)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets validation suites for pre-commit validation.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setProject(com.nomagic.magicdraw.core.Project)">setProject</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set project for the options.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setProjectNotificationByConditions(java.lang.String,java.lang.String)">setProjectNotificationByConditions</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> pluginID,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> notification)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setPublicBranchSyncMode(com.nomagic.magicdraw.core.options.SyncMode)">setPublicBranchSyncMode</a><wbr/>(<a href="SyncMode.html" title="enum class in com.nomagic.magicdraw.core.options">SyncMode</a> syncMode)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Element hiding public branch synchronization mode.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#setQNameDisplayAbsolute(boolean)">setQNameDisplayAbsolute</a><wbr/>(boolean value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#setQNameDisplayStyle(java.lang.String)"><code>setQNameDisplayStyle(String)</code></a> instead.</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setQNameDisplayStyle(java.lang.String)">setQNameDisplayStyle</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> newValue)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the QNAME_DISPLAY_STYLE property value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setRecentlyOpenedWindowsIDs(java.util.List)">setRecentlyOpenedWindowsIDs</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; ids)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setRecentTypes(java.util.List)">setRecentTypes</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt; recentMetaclasses)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets last selected metaclass for type creation</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setReportExtensionIndex(int)">setReportExtensionIndex</a><wbr/>(int index)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSecretProperty(java.lang.String,java.lang.String)">setSecretProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets secret property (maps given key to given value) Secret properties are encrypted properties that are not
 available as plain text when project options are persisted to xml.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSeparateDecisionMergeAndJoinForkNotation(boolean)">setSeparateDecisionMergeAndJoinForkNotation</a><wbr/>(boolean separateDecisionMergeAndJoinForkNotation)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowDiagramAbbreviation(boolean)">setShowDiagramAbbreviation</a><wbr/>(boolean showDiagramAbbreviation)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set show diagram abbreviation option</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowDotNotationForAssociations(boolean)">setShowDotNotationForAssociations</a><wbr/>(boolean value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the SHOW_DOT_NOTATION_FOR_ASSOCIATIONS property value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setStyle(com.nomagic.magicdraw.properties.Style)">setStyle</a><wbr/>(<a href="../../properties/Style.html" title="class in com.nomagic.magicdraw.properties">Style</a> style)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets style that holds two properties manager - one for visible and user editable properties, other for
 invisible project properties.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSuspendAutoDisplayingOfLabels(boolean)">setSuspendAutoDisplayingOfLabels</a><wbr/>(boolean suspend)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSuspendAutoResizingOfShapes(boolean)">setSuspendAutoResizingOfShapes</a><wbr/>(boolean suspend)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setTimeLimitToBuild(java.lang.Integer)">setTimeLimitToBuild</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> timeLimitToBuild)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#setTipsStyle(int)">setTipsStyle</a><wbr/>(int st)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#setTooltipsStyle(com.nomagic.magicdraw.core.options.ProjectOptions.TooltipsStyleChoice)"><code>setTooltipsStyle(TooltipsStyleChoice)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setTooltipsStyle(com.nomagic.magicdraw.core.options.ProjectOptions.TooltipsStyleChoice)">setTooltipsStyle</a><wbr/>(<a href="ProjectOptions.TooltipsStyleChoice.html" title="enum class in com.nomagic.magicdraw.core.options">ProjectOptions.TooltipsStyleChoice</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets Tooltips Style property</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setTransformationDestination(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)">setTransformationDestination</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> destination)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setTransformationInPlace(boolean)">setTransformationInPlace</a><wbr/>(boolean inPlace)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setUniqueElementNumberScope(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element%5B%5D)">setUniqueElementNumberScope</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>[] elements)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set the Packages where AutoIds are to be unique</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setUnlockedElementRemovalInfo(java.util.Map)">setUnlockedElementRemovalInfo</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; unlockedElementRemovalInfo)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setUseDiagramInfoCustomMode(boolean)">setUseDiagramInfoCustomMode</a><wbr/>(boolean value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setUseDiagramsAspects(boolean)">setUseDiagramsAspects</a><wbr/>(boolean use)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setUseI18NTextInDiagrams(boolean)">setUseI18NTextInDiagrams</a><wbr/>(boolean value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set useI18N property for painting a text in diagrams</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setValidateOnlyActiveDiagrams(boolean)">setValidateOnlyActiveDiagrams</a><wbr/>(boolean validateOnlyActiveDiagrams)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setValidateOnlyLocallyChangedElementsPreCommit(boolean)">setValidateOnlyLocallyChangedElementsPreCommit</a><wbr/>(boolean validateOnlyLocallyChangedElements)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets value for the Validate Only Locally Changed Elements property in the pre-commit validation group.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setValidationIgnoredOption(java.lang.String)">setValidationIgnoredOption</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setXpdlImportLocation(java.lang.String)">setXpdlImportLocation</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> importLocation)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showDotNotationForAssociations()">showDotNotationForAssociations</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the SHOW_DOT_NOTATION_FOR_ASSOCIATIONS property value</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#updateBrowserAfterFilterChange()">updateBrowserAfterFilterChange</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Updates a <a href="../../ui/browser/Browser.html" title="class in com.nomagic.magicdraw.ui.browser"><code>Browser</code></a> after the filtering was done through
 the <em>GUI</em> element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#updateBrowserAfterFilterChange(java.util.function.Consumer)">updateBrowserAfterFilterChange</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function">Consumer</a>&lt;<a href="../../ui/browser/Browser.html" title="class in com.nomagic.magicdraw.ui.browser">Browser</a>&gt; savedStateBrowserConsumer)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Updates a <a href="../../ui/browser/Browser.html" title="class in com.nomagic.magicdraw.ui.browser"><code>Browser</code></a> after the filtering was done through
 the <em>GUI</em> element.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.MDElementImpl">Methods inherited from class com.nomagic.magicdraw.uml.MDElementImpl</h3>
<code>accept, addPropertyChangeListener, atInsert, canAdd, canAddChild, canAddChild, canAddInstance, canBeDeleted, canChangeParent, canDeleteChild, clone, compareTo, createSortKeys, dispose, firePropertyChange, generateID, getClassType, getCommandForAppending, getHumanName, getHumanType, getID, getName, getObjectParent, getProject, getProjectProvider, getResourceID, getSortKeys, hasListeners, isEditable, isParentOf, removeAllParents, removeAllPropertyChangeListeners, removePropertyChangeListener, setID, setProjectProvider, sGetID, toString</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.BaseElement">Methods inherited from interface com.nomagic.magicdraw.uml.<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></h3>
<code><a href="../../uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)">canAdd</a></code></div>
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
<section class="detail" id="OPTIONS_LOCK">
<h3>OPTIONS_LOCK</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">OPTIONS_LOCK</span></div>
<div class="block">Options lock event property name.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.OPTIONS_LOCK">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PROJECT_GENERAL_PROPERTIES">
<h3>PROJECT_GENERAL_PROPERTIES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">PROJECT_GENERAL_PROPERTIES</span></div>
<div class="block">The name of the manager that contains user editable properties in Project options dialog.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getManager(java.lang.String)"><code>getManager(String)</code></a></li>
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.PROJECT_GENERAL_PROPERTIES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PROJECT_INVISIBLE_PROPERTIES">
<h3>PROJECT_INVISIBLE_PROPERTIES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">PROJECT_INVISIBLE_PROPERTIES</span></div>
<div class="block">The name of the manager of not visible properties in Project options dialog.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getManager(java.lang.String)"><code>getManager(String)</code></a></li>
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.PROJECT_INVISIBLE_PROPERTIES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PERSONAL_INVISIBLE_PROPERTIES">
<h3>PERSONAL_INVISIBLE_PROPERTIES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">PERSONAL_INVISIBLE_PROPERTIES</span></div>
<div class="block">The name of the manager of not visible properties that affect only one
 user in multi-user environment.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getManager(java.lang.String)"><code>getManager(String)</code></a></li>
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.PERSONAL_INVISIBLE_PROPERTIES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PERSONAL_VISIBLE_PROPERTIES">
<h3>PERSONAL_VISIBLE_PROPERTIES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">PERSONAL_VISIBLE_PROPERTIES</span></div>
<div class="block">The name of the manager of visible properties that affect only one
 user in multi-user environment</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.PERSONAL_VISIBLE_PROPERTIES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="STYLE_USER_PROPERTIES">
<h3>STYLE_USER_PROPERTIES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">STYLE_USER_PROPERTIES</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.STYLE_USER_PROPERTIES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="STYLE_PERSONAL_PROPERTIES">
<h3>STYLE_PERSONAL_PROPERTIES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">STYLE_PERSONAL_PROPERTIES</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.STYLE_PERSONAL_PROPERTIES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="STYLE_DIAGRAM_PROPERTIES">
<h3>STYLE_DIAGRAM_PROPERTIES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">STYLE_DIAGRAM_PROPERTIES</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.STYLE_DIAGRAM_PROPERTIES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="STYLE_MODEL_ELEMENT_DEFAULTS">
<h3>STYLE_MODEL_ELEMENT_DEFAULTS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">STYLE_MODEL_ELEMENT_DEFAULTS</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.STYLE_MODEL_ELEMENT_DEFAULTS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ACTIVE_VALIDATION_GROUP">
<h3>ACTIVE_VALIDATION_GROUP</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ACTIVE_VALIDATION_GROUP</span></div>
<div class="block">Real time validation group name</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.ACTIVE_VALIDATION_GROUP">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="VALIDATION_GROUP">
<h3>VALIDATION_GROUP</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">VALIDATION_GROUP</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.VALIDATION_GROUP">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PRE_COMMIT_VALIDATION_GROUP">
<h3>PRE_COMMIT_VALIDATION_GROUP</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">PRE_COMMIT_VALIDATION_GROUP</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.PRE_COMMIT_VALIDATION_GROUP">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="COMPOSITION_INSPECTION_GROUP">
<h3>COMPOSITION_INSPECTION_GROUP</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">COMPOSITION_INSPECTION_GROUP</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.COMPOSITION_INSPECTION_GROUP">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DIAGRAM_ASPECTS_GROUP">
<h3>DIAGRAM_ASPECTS_GROUP</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DIAGRAM_ASPECTS_GROUP</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.DIAGRAM_ASPECTS_GROUP">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="COMPLETE_DIAGRAMS">
<h3>COMPLETE_DIAGRAMS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">COMPLETE_DIAGRAMS</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.COMPLETE_DIAGRAMS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="EXPORT">
<h3>EXPORT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">EXPORT</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.EXPORT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CREATE_AUTOMATICALLY">
<h3>CREATE_AUTOMATICALLY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">CREATE_AUTOMATICALLY</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.CREATE_AUTOMATICALLY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DO_NOT_CREATE">
<h3>DO_NOT_CREATE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DO_NOT_CREATE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.DO_NOT_CREATE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DIAGRAM_CONTEXT_MODES">
<h3>DIAGRAM_CONTEXT_MODES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></span> <span class="element-name">DIAGRAM_CONTEXT_MODES</span></div>
</section>
</li>
<li>
<section class="detail" id="COLLABORATION_GROUP">
<h3>COLLABORATION_GROUP</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">COLLABORATION_GROUP</span></div>
<div class="block">Collaboration group name</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.COLLABORATION_GROUP">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ELEMENT_HIDING_GROUP">
<h3>ELEMENT_HIDING_GROUP</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ELEMENT_HIDING_GROUP</span></div>
<div class="block">Element hiding group name</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.ELEMENT_HIDING_GROUP">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LOCKING_GROUP">
<h3>LOCKING_GROUP</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">LOCKING_GROUP</span></div>
<div class="block">Locking group name</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.LOCKING_GROUP">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DEPENDENCY_CHECKER_GROUP">
<h3>DEPENDENCY_CHECKER_GROUP</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DEPENDENCY_CHECKER_GROUP</span></div>
<div class="block">Dependency checker group name.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.DEPENDENCY_CHECKER_GROUP">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="QNAME_DISPLAY_STYLE_ABSOLUTE">
<h3>QNAME_DISPLAY_STYLE_ABSOLUTE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">QNAME_DISPLAY_STYLE_ABSOLUTE</span></div>
<div class="block">Qualified is calculated using named elements up to the project root - "Data"</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.QNAME_DISPLAY_STYLE_ABSOLUTE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="QNAME_DISPLAY_STYLE_RELATIVE">
<h3>QNAME_DISPLAY_STYLE_RELATIVE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">QNAME_DISPLAY_STYLE_RELATIVE</span></div>
<div class="block">Qualified is calculated using named elements up to the nearest package with applied stereotype "ModelLibrary"</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.QNAME_DISPLAY_STYLE_RELATIVE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="QNAME_DISPLAY_STYLE_MODEL_RELATIVE">
<h3>QNAME_DISPLAY_STYLE_MODEL_RELATIVE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">QNAME_DISPLAY_STYLE_MODEL_RELATIVE</span></div>
<div class="block">Qualified is calculated using named elements up to the nearest "Model" element</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.QNAME_DISPLAY_STYLE_MODEL_RELATIVE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="QNAME_DISPLAY_STYLE_MODEL_OR_LIBRARY_RELATIVE">
<h3>QNAME_DISPLAY_STYLE_MODEL_OR_LIBRARY_RELATIVE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">QNAME_DISPLAY_STYLE_MODEL_OR_LIBRARY_RELATIVE</span></div>
<div class="block">Qualified is calculated using named elements up to the nearest "Model" element or package with applied stereotype
 "ModelLibrary"</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.QNAME_DISPLAY_STYLE_MODEL_OR_LIBRARY_RELATIVE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="QNAME_DISPLAY_STYLE_OPTIONS">
<h3>QNAME_DISPLAY_STYLE_OPTIONS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></span> <span class="element-name">QNAME_DISPLAY_STYLE_OPTIONS</span></div>
<div class="block">Collection of all possible qualified name display style modes.</div>
</section>
</li>
<li>
<section class="detail" id="LAYOUT_TEMPLATE_CREATION_MODE_USAGE">
<h3>LAYOUT_TEMPLATE_CREATION_MODE_USAGE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">LAYOUT_TEMPLATE_CREATION_MODE_USAGE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.LAYOUT_TEMPLATE_CREATION_MODE_USAGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LAYOUT_TEMPLATE_CREATION_MODE_DEFINITION">
<h3>LAYOUT_TEMPLATE_CREATION_MODE_DEFINITION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">LAYOUT_TEMPLATE_CREATION_MODE_DEFINITION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.LAYOUT_TEMPLATE_CREATION_MODE_DEFINITION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LAYOUT_TEMPLATE_CREATION_MODES">
<h3>LAYOUT_TEMPLATE_CREATION_MODES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></span> <span class="element-name">LAYOUT_TEMPLATE_CREATION_MODES</span></div>
</section>
</li>
<li>
<section class="detail" id="NUMBERING_GROUP">
<h3>NUMBERING_GROUP</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">NUMBERING_GROUP</span></div>
<div class="block">Numbering group name.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.NUMBERING_GROUP">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="BROWSER_GROUP">
<h3>BROWSER_GROUP</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">BROWSER_GROUP</span></div>
<div class="block">Browser group</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.BROWSER_GROUP">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DIAGRAMS_GROUP">
<h3>DIAGRAMS_GROUP</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DIAGRAMS_GROUP</span></div>
<div class="block">Diagrams group name</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.DIAGRAMS_GROUP">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="GENERAL_GROUP">
<h3>GENERAL_GROUP</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">GENERAL_GROUP</span></div>
<div class="block">General group name</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.GENERAL_GROUP">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="UNIQUE_ELEMENT_NUMBER_PROJECT_SCOPE">
<h3>UNIQUE_ELEMENT_NUMBER_PROJECT_SCOPE</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">UNIQUE_ELEMENT_NUMBER_PROJECT_SCOPE</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">option no longer exists</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.UNIQUE_ELEMENT_NUMBER_PROJECT_SCOPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="UNIQUE_ELEMENT_NUMBER_PACKAGE_SCOPE">
<h3>UNIQUE_ELEMENT_NUMBER_PACKAGE_SCOPE</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">UNIQUE_ELEMENT_NUMBER_PACKAGE_SCOPE</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">option no longer exists</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.UNIQUE_ELEMENT_NUMBER_PACKAGE_SCOPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="UNIQUE_ELEMENT_NUMBER_SCOPE_OPTIONS">
<h3>UNIQUE_ELEMENT_NUMBER_SCOPE_OPTIONS</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></span> <span class="element-name">UNIQUE_ELEMENT_NUMBER_SCOPE_OPTIONS</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">options no longer exists</div>
</div>
</section>
</li>
<li>
<section class="detail" id="NO_TIPS">
<h3>NO_TIPS</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">NO_TIPS</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Tool tips style constant. No tooltip is displayed if mouse cursor is over PresentationElement in diagram.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.NO_TIPS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="NAME_TIPS">
<h3>NAME_TIPS</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">NAME_TIPS</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Tool tips style constant. Name as tooltip is displayed if mouse cursor is over PresentationElement in diagram.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.NAME_TIPS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DOC_TIPS">
<h3>DOC_TIPS</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">DOC_TIPS</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Tool tips style constant. Model element documentation as tooltip is displayed if mouse cursor is over
 PresentationElement in diagram.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.DOC_TIPS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="INDEX_NONE">
<h3>INDEX_NONE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">INDEX_NONE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.INDEX_NONE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="INDEX_COMMON">
<h3>INDEX_COMMON</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">INDEX_COMMON</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.INDEX_COMMON">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="INDEX_CUSTOM">
<h3>INDEX_CUSTOM</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">INDEX_CUSTOM</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.INDEX_CUSTOM">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="COMPOSITION_INSPECTION_SEVERITY_STANDARD">
<h3>COMPOSITION_INSPECTION_SEVERITY_STANDARD</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">COMPOSITION_INSPECTION_SEVERITY_STANDARD</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.COMPOSITION_INSPECTION_SEVERITY_STANDARD">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="COMPOSITION_INSPECTION_SEVERITY_ADVANCED">
<h3>COMPOSITION_INSPECTION_SEVERITY_ADVANCED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">COMPOSITION_INSPECTION_SEVERITY_ADVANCED</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ProjectOptions.COMPOSITION_INSPECTION_SEVERITY_ADVANCED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="COMPOSITION_INSPECTION_SEVERITY_CHOICE">
<h3>COMPOSITION_INSPECTION_SEVERITY_CHOICE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">COMPOSITION_INSPECTION_SEVERITY_CHOICE</span></div>
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
<section class="detail" id="&lt;init&gt;()">
<h3>ProjectOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ProjectOptions</span>()</div>
<div class="block">Constructor. Creates project options with initialized defaults.
 Use this constructor when compatibility properties converting should be performed.</div>
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
<section class="detail" id="remapGroupInUI(java.util.Collection,com.nomagic.magicdraw.core.options.Group)">
<h3>remapGroupInUI</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">remapGroupInUI</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; groupsToRemap,
 <a href="Group.html" title="class in com.nomagic.magicdraw.core.options">Group</a> newGroup)</span></div>
<div class="block">Remap properties group to a some other group in options UI</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>groupsToRemap</code> - groups to remap</dd>
<dd><code>newGroup</code> - new group</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getGroupRemap()">
<h3>getGroupRemap</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;,<wbr/><a href="Group.html" title="class in com.nomagic.magicdraw.core.options">Group</a>&gt;</span> <span class="element-name">getGroupRemap</span>()</div>
</section>
</li>
<li>
<section class="detail" id="createDefaultProjectOptions(com.nomagic.magicdraw.core.Project)">
<h3>createDefaultProjectOptions</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="ProjectOptions.html" title="class in com.nomagic.magicdraw.core.options">ProjectOptions</a></span> <span class="element-name">createDefaultProjectOptions</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Create default options for a given project</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dt>Returns:</dt>
<dd>options with default settings</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setProject(com.nomagic.magicdraw.core.Project)">
<h3>setProject</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setProject</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Set project for the options.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDefaults()">
<h3>setDefaults</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDefaults</span>()</div>
<div class="block">Sets default project options.</div>
</section>
</li>
<li>
<section class="detail" id="getStyle()">
<h3>getStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../properties/Style.html" title="class in com.nomagic.magicdraw.properties">Style</a></span> <span class="element-name">getStyle</span>()</div>
<div class="block">Gets style that holds two properties manager - one for visible and user editable properties, other for
 invisible project properties.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>project properties</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setStyle(com.nomagic.magicdraw.properties.Style)">
<h3>setStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setStyle</span><wbr/><span class="parameters">(<a href="../../properties/Style.html" title="class in com.nomagic.magicdraw.properties">Style</a> style)</span></div>
<div class="block">Sets style that holds two properties manager - one for visible and user editable properties, other for
 invisible project properties.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>style</code> - project properties</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPersonalOptionsStyle()">
<h3>getPersonalOptionsStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../properties/Style.html" title="class in com.nomagic.magicdraw.properties">Style</a></span> <span class="element-name">getPersonalOptionsStyle</span>()</div>
<div class="block">Gets personalOptionsStyle from the ProjectOptions. Personal options are GUI setting that
 are user specific in multiple user env.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Style object</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramViewStyle()">
<h3>getDiagramViewStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../properties/Style.html" title="class in com.nomagic.magicdraw.properties">Style</a></span> <span class="element-name">getDiagramViewStyle</span>()</div>
<div class="block">Gets diagramViewStyle from the ProjectOptions. Personal options are GUI setting that
 are user specific in multiple user env.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Style object</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSymbolStyles()">
<h3>getSymbolStyles</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../properties/StyleManager.html" title="class in com.nomagic.magicdraw.properties">StyleManager</a></span> <span class="element-name">getSymbolStyles</span>()</div>
<div class="block">Gets symbol style manager.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>symbol style manager.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="configureLoadedOptions(com.nomagic.magicdraw.core.options.ProjectOptions)">
<h3>configureLoadedOptions</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">configureLoadedOptions</span><wbr/><span class="parameters">(<a href="ProjectOptions.html" title="class in com.nomagic.magicdraw.core.options">ProjectOptions</a> options)</span></div>
</section>
</li>
<li>
<section class="detail" id="addModuleDirectory(java.lang.String)">
<h3>addModuleDirectory</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addModuleDirectory</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> directory)</span></div>
<div class="block">Adds directory to project module directories.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>directory</code> - directory to add.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="checkAndAddModuleDirectory(java.lang.String)">
<h3>checkAndAddModuleDirectory</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">checkAndAddModuleDirectory</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> directory)</span></div>
<div class="block">Adds directory to project module directories if it was not added yet</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>directory</code> - directory to add.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setModulesDirectories(java.util.Collection)">
<h3>setModulesDirectories</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setModulesDirectories</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; collection)</span></div>
<div class="block">Sets project modules paths.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>collection</code> - collections of String objects specifying paths to module directories.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getModulesDirectories(boolean)">
<h3>getModulesDirectories</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getModulesDirectories</span><wbr/><span class="parameters">(boolean resolvePathVariables)</span></div>
<div class="block">Returns modules paths.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>resolvePathVariables</code> - true if path variables must be resolved (real paths returned)</dd>
<dt>Returns:</dt>
<dd>list of String objects file paths to module dirs.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTipsStyle(int)">
<h3>setTipsStyle</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTipsStyle</span><wbr/><span class="parameters">(int st)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#setTooltipsStyle(com.nomagic.magicdraw.core.options.ProjectOptions.TooltipsStyleChoice)"><code>setTooltipsStyle(TooltipsStyleChoice)</code></a></div>
</div>
<div class="block">Set tooltips style.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>st</code> - tips style constant.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTipsStyle()">
<h3>getTipsStyle</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getTipsStyle</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#getTooltipsStyle()"><code>getTooltipsStyle()</code></a></div>
</div>
<div class="block">Get tooltips style.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>tooltip style constant.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="accept(com.nomagic.magicdraw.uml.Visitor)">
<h3>accept</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">accept</span><wbr/><span class="parameters">(<a href="../../uml/Visitor.html" title="class in com.nomagic.magicdraw.uml">Visitor</a> v)</span>
            throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../../uml/MDElement.html#accept(com.nomagic.magicdraw.uml.Visitor)">MDElement</a></code></span></div>
<div class="block">Method accepts visitor, and calls method visit&lt;class name&gt;(this) of visitor .
 See Visitor pattern for more details.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../uml/MDElement.html#accept(com.nomagic.magicdraw.uml.Visitor)">accept</a></code> in interface <code><a href="../../uml/MDElement.html" title="interface in com.nomagic.magicdraw.uml">MDElement</a></code></dd>
<dt>Overrides:</dt>
<dd><code>accept</code> in class <code>com.nomagic.magicdraw.uml.MDElementImpl</code></dd>
<dt>Parameters:</dt>
<dd><code>v</code> - which visits this element.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="propertyChange(java.beans.PropertyChangeEvent)">
<h3>propertyChange</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">propertyChange</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans">PropertyChangeEvent</a> evt)</span></div>
<div class="block">Listens for property change event.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html#propertyChange(java.beans.PropertyChangeEvent)" title="class or interface in java.beans">propertyChange</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateBrowserAfterFilterChange()">
<h3>updateBrowserAfterFilterChange</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">updateBrowserAfterFilterChange</span>()</div>
<div class="block">Updates a <a href="../../ui/browser/Browser.html" title="class in com.nomagic.magicdraw.ui.browser"><code>Browser</code></a> after the filtering was done through
 the <em>GUI</em> element.
 <p></p>Method does save the state of <a href="../../ui/browser/BrowserTabTree.html" title="class in com.nomagic.magicdraw.ui.browser"><code>trees</code></a>
 and restores it before returning from a call.</div>
</section>
</li>
<li>
<section class="detail" id="updateBrowserAfterFilterChange(java.util.function.Consumer)">
<h3>updateBrowserAfterFilterChange</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">updateBrowserAfterFilterChange</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function">Consumer</a>&lt;<a href="../../ui/browser/Browser.html" title="class in com.nomagic.magicdraw.ui.browser">Browser</a>&gt; savedStateBrowserConsumer)</span></div>
<div class="block">Updates a <a href="../../ui/browser/Browser.html" title="class in com.nomagic.magicdraw.ui.browser"><code>Browser</code></a> after the filtering was done through
 the <em>GUI</em> element.
 <p></p>Method does save the state of <a href="../../ui/browser/BrowserTabTree.html" title="class in com.nomagic.magicdraw.ui.browser"><code>trees</code></a>
 and restores it before returning from a call.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>savedStateBrowserConsumer</code> - an implementation of <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function"><code>Consumer</code></a>
                                  that accepts a <a href="../../ui/browser/Browser.html" title="class in com.nomagic.magicdraw.ui.browser"><code>Browser</code></a> whose state
                                  was already saved.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setBrowserItemsTypes(java.util.Collection)">
<h3>setBrowserItemsTypes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setBrowserItemsTypes</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> v)</span></div>
<div class="block">Set types that are filtered (not shown) in browser.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>v</code> - collection of String objects short name of class type (something like <code>ClassTypes.getShortName(Actor.class)</code>).</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBrowserItemsTypes()">
<h3>getBrowserItemsTypes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></span> <span class="element-name">getBrowserItemsTypes</span>()</div>
<div class="block">Gets types that are filtered (not shown) in browser.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>collection of String objects short name of class type (something like <code>ClassTypes.getShortName(Actor.class)</code>).</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setBrowserVisible(boolean)">
<h3>setBrowserVisible</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setBrowserVisible</span><wbr/><span class="parameters">(boolean v)</span></div>
<div class="block">Set browser visibility flag</div>
</section>
</li>
<li>
<section class="detail" id="isBrowserVisible()">
<h3>isBrowserVisible</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isBrowserVisible</span>()</div>
<div class="block">Gets browser visibility flag</div>
</section>
</li>
<li>
<section class="detail" id="setChoosePackageLastSelection(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)">
<h3>setChoosePackageLastSelection</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setChoosePackageLastSelection</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> pck)</span></div>
</section>
</li>
<li>
<section class="detail" id="getChoosePackageLastSelection()">
<h3>getChoosePackageLastSelection</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a></span> <span class="element-name">getChoosePackageLastSelection</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setDisableHighlightSuspended(java.util.Collection)">
<h3>setDisableHighlightSuspended</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDisableHighlightSuspended</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt; elements)</span></div>
</section>
</li>
<li>
<section class="detail" id="getDisableHighlightSuspended()">
<h3>getDisableHighlightSuspended</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;</span> <span class="element-name">getDisableHighlightSuspended</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getManager(java.lang.String)">
<h3>getManager</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a></span> <span class="element-name">getManager</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Returns the manager for properties.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>property manager name.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#PROJECT_GENERAL_PROPERTIES"><code>PROJECT_GENERAL_PROPERTIES</code></a></li>
<li><a href="#PROJECT_INVISIBLE_PROPERTIES"><code>PROJECT_INVISIBLE_PROPERTIES</code></a></li>
<li><a href="#PERSONAL_INVISIBLE_PROPERTIES"><code>PERSONAL_INVISIBLE_PROPERTIES</code></a></li>
<li><a href="#PERSONAL_VISIBLE_PROPERTIES"><code>PERSONAL_VISIBLE_PROPERTIES</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProperty(java.lang.String,java.lang.String)">
<h3>getProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../properties/Property.html" title="class in com.nomagic.magicdraw.properties">Property</a></span> <span class="element-name">getProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> manager,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</span></div>
<div class="block">Returns property</div>
</section>
</li>
<li>
<section class="detail" id="addProperty(java.lang.String,com.nomagic.magicdraw.properties.Property)">
<h3>addProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> manager,
 <a href="../../properties/Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> p)</span></div>
<div class="block">Adds property</div>
</section>
</li>
<li>
<section class="detail" id="getRecentlyOpenedWindowsIDs()">
<h3>getRecentlyOpenedWindowsIDs</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getRecentlyOpenedWindowsIDs</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setRecentlyOpenedWindowsIDs(java.util.List)">
<h3>setRecentlyOpenedWindowsIDs</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRecentlyOpenedWindowsIDs</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; ids)</span></div>
</section>
</li>
<li>
<section class="detail" id="setBrowserLayout(java.lang.String)">
<h3>setBrowserLayout</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setBrowserLayout</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> rez)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>rez</code> - browser layout value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBrowserLayout()">
<h3>getBrowserLayout</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getBrowserLayout</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setDiagramsLayout(java.lang.String)">
<h3>setDiagramsLayout</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDiagramsLayout</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> rez)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#setEditorWindowsLayout(java.lang.String)"><code>setEditorWindowsLayout(String)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="setEditorWindowsLayout(java.lang.String)">
<h3>setEditorWindowsLayout</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setEditorWindowsLayout</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> rez)</span></div>
</section>
</li>
<li>
<section class="detail" id="getDiagramsLayout()">
<h3>getDiagramsLayout</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDiagramsLayout</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#getEditorWindowsLayout()"><code>getEditorWindowsLayout()</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="getEditorWindowsLayout()">
<h3>getEditorWindowsLayout</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getEditorWindowsLayout</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setProjectNotificationByConditions(java.lang.String,java.lang.String)">
<h3>setProjectNotificationByConditions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setProjectNotificationByConditions</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> pluginID,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> notification)</span></div>
</section>
</li>
<li>
<section class="detail" id="getProjectNotificationsByConditions()">
<h3>getProjectNotificationsByConditions</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getProjectNotificationsByConditions</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setRecentTypes(java.util.List)">
<h3>setRecentTypes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRecentTypes</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt; recentMetaclasses)</span></div>
<div class="block">Sets last selected metaclass for type creation</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>recentMetaclasses</code> - recent metaclasses</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRecentTypes()">
<h3>getRecentTypes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;</span> <span class="element-name">getRecentTypes</span>()</div>
<div class="block">Returns recent metaclasses for created types</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>recent metaclass list</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setLayoutBeforeFullScreen(java.lang.String)">
<h3>setLayoutBeforeFullScreen</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLayoutBeforeFullScreen</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> rez)</span></div>
</section>
</li>
<li>
<section class="detail" id="setLayoutBeforeExitFullScreen(java.lang.String)">
<h3>setLayoutBeforeExitFullScreen</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLayoutBeforeExitFullScreen</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> rez)</span></div>
</section>
</li>
<li>
<section class="detail" id="getLayoutBeforeFullScreen()">
<h3>getLayoutBeforeFullScreen</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getLayoutBeforeFullScreen</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getLayoutBeforeExitFullScreen()">
<h3>getLayoutBeforeExitFullScreen</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getLayoutBeforeExitFullScreen</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setExitFullScreenToolbarBounds(java.awt.Rectangle)">
<h3>setExitFullScreenToolbarBounds</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setExitFullScreenToolbarBounds</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> bounds)</span></div>
<div class="block">Sets full screen toolbar bounds.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>bounds</code> - new bounds.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getExitFullScreenToolbarBounds()">
<h3>getExitFullScreenToolbarBounds</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></span> <span class="element-name">getExitFullScreenToolbarBounds</span>()</div>
<div class="block">Getter for browser bounds.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>browser bounds.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAdditionalBrowserTrees()">
<h3>getAdditionalBrowserTrees</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getAdditionalBrowserTrees</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setAdditionalBrowserTrees(java.util.Collection)">
<h3>setAdditionalBrowserTrees</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAdditionalBrowserTrees</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; trees)</span></div>
</section>
</li>
<li>
<section class="detail" id="getHiddenBrowserTrees()">
<h3>getHiddenBrowserTrees</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getHiddenBrowserTrees</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setHiddenBrowserTrees(java.util.Collection)">
<h3>setHiddenBrowserTrees</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setHiddenBrowserTrees</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; trees)</span></div>
</section>
</li>
<li>
<section class="detail" id="addHiddenBrowserTree(java.lang.String)">
<h3>addHiddenBrowserTree</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addHiddenBrowserTree</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> treeID)</span></div>
</section>
</li>
<li>
<section class="detail" id="removeHiddenBrowserTree(java.lang.String)">
<h3>removeHiddenBrowserTree</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeHiddenBrowserTree</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> treeID)</span></div>
</section>
</li>
<li>
<section class="detail" id="setUseDiagramInfoCustomMode(boolean)">
<h3>setUseDiagramInfoCustomMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setUseDiagramInfoCustomMode</span><wbr/><span class="parameters">(boolean value)</span></div>
</section>
</li>
<li>
<section class="detail" id="isUseDiagramInfoCustomMode()">
<h3>isUseDiagramInfoCustomMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isUseDiagramInfoCustomMode</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setExportedVersionChanged(boolean)">
<h3>setExportedVersionChanged</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setExportedVersionChanged</span><wbr/><span class="parameters">(boolean value)</span></div>
</section>
</li>
<li>
<section class="detail" id="isExportedVersionChanged()">
<h3>isExportedVersionChanged</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isExportedVersionChanged</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setDiagramInfoCustomHTML(java.lang.String)">
<h3>setDiagramInfoCustomHTML</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDiagramInfoCustomHTML</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="getDiagramInfoCustomHTML()">
<h3>getDiagramInfoCustomHTML</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDiagramInfoCustomHTML</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setDiagramInfoKeywords(java.util.Collection)">
<h3>setDiagramInfoKeywords</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDiagramInfoKeywords</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; keywords)</span></div>
</section>
</li>
<li>
<section class="detail" id="getDiagramInfoKeywords()">
<h3>getDiagramInfoKeywords</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getDiagramInfoKeywords</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setSecretProperty(java.lang.String,java.lang.String)">
<h3>setSecretProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSecretProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div class="block">Sets secret property (maps given key to given value) Secret properties are encrypted properties that are not
 available as plain text when project options are persisted to xml.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>key</code> - key for the property.</dd>
<dd><code>value</code> - value of the property.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSecretProperty(java.lang.String)">
<h3>getSecretProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getSecretProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key)</span></div>
<div class="block">Retrieves secret property value according given key. Secret properties are encrypted properties that are not
 available as plain text when project options are persisted to xml.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>key</code> - key of the property.</dd>
<dt>Returns:</dt>
<dd>property value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setInvisibleProperties(com.nomagic.magicdraw.properties.PropertyManager)">
<h3>setInvisibleProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setInvisibleProperties</span><wbr/><span class="parameters">(<a href="../../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> newManager)</span></div>
</section>
</li>
<li>
<section class="detail" id="setLastSelectedTransformationName(java.lang.String)">
<h3>setLastSelectedTransformationName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLastSelectedTransformationName</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
</section>
</li>
<li>
<section class="detail" id="getLastSelectedTransformationName()">
<h3>getLastSelectedTransformationName</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getLastSelectedTransformationName</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setTransformationDestination(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)">
<h3>setTransformationDestination</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTransformationDestination</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> destination)</span></div>
</section>
</li>
<li>
<section class="detail" id="getTransformationDestination()">
<h3>getTransformationDestination</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a></span> <span class="element-name">getTransformationDestination</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setLastSelectedTypeMapProfileName(java.lang.String)">
<h3>setLastSelectedTypeMapProfileName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLastSelectedTypeMapProfileName</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
</section>
</li>
<li>
<section class="detail" id="getLastSelectedTypeMapProfileName()">
<h3>getLastSelectedTypeMapProfileName</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getLastSelectedTypeMapProfileName</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setLastSelectedTypeMapProfileDirection(boolean)">
<h3>setLastSelectedTypeMapProfileDirection</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLastSelectedTypeMapProfileDirection</span><wbr/><span class="parameters">(boolean forward)</span></div>
</section>
</li>
<li>
<section class="detail" id="getLastSelectedTypeMapProfileDirection()">
<h3>getLastSelectedTypeMapProfileDirection</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">getLastSelectedTypeMapProfileDirection</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setTransformationInPlace(boolean)">
<h3>setTransformationInPlace</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTransformationInPlace</span><wbr/><span class="parameters">(boolean inPlace)</span></div>
</section>
</li>
<li>
<section class="detail" id="isTransformationInPlace()">
<h3>isTransformationInPlace</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isTransformationInPlace</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setLastSelectedElement(com.nomagic.magicdraw.uml.BaseElement)">
<h3>setLastSelectedElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLastSelectedElement</span><wbr/><span class="parameters">(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getLastSelectedElement()">
<h3>getLastSelectedElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></span> <span class="element-name">getLastSelectedElement</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setIndexMode(int)">
<h3>setIndexMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setIndexMode</span><wbr/><span class="parameters">(int status)</span></div>
</section>
</li>
<li>
<section class="detail" id="getIndexMode()">
<h3>getIndexMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getIndexMode</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setIndexScopeAll(boolean)">
<h3>setIndexScopeAll</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setIndexScopeAll</span><wbr/><span class="parameters">(boolean all)</span></div>
</section>
</li>
<li>
<section class="detail" id="isIndexScopeAll()">
<h3>isIndexScopeAll</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isIndexScopeAll</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setIndexScope(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package[])">
<h3>setIndexScope</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setIndexScope</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a>[] scope)</span></div>
</section>
</li>
<li>
<section class="detail" id="getIndexScope()">
<h3>getIndexScope</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a>[]</span> <span class="element-name">getIndexScope</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setIndexTypes(java.util.Collection)">
<h3>setIndexTypes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setIndexTypes</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> types)</span></div>
</section>
</li>
<li>
<section class="detail" id="getIndexTypes()">
<h3>getIndexTypes</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></span> <span class="element-name">getIndexTypes</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setLastDirectory(java.lang.String)">
<h3>setLastDirectory</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLastDirectory</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> path)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../ProjectSpecificLocationRegister.html" title="class in com.nomagic.magicdraw.core"><code>ProjectSpecificLocationRegister</code></a> to store and retrieve this information</div>
</div>
<div class="block">Sets the last used project related directory.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>path</code> - last dir path.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getReportExtensionIndex()">
<h3>getReportExtensionIndex</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getReportExtensionIndex</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setReportExtensionIndex(int)">
<h3>setReportExtensionIndex</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setReportExtensionIndex</span><wbr/><span class="parameters">(int index)</span></div>
</section>
</li>
<li>
<section class="detail" id="getLastDirectory()">
<h3>getLastDirectory</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getLastDirectory</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../ProjectSpecificLocationRegister.html" title="class in com.nomagic.magicdraw.core"><code>ProjectSpecificLocationRegister</code></a> to store and retrieve this information</div>
</div>
<div class="block">Returns the last used project related directory.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the path</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addInvisibleProperty(com.nomagic.magicdraw.properties.Property)">
<h3>addInvisibleProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addInvisibleProperty</span><wbr/><span class="parameters">(<a href="../../properties/Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> property)</span></div>
<div class="block">Adds invisible property that affects all users in multi user environment.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>property</code> - property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInvisibleProperty(java.lang.String)">
<h3>getInvisibleProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../properties/Property.html" title="class in com.nomagic.magicdraw.properties">Property</a></span> <span class="element-name">getInvisibleProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</span></div>
<div class="block">Gets invisible property that affects all users in multi user environment.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - property identifier</dd>
<dt>Returns:</dt>
<dd>invisible property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addPersonalVisibleProperty(com.nomagic.magicdraw.properties.Property)">
<h3>addPersonalVisibleProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addPersonalVisibleProperty</span><wbr/><span class="parameters">(<a href="../../properties/Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> property)</span></div>
<div class="block">Adds personal visible property that affects one user in multi user environment</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>property</code> - property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPersonalVisibleProperty(java.lang.String)">
<h3>getPersonalVisibleProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../properties/Property.html" title="class in com.nomagic.magicdraw.properties">Property</a></span> <span class="element-name">getPersonalVisibleProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</span></div>
<div class="block">Gets personal visible property that affects one user in multi user environment</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - property identifier</dd>
<dt>Returns:</dt>
<dd>personal visible property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addConfigurator(com.nomagic.magicdraw.core.options.ProjectOptionsConfigurator)">
<h3>addConfigurator</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">addConfigurator</span><wbr/><span class="parameters">(<a href="ProjectOptionsConfigurator.html" title="interface in com.nomagic.magicdraw.core.options">ProjectOptionsConfigurator</a> configurator)</span></div>
<div class="block">Add project options configurator</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - options configurator.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeConfigurator(com.nomagic.magicdraw.core.options.ProjectOptionsConfigurator)">
<h3>removeConfigurator</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">removeConfigurator</span><wbr/><span class="parameters">(<a href="ProjectOptionsConfigurator.html" title="interface in com.nomagic.magicdraw.core.options">ProjectOptionsConfigurator</a> configurator)</span></div>
<div class="block">Remove project options configurator</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - options configurator.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setModelElementStyle(com.nomagic.magicdraw.properties.Style)">
<h3>setModelElementStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setModelElementStyle</span><wbr/><span class="parameters">(<a href="../../properties/Style.html" title="class in com.nomagic.magicdraw.properties">Style</a> modelElementStyle)</span></div>
<div class="block">Sets style for default property values for all uml entities.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>modelElementStyle</code> - style</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="applyModifiedModelElementStyle(com.nomagic.magicdraw.properties.Style)">
<h3>applyModifiedModelElementStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">applyModifiedModelElementStyle</span><wbr/><span class="parameters">(<a href="../../properties/Style.html" title="class in com.nomagic.magicdraw.properties">Style</a> modelElementStyle)</span></div>
<div class="block">Applies user modified values to model element style</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>modelElementStyle</code> - style to retrieve modified values from</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFullModelElementStyle()">
<h3>getFullModelElementStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../properties/Style.html" title="class in com.nomagic.magicdraw.properties">Style</a></span> <span class="element-name">getFullModelElementStyle</span>()</div>
<div class="block">Returns default model element values with modified values. Method is useful for full review of values.
 <p>
 Does not return actual project model element style, used for review purposes.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>all modified values and all unchanged</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getActualModelElementStyle()">
<h3>getActualModelElementStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../properties/Style.html" title="class in com.nomagic.magicdraw.properties">Style</a></span> <span class="element-name">getActualModelElementStyle</span>()</div>
<div class="block">Fast method. Returns default model element values.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>all modified values and some unmodified (unmodified values are not filtered)</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getModifiedModelElementsStyle()">
<h3>getModifiedModelElementsStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../properties/Style.html" title="class in com.nomagic.magicdraw.properties">Style</a></span> <span class="element-name">getModifiedModelElementsStyle</span>()</div>
<div class="block">Returns default model element values.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>all modified values, unchanged values are filtered</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDefaultModelElementStyle()">
<h3>createDefaultModelElementStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../properties/Style.html" title="class in com.nomagic.magicdraw.properties">Style</a></span> <span class="element-name">createDefaultModelElementStyle</span>()</div>
<div class="block">Returns default model element values.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>all default values, none of them are modified</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showDotNotationForAssociations()">
<h3>showDotNotationForAssociations</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">showDotNotationForAssociations</span>()</div>
<div class="block">Gets the SHOW_DOT_NOTATION_FOR_ASSOCIATIONS property value</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>value of SHOW_DOT_NOTATION_FOR_ASSOCIATIONS property or false if such property wasn't set.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setShowDotNotationForAssociations(boolean)">
<h3>setShowDotNotationForAssociations</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setShowDotNotationForAssociations</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block">Sets the SHOW_DOT_NOTATION_FOR_ASSOCIATIONS property value. If such property wasn't yet created, then creates one.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - boolean property value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="changeOwnershipForNavigability()">
<h3>changeOwnershipForNavigability</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">changeOwnershipForNavigability</span>()</div>
<div class="block">Gets the CHANGE_OWNERSHIP_FOR_NAVIGABILITY property value</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>value of CHANGE_OWNERSHIP_FOR_NAVIGABILITY property or false if such property wasn't set.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setChangeOwnershipForNavigability(boolean)">
<h3>setChangeOwnershipForNavigability</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setChangeOwnershipForNavigability</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block">Sets the HOW_DOT_NOTATION_FOR_ASSOCIATIONS property value. If such property wasn't yet created, then creates one.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - boolean property value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setBooleanProperty(boolean,java.lang.String,java.lang.String,java.lang.String)">
<h3>setBooleanProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setBooleanProperty</span><wbr/><span class="parameters">(boolean value,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> manager,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group)</span></div>
</section>
</li>
<li>
<section class="detail" id="isDisplayAllActivityParameterNodesInDiagrams()">
<h3>isDisplayAllActivityParameterNodesInDiagrams</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDisplayAllActivityParameterNodesInDiagrams</span>()</div>
<div class="block">Indicates if activity parameter nodes should be displayed in diagrams.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if activity parameter nodes should be displayed, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDisplayAllActivityParameterNodesInDiagrams(boolean)">
<h3>setDisplayAllActivityParameterNodesInDiagrams</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDisplayAllActivityParameterNodesInDiagrams</span><wbr/><span class="parameters">(boolean displayAllActivityParameterNodesInDiagrams)</span></div>
<div class="block">Sets whether to display activity parameter nodes in diagrams.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>displayAllActivityParameterNodesInDiagrams</code> - property value to set.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDisplayAllPinsInDiagrams()">
<h3>isDisplayAllPinsInDiagrams</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDisplayAllPinsInDiagrams</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setDisplayAllPinsInDiagrams(boolean)">
<h3>setDisplayAllPinsInDiagrams</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDisplayAllPinsInDiagrams</span><wbr/><span class="parameters">(boolean displayAllPinsInDiagrams)</span></div>
</section>
</li>
<li>
<section class="detail" id="isSeparateDecisionMergeAndJoinForkNotation()">
<h3>isSeparateDecisionMergeAndJoinForkNotation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isSeparateDecisionMergeAndJoinForkNotation</span>()</div>
</section>
</li>
<li>
<section class="detail" id="isHideInformationFlowVisibility()">
<h3>isHideInformationFlowVisibility</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isHideInformationFlowVisibility</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setHideInformationFlowVisibility(boolean)">
<h3>setHideInformationFlowVisibility</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setHideInformationFlowVisibility</span><wbr/><span class="parameters">(boolean hideInformationFlowVisibility)</span></div>
</section>
</li>
<li>
<section class="detail" id="setSeparateDecisionMergeAndJoinForkNotation(boolean)">
<h3>setSeparateDecisionMergeAndJoinForkNotation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSeparateDecisionMergeAndJoinForkNotation</span><wbr/><span class="parameters">(boolean separateDecisionMergeAndJoinForkNotation)</span></div>
</section>
</li>
<li>
<section class="detail" id="isAutoSynchronizeParametersAndArguments()">
<h3>isAutoSynchronizeParametersAndArguments</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isAutoSynchronizeParametersAndArguments</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if parameters and arguments should be auto-synchronized.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isLayoutScenarioDiagram()">
<h3>isLayoutScenarioDiagram</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isLayoutScenarioDiagram</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if scenario diagram should be layouted each time it is opened.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setLayoutScenarioDiagram(boolean)">
<h3>setLayoutScenarioDiagram</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLayoutScenarioDiagram</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block">Sets to layout scenario diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - value of the property.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setAutoSynchronizeParametersAndArguments(boolean)">
<h3>setAutoSynchronizeParametersAndArguments</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAutoSynchronizeParametersAndArguments</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block">Sets auto synchronize parameters and arguments property value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - - value of the property.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setGlobalPermission(boolean)">
<h3>setGlobalPermission</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setGlobalPermission</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block">Sets package permission global property value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - - value of the property.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getQNameDisplayAbsolute()">
<h3>getQNameDisplayAbsolute</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">getQNameDisplayAbsolute</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#getQNameDisplayStyle()"><code>getQNameDisplayStyle()</code></a> instead.</div>
</div>
<div class="block">Gets the QNAME_DISPLAY_STYLE property value.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if qualified name should be calculated starting from the project root, or false when qualified name
 should be calculated starting from the model library element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getQNameDisplayStyle()">
<h3>getQNameDisplayStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getQNameDisplayStyle</span>()</div>
<div class="block">Gets the QNAME_DISPLAY_STYLE property value.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>string that is one of the #QNAME_DISPLAY_STYLE_OPTIONS collection elements item.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setQNameDisplayAbsolute(boolean)">
<h3>setQNameDisplayAbsolute</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setQNameDisplayAbsolute</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#setQNameDisplayStyle(java.lang.String)"><code>setQNameDisplayStyle(String)</code></a> instead.</div>
</div>
<div class="block">Sets the QNAME_DISPLAY_STYLE property value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - true if qualified name should be calculated starting from the project root, or false when qualified
              name should be calculated starting from the model library element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setQNameDisplayStyle(java.lang.String)">
<h3>setQNameDisplayStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setQNameDisplayStyle</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> newValue)</span></div>
<div class="block">Sets the QNAME_DISPLAY_STYLE property value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>newValue</code> - one of the #QNAME_DISPLAY_STYLE_OPTIONS collection elements item, otherwise nothing happens -
                 property remains unchanged.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLayoutTemplateCreationMode()">
<h3>getLayoutTemplateCreationMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getLayoutTemplateCreationMode</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setLayoutTemplateCreationMode(java.lang.String)">
<h3>setLayoutTemplateCreationMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLayoutTemplateCreationMode</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> newValue)</span></div>
</section>
</li>
<li>
<section class="detail" id="getTooltipsStyle()">
<h3>getTooltipsStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ProjectOptions.TooltipsStyleChoice.html" title="enum class in com.nomagic.magicdraw.core.options">ProjectOptions.TooltipsStyleChoice</a></span> <span class="element-name">getTooltipsStyle</span>()</div>
<div class="block">Returns Tooltips Style property</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>selected value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTooltipsStyle(com.nomagic.magicdraw.core.options.ProjectOptions.TooltipsStyleChoice)">
<h3>setTooltipsStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTooltipsStyle</span><wbr/><span class="parameters">(<a href="ProjectOptions.TooltipsStyleChoice.html" title="enum class in com.nomagic.magicdraw.core.options">ProjectOptions.TooltipsStyleChoice</a> value)</span></div>
<div class="block">Sets Tooltips Style property</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - new value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setIgnoredValidationResults(java.lang.String[])">
<h3>setIgnoredValidationResults</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setIgnoredValidationResults</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] ignoredPairs)</span></div>
</section>
</li>
<li>
<section class="detail" id="getIgnoredActiveSuites()">
<h3>getIgnoredActiveSuites</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a>&gt;</span> <span class="element-name">getIgnoredActiveSuites</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getIgnoredPassiveValidationSuites()">
<h3>getIgnoredPassiveValidationSuites</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a>&gt;</span> <span class="element-name">getIgnoredPassiveValidationSuites</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getIgnoredValidationRules()">
<h3>getIgnoredValidationRules</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a>&gt;</span> <span class="element-name">getIgnoredValidationRules</span>()</div>
<div class="block">Return collection of ignored constraints.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>collection of ignored constraints.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIgnoredPassiveValidationRules()">
<h3>getIgnoredPassiveValidationRules</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a>&gt;</span> <span class="element-name">getIgnoredPassiveValidationRules</span>()</div>
<div class="block">Gets ignored passive validation rules</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>ignored passive validation rules.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIgnoredDuplicatedModules()">
<h3>getIgnoredDuplicatedModules</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getIgnoredDuplicatedModules</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>modules for which warning that they found in duplicated path is not shown.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setIgnoredDuplicatedModules(java.util.Collection)">
<h3>setIgnoredDuplicatedModules</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setIgnoredDuplicatedModules</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; value)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - modules for which warning that they found in duplicated path is not shown.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setIgnoredActiveSuites(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package[])">
<h3>setIgnoredActiveSuites</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setIgnoredActiveSuites</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a>[] elements)</span></div>
</section>
</li>
<li>
<section class="detail" id="setIgnoredPassiveValidationSuites(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package[])">
<h3>setIgnoredPassiveValidationSuites</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setIgnoredPassiveValidationSuites</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a>[] elements)</span></div>
</section>
</li>
<li>
<section class="detail" id="setIgnoredValidationRules(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint[])">
<h3>setIgnoredValidationRules</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setIgnoredValidationRules</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a>[] elements)</span></div>
</section>
</li>
<li>
<section class="detail" id="setIgnoredPassiveValidationRules(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint[])">
<h3>setIgnoredPassiveValidationRules</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setIgnoredPassiveValidationRules</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a>[] elements)</span></div>
</section>
</li>
<li>
<section class="detail" id="setPublicBranchSyncMode(com.nomagic.magicdraw.core.options.SyncMode)">
<h3>setPublicBranchSyncMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPublicBranchSyncMode</span><wbr/><span class="parameters">(<a href="SyncMode.html" title="enum class in com.nomagic.magicdraw.core.options">SyncMode</a> syncMode)</span></div>
<div class="block">Element hiding public branch synchronization mode.
 Project and user specific option.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>syncMode</code> - sync mode to set</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPublicBranchSyncMode()">
<h3>getPublicBranchSyncMode</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="SyncMode.html" title="enum class in com.nomagic.magicdraw.core.options">SyncMode</a></span> <span class="element-name">getPublicBranchSyncMode</span>()</div>
<div class="block">Method to get element hiding feature public branch synchronization mode.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>returns current synchronization mode or null if mode is not applicable for this project</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isLockFreeEditingEnabled()">
<h3>isLockFreeEditingEnabled</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isLockFreeEditingEnabled</span>()</div>
<div class="block">Determines if lock free editing is enabled in the project</div>
<dl class="notes">
<dt>Returns:</dt>
<dd><code>true</code> if enabled, <code>false</code> otherwise</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isGlobalEditingEnabled()">
<h3>isGlobalEditingEnabled</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isGlobalEditingEnabled</span>()</div>
<div class="block">Determines if global package permission is set to Read-Write or Read-Only</div>
<dl class="notes">
<dt>Returns:</dt>
<dd><code>true</code> if Read-Write, <code>false</code> if Read-Only</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setLockFreeEditingEnabled(boolean)">
<h3>setLockFreeEditingEnabled</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLockFreeEditingEnabled</span><wbr/><span class="parameters">(boolean enabled)</span></div>
<div class="block">Enables or disables lock free editing</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>enabled</code> - <code>true</code> to enable, <code>false</code> to disable</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getActiveValidationScope()">
<h3>getActiveValidationScope</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getActiveValidationScope</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setActiveValidationScope(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element[])">
<h3>setActiveValidationScope</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setActiveValidationScope</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>[] elements)</span></div>
</section>
</li>
<li>
<section class="detail" id="isFilterExcludesAuxiliaryResources()">
<h3>isFilterExcludesAuxiliaryResources</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isFilterExcludesAuxiliaryResources</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setFilterExcludesAuxiliaryResources(boolean)">
<h3>setFilterExcludesAuxiliaryResources</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setFilterExcludesAuxiliaryResources</span><wbr/><span class="parameters">(boolean value)</span></div>
</section>
</li>
<li>
<section class="detail" id="setFilterHidesIrrelevantElements(boolean)">
<h3>setFilterHidesIrrelevantElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setFilterHidesIrrelevantElements</span><wbr/><span class="parameters">(boolean value)</span></div>
</section>
</li>
<li>
<section class="detail" id="isFilterHidesIrrelevantElements()">
<h3>isFilterHidesIrrelevantElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isFilterHidesIrrelevantElements</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setFilterShowsImportedElements(boolean)">
<h3>setFilterShowsImportedElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setFilterShowsImportedElements</span><wbr/><span class="parameters">(boolean value)</span></div>
</section>
</li>
<li>
<section class="detail" id="isFilterShowsImportedElements()">
<h3>isFilterShowsImportedElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isFilterShowsImportedElements</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setFilterEnabled(boolean)">
<h3>setFilterEnabled</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setFilterEnabled</span><wbr/><span class="parameters">(boolean value)</span></div>
</section>
</li>
<li>
<section class="detail" id="isFilterEnabled()">
<h3>isFilterEnabled</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isFilterEnabled</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getFavoriteElements()">
<h3>getFavoriteElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getFavoriteElements</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setFavoriteElements(java.util.List)">
<h3>setFavoriteElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setFavoriteElements</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements)</span></div>
</section>
</li>
<li>
<section class="detail" id="getFavoriteElementsProperty()">
<h3>getFavoriteElementsProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../properties/ElementListProperty.html" title="class in com.nomagic.magicdraw.properties">ElementListProperty</a></span> <span class="element-name">getFavoriteElementsProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setActiveValidationSeverity(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral)">
<h3>setActiveValidationSeverity</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setActiveValidationSeverity</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> literal)</span></div>
</section>
</li>
<li>
<section class="detail" id="setPassiveValidationSeverity(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral)">
<h3>setPassiveValidationSeverity</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPassiveValidationSeverity</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> literal)</span></div>
</section>
</li>
<li>
<section class="detail" id="getActiveValidationSeverity()">
<h3>getActiveValidationSeverity</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a></span> <span class="element-name">getActiveValidationSeverity</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getPassiveValidationSeverity()">
<h3>getPassiveValidationSeverity</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a></span> <span class="element-name">getPassiveValidationSeverity</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setCompositionInspectionSeverity(java.lang.String)">
<h3>setCompositionInspectionSeverity</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCompositionInspectionSeverity</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> severity)</span></div>
</section>
</li>
<li>
<section class="detail" id="getCompositionInspectionSeverity()">
<h3>getCompositionInspectionSeverity</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getCompositionInspectionSeverity</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setDetectIllegalModelReferences(boolean)">
<h3>setDetectIllegalModelReferences</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDetectIllegalModelReferences</span><wbr/><span class="parameters">(boolean isDetectIllegalReferences)</span></div>
</section>
</li>
<li>
<section class="detail" id="isDetectIllegalModelReferences()">
<h3>isDetectIllegalModelReferences</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDetectIllegalModelReferences</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setValidationIgnoredOption(java.lang.String)">
<h3>setValidationIgnoredOption</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setValidationIgnoredOption</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="getValidationIgnoredOption()">
<h3>getValidationIgnoredOption</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getValidationIgnoredOption</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setMarkInTreeAndDiagrams(boolean)">
<h3>setMarkInTreeAndDiagrams</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setMarkInTreeAndDiagrams</span><wbr/><span class="parameters">(boolean mark)</span></div>
</section>
</li>
<li>
<section class="detail" id="isMarkInTreeAndDiagrams()">
<h3>isMarkInTreeAndDiagrams</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isMarkInTreeAndDiagrams</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setExcludeReadonlyElements(boolean)">
<h3>setExcludeReadonlyElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setExcludeReadonlyElements</span><wbr/><span class="parameters">(boolean exclude)</span></div>
</section>
</li>
<li>
<section class="detail" id="isExcludeElementsFromReadOnlyModules()">
<h3>isExcludeElementsFromReadOnlyModules</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isExcludeElementsFromReadOnlyModules</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setValidateOnlyActiveDiagrams(boolean)">
<h3>setValidateOnlyActiveDiagrams</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setValidateOnlyActiveDiagrams</span><wbr/><span class="parameters">(boolean validateOnlyActiveDiagrams)</span></div>
</section>
</li>
<li>
<section class="detail" id="isValidateOnlyActiveDiagrams()">
<h3>isValidateOnlyActiveDiagrams</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isValidateOnlyActiveDiagrams</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setValidateOnlyLocallyChangedElementsPreCommit(boolean)">
<h3>setValidateOnlyLocallyChangedElementsPreCommit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setValidateOnlyLocallyChangedElementsPreCommit</span><wbr/><span class="parameters">(boolean validateOnlyLocallyChangedElements)</span></div>
<div class="block">Sets value for the Validate Only Locally Changed Elements property in the pre-commit validation group.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>validateOnlyLocallyChangedElements</code> - new value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setExcludeElementsFromReadOnlyModulesPreCommit(boolean)">
<h3>setExcludeElementsFromReadOnlyModulesPreCommit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setExcludeElementsFromReadOnlyModulesPreCommit</span><wbr/><span class="parameters">(boolean excludeFromUsedReadOnly)</span></div>
<div class="block">Sets value for the Exclude Elements from Used Read-Only Project property in the pre-commit validation group.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>excludeFromUsedReadOnly</code> - new value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isValidateOnlyLocallyChangedElementsPreCommit()">
<h3>isValidateOnlyLocallyChangedElementsPreCommit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isValidateOnlyLocallyChangedElementsPreCommit</span>()</div>
<div class="block">Gets value of the Validate Only Locally Changed Elements property in the pre-commit validation group.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if property exists and is set to true</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isExcludeElementsFromReadOnlyModulesPreCommit()">
<h3>isExcludeElementsFromReadOnlyModulesPreCommit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isExcludeElementsFromReadOnlyModulesPreCommit</span>()</div>
<div class="block">Gets value of the Exclude Elements from Used Read-Only Project property in the pre-commit validation group.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if property exists and is set to true</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setPreCommitValidationSuites(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package[])">
<h3>setPreCommitValidationSuites</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPreCommitValidationSuites</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a>[] elements)</span></div>
<div class="block">Sets validation suites for pre-commit validation.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elements</code> - suites</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPreCommitValidationSuites()">
<h3>getPreCommitValidationSuites</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a>&gt;</span> <span class="element-name">getPreCommitValidationSuites</span>()</div>
<div class="block">Gets pre-commit validation suites.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>suites or null, if the property does not exist</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setPreCommitValidationExcludedScope(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element[])">
<h3>setPreCommitValidationExcludedScope</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPreCommitValidationExcludedScope</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>[] elements)</span></div>
<div class="block">Sets elements, excluded from pre-commit validation. Creates the property, if it does not yet exist.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elements</code> - excluded elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPreCommitValidationExcludedScope()">
<h3>getPreCommitValidationExcludedScope</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getPreCommitValidationExcludedScope</span>()</div>
<div class="block">Get elements, excluded from pre-commit validation.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>excluded scope</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setMinimalSeverityProhibitingCommit(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral)">
<h3>setMinimalSeverityProhibitingCommit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setMinimalSeverityProhibitingCommit</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> literal)</span></div>
<div class="block">Set minimal severity which prohibits commit after pre-commit validation.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>literal</code> - new severity. Null value sets the highest level - None</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMinimalSeverityProhibitingCommit()">
<h3>getMinimalSeverityProhibitingCommit</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a></span> <span class="element-name">getMinimalSeverityProhibitingCommit</span>()</div>
<div class="block">Get minimal severity which prohibits commit after pre-commit validation.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>minimal severity or null, if such property does not exist</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setMinimalSeverityProducingPreCommitWarning(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral)">
<h3>setMinimalSeverityProducingPreCommitWarning</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setMinimalSeverityProducingPreCommitWarning</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> literal)</span></div>
<div class="block">Sets minimal severity which produces warning after pre-commit validation.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>literal</code> - new severity. Null value sets the highest level - None</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMinimalSeverityProducingPreCommitWarning()">
<h3>getMinimalSeverityProducingPreCommitWarning</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a></span> <span class="element-name">getMinimalSeverityProducingPreCommitWarning</span>()</div>
<div class="block">Gets minimal severity which produces warning after pre-commit validation.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>minimal severity or null, if such property does not exist</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setLastSelectedModulePath(java.lang.String)">
<h3>setLastSelectedModulePath</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLastSelectedModulePath</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> path)</span></div>
<div class="block">Set last selected module path.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>path</code> - module path.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLastSelectedModulePath()">
<h3>getLastSelectedModulePath</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getLastSelectedModulePath</span>()</div>
<div class="block">Get last selected module path.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>last module path.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setLocksFilterUsername(java.lang.String)">
<h3>setLocksFilterUsername</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLocksFilterUsername</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> userName)</span></div>
<div class="block">Sets Lock view filter user name</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>userName</code> - name of user which was filtered in locks view.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLocksFilterUsername()">
<h3>getLocksFilterUsername</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getLocksFilterUsername</span>()</div>
<div class="block">Returns user name of lock view filter.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>name of user which was filtered in locks view.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="afterLoad()">
<h3>afterLoad</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">afterLoad</span>()</div>
</section>
</li>
<li>
<section class="detail" id="addToProjectSpellingIgnoreList(java.lang.String)">
<h3>addToProjectSpellingIgnoreList</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addToProjectSpellingIgnoreList</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> newTextToBeIgnored)</span></div>
</section>
</li>
<li>
<section class="detail" id="getProjectSpellingIgnoreList()">
<h3>getProjectSpellingIgnoreList</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[]</span> <span class="element-name">getProjectSpellingIgnoreList</span>()</div>
</section>
</li>
<li>
<section class="detail" id="isCheckForCyclicDependencies()">
<h3>isCheckForCyclicDependencies</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isCheckForCyclicDependencies</span>()</div>
<div class="block">Returns whether check for cyclic dependencies must be performed.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if checking for cyclic properties must be performed, otherwise - false.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCheckForCyclicDependencies(boolean)">
<h3>setCheckForCyclicDependencies</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCheckForCyclicDependencies</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block">Sets check for cyclic dependencies property value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - new value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDependencySeverityLevel()">
<h3>getDependencySeverityLevel</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="DependencySeverityLevel.html" title="enum class in com.nomagic.magicdraw.core.options">DependencySeverityLevel</a></span> <span class="element-name">getDependencySeverityLevel</span>()</div>
<div class="block">Returns dependency checker severity level.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if checking for cyclic properties must be performed, otherwise - false.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDependencySeverityLevel(com.nomagic.magicdraw.core.options.DependencySeverityLevel)">
<h3>setDependencySeverityLevel</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDependencySeverityLevel</span><wbr/><span class="parameters">(<a href="DependencySeverityLevel.html" title="enum class in com.nomagic.magicdraw.core.options">DependencySeverityLevel</a> value)</span></div>
<div class="block">Sets check for cyclic dependencies property value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - new value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getApplyPropertyImageProperty()">
<h3>getApplyPropertyImageProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ProjectOptions.ApplyPropertyImageChoice.html" title="enum class in com.nomagic.magicdraw.core.options">ProjectOptions.ApplyPropertyImageChoice</a></span> <span class="element-name">getApplyPropertyImageProperty</span>()</div>
<div class="block">Returns Apply Property Image property</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>selected value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setApplyPropertyImageProperty(com.nomagic.magicdraw.core.options.ProjectOptions.ApplyPropertyImageChoice)">
<h3>setApplyPropertyImageProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setApplyPropertyImageProperty</span><wbr/><span class="parameters">(<a href="ProjectOptions.ApplyPropertyImageChoice.html" title="enum class in com.nomagic.magicdraw.core.options">ProjectOptions.ApplyPropertyImageChoice</a> value)</span></div>
<div class="block">Sets Apply Property Image property</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - new value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramContextMode()">
<h3>getDiagramContextMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDiagramContextMode</span>()</div>
<div class="block">Returns diagram context mode for project</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>diagram context mode</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDiagramContextMode(java.lang.String)">
<h3>setDiagramContextMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDiagramContextMode</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> newValue)</span></div>
<div class="block">Sets diagram context mode for project</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>newValue</code> - context mode</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isIgnoreStandardProfiles()">
<h3>isIgnoreStandardProfiles</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isIgnoreStandardProfiles</span>()</div>
<div class="block">Returns indication that standard profiles must be ignored in dependency checking.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if checking for cyclic properties must be performed, otherwise - false.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setIgnoreStandardProfiles(boolean)">
<h3>setIgnoreStandardProfiles</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setIgnoreStandardProfiles</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block">Sets ignore standard profiles in dependency checking property.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - new value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProjectImpl()">
<h3>getProjectImpl</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a></span> <span class="element-name">getProjectImpl</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>getProjectImpl</code> in class <code>com.nomagic.magicdraw.uml.MDElementImpl</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setAutoNumbering(boolean)">
<h3>setAutoNumbering</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAutoNumbering</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block">Set AutoNumbering option</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - true of autoNumber option is on</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isAutoNumbering()">
<h3>isAutoNumbering</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isAutoNumbering</span>()</div>
<div class="block">Get the state of the  autoNumber Option</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if it is on</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDisplayNestedInstances(boolean)">
<h3>setDisplayNestedInstances</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDisplayNestedInstances</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block">Set Display Nested instances option</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - true if to display nested instances, else false</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDisplayNestedInstances()">
<h3>isDisplayNestedInstances</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDisplayNestedInstances</span>()</div>
<div class="block">Get the state of the display nested instances property</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if it is on</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setShowDiagramAbbreviation(boolean)">
<h3>setShowDiagramAbbreviation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setShowDiagramAbbreviation</span><wbr/><span class="parameters">(boolean showDiagramAbbreviation)</span></div>
<div class="block">Set show diagram abbreviation option</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>showDiagramAbbreviation</code> - true if to show diagram abbreviations, else false</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isShowDiagramAbbreviation()">
<h3>isShowDiagramAbbreviation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isShowDiagramAbbreviation</span>()</div>
<div class="block">Get the state of the show diagram abbreviation property</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if it is on</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDisplayElementNumberInBrowser(boolean)">
<h3>setDisplayElementNumberInBrowser</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDisplayElementNumberInBrowser</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block">Set the value to display/hide autoIds in the Browser</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - true if autoIds are to be shown</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setLockElementNumber(boolean)">
<h3>setLockElementNumber</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLockElementNumber</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block">Set the value to lock element number</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - true if lock numbers, else false</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCheckIdUniques(boolean)">
<h3>setCheckIdUniques</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCheckIdUniques</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block">Set the value to check element id uniques in all id properties</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - true if to check id uniques, else false</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCheckElementNumberUniques(boolean)">
<h3>setCheckElementNumberUniques</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCheckElementNumberUniques</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block">Set the value to check element number uniques</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - true if to check id uniques, else false</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDisplayElementNumberInBrowser()">
<h3>isDisplayElementNumberInBrowser</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDisplayElementNumberInBrowser</span>()</div>
<div class="block">Get the value of display/hide autoId in the Browser</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if the autoId is shown</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isLockedElementNumber()">
<h3>isLockedElementNumber</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isLockedElementNumber</span>()</div>
<div class="block">Get the value of number lock.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if locked, else false</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isCheckIdUniques()">
<h3>isCheckIdUniques</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isCheckIdUniques</span>()</div>
<div class="block">Get the value to check element id uniques in all id properties</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if to check uniques, else false</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isCheckElementNumberUniques()">
<h3>isCheckElementNumberUniques</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isCheckElementNumberUniques</span>()</div>
<div class="block">Get the value to check element id uniques in all id properties</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if to check uniques, else false</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUniqueElementNumberScope()">
<h3>getUniqueElementNumberScope</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getUniqueElementNumberScope</span>()</div>
<div class="block">Get the Packages where autoIds are to be unique</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a list of Packages</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setUniqueElementNumberScope(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element[])">
<h3>setUniqueElementNumberScope</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setUniqueElementNumberScope</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>[] elements)</span></div>
<div class="block">Set the Packages where AutoIds are to be unique</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elements</code> - the Packages</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setUseI18NTextInDiagrams(boolean)">
<h3>setUseI18NTextInDiagrams</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setUseI18NTextInDiagrams</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block">Set useI18N property for painting a text in diagrams</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isUseI18NTextInDiagrams()">
<h3>isUseI18NTextInDiagrams</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isUseI18NTextInDiagrams</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>use useI18N property for painting a text in diagrams</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLastSelectedXpdlImportLocation()">
<h3>getLastSelectedXpdlImportLocation</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getLastSelectedXpdlImportLocation</span>()</div>
<div class="block">The directory last accessed for XPDL import</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>location</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setXpdlImportLocation(java.lang.String)">
<h3>setXpdlImportLocation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setXpdlImportLocation</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> importLocation)</span></div>
</section>
</li>
<li>
<section class="detail" id="getFavoriteHyperlinks()">
<h3>getFavoriteHyperlinks</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getFavoriteHyperlinks</span>()</div>
<div class="block">Get favorite hyperlinks.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>URLs of hyperlinks.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setFavoriteHyperlinks(java.util.List)">
<h3>setFavoriteHyperlinks</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setFavoriteHyperlinks</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; urls)</span></div>
<div class="block">Set favorite hyperlinks.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>urls</code> - URLs of hyperlinks.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setUnlockedElementRemovalInfo(java.util.Map)">
<h3>setUnlockedElementRemovalInfo</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setUnlockedElementRemovalInfo</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; unlockedElementRemovalInfo)</span></div>
</section>
</li>
<li>
<section class="detail" id="getUnlockedElementRemovalInfo()">
<h3>getUnlockedElementRemovalInfo</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getUnlockedElementRemovalInfo</span>()</div>
</section>
</li>
<li>
<section class="detail" id="isUseDiagramsAspects()">
<h3>isUseDiagramsAspects</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isUseDiagramsAspects</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setUseDiagramsAspects(boolean)">
<h3>setUseDiagramsAspects</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setUseDiagramsAspects</span><wbr/><span class="parameters">(boolean use)</span></div>
</section>
</li>
<li>
<section class="detail" id="isSuspendAutoResizingOfShapes()">
<h3>isSuspendAutoResizingOfShapes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isSuspendAutoResizingOfShapes</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setSuspendAutoResizingOfShapes(boolean)">
<h3>setSuspendAutoResizingOfShapes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSuspendAutoResizingOfShapes</span><wbr/><span class="parameters">(boolean suspend)</span></div>
</section>
</li>
<li>
<section class="detail" id="isSuspendAutoDisplayingOfLabels()">
<h3>isSuspendAutoDisplayingOfLabels</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isSuspendAutoDisplayingOfLabels</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setSuspendAutoDisplayingOfLabels(boolean)">
<h3>setSuspendAutoDisplayingOfLabels</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSuspendAutoDisplayingOfLabels</span><wbr/><span class="parameters">(boolean suspend)</span></div>
</section>
</li>
<li>
<section class="detail" id="isHighlightSuspended()">
<h3>isHighlightSuspended</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isHighlightSuspended</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setHighlightSuspended(boolean)">
<h3>setHighlightSuspended</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setHighlightSuspended</span><wbr/><span class="parameters">(boolean highlight)</span></div>
</section>
</li>
<li>
<section class="detail" id="getTimeLimitToBuild()">
<h3>getTimeLimitToBuild</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">getTimeLimitToBuild</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setTimeLimitToBuild(java.lang.Integer)">
<h3>setTimeLimitToBuild</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTimeLimitToBuild</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> timeLimitToBuild)</span></div>
</section>
</li>
<li>
<section class="detail" id="getImageHeightLimit()">
<h3>getImageHeightLimit</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">getImageHeightLimit</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setImageHeightLimit(java.lang.Integer)">
<h3>setImageHeightLimit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setImageHeightLimit</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> imageHeightLimit)</span></div>
</section>
</li>
<li>
<section class="detail" id="getImageWidthLimit()">
<h3>getImageWidthLimit</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">getImageWidthLimit</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setImageWidthLimit(java.lang.Integer)">
<h3>setImageWidthLimit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setImageWidthLimit</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> imageWidthLimit)</span></div>
</section>
</li>
<li>
<section class="detail" id="getExportPrefWhenLimitsExceeded()">
<h3>getExportPrefWhenLimitsExceeded</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ProjectOptions.ExportPreferenceWhenLimitsExceeded.html" title="enum class in com.nomagic.magicdraw.core.options">ProjectOptions.ExportPreferenceWhenLimitsExceeded</a></span> <span class="element-name">getExportPrefWhenLimitsExceeded</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setExportPrefWhenLimitsExceeded(com.nomagic.magicdraw.core.options.ProjectOptions.ExportPreferenceWhenLimitsExceeded)">
<h3>setExportPrefWhenLimitsExceeded</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setExportPrefWhenLimitsExceeded</span><wbr/><span class="parameters">(<a href="ProjectOptions.ExportPreferenceWhenLimitsExceeded.html" title="enum class in com.nomagic.magicdraw.core.options">ProjectOptions.ExportPreferenceWhenLimitsExceeded</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="getIgnoredDiagramAspects()">
<h3>getIgnoredDiagramAspects</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt;</span> <span class="element-name">getIgnoredDiagramAspects</span>()</div>
<div class="block">Gets ignored diagram aspects</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>ignored diagram aspects</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setIgnoredDiagramAspects(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype[])">
<h3>setIgnoredDiagramAspects</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setIgnoredDiagramAspects</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>[] aspects)</span></div>
</section>
</li>
<li>
<section class="detail" id="setAutomaticTypeCreationMode(boolean)">
<h3>setAutomaticTypeCreationMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAutomaticTypeCreationMode</span><wbr/><span class="parameters">(boolean val)</span></div>
<div class="block">Sets automatic type creation property value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>val</code> - - automatic type creation property value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isAutomaticTypeCreationMode()">
<h3>isAutomaticTypeCreationMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isAutomaticTypeCreationMode</span>()</div>
<div class="block">Gets automatic type creation property value.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>automatic type creation layout property value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setAutomaticBehaviorCreationMode(boolean)">
<h3>setAutomaticBehaviorCreationMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAutomaticBehaviorCreationMode</span><wbr/><span class="parameters">(boolean val)</span></div>
<div class="block">Sets automatic behavior creation property value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>val</code> - - automatic behavior creation property value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isAutomaticBehaviorCreationMode()">
<h3>isAutomaticBehaviorCreationMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isAutomaticBehaviorCreationMode</span>()</div>
<div class="block">Gets automatic behavior creation property value.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>automatic behavior creation layout property value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDecimalPlaces()">
<h3>getDecimalPlaces</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">getDecimalPlaces</span>()</div>
<div class="block">Decimal places property to render the number (double/float) property in table and specification</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>decimal places or null if decimal places rendering is off</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDecimalPlaces(java.lang.Integer)">
<h3>setDecimalPlaces</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDecimalPlaces</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> decimalPlaces)</span></div>
<div class="block">Sets decimal places option value</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>decimalPlaces</code> - option, null indicates option off</dd>
</dl>
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
