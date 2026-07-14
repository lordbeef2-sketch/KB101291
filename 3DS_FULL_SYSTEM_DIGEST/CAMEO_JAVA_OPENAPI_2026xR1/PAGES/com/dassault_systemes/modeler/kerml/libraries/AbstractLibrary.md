# JAVA OPENAPI: AbstractLibrary (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/libraries/AbstractLibrary.html
- source_path: `com/dassault_systemes/modeler/kerml/libraries/AbstractLibrary.html`
- source_sha256: `02ecd61aea0ce57368a1d117d2b10ef5ba8b00f300c49c1e06b8e4de25bfbfc5`
- captured_utc: `2026-07-14T16:44:44.829801+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.libraries](package-summary.html)

## Class AbstractLibrary

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService<[ModelElementProject](../../foundation/project/ModelElementProject.html)>
com.dassault_systemes.modeler.kerml.libraries.AbstractLibrary

All Implemented Interfaces:
`com.dassault_systemes.modeler.foundation.project.service.DisposableService`

Direct Known Subclasses:
`[ActionsLibrary](../../sysml/libraries/standard/ActionsLibrary.html)`, `[AllocationsLibrary](../../sysml/libraries/standard/AllocationsLibrary.html)`, `[AnalysisCasesLibrary](../../sysml/libraries/standard/AnalysisCasesLibrary.html)`, `[AnalysisToolingLibrary](../../sysml/libraries/standard/AnalysisToolingLibrary.html)`, `[AttributesLibrary](../../sysml/libraries/standard/AttributesLibrary.html)`, `[BaseFunctionsLibrary](standard/BaseFunctionsLibrary.html)`, `[BaseLibrary](standard/BaseLibrary.html)`, `[BooleanFunctionsLibrary](standard/BooleanFunctionsLibrary.html)`, `[CalculationsLibrary](../../sysml/libraries/standard/CalculationsLibrary.html)`, `[CasesLibrary](../../sysml/libraries/standard/CasesLibrary.html)`, `[CausationConnectionsLibrary](../../sysml/libraries/standard/CausationConnectionsLibrary.html)`, `[CauseAndEffectLibrary](../../sysml/libraries/standard/CauseAndEffectLibrary.html)`, `[ClocksLibrary](standard/ClocksLibrary.html)`, `[CollectionFunctionsLibrary](standard/CollectionFunctionsLibrary.html)`, `[CollectionsLibrary](standard/CollectionsLibrary.html)`, `[ComplexFunctionsLibrary](standard/ComplexFunctionsLibrary.html)`, `[ConnectionsLibrary](../../sysml/libraries/standard/ConnectionsLibrary.html)`, `[ConstraintsLibrary](../../sysml/libraries/standard/ConstraintsLibrary.html)`, `[ControlFunctionsLibrary](standard/ControlFunctionsLibrary.html)`, `[ControlPerformancesLibrary](standard/ControlPerformancesLibrary.html)`, `[DataFunctionsLibrary](standard/DataFunctionsLibrary.html)`, `[DerivationConnectionsLibrary](../../sysml/libraries/standard/DerivationConnectionsLibrary.html)`, `[FeatureReferencingPerformancesLibrary](standard/FeatureReferencingPerformancesLibrary.html)`, `[FlowsLibrary](../../sysml/libraries/standard/FlowsLibrary.html)`, `[ImageMetadataLibrary](../../sysml/libraries/standard/ImageMetadataLibrary.html)`, `[IntegerFunctionsLibrary](standard/IntegerFunctionsLibrary.html)`, `[InterfacesLibrary](../../sysml/libraries/standard/InterfacesLibrary.html)`, `[ISQAcousticsLibrary](../../sysml/libraries/standard/ISQAcousticsLibrary.html)`, `[ISQAtomicNuclearLibrary](../../sysml/libraries/standard/ISQAtomicNuclearLibrary.html)`, `[ISQBaseLibrary](../../sysml/libraries/standard/ISQBaseLibrary.html)`, `[ISQCharacteristicNumbersLibrary](../../sysml/libraries/standard/ISQCharacteristicNumbersLibrary.html)`, `[ISQChemistryMolecularLibrary](../../sysml/libraries/standard/ISQChemistryMolecularLibrary.html)`, `[ISQCondensedMatterLibrary](../../sysml/libraries/standard/ISQCondensedMatterLibrary.html)`, `[ISQElectromagnetismLibrary](../../sysml/libraries/standard/ISQElectromagnetismLibrary.html)`, `[ISQInformationLibrary](../../sysml/libraries/standard/ISQInformationLibrary.html)`, `[ISQLibrary](../../sysml/libraries/standard/ISQLibrary.html)`, `[ISQLightLibrary](../../sysml/libraries/standard/ISQLightLibrary.html)`, `[ISQMechanicsLibrary](../../sysml/libraries/standard/ISQMechanicsLibrary.html)`, `[ISQSpaceTimeLibrary](../../sysml/libraries/standard/ISQSpaceTimeLibrary.html)`, `[ISQThermodynamicsLibrary](../../sysml/libraries/standard/ISQThermodynamicsLibrary.html)`, `[ItemsLibrary](../../sysml/libraries/standard/ItemsLibrary.html)`, `[KerMLLibrary](standard/KerMLLibrary.html)`, `[LinksLibrary](standard/LinksLibrary.html)`, `[MeasurementRefCalculationsLibrary](../../sysml/libraries/standard/MeasurementRefCalculationsLibrary.html)`, `[MeasurementReferencesLibrary](../../sysml/libraries/standard/MeasurementReferencesLibrary.html)`, `[MetadataLibrary](../../sysml/libraries/standard/MetadataLibrary.html)`, `[MetaobjectsLibrary](standard/MetaobjectsLibrary.html)`, `[ModelingMetadataLibrary](../../sysml/libraries/standard/ModelingMetadataLibrary.html)`, `[NaturalFunctionsLibrary](standard/NaturalFunctionsLibrary.html)`, `[NumericalFunctionsLibrary](standard/NumericalFunctionsLibrary.html)`, `[ObjectsLibrary](standard/ObjectsLibrary.html)`, `[ObservationLibrary](standard/ObservationLibrary.html)`, `[OccurrenceFunctionsLibrary](standard/OccurrenceFunctionsLibrary.html)`, `[OccurrencesLibrary](standard/OccurrencesLibrary.html)`, `[ParametersOfInterestMetadataLibrary](../../sysml/libraries/standard/ParametersOfInterestMetadataLibrary.html)`, `[PartsLibrary](../../sysml/libraries/standard/PartsLibrary.html)`, `[PerformancesLibrary](standard/PerformancesLibrary.html)`, `[PortsLibrary](../../sysml/libraries/standard/PortsLibrary.html)`, `[QuantitiesLibrary](../../sysml/libraries/standard/QuantitiesLibrary.html)`, `[QuantityCalculationsLibrary](../../sysml/libraries/standard/QuantityCalculationsLibrary.html)`, `[RationalFunctionsLibrary](standard/RationalFunctionsLibrary.html)`, `[RealFunctionsLibrary](standard/RealFunctionsLibrary.html)`, `[RequirementDerivationLibrary](../../sysml/libraries/standard/RequirementDerivationLibrary.html)`, `[RequirementsLibrary](../../sysml/libraries/standard/RequirementsLibrary.html)`, `[RiskMetadataLibrary](../../sysml/libraries/standard/RiskMetadataLibrary.html)`, `[SampledFunctionsLibrary](../../sysml/libraries/standard/SampledFunctionsLibrary.html)`, `[ScalarFunctionsLibrary](standard/ScalarFunctionsLibrary.html)`, `[ScalarValuesLibrary](standard/ScalarValuesLibrary.html)`, `[SequenceFunctionsLibrary](standard/SequenceFunctionsLibrary.html)`, `[ShapeItemsLibrary](../../sysml/libraries/standard/ShapeItemsLibrary.html)`, `[SILibrary](../../sysml/libraries/standard/SILibrary.html)`, `[SIPrefixesLibrary](../../sysml/libraries/standard/SIPrefixesLibrary.html)`, `[SpatialFramesLibrary](standard/SpatialFramesLibrary.html)`, `[SpatialItemsLibrary](../../sysml/libraries/standard/SpatialItemsLibrary.html)`, `[StandardViewDefinitionsLibrary](../../sysml/libraries/standard/StandardViewDefinitionsLibrary.html)`, `[StatePerformancesLibrary](standard/StatePerformancesLibrary.html)`, `[StatesLibrary](../../sysml/libraries/standard/StatesLibrary.html)`, `[StateSpaceRepresentationLibrary](../../sysml/libraries/standard/StateSpaceRepresentationLibrary.html)`, `[StringFunctionsLibrary](standard/StringFunctionsLibrary.html)`, `[SysMLLibrary](../../sysml/libraries/standard/SysMLLibrary.html)`, `[TensorCalculationsLibrary](../../sysml/libraries/standard/TensorCalculationsLibrary.html)`, `[TimeLibrary](../../sysml/libraries/standard/TimeLibrary.html)`, `[TradeStudiesLibrary](../../sysml/libraries/standard/TradeStudiesLibrary.html)`, `[TransfersLibrary](standard/TransfersLibrary.html)`, `[TransitionPerformancesLibrary](standard/TransitionPerformancesLibrary.html)`, `[TrigFunctionsLibrary](standard/TrigFunctionsLibrary.html)`, `[TriggersLibrary](standard/TriggersLibrary.html)`, `[USCustomaryUnitsLibrary](../../sysml/libraries/standard/USCustomaryUnitsLibrary.html)`, `[UseCasesLibrary](../../sysml/libraries/standard/UseCasesLibrary.html)`, `[VectorCalculationsLibrary](../../sysml/libraries/standard/VectorCalculationsLibrary.html)`, `[VectorFunctionsLibrary](standard/VectorFunctionsLibrary.html)`, `[VectorValuesLibrary](standard/VectorValuesLibrary.html)`, `[VerificationCasesLibrary](../../sysml/libraries/standard/VerificationCasesLibrary.html)`, `[ViewsLibrary](../../sysml/libraries/standard/ViewsLibrary.html)`

@OpenApiAllpublic abstract classAbstractLibrary
extends com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService<[ModelElementProject](../../foundation/project/ModelElementProject.html)>

Base class for all kinds of libraries implementation.
 Those implementations provide an API for accessing elements inside the libraries.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Modifier
Constructor
Description
`protected`
`[AbstractLibrary](#%3Cinit%3E(com.dassault_systemes.modeler.foundation.project.ModelElementProject))([ModelElementProject](../../foundation/project/ModelElementProject.html) project)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsConcrete Methods
Modifier and Type
Method
Description
`[Function](../model/kerml/Function.html)`
`[findFunctionInLibrary](#findFunctionInLibrary(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) functionName)`

`protected [LibraryPackage](../model/kerml/LibraryPackage.html)`
`[findLibraryPackage](#findLibraryPackage(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) packageName)`

`protected [Package](../model/kerml/Package.html)`
`[findPackage](#findPackage(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) libraryPackageName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) packageName)`

`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[LibraryPackage](../model/kerml/LibraryPackage.html)>`
`[getLibraryPackages](#getLibraryPackages())()`

`final [Namespace](../model/kerml/Namespace.html)`
`[getNamespace](#getNamespace())()`

`protected abstract [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<com.dassault_systemes.modeler.kerml.libraries.TypeWrapper>`
`[getTypeWrappers](#getTypeWrappers())()`

`protected final void`
`[initialized](#initialized())()`

`abstract boolean`
`[isSemantic](#isSemantic())()`

`protected abstract [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[packagesNames](#packagesNames())()`
Methods inherited from class com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService
`disposeService, getIfPresent, getOrCreateInstance, getOrCreateInstanceWithNullSupport, getReferencedProject`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
AbstractLibrary
protected AbstractLibrary([ModelElementProject](../../foundation/project/ModelElementProject.html) project)
 ============ METHOD DETAIL ========== 
Method Details
initialized
protected final void initialized()
isSemantic
public abstract boolean isSemantic()
getLibraryPackages
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[LibraryPackage](../model/kerml/LibraryPackage.html)> getLibraryPackages()
findFunctionInLibrary
@CheckForNullpublic [Function](../model/kerml/Function.html) findFunctionInLibrary([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) functionName)
getNamespace
@CheckForNullpublic final [Namespace](../model/kerml/Namespace.html) getNamespace()
findLibraryPackage
@CheckForNullprotected [LibraryPackage](../model/kerml/LibraryPackage.html) findLibraryPackage([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) packageName)
findPackage
@CheckForNullprotected [Package](../model/kerml/Package.html) findPackage([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) libraryPackageName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) packageName)
packagesNames
protected abstract [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> packagesNames()
getTypeWrappers
protected abstract [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<com.dassault_systemes.modeler.kerml.libraries.TypeWrapper> getTypeWrappers()

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.libraries</a></div>
<h1 class="title" title="Class AbstractLibrary">Class AbstractLibrary</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService&lt;<a href="../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a>&gt;
<div class="inheritance">com.dassault_systemes.modeler.kerml.libraries.AbstractLibrary</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.dassault_systemes.modeler.foundation.project.service.DisposableService</code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="../../sysml/libraries/standard/ActionsLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ActionsLibrary</a></code>, <code><a href="../../sysml/libraries/standard/AllocationsLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">AllocationsLibrary</a></code>, <code><a href="../../sysml/libraries/standard/AnalysisCasesLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">AnalysisCasesLibrary</a></code>, <code><a href="../../sysml/libraries/standard/AnalysisToolingLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">AnalysisToolingLibrary</a></code>, <code><a href="../../sysml/libraries/standard/AttributesLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">AttributesLibrary</a></code>, <code><a href="standard/BaseFunctionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">BaseFunctionsLibrary</a></code>, <code><a href="standard/BaseLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">BaseLibrary</a></code>, <code><a href="standard/BooleanFunctionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">BooleanFunctionsLibrary</a></code>, <code><a href="../../sysml/libraries/standard/CalculationsLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">CalculationsLibrary</a></code>, <code><a href="../../sysml/libraries/standard/CasesLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">CasesLibrary</a></code>, <code><a href="../../sysml/libraries/standard/CausationConnectionsLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">CausationConnectionsLibrary</a></code>, <code><a href="../../sysml/libraries/standard/CauseAndEffectLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">CauseAndEffectLibrary</a></code>, <code><a href="standard/ClocksLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ClocksLibrary</a></code>, <code><a href="standard/CollectionFunctionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">CollectionFunctionsLibrary</a></code>, <code><a href="standard/CollectionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">CollectionsLibrary</a></code>, <code><a href="standard/ComplexFunctionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ComplexFunctionsLibrary</a></code>, <code><a href="../../sysml/libraries/standard/ConnectionsLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ConnectionsLibrary</a></code>, <code><a href="../../sysml/libraries/standard/ConstraintsLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ConstraintsLibrary</a></code>, <code><a href="standard/ControlFunctionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ControlFunctionsLibrary</a></code>, <code><a href="standard/ControlPerformancesLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ControlPerformancesLibrary</a></code>, <code><a href="standard/DataFunctionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">DataFunctionsLibrary</a></code>, <code><a href="../../sysml/libraries/standard/DerivationConnectionsLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">DerivationConnectionsLibrary</a></code>, <code><a href="standard/FeatureReferencingPerformancesLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">FeatureReferencingPerformancesLibrary</a></code>, <code><a href="../../sysml/libraries/standard/FlowsLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">FlowsLibrary</a></code>, <code><a href="../../sysml/libraries/standard/ImageMetadataLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ImageMetadataLibrary</a></code>, <code><a href="standard/IntegerFunctionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">IntegerFunctionsLibrary</a></code>, <code><a href="../../sysml/libraries/standard/InterfacesLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">InterfacesLibrary</a></code>, <code><a href="../../sysml/libraries/standard/ISQAcousticsLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ISQAcousticsLibrary</a></code>, <code><a href="../../sysml/libraries/standard/ISQAtomicNuclearLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ISQAtomicNuclearLibrary</a></code>, <code><a href="../../sysml/libraries/standard/ISQBaseLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ISQBaseLibrary</a></code>, <code><a href="../../sysml/libraries/standard/ISQCharacteristicNumbersLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ISQCharacteristicNumbersLibrary</a></code>, <code><a href="../../sysml/libraries/standard/ISQChemistryMolecularLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ISQChemistryMolecularLibrary</a></code>, <code><a href="../../sysml/libraries/standard/ISQCondensedMatterLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ISQCondensedMatterLibrary</a></code>, <code><a href="../../sysml/libraries/standard/ISQElectromagnetismLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ISQElectromagnetismLibrary</a></code>, <code><a href="../../sysml/libraries/standard/ISQInformationLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ISQInformationLibrary</a></code>, <code><a href="../../sysml/libraries/standard/ISQLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ISQLibrary</a></code>, <code><a href="../../sysml/libraries/standard/ISQLightLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ISQLightLibrary</a></code>, <code><a href="../../sysml/libraries/standard/ISQMechanicsLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ISQMechanicsLibrary</a></code>, <code><a href="../../sysml/libraries/standard/ISQSpaceTimeLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ISQSpaceTimeLibrary</a></code>, <code><a href="../../sysml/libraries/standard/ISQThermodynamicsLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ISQThermodynamicsLibrary</a></code>, <code><a href="../../sysml/libraries/standard/ItemsLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ItemsLibrary</a></code>, <code><a href="standard/KerMLLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary</a></code>, <code><a href="standard/LinksLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">LinksLibrary</a></code>, <code><a href="../../sysml/libraries/standard/MeasurementRefCalculationsLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">MeasurementRefCalculationsLibrary</a></code>, <code><a href="../../sysml/libraries/standard/MeasurementReferencesLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">MeasurementReferencesLibrary</a></code>, <code><a href="../../sysml/libraries/standard/MetadataLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">MetadataLibrary</a></code>, <code><a href="standard/MetaobjectsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">MetaobjectsLibrary</a></code>, <code><a href="../../sysml/libraries/standard/ModelingMetadataLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ModelingMetadataLibrary</a></code>, <code><a href="standard/NaturalFunctionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">NaturalFunctionsLibrary</a></code>, <code><a href="standard/NumericalFunctionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">NumericalFunctionsLibrary</a></code>, <code><a href="standard/ObjectsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ObjectsLibrary</a></code>, <code><a href="standard/ObservationLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ObservationLibrary</a></code>, <code><a href="standard/OccurrenceFunctionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">OccurrenceFunctionsLibrary</a></code>, <code><a href="standard/OccurrencesLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">OccurrencesLibrary</a></code>, <code><a href="../../sysml/libraries/standard/ParametersOfInterestMetadataLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ParametersOfInterestMetadataLibrary</a></code>, <code><a href="../../sysml/libraries/standard/PartsLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">PartsLibrary</a></code>, <code><a href="standard/PerformancesLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">PerformancesLibrary</a></code>, <code><a href="../../sysml/libraries/standard/PortsLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">PortsLibrary</a></code>, <code><a href="../../sysml/libraries/standard/QuantitiesLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">QuantitiesLibrary</a></code>, <code><a href="../../sysml/libraries/standard/QuantityCalculationsLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">QuantityCalculationsLibrary</a></code>, <code><a href="standard/RationalFunctionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">RationalFunctionsLibrary</a></code>, <code><a href="standard/RealFunctionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">RealFunctionsLibrary</a></code>, <code><a href="../../sysml/libraries/standard/RequirementDerivationLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">RequirementDerivationLibrary</a></code>, <code><a href="../../sysml/libraries/standard/RequirementsLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">RequirementsLibrary</a></code>, <code><a href="../../sysml/libraries/standard/RiskMetadataLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">RiskMetadataLibrary</a></code>, <code><a href="../../sysml/libraries/standard/SampledFunctionsLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SampledFunctionsLibrary</a></code>, <code><a href="standard/ScalarFunctionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ScalarFunctionsLibrary</a></code>, <code><a href="standard/ScalarValuesLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ScalarValuesLibrary</a></code>, <code><a href="standard/SequenceFunctionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">SequenceFunctionsLibrary</a></code>, <code><a href="../../sysml/libraries/standard/ShapeItemsLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ShapeItemsLibrary</a></code>, <code><a href="../../sysml/libraries/standard/SILibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SILibrary</a></code>, <code><a href="../../sysml/libraries/standard/SIPrefixesLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SIPrefixesLibrary</a></code>, <code><a href="standard/SpatialFramesLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">SpatialFramesLibrary</a></code>, <code><a href="../../sysml/libraries/standard/SpatialItemsLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SpatialItemsLibrary</a></code>, <code><a href="../../sysml/libraries/standard/StandardViewDefinitionsLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">StandardViewDefinitionsLibrary</a></code>, <code><a href="standard/StatePerformancesLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">StatePerformancesLibrary</a></code>, <code><a href="../../sysml/libraries/standard/StatesLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">StatesLibrary</a></code>, <code><a href="../../sysml/libraries/standard/StateSpaceRepresentationLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">StateSpaceRepresentationLibrary</a></code>, <code><a href="standard/StringFunctionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">StringFunctionsLibrary</a></code>, <code><a href="../../sysml/libraries/standard/SysMLLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary</a></code>, <code><a href="../../sysml/libraries/standard/TensorCalculationsLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">TensorCalculationsLibrary</a></code>, <code><a href="../../sysml/libraries/standard/TimeLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">TimeLibrary</a></code>, <code><a href="../../sysml/libraries/standard/TradeStudiesLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">TradeStudiesLibrary</a></code>, <code><a href="standard/TransfersLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">TransfersLibrary</a></code>, <code><a href="standard/TransitionPerformancesLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">TransitionPerformancesLibrary</a></code>, <code><a href="standard/TrigFunctionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">TrigFunctionsLibrary</a></code>, <code><a href="standard/TriggersLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">TriggersLibrary</a></code>, <code><a href="../../sysml/libraries/standard/USCustomaryUnitsLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">USCustomaryUnitsLibrary</a></code>, <code><a href="../../sysml/libraries/standard/UseCasesLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">UseCasesLibrary</a></code>, <code><a href="../../sysml/libraries/standard/VectorCalculationsLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">VectorCalculationsLibrary</a></code>, <code><a href="standard/VectorFunctionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">VectorFunctionsLibrary</a></code>, <code><a href="standard/VectorValuesLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">VectorValuesLibrary</a></code>, <code><a href="../../sysml/libraries/standard/VerificationCasesLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">VerificationCasesLibrary</a></code>, <code><a href="../../sysml/libraries/standard/ViewsLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ViewsLibrary</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">AbstractLibrary</span>
<span class="extends-implements">extends com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService&lt;<a href="../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a>&gt;</span></div>
<div class="block">Base class for all kinds of libraries implementation.
 Those implementations provide an API for accessing elements inside the libraries.</div>
</section>
<section class="summary">
<ul class="summary-list">
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.dassault_systemes.modeler.foundation.project.ModelElementProject)">AbstractLibrary</a><wbr/>(<a href="../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project)</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../model/kerml/Function.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Function</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#findFunctionInLibrary(java.lang.String)">findFunctionInLibrary</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> functionName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a href="../model/kerml/LibraryPackage.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LibraryPackage</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#findLibraryPackage(java.lang.String)">findLibraryPackage</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> packageName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a href="../model/kerml/Package.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Package</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#findPackage(java.lang.String,java.lang.String)">findPackage</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> libraryPackageName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> packageName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="../model/kerml/LibraryPackage.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LibraryPackage</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLibraryPackages()">getLibraryPackages</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a href="../model/kerml/Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNamespace()">getNamespace</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>protected abstract <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a><wbr/>&lt;com.dassault_systemes.modeler.kerml.libraries.TypeWrapper&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getTypeWrappers()">getTypeWrappers</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#initialized()">initialized</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isSemantic()">isSemantic</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>protected abstract <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#packagesNames()">packagesNames</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService">Methods inherited from class com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService</h3>
<code>disposeService, getIfPresent, getOrCreateInstance, getOrCreateInstanceWithNullSupport, getReferencedProject</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(com.dassault_systemes.modeler.foundation.project.ModelElementProject)">
<h3>AbstractLibrary</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="element-name">AbstractLibrary</span><wbr/><span class="parameters">(<a href="../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project)</span></div>
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
<section class="detail" id="initialized()">
<h3>initialized</h3>
<div class="member-signature"><span class="modifiers">protected final</span> <span class="return-type">void</span> <span class="element-name">initialized</span>()</div>
</section>
</li>
<li>
<section class="detail" id="isSemantic()">
<h3>isSemantic</h3>
<div class="member-signature"><span class="modifiers">public abstract</span> <span class="return-type">boolean</span> <span class="element-name">isSemantic</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getLibraryPackages()">
<h3>getLibraryPackages</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../model/kerml/LibraryPackage.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LibraryPackage</a>&gt;</span> <span class="element-name">getLibraryPackages</span>()</div>
</section>
</li>
<li>
<section class="detail" id="findFunctionInLibrary(java.lang.String)">
<h3>findFunctionInLibrary</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../model/kerml/Function.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Function</a></span> <span class="element-name">findFunctionInLibrary</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> functionName)</span></div>
</section>
</li>
<li>
<section class="detail" id="getNamespace()">
<h3>getNamespace</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public final</span> <span class="return-type"><a href="../model/kerml/Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a></span> <span class="element-name">getNamespace</span>()</div>
</section>
</li>
<li>
<section class="detail" id="findLibraryPackage(java.lang.String)">
<h3>findLibraryPackage</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">protected</span> <span class="return-type"><a href="../model/kerml/LibraryPackage.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LibraryPackage</a></span> <span class="element-name">findLibraryPackage</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> packageName)</span></div>
</section>
</li>
<li>
<section class="detail" id="findPackage(java.lang.String,java.lang.String)">
<h3>findPackage</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">protected</span> <span class="return-type"><a href="../model/kerml/Package.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Package</a></span> <span class="element-name">findPackage</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> libraryPackageName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> packageName)</span></div>
</section>
</li>
<li>
<section class="detail" id="packagesNames()">
<h3>packagesNames</h3>
<div class="member-signature"><span class="modifiers">protected abstract</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">packagesNames</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getTypeWrappers()">
<h3>getTypeWrappers</h3>
<div class="member-signature"><span class="modifiers">protected abstract</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;com.dassault_systemes.modeler.kerml.libraries.TypeWrapper&gt;</span> <span class="element-name">getTypeWrappers</span>()</div>
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
