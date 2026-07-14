# JAVA OPENAPI: StandardProfile (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/uml2/StandardProfile.html
- source_path: `com/nomagic/uml2/StandardProfile.html`
- source_sha256: `e07a55983d01f925ed0dcbcea910537eebaed37eeb073029b1b5210f16399a56`
- captured_utc: `2026-07-14T16:58:46.152383+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2](package-summary.html)

## Class StandardProfile

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[com.nomagic.profiles.ProfileImplementation](../profiles/ProfileImplementation.html)
com.nomagic.uml2.StandardProfile

@OpenApiAllpublic classStandardProfile
extends [ProfileImplementation](../profiles/ProfileImplementation.html)

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`static class`
`[StandardProfile.AuxiliaryStereotype](StandardProfile.AuxiliaryStereotype.html)`

`static class`
`[StandardProfile.BuildComponentStereotype](StandardProfile.BuildComponentStereotype.html)`

`static class`
`[StandardProfile.CallStereotype](StandardProfile.CallStereotype.html)`

`static class`
`[StandardProfile.CreateStereotype](StandardProfile.CreateStereotype.html)`

`static class`
`[StandardProfile.DeriveStereotype](StandardProfile.DeriveStereotype.html)`

`static class`
`[StandardProfile.DestroyStereotype](StandardProfile.DestroyStereotype.html)`

`static class`
`[StandardProfile.DocumentStereotype](StandardProfile.DocumentStereotype.html)`

`static class`
`[StandardProfile.EntityStereotype](StandardProfile.EntityStereotype.html)`

`static class`
`[StandardProfile.ExecutableStereotype](StandardProfile.ExecutableStereotype.html)`

`static class`
`[StandardProfile.FileStereotype](StandardProfile.FileStereotype.html)`

`static class`
`[StandardProfile.FocusStereotype](StandardProfile.FocusStereotype.html)`

`static class`
`[StandardProfile.FrameworkStereotype](StandardProfile.FrameworkStereotype.html)`

`static class`
`[StandardProfile.ImplementationClassStereotype](StandardProfile.ImplementationClassStereotype.html)`

`static class`
`[StandardProfile.ImplementStereotype](StandardProfile.ImplementStereotype.html)`

`static class`
`[StandardProfile.InstantiateStereotype](StandardProfile.InstantiateStereotype.html)`

`static class`
`[StandardProfile.LibraryStereotype](StandardProfile.LibraryStereotype.html)`

`static class`
`[StandardProfile.MetaclassStereotype](StandardProfile.MetaclassStereotype.html)`

`static class`
`[StandardProfile.MetamodelStereotype](StandardProfile.MetamodelStereotype.html)`

`static class`
`[StandardProfile.ModelLibraryStereotype](StandardProfile.ModelLibraryStereotype.html)`

`static class`
`[StandardProfile.ProcessStereotype](StandardProfile.ProcessStereotype.html)`

`static class`
`[StandardProfile.RealizationStereotype](StandardProfile.RealizationStereotype.html)`

`static class`
`[StandardProfile.RefineStereotype](StandardProfile.RefineStereotype.html)`

`static class`
`[StandardProfile.ResponsibilityStereotype](StandardProfile.ResponsibilityStereotype.html)`

`static class`
`[StandardProfile.ScriptStereotype](StandardProfile.ScriptStereotype.html)`

`static class`
`[StandardProfile.SendStereotype](StandardProfile.SendStereotype.html)`

`static class`
`[StandardProfile.ServiceStereotype](StandardProfile.ServiceStereotype.html)`

`static class`
`[StandardProfile.SourceStereotype](StandardProfile.SourceStereotype.html)`

`static class`
`[StandardProfile.SpecificationStereotype](StandardProfile.SpecificationStereotype.html)`

`static class`
`[StandardProfile.SubsystemStereotype](StandardProfile.SubsystemStereotype.html)`

`static class`
`[StandardProfile.SystemModelStereotype](StandardProfile.SystemModelStereotype.html)`

`static class`
`[StandardProfile.TraceStereotype](StandardProfile.TraceStereotype.html)`

`static class`
`[StandardProfile.TypeStereotype](StandardProfile.TypeStereotype.html)`

`static class`
`[StandardProfile.UtilityStereotype](StandardProfile.UtilityStereotype.html)`
Nested classes/interfaces inherited from class com.nomagic.profiles.[ProfileImplementation](../profiles/ProfileImplementation.html)
`[ProfileImplementation.StereotypeWrapper](../profiles/ProfileImplementation.StereotypeWrapper.html)`
 =========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[AUXILIARY_STEREOTYPE](#AUXILIARY_STEREOTYPE)`
