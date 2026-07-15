# JAVA OPENAPI: ReportHelper (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/magicreport/helper/ReportHelper.html
- source_path: `com/nomagic/magicdraw/magicreport/helper/ReportHelper.html`
- source_sha256: `361ac9f965647ef04e43135740fa940e65a234077807c60c9612e2d3d44e202d`
- captured_utc: `2026-07-14T16:51:25.894266+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.magicreport.helper](package-summary.html)

## Class ReportHelper

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.util.Observable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html)
com.nomagic.magicreport.engine.Tool
com.nomagic.magicdraw.magicreport.helper.ReportHelper

All Implemented Interfaces:
`com.nomagic.magicreport.engine.ITool`, `com.nomagic.magicreport.IVariable`, `[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`

@OpenApiAllpublic classReportHelper
extends com.nomagic.magicreport.engine.Tool

Contains utilities functions for template report. Context name of this class is "report". Public functions of
 this class are able to access via template by using

$report

For example:

````java
<code>
    #foreach ($rel in $report.getRelationships($package))
       $rel.name
    #end
 </code>
````

Since:
Jun 13, 2007e
See Also:
[Serialized Form](../../../../../serialized-form.html#com.nomagic.magicdraw.magicreport.helper.ReportHelper)

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested classes/interfaces inherited from interface com.nomagic.magicreport.engine.ITool
`com.nomagic.magicreport.engine.ITool.HTMLString, com.nomagic.magicreport.engine.ITool.RetainedString, com.nomagic.magicreport.engine.ITool.Void`
 =========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ICON_PROPERTY_RETINASCALING](#ICON_PROPERTY_RETINASCALING)`
Fields inherited from class com.nomagic.magicreport.engine.Tool
`context, properties`
Fields inherited from interface com.nomagic.magicreport.engine.ITool
`VOID`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ReportHelper](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[collectRelationships](#collectRelationships(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Gets direct relationships of specified element.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[collectRelationships](#collectRelationships(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 boolean includeIndirect)`
Gets relationships of specified element.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[collectRelationships](#collectRelationships(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,boolean))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 boolean includeIndirect,
 boolean isRecursive)`
Gets relationships of specified element.
`boolean`
`[containsStereotype](#containsStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotypeName)`
Returns true if element contains a stereotype (include all derived stereotype) for the specified stereotype
 name.
`boolean`
`[containsStereotype](#containsStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,boolean))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotypeName,
 boolean includeDerived)`
Returns true if element contains a stereotype for the specified stereotype name.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createValueSpecificationText](#createValueSpecificationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification))([ValueSpecification](../../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html) specification)`
Create text represents the ValueSpecification element.
`void`
`[ensureLoad](#ensureLoad(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram))([Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)`

`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[filter](#filter(java.util.Collection,java.lang.String,java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elementList,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> propertyValue)`
Return the collection from the element list filtered by specified property name.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[BaseElement](../../uml/BaseElement.html)>`
`[filterClassName](#filterClassName(java.util.Collection,java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[BaseElement](../../uml/BaseElement.html)> elementList,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> shortNameForClassTypes)`
Return the collection from the element list filtered by short name for class types.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html)>`
`[filterDiagram](#filterDiagram(java.util.Collection,java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html)> diagramList,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> digramTypes)`
Return the collection from the diagram list filtered by types.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[BaseElement](../../uml/BaseElement.html)>`
`[filterElement](#filterElement(java.util.Collection,java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[BaseElement](../../uml/BaseElement.html)> elementList,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> humanTypes)`
Return the collection from the element list filtered by human types.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[filterElementByElementFilters](#filterElementByElementFilters(java.util.List,java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<com.nomagic.magicdraw.ui.ElementFilter> elementFilters)`

`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[BaseElement](../../uml/BaseElement.html)>`
`[filterElementByStereotypeName](#filterElementByStereotypeName(java.util.Collection,java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[BaseElement](../../uml/BaseElement.html)> elementList,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> stereotypesNames)`
Return the collection from the element list filtered by stereotype.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[BaseElement](../../uml/BaseElement.html)>`
`[filterElementType](#filterElementType(java.util.Collection,java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[BaseElement](../../uml/BaseElement.html)> elementList,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> elementTypes)`
Return the collection from the element list filtered by element types.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[filterVisibleElement](#filterVisibleElement(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements)`

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[filterVisibleElement](#filterVisibleElement(java.util.List,boolean))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements,
 boolean includeAuxiliaryResources)`

`[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[findDiagramByName](#findDiagramByName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) elementName)`

`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[findElementByName](#findElementByName(java.util.Collection,java.lang.String))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> source,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) regex)`
Search and return the elements from name by regular expression.
`[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[findElementInCollection](#findElementInCollection(java.util.Collection,java.lang.String))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> col,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) elementName)`
Search and return the element in the collection by element name.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[findRelationship](#findRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package))([Package](../../../uml2/ext/magicdraw/classes/mdkernel/Package.html) modelPackage)`
Search and return a collection of relationship element inside package.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[findRelationship](#findRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,boolean))([Package](../../../uml2/ext/magicdraw/classes/mdkernel/Package.html) modelPackage,
 boolean recursive)`
Search and return a collection of relationship element inside package.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getActorNumber](#getActorNumber(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Return the actor ID of Actor.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Class](../../../uml2/ext/magicdraw/classes/mdkernel/Class.html)>`
`[getAllCustomizationsByElement](#getAllCustomizationsByElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Get all customizations from specific element.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Class](../../../uml2/ext/magicdraw/classes/mdkernel/Class.html)>`
`[getAllCustomizationsByElement](#getAllCustomizationsByElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Object))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) aStereotype)`
Get all customizations from specific stereotype on element.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Class](../../../uml2/ext/magicdraw/classes/mdkernel/Class.html)>`
`[getAllCustomizationsByTarget](#getAllCustomizationsByTarget(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) targetElement)`
Get all customizations from specific target element of customization element.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[FlowStep](../../usecasescenarios/scenarios/FlowStep.html)>`
`[getAlternativeFlows](#getAlternativeFlows(com.nomagic.uml2.ext.magicdraw.mdusecases.UseCase))([UseCase](../../../uml2/ext/magicdraw/mdusecases/UseCase.html) useCase)`
Find and return all alternative flows from given use case.
`[Stereotype](../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html)`
`[getAppliedStereotypeByName](#getAppliedStereotypeByName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotypeName)`
Returns stereotype assigned to element.
`[Stereotype](../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html)`
`[getAppliedStereotypeByString](#getAppliedStereotypeByString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotype)`
Deprecated.
See [`getAppliedStereotypeByName(Element, String)`](#getAppliedStereotypeByName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))
`[File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html)`
`[getAttachedFile](#getAttachedFile(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Get file from attached file.
`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getAttachedImage](#getAttachedImage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getAttachedImage](#getAttachedImage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) cannotRenderImageMsg)`
Get image from attached image.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)`
`[getBaseClassAssociations](#getBaseClassAssociations(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))([Classifier](../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) classifier)`
Gets the classifier associations.
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Classifier](../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)>`
`[getBaseClassifiers](#getBaseClassifiers(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))([Classifier](../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) classifier)`
Return classifier based elements.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)`
`[getBaseClassInheritableAttributes](#getBaseClassInheritableAttributes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))([Classifier](../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) classifier)`
Gets the classifier inheritable attributes.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)`
`[getBaseClassInheritableOperations](#getBaseClassInheritableOperations(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))([Classifier](../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) classifier)`
Gets the classifier inheritable operations.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)`
`[getBaseClassPorts](#getBaseClassPorts(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))([Classifier](../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) classifier)`
Gets the classifier port.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)`
`[getBaseRealizedInterfaces](#getBaseRealizedInterfaces(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier))([BehavioredClassifier](../../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html) behavioredClassifier)`
Gets the behavior classifier realized interfaces.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)`
`[getBaseRelations](#getBaseRelations(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))([Classifier](../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) classifier)`
Gets the classifier relations.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[FlowStep](../../usecasescenarios/scenarios/FlowStep.html)>`
`[getBasicFlows](#getBasicFlows(com.nomagic.uml2.ext.magicdraw.mdusecases.UseCase))([UseCase](../../../uml2/ext/magicdraw/mdusecases/UseCase.html) useCase)`
Find and return a list of basic flows from given use case.
`[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[getClientElement](#getClientElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Gets relationship client.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getComment](#getComment(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Returns documentation of given element.
`com.nomagic.magicreport.Image`
`[getCustomImage](#getCustomImage(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../../uml/symbols/PresentationElement.html) presentationElement)`
Return original image of Image property from presentationElement
`com.nomagic.magicreport.Image`
`[getCustomImage](#getCustomImage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Return original image of Image property
`[ElementImageHelper.ImageInformation](../../../uml2/ext/jmi/helpers/ElementImageHelper.ImageInformation.html)`
`[getCustomImageInformation](#getCustomImageInformation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Return a CustomImageHolder information
`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getCustomizationProperty](#getCustomizationProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Object,java.lang.String))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) aStereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName)`
Return property value from Customization element of the specified stereotype, on the element.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getCustomizationPropertyString](#getCustomizationPropertyString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Object,java.lang.String))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) aStereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName)`
Return property value as string from Customization element of the specified stereotype, on the element.
`com.nomagic.magicdraw.ui.ElementFilter`
`[getDefaultElementFilter](#getDefaultElementFilter())()`

`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Classifier](../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)>`
`[getDerivedClassifiers](#getDerivedClassifiers(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))([Classifier](../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) parentClassifier)`
Returns classifier derived elements.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getDiagramElements](#getDiagramElements(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement))([DiagramPresentationElement](../../uml/symbols/DiagramPresentationElement.html) diagram)`
Gets presentation elements from this diagram.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getDiagramElements](#getDiagramElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram))([Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)`
Gets elements from this diagram.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getDiagramType](#getDiagramType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram))([Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)`
Gets diagram type.
`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getDSLProperty](#getDSLProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName)`
Get DSL Property.
`[Comment](../../../uml2/ext/magicdraw/classes/mdkernel/Comment.html)`
`[getElementComment](#getElementComment(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Returns comment annotated to this element.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getElementName](#getElementName(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) element)`
Gets name of the element.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Property](../../properties/Property.html)>`
`[getElementProperties](#getElementProperties(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Get all properties from specific element.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Property](../../properties/Property.html)>`
`[getElementProperties](#getElementProperties(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) mode)`
Collects properties that appears in element's specification dialog tree at specific view mode (Standard/Expert/All)
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getElementPropertiesName](#getElementPropertiesName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Get name of all properties from specific element.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getElementPropertiesNameWithMode](#getElementPropertiesNameWithMode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Get name of all properties from specific element and current mode.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getElementPropertiesNameWithMode](#getElementPropertiesNameWithMode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) mode)`
Get name of all properties from specific element and specific mode.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getElementURL](#getElementURL(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Retrieve MagicDraw's element URL.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[FlowStep](../../usecasescenarios/scenarios/FlowStep.html)>`
`[getExceptionalFlows](#getExceptionalFlows(com.nomagic.uml2.ext.magicdraw.mdusecases.UseCase))([UseCase](../../../uml2/ext/magicdraw/mdusecases/UseCase.html) useCase)`
Find and return a basic flow from given use case.
`com.nomagic.magicdraw.ui.ElementFilter`
`[getExcludeAuxiliaryResourceFilter](#getExcludeAuxiliaryResourceFilter())()`

`com.nomagic.magicdraw.ui.ElementFilter`
`[getExcludeRelationshipElementFilter](#getExcludeRelationshipElementFilter())()`

`com.nomagic.magicreport.Image`
`[getIconFor](#getIconFor(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../../uml/BaseElement.html) element)`
Return image icon for element.
`com.nomagic.magicreport.Image`
`[getIconFor](#getIconFor(com.nomagic.magicdraw.uml.BaseElement,boolean))([BaseElement](../../uml/BaseElement.html) element,
 boolean allowDuplicate)`
Return image icon for element.
`com.nomagic.magicreport.Image`
`[getIconFor](#getIconFor(com.nomagic.magicdraw.uml.BaseElement,boolean,java.util.Map))([BaseElement](../../uml/BaseElement.html) element,
 boolean allowDuplicate,
 [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> iconProperty)`
Return image icon for element.
`com.nomagic.magicreport.Image`
`[getIconFor](#getIconFor(com.nomagic.magicdraw.uml.BaseElement,java.lang.String,java.lang.String,boolean))([BaseElement](../../uml/BaseElement.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) prefix,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) suffix,
 boolean hashCode)`
Return image icon for element.
`com.nomagic.magicreport.Image`
`[getIconFor](#getIconFor(com.nomagic.magicdraw.uml.BaseElement,java.lang.String,java.lang.String,boolean,boolean))([BaseElement](../../uml/BaseElement.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) prefix,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) suffix,
 boolean hashCode,
 boolean allowDuplicate)`
Return image icon for element.
`com.nomagic.magicreport.Image`
`[getIconFor](#getIconFor(com.nomagic.magicdraw.uml.BaseElement,java.lang.String,java.lang.String,boolean,boolean,java.util.Map))([BaseElement](../../uml/BaseElement.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) prefix,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) suffix,
 boolean hashCode,
 boolean allowDuplicate,
 [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> iconProperty)`
Return image icon for element.
`com.nomagic.magicreport.Image`
`[getIconFor](#getIconFor(com.nomagic.magicdraw.uml.BaseElement,java.lang.String,java.lang.String,boolean,java.util.Map))([BaseElement](../../uml/BaseElement.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) prefix,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) suffix,
 boolean hashCode,
 [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> iconProperty)`
Return image icon for element.
`com.nomagic.magicreport.Image`
`[getIconFor](#getIconFor(com.nomagic.magicdraw.uml.BaseElement,java.util.Map))([BaseElement](../../uml/BaseElement.html) element,
 [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> iconProperty)`
Return image icon for element.
`com.nomagic.magicreport.Image`
`[getIconFor](#getIconFor(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) type)`
Return image icon for element.
`com.nomagic.magicreport.Image`
`[getIconFor](#getIconFor(java.lang.String,java.lang.String,java.lang.String,boolean))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) type,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) prefix,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) suffix,
 boolean hashCode)`
Return image icon for element.
`com.nomagic.magicreport.Image`
`[getIconFor](#getIconFor(java.lang.String,java.lang.String,java.lang.String,boolean,java.util.Map))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) type,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) prefix,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) suffix,
 boolean hashCode,
 [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> iconProperty)`
Return image icon for element.
`com.nomagic.magicreport.Image`
`[getIconFor](#getIconFor(java.lang.String,java.util.Map))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) type,
 [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> iconProperty)`
Return image icon for element.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getIconId](#getIconId(com.nomagic.magicdraw.uml.BaseElement,java.lang.String,java.lang.String,boolean,boolean,com.nomagic.ui.ResizableIcon))([BaseElement](../../uml/BaseElement.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) prefix,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) suffix,
 boolean hashCode,
 boolean allowDuplicate,
 [ResizableIcon](../../../ui/ResizableIcon.html) icon)`

`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getImageFor](#getImageFor(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Create image from element.
`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getImageFor](#getImageFor(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,int))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 int dpi)`
Create image from element.
`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getImageFor](#getImageFor(java.lang.Object,boolean))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) object,
 boolean allowDuplicate)`
Create image from object.
`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getImageFor](#getImageFor(java.lang.Object,boolean,java.lang.String))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) object,
 boolean allowDuplicate,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) cannotRenderImageMsg)`
Create image from object.
`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getImageFor](#getImageFor(java.lang.Object,boolean,java.lang.String,int))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) object,
 boolean allowDuplicate,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) cannotRenderImageMsg,
 int dpi)`
Create image from object.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getIncludeUseCase](#getIncludeUseCase(com.nomagic.uml2.ext.magicdraw.mdusecases.UseCase))([UseCase](../../../uml2/ext/magicdraw/mdusecases/UseCase.html) useCase)`
Gets use case included element.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getInnerElement](#getInnerElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Return a collection of inner element.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getInteractionMessageType](#getInteractionMessageType(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message))([Message](../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html) message)`
Gets interaction message type.
`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getMetaClass](#getMetaClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Get meta class of specific element
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Class](../../../uml2/ext/magicdraw/classes/mdkernel/Class.html)>`
`[getMetaClass](#getMetaClass(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))([Stereotype](../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) stereotype)`
Get stereotype meta class.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getOwnedElementsIncludingAdditional](#getOwnedElementsIncludingAdditional(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 boolean includePureOwned)`
Return owned elements of the given Element including additional owned elements defined in DSL specification by additionalContentProperty.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getOwnedElementsIncludingAdditional](#getOwnedElementsIncludingAdditional(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,boolean))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 boolean includePureOwned,
 boolean excludeRelationship)`
Return owned elements of the given Element including additional owned elements defined in DSL specification by additionalContentProperty.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getOwnedElementsIncludingAdditional](#getOwnedElementsIncludingAdditional(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,boolean,boolean))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 boolean includePureOwned,
 boolean excludeRelationship,
 boolean excludeAuxiliaryResources)`
Return owned elements of the given Element including additional owned elements defined in DSL specification by additionalContentProperty.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getOwnedElementsIncludingAdditional](#getOwnedElementsIncludingAdditional(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,boolean,boolean,boolean))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 boolean includePureOwned,
 boolean excludeRelationship,
 boolean excludeAuxiliaryResources,
 boolean excludeInvisibleElement)`
Return owned elements of the given Element including additional owned elements defined in DSL specification by additionalContentProperty.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getPackageQualifiedName](#getPackageQualifiedName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,java.lang.String))([NamedElement](../../../uml2/ext/magicdraw/classes/mdkernel/NamedElement.html) namedElement,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) separator)`
Get a qualified name by consider only Package and given element.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getPackages](#getPackages(boolean))(boolean includeSmartPackage)`

`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](../../uml/symbols/PresentationElement.html)>`
`[getPresentationDiagramElements](#getPresentationDiagramElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram))([Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)`
Gets presentation element in the diagram.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](../../uml/symbols/PresentationElement.html)>`
`[getPresentationDiagramElements](#getPresentationDiagramElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,boolean))([Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram,
 boolean includeNonManipulator)`
Gets presentation element in the diagram.
`com.nomagic.magicdraw.magicreport.helper.Polygon`
`[getPresentationElementBounds](#getPresentationElementBounds(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../../uml/symbols/PresentationElement.html) element)`
Gets the bounds of this element in the form of a Polygon object.
`com.nomagic.magicdraw.magicreport.helper.Polygon`
`[getPresentationElementBounds](#getPresentationElementBounds(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.export.image.ImageExportResult))([PresentationElement](../../uml/symbols/PresentationElement.html) element,
 [ImageExportResult](../../export/image/ImageExportResult.html) exportResult)`
Gets the bounds of this element in the form of a Polygon object.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<com.nomagic.magicdraw.magicreport.helper.Polygon>`
`[getPresentationElementBounds](#getPresentationElementBounds(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram,
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Gets the bounds of this element in the form of a Polygon object.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html)>`
`[getPresentationElementRectangle](#getPresentationElementRectangle(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram,
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Gets the bounds of this element in the form of a Rectangle object.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](../../uml/symbols/PresentationElement.html)>`
`[getPresentationElements](#getPresentationElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram))([Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)`
Deprecated.
`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getProperty](#getProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName)`
Get the element property value.
`[Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<com.nomagic.magicdraw.propertygroup.PropertyGroup>`
`[getPropertyGroupsByElement](#getPropertyGroupsByElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 boolean addAlwaysVisible)`
Get set of `PropertyGroup` by specific element.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.nomagic.magicdraw.propertygroup.PropertyGroup>`
`[getPropertyGroupsByStereotype](#getPropertyGroupsByStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class))([Class](../../../uml2/ext/magicdraw/classes/mdkernel/Class.html) stereotype)`
Get collection of `PropertyGroup` by specific stereotype.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Property](../../properties/Property.html)>`
`[getQProperties](#getQProperties(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName)`
Get list of properties for element with DSL property groups, and each property group has its own property.
`[Property](../../properties/Property.html)`
`[getQProperty](#getQProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName)`
Get a property for element with DSL property groups, and each property group has its own property.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getQualifiedName](#getQualifiedName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,java.lang.String))([NamedElement](../../../uml2/ext/magicdraw/classes/mdkernel/NamedElement.html) namedElement,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) separator)`
Get a qualified name.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getQualifiedOwnerName](#getQualifiedOwnerName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement))([NamedElement](../../../uml2/ext/magicdraw/classes/mdkernel/NamedElement.html) obj)`
Deprecated.
result from this method is incorrect.
`[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[getRecievingOperationalNode](#getRecievingOperationalNode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Get needline association ends.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getRelationship](#getRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Gets direct relationships of specified element.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getRelationship](#getRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 boolean recursive)`
Gets direct relationships of specified element.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getRelationship](#getRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,boolean))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 boolean recursive,
 boolean includeIndirect)`
Gets relationships of specified element.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Actor](../../../uml2/ext/magicdraw/mdusecases/Actor.html)>`
`[getRelativeActor](#getRelativeActor(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Gets element relative actor.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getRepresentationText](#getRepresentationText(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../../uml/BaseElement.html) e)`

`static [Node](../../ui/browser/Node.html)`
`[getRootNodeOfContainmentTree](#getRootNodeOfContainmentTree(boolean))(boolean startWithPrimaryModel)`
Get root node from containment tree.
`[Node](../../ui/browser/Node.html)`
`[getRootNodeOfDiagramTree](#getRootNodeOfDiagramTree())()`
Get root node from diagram tree.
`[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[getSendingOperationalNode](#getSendingOperationalNode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Get needline association ends.
`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getSlotProperty](#getSlotProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) classifierName)`
Get slot property by classifier name If there are more than one classifier matching with specified
 parameters, return only the property of first matching classifier.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)>`
`[getSlotValue](#getSlotValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) classifierName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) definingFeatureName)`
Get slot value by classifier name and definingFeature name.
`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getStereotypeProperty](#getStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName)`
Gets stereotype property.
`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getStereotypeProperty](#getStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,boolean))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName,
 boolean checkMultiplicity)`
Gets stereotype property.
`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getStereotypeProperty](#getStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotypeName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName)`
Gets stereotype property.
`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getStereotypeProperty](#getStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String,boolean))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotypeName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName,
 boolean checkMultiplicity)`
Gets stereotype property.
`static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getStereotypeProperty](#getStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String,java.lang.String))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) profileName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotypeName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName)`
Get Stereotype Property.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)>`
`[getStereotypePropertyList](#getStereotypePropertyList(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotypeName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName)`
Deprecated.
value return from this method is improperly converted.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getStereotypePropertyString](#getStereotypePropertyString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName)`
Gets stereotype property as String value.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getStereotypePropertyString](#getStereotypePropertyString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,java.lang.String))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) separator)`
Gets stereotype property as String value.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getStereotypePropertyString](#getStereotypePropertyString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotypeName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName)`
Gets stereotype property as String value.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getStereotypePropertyString](#getStereotypePropertyString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String,java.lang.String))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) profileName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotypeName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName)`
Gets stereotype property as String value.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getStereotypePropertyString](#getStereotypePropertyString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String,java.lang.String,java.lang.String))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) profileName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotypeName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) separator)`
Gets stereotype property as String value.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getStereotypePropertyStringValue](#getStereotypePropertyStringValue(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) o)`
Deprecated.
value return from this method is improperly converted.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Stereotype](../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html)>`
`[getStereotypes](#getStereotypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Gets all stereotypes applied to element.
`[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[getSupplierElement](#getSupplierElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Gets relationship supplier.
`[File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html)`
`[getTemplateFile](#getTemplateFile(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Get template file from element.
`[File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html)`
`[getTemplateFile](#getTemplateFile(java.lang.String,java.lang.String,java.lang.String,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) templateFileName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) templateLocation,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) extension,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) marker)`
Get Template file from template file name/path.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getUCOwnerNumber](#getUCOwnerNumber(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Return the use case number or use case ID of element.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[BaseElement](../../uml/BaseElement.html)>`
`[getUsageElements](#getUsageElements(java.util.Map,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[BaseElement](../../uml/BaseElement.html),[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<com.nomagic.magicdraw.uml.DependencyType>> usagesMap,
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Gets the element usages from usage map.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getUsageRepresentationText](#getUsageRepresentationText(com.nomagic.magicdraw.uml.BaseElement,boolean))([BaseElement](../../uml/BaseElement.html) be,
 boolean addFullPath)`
Formats the usage subject.
`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[BaseElement](../../uml/BaseElement.html),[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<com.nomagic.magicdraw.uml.DependencyType>>`
`[getUsages](#getUsages(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) selectedObjects)`
Returns Usage Map of MD and then use getUsageElements method for returning the usage of the specified
 element.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getUseCaseAssociatedElement](#getUseCaseAssociatedElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) obj)`
Deprecated.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getUseCaseNumber](#getUseCaseNumber(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Return the use case number or use case ID of element.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[BaseElement](../../uml/BaseElement.html)>`
`[getUsedBy](#getUsedBy(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Return a list of element used by this element (except diagram).
`com.nomagic.magicdraw.ui.ElementFilter`
`[getVisibleElementFilter](#getVisibleElementFilter())()`

`static boolean`
`[hasBaseClassifier](#hasBaseClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.lang.String))([Classifier](../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) classifier,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) baseClassifier)`
Checks if element has base classifier with given name.
`boolean`
`[hasProperty](#hasProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName)`
Returns true when a property with a given name is specified on this element, false otherwise.
`boolean`
`[hasStereotype](#hasStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Checks if element has stereotypes.
`boolean`
`[hasStereotype](#hasStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotype)`
Deprecated.
See [`containsStereotype(Element, String)`](#containsStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))
`boolean`
`[isAssignableFrom](#isAssignableFrom(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) classTypeName)`
A function for checking super type of the specific element.
`boolean`
`[isAttachedFile](#isAttachedFile(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Check if element is attached file.
`boolean`
`[isAttachedImage](#isAttachedImage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Check if element is attached image.
`boolean`
`[isDerivedClassifier](#isDerivedClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))([Classifier](../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) parent,
 [Classifier](../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) child)`
Checks if child is derived from parent by generalization.
`boolean`
`[isEmpty](#isEmpty(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)`
Test and return true if object is null, empty string or empty collection.
`boolean`
`[isEmpty](#isEmpty(java.lang.Object,boolean))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj,
 boolean isIgnoreSpace)`
Test and return true if object is null, empty string or empty collection.
`boolean`
`[isInvisibleElement](#isInvisibleElement(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../../uml/BaseElement.html) element)`

`boolean`
`[isInvisibleElement](#isInvisibleElement(com.nomagic.magicdraw.uml.BaseElement,boolean))([BaseElement](../../uml/BaseElement.html) element,
 boolean isTypeFilter)`

`boolean`
`[isInvisibleElement](#isInvisibleElement(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.ui.ElementFilter))([BaseElement](../../uml/BaseElement.html) element,
 com.nomagic.magicdraw.ui.ElementFilter elementFilter)`

`boolean`
`[isNamedElement](#isNamedElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Returns whether the element an `NamedElement`.
`boolean`
`[isNull](#isNull(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)`
Test and return true if object is null.
`boolean`
`[isRelationship](#isRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Test and return true if element is relationship.
`boolean`
`[isTypeOf](#isTypeOf(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) typeName)`
A function for checking super type of the specific element.
`boolean`
`[isTypeOf](#isTypeOf(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,boolean))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) typeName,
 boolean checkClassTypeName)`
A function for checking super type of the specific element.
`static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[parseObjectForPrinting](#parseObjectForPrinting(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)`
Parses Strings and Collections of Strings
`com.nomagic.magicdraw.magicreport.helper.Hyperlink`
`[serialize](#serialize(com.nomagic.magicdraw.hyperlinks.Hyperlink))([Hyperlink](../../hyperlinks/Hyperlink.html) hyperlink)`
Convert `com.nomagic.magicdraw.hyperlinks.Hyperlink` to `Hyperlink`.
`void`
`[setActiveValidationEnabled](#setActiveValidationEnabled(boolean))(boolean enable)`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[trimString](#trimString(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) s)`
Deprecated.
replaced with $s.trim()
Methods inherited from class com.nomagic.magicreport.engine.Tool
`clone, getContext, getProperties, getProperty, getProperty, notifyObservers, setContext, setProperties`
Methods inherited from class java.util.[Observable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html)
`[addObserver](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#addObserver(java.util.Observer)), [clearChanged](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#clearChanged()), [countObservers](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#countObservers()), [deleteObserver](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#deleteObserver(java.util.Observer)), [deleteObservers](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#deleteObservers()), [hasChanged](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#hasChanged()), [notifyObservers](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#notifyObservers()), [setChanged](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#setChanged())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicreport.engine.ITool
`clearTool`

============ FIELD DETAIL =========== 
Field Details
ICON_PROPERTY_RETINASCALING
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ICON_PROPERTY_RETINASCALING
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.magicreport.helper.ReportHelper.ICON_PROPERTY_RETINASCALING)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ReportHelper
public ReportHelper()
 ============ METHOD DETAIL ========== 
Method Details
getDSLProperty
public [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getDSLProperty([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName)
Get DSL Property.
Parameters:
`element` - the element.
`propertyName` - the property name.
Returns:
the property value.
getStereotypeProperty
public [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getStereotypeProperty([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotypeName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName)
Gets stereotype property.
Parameters:
`element` - the element.
`stereotypeName` - the stereotype name.
`propertyName` - the property name.
Returns:
the property value.
See Also:
[`getStereotypeProperty(Element, Stereotype, String)`](#getStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String))
[`getStereotypeProperty(Element, String, String, String)`](#getStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String,java.lang.String))
getStereotypeProperty
public [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getStereotypeProperty([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotypeName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName,
 boolean checkMultiplicity)
Gets stereotype property.
Parameters:
`element` - the element.
`stereotypeName` - the stereotype name.
`propertyName` - the property name.
`checkMultiplicity` - check multiplicity before return value
Returns:
the property value.
See Also:
[`getStereotypeProperty(Element, Stereotype, String)`](#getStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String))
[`getStereotypeProperty(Element, String, String, String)`](#getStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String,java.lang.String))
parseObjectForPrinting
public static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) parseObjectForPrinting([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)
Parses Strings and Collections of Strings
getStereotypeProperty
public [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getStereotypeProperty([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName)
Gets stereotype property.
Parameters:
`element` - the element.
`stereotype` - the stereotype.
`propertyName` - the property name.
Returns:
the property value.
See Also:
[`getStereotypeProperty(Element, String, String)`](#getStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String))
[`getStereotypeProperty(Element, String, String, String)`](#getStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String,java.lang.String))
getStereotypeProperty
public [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getStereotypeProperty([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName,
 boolean checkMultiplicity)
Gets stereotype property.
Parameters:
`element` - the element.
`stereotype` - the stereotype.
`propertyName` - the property name.
`checkMultiplicity` - check multiplicity before return value
Returns:
the property value.
See Also:
[`getStereotypeProperty(Element, String, String)`](#getStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String))
[`getStereotypeProperty(Element, String, String, String)`](#getStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String,java.lang.String))
getStereotypeProperty
public static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getStereotypeProperty([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) profileName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotypeName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName)
Get Stereotype Property.
Parameters:
`element` - the element.
`profileName` - profile name
`stereotypeName` - the stereotype name.
`propertyName` - the property name.
Returns:
the property value.
getStereotypePropertyList
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)> getStereotypePropertyList([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotypeName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName)
Deprecated.
value return from this method is improperly converted.
Gets stereotype property value as list of strings.
Parameters:
`element` - element with assigned stereotype
`stereotypeName` - stereotype name
`propertyName` - name of the property
Returns:
List of the property name.
getStereotypePropertyString
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getStereotypePropertyString([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotypeName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName)
Gets stereotype property as String value.
Parameters:
`element` - the element instance
`stereotypeName` - the stereotype name
`propertyName` - the property name
Returns:
the value as String
getStereotypePropertyString
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getStereotypePropertyString([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName)
Gets stereotype property as String value.
Parameters:
`element` - the element instance
`stereotype` - the stereotype instance
`propertyName` - the property name
Returns:
the value as String
getStereotypePropertyString
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getStereotypePropertyString([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) separator)
Gets stereotype property as String value.
Parameters:
`element` - the element instance
`stereotype` - the stereotype instance
`propertyName` - the property name
`separator` - when property value is list, the string will be added when convert list to string
Returns:
the value as String
getStereotypePropertyString
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getStereotypePropertyString([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) profileName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotypeName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName)
Gets stereotype property as String value.
Parameters:
`element` - the element instance
`profileName` - profile name
`stereotypeName` - the stereotype name
`propertyName` - the property name
Returns:
the value as String
getStereotypePropertyString
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getStereotypePropertyString([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) profileName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotypeName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) separator)
Gets stereotype property as String value.
Parameters:
`element` - the element instance
`profileName` - profile name
`stereotypeName` - the stereotype name
`propertyName` - the property name
`separator` - when property value is list, the string will be added when convert list to string
Returns:
the value as String
getStereotypePropertyStringValue
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getStereotypePropertyStringValue([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) o)
Deprecated.
value return from this method is improperly converted.
Gets Stereotype Property As String value.
Parameters:
`o` - the property
Returns:
the value as String
getRepresentationText
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getRepresentationText([BaseElement](../../uml/BaseElement.html) e)
isNamedElement
public boolean isNamedElement([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Returns whether the element an `NamedElement`.
Parameters:
`element` - element to test
Returns:
true if given element is `NamedElement`; otherwise false
getAppliedStereotypeByString
@CheckForNull
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public [Stereotype](../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) getAppliedStereotypeByString([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotype)
Deprecated.
See [`getAppliedStereotypeByName(Element, String)`](#getAppliedStereotypeByName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))
Returns stereotype assigned to element.
Parameters:
`element` - element
`stereotype` - name of stereotype
Returns:
assigned stereotype with that name.
getAppliedStereotypeByName
@CheckForNullpublic [Stereotype](../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) getAppliedStereotypeByName([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotypeName)
Returns stereotype assigned to element.
Parameters:
`element` - element
`stereotypeName` - name of stereotype
Returns:
assigned stereotype with that name.
hasStereotype
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public boolean hasStereotype([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotype)
Deprecated.
See [`containsStereotype(Element, String)`](#containsStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))
Checks if element has assigned stereotype with given name.
Parameters:
`element` - element to check
`stereotype` - stereotype name to check
Returns:
true if element has assigned stereotype with given name
containsStereotype
public boolean containsStereotype([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotypeName)
Returns true if element contains a stereotype (include all derived stereotype) for the specified stereotype
 name.
Parameters:
`element` - element to test
`stereotypeName` - stereotype name to be tested
Returns:
true if element contains a stereotype for the specified stereotype name.
See Also:
[`containsStereotype(Element, String, boolean)`](#containsStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,boolean))
containsStereotype
public boolean containsStereotype([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotypeName,
 boolean includeDerived)
Returns true if element contains a stereotype for the specified stereotype name.
Parameters:
`element` - element to test
`stereotypeName` - stereotype name to be tested
`includeDerived` - true if search target include all derived stereotypes; otherwise false
Returns:
true if element contains a stereotype for the specified stereotype name.
See Also:
[`containsStereotype(Element, String)`](#containsStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))
hasProperty
public boolean hasProperty([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName)
Returns true when a property with a given name is specified on this element, false otherwise.
Parameters:
`element` - element to test
`propertyName` - property name
Returns:
true when a property with a given name is specified on this element, false otherwise.
getProperty
public [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getProperty([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName)
 throws com.nomagic.magicdraw.magicreport.helper.PropertyNotFoundException
Get the element property value.
Parameters:
`element` - the object that will be gotten that data.
`propertyName` - the field of the element.
Returns:
the data of that field in the element.
Throws:
`com.nomagic.magicdraw.magicreport.helper.PropertyNotFoundException` - when a request property name is not found on target element.
getStereotypes
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Stereotype](../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html)> getStereotypes([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
 throws [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)
Gets all stereotypes applied to element. This method is replaced with $element.appliedStereotype.
Parameters:
`element` - the element
Returns:
the stereotype instances
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)` - from `StereotypesHelper.getStereotypes`
hasStereotype
public boolean hasStereotype([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
 throws [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)
Checks if element has stereotypes.
Parameters:
`element` - element to check
Returns:
true if has
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if element is null
findElementInCollection
@CheckForNullpublic [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) findElementInCollection([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> col,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) elementName)
Search and return the element in the collection by element name.
Parameters:
`col` - the collection of elements
`elementName` - the name of element
Returns:
the element instance, If it does not find, it will return null.
findDiagramByName
public [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) findDiagramByName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) elementName)
findElementByName
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> findElementByName([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> source,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) regex)
Search and return the elements from name by regular expression.
Parameters:
`source` - source
`regex` - the regular expression to which name is to be matched
Returns:
collection of matches element
getDerivedClassifiers
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Classifier](../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)> getDerivedClassifiers([Classifier](../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) parentClassifier)
Returns classifier derived elements.
Parameters:
`parentClassifier` - the parent class
Returns:
collection of derived elements (classifiers)
hasBaseClassifier
public static boolean hasBaseClassifier([Classifier](../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) classifier,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) baseClassifier)
Checks if element has base classifier with given name.
Parameters:
`classifier` - the classifier
`baseClassifier` - base classifier name
Returns:
true if the element contains specific base classifiers.
getBaseClassifiers
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Classifier](../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)> getBaseClassifiers([Classifier](../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) classifier)
Return classifier based elements. The list contains all base classifiers include all its derived
 classifiers.
Parameters:
`classifier` - the classifier
Returns:
collection of based elements (classifiers)
getComment
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getComment([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Returns documentation of given element.
Parameters:
`element` - the element which will be gotten the name.
Returns:
the document
getElementComment
@CheckForNullpublic [Comment](../../../uml2/ext/magicdraw/classes/mdkernel/Comment.html) getElementComment([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Returns comment annotated to this element. If comment is attached to this element, returns null.
Parameters:
`element` - the element which will be gotten the Comment.
Returns:
Comment instance of this element.
getRelativeActor
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Actor](../../../uml2/ext/magicdraw/mdusecases/Actor.html)> getRelativeActor([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Gets element relative actor.
Parameters:
`element` - the element
Returns:
the collection of Actor.
getUseCaseAssociatedElement
@CheckForNull
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getUseCaseAssociatedElement([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) obj)
Deprecated.
Gets associated Element.
Parameters:
`obj` - the element that we would like to find the other part
Returns:
the other parts
getIncludeUseCase
@CheckForNullpublic [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getIncludeUseCase([UseCase](../../../uml2/ext/magicdraw/mdusecases/UseCase.html) useCase)
Gets use case included element.
Parameters:
`useCase` - the UseCase instance
Returns:
the collection of included use case.
trimString
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) trimString([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) s)
Deprecated.
replaced with $s.trim()
Trim string.
Parameters:
`s` - the String
Returns:
the trimmed String
createValueSpecificationText
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createValueSpecificationText([ValueSpecification](../../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html) specification)
Create text represents the ValueSpecification element.
Parameters:
`specification` - The given ValueSpecification.
Returns:
the String value for ValueSpecification
getPresentationElements
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](../../uml/symbols/PresentationElement.html)> getPresentationElements([Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)
Deprecated.
Gets presentation element in the diagram. This method equivalent to
 [`getPresentationDiagramElements(Diagram)`](#getPresentationDiagramElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)).
Parameters:
`diagram` - the diagram instance.
Returns:
the collection of elements.
See Also:
[`getPresentationDiagramElements(Diagram)`](#getPresentationDiagramElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram))
getPresentationDiagramElements
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](../../uml/symbols/PresentationElement.html)> getPresentationDiagramElements([Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)
Gets presentation element in the diagram. This method will return all presentation elements from diagram
 except non-manipulator symbols.
Parameters:
`diagram` - the diagram instance.
Returns:
the collection of elements.
See Also:
[`getPresentationDiagramElements(Diagram, boolean)`](#getPresentationDiagramElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,boolean))
getPresentationDiagramElements
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](../../uml/symbols/PresentationElement.html)> getPresentationDiagramElements([Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram,
 boolean includeNonManipulator)
Gets presentation element in the diagram.
Parameters:
`diagram` - the diagram instance.
`includeNonManipulator` - true for include all non-manipulator element.
Returns:
the collection of elements.
See Also:
[`getPresentationDiagramElements(Diagram)`](#getPresentationDiagramElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram))
getPresentationElementBounds
@CheckForNullpublic com.nomagic.magicdraw.magicreport.helper.Polygon getPresentationElementBounds([PresentationElement](../../uml/symbols/PresentationElement.html) element)
Gets the bounds of this element in the form of a Polygon object. The bounds specify this component's
 coordinate to its diagram.
Parameters:
`element` - the presentation element on diagram.
Returns:
the bound of element as Polygon
getPresentationElementBounds
@CheckForNullpublic com.nomagic.magicdraw.magicreport.helper.Polygon getPresentationElementBounds([PresentationElement](../../uml/symbols/PresentationElement.html) element,
 [ImageExportResult](../../export/image/ImageExportResult.html) exportResult)
Gets the bounds of this element in the form of a Polygon object. The bounds specify this component's
 coordinate to its diagram.
Parameters:
`element` - the presentation element on diagram.
Returns:
the bound of element as Polygon
getPresentationElementRectangle
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html)> getPresentationElementRectangle([Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram,
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Gets the bounds of this element in the form of a Rectangle object. The bounds specify this component's
 coordinate to its diagram.
Parameters:
`diagram` - the target diagram.
`element` - the presentation element on given diagram.
Returns:
the bound of element as Rectangle. If element is not found in the diagram, it will return null.
getPresentationElementBounds
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<com.nomagic.magicdraw.magicreport.helper.Polygon> getPresentationElementBounds([Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram,
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Gets the bounds of this element in the form of a Polygon object. The bounds specify this component's
 coordinate to its diagram.
Parameters:
`diagram` - the target diagram.
`element` - the presentation element on given diagram.
Returns:
the bound of element as Polygon. If element is not found in the diagram, it will return null.
getDiagramType
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getDiagramType([Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)
Gets diagram type.
Parameters:
`diagram` - the diagram instance.
Returns:
the type of diagram.
getMetaClass
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Class](../../../uml2/ext/magicdraw/classes/mdkernel/Class.html)> getMetaClass([Stereotype](../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) stereotype)
Get stereotype meta class.
Parameters:
`stereotype` - the stereotype
Returns:
the collection of Meta Class
getMetaClass
public [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getMetaClass([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Get meta class of specific element
Parameters:
`element` - element
Returns:
a Meta Class or Collection of Meta Class
getDiagramElements
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getDiagramElements([Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)
Gets elements from this diagram.
Parameters:
`diagram` - the target diagram.
Returns:
the collection of elements.
getDiagramElements
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getDiagramElements([DiagramPresentationElement](../../uml/symbols/DiagramPresentationElement.html) diagram)
Gets presentation elements from this diagram.
Parameters:
`diagram` - the target diagram.
Returns:
the collection of elements.
getQualifiedOwnerName
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getQualifiedOwnerName([NamedElement](../../../uml2/ext/magicdraw/classes/mdkernel/NamedElement.html) obj)
Deprecated.
result from this method is incorrect. Use $element.owner.qualifiedName
Get qualified owner name.
Parameters:
`obj` - the object instance
Returns:
the qualified owner name
getQualifiedName
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getQualifiedName([NamedElement](../../../uml2/ext/magicdraw/classes/mdkernel/NamedElement.html) namedElement,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) separator)
Get a qualified name. Qualified is a name which allows the NamedElement to be identified within a hierarchy
 of nested Namespaces. It is constructed from the names of the containing namespaces starting at the root of
 the hierarchy and ending with the name of the NamedElement itself.
Parameters:
`namedElement` - NamedElement
`separator` - separator symbol. If value is null or empty string, the '::' will be used.
Returns:
a qualified name.
getPackageQualifiedName
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getPackageQualifiedName([NamedElement](../../../uml2/ext/magicdraw/classes/mdkernel/NamedElement.html) namedElement,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) separator)
Get a qualified name by consider only Package and given element. Model and Profile will not be included on
 the qualified name.
 For example: The element hierarchy is `Design : Model -> com : Package -> nomagic : Package -> ui -> Package -> BaseDialog : Class` When template code is: `$report.getPackageQualifiedName($class, ".")` Where $class is "BaseDialog" element, the result from above code will be: `com.nomagic.ui.BaseDialog`
Parameters:
`namedElement` - NamedElement
`separator` - separator symbol. If value is null or empty string, the '::' will be used.
Returns:
a qualified name.
serialize
public com.nomagic.magicdraw.magicreport.helper.Hyperlink serialize([Hyperlink](../../hyperlinks/Hyperlink.html) hyperlink)
Convert `com.nomagic.magicdraw.hyperlinks.Hyperlink` to `Hyperlink`.
Parameters:
`hyperlink` - the magicdraw hyperlink
Returns:
the magic report hyperlink instance
getSendingOperationalNode
public [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) getSendingOperationalNode([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Get needline association ends.
Parameters:
`element` - element
Returns:
needline association ends
getRecievingOperationalNode
public [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) getRecievingOperationalNode([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Get needline association ends.
Parameters:
`element` - element
Returns:
needline association ends
findRelationship
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> findRelationship([Package](../../../uml2/ext/magicdraw/classes/mdkernel/Package.html) modelPackage)
Search and return a collection of relationship element inside package.
Parameters:
`modelPackage` - package element
Returns:
Collection of relationship in this package
findRelationship
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> findRelationship([Package](../../../uml2/ext/magicdraw/classes/mdkernel/Package.html) modelPackage,
 boolean recursive)
Search and return a collection of relationship element inside package.
Parameters:
`modelPackage` - package element
`recursive` - if true, perform recursively
Returns:
Collection of relationship in this package
getRelationship
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getRelationship([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Gets direct relationships of specified element.
Parameters:
`element` - Element element to be collect
Returns:
Collection of relationship
getRelationship
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getRelationship([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 boolean recursive)
Gets direct relationships of specified element.
Parameters:
`element` - Element element to be collect
`recursive` - if true, perform recursively
Returns:
Collection of relationship
getRelationship
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getRelationship([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 boolean recursive,
 boolean includeIndirect)
Gets relationships of specified element.
Parameters:
`element` - element to be collect
`recursive` - if true, perform recursively
`includeIndirect` - true to include indirect relationships
Returns:
Collection of relationship
collectRelationships
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> collectRelationships([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Gets direct relationships of specified element.
Parameters:
`element` - Element element to be collect
Returns:
Collection of relationship
collectRelationships
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> collectRelationships([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 boolean includeIndirect)
Gets relationships of specified element.
Parameters:
`element` - element to be collect
`includeIndirect` - true to include indirect relationships
Returns:
Collection of relationship
collectRelationships
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> collectRelationships([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 boolean includeIndirect,
 boolean isRecursive)
Gets relationships of specified element.
Parameters:
`element` - element to be collect
`includeIndirect` - true to include indirect relationships
`isRecursive` - if true, perform recursively
Returns:
Collection of relationship
getClientElement
public [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) getClientElement([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Gets relationship client.
Parameters:
`element` - relationship model element.
Returns:
client element
getSupplierElement
public [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) getSupplierElement([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Gets relationship supplier.
Parameters:
`element` - relationship model element.
Returns:
supplier element
getInnerElement
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getInnerElement([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Return a collection of inner element.
Parameters:
`element` - Element element to be collect
Returns:
Collection of inner
getIconFor
public com.nomagic.magicreport.Image getIconFor([BaseElement](../../uml/BaseElement.html) element)
Return image icon for element.
Parameters:
`element` - a Magic Draw element
Returns:
Image object for element's icon
getIconFor
public com.nomagic.magicreport.Image getIconFor([BaseElement](../../uml/BaseElement.html) element,
 [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> iconProperty)
Return image icon for element.
Parameters:
`element` - a Magic Draw element
`iconProperty` - custom property to create icon
Returns:
Image object for element's icon
getIconFor
public com.nomagic.magicreport.Image getIconFor([BaseElement](../../uml/BaseElement.html) element,
 boolean allowDuplicate)
Return image icon for element.
Parameters:
`element` - a Magic Draw element
`allowDuplicate` - true to always create new icon and don't keep the icon in map
Returns:
Image object for element's icon
getIconFor
public com.nomagic.magicreport.Image getIconFor([BaseElement](../../uml/BaseElement.html) element,
 boolean allowDuplicate,
 [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> iconProperty)
Return image icon for element.
Parameters:
`element` - a Magic Draw element
`allowDuplicate` - true to always create new icon and don't keep the icon in map
`iconProperty` - custom property to create icon
Returns:
Image object for element's icon
getIconFor
public com.nomagic.magicreport.Image getIconFor([BaseElement](../../uml/BaseElement.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) prefix,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) suffix,
 boolean hashCode)
Return image icon for element. In case of `hashCode` equals true, icon's name format is set to
 "icon_"+hash code and doesn't include prefix/suffix.
Parameters:
`element` - a MagicDraw element
`prefix` - prefix for icon's name
`suffix` - suffix for icon's name
`hashCode` - uses hash code in icon's name
Returns:
Image object for element's icon
getIconFor
public com.nomagic.magicreport.Image getIconFor([BaseElement](../../uml/BaseElement.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) prefix,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) suffix,
 boolean hashCode,
 [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> iconProperty)
Return image icon for element. In case of `hashCode` equals true, icon's name format is set to
 "icon_"+hash code and doesn't include prefix/suffix.
Parameters:
`element` - a MagicDraw element
`prefix` - prefix for icon's name
`suffix` - suffix for icon's name
`hashCode` - uses hash code in icon's name
`iconProperty` - custom property to create icon
Returns:
Image object for element's icon
getIconFor
public com.nomagic.magicreport.Image getIconFor([BaseElement](../../uml/BaseElement.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) prefix,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) suffix,
 boolean hashCode,
 boolean allowDuplicate)
Return image icon for element. In case of `hashCode` equals true, icon's name format is set to
 "icon_"+hash code and doesn't include prefix/suffix.
Parameters:
`element` - a MagicDraw element
`prefix` - prefix for icon's name
`suffix` - suffix for icon's name
`hashCode` - uses hash code in icon's name
`allowDuplicate` - true to always create new icon and don't keep the icon in map
Returns:
Image object for element's icon
getIconId
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getIconId([BaseElement](../../uml/BaseElement.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) prefix,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) suffix,
 boolean hashCode,
 boolean allowDuplicate,
 [ResizableIcon](../../../ui/ResizableIcon.html) icon)
getIconFor
@CheckForNullpublic com.nomagic.magicreport.Image getIconFor([BaseElement](../../uml/BaseElement.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) prefix,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) suffix,
 boolean hashCode,
 boolean allowDuplicate,
 @CheckForNull
 [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> iconProperty)
Return image icon for element. In case of `hashCode` equals true, icon's name format is set to
 "icon_"+hash code and doesn't include prefix/suffix.
Parameters:
`element` - a MagicDraw element
`prefix` - prefix for icon's name
`suffix` - suffix for icon's name
`hashCode` - uses hash code in icon's name
`allowDuplicate` - true to always create new icon and don't keep the icon in map
`iconProperty` - custom property to create icon
Returns:
Image object for element's icon
getIconFor
public com.nomagic.magicreport.Image getIconFor([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) type)
Return image icon for element.
Parameters:
`type` - element type
Returns:
Image object for element's icon
getIconFor
public com.nomagic.magicreport.Image getIconFor([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) type,
 [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> iconProperty)
Return image icon for element.
Parameters:
`type` - element type
Returns:
Image object for element's icon
getIconFor
public com.nomagic.magicreport.Image getIconFor([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) type,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) prefix,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) suffix,
 boolean hashCode)
Return image icon for element. In case of `hashCode` equals true, icon's name format is set to
 "icon_"+hash code and doesn't include prefix/suffix.
Parameters:
`type` - element type
`prefix` - prefix for icon's name
`suffix` - suffix for icon's name
`hashCode` - uses hash code in icon's name
Returns:
Image object for element's icon
getIconFor
public com.nomagic.magicreport.Image getIconFor([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) type,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) prefix,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) suffix,
 boolean hashCode,
 [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> iconProperty)
Return image icon for element. In case of `hashCode` equals true, icon's name format is set to
 "icon_"+hash code and doesn't include prefix/suffix.
Parameters:
`type` - element type
`prefix` - prefix for icon's name
`suffix` - suffix for icon's name
`hashCode` - uses hash code in icon's name
`iconProperty` - custom property to create icon
Returns:
Image object for element's icon
getCustomImage
public com.nomagic.magicreport.Image getCustomImage([PresentationElement](../../uml/symbols/PresentationElement.html) presentationElement)
Return original image of Image property from presentationElement
Parameters:
`presentationElement` - a presentationElement
Returns:
original image in Image property
getCustomImage
public com.nomagic.magicreport.Image getCustomImage([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Return original image of Image property
Parameters:
`element` - an element
Returns:
original image in Image property
getCustomImageInformation
public [ElementImageHelper.ImageInformation](../../../uml2/ext/jmi/helpers/ElementImageHelper.ImageInformation.html) getCustomImageInformation([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Return a CustomImageHolder information
Parameters:
`element` - element
Returns:
CustomImageHolder
isNull
public boolean isNull([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Test and return true if object is null.
Parameters:
`obj` - object being tested.
Returns:
true if object is null
isEmpty
public boolean isEmpty([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Test and return true if object is null, empty string or empty collection.
Parameters:
`obj` - object being tested.
Returns:
true if object is null, empty string or empty collection.
isEmpty
public boolean isEmpty([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj,
 boolean isIgnoreSpace)
Test and return true if object is null, empty string or empty collection.
Parameters:
`obj` - object being tested.
`isIgnoreSpace` - true for ignoring all spaces, line feeds, etc. for html string only
Returns:
true if object is null, empty string or empty collection.
isRelationship
public boolean isRelationship([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Test and return true if element is relationship.
Parameters:
`element` - element being tested.
Returns:
true if object is relationship
getInteractionMessageType
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getInteractionMessageType([Message](../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html) message)
Gets interaction message type.
Parameters:
`message` - Message
Returns:
type of message
getUsageRepresentationText
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getUsageRepresentationText([BaseElement](../../uml/BaseElement.html) be,
 boolean addFullPath)
Formats the usage subject. The output string is the same as Result column of **Used by** table in Magic
 Draw.
Parameters:
`be` - `ModelElement` to format.
`addFullPath` - use full path.
Returns:
formatted element, String.
getUsedBy
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[BaseElement](../../uml/BaseElement.html)> getUsedBy([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Return a list of element used by this element (except diagram).
Parameters:
`element` - the the element which will be gotten the list of element name that uses the specified
 element.
Returns:
Collection of elements used by input element.
getUsages
public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[BaseElement](../../uml/BaseElement.html),[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<com.nomagic.magicdraw.uml.DependencyType>> getUsages([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) selectedObjects)
Returns Usage Map of MD and then use getUsageElements method for returning the usage of the specified
 element.
Parameters:
`selectedObjects` - the elements that this method will find the usage.
Returns:
Map of Usages of elements
getUsageElements
@CheckForNullpublic [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[BaseElement](../../uml/BaseElement.html)> getUsageElements([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[BaseElement](../../uml/BaseElement.html),[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<com.nomagic.magicdraw.uml.DependencyType>> usagesMap,
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Gets the element usages from usage map.
Parameters:
`usagesMap` - the Usages Map of MagicDraw.
`element` - the element which will be gotten the list of element name that uses the specified element.
Returns:
Collection of usage name of elements.
getElementName
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getElementName([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) element)
Gets name of the element. If the name of element is empty, it will return "<unnamed>". This method
 performs the following procedures:
 If element is generalized from NamedElement, return $element.name
If element is generalized from Slot, return $element.definingFeature.name
If element is an UML element, return $element.humanName
else return $element.toString()
Parameters:
`element` - the element.
Returns:
element name
filterDiagram
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html)> filterDiagram([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html)> diagramList,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> digramTypes)
Return the collection from the diagram list filtered by types.
 Example: `#foreach ($d in $report.filterElement($Diagram, ['Use Case Diagram', 'Class Diagram'])
 $d.name
 #end`
Parameters:
`diagramList` - the collection of diagrams.
`digramTypes` - the collection of diagram types which is used to filter.
Returns:
the collection of filtered diagrams.
filterElement
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[BaseElement](../../uml/BaseElement.html)> filterElement([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[BaseElement](../../uml/BaseElement.html)> elementList,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> humanTypes)
Return the collection from the element list filtered by human types.
 Example: `#foreach ($e in $report.filterElement($elements, ['Class', 'Interface'])
 $e.name $e.humanType
 #end`
Parameters:
`elementList` - the collection of element.
`humanTypes` - the collection of human types which is used to filter.
Returns:
the collection of filtered elements.
filterElementByStereotypeName
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[BaseElement](../../uml/BaseElement.html)> filterElementByStereotypeName([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[BaseElement](../../uml/BaseElement.html)> elementList,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> stereotypesNames)
Return the collection from the element list filtered by stereotype.
Parameters:
`elementList` - the collection of element.
`stereotypesNames` - the collection of stereotypes names which is used to filter.
Returns:
the collection of filtered elements.
filterElementType
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[BaseElement](../../uml/BaseElement.html)> filterElementType([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[BaseElement](../../uml/BaseElement.html)> elementList,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> elementTypes)
Return the collection from the element list filtered by element types.
 Example: `#foreach ($e in $report.filterElementType($elements, ['class', 'interface'])
 $e.name $e.elementType
 #end`
Parameters:
`elementList` - the collection of element.
`elementTypes` - the collection of element types which is used to filter.
Returns:
the collection of filtered elements.
filterClassName
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[BaseElement](../../uml/BaseElement.html)> filterClassName([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[BaseElement](../../uml/BaseElement.html)> elementList,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> shortNameForClassTypes)
Return the collection from the element list filtered by short name for class types.
 Example: `#foreach ($e in $report.filterClassName($elements, ['Diagram', 'UseCase'])
 $e.name $e.className
 #end`
Parameters:
`elementList` - the collection of element.
`shortNameForClassTypes` - the collection of short name for class type which is used to filter.
Returns:
the collection of filtered elements.
filter
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> filter([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elementList,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> propertyValue)
Return the collection from the element list filtered by specified property name.
 Example: `#foreach ($e in $report.filter($elements, 'name', ['foo', 'bar'])
 $e.name
 #end`
Parameters:
`elementList` - the collection of element.
`propertyName` - the property name which is used to filter.
`propertyValue` - the collection of element property values which is used to filter.
Returns:
the collection of filtered elements.
getBaseClassInheritableAttributes
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) getBaseClassInheritableAttributes([Classifier](../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) classifier)
Gets the classifier inheritable attributes.
Parameters:
`classifier` - the Classifier.
Returns:
the Collection of Attributes.
getBaseClassInheritableOperations
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) getBaseClassInheritableOperations([Classifier](../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) classifier)
Gets the classifier inheritable operations.
Parameters:
`classifier` - the Classifier.
Returns:
the Collection of Operations.
getBaseClassAssociations
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) getBaseClassAssociations([Classifier](../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) classifier)
Gets the classifier associations.
Parameters:
`classifier` - the Classifier.
Returns:
the Collection of Associations.
getBaseRelations
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) getBaseRelations([Classifier](../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) classifier)
Gets the classifier relations.
Parameters:
`classifier` - the Classifier.
Returns:
the Collection of Relations.
getBaseClassPorts
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) getBaseClassPorts([Classifier](../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) classifier)
Gets the classifier port.
Parameters:
`classifier` - the Classifier.
Returns:
the Collection of Ports.
getBaseRealizedInterfaces
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) getBaseRealizedInterfaces([BehavioredClassifier](../../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html) behavioredClassifier)
Gets the behavior classifier realized interfaces.
Parameters:
`behavioredClassifier` - the BehavioredClassifier.
Returns:
the Collection of RealizedInterfaces.
isDerivedClassifier
public boolean isDerivedClassifier([Classifier](../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) parent,
 [Classifier](../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) child)
Checks if child is derived from parent by generalization.
Parameters:
`parent` - parent
`child` - possible parent
Returns:
true if derived
getUseCaseNumber
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getUseCaseNumber([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Return the use case number or use case ID of element.
Parameters:
`element` - the element
Returns:
the use case number.
getActorNumber
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getActorNumber([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Return the actor ID of Actor.
Parameters:
`element` - element
Returns:
the actor ID
getUCOwnerNumber
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getUCOwnerNumber([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Return the use case number or use case ID of element.
Parameters:
`element` - the element
Returns:
the use case owner number or ID.
getElementURL
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getElementURL([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Retrieve MagicDraw's element URL.
Parameters:
`element` - element object
Returns:
MagicDraw's element URL
getBasicFlows
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[FlowStep](../../usecasescenarios/scenarios/FlowStep.html)> getBasicFlows([UseCase](../../../uml2/ext/magicdraw/mdusecases/UseCase.html) useCase)
Find and return a list of basic flows from given use case. If use case scenario is not being used, it will
 retrieve the value from "requirementUseCase" stereotype tags.
Parameters:
`useCase` - a use case.
Returns:
a list of flow step [`FlowStep`](../../usecasescenarios/scenarios/FlowStep.html)
getAlternativeFlows
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[FlowStep](../../usecasescenarios/scenarios/FlowStep.html)> getAlternativeFlows([UseCase](../../../uml2/ext/magicdraw/mdusecases/UseCase.html) useCase)
Find and return all alternative flows from given use case. The alternative flows will be listed from all
 possible branches of basic flows. If use case scenario is not being used, it will the retrieve value from
 "requirementUseCase" stereotype tags.
Parameters:
`useCase` - a use case.
Returns:
a list of flow step [`FlowStep`](../../usecasescenarios/scenarios/FlowStep.html)
getExceptionalFlows
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[FlowStep](../../usecasescenarios/scenarios/FlowStep.html)> getExceptionalFlows([UseCase](../../../uml2/ext/magicdraw/mdusecases/UseCase.html) useCase)
Find and return a basic flow from given use case. If use case scenario is not being used, it will the
 retrieve value from "requirementUseCase" stereotype tags.
Parameters:
`useCase` - a use case.
Returns:
a list of flow step [`FlowStep`](../../usecasescenarios/scenarios/FlowStep.html)
getSlotValue
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)> getSlotValue([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) classifierName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) definingFeatureName)
Get slot value by classifier name and definingFeature name. If there are more than one slots matching with
 specified parameters, return only the value of first matching slot.
Parameters:
`element` - an element.
`classifierName` - classifier name. [case-sensitive]
`definingFeatureName` - defining feature name. [case-sensitive]
Returns:
result value in ValueSpecification or value in array of ValueSpecification, up to multiplicity.
getSlotProperty
@CheckForNullpublic [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getSlotProperty([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) classifierName)
Get slot property by classifier name If there are more than one classifier matching with specified
 parameters, return only the property of first matching classifier.
Parameters:
`element` - an element.
`classifierName` - classifier name. [case-sensitive]
Returns:
slot property
getOwnedElementsIncludingAdditional
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getOwnedElementsIncludingAdditional([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 boolean includePureOwned)
Return owned elements of the given Element including additional owned elements defined in DSL specification by additionalContentProperty.
Parameters:
`element` - an element to be found owned element
`includePureOwned` - include element owned directly in ownedElement UML metaproperty
Returns:
owned elements of the given Element
getOwnedElementsIncludingAdditional
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getOwnedElementsIncludingAdditional([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 boolean includePureOwned,
 boolean excludeRelationship)
Return owned elements of the given Element including additional owned elements defined in DSL specification by additionalContentProperty.
Parameters:
`element` - an element to be found owned element
`includePureOwned` - include element owned directly in ownedElement UML metaproperty
`excludeRelationship` - true to exclude relationship
getOwnedElementsIncludingAdditional
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getOwnedElementsIncludingAdditional([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 boolean includePureOwned,
 boolean excludeRelationship,
 boolean excludeAuxiliaryResources)
Return owned elements of the given Element including additional owned elements defined in DSL specification by additionalContentProperty.
Parameters:
`element` - an element to be found owned element
`includePureOwned` - include element owned directly in ownedElement UML metaproperty
`excludeRelationship` - true to exclude relationship of given element
`excludeAuxiliaryResources` - true to exclude auxiliary resoures
Returns:
owned elements of the given Element
getOwnedElementsIncludingAdditional
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getOwnedElementsIncludingAdditional([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 boolean includePureOwned,
 boolean excludeRelationship,
 boolean excludeAuxiliaryResources,
 boolean excludeInvisibleElement)
Return owned elements of the given Element including additional owned elements defined in DSL specification by additionalContentProperty.
Parameters:
`element` - an element to be found owned element
`includePureOwned` - include element owned directly in ownedElement UML metaproperty
`excludeRelationship` - true to exclude relationship of given element
`excludeAuxiliaryResources` - true to exclude auxiliary resources
`excludeInvisibleElement` - true to exclude invisible element
Returns:
owned elements of the given Element
filterElementByElementFilters
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> filterElementByElementFilters([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<com.nomagic.magicdraw.ui.ElementFilter> elementFilters)
getPackages
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getPackages(boolean includeSmartPackage)
isAttachedFile
public boolean isAttachedFile([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Check if element is attached file.
Parameters:
`element` - specific element
Returns:
true if element is attached element, otherwise; false
isAttachedImage
public boolean isAttachedImage([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Check if element is attached image.
Parameters:
`element` - specific element
Returns:
true if element is attached image, otherwise; false
getAttachedImage
public [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getAttachedImage([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
 throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)`
getAttachedImage
@CheckForNullpublic [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getAttachedImage([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) cannotRenderImageMsg)
 throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)
Get image from attached image.
Parameters:
`element` - specific element
`cannotRenderImageMsg` - in case the element is attached file but not image, return this msg instead.
Returns:
image of attached image.
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)`
getAttachedFile
public [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) getAttachedFile([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
 throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)
Get file from attached file.
Parameters:
`element` - specific element
Returns:
image of attached image.
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)`
getTemplateFile
@CheckForNullpublic [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) getTemplateFile([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) templateFileName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) templateLocation,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) extension,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) marker)
Get Template file from template file name/path.
Parameters:
`templateFileName` - template file name or path
`templateLocation` - template location/dir
`extension` - extension for template file. in case it has no extension
`marker` - The marker object used to track the file.
Returns:
template file
getTemplateFile
public [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) getTemplateFile([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
 throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)
Get template file from element.
Parameters:
`element` - attached file
Returns:
template file
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)`
getImageFor
public [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getImageFor([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Create image from element. 

 The image is always created.
Parameters:
`element` - target element
Returns:
image
getImageFor
public [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getImageFor([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 int dpi)
Create image from element. 

 The image is always created.
Parameters:
`element` - target element
`dpi` -
Returns:
image
getImageFor
public [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getImageFor([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) object,
 boolean allowDuplicate)
Create image from object. 

 The image is newly created or returned old image from map up to 'allowDuplicate'.
Parameters:
`object` - object to be exported as image
`allowDuplicate` - allowDuplicated true to always create new image and don't keep the image in map
Returns:
Image
getImageFor
public [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getImageFor([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) object,
 boolean allowDuplicate,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) cannotRenderImageMsg)
Create image from object. 

 The image is newly created or returned old image from map up to 'allowDuplicate'.
Parameters:
`object` - object to be exported as image
`allowDuplicate` - allowDuplicated true to always create new image and don't keep the image in map
`cannotRenderImageMsg` - in case the element is attached file but not image, return error message instead.
Returns:
Image
getImageFor
public [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getImageFor([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) object,
 boolean allowDuplicate,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) cannotRenderImageMsg,
 int dpi)
Create image from object. 

 The image is newly created or returned old image from map up to 'allowDuplicate'.
Parameters:
`object` - object to be exported as image
`allowDuplicate` - allowDuplicated true to always create new image and don't keep the image in map
`cannotRenderImageMsg` - in case the element is attached file but not image, return error message instead.
`dpi` - image dpi
Returns:
Image
getCustomizationPropertyString
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getCustomizationPropertyString([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) aStereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName)
Return property value as string from Customization element of the specified stereotype, on the element.
Parameters:
`element` - an element
`aStereotype` - stereotype name or element
`propertyName` - property name
Returns:
property value as string from Customization element
getCustomizationProperty
public [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getCustomizationProperty([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) aStereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName)
Return property value from Customization element of the specified stereotype, on the element.
Parameters:
`element` - an element
`aStereotype` - stereotype name or element
`propertyName` - property name
Returns:
property value from Customization element
getAllCustomizationsByElement
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Class](../../../uml2/ext/magicdraw/classes/mdkernel/Class.html)> getAllCustomizationsByElement([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Get all customizations from specific element.
Parameters:
`element` - an element
Returns:
all customization elements of the stereotype on the element.
getAllCustomizationsByElement
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Class](../../../uml2/ext/magicdraw/classes/mdkernel/Class.html)> getAllCustomizationsByElement([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) aStereotype)
Get all customizations from specific stereotype on element.
Parameters:
`element` - an element
`aStereotype` - stereotype name or element
Returns:
all customization elements of the stereotype on the element.
getAllCustomizationsByTarget
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Class](../../../uml2/ext/magicdraw/classes/mdkernel/Class.html)> getAllCustomizationsByTarget([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) targetElement)
Get all customizations from specific target element of customization element.
Parameters:
`targetElement` - a target element
Returns:
all customizations from specific target element of customization element.
getElementPropertiesName
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getElementPropertiesName([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Get name of all properties from specific element.
Parameters:
`element` - element
Returns:
list of properties name
getElementPropertiesNameWithMode
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getElementPropertiesNameWithMode([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Get name of all properties from specific element and current mode.
Parameters:
`element` - element
Returns:
list of properties name
getElementPropertiesNameWithMode
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getElementPropertiesNameWithMode([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) mode)
Get name of all properties from specific element and specific mode.
Parameters:
`element` - element
`mode` - view mode from PropertiesModeHelper.MODES
Returns:
list of properties name
getElementProperties
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Property](../../properties/Property.html)> getElementProperties([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Get all properties from specific element.
Parameters:
`element` - element
Returns:
list of properties
getElementProperties
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Property](../../properties/Property.html)> getElementProperties([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) mode)
Collects properties that appears in element's specification dialog tree at specific view mode (Standard/Expert/All)
Parameters:
`element` - element
`mode` - view mode from PropertiesModeHelper.MODES -- STANDARD, EXPERT, ALL
Returns:
list of properties
getDefaultElementFilter
public com.nomagic.magicdraw.ui.ElementFilter getDefaultElementFilter()
getExcludeAuxiliaryResourceFilter
public com.nomagic.magicdraw.ui.ElementFilter getExcludeAuxiliaryResourceFilter()
getVisibleElementFilter
public com.nomagic.magicdraw.ui.ElementFilter getVisibleElementFilter()
getExcludeRelationshipElementFilter
public com.nomagic.magicdraw.ui.ElementFilter getExcludeRelationshipElementFilter()
filterVisibleElement
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> filterVisibleElement([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements)
filterVisibleElement
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> filterVisibleElement([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements,
 boolean includeAuxiliaryResources)
isInvisibleElement
public boolean isInvisibleElement([BaseElement](../../uml/BaseElement.html) element)
isInvisibleElement
public boolean isInvisibleElement([BaseElement](../../uml/BaseElement.html) element,
 boolean isTypeFilter)
isInvisibleElement
public boolean isInvisibleElement([BaseElement](../../uml/BaseElement.html) element,
 @CheckForNull
 com.nomagic.magicdraw.ui.ElementFilter elementFilter)
getRootNodeOfContainmentTree
public static [Node](../../ui/browser/Node.html) getRootNodeOfContainmentTree(boolean startWithPrimaryModel)
Get root node from containment tree.
Parameters:
`startWithPrimaryModel` - true to filter only primary model, 

 otherwise it will return Project node that may contain primary model and usage project
Returns:
root node from containment tree
getRootNodeOfDiagramTree
public [Node](../../ui/browser/Node.html) getRootNodeOfDiagramTree()
Get root node from diagram tree.
Returns:
root node from diagram tree
getPropertyGroupsByStereotype
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.nomagic.magicdraw.propertygroup.PropertyGroup> getPropertyGroupsByStereotype([Class](../../../uml2/ext/magicdraw/classes/mdkernel/Class.html) stereotype)
Get collection of `PropertyGroup` by specific stereotype.
Parameters:
`stereotype` - a stereotype
Returns:
collection of `PropertyGroup`
getPropertyGroupsByElement
public [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<com.nomagic.magicdraw.propertygroup.PropertyGroup> getPropertyGroupsByElement([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 boolean addAlwaysVisible)
Get set of `PropertyGroup` by specific element.
Parameters:
`element` - an element
`addAlwaysVisible` - true to use all set stereotypes + all settable showWhenNotApplied stereotypes, false to use only all set stereotypes.
Returns:
set of `PropertyGroup`
getQProperty
@CheckForNullpublic [Property](../../properties/Property.html) getQProperty([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName)
Get a property for element with DSL property groups, and each property group has its own property.
Parameters:
`element` - an element.
`propertyName` - property name
Returns:
a [`Property`](../../properties/Property.html)
getQProperties
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Property](../../properties/Property.html)> getQProperties([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName)
Get list of properties for element with DSL property groups, and each property group has its own property.
Parameters:
`element` - an element.
`propertyName` - property name
Returns:
a list of [`Property`](../../properties/Property.html)
setActiveValidationEnabled
public void setActiveValidationEnabled(boolean enable)
ensureLoad
public void ensureLoad([Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)
isTypeOf
public boolean isTypeOf([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) typeName)
A function for checking super type of the specific element.
Parameters:
`element` - an element
`typeName` - stereotype name or java class name
Returns:
return true, if the element is subtype of the specific stereotype name or class name.
isTypeOf
public boolean isTypeOf([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) typeName,
 boolean checkClassTypeName)
A function for checking super type of the specific element.
Parameters:
`element` - an element
`typeName` - stereotype name or java class name
`checkClassTypeName` - false to check type by stereotype name only
Returns:
return true, if the element is subtype of the specific stereotype name or class name.
isAssignableFrom
public boolean isAssignableFrom([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) classTypeName)
A function for checking super type of the specific element.
Parameters:
`element` - an element
`classTypeName` - java class name
Returns:
return true, if the element is subtype of the specific class type name.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.magicreport.helper</a></div>
<h1 class="title" title="Class ReportHelper">Class ReportHelper</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html" title="class or interface in java.util">java.util.Observable</a>
<div class="inheritance">com.nomagic.magicreport.engine.Tool
<div class="inheritance">com.nomagic.magicdraw.magicreport.helper.ReportHelper</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.nomagic.magicreport.engine.ITool</code>, <code>com.nomagic.magicreport.IVariable</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ReportHelper</span>
<span class="extends-implements">extends com.nomagic.magicreport.engine.Tool</span></div>
<div class="block">Contains utilities functions for template report. Context name of this class is "report". Public functions of
 this class are able to access via template by using <code>$report</code>
<p></p>
 For example:

 <pre>
 &lt;code&gt;
    #foreach ($rel in $report.getRelationships($package))
       $rel.name
    #end
 &lt;/code&gt;
 </pre></div>
<dl class="notes">
<dt>Since:</dt>
<dd>Jun 13, 2007e</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../serialized-form.html#com.nomagic.magicdraw.magicreport.helper.ReportHelper">Serialized Form</a></li>
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
<div class="inherited-list">
<h2 id="nested-classes-inherited-from-class-com.nomagic.magicreport.engine.ITool">Nested classes/interfaces inherited from interface com.nomagic.magicreport.engine.ITool</h2>
<code>com.nomagic.magicreport.engine.ITool.HTMLString, com.nomagic.magicreport.engine.ITool.RetainedString, com.nomagic.magicreport.engine.ITool.Void</code></div>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ICON_PROPERTY_RETINASCALING">ICON_PROPERTY_RETINASCALING</a></code></div>
<div class="col-last even-row-color"> </div>
</div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicreport.engine.Tool">Fields inherited from class com.nomagic.magicreport.engine.Tool</h3>
<code>context, properties</code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicreport.engine.ITool">Fields inherited from interface com.nomagic.magicreport.engine.ITool</h3>
<code>VOID</code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ReportHelper</a>()</code></div>
<div class="col-last even-row-color"> </div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#collectRelationships(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">collectRelationships</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets direct relationships of specified element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#collectRelationships(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">collectRelationships</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 boolean includeIndirect)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets relationships of specified element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#collectRelationships(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,boolean)">collectRelationships</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 boolean includeIndirect,
 boolean isRecursive)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets relationships of specified element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#containsStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">containsStereotype</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotypeName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns true if element contains a stereotype (include all derived stereotype) for the specified stereotype
 name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#containsStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,boolean)">containsStereotype</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotypeName,
 boolean includeDerived)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns true if element contains a stereotype for the specified stereotype name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createValueSpecificationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)">createValueSpecificationText</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> specification)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Create text represents the ValueSpecification element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#ensureLoad(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">ensureLoad</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#filter(java.util.Collection,java.lang.String,java.util.Collection)">filter</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elementList,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; propertyValue)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return the collection from the element list filtered by specified property name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#filterClassName(java.util.Collection,java.util.Collection)">filterClassName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt; elementList,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; shortNameForClassTypes)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return the collection from the element list filtered by short name for class types.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#filterDiagram(java.util.Collection,java.util.Collection)">filterDiagram</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a>&gt; diagramList,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; digramTypes)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return the collection from the diagram list filtered by types.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#filterElement(java.util.Collection,java.util.Collection)">filterElement</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt; elementList,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; humanTypes)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return the collection from the element list filtered by human types.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#filterElementByElementFilters(java.util.List,java.util.List)">filterElementByElementFilters</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;com.nomagic.magicdraw.ui.ElementFilter&gt; elementFilters)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#filterElementByStereotypeName(java.util.Collection,java.util.Collection)">filterElementByStereotypeName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt; elementList,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; stereotypesNames)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return the collection from the element list filtered by stereotype.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#filterElementType(java.util.Collection,java.util.Collection)">filterElementType</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt; elementList,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; elementTypes)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return the collection from the element list filtered by element types.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#filterVisibleElement(java.util.List)">filterVisibleElement</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#filterVisibleElement(java.util.List,boolean)">filterVisibleElement</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements,
 boolean includeAuxiliaryResources)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#findDiagramByName(java.lang.String)">findDiagramByName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> elementName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#findElementByName(java.util.Collection,java.lang.String)">findElementByName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; source,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> regex)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Search and return the elements from name by regular expression.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#findElementInCollection(java.util.Collection,java.lang.String)">findElementInCollection</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; col,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> elementName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Search and return the element in the collection by element name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#findRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)">findRelationship</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> modelPackage)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Search and return a collection of relationship element inside package.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#findRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,boolean)">findRelationship</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> modelPackage,
 boolean recursive)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Search and return a collection of relationship element inside package.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getActorNumber(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getActorNumber</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return the actor ID of Actor.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAllCustomizationsByElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getAllCustomizationsByElement</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get all customizations from specific element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAllCustomizationsByElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Object)">getAllCustomizationsByElement</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> aStereotype)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get all customizations from specific stereotype on element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAllCustomizationsByTarget(java.lang.Object)">getAllCustomizationsByTarget</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> targetElement)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get all customizations from specific target element of customization element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../usecasescenarios/scenarios/FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAlternativeFlows(com.nomagic.uml2.ext.magicdraw.mdusecases.UseCase)">getAlternativeFlows</a><wbr/>(<a href="../../../uml2/ext/magicdraw/mdusecases/UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">UseCase</a> useCase)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Find and return all alternative flows from given use case.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAppliedStereotypeByName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">getAppliedStereotypeByName</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotypeName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns stereotype assigned to element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getAppliedStereotypeByString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">getAppliedStereotypeByString</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotype)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">See <a href="#getAppliedStereotypeByName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)"><code>getAppliedStereotypeByName(Element, String)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAttachedFile(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getAttachedFile</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get file from attached file.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAttachedImage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getAttachedImage</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAttachedImage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">getAttachedImage</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> cannotRenderImageMsg)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get image from attached image.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBaseClassAssociations(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">getBaseClassAssociations</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the classifier associations.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getBaseClassifiers(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">getBaseClassifiers</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return classifier based elements.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBaseClassInheritableAttributes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">getBaseClassInheritableAttributes</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the classifier inheritable attributes.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBaseClassInheritableOperations(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">getBaseClassInheritableOperations</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the classifier inheritable operations.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBaseClassPorts(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">getBaseClassPorts</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the classifier port.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBaseRealizedInterfaces(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier)">getBaseRealizedInterfaces</a><wbr/>(<a href="../../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">BehavioredClassifier</a> behavioredClassifier)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the behavior classifier realized interfaces.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBaseRelations(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">getBaseRelations</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the classifier relations.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../usecasescenarios/scenarios/FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBasicFlows(com.nomagic.uml2.ext.magicdraw.mdusecases.UseCase)">getBasicFlows</a><wbr/>(<a href="../../../uml2/ext/magicdraw/mdusecases/UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">UseCase</a> useCase)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Find and return a list of basic flows from given use case.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getClientElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getClientElement</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets relationship client.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getComment(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getComment</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns documentation of given element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicreport.Image</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCustomImage(com.nomagic.magicdraw.uml.symbols.PresentationElement)">getCustomImage</a><wbr/>(<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> presentationElement)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return original image of Image property from presentationElement</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicreport.Image</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCustomImage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getCustomImage</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return original image of Image property</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/jmi/helpers/ElementImageHelper.ImageInformation.html" title="class in com.nomagic.uml2.ext.jmi.helpers">ElementImageHelper.ImageInformation</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCustomImageInformation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getCustomImageInformation</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a CustomImageHolder information</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCustomizationProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Object,java.lang.String)">getCustomizationProperty</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> aStereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return property value from Customization element of the specified stereotype, on the element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCustomizationPropertyString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Object,java.lang.String)">getCustomizationPropertyString</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> aStereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return property value as string from Customization element of the specified stereotype, on the element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.ui.ElementFilter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDefaultElementFilter()">getDefaultElementFilter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDerivedClassifiers(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">getDerivedClassifiers</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> parentClassifier)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns classifier derived elements.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDiagramElements(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement)">getDiagramElements</a><wbr/>(<a href="../../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a> diagram)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets presentation elements from this diagram.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDiagramElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">getDiagramElements</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets elements from this diagram.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDiagramType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">getDiagramType</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets diagram type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDSLProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">getDSLProperty</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get DSL Property.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Comment.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Comment</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElementComment(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getElementComment</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns comment annotated to this element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElementName(java.lang.Object)">getElementName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets name of the element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../properties/Property.html" title="class in com.nomagic.magicdraw.properties">Property</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElementProperties(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getElementProperties</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get all properties from specific element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../properties/Property.html" title="class in com.nomagic.magicdraw.properties">Property</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElementProperties(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">getElementProperties</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> mode)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collects properties that appears in element's specification dialog tree at specific view mode (Standard/Expert/All)</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElementPropertiesName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getElementPropertiesName</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get name of all properties from specific element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElementPropertiesNameWithMode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getElementPropertiesNameWithMode</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get name of all properties from specific element and current mode.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElementPropertiesNameWithMode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">getElementPropertiesNameWithMode</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> mode)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get name of all properties from specific element and specific mode.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElementURL(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getElementURL</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Retrieve MagicDraw's element URL.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../usecasescenarios/scenarios/FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getExceptionalFlows(com.nomagic.uml2.ext.magicdraw.mdusecases.UseCase)">getExceptionalFlows</a><wbr/>(<a href="../../../uml2/ext/magicdraw/mdusecases/UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">UseCase</a> useCase)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Find and return a basic flow from given use case.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.ui.ElementFilter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getExcludeAuxiliaryResourceFilter()">getExcludeAuxiliaryResourceFilter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.ui.ElementFilter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getExcludeRelationshipElementFilter()">getExcludeRelationshipElementFilter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicreport.Image</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIconFor(com.nomagic.magicdraw.uml.BaseElement)">getIconFor</a><wbr/>(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return image icon for element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicreport.Image</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIconFor(com.nomagic.magicdraw.uml.BaseElement,boolean)">getIconFor</a><wbr/>(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 boolean allowDuplicate)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return image icon for element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicreport.Image</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIconFor(com.nomagic.magicdraw.uml.BaseElement,boolean,java.util.Map)">getIconFor</a><wbr/>(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 boolean allowDuplicate,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; iconProperty)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return image icon for element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicreport.Image</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIconFor(com.nomagic.magicdraw.uml.BaseElement,java.lang.String,java.lang.String,boolean)">getIconFor</a><wbr/>(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> prefix,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> suffix,
 boolean hashCode)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return image icon for element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicreport.Image</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIconFor(com.nomagic.magicdraw.uml.BaseElement,java.lang.String,java.lang.String,boolean,boolean)">getIconFor</a><wbr/>(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> prefix,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> suffix,
 boolean hashCode,
 boolean allowDuplicate)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return image icon for element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicreport.Image</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIconFor(com.nomagic.magicdraw.uml.BaseElement,java.lang.String,java.lang.String,boolean,boolean,java.util.Map)">getIconFor</a><wbr/>(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> prefix,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> suffix,
 boolean hashCode,
 boolean allowDuplicate,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; iconProperty)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return image icon for element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicreport.Image</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIconFor(com.nomagic.magicdraw.uml.BaseElement,java.lang.String,java.lang.String,boolean,java.util.Map)">getIconFor</a><wbr/>(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> prefix,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> suffix,
 boolean hashCode,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; iconProperty)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return image icon for element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicreport.Image</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIconFor(com.nomagic.magicdraw.uml.BaseElement,java.util.Map)">getIconFor</a><wbr/>(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; iconProperty)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return image icon for element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicreport.Image</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIconFor(java.lang.String)">getIconFor</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return image icon for element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicreport.Image</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIconFor(java.lang.String,java.lang.String,java.lang.String,boolean)">getIconFor</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> prefix,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> suffix,
 boolean hashCode)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return image icon for element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicreport.Image</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIconFor(java.lang.String,java.lang.String,java.lang.String,boolean,java.util.Map)">getIconFor</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> prefix,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> suffix,
 boolean hashCode,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; iconProperty)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return image icon for element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicreport.Image</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIconFor(java.lang.String,java.util.Map)">getIconFor</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; iconProperty)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return image icon for element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIconId(com.nomagic.magicdraw.uml.BaseElement,java.lang.String,java.lang.String,boolean,boolean,com.nomagic.ui.ResizableIcon)">getIconId</a><wbr/>(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> prefix,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> suffix,
 boolean hashCode,
 boolean allowDuplicate,
 <a href="../../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a> icon)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getImageFor(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getImageFor</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Create image from element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getImageFor(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,int)">getImageFor</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 int dpi)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Create image from element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getImageFor(java.lang.Object,boolean)">getImageFor</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object,
 boolean allowDuplicate)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Create image from object.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getImageFor(java.lang.Object,boolean,java.lang.String)">getImageFor</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object,
 boolean allowDuplicate,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> cannotRenderImageMsg)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Create image from object.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getImageFor(java.lang.Object,boolean,java.lang.String,int)">getImageFor</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object,
 boolean allowDuplicate,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> cannotRenderImageMsg,
 int dpi)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Create image from object.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIncludeUseCase(com.nomagic.uml2.ext.magicdraw.mdusecases.UseCase)">getIncludeUseCase</a><wbr/>(<a href="../../../uml2/ext/magicdraw/mdusecases/UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">UseCase</a> useCase)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets use case included element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getInnerElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getInnerElement</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a collection of inner element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getInteractionMessageType(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">getInteractionMessageType</a><wbr/>(<a href="../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets interaction message type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMetaClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getMetaClass</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get meta class of specific element</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMetaClass(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">getMetaClass</a><wbr/>(<a href="../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get stereotype meta class.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOwnedElementsIncludingAdditional(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">getOwnedElementsIncludingAdditional</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 boolean includePureOwned)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return owned elements of the given Element including additional owned elements defined in DSL specification by additionalContentProperty.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOwnedElementsIncludingAdditional(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,boolean)">getOwnedElementsIncludingAdditional</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 boolean includePureOwned,
 boolean excludeRelationship)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return owned elements of the given Element including additional owned elements defined in DSL specification by additionalContentProperty.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOwnedElementsIncludingAdditional(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,boolean,boolean)">getOwnedElementsIncludingAdditional</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 boolean includePureOwned,
 boolean excludeRelationship,
 boolean excludeAuxiliaryResources)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return owned elements of the given Element including additional owned elements defined in DSL specification by additionalContentProperty.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOwnedElementsIncludingAdditional(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,boolean,boolean,boolean)">getOwnedElementsIncludingAdditional</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 boolean includePureOwned,
 boolean excludeRelationship,
 boolean excludeAuxiliaryResources,
 boolean excludeInvisibleElement)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return owned elements of the given Element including additional owned elements defined in DSL specification by additionalContentProperty.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getPackageQualifiedName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,java.lang.String)">getPackageQualifiedName</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a> namedElement,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> separator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get a qualified name by consider only Package and given element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPackages(boolean)">getPackages</a><wbr/>(boolean includeSmartPackage)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPresentationDiagramElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">getPresentationDiagramElements</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets presentation element in the diagram.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPresentationDiagramElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,boolean)">getPresentationDiagramElements</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram,
 boolean includeNonManipulator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets presentation element in the diagram.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.magicreport.helper.Polygon</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPresentationElementBounds(com.nomagic.magicdraw.uml.symbols.PresentationElement)">getPresentationElementBounds</a><wbr/>(<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the bounds of this element in the form of a Polygon object.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.magicreport.helper.Polygon</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPresentationElementBounds(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.export.image.ImageExportResult)">getPresentationElementBounds</a><wbr/>(<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element,
 <a href="../../export/image/ImageExportResult.html" title="class in com.nomagic.magicdraw.export.image">ImageExportResult</a> exportResult)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the bounds of this element in the form of a Polygon object.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;com.nomagic.magicdraw.magicreport.helper.Polygon&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPresentationElementBounds(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getPresentationElementBounds</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the bounds of this element in the form of a Polygon object.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPresentationElementRectangle(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getPresentationElementRectangle</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the bounds of this element in the form of a Rectangle object.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getPresentationElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">getPresentationElements</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span> </div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">getProperty</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get the element property value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;com.nomagic.magicdraw.propertygroup.PropertyGroup&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPropertyGroupsByElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">getPropertyGroupsByElement</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 boolean addAlwaysVisible)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get set of <code>PropertyGroup</code> by specific element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.nomagic.magicdraw.propertygroup.PropertyGroup&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPropertyGroupsByStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)">getPropertyGroupsByStereotype</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a> stereotype)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get collection of <code>PropertyGroup</code> by specific stereotype.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../properties/Property.html" title="class in com.nomagic.magicdraw.properties">Property</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getQProperties(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">getQProperties</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get list of properties for element with DSL property groups, and each property group has its own property.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../properties/Property.html" title="class in com.nomagic.magicdraw.properties">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getQProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">getQProperty</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get a property for element with DSL property groups, and each property group has its own property.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getQualifiedName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,java.lang.String)">getQualifiedName</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a> namedElement,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> separator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get a qualified name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getQualifiedOwnerName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement)">getQualifiedOwnerName</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a> obj)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">result from this method is incorrect.</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRecievingOperationalNode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getRecievingOperationalNode</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get needline association ends.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getRelationship</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets direct relationships of specified element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">getRelationship</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 boolean recursive)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets direct relationships of specified element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,boolean)">getRelationship</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 boolean recursive,
 boolean includeIndirect)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets relationships of specified element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/mdusecases/Actor.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">Actor</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRelativeActor(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getRelativeActor</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets element relative actor.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRepresentationText(com.nomagic.magicdraw.uml.BaseElement)">getRepresentationText</a><wbr/>(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> e)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../ui/browser/Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getRootNodeOfContainmentTree(boolean)">getRootNodeOfContainmentTree</a><wbr/>(boolean startWithPrimaryModel)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get root node from containment tree.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../ui/browser/Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRootNodeOfDiagramTree()">getRootNodeOfDiagramTree</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get root node from diagram tree.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSendingOperationalNode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getSendingOperationalNode</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get needline association ends.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSlotProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">getSlotProperty</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> classifierName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get slot property by classifier name If there are more than one classifier matching with specified
 parameters, return only the property of first matching classifier.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSlotValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String)">getSlotValue</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> classifierName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> definingFeatureName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get slot value by classifier name and definingFeature name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String)">getStereotypeProperty</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets stereotype property.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,boolean)">getStereotypeProperty</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 boolean checkMultiplicity)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets stereotype property.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String)">getStereotypeProperty</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotypeName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets stereotype property.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String,boolean)">getStereotypeProperty</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotypeName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 boolean checkMultiplicity)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets stereotype property.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String,java.lang.String)">getStereotypeProperty</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> profileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotypeName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get Stereotype Property.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getStereotypePropertyList(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String)">getStereotypePropertyList</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotypeName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">value return from this method is improperly converted.</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getStereotypePropertyString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String)">getStereotypePropertyString</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets stereotype property as String value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getStereotypePropertyString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,java.lang.String)">getStereotypePropertyString</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> separator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets stereotype property as String value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getStereotypePropertyString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String)">getStereotypePropertyString</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotypeName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets stereotype property as String value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getStereotypePropertyString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String,java.lang.String)">getStereotypePropertyString</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> profileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotypeName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets stereotype property as String value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getStereotypePropertyString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String,java.lang.String,java.lang.String)">getStereotypePropertyString</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> profileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotypeName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> separator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets stereotype property as String value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getStereotypePropertyStringValue(java.lang.Object)">getStereotypePropertyStringValue</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">value return from this method is improperly converted.</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStereotypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getStereotypes</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets all stereotypes applied to element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSupplierElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getSupplierElement</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets relationship supplier.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTemplateFile(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getTemplateFile</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get template file from element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTemplateFile(java.lang.String,java.lang.String,java.lang.String,java.lang.Object)">getTemplateFile</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> templateFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> templateLocation,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> extension,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> marker)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get Template file from template file name/path.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getUCOwnerNumber(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getUCOwnerNumber</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return the use case number or use case ID of element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getUsageElements(java.util.Map,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getUsageElements</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;com.nomagic.magicdraw.uml.DependencyType&gt;&gt; usagesMap,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the element usages from usage map.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getUsageRepresentationText(com.nomagic.magicdraw.uml.BaseElement,boolean)">getUsageRepresentationText</a><wbr/>(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> be,
 boolean addFullPath)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Formats the usage subject.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;com.nomagic.magicdraw.uml.DependencyType&gt;&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getUsages(java.lang.Object)">getUsages</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> selectedObjects)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns Usage Map of MD and then use getUsageElements method for returning the usage of the specified
 element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getUseCaseAssociatedElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getUseCaseAssociatedElement</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> obj)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span> </div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getUseCaseNumber(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getUseCaseNumber</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return the use case number or use case ID of element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getUsedBy(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getUsedBy</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a list of element used by this element (except diagram).</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.ui.ElementFilter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getVisibleElementFilter()">getVisibleElementFilter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#hasBaseClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.lang.String)">hasBaseClassifier</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> baseClassifier)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if element has base classifier with given name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hasProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">hasProperty</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns true when a property with a given name is specified on this element, false otherwise.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hasStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">hasStereotype</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if element has stereotypes.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#hasStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">hasStereotype</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotype)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">See <a href="#containsStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)"><code>containsStereotype(Element, String)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isAssignableFrom(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">isAssignableFrom</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> classTypeName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">A function for checking super type of the specific element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isAttachedFile(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isAttachedFile</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check if element is attached file.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isAttachedImage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isAttachedImage</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check if element is attached image.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isDerivedClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">isDerivedClassifier</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> parent,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> child)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if child is derived from parent by generalization.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isEmpty(java.lang.Object)">isEmpty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Test and return true if object is null, empty string or empty collection.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isEmpty(java.lang.Object,boolean)">isEmpty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj,
 boolean isIgnoreSpace)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Test and return true if object is null, empty string or empty collection.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isInvisibleElement(com.nomagic.magicdraw.uml.BaseElement)">isInvisibleElement</a><wbr/>(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isInvisibleElement(com.nomagic.magicdraw.uml.BaseElement,boolean)">isInvisibleElement</a><wbr/>(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 boolean isTypeFilter)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isInvisibleElement(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.ui.ElementFilter)">isInvisibleElement</a><wbr/>(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 com.nomagic.magicdraw.ui.ElementFilter elementFilter)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isNamedElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isNamedElement</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns whether the element an <code>NamedElement</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isNull(java.lang.Object)">isNull</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Test and return true if object is null.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isRelationship</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Test and return true if element is relationship.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isTypeOf(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">isTypeOf</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> typeName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">A function for checking super type of the specific element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isTypeOf(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,boolean)">isTypeOf</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> typeName,
 boolean checkClassTypeName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">A function for checking super type of the specific element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#parseObjectForPrinting(java.lang.Object)">parseObjectForPrinting</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Parses Strings and Collections of Strings</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.magicreport.helper.Hyperlink</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#serialize(com.nomagic.magicdraw.hyperlinks.Hyperlink)">serialize</a><wbr/>(<a href="../../hyperlinks/Hyperlink.html" title="interface in com.nomagic.magicdraw.hyperlinks">Hyperlink</a> hyperlink)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Convert <code>com.nomagic.magicdraw.hyperlinks.Hyperlink</code> to <code>Hyperlink</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setActiveValidationEnabled(boolean)">setActiveValidationEnabled</a><wbr/>(boolean enable)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#trimString(java.lang.String)">trimString</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> s)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">replaced with $s.trim()</div>
</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.engine.Tool">Methods inherited from class com.nomagic.magicreport.engine.Tool</h3>
<code>clone, getContext, getProperties, getProperty, getProperty, notifyObservers, setContext, setProperties</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.Observable">Methods inherited from class java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html" title="class or interface in java.util">Observable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#addObserver(java.util.Observer)" title="class or interface in java.util">addObserver</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#clearChanged()" title="class or interface in java.util">clearChanged</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#countObservers()" title="class or interface in java.util">countObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#deleteObserver(java.util.Observer)" title="class or interface in java.util">deleteObserver</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#deleteObservers()" title="class or interface in java.util">deleteObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#hasChanged()" title="class or interface in java.util">hasChanged</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#notifyObservers()" title="class or interface in java.util">notifyObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#setChanged()" title="class or interface in java.util">setChanged</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.engine.ITool">Methods inherited from interface com.nomagic.magicreport.engine.ITool</h3>
<code>clearTool</code></div>
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
<section class="detail" id="ICON_PROPERTY_RETINASCALING">
<h3>ICON_PROPERTY_RETINASCALING</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ICON_PROPERTY_RETINASCALING</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.magicreport.helper.ReportHelper.ICON_PROPERTY_RETINASCALING">Constant Field Values</a></li>
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
<section class="detail" id="&lt;init&gt;()">
<h3>ReportHelper</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ReportHelper</span>()</div>
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
<section class="detail" id="getDSLProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>getDSLProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getDSLProperty</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</span></div>
<div class="block">Get DSL Property.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element.</dd>
<dd><code>propertyName</code> - the property name.</dd>
<dt>Returns:</dt>
<dd>the property value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String)">
<h3>getStereotypeProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getStereotypeProperty</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotypeName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</span></div>
<div class="block">Gets stereotype property.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element.</dd>
<dd><code>stereotypeName</code> - the stereotype name.</dd>
<dd><code>propertyName</code> - the property name.</dd>
<dt>Returns:</dt>
<dd>the property value.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#getStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String)"><code>getStereotypeProperty(Element, Stereotype, String)</code></a></li>
<li><a href="#getStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String,java.lang.String)"><code>getStereotypeProperty(Element, String, String, String)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String,boolean)">
<h3>getStereotypeProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getStereotypeProperty</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotypeName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 boolean checkMultiplicity)</span></div>
<div class="block">Gets stereotype property.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element.</dd>
<dd><code>stereotypeName</code> - the stereotype name.</dd>
<dd><code>propertyName</code> - the property name.</dd>
<dd><code>checkMultiplicity</code> - check multiplicity before return value</dd>
<dt>Returns:</dt>
<dd>the property value.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#getStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String)"><code>getStereotypeProperty(Element, Stereotype, String)</code></a></li>
<li><a href="#getStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String,java.lang.String)"><code>getStereotypeProperty(Element, String, String, String)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="parseObjectForPrinting(java.lang.Object)">
<h3>parseObjectForPrinting</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">parseObjectForPrinting</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">Parses Strings and Collections of Strings</div>
</section>
</li>
<li>
<section class="detail" id="getStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String)">
<h3>getStereotypeProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getStereotypeProperty</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</span></div>
<div class="block">Gets stereotype property.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element.</dd>
<dd><code>stereotype</code> - the stereotype.</dd>
<dd><code>propertyName</code> - the property name.</dd>
<dt>Returns:</dt>
<dd>the property value.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#getStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String)"><code>getStereotypeProperty(Element, String, String)</code></a></li>
<li><a href="#getStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String,java.lang.String)"><code>getStereotypeProperty(Element, String, String, String)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,boolean)">
<h3>getStereotypeProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getStereotypeProperty</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 boolean checkMultiplicity)</span></div>
<div class="block">Gets stereotype property.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element.</dd>
<dd><code>stereotype</code> - the stereotype.</dd>
<dd><code>propertyName</code> - the property name.</dd>
<dd><code>checkMultiplicity</code> - check multiplicity before return value</dd>
<dt>Returns:</dt>
<dd>the property value.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#getStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String)"><code>getStereotypeProperty(Element, String, String)</code></a></li>
<li><a href="#getStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String,java.lang.String)"><code>getStereotypeProperty(Element, String, String, String)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String,java.lang.String)">
<h3>getStereotypeProperty</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getStereotypeProperty</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> profileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotypeName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</span></div>
<div class="block">Get Stereotype Property.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element.</dd>
<dd><code>profileName</code> - profile name</dd>
<dd><code>stereotypeName</code> - the stereotype name.</dd>
<dd><code>propertyName</code> - the property name.</dd>
<dt>Returns:</dt>
<dd>the property value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStereotypePropertyList(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String)">
<h3>getStereotypePropertyList</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</span> <span class="element-name">getStereotypePropertyList</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotypeName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">value return from this method is improperly converted.</div>
</div>
<div class="block">Gets stereotype property value as list of strings.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element with assigned stereotype</dd>
<dd><code>stereotypeName</code> - stereotype name</dd>
<dd><code>propertyName</code> - name of the property</dd>
<dt>Returns:</dt>
<dd>List of the property name.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStereotypePropertyString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String)">
<h3>getStereotypePropertyString</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getStereotypePropertyString</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotypeName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</span></div>
<div class="block">Gets stereotype property as String value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element instance</dd>
<dd><code>stereotypeName</code> - the stereotype name</dd>
<dd><code>propertyName</code> - the property name</dd>
<dt>Returns:</dt>
<dd>the value as String</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStereotypePropertyString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String)">
<h3>getStereotypePropertyString</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getStereotypePropertyString</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</span></div>
<div class="block">Gets stereotype property as String value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element instance</dd>
<dd><code>stereotype</code> - the stereotype instance</dd>
<dd><code>propertyName</code> - the property name</dd>
<dt>Returns:</dt>
<dd>the value as String</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStereotypePropertyString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,java.lang.String)">
<h3>getStereotypePropertyString</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getStereotypePropertyString</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> separator)</span></div>
<div class="block">Gets stereotype property as String value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element instance</dd>
<dd><code>stereotype</code> - the stereotype instance</dd>
<dd><code>propertyName</code> - the property name</dd>
<dd><code>separator</code> - when property value is list, the string will be added when convert list to string</dd>
<dt>Returns:</dt>
<dd>the value as String</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStereotypePropertyString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String,java.lang.String)">
<h3>getStereotypePropertyString</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getStereotypePropertyString</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> profileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotypeName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</span></div>
<div class="block">Gets stereotype property as String value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element instance</dd>
<dd><code>profileName</code> - profile name</dd>
<dd><code>stereotypeName</code> - the stereotype name</dd>
<dd><code>propertyName</code> - the property name</dd>
<dt>Returns:</dt>
<dd>the value as String</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStereotypePropertyString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String,java.lang.String,java.lang.String)">
<h3>getStereotypePropertyString</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getStereotypePropertyString</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> profileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotypeName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> separator)</span></div>
<div class="block">Gets stereotype property as String value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element instance</dd>
<dd><code>profileName</code> - profile name</dd>
<dd><code>stereotypeName</code> - the stereotype name</dd>
<dd><code>propertyName</code> - the property name</dd>
<dd><code>separator</code> - when property value is list, the string will be added when convert list to string</dd>
<dt>Returns:</dt>
<dd>the value as String</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStereotypePropertyStringValue(java.lang.Object)">
<h3>getStereotypePropertyStringValue</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getStereotypePropertyStringValue</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">value return from this method is improperly converted.</div>
</div>
<div class="block">Gets Stereotype Property As String value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>o</code> - the property</dd>
<dt>Returns:</dt>
<dd>the value as String</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRepresentationText(com.nomagic.magicdraw.uml.BaseElement)">
<h3>getRepresentationText</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getRepresentationText</span><wbr/><span class="parameters">(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> e)</span></div>
</section>
</li>
<li>
<section class="detail" id="isNamedElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isNamedElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isNamedElement</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Returns whether the element an <code>NamedElement</code>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to test</dd>
<dt>Returns:</dt>
<dd>true if given element is <code>NamedElement</code>; otherwise false</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAppliedStereotypeByString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>getAppliedStereotypeByString</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getAppliedStereotypeByString</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotype)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">See <a href="#getAppliedStereotypeByName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)"><code>getAppliedStereotypeByName(Element, String)</code></a></div>
</div>
<div class="block">Returns stereotype assigned to element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>stereotype</code> - name of stereotype</dd>
<dt>Returns:</dt>
<dd>assigned stereotype with that name.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAppliedStereotypeByName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>getAppliedStereotypeByName</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getAppliedStereotypeByName</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotypeName)</span></div>
<div class="block">Returns stereotype assigned to element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>stereotypeName</code> - name of stereotype</dd>
<dt>Returns:</dt>
<dd>assigned stereotype with that name.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>hasStereotype</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">hasStereotype</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotype)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">See <a href="#containsStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)"><code>containsStereotype(Element, String)</code></a></div>
</div>
<div class="block">Checks if element has assigned stereotype with given name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to check</dd>
<dd><code>stereotype</code> - stereotype name to check</dd>
<dt>Returns:</dt>
<dd>true if element has assigned stereotype with given name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="containsStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>containsStereotype</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">containsStereotype</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotypeName)</span></div>
<div class="block">Returns true if element contains a stereotype (include all derived stereotype) for the specified stereotype
 name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to test</dd>
<dd><code>stereotypeName</code> - stereotype name to be tested</dd>
<dt>Returns:</dt>
<dd>true if element contains a stereotype for the specified stereotype name.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#containsStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,boolean)"><code>containsStereotype(Element, String, boolean)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="containsStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,boolean)">
<h3>containsStereotype</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">containsStereotype</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotypeName,
 boolean includeDerived)</span></div>
<div class="block">Returns true if element contains a stereotype for the specified stereotype name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to test</dd>
<dd><code>stereotypeName</code> - stereotype name to be tested</dd>
<dd><code>includeDerived</code> - true if search target include all derived stereotypes; otherwise false</dd>
<dt>Returns:</dt>
<dd>true if element contains a stereotype for the specified stereotype name.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#containsStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)"><code>containsStereotype(Element, String)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>hasProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">hasProperty</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</span></div>
<div class="block">Returns true when a property with a given name is specified on this element, false otherwise.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to test</dd>
<dd><code>propertyName</code> - property name</dd>
<dt>Returns:</dt>
<dd>true when a property with a given name is specified on this element, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>getProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getProperty</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</span>
                   throws <span class="exceptions">com.nomagic.magicdraw.magicreport.helper.PropertyNotFoundException</span></div>
<div class="block">Get the element property value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the object that will be gotten that data.</dd>
<dd><code>propertyName</code> - the field of the element.</dd>
<dt>Returns:</dt>
<dd>the data of that field in the element.</dd>
<dt>Throws:</dt>
<dd><code>com.nomagic.magicdraw.magicreport.helper.PropertyNotFoundException</code> - when a request property name is not found on target element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStereotypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getStereotypes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt;</span> <span class="element-name">getStereotypes</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span>
                                throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></span></div>
<div class="block">Gets all stereotypes applied to element. This method is replaced with $element.appliedStereotype.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element</dd>
<dt>Returns:</dt>
<dd>the stereotype instances</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - from <code>StereotypesHelper.getStereotypes</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>hasStereotype</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">hasStereotype</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span>
                      throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></span></div>
<div class="block">Checks if element has stereotypes.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to check</dd>
<dt>Returns:</dt>
<dd>true if has</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if element is null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findElementInCollection(java.util.Collection,java.lang.String)">
<h3>findElementInCollection</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">findElementInCollection</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; col,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> elementName)</span></div>
<div class="block">Search and return the element in the collection by element name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>col</code> - the collection of elements</dd>
<dd><code>elementName</code> - the name of element</dd>
<dt>Returns:</dt>
<dd>the element instance, If it does not find, it will return null.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findDiagramByName(java.lang.String)">
<h3>findDiagramByName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">findDiagramByName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> elementName)</span></div>
</section>
</li>
<li>
<section class="detail" id="findElementByName(java.util.Collection,java.lang.String)">
<h3>findElementByName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">findElementByName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; source,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> regex)</span></div>
<div class="block">Search and return the elements from name by regular expression.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>source</code> - source</dd>
<dd><code>regex</code> - the regular expression to which name is to be matched</dd>
<dt>Returns:</dt>
<dd>collection of matches element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDerivedClassifiers(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">
<h3>getDerivedClassifiers</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;</span> <span class="element-name">getDerivedClassifiers</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> parentClassifier)</span></div>
<div class="block">Returns classifier derived elements.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parentClassifier</code> - the parent class</dd>
<dt>Returns:</dt>
<dd>collection of derived elements (classifiers)</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasBaseClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.lang.String)">
<h3>hasBaseClassifier</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">hasBaseClassifier</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> baseClassifier)</span></div>
<div class="block">Checks if element has base classifier with given name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifier</code> - the classifier</dd>
<dd><code>baseClassifier</code> - base classifier name</dd>
<dt>Returns:</dt>
<dd>true if the element contains specific base classifiers.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBaseClassifiers(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">
<h3>getBaseClassifiers</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;</span> <span class="element-name">getBaseClassifiers</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier)</span></div>
<div class="block">Return classifier based elements. The list contains all base classifiers include all its derived
 classifiers.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifier</code> - the classifier</dd>
<dt>Returns:</dt>
<dd>collection of based elements (classifiers)</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getComment(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getComment</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getComment</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Returns documentation of given element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element which will be gotten the name.</dd>
<dt>Returns:</dt>
<dd>the document</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getElementComment(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getElementComment</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Comment.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Comment</a></span> <span class="element-name">getElementComment</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Returns comment annotated to this element. If comment is attached to this element, returns null.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element which will be gotten the Comment.</dd>
<dt>Returns:</dt>
<dd>Comment instance of this element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRelativeActor(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getRelativeActor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/mdusecases/Actor.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">Actor</a>&gt;</span> <span class="element-name">getRelativeActor</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Gets element relative actor.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element</dd>
<dt>Returns:</dt>
<dd>the collection of Actor.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUseCaseAssociatedElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getUseCaseAssociatedElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getUseCaseAssociatedElement</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> obj)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Gets associated Element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>obj</code> - the element that we would like to find the other part</dd>
<dt>Returns:</dt>
<dd>the other parts</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIncludeUseCase(com.nomagic.uml2.ext.magicdraw.mdusecases.UseCase)">
<h3>getIncludeUseCase</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getIncludeUseCase</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/mdusecases/UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">UseCase</a> useCase)</span></div>
<div class="block">Gets use case included element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>useCase</code> - the UseCase instance</dd>
<dt>Returns:</dt>
<dd>the collection of included use case.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="trimString(java.lang.String)">
<h3>trimString</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">trimString</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> s)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">replaced with $s.trim()</div>
</div>
<div class="block">Trim string.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>s</code> - the String</dd>
<dt>Returns:</dt>
<dd>the trimmed String</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createValueSpecificationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)">
<h3>createValueSpecificationText</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createValueSpecificationText</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> specification)</span></div>
<div class="block">Create text represents the ValueSpecification element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>specification</code> - The given ValueSpecification.</dd>
<dt>Returns:</dt>
<dd>the String value for ValueSpecification</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPresentationElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">
<h3>getPresentationElements</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">getPresentationElements</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Gets presentation element in the diagram. This method equivalent to
 <a href="#getPresentationDiagramElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)"><code>getPresentationDiagramElements(Diagram)</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - the diagram instance.</dd>
<dt>Returns:</dt>
<dd>the collection of elements.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#getPresentationDiagramElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)"><code>getPresentationDiagramElements(Diagram)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPresentationDiagramElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">
<h3>getPresentationDiagramElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">getPresentationDiagramElements</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</span></div>
<div class="block">Gets presentation element in the diagram. This method will return all presentation elements from diagram
 except non-manipulator symbols.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - the diagram instance.</dd>
<dt>Returns:</dt>
<dd>the collection of elements.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#getPresentationDiagramElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,boolean)"><code>getPresentationDiagramElements(Diagram, boolean)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPresentationDiagramElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,boolean)">
<h3>getPresentationDiagramElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">getPresentationDiagramElements</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram,
 boolean includeNonManipulator)</span></div>
<div class="block">Gets presentation element in the diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - the diagram instance.</dd>
<dd><code>includeNonManipulator</code> - true for include all non-manipulator element.</dd>
<dt>Returns:</dt>
<dd>the collection of elements.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#getPresentationDiagramElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)"><code>getPresentationDiagramElements(Diagram)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPresentationElementBounds(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>getPresentationElementBounds</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.magicreport.helper.Polygon</span> <span class="element-name">getPresentationElementBounds</span><wbr/><span class="parameters">(<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element)</span></div>
<div class="block">Gets the bounds of this element in the form of a Polygon object. The bounds specify this component's
 coordinate to its diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the presentation element on diagram.</dd>
<dt>Returns:</dt>
<dd>the bound of element as Polygon</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPresentationElementBounds(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.export.image.ImageExportResult)">
<h3>getPresentationElementBounds</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.magicreport.helper.Polygon</span> <span class="element-name">getPresentationElementBounds</span><wbr/><span class="parameters">(<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element,
 <a href="../../export/image/ImageExportResult.html" title="class in com.nomagic.magicdraw.export.image">ImageExportResult</a> exportResult)</span></div>
<div class="block">Gets the bounds of this element in the form of a Polygon object. The bounds specify this component's
 coordinate to its diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the presentation element on diagram.</dd>
<dt>Returns:</dt>
<dd>the bound of element as Polygon</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPresentationElementRectangle(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getPresentationElementRectangle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a>&gt;</span> <span class="element-name">getPresentationElementRectangle</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Gets the bounds of this element in the form of a Rectangle object. The bounds specify this component's
 coordinate to its diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - the target diagram.</dd>
<dd><code>element</code> - the presentation element on given diagram.</dd>
<dt>Returns:</dt>
<dd>the bound of element as Rectangle. If element is not found in the diagram, it will return null.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPresentationElementBounds(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getPresentationElementBounds</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;com.nomagic.magicdraw.magicreport.helper.Polygon&gt;</span> <span class="element-name">getPresentationElementBounds</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Gets the bounds of this element in the form of a Polygon object. The bounds specify this component's
 coordinate to its diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - the target diagram.</dd>
<dd><code>element</code> - the presentation element on given diagram.</dd>
<dt>Returns:</dt>
<dd>the bound of element as Polygon. If element is not found in the diagram, it will return null.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">
<h3>getDiagramType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDiagramType</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</span></div>
<div class="block">Gets diagram type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - the diagram instance.</dd>
<dt>Returns:</dt>
<dd>the type of diagram.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMetaClass(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">
<h3>getMetaClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a>&gt;</span> <span class="element-name">getMetaClass</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</span></div>
<div class="block">Get stereotype meta class.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stereotype</code> - the stereotype</dd>
<dt>Returns:</dt>
<dd>the collection of Meta Class</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMetaClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getMetaClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getMetaClass</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Get meta class of specific element</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dt>Returns:</dt>
<dd>a Meta Class or Collection of Meta Class</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">
<h3>getDiagramElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getDiagramElements</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</span></div>
<div class="block">Gets elements from this diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - the target diagram.</dd>
<dt>Returns:</dt>
<dd>the collection of elements.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramElements(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement)">
<h3>getDiagramElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getDiagramElements</span><wbr/><span class="parameters">(<a href="../../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a> diagram)</span></div>
<div class="block">Gets presentation elements from this diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - the target diagram.</dd>
<dt>Returns:</dt>
<dd>the collection of elements.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getQualifiedOwnerName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement)">
<h3>getQualifiedOwnerName</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getQualifiedOwnerName</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a> obj)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">result from this method is incorrect. Use $element.owner.qualifiedName</div>
</div>
<div class="block">Get qualified owner name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>obj</code> - the object instance</dd>
<dt>Returns:</dt>
<dd>the qualified owner name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getQualifiedName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,java.lang.String)">
<h3>getQualifiedName</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getQualifiedName</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a> namedElement,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> separator)</span></div>
<div class="block">Get a qualified name. Qualified is a name which allows the NamedElement to be identified within a hierarchy
 of nested Namespaces. It is constructed from the names of the containing namespaces starting at the root of
 the hierarchy and ending with the name of the NamedElement itself.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>namedElement</code> - NamedElement</dd>
<dd><code>separator</code> - separator symbol. If value is null or empty string, the '::' will be used.</dd>
<dt>Returns:</dt>
<dd>a qualified name.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPackageQualifiedName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,java.lang.String)">
<h3>getPackageQualifiedName</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getPackageQualifiedName</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a> namedElement,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> separator)</span></div>
<div class="block">Get a qualified name by consider only Package and given element. Model and Profile will not be included on
 the qualified name.
 <p>
 For example: The element hierarchy is <code><pre>
        Design : Model -&gt; com : Package -&gt; nomagic : Package -&gt; ui -&gt; Package -&gt; BaseDialog : Class
 </pre></code> When template code is: <code><pre>
    $report.getPackageQualifiedName($class, ".")
 </pre></code> Where $class is "BaseDialog" element, the result from above code will be: <code><pre>
    com.nomagic.ui.BaseDialog
 </pre></code>
</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>namedElement</code> - NamedElement</dd>
<dd><code>separator</code> - separator symbol. If value is null or empty string, the '::' will be used.</dd>
<dt>Returns:</dt>
<dd>a qualified name.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="serialize(com.nomagic.magicdraw.hyperlinks.Hyperlink)">
<h3>serialize</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.magicreport.helper.Hyperlink</span> <span class="element-name">serialize</span><wbr/><span class="parameters">(<a href="../../hyperlinks/Hyperlink.html" title="interface in com.nomagic.magicdraw.hyperlinks">Hyperlink</a> hyperlink)</span></div>
<div class="block">Convert <code>com.nomagic.magicdraw.hyperlinks.Hyperlink</code> to <code>Hyperlink</code>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>hyperlink</code> - the magicdraw hyperlink</dd>
<dt>Returns:</dt>
<dd>the magic report hyperlink instance</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSendingOperationalNode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getSendingOperationalNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getSendingOperationalNode</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Get needline association ends.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dt>Returns:</dt>
<dd>needline association ends</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRecievingOperationalNode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getRecievingOperationalNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getRecievingOperationalNode</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Get needline association ends.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dt>Returns:</dt>
<dd>needline association ends</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)">
<h3>findRelationship</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">findRelationship</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> modelPackage)</span></div>
<div class="block">Search and return a collection of relationship element inside package.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>modelPackage</code> - package element</dd>
<dt>Returns:</dt>
<dd>Collection of relationship in this package</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,boolean)">
<h3>findRelationship</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">findRelationship</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> modelPackage,
 boolean recursive)</span></div>
<div class="block">Search and return a collection of relationship element inside package.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>modelPackage</code> - package element</dd>
<dd><code>recursive</code> - if true, perform recursively</dd>
<dt>Returns:</dt>
<dd>Collection of relationship in this package</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getRelationship</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getRelationship</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Gets direct relationships of specified element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - Element element to be collect</dd>
<dt>Returns:</dt>
<dd>Collection of relationship</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">
<h3>getRelationship</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getRelationship</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 boolean recursive)</span></div>
<div class="block">Gets direct relationships of specified element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - Element element to be collect</dd>
<dd><code>recursive</code> - if true, perform recursively</dd>
<dt>Returns:</dt>
<dd>Collection of relationship</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,boolean)">
<h3>getRelationship</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getRelationship</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 boolean recursive,
 boolean includeIndirect)</span></div>
<div class="block">Gets relationships of specified element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to be collect</dd>
<dd><code>recursive</code> - if true, perform recursively</dd>
<dd><code>includeIndirect</code> - true to include indirect relationships</dd>
<dt>Returns:</dt>
<dd>Collection of relationship</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="collectRelationships(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>collectRelationships</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">collectRelationships</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Gets direct relationships of specified element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - Element element to be collect</dd>
<dt>Returns:</dt>
<dd>Collection of relationship</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="collectRelationships(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">
<h3>collectRelationships</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">collectRelationships</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 boolean includeIndirect)</span></div>
<div class="block">Gets relationships of specified element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to be collect</dd>
<dd><code>includeIndirect</code> - true to include indirect relationships</dd>
<dt>Returns:</dt>
<dd>Collection of relationship</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="collectRelationships(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,boolean)">
<h3>collectRelationships</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">collectRelationships</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 boolean includeIndirect,
 boolean isRecursive)</span></div>
<div class="block">Gets relationships of specified element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to be collect</dd>
<dd><code>includeIndirect</code> - true to include indirect relationships</dd>
<dd><code>isRecursive</code> - if true, perform recursively</dd>
<dt>Returns:</dt>
<dd>Collection of relationship</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getClientElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getClientElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getClientElement</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Gets relationship client.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - relationship model element.</dd>
<dt>Returns:</dt>
<dd>client element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSupplierElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getSupplierElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getSupplierElement</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Gets relationship supplier.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - relationship model element.</dd>
<dt>Returns:</dt>
<dd>supplier element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInnerElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getInnerElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getInnerElement</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Return a collection of inner element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - Element element to be collect</dd>
<dt>Returns:</dt>
<dd>Collection of inner</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIconFor(com.nomagic.magicdraw.uml.BaseElement)">
<h3>getIconFor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicreport.Image</span> <span class="element-name">getIconFor</span><wbr/><span class="parameters">(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</span></div>
<div class="block">Return image icon for element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - a Magic Draw element</dd>
<dt>Returns:</dt>
<dd>Image object for element's icon</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIconFor(com.nomagic.magicdraw.uml.BaseElement,java.util.Map)">
<h3>getIconFor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicreport.Image</span> <span class="element-name">getIconFor</span><wbr/><span class="parameters">(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; iconProperty)</span></div>
<div class="block">Return image icon for element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - a Magic Draw element</dd>
<dd><code>iconProperty</code> - custom property to create icon</dd>
<dt>Returns:</dt>
<dd>Image object for element's icon</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIconFor(com.nomagic.magicdraw.uml.BaseElement,boolean)">
<h3>getIconFor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicreport.Image</span> <span class="element-name">getIconFor</span><wbr/><span class="parameters">(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 boolean allowDuplicate)</span></div>
<div class="block">Return image icon for element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - a Magic Draw element</dd>
<dd><code>allowDuplicate</code> - true to always create new icon and don't keep the icon in map</dd>
<dt>Returns:</dt>
<dd>Image object for element's icon</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIconFor(com.nomagic.magicdraw.uml.BaseElement,boolean,java.util.Map)">
<h3>getIconFor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicreport.Image</span> <span class="element-name">getIconFor</span><wbr/><span class="parameters">(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 boolean allowDuplicate,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; iconProperty)</span></div>
<div class="block">Return image icon for element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - a Magic Draw element</dd>
<dd><code>allowDuplicate</code> - true to always create new icon and don't keep the icon in map</dd>
<dd><code>iconProperty</code> - custom property to create icon</dd>
<dt>Returns:</dt>
<dd>Image object for element's icon</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIconFor(com.nomagic.magicdraw.uml.BaseElement,java.lang.String,java.lang.String,boolean)">
<h3>getIconFor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicreport.Image</span> <span class="element-name">getIconFor</span><wbr/><span class="parameters">(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> prefix,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> suffix,
 boolean hashCode)</span></div>
<div class="block">Return image icon for element. In case of <code>hashCode</code> equals true, icon's name format is set to
 "icon_"+hash code and doesn't include prefix/suffix.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - a MagicDraw element</dd>
<dd><code>prefix</code> - prefix for icon's name</dd>
<dd><code>suffix</code> - suffix for icon's name</dd>
<dd><code>hashCode</code> - uses hash code in icon's name</dd>
<dt>Returns:</dt>
<dd>Image object for element's icon</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIconFor(com.nomagic.magicdraw.uml.BaseElement,java.lang.String,java.lang.String,boolean,java.util.Map)">
<h3>getIconFor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicreport.Image</span> <span class="element-name">getIconFor</span><wbr/><span class="parameters">(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> prefix,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> suffix,
 boolean hashCode,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; iconProperty)</span></div>
<div class="block">Return image icon for element. In case of <code>hashCode</code> equals true, icon's name format is set to
 "icon_"+hash code and doesn't include prefix/suffix.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - a MagicDraw element</dd>
<dd><code>prefix</code> - prefix for icon's name</dd>
<dd><code>suffix</code> - suffix for icon's name</dd>
<dd><code>hashCode</code> - uses hash code in icon's name</dd>
<dd><code>iconProperty</code> - custom property to create icon</dd>
<dt>Returns:</dt>
<dd>Image object for element's icon</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIconFor(com.nomagic.magicdraw.uml.BaseElement,java.lang.String,java.lang.String,boolean,boolean)">
<h3>getIconFor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicreport.Image</span> <span class="element-name">getIconFor</span><wbr/><span class="parameters">(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> prefix,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> suffix,
 boolean hashCode,
 boolean allowDuplicate)</span></div>
<div class="block">Return image icon for element. In case of <code>hashCode</code> equals true, icon's name format is set to
 "icon_"+hash code and doesn't include prefix/suffix.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - a MagicDraw element</dd>
<dd><code>prefix</code> - prefix for icon's name</dd>
<dd><code>suffix</code> - suffix for icon's name</dd>
<dd><code>hashCode</code> - uses hash code in icon's name</dd>
<dd><code>allowDuplicate</code> - true to always create new icon and don't keep the icon in map</dd>
<dt>Returns:</dt>
<dd>Image object for element's icon</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIconId(com.nomagic.magicdraw.uml.BaseElement,java.lang.String,java.lang.String,boolean,boolean,com.nomagic.ui.ResizableIcon)">
<h3>getIconId</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getIconId</span><wbr/><span class="parameters">(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> prefix,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> suffix,
 boolean hashCode,
 boolean allowDuplicate,
 <a href="../../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a> icon)</span></div>
</section>
</li>
<li>
<section class="detail" id="getIconFor(com.nomagic.magicdraw.uml.BaseElement,java.lang.String,java.lang.String,boolean,boolean,java.util.Map)">
<h3>getIconFor</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicreport.Image</span> <span class="element-name">getIconFor</span><wbr/><span class="parameters">(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> prefix,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> suffix,
 boolean hashCode,
 boolean allowDuplicate,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; iconProperty)</span></div>
<div class="block">Return image icon for element. In case of <code>hashCode</code> equals true, icon's name format is set to
 "icon_"+hash code and doesn't include prefix/suffix.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - a MagicDraw element</dd>
<dd><code>prefix</code> - prefix for icon's name</dd>
<dd><code>suffix</code> - suffix for icon's name</dd>
<dd><code>hashCode</code> - uses hash code in icon's name</dd>
<dd><code>allowDuplicate</code> - true to always create new icon and don't keep the icon in map</dd>
<dd><code>iconProperty</code> - custom property to create icon</dd>
<dt>Returns:</dt>
<dd>Image object for element's icon</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIconFor(java.lang.String)">
<h3>getIconFor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicreport.Image</span> <span class="element-name">getIconFor</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type)</span></div>
<div class="block">Return image icon for element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - element type</dd>
<dt>Returns:</dt>
<dd>Image object for element's icon</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIconFor(java.lang.String,java.util.Map)">
<h3>getIconFor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicreport.Image</span> <span class="element-name">getIconFor</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; iconProperty)</span></div>
<div class="block">Return image icon for element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - element type</dd>
<dt>Returns:</dt>
<dd>Image object for element's icon</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIconFor(java.lang.String,java.lang.String,java.lang.String,boolean)">
<h3>getIconFor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicreport.Image</span> <span class="element-name">getIconFor</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> prefix,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> suffix,
 boolean hashCode)</span></div>
<div class="block">Return image icon for element. In case of <code>hashCode</code> equals true, icon's name format is set to
 "icon_"+hash code and doesn't include prefix/suffix.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - element type</dd>
<dd><code>prefix</code> - prefix for icon's name</dd>
<dd><code>suffix</code> - suffix for icon's name</dd>
<dd><code>hashCode</code> - uses hash code in icon's name</dd>
<dt>Returns:</dt>
<dd>Image object for element's icon</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIconFor(java.lang.String,java.lang.String,java.lang.String,boolean,java.util.Map)">
<h3>getIconFor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicreport.Image</span> <span class="element-name">getIconFor</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> prefix,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> suffix,
 boolean hashCode,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; iconProperty)</span></div>
<div class="block">Return image icon for element. In case of <code>hashCode</code> equals true, icon's name format is set to
 "icon_"+hash code and doesn't include prefix/suffix.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - element type</dd>
<dd><code>prefix</code> - prefix for icon's name</dd>
<dd><code>suffix</code> - suffix for icon's name</dd>
<dd><code>hashCode</code> - uses hash code in icon's name</dd>
<dd><code>iconProperty</code> - custom property to create icon</dd>
<dt>Returns:</dt>
<dd>Image object for element's icon</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCustomImage(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>getCustomImage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicreport.Image</span> <span class="element-name">getCustomImage</span><wbr/><span class="parameters">(<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> presentationElement)</span></div>
<div class="block">Return original image of Image property from presentationElement</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>presentationElement</code> - a presentationElement</dd>
<dt>Returns:</dt>
<dd>original image in Image property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCustomImage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getCustomImage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicreport.Image</span> <span class="element-name">getCustomImage</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Return original image of Image property</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - an element</dd>
<dt>Returns:</dt>
<dd>original image in Image property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCustomImageInformation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getCustomImageInformation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/jmi/helpers/ElementImageHelper.ImageInformation.html" title="class in com.nomagic.uml2.ext.jmi.helpers">ElementImageHelper.ImageInformation</a></span> <span class="element-name">getCustomImageInformation</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Return a CustomImageHolder information</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dt>Returns:</dt>
<dd>CustomImageHolder</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isNull(java.lang.Object)">
<h3>isNull</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isNull</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<div class="block">Test and return true if object is null.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>obj</code> - object being tested.</dd>
<dt>Returns:</dt>
<dd>true if object is null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isEmpty(java.lang.Object)">
<h3>isEmpty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isEmpty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<div class="block">Test and return true if object is null, empty string or empty collection.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>obj</code> - object being tested.</dd>
<dt>Returns:</dt>
<dd>true if object is null, empty string or empty collection.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isEmpty(java.lang.Object,boolean)">
<h3>isEmpty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isEmpty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj,
 boolean isIgnoreSpace)</span></div>
<div class="block">Test and return true if object is null, empty string or empty collection.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>obj</code> - object being tested.</dd>
<dd><code>isIgnoreSpace</code> - true for ignoring all spaces, line feeds, etc. for html string only</dd>
<dt>Returns:</dt>
<dd>true if object is null, empty string or empty collection.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isRelationship</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isRelationship</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Test and return true if element is relationship.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element being tested.</dd>
<dt>Returns:</dt>
<dd>true if object is relationship</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInteractionMessageType(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">
<h3>getInteractionMessageType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getInteractionMessageType</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</span></div>
<div class="block">Gets interaction message type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - Message</dd>
<dt>Returns:</dt>
<dd>type of message</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUsageRepresentationText(com.nomagic.magicdraw.uml.BaseElement,boolean)">
<h3>getUsageRepresentationText</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getUsageRepresentationText</span><wbr/><span class="parameters">(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> be,
 boolean addFullPath)</span></div>
<div class="block">Formats the usage subject. The output string is the same as Result column of <b>Used by</b> table in Magic
 Draw.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>be</code> - <code>ModelElement</code> to format.</dd>
<dd><code>addFullPath</code> - use full path.</dd>
<dt>Returns:</dt>
<dd>formatted element, String.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUsedBy(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getUsedBy</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;</span> <span class="element-name">getUsedBy</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Return a list of element used by this element (except diagram).</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the the element which will be gotten the list of element name that uses the specified
                element.</dd>
<dt>Returns:</dt>
<dd>Collection of elements used by input element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUsages(java.lang.Object)">
<h3>getUsages</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;com.nomagic.magicdraw.uml.DependencyType&gt;&gt;</span> <span class="element-name">getUsages</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> selectedObjects)</span></div>
<div class="block">Returns Usage Map of MD and then use getUsageElements method for returning the usage of the specified
 element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>selectedObjects</code> - the elements that this method will find the usage.</dd>
<dt>Returns:</dt>
<dd>Map of Usages of elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUsageElements(java.util.Map,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getUsageElements</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;</span> <span class="element-name">getUsageElements</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;com.nomagic.magicdraw.uml.DependencyType&gt;&gt; usagesMap,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Gets the element usages from usage map.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>usagesMap</code> - the Usages Map of MagicDraw.</dd>
<dd><code>element</code> - the element which will be gotten the list of element name that uses the specified element.</dd>
<dt>Returns:</dt>
<dd>Collection of usage name of elements.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getElementName(java.lang.Object)">
<h3>getElementName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getElementName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> element)</span></div>
<div class="block">Gets name of the element. If the name of element is empty, it will return "&lt;unnamed&gt;". This method
 performs the following procedures:
 <ol>
<li>If element is generalized from NamedElement, return $element.name</li>
<li>If element is generalized from Slot, return $element.definingFeature.name</li>
<li>If element is an UML element, return $element.humanName</li>
<li>else return $element.toString()</li>
</ol></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element.</dd>
<dt>Returns:</dt>
<dd>element name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="filterDiagram(java.util.Collection,java.util.Collection)">
<h3>filterDiagram</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a>&gt;</span> <span class="element-name">filterDiagram</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a>&gt; diagramList,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; digramTypes)</span></div>
<div class="block">Return the collection from the diagram list filtered by types.
 <p>
 Example: <code><pre>
 #foreach ($d in $report.filterElement($Diagram, ['Use Case Diagram', 'Class Diagram'])
    $d.name
 #end
 </pre></code>
</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagramList</code> - the collection of diagrams.</dd>
<dd><code>digramTypes</code> - the collection of diagram types which is used to filter.</dd>
<dt>Returns:</dt>
<dd>the collection of filtered diagrams.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="filterElement(java.util.Collection,java.util.Collection)">
<h3>filterElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;</span> <span class="element-name">filterElement</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt; elementList,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; humanTypes)</span></div>
<div class="block">Return the collection from the element list filtered by human types.
 <p>
 Example: <code><pre>
 #foreach ($e in $report.filterElement($elements, ['Class', 'Interface'])
    $e.name $e.humanType
 #end
 </pre></code>
</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elementList</code> - the collection of element.</dd>
<dd><code>humanTypes</code> - the collection of human types which is used to filter.</dd>
<dt>Returns:</dt>
<dd>the collection of filtered elements.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="filterElementByStereotypeName(java.util.Collection,java.util.Collection)">
<h3>filterElementByStereotypeName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;</span> <span class="element-name">filterElementByStereotypeName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt; elementList,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; stereotypesNames)</span></div>
<div class="block">Return the collection from the element list filtered by stereotype.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elementList</code> - the collection of element.</dd>
<dd><code>stereotypesNames</code> - the collection of stereotypes names which is used to filter.</dd>
<dt>Returns:</dt>
<dd>the collection of filtered elements.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="filterElementType(java.util.Collection,java.util.Collection)">
<h3>filterElementType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;</span> <span class="element-name">filterElementType</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt; elementList,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; elementTypes)</span></div>
<div class="block">Return the collection from the element list filtered by element types.
 <p>
 Example: <code><pre>
 #foreach ($e in $report.filterElementType($elements, ['class', 'interface'])
    $e.name $e.elementType
 #end
 </pre></code>
</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elementList</code> - the collection of element.</dd>
<dd><code>elementTypes</code> - the collection of element types which is used to filter.</dd>
<dt>Returns:</dt>
<dd>the collection of filtered elements.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="filterClassName(java.util.Collection,java.util.Collection)">
<h3>filterClassName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;</span> <span class="element-name">filterClassName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt; elementList,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; shortNameForClassTypes)</span></div>
<div class="block">Return the collection from the element list filtered by short name for class types.
 <p>
 Example: <code><pre>
 #foreach ($e in $report.filterClassName($elements, ['Diagram', 'UseCase'])
    $e.name $e.className
 #end
 </pre></code>
</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elementList</code> - the collection of element.</dd>
<dd><code>shortNameForClassTypes</code> - the collection of short name for class type which is used to filter.</dd>
<dt>Returns:</dt>
<dd>the collection of filtered elements.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="filter(java.util.Collection,java.lang.String,java.util.Collection)">
<h3>filter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">filter</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elementList,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; propertyValue)</span></div>
<div class="block">Return the collection from the element list filtered by specified property name.
 <p>
 Example: <code><pre>
 #foreach ($e in $report.filter($elements, 'name', ['foo', 'bar'])
    $e.name
 #end
 </pre></code>
</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elementList</code> - the collection of element.</dd>
<dd><code>propertyName</code> - the property name which is used to filter.</dd>
<dd><code>propertyValue</code> - the collection of element property values which is used to filter.</dd>
<dt>Returns:</dt>
<dd>the collection of filtered elements.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBaseClassInheritableAttributes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">
<h3>getBaseClassInheritableAttributes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></span> <span class="element-name">getBaseClassInheritableAttributes</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier)</span></div>
<div class="block">Gets the classifier inheritable attributes.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifier</code> - the Classifier.</dd>
<dt>Returns:</dt>
<dd>the Collection of Attributes.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBaseClassInheritableOperations(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">
<h3>getBaseClassInheritableOperations</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></span> <span class="element-name">getBaseClassInheritableOperations</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier)</span></div>
<div class="block">Gets the classifier inheritable operations.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifier</code> - the Classifier.</dd>
<dt>Returns:</dt>
<dd>the Collection of Operations.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBaseClassAssociations(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">
<h3>getBaseClassAssociations</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></span> <span class="element-name">getBaseClassAssociations</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier)</span></div>
<div class="block">Gets the classifier associations.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifier</code> - the Classifier.</dd>
<dt>Returns:</dt>
<dd>the Collection of Associations.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBaseRelations(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">
<h3>getBaseRelations</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></span> <span class="element-name">getBaseRelations</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier)</span></div>
<div class="block">Gets the classifier relations.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifier</code> - the Classifier.</dd>
<dt>Returns:</dt>
<dd>the Collection of Relations.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBaseClassPorts(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">
<h3>getBaseClassPorts</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></span> <span class="element-name">getBaseClassPorts</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier)</span></div>
<div class="block">Gets the classifier port.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifier</code> - the Classifier.</dd>
<dt>Returns:</dt>
<dd>the Collection of Ports.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBaseRealizedInterfaces(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier)">
<h3>getBaseRealizedInterfaces</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></span> <span class="element-name">getBaseRealizedInterfaces</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">BehavioredClassifier</a> behavioredClassifier)</span></div>
<div class="block">Gets the behavior classifier realized interfaces.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>behavioredClassifier</code> - the BehavioredClassifier.</dd>
<dt>Returns:</dt>
<dd>the Collection of RealizedInterfaces.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDerivedClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">
<h3>isDerivedClassifier</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDerivedClassifier</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> parent,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> child)</span></div>
<div class="block">Checks if child is derived from parent by generalization.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parent</code> - parent</dd>
<dd><code>child</code> - possible parent</dd>
<dt>Returns:</dt>
<dd>true if derived</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUseCaseNumber(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getUseCaseNumber</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getUseCaseNumber</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Return the use case number or use case ID of element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element</dd>
<dt>Returns:</dt>
<dd>the use case number.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getActorNumber(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getActorNumber</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getActorNumber</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Return the actor ID of Actor.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dt>Returns:</dt>
<dd>the actor ID</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUCOwnerNumber(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getUCOwnerNumber</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getUCOwnerNumber</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Return the use case number or use case ID of element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element</dd>
<dt>Returns:</dt>
<dd>the use case owner number or ID.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getElementURL(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getElementURL</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getElementURL</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Retrieve MagicDraw's element URL.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element object</dd>
<dt>Returns:</dt>
<dd>MagicDraw's element URL</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBasicFlows(com.nomagic.uml2.ext.magicdraw.mdusecases.UseCase)">
<h3>getBasicFlows</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../usecasescenarios/scenarios/FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a>&gt;</span> <span class="element-name">getBasicFlows</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/mdusecases/UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">UseCase</a> useCase)</span></div>
<div class="block">Find and return a list of basic flows from given use case. If use case scenario is not being used, it will
 retrieve the value from "requirementUseCase" stereotype tags.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>useCase</code> - a use case.</dd>
<dt>Returns:</dt>
<dd>a list of flow step <a href="../../usecasescenarios/scenarios/FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios"><code>FlowStep</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAlternativeFlows(com.nomagic.uml2.ext.magicdraw.mdusecases.UseCase)">
<h3>getAlternativeFlows</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../usecasescenarios/scenarios/FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a>&gt;</span> <span class="element-name">getAlternativeFlows</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/mdusecases/UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">UseCase</a> useCase)</span></div>
<div class="block">Find and return all alternative flows from given use case. The alternative flows will be listed from all
 possible branches of basic flows. If use case scenario is not being used, it will the retrieve value from
 "requirementUseCase" stereotype tags.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>useCase</code> - a use case.</dd>
<dt>Returns:</dt>
<dd>a list of flow step <a href="../../usecasescenarios/scenarios/FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios"><code>FlowStep</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getExceptionalFlows(com.nomagic.uml2.ext.magicdraw.mdusecases.UseCase)">
<h3>getExceptionalFlows</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../usecasescenarios/scenarios/FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a>&gt;</span> <span class="element-name">getExceptionalFlows</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/mdusecases/UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">UseCase</a> useCase)</span></div>
<div class="block">Find and return a basic flow from given use case. If use case scenario is not being used, it will the
 retrieve value from "requirementUseCase" stereotype tags.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>useCase</code> - a use case.</dd>
<dt>Returns:</dt>
<dd>a list of flow step <a href="../../usecasescenarios/scenarios/FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios"><code>FlowStep</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSlotValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String)">
<h3>getSlotValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</span> <span class="element-name">getSlotValue</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> classifierName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> definingFeatureName)</span></div>
<div class="block">Get slot value by classifier name and definingFeature name. If there are more than one slots matching with
 specified parameters, return only the value of first matching slot.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - an element.</dd>
<dd><code>classifierName</code> - classifier name. [case-sensitive]</dd>
<dd><code>definingFeatureName</code> - defining feature name. [case-sensitive]</dd>
<dt>Returns:</dt>
<dd>result value in ValueSpecification or value in array of ValueSpecification, up to multiplicity.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSlotProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>getSlotProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getSlotProperty</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> classifierName)</span></div>
<div class="block">Get slot property by classifier name If there are more than one classifier matching with specified
 parameters, return only the property of first matching classifier.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - an element.</dd>
<dd><code>classifierName</code> - classifier name. [case-sensitive]</dd>
<dt>Returns:</dt>
<dd>slot property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedElementsIncludingAdditional(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">
<h3>getOwnedElementsIncludingAdditional</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getOwnedElementsIncludingAdditional</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 boolean includePureOwned)</span></div>
<div class="block">Return owned elements of the given Element including additional owned elements defined in DSL specification by additionalContentProperty.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - an element to be found owned element</dd>
<dd><code>includePureOwned</code> - include element owned directly in ownedElement UML metaproperty</dd>
<dt>Returns:</dt>
<dd>owned elements of the given Element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedElementsIncludingAdditional(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,boolean)">
<h3>getOwnedElementsIncludingAdditional</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getOwnedElementsIncludingAdditional</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 boolean includePureOwned,
 boolean excludeRelationship)</span></div>
<div class="block">Return owned elements of the given Element including additional owned elements defined in DSL specification by additionalContentProperty.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - an element to be found owned element</dd>
<dd><code>includePureOwned</code> - include element owned directly in ownedElement UML metaproperty</dd>
<dd><code>excludeRelationship</code> - true to exclude relationship</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedElementsIncludingAdditional(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,boolean,boolean)">
<h3>getOwnedElementsIncludingAdditional</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getOwnedElementsIncludingAdditional</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 boolean includePureOwned,
 boolean excludeRelationship,
 boolean excludeAuxiliaryResources)</span></div>
<div class="block">Return owned elements of the given Element including additional owned elements defined in DSL specification by additionalContentProperty.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - an element to be found owned element</dd>
<dd><code>includePureOwned</code> - include element owned directly in ownedElement UML metaproperty</dd>
<dd><code>excludeRelationship</code> - true to exclude relationship of given element</dd>
<dd><code>excludeAuxiliaryResources</code> - true to exclude auxiliary resoures</dd>
<dt>Returns:</dt>
<dd>owned elements of the given Element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedElementsIncludingAdditional(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,boolean,boolean,boolean)">
<h3>getOwnedElementsIncludingAdditional</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getOwnedElementsIncludingAdditional</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 boolean includePureOwned,
 boolean excludeRelationship,
 boolean excludeAuxiliaryResources,
 boolean excludeInvisibleElement)</span></div>
<div class="block">Return owned elements of the given Element including additional owned elements defined in DSL specification by additionalContentProperty.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - an element to be found owned element</dd>
<dd><code>includePureOwned</code> - include element owned directly in ownedElement UML metaproperty</dd>
<dd><code>excludeRelationship</code> - true to exclude relationship of given element</dd>
<dd><code>excludeAuxiliaryResources</code> - true to exclude auxiliary resources</dd>
<dd><code>excludeInvisibleElement</code> - true to exclude invisible element</dd>
<dt>Returns:</dt>
<dd>owned elements of the given Element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="filterElementByElementFilters(java.util.List,java.util.List)">
<h3>filterElementByElementFilters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">filterElementByElementFilters</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;com.nomagic.magicdraw.ui.ElementFilter&gt; elementFilters)</span></div>
</section>
</li>
<li>
<section class="detail" id="getPackages(boolean)">
<h3>getPackages</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getPackages</span><wbr/><span class="parameters">(boolean includeSmartPackage)</span></div>
</section>
</li>
<li>
<section class="detail" id="isAttachedFile(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isAttachedFile</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isAttachedFile</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Check if element is attached file.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - specific element</dd>
<dt>Returns:</dt>
<dd>true if element is attached element, otherwise; false</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isAttachedImage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isAttachedImage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isAttachedImage</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Check if element is attached image.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - specific element</dd>
<dt>Returns:</dt>
<dd>true if element is attached image, otherwise; false</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAttachedImage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getAttachedImage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getAttachedImage</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span>
                        throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAttachedImage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>getAttachedImage</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getAttachedImage</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> cannotRenderImageMsg)</span>
                        throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Get image from attached image.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - specific element</dd>
<dd><code>cannotRenderImageMsg</code> - in case the element is attached file but not image, return this msg instead.</dd>
<dt>Returns:</dt>
<dd>image of attached image.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAttachedFile(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getAttachedFile</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></span> <span class="element-name">getAttachedFile</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span>
                     throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Get file from attached file.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - specific element</dd>
<dt>Returns:</dt>
<dd>image of attached image.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTemplateFile(java.lang.String,java.lang.String,java.lang.String,java.lang.Object)">
<h3>getTemplateFile</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></span> <span class="element-name">getTemplateFile</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> templateFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> templateLocation,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> extension,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> marker)</span></div>
<div class="block">Get Template file from template file name/path.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>templateFileName</code> - template file name or path</dd>
<dd><code>templateLocation</code> - template location/dir</dd>
<dd><code>extension</code> - extension for template file. in case it has no extension</dd>
<dd><code>marker</code> - The marker object used to track the file.</dd>
<dt>Returns:</dt>
<dd>template file</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTemplateFile(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getTemplateFile</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></span> <span class="element-name">getTemplateFile</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span>
                     throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Get template file from element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - attached file</dd>
<dt>Returns:</dt>
<dd>template file</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getImageFor(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getImageFor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getImageFor</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Create image from element. <br/>
 The image is always created.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - target element</dd>
<dt>Returns:</dt>
<dd>image</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getImageFor(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,int)">
<h3>getImageFor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getImageFor</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 int dpi)</span></div>
<div class="block">Create image from element. <br/>
 The image is always created.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - target element</dd>
<dd><code>dpi</code> - </dd>
<dt>Returns:</dt>
<dd>image</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getImageFor(java.lang.Object,boolean)">
<h3>getImageFor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getImageFor</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object,
 boolean allowDuplicate)</span></div>
<div class="block">Create image from object. <br/>
 The image is newly created or returned old image from map up to 'allowDuplicate'.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - object to be exported as image</dd>
<dd><code>allowDuplicate</code> - allowDuplicated true to always create new image and don't keep the image in map</dd>
<dt>Returns:</dt>
<dd>Image</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getImageFor(java.lang.Object,boolean,java.lang.String)">
<h3>getImageFor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getImageFor</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object,
 boolean allowDuplicate,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> cannotRenderImageMsg)</span></div>
<div class="block">Create image from object. <br/>
 The image is newly created or returned old image from map up to 'allowDuplicate'.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - object to be exported as image</dd>
<dd><code>allowDuplicate</code> - allowDuplicated true to always create new image and don't keep the image in map</dd>
<dd><code>cannotRenderImageMsg</code> - in case the element is attached file but not image, return error message instead.</dd>
<dt>Returns:</dt>
<dd>Image</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getImageFor(java.lang.Object,boolean,java.lang.String,int)">
<h3>getImageFor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getImageFor</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object,
 boolean allowDuplicate,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> cannotRenderImageMsg,
 int dpi)</span></div>
<div class="block">Create image from object. <br/>
 The image is newly created or returned old image from map up to 'allowDuplicate'.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - object to be exported as image</dd>
<dd><code>allowDuplicate</code> - allowDuplicated true to always create new image and don't keep the image in map</dd>
<dd><code>cannotRenderImageMsg</code> - in case the element is attached file but not image, return error message instead.</dd>
<dd><code>dpi</code> - image dpi</dd>
<dt>Returns:</dt>
<dd>Image</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCustomizationPropertyString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Object,java.lang.String)">
<h3>getCustomizationPropertyString</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getCustomizationPropertyString</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> aStereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</span></div>
<div class="block">Return property value as string from Customization element of the specified stereotype, on the element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - an element</dd>
<dd><code>aStereotype</code> - stereotype name or element</dd>
<dd><code>propertyName</code> - property name</dd>
<dt>Returns:</dt>
<dd>property value as string from Customization element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCustomizationProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Object,java.lang.String)">
<h3>getCustomizationProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getCustomizationProperty</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> aStereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</span></div>
<div class="block">Return property value from Customization element of the specified stereotype, on the element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - an element</dd>
<dd><code>aStereotype</code> - stereotype name or element</dd>
<dd><code>propertyName</code> - property name</dd>
<dt>Returns:</dt>
<dd>property value from Customization element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAllCustomizationsByElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getAllCustomizationsByElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a>&gt;</span> <span class="element-name">getAllCustomizationsByElement</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Get all customizations from specific element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - an element</dd>
<dt>Returns:</dt>
<dd>all customization elements of the stereotype on the element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAllCustomizationsByElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Object)">
<h3>getAllCustomizationsByElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a>&gt;</span> <span class="element-name">getAllCustomizationsByElement</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> aStereotype)</span></div>
<div class="block">Get all customizations from specific stereotype on element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - an element</dd>
<dd><code>aStereotype</code> - stereotype name or element</dd>
<dt>Returns:</dt>
<dd>all customization elements of the stereotype on the element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAllCustomizationsByTarget(java.lang.Object)">
<h3>getAllCustomizationsByTarget</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a>&gt;</span> <span class="element-name">getAllCustomizationsByTarget</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> targetElement)</span></div>
<div class="block">Get all customizations from specific target element of customization element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>targetElement</code> - a target element</dd>
<dt>Returns:</dt>
<dd>all customizations from specific target element of customization element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getElementPropertiesName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getElementPropertiesName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getElementPropertiesName</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Get name of all properties from specific element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dt>Returns:</dt>
<dd>list of properties name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getElementPropertiesNameWithMode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getElementPropertiesNameWithMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getElementPropertiesNameWithMode</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Get name of all properties from specific element and current mode.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dt>Returns:</dt>
<dd>list of properties name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getElementPropertiesNameWithMode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>getElementPropertiesNameWithMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getElementPropertiesNameWithMode</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> mode)</span></div>
<div class="block">Get name of all properties from specific element and specific mode.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>mode</code> - view mode from PropertiesModeHelper.MODES</dd>
<dt>Returns:</dt>
<dd>list of properties name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getElementProperties(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getElementProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../properties/Property.html" title="class in com.nomagic.magicdraw.properties">Property</a>&gt;</span> <span class="element-name">getElementProperties</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Get all properties from specific element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dt>Returns:</dt>
<dd>list of properties</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getElementProperties(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>getElementProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../properties/Property.html" title="class in com.nomagic.magicdraw.properties">Property</a>&gt;</span> <span class="element-name">getElementProperties</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> mode)</span></div>
<div class="block">Collects properties that appears in element's specification dialog tree at specific view mode (Standard/Expert/All)</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>mode</code> - view mode from PropertiesModeHelper.MODES -- STANDARD, EXPERT, ALL</dd>
<dt>Returns:</dt>
<dd>list of properties</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDefaultElementFilter()">
<h3>getDefaultElementFilter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.ui.ElementFilter</span> <span class="element-name">getDefaultElementFilter</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getExcludeAuxiliaryResourceFilter()">
<h3>getExcludeAuxiliaryResourceFilter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.ui.ElementFilter</span> <span class="element-name">getExcludeAuxiliaryResourceFilter</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getVisibleElementFilter()">
<h3>getVisibleElementFilter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.ui.ElementFilter</span> <span class="element-name">getVisibleElementFilter</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getExcludeRelationshipElementFilter()">
<h3>getExcludeRelationshipElementFilter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.ui.ElementFilter</span> <span class="element-name">getExcludeRelationshipElementFilter</span>()</div>
</section>
</li>
<li>
<section class="detail" id="filterVisibleElement(java.util.List)">
<h3>filterVisibleElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">filterVisibleElement</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements)</span></div>
</section>
</li>
<li>
<section class="detail" id="filterVisibleElement(java.util.List,boolean)">
<h3>filterVisibleElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">filterVisibleElement</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements,
 boolean includeAuxiliaryResources)</span></div>
</section>
</li>
<li>
<section class="detail" id="isInvisibleElement(com.nomagic.magicdraw.uml.BaseElement)">
<h3>isInvisibleElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isInvisibleElement</span><wbr/><span class="parameters">(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="isInvisibleElement(com.nomagic.magicdraw.uml.BaseElement,boolean)">
<h3>isInvisibleElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isInvisibleElement</span><wbr/><span class="parameters">(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 boolean isTypeFilter)</span></div>
</section>
</li>
<li>
<section class="detail" id="isInvisibleElement(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.ui.ElementFilter)">
<h3>isInvisibleElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isInvisibleElement</span><wbr/><span class="parameters">(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 @CheckForNull
 com.nomagic.magicdraw.ui.ElementFilter elementFilter)</span></div>
</section>
</li>
<li>
<section class="detail" id="getRootNodeOfContainmentTree(boolean)">
<h3>getRootNodeOfContainmentTree</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../ui/browser/Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a></span> <span class="element-name">getRootNodeOfContainmentTree</span><wbr/><span class="parameters">(boolean startWithPrimaryModel)</span></div>
<div class="block">Get root node from containment tree.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>startWithPrimaryModel</code> - true to filter only primary model, <br/>
                              otherwise it will return Project node that may contain primary model and usage project</dd>
<dt>Returns:</dt>
<dd>root node from containment tree</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRootNodeOfDiagramTree()">
<h3>getRootNodeOfDiagramTree</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../ui/browser/Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a></span> <span class="element-name">getRootNodeOfDiagramTree</span>()</div>
<div class="block">Get root node from diagram tree.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>root node from diagram tree</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPropertyGroupsByStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)">
<h3>getPropertyGroupsByStereotype</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.nomagic.magicdraw.propertygroup.PropertyGroup&gt;</span> <span class="element-name">getPropertyGroupsByStereotype</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a> stereotype)</span></div>
<div class="block">Get collection of <code>PropertyGroup</code> by specific stereotype.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stereotype</code> - a stereotype</dd>
<dt>Returns:</dt>
<dd>collection of <code>PropertyGroup</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPropertyGroupsByElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">
<h3>getPropertyGroupsByElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;com.nomagic.magicdraw.propertygroup.PropertyGroup&gt;</span> <span class="element-name">getPropertyGroupsByElement</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 boolean addAlwaysVisible)</span></div>
<div class="block">Get set of <code>PropertyGroup</code> by specific element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - an element</dd>
<dd><code>addAlwaysVisible</code> - true to use all set stereotypes + all settable showWhenNotApplied stereotypes, false to use only all set stereotypes.</dd>
<dt>Returns:</dt>
<dd>set of <code>PropertyGroup</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getQProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>getQProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../properties/Property.html" title="class in com.nomagic.magicdraw.properties">Property</a></span> <span class="element-name">getQProperty</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</span></div>
<div class="block">Get a property for element with DSL property groups, and each property group has its own property.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - an element.</dd>
<dd><code>propertyName</code> - property name</dd>
<dt>Returns:</dt>
<dd>a <a href="../../properties/Property.html" title="class in com.nomagic.magicdraw.properties"><code>Property</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getQProperties(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>getQProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../properties/Property.html" title="class in com.nomagic.magicdraw.properties">Property</a>&gt;</span> <span class="element-name">getQProperties</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</span></div>
<div class="block">Get list of properties for element with DSL property groups, and each property group has its own property.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - an element.</dd>
<dd><code>propertyName</code> - property name</dd>
<dt>Returns:</dt>
<dd>a list of <a href="../../properties/Property.html" title="class in com.nomagic.magicdraw.properties"><code>Property</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setActiveValidationEnabled(boolean)">
<h3>setActiveValidationEnabled</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setActiveValidationEnabled</span><wbr/><span class="parameters">(boolean enable)</span></div>
</section>
</li>
<li>
<section class="detail" id="ensureLoad(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">
<h3>ensureLoad</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">ensureLoad</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</span></div>
</section>
</li>
<li>
<section class="detail" id="isTypeOf(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>isTypeOf</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isTypeOf</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> typeName)</span></div>
<div class="block">A function for checking super type of the specific element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - an element</dd>
<dd><code>typeName</code> - stereotype name or java class name</dd>
<dt>Returns:</dt>
<dd>return true, if the element is subtype of the specific stereotype name or class name.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isTypeOf(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,boolean)">
<h3>isTypeOf</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isTypeOf</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> typeName,
 boolean checkClassTypeName)</span></div>
<div class="block">A function for checking super type of the specific element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - an element</dd>
<dd><code>typeName</code> - stereotype name or java class name</dd>
<dd><code>checkClassTypeName</code> - false to check type by stereotype name only</dd>
<dt>Returns:</dt>
<dd>return true, if the element is subtype of the specific stereotype name or class name.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isAssignableFrom(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>isAssignableFrom</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isAssignableFrom</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> classTypeName)</span></div>
<div class="block">A function for checking super type of the specific element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - an element</dd>
<dd><code>classTypeName</code> - java class name</dd>
<dt>Returns:</dt>
<dd>return true, if the element is subtype of the specific class type name.</dd>
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