Deprecated.
use AuxiliaryStereotype.STEREOTYPE_NAME
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[BUILDCOMPONENT_STEREOTYPE](#BUILDCOMPONENT_STEREOTYPE)`
Deprecated.
use BuildComponentStereotype.STEREOTYPE_NAME
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[CALL_STEREOTYPE](#CALL_STEREOTYPE)`
Deprecated.
use CallStereotype.STEREOTYPE_NAME
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[CREATE_STEREOTYPE](#CREATE_STEREOTYPE)`
Deprecated.
use CreateStereotype.STEREOTYPE_NAME
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[DERIVE_STEREOTYPE](#DERIVE_STEREOTYPE)`
Deprecated.
use DeriveStereotype.STEREOTYPE_NAME
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[DESTROY_STEREOTYPE](#DESTROY_STEREOTYPE)`
Deprecated.
use DestroyStereotype.STEREOTYPE_NAME
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[DOCUMENT_STEREOTYPE](#DOCUMENT_STEREOTYPE)`
Deprecated.
use DocumentStereotype.STEREOTYPE_NAME
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[ENTITY_STEREOTYPE](#ENTITY_STEREOTYPE)`
Deprecated.
use EntityStereotype.STEREOTYPE_NAME
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[EXECUTABLE_STEREOTYPE](#EXECUTABLE_STEREOTYPE)`
Deprecated.
use ExecutableStereotype.STEREOTYPE_NAME
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[FILE_STEREOTYPE](#FILE_STEREOTYPE)`
Deprecated.
use FileStereotype.STEREOTYPE_NAME
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[FOCUS_STEREOTYPE](#FOCUS_STEREOTYPE)`
Deprecated.
use FocusStereotype.STEREOTYPE_NAME
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[FRAMEWORK_STEREOTYPE](#FRAMEWORK_STEREOTYPE)`
Deprecated.
use FrameworkStereotype.STEREOTYPE_NAME
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[IMPLEMENT_STEREOTYPE](#IMPLEMENT_STEREOTYPE)`
Deprecated.
use ImplementStereotype.STEREOTYPE_NAME
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[IMPLEMENTATIONCLASS_STEREOTYPE](#IMPLEMENTATIONCLASS_STEREOTYPE)`
Deprecated.
use ImplementationClassStereotype.STEREOTYPE_NAME
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[INSTANTIATE_STEREOTYPE](#INSTANTIATE_STEREOTYPE)`
Deprecated.
use InstantiateStereotype.STEREOTYPE_NAME
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[LIBRARY_STEREOTYPE](#LIBRARY_STEREOTYPE)`
Deprecated.
use LibraryStereotype.STEREOTYPE_NAME
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[METACLASS_STEREOTYPE](#METACLASS_STEREOTYPE)`
Deprecated.
use MetaclassStereotype.STEREOTYPE_NAME
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[METAMODEL_STEREOTYPE](#METAMODEL_STEREOTYPE)`
Deprecated.
use MetamodelStereotype.STEREOTYPE_NAME
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[MODELLIBRARY_STEREOTYPE](#MODELLIBRARY_STEREOTYPE)`
Deprecated.
use ModelLibraryStereotype.STEREOTYPE_NAME
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[PROCESS_STEREOTYPE](#PROCESS_STEREOTYPE)`
Deprecated.
use ProcessStereotype.STEREOTYPE_NAME
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[PROFILE_NAME](#PROFILE_NAME)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[PROFILE_URI](#PROFILE_URI)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[REALIZATION_STEREOTYPE](#REALIZATION_STEREOTYPE)`
Deprecated.
use RealizationStereotype.STEREOTYPE_NAME
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[REFINE_STEREOTYPE](#REFINE_STEREOTYPE)`
Deprecated.
use RefineStereotype.STEREOTYPE_NAME
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[RESPONSIBILITY_STEREOTYPE](#RESPONSIBILITY_STEREOTYPE)`
Deprecated.
use ResponsibilityStereotype.STEREOTYPE_NAME
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[SCRIPT_STEREOTYPE](#SCRIPT_STEREOTYPE)`
Deprecated.
use ScriptStereotype.STEREOTYPE_NAME
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[SEND_STEREOTYPE](#SEND_STEREOTYPE)`
Deprecated.
use SendStereotype.STEREOTYPE_NAME
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[SERVICE_STEREOTYPE](#SERVICE_STEREOTYPE)`
Deprecated.
use ServiceStereotype.STEREOTYPE_NAME
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[SOURCE_STEREOTYPE](#SOURCE_STEREOTYPE)`
Deprecated.
use SourceStereotype.STEREOTYPE_NAME
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[SPECIFICATION_STEREOTYPE](#SPECIFICATION_STEREOTYPE)`
Deprecated.
use SpecificationStereotype.STEREOTYPE_NAME
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[SUBSYSTEM_STEREOTYPE](#SUBSYSTEM_STEREOTYPE)`
Deprecated.
use SubsystemStereotype.STEREOTYPE_NAME
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[SYSTEMMODEL_STEREOTYPE](#SYSTEMMODEL_STEREOTYPE)`
Deprecated.
use SystemModelStereotype.STEREOTYPE_NAME
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TRACE_STEREOTYPE](#TRACE_STEREOTYPE)`
Deprecated.
use TraceStereotype.STEREOTYPE_NAME
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TYPE_STEREOTYPE](#TYPE_STEREOTYPE)`
Deprecated.
use TypeStereotype.STEREOTYPE_NAME
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[UTILITY_STEREOTYPE](#UTILITY_STEREOTYPE)`
Deprecated.
use UtilityStereotype.STEREOTYPE_NAME
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[StandardProfile](#%3Cinit%3E(com.nomagic.profiles.ProfileCache))(com.nomagic.profiles.ProfileCache cache)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`[StandardProfile.AuxiliaryStereotype](StandardProfile.AuxiliaryStereotype.html)`
`[auxiliary](#auxiliary())()`

`[StandardProfile.BuildComponentStereotype](StandardProfile.BuildComponentStereotype.html)`
`[buildComponent](#buildComponent())()`

`[StandardProfile.CallStereotype](StandardProfile.CallStereotype.html)`
`[call](#call())()`

`[StandardProfile.CreateStereotype](StandardProfile.CreateStereotype.html)`
`[create](#create())()`

`[StandardProfile.DeriveStereotype](StandardProfile.DeriveStereotype.html)`
`[derive](#derive())()`

`[StandardProfile.DestroyStereotype](StandardProfile.DestroyStereotype.html)`
`[destroy](#destroy())()`

`[StandardProfile.DocumentStereotype](StandardProfile.DocumentStereotype.html)`
`[document](#document())()`

`[StandardProfile.EntityStereotype](StandardProfile.EntityStereotype.html)`
`[entity](#entity())()`

`[StandardProfile.ExecutableStereotype](StandardProfile.ExecutableStereotype.html)`
`[executable](#executable())()`

`[StandardProfile.FileStereotype](StandardProfile.FileStereotype.html)`
`[file](#file())()`

`[StandardProfile.FocusStereotype](StandardProfile.FocusStereotype.html)`
`[focus](#focus())()`

`[StandardProfile.FrameworkStereotype](StandardProfile.FrameworkStereotype.html)`
`[framework](#framework())()`

`protected [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<com.nomagic.profiles.ProfileImplementation.ProfileElementWrapper>`
`[generatedGetAllElementWrappers](#generatedGetAllElementWrappers())()`

`protected [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Stereotype](ext/magicdraw/mdprofiles/Stereotype.html)>`
`[generatedGetAllStereotypes](#generatedGetAllStereotypes())()`

`[Stereotype](ext/magicdraw/mdprofiles/Stereotype.html)`
`[getAuxiliary](#getAuxiliary())()`
Deprecated.
use getInstance(element).auxiliary().getStereotype()
`[Stereotype](ext/magicdraw/mdprofiles/Stereotype.html)`
`[getBuildComponent](#getBuildComponent())()`
Deprecated.
use getInstance(element).buildComponent().getStereotype()
`[Stereotype](ext/magicdraw/mdprofiles/Stereotype.html)`
`[getCall](#getCall())()`
Deprecated.
use getInstance(element).call().getStereotype()
`[Stereotype](ext/magicdraw/mdprofiles/Stereotype.html)`
`[getCreate](#getCreate())()`
Deprecated.
use getInstance(element).create().getStereotype()
`[Stereotype](ext/magicdraw/mdprofiles/Stereotype.html)`
`[getDerive](#getDerive())()`
Deprecated.
use getInstance(element).derive().getStereotype()
`[Stereotype](ext/magicdraw/mdprofiles/Stereotype.html)`
`[getDestroy](#getDestroy())()`
Deprecated.
use getInstance(element).destroy().getStereotype()
`[Stereotype](ext/magicdraw/mdprofiles/Stereotype.html)`
`[getDocument](#getDocument())()`
Deprecated.
use getInstance(element).document().getStereotype()
`[Stereotype](ext/magicdraw/mdprofiles/Stereotype.html)`
`[getEntity](#getEntity())()`
Deprecated.
use getInstance(element).entity().getStereotype()
`[Stereotype](ext/magicdraw/mdprofiles/Stereotype.html)`
`[getExecutable](#getExecutable())()`
Deprecated.
use getInstance(element).executable().getStereotype()
`[Stereotype](ext/magicdraw/mdprofiles/Stereotype.html)`
`[getFile](#getFile())()`
Deprecated.
use getInstance(element).file().getStereotype()
`[Stereotype](ext/magicdraw/mdprofiles/Stereotype.html)`
`[getFocus](#getFocus())()`
Deprecated.
use getInstance(element).focus().getStereotype()
`[Stereotype](ext/magicdraw/mdprofiles/Stereotype.html)`
`[getFramework](#getFramework())()`
Deprecated.
use getInstance(element).framework().getStereotype()
`[Stereotype](ext/magicdraw/mdprofiles/Stereotype.html)`
`[getImplement](#getImplement())()`
Deprecated.
use getInstance(element).implement().getStereotype()
`[Stereotype](ext/magicdraw/mdprofiles/Stereotype.html)`
`[getImplementationClass](#getImplementationClass())()`
Deprecated.
use getInstance(element).implementationClass().getStereotype()
`static [StandardProfile](StandardProfile.html)`
`[getInstance](#getInstance(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../magicdraw/uml/BaseElement.html) baseElement)`

`static [StandardProfile](StandardProfile.html)`
`[getInstanceByProject](#getInstanceByProject(com.nomagic.uml2.project.ElementProject))(com.nomagic.uml2.project.ElementProject project)`

`[Stereotype](ext/magicdraw/mdprofiles/Stereotype.html)`
`[getInstantiate](#getInstantiate())()`
Deprecated.
use getInstance(element).instantiate().getStereotype()
`[Stereotype](ext/magicdraw/mdprofiles/Stereotype.html)`
`[getLibrary](#getLibrary())()`
Deprecated.
use getInstance(element).library().getStereotype()
`[Stereotype](ext/magicdraw/mdprofiles/Stereotype.html)`
`[getMetaclass](#getMetaclass())()`
Deprecated.
use getInstance(element).metaclass().getStereotype()
`[Stereotype](ext/magicdraw/mdprofiles/Stereotype.html)`
`[getMetamodel](#getMetamodel())()`
Deprecated.
use getInstance(element).metamodel().getStereotype()
`[Stereotype](ext/magicdraw/mdprofiles/Stereotype.html)`
`[getModelLibrary](#getModelLibrary())()`
Deprecated.
use getInstance(element).modelLibrary().getStereotype()
`[Stereotype](ext/magicdraw/mdprofiles/Stereotype.html)`
`[getProcess](#getProcess())()`
Deprecated.
use getInstance(element).process().getStereotype()
`[Stereotype](ext/magicdraw/mdprofiles/Stereotype.html)`
`[getRealization](#getRealization())()`
Deprecated.
use getInstance(element).realization().getStereotype()
`[Stereotype](ext/magicdraw/mdprofiles/Stereotype.html)`
`[getRefine](#getRefine())()`
Deprecated.
use getInstance(element).refine().getStereotype()
`[Stereotype](ext/magicdraw/mdprofiles/Stereotype.html)`
`[getResponsibility](#getResponsibility())()`
Deprecated.
use getInstance(element).responsibility().getStereotype()
`[Stereotype](ext/magicdraw/mdprofiles/Stereotype.html)`
`[getScript](#getScript())()`
Deprecated.
use getInstance(element).script().getStereotype()
`[Stereotype](ext/magicdraw/mdprofiles/Stereotype.html)`
`[getSend](#getSend())()`
Deprecated.
use getInstance(element).send().getStereotype()
`[Stereotype](ext/magicdraw/mdprofiles/Stereotype.html)`
`[getService](#getService())()`
Deprecated.
use getInstance(element).service().getStereotype()
`[Stereotype](ext/magicdraw/mdprofiles/Stereotype.html)`
`[getSource](#getSource())()`
Deprecated.
use getInstance(element).source().getStereotype()
`[Stereotype](ext/magicdraw/mdprofiles/Stereotype.html)`
`[getSpecification](#getSpecification())()`
Deprecated.
use getInstance(element).specification().getStereotype()
`[Stereotype](ext/magicdraw/mdprofiles/Stereotype.html)`
`[getSubsystem](#getSubsystem())()`
Deprecated.
use getInstance(element).subsystem().getStereotype()
`[Stereotype](ext/magicdraw/mdprofiles/Stereotype.html)`
`[getSystemModel](#getSystemModel())()`
Deprecated.
use getInstance(element).systemModel().getStereotype()
`[Stereotype](ext/magicdraw/mdprofiles/Stereotype.html)`
`[getTrace](#getTrace())()`
Deprecated.
use getInstance(element).trace().getStereotype()
`[Stereotype](ext/magicdraw/mdprofiles/Stereotype.html)`
`[getType](#getType())()`
Deprecated.
use getInstance(element).type().getStereotype()
`[Stereotype](ext/magicdraw/mdprofiles/Stereotype.html)`
`[getUtility](#getUtility())()`
Deprecated.
use getInstance(element).utility().getStereotype()
`[StandardProfile.ImplementStereotype](StandardProfile.ImplementStereotype.html)`
`[implement](#implement())()`

`[StandardProfile.ImplementationClassStereotype](StandardProfile.ImplementationClassStereotype.html)`
`[implementationClass](#implementationClass())()`

`[StandardProfile.InstantiateStereotype](StandardProfile.InstantiateStereotype.html)`
`[instantiate](#instantiate())()`

`static boolean`
`[isAuxiliary](#isAuxiliary(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`
Deprecated.
use AuxiliaryStereotype.isInstance(element)
`static boolean`
`[isBuildComponent](#isBuildComponent(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`
Deprecated.
use BuildComponentStereotype.isInstance(element)
`static boolean`
`[isCall](#isCall(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`
Deprecated.
use CallStereotype.isInstance(element)
`static boolean`
`[isCreate](#isCreate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`
Deprecated.
use CreateStereotype.isInstance(element)
`static boolean`
`[isDerive](#isDerive(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`
Deprecated.
use DeriveStereotype.isInstance(element)
`static boolean`
`[isDestroy](#isDestroy(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`
Deprecated.
use DestroyStereotype.isInstance(element)
`static boolean`
`[isDocument](#isDocument(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`
Deprecated.
use DocumentStereotype.isInstance(element)
`static boolean`
`[isEntity](#isEntity(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`
Deprecated.
use EntityStereotype.isInstance(element)
`static boolean`
`[isExecutable](#isExecutable(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`
Deprecated.
use ExecutableStereotype.isInstance(element)
`static boolean`
`[isFile](#isFile(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`
Deprecated.
use FileStereotype.isInstance(element)
`static boolean`
`[isFocus](#isFocus(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`
Deprecated.
use FocusStereotype.isInstance(element)
`static boolean`
`[isFramework](#isFramework(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`
Deprecated.
use FrameworkStereotype.isInstance(element)
`static boolean`
`[isImplement](#isImplement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`
Deprecated.
use ImplementStereotype.isInstance(element)
`static boolean`
`[isImplementationClass](#isImplementationClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`
Deprecated.
use ImplementationClassStereotype.isInstance(element)
`static boolean`
`[isInstantiate](#isInstantiate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`
Deprecated.
use InstantiateStereotype.isInstance(element)
`static boolean`
`[isLibrary](#isLibrary(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`
Deprecated.
use LibraryStereotype.isInstance(element)
`static boolean`
`[isMetaclass](#isMetaclass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`
Deprecated.
use MetaclassStereotype.isInstance(element)
`static boolean`
`[isMetamodel](#isMetamodel(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`
Deprecated.
use MetamodelStereotype.isInstance(element)
`static boolean`
`[isModelLibrary](#isModelLibrary(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`
Deprecated.
use ModelLibraryStereotype.isInstance(element)
`static boolean`
`[isProcess](#isProcess(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`
Deprecated.
use ProcessStereotype.isInstance(element)
`static boolean`
`[isRealization](#isRealization(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`
Deprecated.
use RealizationStereotype.isInstance(element)
`static boolean`
`[isRefine](#isRefine(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`
Deprecated.
use RefineStereotype.isInstance(element)
`static boolean`
`[isResponsibility](#isResponsibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`
Deprecated.
use ResponsibilityStereotype.isInstance(element)
`static boolean`
`[isScript](#isScript(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`
Deprecated.
use ScriptStereotype.isInstance(element)
`static boolean`
`[isSend](#isSend(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`
Deprecated.
use SendStereotype.isInstance(element)
`static boolean`
`[isService](#isService(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`
Deprecated.
use ServiceStereotype.isInstance(element)
`static boolean`
`[isSource](#isSource(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`
Deprecated.
use SourceStereotype.isInstance(element)
`static boolean`
`[isSpecification](#isSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`
Deprecated.
use SpecificationStereotype.isInstance(element)
`static boolean`
`[isSubsystem](#isSubsystem(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`
Deprecated.
use SubsystemStereotype.isInstance(element)
`static boolean`
`[isSystemModel](#isSystemModel(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`
Deprecated.
use SystemModelStereotype.isInstance(element)
`static boolean`
`[isTrace](#isTrace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`
Deprecated.
use TraceStereotype.isInstance(element)
`static boolean`
`[isType](#isType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`
Deprecated.
use TypeStereotype.isInstance(element)
`static boolean`
`[isUtility](#isUtility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`
Deprecated.
use UtilityStereotype.isInstance(element)
`[StandardProfile.LibraryStereotype](StandardProfile.LibraryStereotype.html)`
`[library](#library())()`

`[StandardProfile.MetaclassStereotype](StandardProfile.MetaclassStereotype.html)`
`[metaclass](#metaclass())()`

`[StandardProfile.MetamodelStereotype](StandardProfile.MetamodelStereotype.html)`
`[metamodel](#metamodel())()`

`[StandardProfile.ModelLibraryStereotype](StandardProfile.ModelLibraryStereotype.html)`
`[modelLibrary](#modelLibrary())()`

`[StandardProfile.ProcessStereotype](StandardProfile.ProcessStereotype.html)`
`[process](#process())()`

`[StandardProfile.RealizationStereotype](StandardProfile.RealizationStereotype.html)`
`[realization](#realization())()`

`[StandardProfile.RefineStereotype](StandardProfile.RefineStereotype.html)`
`[refine](#refine())()`

`[StandardProfile.ResponsibilityStereotype](StandardProfile.ResponsibilityStereotype.html)`
`[responsibility](#responsibility())()`

`[StandardProfile.ScriptStereotype](StandardProfile.ScriptStereotype.html)`
`[script](#script())()`

`[StandardProfile.SendStereotype](StandardProfile.SendStereotype.html)`
`[send](#send())()`

`[StandardProfile.ServiceStereotype](StandardProfile.ServiceStereotype.html)`
`[service](#service())()`

`[StandardProfile.SourceStereotype](StandardProfile.SourceStereotype.html)`
`[source](#source())()`

`[StandardProfile.SpecificationStereotype](StandardProfile.SpecificationStereotype.html)`
`[specification](#specification())()`

`[StandardProfile.SubsystemStereotype](StandardProfile.SubsystemStereotype.html)`
`[subsystem](#subsystem())()`

`[StandardProfile.SystemModelStereotype](StandardProfile.SystemModelStereotype.html)`
`[systemModel](#systemModel())()`

`[StandardProfile.TraceStereotype](StandardProfile.TraceStereotype.html)`
`[trace](#trace())()`

`[StandardProfile.TypeStereotype](StandardProfile.TypeStereotype.html)`
`[type](#type())()`

`[StandardProfile.UtilityStereotype](StandardProfile.UtilityStereotype.html)`
`[utility](#utility())()`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
PROFILE_URI
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) PROFILE_URI
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.StandardProfile.PROFILE_URI)
PROFILE_NAME
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) PROFILE_NAME
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.StandardProfile.PROFILE_NAME)
AUXILIARY_STEREOTYPE
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) AUXILIARY_STEREOTYPE
Deprecated.
use AuxiliaryStereotype.STEREOTYPE_NAME
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.StandardProfile.AUXILIARY_STEREOTYPE)
BUILDCOMPONENT_STEREOTYPE
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) BUILDCOMPONENT_STEREOTYPE
Deprecated.
use BuildComponentStereotype.STEREOTYPE_NAME
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.StandardProfile.BUILDCOMPONENT_STEREOTYPE)
CALL_STEREOTYPE
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) CALL_STEREOTYPE
Deprecated.
use CallStereotype.STEREOTYPE_NAME
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.StandardProfile.CALL_STEREOTYPE)
CREATE_STEREOTYPE
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) CREATE_STEREOTYPE
Deprecated.
use CreateStereotype.STEREOTYPE_NAME
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.StandardProfile.CREATE_STEREOTYPE)
DERIVE_STEREOTYPE
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) DERIVE_STEREOTYPE
Deprecated.
use DeriveStereotype.STEREOTYPE_NAME
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.StandardProfile.DERIVE_STEREOTYPE)
DESTROY_STEREOTYPE
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) DESTROY_STEREOTYPE
Deprecated.
use DestroyStereotype.STEREOTYPE_NAME
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.StandardProfile.DESTROY_STEREOTYPE)
DOCUMENT_STEREOTYPE
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) DOCUMENT_STEREOTYPE
Deprecated.
use DocumentStereotype.STEREOTYPE_NAME
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.StandardProfile.DOCUMENT_STEREOTYPE)
ENTITY_STEREOTYPE
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) ENTITY_STEREOTYPE
Deprecated.
use EntityStereotype.STEREOTYPE_NAME
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.StandardProfile.ENTITY_STEREOTYPE)
EXECUTABLE_STEREOTYPE
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) EXECUTABLE_STEREOTYPE
Deprecated.
use ExecutableStereotype.STEREOTYPE_NAME
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.StandardProfile.EXECUTABLE_STEREOTYPE)
FILE_STEREOTYPE
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) FILE_STEREOTYPE
Deprecated.
use FileStereotype.STEREOTYPE_NAME
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.StandardProfile.FILE_STEREOTYPE)
FOCUS_STEREOTYPE
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) FOCUS_STEREOTYPE
Deprecated.
use FocusStereotype.STEREOTYPE_NAME
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.StandardProfile.FOCUS_STEREOTYPE)
FRAMEWORK_STEREOTYPE
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) FRAMEWORK_STEREOTYPE
Deprecated.
use FrameworkStereotype.STEREOTYPE_NAME
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.StandardProfile.FRAMEWORK_STEREOTYPE)
IMPLEMENT_STEREOTYPE
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) IMPLEMENT_STEREOTYPE
Deprecated.
use ImplementStereotype.STEREOTYPE_NAME
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.StandardProfile.IMPLEMENT_STEREOTYPE)
IMPLEMENTATIONCLASS_STEREOTYPE
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) IMPLEMENTATIONCLASS_STEREOTYPE
Deprecated.
use ImplementationClassStereotype.STEREOTYPE_NAME
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.StandardProfile.IMPLEMENTATIONCLASS_STEREOTYPE)
INSTANTIATE_STEREOTYPE
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) INSTANTIATE_STEREOTYPE
Deprecated.
use InstantiateStereotype.STEREOTYPE_NAME
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.StandardProfile.INSTANTIATE_STEREOTYPE)
LIBRARY_STEREOTYPE
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) LIBRARY_STEREOTYPE
Deprecated.
use LibraryStereotype.STEREOTYPE_NAME
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.StandardProfile.LIBRARY_STEREOTYPE)
METACLASS_STEREOTYPE
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) METACLASS_STEREOTYPE
Deprecated.
use MetaclassStereotype.STEREOTYPE_NAME
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.StandardProfile.METACLASS_STEREOTYPE)
METAMODEL_STEREOTYPE
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) METAMODEL_STEREOTYPE
Deprecated.
use MetamodelStereotype.STEREOTYPE_NAME
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.StandardProfile.METAMODEL_STEREOTYPE)
MODELLIBRARY_STEREOTYPE
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) MODELLIBRARY_STEREOTYPE
Deprecated.
use ModelLibraryStereotype.STEREOTYPE_NAME
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.StandardProfile.MODELLIBRARY_STEREOTYPE)
PROCESS_STEREOTYPE
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) PROCESS_STEREOTYPE
Deprecated.
use ProcessStereotype.STEREOTYPE_NAME
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.StandardProfile.PROCESS_STEREOTYPE)
REALIZATION_STEREOTYPE
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) REALIZATION_STEREOTYPE
Deprecated.
use RealizationStereotype.STEREOTYPE_NAME
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.StandardProfile.REALIZATION_STEREOTYPE)
REFINE_STEREOTYPE
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) REFINE_STEREOTYPE
Deprecated.
use RefineStereotype.STEREOTYPE_NAME
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.StandardProfile.REFINE_STEREOTYPE)
RESPONSIBILITY_STEREOTYPE
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) RESPONSIBILITY_STEREOTYPE
Deprecated.
use ResponsibilityStereotype.STEREOTYPE_NAME
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.StandardProfile.RESPONSIBILITY_STEREOTYPE)
SCRIPT_STEREOTYPE
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) SCRIPT_STEREOTYPE
Deprecated.
use ScriptStereotype.STEREOTYPE_NAME
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.StandardProfile.SCRIPT_STEREOTYPE)
SEND_STEREOTYPE
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) SEND_STEREOTYPE
Deprecated.
use SendStereotype.STEREOTYPE_NAME
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.StandardProfile.SEND_STEREOTYPE)
SERVICE_STEREOTYPE
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) SERVICE_STEREOTYPE
Deprecated.
use ServiceStereotype.STEREOTYPE_NAME
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.StandardProfile.SERVICE_STEREOTYPE)
SOURCE_STEREOTYPE
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) SOURCE_STEREOTYPE
Deprecated.
use SourceStereotype.STEREOTYPE_NAME
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.StandardProfile.SOURCE_STEREOTYPE)
SPECIFICATION_STEREOTYPE
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) SPECIFICATION_STEREOTYPE
Deprecated.
use SpecificationStereotype.STEREOTYPE_NAME
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.StandardProfile.SPECIFICATION_STEREOTYPE)
SUBSYSTEM_STEREOTYPE
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) SUBSYSTEM_STEREOTYPE
Deprecated.
use SubsystemStereotype.STEREOTYPE_NAME
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.StandardProfile.SUBSYSTEM_STEREOTYPE)
SYSTEMMODEL_STEREOTYPE
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) SYSTEMMODEL_STEREOTYPE
Deprecated.
use SystemModelStereotype.STEREOTYPE_NAME
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.StandardProfile.SYSTEMMODEL_STEREOTYPE)
TRACE_STEREOTYPE
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TRACE_STEREOTYPE
Deprecated.
use TraceStereotype.STEREOTYPE_NAME
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.StandardProfile.TRACE_STEREOTYPE)
TYPE_STEREOTYPE
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TYPE_STEREOTYPE
Deprecated.
use TypeStereotype.STEREOTYPE_NAME
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.StandardProfile.TYPE_STEREOTYPE)
UTILITY_STEREOTYPE
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) UTILITY_STEREOTYPE
Deprecated.
use UtilityStereotype.STEREOTYPE_NAME
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.StandardProfile.UTILITY_STEREOTYPE)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
StandardProfile
public StandardProfile(com.nomagic.profiles.ProfileCache cache)
 ============ METHOD DETAIL ========== 
Method Details
getInstance
public static [StandardProfile](StandardProfile.html) getInstance([BaseElement](../magicdraw/uml/BaseElement.html) baseElement)
getInstanceByProject
public static [StandardProfile](StandardProfile.html) getInstanceByProject(com.nomagic.uml2.project.ElementProject project)
auxiliary
public [StandardProfile.AuxiliaryStereotype](StandardProfile.AuxiliaryStereotype.html) auxiliary()
buildComponent
public [StandardProfile.BuildComponentStereotype](StandardProfile.BuildComponentStereotype.html) buildComponent()
call
public [StandardProfile.CallStereotype](StandardProfile.CallStereotype.html) call()
create
public [StandardProfile.CreateStereotype](StandardProfile.CreateStereotype.html) create()
derive
public [StandardProfile.DeriveStereotype](StandardProfile.DeriveStereotype.html) derive()
destroy
public [StandardProfile.DestroyStereotype](StandardProfile.DestroyStereotype.html) destroy()
document
public [StandardProfile.DocumentStereotype](StandardProfile.DocumentStereotype.html) document()
entity
public [StandardProfile.EntityStereotype](StandardProfile.EntityStereotype.html) entity()
executable
public [StandardProfile.ExecutableStereotype](StandardProfile.ExecutableStereotype.html) executable()
file
public [StandardProfile.FileStereotype](StandardProfile.FileStereotype.html) file()
focus
public [StandardProfile.FocusStereotype](StandardProfile.FocusStereotype.html) focus()
framework
public [StandardProfile.FrameworkStereotype](StandardProfile.FrameworkStereotype.html) framework()
implement
public [StandardProfile.ImplementStereotype](StandardProfile.ImplementStereotype.html) implement()
implementationClass
public [StandardProfile.ImplementationClassStereotype](StandardProfile.ImplementationClassStereotype.html) implementationClass()
instantiate
public [StandardProfile.InstantiateStereotype](StandardProfile.InstantiateStereotype.html) instantiate()
library
public [StandardProfile.LibraryStereotype](StandardProfile.LibraryStereotype.html) library()
metaclass
public [StandardProfile.MetaclassStereotype](StandardProfile.MetaclassStereotype.html) metaclass()
metamodel
public [StandardProfile.MetamodelStereotype](StandardProfile.MetamodelStereotype.html) metamodel()
modelLibrary
public [StandardProfile.ModelLibraryStereotype](StandardProfile.ModelLibraryStereotype.html) modelLibrary()
process
public [StandardProfile.ProcessStereotype](StandardProfile.ProcessStereotype.html) process()
realization
public [StandardProfile.RealizationStereotype](StandardProfile.RealizationStereotype.html) realization()
refine
public [StandardProfile.RefineStereotype](StandardProfile.RefineStereotype.html) refine()
responsibility
public [StandardProfile.ResponsibilityStereotype](StandardProfile.ResponsibilityStereotype.html) responsibility()
script
public [StandardProfile.ScriptStereotype](StandardProfile.ScriptStereotype.html) script()
send
public [StandardProfile.SendStereotype](StandardProfile.SendStereotype.html) send()
service
public [StandardProfile.ServiceStereotype](StandardProfile.ServiceStereotype.html) service()
source
public [StandardProfile.SourceStereotype](StandardProfile.SourceStereotype.html) source()
specification
public [StandardProfile.SpecificationStereotype](StandardProfile.SpecificationStereotype.html) specification()
subsystem
public [StandardProfile.SubsystemStereotype](StandardProfile.SubsystemStereotype.html) subsystem()
systemModel
public [StandardProfile.SystemModelStereotype](StandardProfile.SystemModelStereotype.html) systemModel()
trace
public [StandardProfile.TraceStereotype](StandardProfile.TraceStereotype.html) trace()
type
public [StandardProfile.TypeStereotype](StandardProfile.TypeStereotype.html) type()
utility
public [StandardProfile.UtilityStereotype](StandardProfile.UtilityStereotype.html) utility()
getAuxiliary
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public [Stereotype](ext/magicdraw/mdprofiles/Stereotype.html) getAuxiliary()
Deprecated.
use getInstance(element).auxiliary().getStereotype()
A class that supports another more central or fundamental
 class, typically by implementing secondary logic or control
 flow. The class that the auxiliary supports may be defined
 explicitly using a Focus class or implicitly by a dependency
 relationship. Auxiliary classes are typically used together
 with Focus classes, and are particularly useful for specifying
 the secondary business logic or control flow of components
 during design. See also: focus .
Returns:
stereotype
isAuxiliary
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static boolean isAuxiliary(@CheckForNull
 [Element](ext/magicdraw/classes/mdkernel/Element.html) element)
Deprecated.
use AuxiliaryStereotype.isInstance(element)
getBuildComponent
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public [Stereotype](ext/magicdraw/mdprofiles/Stereotype.html) getBuildComponent()
Deprecated.
use getInstance(element).buildComponent().getStereotype()
A collection of elements defined for the purpose of system level development activities, such as compilation and versioning.
Returns:
stereotype
isBuildComponent
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static boolean isBuildComponent(@CheckForNull
 [Element](ext/magicdraw/classes/mdkernel/Element.html) element)
Deprecated.
use BuildComponentStereotype.isInstance(element)
getCall
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public [Stereotype](ext/magicdraw/mdprofiles/Stereotype.html) getCall()
Deprecated.
use getInstance(element).call().getStereotype()
A usage dependency whose source is an operation and
 whose target is an operation. The relationship may also be
 subsumed to the class containing an operation, with the
 meaning that there exists an operation in the class to which
 the dependency applies.
 A call dependency specifies that the source operation or an
 operation in the source class invokes the target operation or
 an operation in the target class. A call dependency may
 connect a source operation to any target operation that is
 within scope including, but not limited to, operations of the
 enclosing classifier and operations of other visible
 classifiers.
Returns:
stereotype
isCall
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static boolean isCall(@CheckForNull
 [Element](ext/magicdraw/classes/mdkernel/Element.html) element)
Deprecated.
use CallStereotype.isInstance(element)
getCreate
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public [Stereotype](ext/magicdraw/mdprofiles/Stereotype.html) getCreate()
Deprecated.
use getInstance(element).create().getStereotype()
A usage dependency denoting that the client classifier
 creates instances of the supplier classifier.
 Specifies that the designated feature creates an instance of the classifier to which the feature is attached. May be promoted to the Classifier containing the feature.
Returns:
stereotype
isCreate
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static boolean isCreate(@CheckForNull
 [Element](ext/magicdraw/classes/mdkernel/Element.html) element)
Deprecated.
use CreateStereotype.isInstance(element)
getDerive
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public [Stereotype](ext/magicdraw/mdprofiles/Stereotype.html) getDerive()
Deprecated.
use getInstance(element).derive().getStereotype()
Specifies a derivation relationship among model elements
 that are usually, but not necessarily, of the same type. A
 derived dependency specifies that the client may be
 computed from the supplier. The mapping specifies the
 computation. The client may be implemented for design
 reasons, such as efficiency, even though it is logically
 redundant.
Returns:
stereotype
isDerive
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static boolean isDerive(@CheckForNull
 [Element](ext/magicdraw/classes/mdkernel/Element.html) element)
Deprecated.
use DeriveStereotype.isInstance(element)
getDestroy
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public [Stereotype](ext/magicdraw/mdprofiles/Stereotype.html) getDestroy()
Deprecated.
use getInstance(element).destroy().getStereotype()
Specifies that the designated feature destroys an instance of the classifier to which the feature is attached. May be promoted to the classifier containing the feature.
Returns:
stereotype
isDestroy
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static boolean isDestroy(@CheckForNull
 [Element](ext/magicdraw/classes/mdkernel/Element.html) element)
Deprecated.
use DestroyStereotype.isInstance(element)
getDocument
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public [Stereotype](ext/magicdraw/mdprofiles/Stereotype.html) getDocument()
Deprecated.
use getInstance(element).document().getStereotype()
A generic file that is not a source file or executable .
 Subclass of file .
Returns:
stereotype
isDocument
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static boolean isDocument(@CheckForNull
 [Element](ext/magicdraw/classes/mdkernel/Element.html) element)
Deprecated.
use DocumentStereotype.isInstance(element)
getEntity
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public [Stereotype](ext/magicdraw/mdprofiles/Stereotype.html) getEntity()
Deprecated.
use getInstance(element).entity().getStereotype()
A persistent information component representing a business
 concept.
Returns:
stereotype
isEntity
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static boolean isEntity(@CheckForNull
 [Element](ext/magicdraw/classes/mdkernel/Element.html) element)
Deprecated.
use EntityStereotype.isInstance(element)
getExecutable
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public [Stereotype](ext/magicdraw/mdprofiles/Stereotype.html) getExecutable()
Deprecated.
use getInstance(element).executable().getStereotype()
Denotes a program that may be run on a node.
 Denotes a program file that can be executed on a computer system.Subclass of invalid input: '<'>.
Returns:
stereotype
isExecutable
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static boolean isExecutable(@CheckForNull
 [Element](ext/magicdraw/classes/mdkernel/Element.html) element)
Deprecated.
use ExecutableStereotype.isInstance(element)
getFile
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public [Stereotype](ext/magicdraw/mdprofiles/Stereotype.html) getFile()
Deprecated.
use getInstance(element).file().getStereotype()
A physical file in the context of the system developed.
Returns:
stereotype
isFile
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static boolean isFile(@CheckForNull
 [Element](ext/magicdraw/classes/mdkernel/Element.html) element)
Deprecated.
use FileStereotype.isInstance(element)
getFocus
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public [Stereotype](ext/magicdraw/mdprofiles/Stereotype.html) getFocus()
Deprecated.
use getInstance(element).focus().getStereotype()
A class that defines the core logic or control flow for one or
 more auxiliary classes that support it. Support classes may be
 defined explicitly using Auxiliary classes or implicitly by
 dependency relationships. Focus classes are typically used
 together with one or more Auxiliary classes, and are
 particularly useful for specifying the core business logic or
 control flow of components during design. See also:
 auxiliary .
Returns:
stereotype
isFocus
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static boolean isFocus(@CheckForNull
 [Element](ext/magicdraw/classes/mdkernel/Element.html) element)
Deprecated.
use FocusStereotype.isInstance(element)
getFramework
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public [Stereotype](ext/magicdraw/mdprofiles/Stereotype.html) getFramework()
Deprecated.
use getInstance(element).framework().getStereotype()
A package that contains model elements which specify a
 reusable architecture for all or part of a
 system. Frameworks typically include classes, patterns or
 templates. When frameworks are specialized for an
 application domain, they are sometimes referred to as
 application frameworks.
Returns:
stereotype
isFramework
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static boolean isFramework(@CheckForNull
 [Element](ext/magicdraw/classes/mdkernel/Element.html) element)
Deprecated.
use FrameworkStereotype.isInstance(element)
getImplement
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public [Stereotype](ext/magicdraw/mdprofiles/Stereotype.html) getImplement()
Deprecated.
use getInstance(element).implement().getStereotype()
A component definition that is not intended to have a
 specification itself. Rather, it is an implementation for a
 separate specification to which it has a Dependency.
Returns:
stereotype
isImplement
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static boolean isImplement(@CheckForNull
 [Element](ext/magicdraw/classes/mdkernel/Element.html) element)
Deprecated.
use ImplementStereotype.isInstance(element)
getImplementationClass
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public [Stereotype](ext/magicdraw/mdprofiles/Stereotype.html) getImplementationClass()
Deprecated.
use getInstance(element).implementationClass().getStereotype()
The implementation of a class in some programming
 language (e.g., C++, Smalltalk, Java) in which an instance
 may not have more than one class. This is in contrast to
 Class, for which an instance may have multiple classes at one
 time and may gain or lose classes over time, and an object (a
 child of instance) may dynamically
 have multiple classes.
 An Implementation class is said to realize a Classifier if it
 provides all of the operations defined for the Classifier with
 the same behavior as specified for the Classifier's operations.
 An Implementation Class may realize a number of different
 Types. Note that the physical attributes and associations of
 the Implementation class do not have to be the same as those
 of any Classifier it realizes and that the Implementation
 Class may provide methods for its operations in terms of its
 physical attributes and associations. See also: type .
Returns:
stereotype
isImplementationClass
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static boolean isImplementationClass(@CheckForNull
 [Element](ext/magicdraw/classes/mdkernel/Element.html) element)
Deprecated.
use ImplementationClassStereotype.isInstance(element)
getInstantiate
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public [Stereotype](ext/magicdraw/mdprofiles/Stereotype.html) getInstantiate()
Deprecated.
use getInstance(element).instantiate().getStereotype()
A usage dependency among classifiers indicating that
 operations on the client create instances of the supplier.
Returns:
stereotype
isInstantiate
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static boolean isInstantiate(@CheckForNull
 [Element](ext/magicdraw/classes/mdkernel/Element.html) element)
Deprecated.
use InstantiateStereotype.isInstance(element)
getLibrary
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public [Stereotype](ext/magicdraw/mdprofiles/Stereotype.html) getLibrary()
Deprecated.
use getInstance(element).library().getStereotype()
Denotes a static or dynamic library.
 Denotes a static or dynamic library file. Subclass of invalid input: '<'>.
Returns:
stereotype
isLibrary
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static boolean isLibrary(@CheckForNull
 [Element](ext/magicdraw/classes/mdkernel/Element.html) element)
Deprecated.
use LibraryStereotype.isInstance(element)
getMetaclass
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public [Stereotype](ext/magicdraw/mdprofiles/Stereotype.html) getMetaclass()
Deprecated.
use getInstance(element).metaclass().getStereotype()
isMetaclass
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static boolean isMetaclass(@CheckForNull
 [Element](ext/magicdraw/classes/mdkernel/Element.html) element)
Deprecated.
use MetaclassStereotype.isInstance(element)
getMetamodel
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public [Stereotype](ext/magicdraw/mdprofiles/Stereotype.html) getMetamodel()
Deprecated.
use getInstance(element).metamodel().getStereotype()
A model of a model, that typically contains metaclasses.
Returns:
stereotype
isMetamodel
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static boolean isMetamodel(@CheckForNull
 [Element](ext/magicdraw/classes/mdkernel/Element.html) element)
Deprecated.
use MetamodelStereotype.isInstance(element)
getModelLibrary
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public [Stereotype](ext/magicdraw/mdprofiles/Stereotype.html) getModelLibrary()
Deprecated.
use getInstance(element).modelLibrary().getStereotype()
A package that contains model elements which are intended to
 be reused by other packages. Model libraries are frequently
 used in conjunction with applied profiles. This is expressed
 by defining a dependency between a profile and a model
 library package, or by defining a model library as contained
 in a profile package. The classes in a model library are not
 stereotypes and tagged definitions extending the metamodel.
 A model library is analogous to a class library in some
 programming languages.
 When a model library is defined as a part of a profile, it is
 imported or deleted with the application or removal of the
 profile. The profile is implicitly applied to its model library.
 In the other case, when the model library is defined as an
 external package imported by a profile, the profile requires
 that the model library be there in the model at the stage of the
 profile application. The application or the removal of the
 profile does not affect the presence of the model library
 elements.
Returns:
stereotype
isModelLibrary
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static boolean isModelLibrary(@CheckForNull
 [Element](ext/magicdraw/classes/mdkernel/Element.html) element)
Deprecated.
use ModelLibraryStereotype.isInstance(element)
getProcess
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public [Stereotype](ext/magicdraw/mdprofiles/Stereotype.html) getProcess()
Deprecated.
use getInstance(element).process().getStereotype()
A transaction based component.
Returns:
stereotype
isProcess
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static boolean isProcess(@CheckForNull
 [Element](ext/magicdraw/classes/mdkernel/Element.html) element)
Deprecated.
use ProcessStereotype.isInstance(element)
getRealization
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public [Stereotype](ext/magicdraw/mdprofiles/Stereotype.html) getRealization()
Deprecated.
use getInstance(element).realization().getStereotype()
A classifier that specifies a domain of objects and that also
 defines the physical implementation of those objects. For
 example, a Component stereotyped by realization will
 only have realizing Classifiers that implement behavior
 specified by a separate specification Component. See
 specification . This differs from implementation class
 because an implementation class is a realization of a Class
 which can have features such as attributes and methods
 which is useful to system designers.
Returns:
stereotype
isRealization
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static boolean isRealization(@CheckForNull
 [Element](ext/magicdraw/classes/mdkernel/Element.html) element)
Deprecated.
use RealizationStereotype.isInstance(element)
getRefine
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public [Stereotype](ext/magicdraw/mdprofiles/Stereotype.html) getRefine()
Deprecated.
use getInstance(element).refine().getStereotype()
Specifies a refinement relationship between model elements
 at different semantic levels, such as analysis and design. The
 mapping specifies the relationship between the two elements
 or sets of elements. The mapping may or may not be
 computable, and it may be unidirectional or bidirectional.
 Refinement can be used to model transformations from
 analysis to design and other such changes.
Returns:
stereotype
isRefine
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static boolean isRefine(@CheckForNull
 [Element](ext/magicdraw/classes/mdkernel/Element.html) element)
Deprecated.
use RefineStereotype.isInstance(element)
getResponsibility
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public [Stereotype](ext/magicdraw/mdprofiles/Stereotype.html) getResponsibility()
Deprecated.
use getInstance(element).responsibility().getStereotype()
A contract or an obligation of an element in its relationship
 to other elements.
Returns:
stereotype
isResponsibility
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static boolean isResponsibility(@CheckForNull
 [Element](ext/magicdraw/classes/mdkernel/Element.html) element)
Deprecated.
use ResponsibilityStereotype.isInstance(element)
getScript
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public [Stereotype](ext/magicdraw/mdprofiles/Stereotype.html) getScript()
Deprecated.
use getInstance(element).script().getStereotype()
A script file that can be interpreted by a computer system.
 Subclass of file .
Returns:
stereotype
isScript
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static boolean isScript(@CheckForNull
 [Element](ext/magicdraw/classes/mdkernel/Element.html) element)
Deprecated.
use ScriptStereotype.isInstance(element)
getSend
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public [Stereotype](ext/magicdraw/mdprofiles/Stereotype.html) getSend()
Deprecated.
use getInstance(element).send().getStereotype()
A usage dependency whose source is an operation and
 whose target is a signal, specifying that the source sends the
 target signal.
Returns:
stereotype
isSend
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static boolean isSend(@CheckForNull
 [Element](ext/magicdraw/classes/mdkernel/Element.html) element)
Deprecated.
use SendStereotype.isInstance(element)
getService
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public [Stereotype](ext/magicdraw/mdprofiles/Stereotype.html) getService()
Deprecated.
use getInstance(element).service().getStereotype()
A stateless, functional component (computes a value).
Returns:
stereotype
isService
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static boolean isService(@CheckForNull
 [Element](ext/magicdraw/classes/mdkernel/Element.html) element)
Deprecated.
use ServiceStereotype.isInstance(element)
getSource
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public [Stereotype](ext/magicdraw/mdprofiles/Stereotype.html) getSource()
Deprecated.
use getInstance(element).source().getStereotype()
Denotes a source file that can be compiled into an executable file.Subclass of invalid input: '<'>.
Returns:
stereotype
isSource
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static boolean isSource(@CheckForNull
 [Element](ext/magicdraw/classes/mdkernel/Element.html) element)
Deprecated.
use SourceStereotype.isInstance(element)
getSpecification
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public [Stereotype](ext/magicdraw/mdprofiles/Stereotype.html) getSpecification()
Deprecated.
use getInstance(element).specification().getStereotype()
A classifier that specifies a domain of objects without
 defining the physical implementation of those objects. For
 example, a Component stereotyped by specification will
 only have provided and required interfaces, and is not
 intended to have any realizingClassifiers as part of its
 definition. This differs from type because a type can
 have features such as attributes and methods which is useful
 to analysts modeling systems. Also see: realization
Returns:
stereotype
isSpecification
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static boolean isSpecification(@CheckForNull
 [Element](ext/magicdraw/classes/mdkernel/Element.html) element)
Deprecated.
use SpecificationStereotype.isInstance(element)
getSubsystem
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public [Stereotype](ext/magicdraw/mdprofiles/Stereotype.html) getSubsystem()
Deprecated.
use getInstance(element).subsystem().getStereotype()
A unit of hierarchical decomposition for large systems. A
 subsystem is commonly instantiated indirectly. Definitions
 of subsystems vary widely among domains and methods,
 and it is expected that domain and method profiles will
 specialize this construct. A subsystem may be defined to
 have specification and realization elements. See also:
 specification and realization .
Returns:
stereotype
isSubsystem
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static boolean isSubsystem(@CheckForNull
 [Element](ext/magicdraw/classes/mdkernel/Element.html) element)
Deprecated.
use SubsystemStereotype.isInstance(element)
getSystemModel
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public [Stereotype](ext/magicdraw/mdprofiles/Stereotype.html) getSystemModel()
Deprecated.
use getInstance(element).systemModel().getStereotype()
A systemModel is a stereotyped model that contains a
 collection of models of the same physical system. A
 systemModel also contains all relationships and
 constraints between model elements contained in
 different models.
Returns:
stereotype
isSystemModel
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static boolean isSystemModel(@CheckForNull
 [Element](ext/magicdraw/classes/mdkernel/Element.html) element)
Deprecated.
use SystemModelStereotype.isInstance(element)
getTrace
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public [Stereotype](ext/magicdraw/mdprofiles/Stereotype.html) getTrace()
Deprecated.
use getInstance(element).trace().getStereotype()
Specifies a trace relationship between model elements or sets
 of model elements that represent the same concept in
 different models. Traces are mainly used for tracking
 requirements and changes across models. Since model
 changes can occur in both directions, the directionality of the
 dependency can often be ignored. The mapping specifies the
 relationship between the two, but it is rarely computable and
 is usually informal.
Returns:
stereotype
isTrace
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static boolean isTrace(@CheckForNull
 [Element](ext/magicdraw/classes/mdkernel/Element.html) element)
Deprecated.
use TraceStereotype.isInstance(element)
getType
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public [Stereotype](ext/magicdraw/mdprofiles/Stereotype.html) getType()
Deprecated.
use getInstance(element).type().getStereotype()
A class that specifies a domain of objects together with the
 operations applicable to the objects, without defining the
 physical implementation of those objects. However, it may
 have attributes and associations. Behavioral specifications
 for type operations may be expressed using, for example,
 activity diagrams. An object may have at most one
 implementation class, however it may conform to multiple
 different types. See also: implementationClass .
Returns:
stereotype
isType
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static boolean isType(@CheckForNull
 [Element](ext/magicdraw/classes/mdkernel/Element.html) element)
Deprecated.
use TypeStereotype.isInstance(element)
getUtility
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public [Stereotype](ext/magicdraw/mdprofiles/Stereotype.html) getUtility()
Deprecated.
use getInstance(element).utility().getStereotype()
A class that has no instances, but rather denotes a named
 collection of non-member attributes and operations, all of
 which are class-scoped.
Returns:
stereotype
isUtility
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static boolean isUtility(@CheckForNull
 [Element](ext/magicdraw/classes/mdkernel/Element.html) element)
Deprecated.
use UtilityStereotype.isInstance(element)
generatedGetAllElementWrappers
protected [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<com.nomagic.profiles.ProfileImplementation.ProfileElementWrapper> generatedGetAllElementWrappers()
generatedGetAllStereotypes
protected [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Stereotype](ext/magicdraw/mdprofiles/Stereotype.html)> generatedGetAllStereotypes()

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2</a></div>
<h1 class="title" title="Class StandardProfile">Class StandardProfile</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="../profiles/ProfileImplementation.html" title="class in com.nomagic.profiles">com.nomagic.profiles.ProfileImplementation</a>
<div class="inheritance">com.nomagic.uml2.StandardProfile</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">StandardProfile</span>
<span class="extends-implements">extends <a href="../profiles/ProfileImplementation.html" title="class in com.nomagic.profiles">ProfileImplementation</a></span></div>
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
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="StandardProfile.AuxiliaryStereotype.html" title="class in com.nomagic.uml2">StandardProfile.AuxiliaryStereotype</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="StandardProfile.BuildComponentStereotype.html" title="class in com.nomagic.uml2">StandardProfile.BuildComponentStereotype</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="StandardProfile.CallStereotype.html" title="class in com.nomagic.uml2">StandardProfile.CallStereotype</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="StandardProfile.CreateStereotype.html" title="class in com.nomagic.uml2">StandardProfile.CreateStereotype</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="StandardProfile.DeriveStereotype.html" title="class in com.nomagic.uml2">StandardProfile.DeriveStereotype</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="StandardProfile.DestroyStereotype.html" title="class in com.nomagic.uml2">StandardProfile.DestroyStereotype</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="StandardProfile.DocumentStereotype.html" title="class in com.nomagic.uml2">StandardProfile.DocumentStereotype</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="StandardProfile.EntityStereotype.html" title="class in com.nomagic.uml2">StandardProfile.EntityStereotype</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="StandardProfile.ExecutableStereotype.html" title="class in com.nomagic.uml2">StandardProfile.ExecutableStereotype</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="StandardProfile.FileStereotype.html" title="class in com.nomagic.uml2">StandardProfile.FileStereotype</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="StandardProfile.FocusStereotype.html" title="class in com.nomagic.uml2">StandardProfile.FocusStereotype</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="StandardProfile.FrameworkStereotype.html" title="class in com.nomagic.uml2">StandardProfile.FrameworkStereotype</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="StandardProfile.ImplementationClassStereotype.html" title="class in com.nomagic.uml2">StandardProfile.ImplementationClassStereotype</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="StandardProfile.ImplementStereotype.html" title="class in com.nomagic.uml2">StandardProfile.ImplementStereotype</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="StandardProfile.InstantiateStereotype.html" title="class in com.nomagic.uml2">StandardProfile.InstantiateStereotype</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="StandardProfile.LibraryStereotype.html" title="class in com.nomagic.uml2">StandardProfile.LibraryStereotype</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="StandardProfile.MetaclassStereotype.html" title="class in com.nomagic.uml2">StandardProfile.MetaclassStereotype</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="StandardProfile.MetamodelStereotype.html" title="class in com.nomagic.uml2">StandardProfile.MetamodelStereotype</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="StandardProfile.ModelLibraryStereotype.html" title="class in com.nomagic.uml2">StandardProfile.ModelLibraryStereotype</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="StandardProfile.ProcessStereotype.html" title="class in com.nomagic.uml2">StandardProfile.ProcessStereotype</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="StandardProfile.RealizationStereotype.html" title="class in com.nomagic.uml2">StandardProfile.RealizationStereotype</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="StandardProfile.RefineStereotype.html" title="class in com.nomagic.uml2">StandardProfile.RefineStereotype</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="StandardProfile.ResponsibilityStereotype.html" title="class in com.nomagic.uml2">StandardProfile.ResponsibilityStereotype</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="StandardProfile.ScriptStereotype.html" title="class in com.nomagic.uml2">StandardProfile.ScriptStereotype</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="StandardProfile.SendStereotype.html" title="class in com.nomagic.uml2">StandardProfile.SendStereotype</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="StandardProfile.ServiceStereotype.html" title="class in com.nomagic.uml2">StandardProfile.ServiceStereotype</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="StandardProfile.SourceStereotype.html" title="class in com.nomagic.uml2">StandardProfile.SourceStereotype</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="StandardProfile.SpecificationStereotype.html" title="class in com.nomagic.uml2">StandardProfile.SpecificationStereotype</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="StandardProfile.SubsystemStereotype.html" title="class in com.nomagic.uml2">StandardProfile.SubsystemStereotype</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="StandardProfile.SystemModelStereotype.html" title="class in com.nomagic.uml2">StandardProfile.SystemModelStereotype</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="StandardProfile.TraceStereotype.html" title="class in com.nomagic.uml2">StandardProfile.TraceStereotype</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="StandardProfile.TypeStereotype.html" title="class in com.nomagic.uml2">StandardProfile.TypeStereotype</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="StandardProfile.UtilityStereotype.html" title="class in com.nomagic.uml2">StandardProfile.UtilityStereotype</a></code></div>
<div class="col-last even-row-color"> </div>
</div>
<div class="inherited-list">
<h2 id="nested-classes-inherited-from-class-com.nomagic.profiles.ProfileImplementation">Nested classes/interfaces inherited from class com.nomagic.profiles.<a href="../profiles/ProfileImplementation.html" title="class in com.nomagic.profiles">ProfileImplementation</a></h2>
<code><a href="../profiles/ProfileImplementation.StereotypeWrapper.html" title="class in com.nomagic.profiles">ProfileImplementation.StereotypeWrapper</a></code></div>
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
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#AUXILIARY_STEREOTYPE">AUXILIARY_STEREOTYPE</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use AuxiliaryStereotype.STEREOTYPE_NAME</div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#BUILDCOMPONENT_STEREOTYPE">BUILDCOMPONENT_STEREOTYPE</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use BuildComponentStereotype.STEREOTYPE_NAME</div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CALL_STEREOTYPE">CALL_STEREOTYPE</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use CallStereotype.STEREOTYPE_NAME</div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#CREATE_STEREOTYPE">CREATE_STEREOTYPE</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use CreateStereotype.STEREOTYPE_NAME</div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DERIVE_STEREOTYPE">DERIVE_STEREOTYPE</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DeriveStereotype.STEREOTYPE_NAME</div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DESTROY_STEREOTYPE">DESTROY_STEREOTYPE</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DestroyStereotype.STEREOTYPE_NAME</div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DOCUMENT_STEREOTYPE">DOCUMENT_STEREOTYPE</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DocumentStereotype.STEREOTYPE_NAME</div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ENTITY_STEREOTYPE">ENTITY_STEREOTYPE</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use EntityStereotype.STEREOTYPE_NAME</div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#EXECUTABLE_STEREOTYPE">EXECUTABLE_STEREOTYPE</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ExecutableStereotype.STEREOTYPE_NAME</div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#FILE_STEREOTYPE">FILE_STEREOTYPE</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use FileStereotype.STEREOTYPE_NAME</div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#FOCUS_STEREOTYPE">FOCUS_STEREOTYPE</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use FocusStereotype.STEREOTYPE_NAME</div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#FRAMEWORK_STEREOTYPE">FRAMEWORK_STEREOTYPE</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use FrameworkStereotype.STEREOTYPE_NAME</div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#IMPLEMENT_STEREOTYPE">IMPLEMENT_STEREOTYPE</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ImplementStereotype.STEREOTYPE_NAME</div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#IMPLEMENTATIONCLASS_STEREOTYPE">IMPLEMENTATIONCLASS_STEREOTYPE</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ImplementationClassStereotype.STEREOTYPE_NAME</div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#INSTANTIATE_STEREOTYPE">INSTANTIATE_STEREOTYPE</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use InstantiateStereotype.STEREOTYPE_NAME</div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#LIBRARY_STEREOTYPE">LIBRARY_STEREOTYPE</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use LibraryStereotype.STEREOTYPE_NAME</div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#METACLASS_STEREOTYPE">METACLASS_STEREOTYPE</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use MetaclassStereotype.STEREOTYPE_NAME</div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#METAMODEL_STEREOTYPE">METAMODEL_STEREOTYPE</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use MetamodelStereotype.STEREOTYPE_NAME</div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#MODELLIBRARY_STEREOTYPE">MODELLIBRARY_STEREOTYPE</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ModelLibraryStereotype.STEREOTYPE_NAME</div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#PROCESS_STEREOTYPE">PROCESS_STEREOTYPE</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ProcessStereotype.STEREOTYPE_NAME</div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#PROFILE_NAME">PROFILE_NAME</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#PROFILE_URI">PROFILE_URI</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#REALIZATION_STEREOTYPE">REALIZATION_STEREOTYPE</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use RealizationStereotype.STEREOTYPE_NAME</div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#REFINE_STEREOTYPE">REFINE_STEREOTYPE</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use RefineStereotype.STEREOTYPE_NAME</div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#RESPONSIBILITY_STEREOTYPE">RESPONSIBILITY_STEREOTYPE</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ResponsibilityStereotype.STEREOTYPE_NAME</div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SCRIPT_STEREOTYPE">SCRIPT_STEREOTYPE</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ScriptStereotype.STEREOTYPE_NAME</div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SEND_STEREOTYPE">SEND_STEREOTYPE</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use SendStereotype.STEREOTYPE_NAME</div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SERVICE_STEREOTYPE">SERVICE_STEREOTYPE</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ServiceStereotype.STEREOTYPE_NAME</div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SOURCE_STEREOTYPE">SOURCE_STEREOTYPE</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use SourceStereotype.STEREOTYPE_NAME</div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SPECIFICATION_STEREOTYPE">SPECIFICATION_STEREOTYPE</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use SpecificationStereotype.STEREOTYPE_NAME</div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SUBSYSTEM_STEREOTYPE">SUBSYSTEM_STEREOTYPE</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use SubsystemStereotype.STEREOTYPE_NAME</div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SYSTEMMODEL_STEREOTYPE">SYSTEMMODEL_STEREOTYPE</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use SystemModelStereotype.STEREOTYPE_NAME</div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TRACE_STEREOTYPE">TRACE_STEREOTYPE</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use TraceStereotype.STEREOTYPE_NAME</div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TYPE_STEREOTYPE">TYPE_STEREOTYPE</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use TypeStereotype.STEREOTYPE_NAME</div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#UTILITY_STEREOTYPE">UTILITY_STEREOTYPE</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use UtilityStereotype.STEREOTYPE_NAME</div>
</div>
</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.profiles.ProfileCache)">StandardProfile</a><wbr/>(com.nomagic.profiles.ProfileCache cache)</code></div>
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
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="StandardProfile.AuxiliaryStereotype.html" title="class in com.nomagic.uml2">StandardProfile.AuxiliaryStereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#auxiliary()">auxiliary</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="StandardProfile.BuildComponentStereotype.html" title="class in com.nomagic.uml2">StandardProfile.BuildComponentStereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#buildComponent()">buildComponent</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="StandardProfile.CallStereotype.html" title="class in com.nomagic.uml2">StandardProfile.CallStereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#call()">call</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="StandardProfile.CreateStereotype.html" title="class in com.nomagic.uml2">StandardProfile.CreateStereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#create()">create</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="StandardProfile.DeriveStereotype.html" title="class in com.nomagic.uml2">StandardProfile.DeriveStereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#derive()">derive</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="StandardProfile.DestroyStereotype.html" title="class in com.nomagic.uml2">StandardProfile.DestroyStereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#destroy()">destroy</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="StandardProfile.DocumentStereotype.html" title="class in com.nomagic.uml2">StandardProfile.DocumentStereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#document()">document</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="StandardProfile.EntityStereotype.html" title="class in com.nomagic.uml2">StandardProfile.EntityStereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#entity()">entity</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="StandardProfile.ExecutableStereotype.html" title="class in com.nomagic.uml2">StandardProfile.ExecutableStereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#executable()">executable</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="StandardProfile.FileStereotype.html" title="class in com.nomagic.uml2">StandardProfile.FileStereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#file()">file</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="StandardProfile.FocusStereotype.html" title="class in com.nomagic.uml2">StandardProfile.FocusStereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#focus()">focus</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="StandardProfile.FrameworkStereotype.html" title="class in com.nomagic.uml2">StandardProfile.FrameworkStereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#framework()">framework</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;com.nomagic.profiles.ProfileImplementation.ProfileElementWrapper&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#generatedGetAllElementWrappers()">generatedGetAllElementWrappers</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#generatedGetAllStereotypes()">generatedGetAllStereotypes</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getAuxiliary()">getAuxiliary</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).auxiliary().getStereotype()</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getBuildComponent()">getBuildComponent</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).buildComponent().getStereotype()</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getCall()">getCall</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).call().getStereotype()</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getCreate()">getCreate</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).create().getStereotype()</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getDerive()">getDerive</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).derive().getStereotype()</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getDestroy()">getDestroy</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).destroy().getStereotype()</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getDocument()">getDocument</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).document().getStereotype()</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getEntity()">getEntity</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).entity().getStereotype()</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getExecutable()">getExecutable</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).executable().getStereotype()</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getFile()">getFile</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).file().getStereotype()</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getFocus()">getFocus</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).focus().getStereotype()</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getFramework()">getFramework</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).framework().getStereotype()</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getImplement()">getImplement</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).implement().getStereotype()</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getImplementationClass()">getImplementationClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).implementationClass().getStereotype()</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="StandardProfile.html" title="class in com.nomagic.uml2">StandardProfile</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstance(com.nomagic.magicdraw.uml.BaseElement)">getInstance</a><wbr/>(<a href="../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> baseElement)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="StandardProfile.html" title="class in com.nomagic.uml2">StandardProfile</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstanceByProject(com.nomagic.uml2.project.ElementProject)">getInstanceByProject</a><wbr/>(com.nomagic.uml2.project.ElementProject project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getInstantiate()">getInstantiate</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).instantiate().getStereotype()</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getLibrary()">getLibrary</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).library().getStereotype()</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getMetaclass()">getMetaclass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).metaclass().getStereotype()</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getMetamodel()">getMetamodel</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).metamodel().getStereotype()</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getModelLibrary()">getModelLibrary</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).modelLibrary().getStereotype()</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getProcess()">getProcess</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).process().getStereotype()</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getRealization()">getRealization</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).realization().getStereotype()</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getRefine()">getRefine</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).refine().getStereotype()</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getResponsibility()">getResponsibility</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).responsibility().getStereotype()</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getScript()">getScript</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).script().getStereotype()</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getSend()">getSend</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).send().getStereotype()</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getService()">getService</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).service().getStereotype()</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getSource()">getSource</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).source().getStereotype()</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getSpecification()">getSpecification</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).specification().getStereotype()</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getSubsystem()">getSubsystem</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).subsystem().getStereotype()</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getSystemModel()">getSystemModel</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).systemModel().getStereotype()</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getTrace()">getTrace</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).trace().getStereotype()</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getType()">getType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).type().getStereotype()</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getUtility()">getUtility</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).utility().getStereotype()</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="StandardProfile.ImplementStereotype.html" title="class in com.nomagic.uml2">StandardProfile.ImplementStereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#implement()">implement</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="StandardProfile.ImplementationClassStereotype.html" title="class in com.nomagic.uml2">StandardProfile.ImplementationClassStereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#implementationClass()">implementationClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="StandardProfile.InstantiateStereotype.html" title="class in com.nomagic.uml2">StandardProfile.InstantiateStereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#instantiate()">instantiate</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isAuxiliary(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isAuxiliary</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use AuxiliaryStereotype.isInstance(element)</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isBuildComponent(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isBuildComponent</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use BuildComponentStereotype.isInstance(element)</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isCall(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isCall</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use CallStereotype.isInstance(element)</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isCreate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isCreate</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use CreateStereotype.isInstance(element)</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isDerive(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isDerive</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DeriveStereotype.isInstance(element)</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isDestroy(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isDestroy</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DestroyStereotype.isInstance(element)</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isDocument(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isDocument</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DocumentStereotype.isInstance(element)</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isEntity(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isEntity</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use EntityStereotype.isInstance(element)</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isExecutable(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isExecutable</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ExecutableStereotype.isInstance(element)</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isFile(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isFile</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use FileStereotype.isInstance(element)</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isFocus(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isFocus</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use FocusStereotype.isInstance(element)</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isFramework(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isFramework</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use FrameworkStereotype.isInstance(element)</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isImplement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isImplement</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ImplementStereotype.isInstance(element)</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isImplementationClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isImplementationClass</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ImplementationClassStereotype.isInstance(element)</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isInstantiate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isInstantiate</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use InstantiateStereotype.isInstance(element)</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isLibrary(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isLibrary</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use LibraryStereotype.isInstance(element)</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isMetaclass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isMetaclass</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use MetaclassStereotype.isInstance(element)</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isMetamodel(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isMetamodel</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use MetamodelStereotype.isInstance(element)</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isModelLibrary(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isModelLibrary</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ModelLibraryStereotype.isInstance(element)</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isProcess(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isProcess</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ProcessStereotype.isInstance(element)</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isRealization(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isRealization</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use RealizationStereotype.isInstance(element)</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isRefine(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isRefine</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use RefineStereotype.isInstance(element)</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isResponsibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isResponsibility</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ResponsibilityStereotype.isInstance(element)</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isScript(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isScript</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ScriptStereotype.isInstance(element)</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isSend(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isSend</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use SendStereotype.isInstance(element)</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isService(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isService</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ServiceStereotype.isInstance(element)</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isSource(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isSource</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use SourceStereotype.isInstance(element)</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isSpecification</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use SpecificationStereotype.isInstance(element)</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isSubsystem(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isSubsystem</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use SubsystemStereotype.isInstance(element)</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isSystemModel(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isSystemModel</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use SystemModelStereotype.isInstance(element)</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isTrace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isTrace</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use TraceStereotype.isInstance(element)</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isType</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use TypeStereotype.isInstance(element)</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isUtility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isUtility</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use UtilityStereotype.isInstance(element)</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="StandardProfile.LibraryStereotype.html" title="class in com.nomagic.uml2">StandardProfile.LibraryStereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#library()">library</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="StandardProfile.MetaclassStereotype.html" title="class in com.nomagic.uml2">StandardProfile.MetaclassStereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#metaclass()">metaclass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="StandardProfile.MetamodelStereotype.html" title="class in com.nomagic.uml2">StandardProfile.MetamodelStereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#metamodel()">metamodel</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="StandardProfile.ModelLibraryStereotype.html" title="class in com.nomagic.uml2">StandardProfile.ModelLibraryStereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#modelLibrary()">modelLibrary</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="StandardProfile.ProcessStereotype.html" title="class in com.nomagic.uml2">StandardProfile.ProcessStereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#process()">process</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="StandardProfile.RealizationStereotype.html" title="class in com.nomagic.uml2">StandardProfile.RealizationStereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#realization()">realization</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="StandardProfile.RefineStereotype.html" title="class in com.nomagic.uml2">StandardProfile.RefineStereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#refine()">refine</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="StandardProfile.ResponsibilityStereotype.html" title="class in com.nomagic.uml2">StandardProfile.ResponsibilityStereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#responsibility()">responsibility</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="StandardProfile.ScriptStereotype.html" title="class in com.nomagic.uml2">StandardProfile.ScriptStereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#script()">script</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="StandardProfile.SendStereotype.html" title="class in com.nomagic.uml2">StandardProfile.SendStereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#send()">send</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="StandardProfile.ServiceStereotype.html" title="class in com.nomagic.uml2">StandardProfile.ServiceStereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#service()">service</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="StandardProfile.SourceStereotype.html" title="class in com.nomagic.uml2">StandardProfile.SourceStereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#source()">source</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="StandardProfile.SpecificationStereotype.html" title="class in com.nomagic.uml2">StandardProfile.SpecificationStereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#specification()">specification</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="StandardProfile.SubsystemStereotype.html" title="class in com.nomagic.uml2">StandardProfile.SubsystemStereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#subsystem()">subsystem</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="StandardProfile.SystemModelStereotype.html" title="class in com.nomagic.uml2">StandardProfile.SystemModelStereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#systemModel()">systemModel</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="StandardProfile.TraceStereotype.html" title="class in com.nomagic.uml2">StandardProfile.TraceStereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#trace()">trace</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="StandardProfile.TypeStereotype.html" title="class in com.nomagic.uml2">StandardProfile.TypeStereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#type()">type</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="StandardProfile.UtilityStereotype.html" title="class in com.nomagic.uml2">StandardProfile.UtilityStereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#utility()">utility</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
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
<section class="detail" id="PROFILE_URI">
<h3>PROFILE_URI</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">PROFILE_URI</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.StandardProfile.PROFILE_URI">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PROFILE_NAME">
<h3>PROFILE_NAME</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">PROFILE_NAME</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.StandardProfile.PROFILE_NAME">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="AUXILIARY_STEREOTYPE">
<h3>AUXILIARY_STEREOTYPE</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">AUXILIARY_STEREOTYPE</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use AuxiliaryStereotype.STEREOTYPE_NAME</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.StandardProfile.AUXILIARY_STEREOTYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="BUILDCOMPONENT_STEREOTYPE">
<h3>BUILDCOMPONENT_STEREOTYPE</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">BUILDCOMPONENT_STEREOTYPE</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use BuildComponentStereotype.STEREOTYPE_NAME</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.StandardProfile.BUILDCOMPONENT_STEREOTYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CALL_STEREOTYPE">
<h3>CALL_STEREOTYPE</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">CALL_STEREOTYPE</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use CallStereotype.STEREOTYPE_NAME</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.StandardProfile.CALL_STEREOTYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CREATE_STEREOTYPE">
<h3>CREATE_STEREOTYPE</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">CREATE_STEREOTYPE</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use CreateStereotype.STEREOTYPE_NAME</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.StandardProfile.CREATE_STEREOTYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DERIVE_STEREOTYPE">
<h3>DERIVE_STEREOTYPE</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DERIVE_STEREOTYPE</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DeriveStereotype.STEREOTYPE_NAME</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.StandardProfile.DERIVE_STEREOTYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DESTROY_STEREOTYPE">
<h3>DESTROY_STEREOTYPE</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DESTROY_STEREOTYPE</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DestroyStereotype.STEREOTYPE_NAME</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.StandardProfile.DESTROY_STEREOTYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DOCUMENT_STEREOTYPE">
<h3>DOCUMENT_STEREOTYPE</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DOCUMENT_STEREOTYPE</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DocumentStereotype.STEREOTYPE_NAME</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.StandardProfile.DOCUMENT_STEREOTYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ENTITY_STEREOTYPE">
<h3>ENTITY_STEREOTYPE</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ENTITY_STEREOTYPE</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use EntityStereotype.STEREOTYPE_NAME</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.StandardProfile.ENTITY_STEREOTYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="EXECUTABLE_STEREOTYPE">
<h3>EXECUTABLE_STEREOTYPE</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">EXECUTABLE_STEREOTYPE</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ExecutableStereotype.STEREOTYPE_NAME</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.StandardProfile.EXECUTABLE_STEREOTYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="FILE_STEREOTYPE">
<h3>FILE_STEREOTYPE</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">FILE_STEREOTYPE</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use FileStereotype.STEREOTYPE_NAME</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.StandardProfile.FILE_STEREOTYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="FOCUS_STEREOTYPE">
<h3>FOCUS_STEREOTYPE</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">FOCUS_STEREOTYPE</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use FocusStereotype.STEREOTYPE_NAME</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.StandardProfile.FOCUS_STEREOTYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="FRAMEWORK_STEREOTYPE">
<h3>FRAMEWORK_STEREOTYPE</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">FRAMEWORK_STEREOTYPE</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use FrameworkStereotype.STEREOTYPE_NAME</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.StandardProfile.FRAMEWORK_STEREOTYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="IMPLEMENT_STEREOTYPE">
<h3>IMPLEMENT_STEREOTYPE</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">IMPLEMENT_STEREOTYPE</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ImplementStereotype.STEREOTYPE_NAME</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.StandardProfile.IMPLEMENT_STEREOTYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="IMPLEMENTATIONCLASS_STEREOTYPE">
<h3>IMPLEMENTATIONCLASS_STEREOTYPE</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">IMPLEMENTATIONCLASS_STEREOTYPE</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ImplementationClassStereotype.STEREOTYPE_NAME</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.StandardProfile.IMPLEMENTATIONCLASS_STEREOTYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="INSTANTIATE_STEREOTYPE">
<h3>INSTANTIATE_STEREOTYPE</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">INSTANTIATE_STEREOTYPE</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use InstantiateStereotype.STEREOTYPE_NAME</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.StandardProfile.INSTANTIATE_STEREOTYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LIBRARY_STEREOTYPE">
<h3>LIBRARY_STEREOTYPE</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">LIBRARY_STEREOTYPE</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use LibraryStereotype.STEREOTYPE_NAME</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.StandardProfile.LIBRARY_STEREOTYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="METACLASS_STEREOTYPE">
<h3>METACLASS_STEREOTYPE</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">METACLASS_STEREOTYPE</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use MetaclassStereotype.STEREOTYPE_NAME</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.StandardProfile.METACLASS_STEREOTYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="METAMODEL_STEREOTYPE">
<h3>METAMODEL_STEREOTYPE</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">METAMODEL_STEREOTYPE</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use MetamodelStereotype.STEREOTYPE_NAME</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.StandardProfile.METAMODEL_STEREOTYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="MODELLIBRARY_STEREOTYPE">
<h3>MODELLIBRARY_STEREOTYPE</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">MODELLIBRARY_STEREOTYPE</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ModelLibraryStereotype.STEREOTYPE_NAME</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.StandardProfile.MODELLIBRARY_STEREOTYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PROCESS_STEREOTYPE">
<h3>PROCESS_STEREOTYPE</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">PROCESS_STEREOTYPE</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ProcessStereotype.STEREOTYPE_NAME</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.StandardProfile.PROCESS_STEREOTYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="REALIZATION_STEREOTYPE">
<h3>REALIZATION_STEREOTYPE</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">REALIZATION_STEREOTYPE</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use RealizationStereotype.STEREOTYPE_NAME</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.StandardProfile.REALIZATION_STEREOTYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="REFINE_STEREOTYPE">
<h3>REFINE_STEREOTYPE</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">REFINE_STEREOTYPE</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use RefineStereotype.STEREOTYPE_NAME</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.StandardProfile.REFINE_STEREOTYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="RESPONSIBILITY_STEREOTYPE">
<h3>RESPONSIBILITY_STEREOTYPE</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">RESPONSIBILITY_STEREOTYPE</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ResponsibilityStereotype.STEREOTYPE_NAME</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.StandardProfile.RESPONSIBILITY_STEREOTYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SCRIPT_STEREOTYPE">
<h3>SCRIPT_STEREOTYPE</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SCRIPT_STEREOTYPE</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ScriptStereotype.STEREOTYPE_NAME</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.StandardProfile.SCRIPT_STEREOTYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SEND_STEREOTYPE">
<h3>SEND_STEREOTYPE</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SEND_STEREOTYPE</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use SendStereotype.STEREOTYPE_NAME</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.StandardProfile.SEND_STEREOTYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SERVICE_STEREOTYPE">
<h3>SERVICE_STEREOTYPE</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SERVICE_STEREOTYPE</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ServiceStereotype.STEREOTYPE_NAME</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.StandardProfile.SERVICE_STEREOTYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SOURCE_STEREOTYPE">
<h3>SOURCE_STEREOTYPE</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SOURCE_STEREOTYPE</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use SourceStereotype.STEREOTYPE_NAME</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.StandardProfile.SOURCE_STEREOTYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SPECIFICATION_STEREOTYPE">
<h3>SPECIFICATION_STEREOTYPE</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SPECIFICATION_STEREOTYPE</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use SpecificationStereotype.STEREOTYPE_NAME</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.StandardProfile.SPECIFICATION_STEREOTYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SUBSYSTEM_STEREOTYPE">
<h3>SUBSYSTEM_STEREOTYPE</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SUBSYSTEM_STEREOTYPE</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use SubsystemStereotype.STEREOTYPE_NAME</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.StandardProfile.SUBSYSTEM_STEREOTYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SYSTEMMODEL_STEREOTYPE">
<h3>SYSTEMMODEL_STEREOTYPE</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SYSTEMMODEL_STEREOTYPE</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use SystemModelStereotype.STEREOTYPE_NAME</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.StandardProfile.SYSTEMMODEL_STEREOTYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TRACE_STEREOTYPE">
<h3>TRACE_STEREOTYPE</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TRACE_STEREOTYPE</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use TraceStereotype.STEREOTYPE_NAME</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.StandardProfile.TRACE_STEREOTYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TYPE_STEREOTYPE">
<h3>TYPE_STEREOTYPE</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TYPE_STEREOTYPE</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use TypeStereotype.STEREOTYPE_NAME</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.StandardProfile.TYPE_STEREOTYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="UTILITY_STEREOTYPE">
<h3>UTILITY_STEREOTYPE</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">UTILITY_STEREOTYPE</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use UtilityStereotype.STEREOTYPE_NAME</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.StandardProfile.UTILITY_STEREOTYPE">Constant Field Values</a></li>
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
<section class="detail" id="&lt;init&gt;(com.nomagic.profiles.ProfileCache)">
<h3>StandardProfile</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">StandardProfile</span><wbr/><span class="parameters">(com.nomagic.profiles.ProfileCache cache)</span></div>
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
<section class="detail" id="getInstance(com.nomagic.magicdraw.uml.BaseElement)">
<h3>getInstance</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="StandardProfile.html" title="class in com.nomagic.uml2">StandardProfile</a></span> <span class="element-name">getInstance</span><wbr/><span class="parameters">(<a href="../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> baseElement)</span></div>
</section>
</li>
<li>
<section class="detail" id="getInstanceByProject(com.nomagic.uml2.project.ElementProject)">
<h3>getInstanceByProject</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="StandardProfile.html" title="class in com.nomagic.uml2">StandardProfile</a></span> <span class="element-name">getInstanceByProject</span><wbr/><span class="parameters">(com.nomagic.uml2.project.ElementProject project)</span></div>
</section>
</li>
<li>
<section class="detail" id="auxiliary()">
<h3>auxiliary</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="StandardProfile.AuxiliaryStereotype.html" title="class in com.nomagic.uml2">StandardProfile.AuxiliaryStereotype</a></span> <span class="element-name">auxiliary</span>()</div>
</section>
</li>
<li>
<section class="detail" id="buildComponent()">
<h3>buildComponent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="StandardProfile.BuildComponentStereotype.html" title="class in com.nomagic.uml2">StandardProfile.BuildComponentStereotype</a></span> <span class="element-name">buildComponent</span>()</div>
</section>
</li>
<li>
<section class="detail" id="call()">
<h3>call</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="StandardProfile.CallStereotype.html" title="class in com.nomagic.uml2">StandardProfile.CallStereotype</a></span> <span class="element-name">call</span>()</div>
</section>
</li>
<li>
<section class="detail" id="create()">
<h3>create</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="StandardProfile.CreateStereotype.html" title="class in com.nomagic.uml2">StandardProfile.CreateStereotype</a></span> <span class="element-name">create</span>()</div>
</section>
</li>
<li>
<section class="detail" id="derive()">
<h3>derive</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="StandardProfile.DeriveStereotype.html" title="class in com.nomagic.uml2">StandardProfile.DeriveStereotype</a></span> <span class="element-name">derive</span>()</div>
</section>
</li>
<li>
<section class="detail" id="destroy()">
<h3>destroy</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="StandardProfile.DestroyStereotype.html" title="class in com.nomagic.uml2">StandardProfile.DestroyStereotype</a></span> <span class="element-name">destroy</span>()</div>
</section>
</li>
<li>
<section class="detail" id="document()">
<h3>document</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="StandardProfile.DocumentStereotype.html" title="class in com.nomagic.uml2">StandardProfile.DocumentStereotype</a></span> <span class="element-name">document</span>()</div>
</section>
</li>
<li>
<section class="detail" id="entity()">
<h3>entity</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="StandardProfile.EntityStereotype.html" title="class in com.nomagic.uml2">StandardProfile.EntityStereotype</a></span> <span class="element-name">entity</span>()</div>
</section>
</li>
<li>
<section class="detail" id="executable()">
<h3>executable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="StandardProfile.ExecutableStereotype.html" title="class in com.nomagic.uml2">StandardProfile.ExecutableStereotype</a></span> <span class="element-name">executable</span>()</div>
</section>
</li>
<li>
<section class="detail" id="file()">
<h3>file</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="StandardProfile.FileStereotype.html" title="class in com.nomagic.uml2">StandardProfile.FileStereotype</a></span> <span class="element-name">file</span>()</div>
</section>
</li>
<li>
<section class="detail" id="focus()">
<h3>focus</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="StandardProfile.FocusStereotype.html" title="class in com.nomagic.uml2">StandardProfile.FocusStereotype</a></span> <span class="element-name">focus</span>()</div>
</section>
</li>
<li>
<section class="detail" id="framework()">
<h3>framework</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="StandardProfile.FrameworkStereotype.html" title="class in com.nomagic.uml2">StandardProfile.FrameworkStereotype</a></span> <span class="element-name">framework</span>()</div>
</section>
</li>
<li>
<section class="detail" id="implement()">
<h3>implement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="StandardProfile.ImplementStereotype.html" title="class in com.nomagic.uml2">StandardProfile.ImplementStereotype</a></span> <span class="element-name">implement</span>()</div>
</section>
</li>
<li>
<section class="detail" id="implementationClass()">
<h3>implementationClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="StandardProfile.ImplementationClassStereotype.html" title="class in com.nomagic.uml2">StandardProfile.ImplementationClassStereotype</a></span> <span class="element-name">implementationClass</span>()</div>
</section>
</li>
<li>
<section class="detail" id="instantiate()">
<h3>instantiate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="StandardProfile.InstantiateStereotype.html" title="class in com.nomagic.uml2">StandardProfile.InstantiateStereotype</a></span> <span class="element-name">instantiate</span>()</div>
</section>
</li>
<li>
<section class="detail" id="library()">
<h3>library</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="StandardProfile.LibraryStereotype.html" title="class in com.nomagic.uml2">StandardProfile.LibraryStereotype</a></span> <span class="element-name">library</span>()</div>
</section>
</li>
<li>
<section class="detail" id="metaclass()">
<h3>metaclass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="StandardProfile.MetaclassStereotype.html" title="class in com.nomagic.uml2">StandardProfile.MetaclassStereotype</a></span> <span class="element-name">metaclass</span>()</div>
</section>
</li>
<li>
<section class="detail" id="metamodel()">
<h3>metamodel</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="StandardProfile.MetamodelStereotype.html" title="class in com.nomagic.uml2">StandardProfile.MetamodelStereotype</a></span> <span class="element-name">metamodel</span>()</div>
</section>
</li>
<li>
<section class="detail" id="modelLibrary()">
<h3>modelLibrary</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="StandardProfile.ModelLibraryStereotype.html" title="class in com.nomagic.uml2">StandardProfile.ModelLibraryStereotype</a></span> <span class="element-name">modelLibrary</span>()</div>
</section>
</li>
<li>
<section class="detail" id="process()">
<h3>process</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="StandardProfile.ProcessStereotype.html" title="class in com.nomagic.uml2">StandardProfile.ProcessStereotype</a></span> <span class="element-name">process</span>()</div>
</section>
</li>
<li>
<section class="detail" id="realization()">
<h3>realization</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="StandardProfile.RealizationStereotype.html" title="class in com.nomagic.uml2">StandardProfile.RealizationStereotype</a></span> <span class="element-name">realization</span>()</div>
</section>
</li>
<li>
<section class="detail" id="refine()">
<h3>refine</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="StandardProfile.RefineStereotype.html" title="class in com.nomagic.uml2">StandardProfile.RefineStereotype</a></span> <span class="element-name">refine</span>()</div>
</section>
</li>
<li>
<section class="detail" id="responsibility()">
<h3>responsibility</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="StandardProfile.ResponsibilityStereotype.html" title="class in com.nomagic.uml2">StandardProfile.ResponsibilityStereotype</a></span> <span class="element-name">responsibility</span>()</div>
</section>
</li>
<li>
<section class="detail" id="script()">
<h3>script</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="StandardProfile.ScriptStereotype.html" title="class in com.nomagic.uml2">StandardProfile.ScriptStereotype</a></span> <span class="element-name">script</span>()</div>
</section>
</li>
<li>
<section class="detail" id="send()">
<h3>send</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="StandardProfile.SendStereotype.html" title="class in com.nomagic.uml2">StandardProfile.SendStereotype</a></span> <span class="element-name">send</span>()</div>
</section>
</li>
<li>
<section class="detail" id="service()">
<h3>service</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="StandardProfile.ServiceStereotype.html" title="class in com.nomagic.uml2">StandardProfile.ServiceStereotype</a></span> <span class="element-name">service</span>()</div>
</section>
</li>
<li>
<section class="detail" id="source()">
<h3>source</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="StandardProfile.SourceStereotype.html" title="class in com.nomagic.uml2">StandardProfile.SourceStereotype</a></span> <span class="element-name">source</span>()</div>
</section>
</li>
<li>
<section class="detail" id="specification()">
<h3>specification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="StandardProfile.SpecificationStereotype.html" title="class in com.nomagic.uml2">StandardProfile.SpecificationStereotype</a></span> <span class="element-name">specification</span>()</div>
</section>
</li>
<li>
<section class="detail" id="subsystem()">
<h3>subsystem</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="StandardProfile.SubsystemStereotype.html" title="class in com.nomagic.uml2">StandardProfile.SubsystemStereotype</a></span> <span class="element-name">subsystem</span>()</div>
</section>
</li>
<li>
<section class="detail" id="systemModel()">
<h3>systemModel</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="StandardProfile.SystemModelStereotype.html" title="class in com.nomagic.uml2">StandardProfile.SystemModelStereotype</a></span> <span class="element-name">systemModel</span>()</div>
</section>
</li>
<li>
<section class="detail" id="trace()">
<h3>trace</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="StandardProfile.TraceStereotype.html" title="class in com.nomagic.uml2">StandardProfile.TraceStereotype</a></span> <span class="element-name">trace</span>()</div>
</section>
</li>
<li>
<section class="detail" id="type()">
<h3>type</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="StandardProfile.TypeStereotype.html" title="class in com.nomagic.uml2">StandardProfile.TypeStereotype</a></span> <span class="element-name">type</span>()</div>
</section>
</li>
<li>
<section class="detail" id="utility()">
<h3>utility</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="StandardProfile.UtilityStereotype.html" title="class in com.nomagic.uml2">StandardProfile.UtilityStereotype</a></span> <span class="element-name">utility</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getAuxiliary()">
<h3>getAuxiliary</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getAuxiliary</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).auxiliary().getStereotype()</div>
</div>
<div class="block">A class that supports another more central or fundamental
 class, typically by implementing secondary logic or control
 flow. The class that the auxiliary supports may be defined
 explicitly using a Focus class or implicitly by a dependency
 relationship. Auxiliary classes are typically used together
 with Focus classes, and are particularly useful for specifying
 the secondary business logic or control flow of components
 during design. See also:   focus  .</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>stereotype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isAuxiliary(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isAuxiliary</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isAuxiliary</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use AuxiliaryStereotype.isInstance(element)</div>
</div>
</section>
</li>
<li>
<section class="detail" id="getBuildComponent()">
<h3>getBuildComponent</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getBuildComponent</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).buildComponent().getStereotype()</div>
</div>
<div class="block">A collection of elements defined for the purpose of system level development activities, such as compilation and versioning.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>stereotype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isBuildComponent(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isBuildComponent</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isBuildComponent</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use BuildComponentStereotype.isInstance(element)</div>
</div>
</section>
</li>
<li>
<section class="detail" id="getCall()">
<h3>getCall</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getCall</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).call().getStereotype()</div>
</div>
<div class="block">A usage dependency whose source is an operation and
 whose target is an operation. The relationship may also be
 subsumed to the class containing an operation, with the
 meaning that there exists an operation in the class to which
 the dependency applies.
 A call dependency specifies that the source operation or an
 operation in the source class invokes the target operation or
 an operation in the target class. A call dependency may
 connect a source operation to any target operation that is
 within scope including, but not limited to, operations of the
 enclosing classifier and operations of other visible
 classifiers.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>stereotype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isCall(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isCall</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isCall</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use CallStereotype.isInstance(element)</div>
</div>
</section>
</li>
<li>
<section class="detail" id="getCreate()">
<h3>getCreate</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getCreate</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).create().getStereotype()</div>
</div>
<div class="block">A usage dependency denoting that the client classifier
 creates instances of the supplier classifier.
 Specifies that the designated feature creates an instance of the classifier to which the feature is attached. May be promoted to the Classifier containing the feature.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>stereotype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isCreate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isCreate</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isCreate</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use CreateStereotype.isInstance(element)</div>
</div>
</section>
</li>
<li>
<section class="detail" id="getDerive()">
<h3>getDerive</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getDerive</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).derive().getStereotype()</div>
</div>
<div class="block">Specifies a derivation relationship among model elements
 that are usually, but not necessarily, of the same type. A
 derived dependency specifies that the client may be
 computed from the supplier. The mapping specifies the
 computation. The client may be implemented for design
 reasons, such as efficiency, even though it is logically
 redundant.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>stereotype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDerive(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isDerive</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isDerive</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DeriveStereotype.isInstance(element)</div>
</div>
</section>
</li>
<li>
<section class="detail" id="getDestroy()">
<h3>getDestroy</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getDestroy</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).destroy().getStereotype()</div>
</div>
<div class="block">Specifies that the designated feature destroys an instance of the classifier to which the feature is attached. May be promoted to the classifier containing the feature.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>stereotype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDestroy(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isDestroy</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isDestroy</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DestroyStereotype.isInstance(element)</div>
</div>
</section>
</li>
<li>
<section class="detail" id="getDocument()">
<h3>getDocument</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getDocument</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).document().getStereotype()</div>
</div>
<div class="block">A generic file that is not a   source   file or   executable  .
 Subclass of   file  .</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>stereotype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDocument(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isDocument</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isDocument</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DocumentStereotype.isInstance(element)</div>
</div>
</section>
</li>
<li>
<section class="detail" id="getEntity()">
<h3>getEntity</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getEntity</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).entity().getStereotype()</div>
</div>
<div class="block">A persistent information component representing a business
 concept.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>stereotype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isEntity(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isEntity</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isEntity</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use EntityStereotype.isInstance(element)</div>
</div>
</section>
</li>
<li>
<section class="detail" id="getExecutable()">
<h3>getExecutable</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getExecutable</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).executable().getStereotype()</div>
</div>
<div class="block">Denotes a program that may be run on a node.
 Denotes a program file that can be executed on a computer system.Subclass of <span class="invalid-tag">invalid input: '&lt;'</span><file>&gt;.</file></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>stereotype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isExecutable(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isExecutable</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isExecutable</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ExecutableStereotype.isInstance(element)</div>
</div>
</section>
</li>
<li>
<section class="detail" id="getFile()">
<h3>getFile</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getFile</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).file().getStereotype()</div>
</div>
<div class="block">A physical file in the context of the system developed.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>stereotype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isFile(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isFile</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isFile</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use FileStereotype.isInstance(element)</div>
</div>
</section>
</li>
<li>
<section class="detail" id="getFocus()">
<h3>getFocus</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getFocus</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).focus().getStereotype()</div>
</div>
<div class="block">A class that defines the core logic or control flow for one or
 more auxiliary classes that support it. Support classes may be
 defined explicitly using Auxiliary classes or implicitly by
 dependency relationships. Focus classes are typically used
 together with one or more Auxiliary classes, and are
 particularly useful for specifying the core business logic or
 control flow of components during design. See also:
 auxiliary  .</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>stereotype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isFocus(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isFocus</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isFocus</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use FocusStereotype.isInstance(element)</div>
</div>
</section>
</li>
<li>
<section class="detail" id="getFramework()">
<h3>getFramework</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getFramework</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).framework().getStereotype()</div>
</div>
<div class="block">A package that contains model elements which specify a
 reusable architecture for all or part of a
 system. Frameworks typically include classes, patterns or
 templates. When frameworks are specialized for an
 application domain, they are sometimes referred to as
 application frameworks.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>stereotype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isFramework(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isFramework</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isFramework</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use FrameworkStereotype.isInstance(element)</div>
</div>
</section>
</li>
<li>
<section class="detail" id="getImplement()">
<h3>getImplement</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getImplement</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).implement().getStereotype()</div>
</div>
<div class="block">A component definition that is not intended to have a
 specification itself. Rather, it is an implementation for a
 separate   specification   to which it has a Dependency.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>stereotype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isImplement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isImplement</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isImplement</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ImplementStereotype.isInstance(element)</div>
</div>
</section>
</li>
<li>
<section class="detail" id="getImplementationClass()">
<h3>getImplementationClass</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getImplementationClass</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).implementationClass().getStereotype()</div>
</div>
<div class="block">The implementation of a class in some programming
 language (e.g., C++, Smalltalk, Java) in which an instance
 may not have more than one class. This is in contrast to
 Class, for which an instance may have multiple classes at one
 time and may gain or lose classes over time, and an object (a
 child of instance) may dynamically
 have multiple classes.
 An Implementation class is said to realize a Classifier if it
 provides all of the operations defined for the Classifier with
 the same behavior as specified for the Classifier's operations.
 An Implementation Class may realize a number of different
 Types. Note that the physical attributes and associations of
 the Implementation class do not have to be the same as those
 of any Classifier it realizes and that the Implementation
 Class may provide methods for its operations in terms of its
 physical attributes and associations. See also:   type  .</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>stereotype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isImplementationClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isImplementationClass</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isImplementationClass</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ImplementationClassStereotype.isInstance(element)</div>
</div>
</section>
</li>
<li>
<section class="detail" id="getInstantiate()">
<h3>getInstantiate</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getInstantiate</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).instantiate().getStereotype()</div>
</div>
<div class="block">A usage dependency among classifiers indicating that
 operations on the client create instances of the supplier.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>stereotype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isInstantiate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isInstantiate</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isInstantiate</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use InstantiateStereotype.isInstance(element)</div>
</div>
</section>
</li>
<li>
<section class="detail" id="getLibrary()">
<h3>getLibrary</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getLibrary</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).library().getStereotype()</div>
</div>
<div class="block">Denotes a static or dynamic library.
 Denotes a static or dynamic library file. Subclass of <span class="invalid-tag">invalid input: '&lt;'</span><file>&gt;.</file></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>stereotype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isLibrary(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isLibrary</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isLibrary</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use LibraryStereotype.isInstance(element)</div>
</div>
</section>
</li>
<li>
<section class="detail" id="getMetaclass()">
<h3>getMetaclass</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getMetaclass</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).metaclass().getStereotype()</div>
</div>
</section>
</li>
<li>
<section class="detail" id="isMetaclass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isMetaclass</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isMetaclass</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use MetaclassStereotype.isInstance(element)</div>
</div>
</section>
</li>
<li>
<section class="detail" id="getMetamodel()">
<h3>getMetamodel</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getMetamodel</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).metamodel().getStereotype()</div>
</div>
<div class="block">A model of a model, that typically contains metaclasses.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>stereotype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isMetamodel(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isMetamodel</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isMetamodel</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use MetamodelStereotype.isInstance(element)</div>
</div>
</section>
</li>
<li>
<section class="detail" id="getModelLibrary()">
<h3>getModelLibrary</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getModelLibrary</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).modelLibrary().getStereotype()</div>
</div>
<div class="block">A package that contains model elements which are intended to
 be reused by other packages. Model libraries are frequently
 used in conjunction with applied profiles. This is expressed
 by defining a dependency between a profile and a model
 library package, or by defining a model library as contained
 in a profile package. The classes in a model library are not
 stereotypes and tagged definitions extending the metamodel.
 A model library is analogous to a class library in some
 programming languages.
 When a model library is defined as a part of a profile, it is
 imported or deleted with the application or removal of the
 profile. The profile is implicitly applied to its model library.
 In the other case, when the model library is defined as an
 external package imported by a profile, the profile requires
 that the model library be there in the model at the stage of the
 profile application. The application or the removal of the
 profile does not affect the presence of the model library
 elements.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>stereotype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isModelLibrary(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isModelLibrary</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isModelLibrary</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ModelLibraryStereotype.isInstance(element)</div>
</div>
</section>
</li>
<li>
<section class="detail" id="getProcess()">
<h3>getProcess</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getProcess</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).process().getStereotype()</div>
</div>
<div class="block">A transaction based component.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>stereotype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isProcess(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isProcess</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isProcess</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ProcessStereotype.isInstance(element)</div>
</div>
</section>
</li>
<li>
<section class="detail" id="getRealization()">
<h3>getRealization</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getRealization</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).realization().getStereotype()</div>
</div>
<div class="block">A classifier that specifies a domain of objects and that also
 defines the physical implementation of those objects. For
 example, a Component stereotyped by   realization   will
 only have realizing Classifiers that implement behavior
 specified by a separate   specification   Component. See
 specification  . This differs from   implementation class
 because an   implementation class   is a realization of a Class
 which can have features such as attributes and methods
 which is useful to system designers.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>stereotype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isRealization(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isRealization</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isRealization</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use RealizationStereotype.isInstance(element)</div>
</div>
</section>
</li>
<li>
<section class="detail" id="getRefine()">
<h3>getRefine</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getRefine</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).refine().getStereotype()</div>
</div>
<div class="block">Specifies a refinement relationship between model elements
 at different semantic levels, such as analysis and design. The
 mapping specifies the relationship between the two elements
 or sets of elements. The mapping may or may not be
 computable, and it may be unidirectional or bidirectional.
 Refinement can be used to model transformations from
 analysis to design and other such changes.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>stereotype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isRefine(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isRefine</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isRefine</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use RefineStereotype.isInstance(element)</div>
</div>
</section>
</li>
<li>
<section class="detail" id="getResponsibility()">
<h3>getResponsibility</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getResponsibility</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).responsibility().getStereotype()</div>
</div>
<div class="block">A contract or an obligation of an element in its relationship
 to other elements.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>stereotype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isResponsibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isResponsibility</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isResponsibility</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ResponsibilityStereotype.isInstance(element)</div>
</div>
</section>
</li>
<li>
<section class="detail" id="getScript()">
<h3>getScript</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getScript</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).script().getStereotype()</div>
</div>
<div class="block">A script file that can be interpreted by a computer system.
 Subclass of   file  .</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>stereotype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isScript(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isScript</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isScript</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ScriptStereotype.isInstance(element)</div>
</div>
</section>
</li>
<li>
<section class="detail" id="getSend()">
<h3>getSend</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getSend</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).send().getStereotype()</div>
</div>
<div class="block">A usage dependency whose source is an operation and
 whose target is a signal, specifying that the source sends the
 target signal.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>stereotype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSend(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isSend</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isSend</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use SendStereotype.isInstance(element)</div>
</div>
</section>
</li>
<li>
<section class="detail" id="getService()">
<h3>getService</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getService</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).service().getStereotype()</div>
</div>
<div class="block">A stateless, functional component (computes a value).</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>stereotype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isService(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isService</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isService</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ServiceStereotype.isInstance(element)</div>
</div>
</section>
</li>
<li>
<section class="detail" id="getSource()">
<h3>getSource</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getSource</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).source().getStereotype()</div>
</div>
<div class="block">Denotes a source file that can be compiled into an executable file.Subclass of <span class="invalid-tag">invalid input: '&lt;'</span><file>&gt;.</file></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>stereotype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSource(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isSource</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isSource</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use SourceStereotype.isInstance(element)</div>
</div>
</section>
</li>
<li>
<section class="detail" id="getSpecification()">
<h3>getSpecification</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getSpecification</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).specification().getStereotype()</div>
</div>
<div class="block">A classifier that specifies a domain of objects without
 defining the physical implementation of those objects. For
 example, a Component stereotyped by   specification   will
 only have provided and required interfaces, and is not
 intended to have any realizingClassifiers as part of its
 definition. This differs from   type   because a   type   can
 have features such as attributes and methods which is useful
 to analysts modeling systems. Also see:   realization</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>stereotype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isSpecification</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isSpecification</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use SpecificationStereotype.isInstance(element)</div>
</div>
</section>
</li>
<li>
<section class="detail" id="getSubsystem()">
<h3>getSubsystem</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getSubsystem</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).subsystem().getStereotype()</div>
</div>
<div class="block">A unit of hierarchical decomposition for large systems. A
 subsystem is commonly instantiated indirectly. Definitions
 of subsystems vary widely among domains and methods,
 and it is expected that domain and method profiles will
 specialize this construct. A subsystem may be defined to
 have specification and realization elements. See also:
 specification   and   realization  .</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>stereotype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSubsystem(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isSubsystem</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isSubsystem</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use SubsystemStereotype.isInstance(element)</div>
</div>
</section>
</li>
<li>
<section class="detail" id="getSystemModel()">
<h3>getSystemModel</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getSystemModel</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).systemModel().getStereotype()</div>
</div>
<div class="block">A systemModel is a stereotyped model that contains a
 collection of models of the same physical system. A
 systemModel also contains all relationships and
 constraints between model elements contained in
 different models.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>stereotype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSystemModel(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isSystemModel</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isSystemModel</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use SystemModelStereotype.isInstance(element)</div>
</div>
</section>
</li>
<li>
<section class="detail" id="getTrace()">
<h3>getTrace</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getTrace</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).trace().getStereotype()</div>
</div>
<div class="block">Specifies a trace relationship between model elements or sets
 of model elements that represent the same concept in
 different models. Traces are mainly used for tracking
 requirements and changes across models. Since model
 changes can occur in both directions, the directionality of the
 dependency can often be ignored. The mapping specifies the
 relationship between the two, but it is rarely computable and
 is usually informal.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>stereotype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isTrace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isTrace</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isTrace</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use TraceStereotype.isInstance(element)</div>
</div>
</section>
</li>
<li>
<section class="detail" id="getType()">
<h3>getType</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getType</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).type().getStereotype()</div>
</div>
<div class="block">A class that specifies a domain of objects together with the
 operations applicable to the objects, without defining the
 physical implementation of those objects. However, it may
 have attributes and associations. Behavioral specifications
 for type operations may be expressed using, for example,
 activity diagrams. An object may have at most one
 implementation class, however it may conform to multiple
 different types. See also:   implementationClass  .</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>stereotype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isType</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isType</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use TypeStereotype.isInstance(element)</div>
</div>
</section>
</li>
<li>
<section class="detail" id="getUtility()">
<h3>getUtility</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getUtility</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).utility().getStereotype()</div>
</div>
<div class="block">A class that has no instances, but rather denotes a named
 collection of non-member attributes and operations, all of
 which are class-scoped.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>stereotype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isUtility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isUtility</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isUtility</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use UtilityStereotype.isInstance(element)</div>
</div>
</section>
</li>
<li>
<section class="detail" id="generatedGetAllElementWrappers()">
<h3>generatedGetAllElementWrappers</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.nomagic.profiles.ProfileImplementation.ProfileElementWrapper&gt;</span> <span class="element-name">generatedGetAllElementWrappers</span>()</div>
</section>
</li>
<li>
<section class="detail" id="generatedGetAllStereotypes()">
<h3>generatedGetAllStereotypes</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt;</span> <span class="element-name">generatedGetAllStereotypes</span>()</div>
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
