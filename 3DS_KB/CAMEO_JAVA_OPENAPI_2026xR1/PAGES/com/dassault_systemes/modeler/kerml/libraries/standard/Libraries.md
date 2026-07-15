# JAVA OPENAPI: Libraries (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/libraries/standard/Libraries.html
- source_path: `com/dassault_systemes/modeler/kerml/libraries/standard/Libraries.html`
- source_sha256: `641c6beb99bd8579e77186c100b65cbe4953c8b698e82ea6ef264440d5a55fe4`
- captured_utc: `2026-07-14T16:44:46.014817+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.libraries.standard](package-summary.html)

## Class Libraries

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService<[ModelElementProject](../../../foundation/project/ModelElementProject.html)>
com.dassault_systemes.modeler.kerml.libraries.standard.Libraries

All Implemented Interfaces:
`com.dassault_systemes.modeler.foundation.project.service.DisposableService`

Direct Known Subclasses:
`[Libraries](../../../sysml/libraries/standard/Libraries.html)`

@OpenApiAllpublic classLibraries
extends com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService<[ModelElementProject](../../../foundation/project/ModelElementProject.html)>

A holder of all KerML standard libraries.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Libraries](#%3Cinit%3E(com.dassault_systemes.modeler.foundation.project.ModelElementProject))([ModelElementProject](../../../foundation/project/ModelElementProject.html) project)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[BaseLibrary](BaseLibrary.html)`
`[Base](#Base())()`

`[BaseFunctionsLibrary](BaseFunctionsLibrary.html)`
`[BaseFunctions](#BaseFunctions())()`

`[BooleanFunctionsLibrary](BooleanFunctionsLibrary.html)`
`[BooleanFunctions](#BooleanFunctions())()`

`[ClocksLibrary](ClocksLibrary.html)`
`[Clocks](#Clocks())()`

`[CollectionFunctionsLibrary](CollectionFunctionsLibrary.html)`
`[CollectionFunctions](#CollectionFunctions())()`

`[CollectionsLibrary](CollectionsLibrary.html)`
`[Collections](#Collections())()`

`[ComplexFunctionsLibrary](ComplexFunctionsLibrary.html)`
`[ComplexFunctions](#ComplexFunctions())()`

`[ControlFunctionsLibrary](ControlFunctionsLibrary.html)`
`[ControlFunctions](#ControlFunctions())()`

`[ControlPerformancesLibrary](ControlPerformancesLibrary.html)`
`[ControlPerformances](#ControlPerformances())()`

`[DataFunctionsLibrary](DataFunctionsLibrary.html)`
`[DataFunctions](#DataFunctions())()`

`[FeatureReferencingPerformancesLibrary](FeatureReferencingPerformancesLibrary.html)`
`[FeatureReferencingPerformances](#FeatureReferencingPerformances())()`

`static [Libraries](Libraries.html)`
`[getInstance](#getInstance(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../../../../../nomagic/magicdraw/uml/BaseElement.html) element)`

`static [Libraries](Libraries.html)`
`[getInstanceByProject](#getInstanceByProject(com.dassault_systemes.modeler.foundation.project.ModelElementProject))([ModelElementProject](../../../foundation/project/ModelElementProject.html) project)`

`[IntegerFunctionsLibrary](IntegerFunctionsLibrary.html)`
`[IntegerFunctions](#IntegerFunctions())()`

`[KerMLLibrary](KerMLLibrary.html)`
`[KerML](#KerML())()`

`[LinksLibrary](LinksLibrary.html)`
`[Links](#Links())()`

`[MetaobjectsLibrary](MetaobjectsLibrary.html)`
`[Metaobjects](#Metaobjects())()`

`[NaturalFunctionsLibrary](NaturalFunctionsLibrary.html)`
`[NaturalFunctions](#NaturalFunctions())()`

`[NumericalFunctionsLibrary](NumericalFunctionsLibrary.html)`
`[NumericalFunctions](#NumericalFunctions())()`

`[ObjectsLibrary](ObjectsLibrary.html)`
`[Objects](#Objects())()`

`[ObservationLibrary](ObservationLibrary.html)`
`[Observation](#Observation())()`

`[OccurrenceFunctionsLibrary](OccurrenceFunctionsLibrary.html)`
`[OccurrenceFunctions](#OccurrenceFunctions())()`

`[OccurrencesLibrary](OccurrencesLibrary.html)`
`[Occurrences](#Occurrences())()`

`[PerformancesLibrary](PerformancesLibrary.html)`
`[Performances](#Performances())()`

`[RationalFunctionsLibrary](RationalFunctionsLibrary.html)`
`[RationalFunctions](#RationalFunctions())()`

`[RealFunctionsLibrary](RealFunctionsLibrary.html)`
`[RealFunctions](#RealFunctions())()`

`[ScalarFunctionsLibrary](ScalarFunctionsLibrary.html)`
`[ScalarFunctions](#ScalarFunctions())()`

`[ScalarValuesLibrary](ScalarValuesLibrary.html)`
`[ScalarValues](#ScalarValues())()`

`[SequenceFunctionsLibrary](SequenceFunctionsLibrary.html)`
`[SequenceFunctions](#SequenceFunctions())()`

`[SpatialFramesLibrary](SpatialFramesLibrary.html)`
`[SpatialFrames](#SpatialFrames())()`

`[StatePerformancesLibrary](StatePerformancesLibrary.html)`
`[StatePerformances](#StatePerformances())()`

`[StringFunctionsLibrary](StringFunctionsLibrary.html)`
`[StringFunctions](#StringFunctions())()`

`[TransfersLibrary](TransfersLibrary.html)`
`[Transfers](#Transfers())()`

`[TransitionPerformancesLibrary](TransitionPerformancesLibrary.html)`
`[TransitionPerformances](#TransitionPerformances())()`

`[TrigFunctionsLibrary](TrigFunctionsLibrary.html)`
`[TrigFunctions](#TrigFunctions())()`

`[TriggersLibrary](TriggersLibrary.html)`
`[Triggers](#Triggers())()`

`[VectorFunctionsLibrary](VectorFunctionsLibrary.html)`
`[VectorFunctions](#VectorFunctions())()`

`[VectorValuesLibrary](VectorValuesLibrary.html)`
`[VectorValues](#VectorValues())()`
Methods inherited from class com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService
`disposeService, getIfPresent, getOrCreateInstance, getOrCreateInstanceWithNullSupport, getReferencedProject`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Libraries
public Libraries([ModelElementProject](../../../foundation/project/ModelElementProject.html) project)
 ============ METHOD DETAIL ========== 
Method Details
getInstanceByProject
public static [Libraries](Libraries.html) getInstanceByProject([ModelElementProject](../../../foundation/project/ModelElementProject.html) project)
getInstance
public static [Libraries](Libraries.html) getInstance([BaseElement](../../../../../nomagic/magicdraw/uml/BaseElement.html) element)
BaseFunctions
public [BaseFunctionsLibrary](BaseFunctionsLibrary.html) BaseFunctions()
Base
public [BaseLibrary](BaseLibrary.html) Base()
BooleanFunctions
public [BooleanFunctionsLibrary](BooleanFunctionsLibrary.html) BooleanFunctions()
Clocks
public [ClocksLibrary](ClocksLibrary.html) Clocks()
CollectionFunctions
public [CollectionFunctionsLibrary](CollectionFunctionsLibrary.html) CollectionFunctions()
Collections
public [CollectionsLibrary](CollectionsLibrary.html) Collections()
ComplexFunctions
public [ComplexFunctionsLibrary](ComplexFunctionsLibrary.html) ComplexFunctions()
ControlFunctions
public [ControlFunctionsLibrary](ControlFunctionsLibrary.html) ControlFunctions()
ControlPerformances
public [ControlPerformancesLibrary](ControlPerformancesLibrary.html) ControlPerformances()
DataFunctions
public [DataFunctionsLibrary](DataFunctionsLibrary.html) DataFunctions()
FeatureReferencingPerformances
public [FeatureReferencingPerformancesLibrary](FeatureReferencingPerformancesLibrary.html) FeatureReferencingPerformances()
IntegerFunctions
public [IntegerFunctionsLibrary](IntegerFunctionsLibrary.html) IntegerFunctions()
KerML
public [KerMLLibrary](KerMLLibrary.html) KerML()
Links
public [LinksLibrary](LinksLibrary.html) Links()
Metaobjects
public [MetaobjectsLibrary](MetaobjectsLibrary.html) Metaobjects()
NaturalFunctions
public [NaturalFunctionsLibrary](NaturalFunctionsLibrary.html) NaturalFunctions()
NumericalFunctions
public [NumericalFunctionsLibrary](NumericalFunctionsLibrary.html) NumericalFunctions()
Objects
public [ObjectsLibrary](ObjectsLibrary.html) Objects()
Observation
public [ObservationLibrary](ObservationLibrary.html) Observation()
OccurrenceFunctions
public [OccurrenceFunctionsLibrary](OccurrenceFunctionsLibrary.html) OccurrenceFunctions()
Occurrences
public [OccurrencesLibrary](OccurrencesLibrary.html) Occurrences()
Performances
public [PerformancesLibrary](PerformancesLibrary.html) Performances()
RationalFunctions
public [RationalFunctionsLibrary](RationalFunctionsLibrary.html) RationalFunctions()
RealFunctions
public [RealFunctionsLibrary](RealFunctionsLibrary.html) RealFunctions()
ScalarFunctions
public [ScalarFunctionsLibrary](ScalarFunctionsLibrary.html) ScalarFunctions()
ScalarValues
public [ScalarValuesLibrary](ScalarValuesLibrary.html) ScalarValues()
SequenceFunctions
public [SequenceFunctionsLibrary](SequenceFunctionsLibrary.html) SequenceFunctions()
SpatialFrames
public [SpatialFramesLibrary](SpatialFramesLibrary.html) SpatialFrames()
StatePerformances
public [StatePerformancesLibrary](StatePerformancesLibrary.html) StatePerformances()
StringFunctions
public [StringFunctionsLibrary](StringFunctionsLibrary.html) StringFunctions()
Transfers
public [TransfersLibrary](TransfersLibrary.html) Transfers()
TransitionPerformances
public [TransitionPerformancesLibrary](TransitionPerformancesLibrary.html) TransitionPerformances()
TrigFunctions
public [TrigFunctionsLibrary](TrigFunctionsLibrary.html) TrigFunctions()
Triggers
public [TriggersLibrary](TriggersLibrary.html) Triggers()
VectorFunctions
public [VectorFunctionsLibrary](VectorFunctionsLibrary.html) VectorFunctions()
VectorValues
public [VectorValuesLibrary](VectorValuesLibrary.html) VectorValues()

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.libraries.standard</a></div>
<h1 class="title" title="Class Libraries">Class Libraries</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService&lt;<a href="../../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a>&gt;
<div class="inheritance">com.dassault_systemes.modeler.kerml.libraries.standard.Libraries</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.dassault_systemes.modeler.foundation.project.service.DisposableService</code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="../../../sysml/libraries/standard/Libraries.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">Libraries</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Libraries</span>
<span class="extends-implements">extends com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService&lt;<a href="../../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a>&gt;</span></div>
<div class="block">A holder of all KerML standard libraries.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.dassault_systemes.modeler.foundation.project.ModelElementProject)">Libraries</a><wbr/>(<a href="../../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project)</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="BaseLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">BaseLibrary</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#Base()">Base</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="BaseFunctionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">BaseFunctionsLibrary</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#BaseFunctions()">BaseFunctions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="BooleanFunctionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">BooleanFunctionsLibrary</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#BooleanFunctions()">BooleanFunctions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ClocksLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ClocksLibrary</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#Clocks()">Clocks</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="CollectionFunctionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">CollectionFunctionsLibrary</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#CollectionFunctions()">CollectionFunctions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="CollectionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">CollectionsLibrary</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#Collections()">Collections</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ComplexFunctionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ComplexFunctionsLibrary</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#ComplexFunctions()">ComplexFunctions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ControlFunctionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ControlFunctionsLibrary</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#ControlFunctions()">ControlFunctions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ControlPerformancesLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ControlPerformancesLibrary</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#ControlPerformances()">ControlPerformances</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="DataFunctionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">DataFunctionsLibrary</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#DataFunctions()">DataFunctions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="FeatureReferencingPerformancesLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">FeatureReferencingPerformancesLibrary</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#FeatureReferencingPerformances()">FeatureReferencingPerformances</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="Libraries.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">Libraries</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstance(com.nomagic.magicdraw.uml.BaseElement)">getInstance</a><wbr/>(<a href="../../../../../nomagic/magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="Libraries.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">Libraries</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstanceByProject(com.dassault_systemes.modeler.foundation.project.ModelElementProject)">getInstanceByProject</a><wbr/>(<a href="../../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="IntegerFunctionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">IntegerFunctionsLibrary</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#IntegerFunctions()">IntegerFunctions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="KerMLLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#KerML()">KerML</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="LinksLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">LinksLibrary</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#Links()">Links</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="MetaobjectsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">MetaobjectsLibrary</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#Metaobjects()">Metaobjects</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="NaturalFunctionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">NaturalFunctionsLibrary</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#NaturalFunctions()">NaturalFunctions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="NumericalFunctionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">NumericalFunctionsLibrary</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#NumericalFunctions()">NumericalFunctions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ObjectsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ObjectsLibrary</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#Objects()">Objects</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ObservationLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ObservationLibrary</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#Observation()">Observation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="OccurrenceFunctionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">OccurrenceFunctionsLibrary</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#OccurrenceFunctions()">OccurrenceFunctions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="OccurrencesLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">OccurrencesLibrary</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#Occurrences()">Occurrences</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="PerformancesLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">PerformancesLibrary</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#Performances()">Performances</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="RationalFunctionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">RationalFunctionsLibrary</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#RationalFunctions()">RationalFunctions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="RealFunctionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">RealFunctionsLibrary</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#RealFunctions()">RealFunctions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ScalarFunctionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ScalarFunctionsLibrary</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#ScalarFunctions()">ScalarFunctions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ScalarValuesLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ScalarValuesLibrary</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#ScalarValues()">ScalarValues</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SequenceFunctionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">SequenceFunctionsLibrary</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#SequenceFunctions()">SequenceFunctions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SpatialFramesLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">SpatialFramesLibrary</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#SpatialFrames()">SpatialFrames</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="StatePerformancesLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">StatePerformancesLibrary</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#StatePerformances()">StatePerformances</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="StringFunctionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">StringFunctionsLibrary</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#StringFunctions()">StringFunctions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="TransfersLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">TransfersLibrary</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#Transfers()">Transfers</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="TransitionPerformancesLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">TransitionPerformancesLibrary</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#TransitionPerformances()">TransitionPerformances</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="TrigFunctionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">TrigFunctionsLibrary</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#TrigFunctions()">TrigFunctions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="TriggersLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">TriggersLibrary</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#Triggers()">Triggers</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="VectorFunctionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">VectorFunctionsLibrary</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#VectorFunctions()">VectorFunctions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="VectorValuesLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">VectorValuesLibrary</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#VectorValues()">VectorValues</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
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
<h3>Libraries</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Libraries</span><wbr/><span class="parameters">(<a href="../../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project)</span></div>
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
<section class="detail" id="getInstanceByProject(com.dassault_systemes.modeler.foundation.project.ModelElementProject)">
<h3>getInstanceByProject</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="Libraries.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">Libraries</a></span> <span class="element-name">getInstanceByProject</span><wbr/><span class="parameters">(<a href="../../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project)</span></div>
</section>
</li>
<li>
<section class="detail" id="getInstance(com.nomagic.magicdraw.uml.BaseElement)">
<h3>getInstance</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="Libraries.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">Libraries</a></span> <span class="element-name">getInstance</span><wbr/><span class="parameters">(<a href="../../../../../nomagic/magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="BaseFunctions()">
<h3>BaseFunctions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="BaseFunctionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">BaseFunctionsLibrary</a></span> <span class="element-name">BaseFunctions</span>()</div>
</section>
</li>
<li>
<section class="detail" id="Base()">
<h3>Base</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="BaseLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">BaseLibrary</a></span> <span class="element-name">Base</span>()</div>
</section>
</li>
<li>
<section class="detail" id="BooleanFunctions()">
<h3>BooleanFunctions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="BooleanFunctionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">BooleanFunctionsLibrary</a></span> <span class="element-name">BooleanFunctions</span>()</div>
</section>
</li>
<li>
<section class="detail" id="Clocks()">
<h3>Clocks</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ClocksLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ClocksLibrary</a></span> <span class="element-name">Clocks</span>()</div>
</section>
</li>
<li>
<section class="detail" id="CollectionFunctions()">
<h3>CollectionFunctions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="CollectionFunctionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">CollectionFunctionsLibrary</a></span> <span class="element-name">CollectionFunctions</span>()</div>
</section>
</li>
<li>
<section class="detail" id="Collections()">
<h3>Collections</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="CollectionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">CollectionsLibrary</a></span> <span class="element-name">Collections</span>()</div>
</section>
</li>
<li>
<section class="detail" id="ComplexFunctions()">
<h3>ComplexFunctions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ComplexFunctionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ComplexFunctionsLibrary</a></span> <span class="element-name">ComplexFunctions</span>()</div>
</section>
</li>
<li>
<section class="detail" id="ControlFunctions()">
<h3>ControlFunctions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ControlFunctionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ControlFunctionsLibrary</a></span> <span class="element-name">ControlFunctions</span>()</div>
</section>
</li>
<li>
<section class="detail" id="ControlPerformances()">
<h3>ControlPerformances</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ControlPerformancesLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ControlPerformancesLibrary</a></span> <span class="element-name">ControlPerformances</span>()</div>
</section>
</li>
<li>
<section class="detail" id="DataFunctions()">
<h3>DataFunctions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="DataFunctionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">DataFunctionsLibrary</a></span> <span class="element-name">DataFunctions</span>()</div>
</section>
</li>
<li>
<section class="detail" id="FeatureReferencingPerformances()">
<h3>FeatureReferencingPerformances</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="FeatureReferencingPerformancesLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">FeatureReferencingPerformancesLibrary</a></span> <span class="element-name">FeatureReferencingPerformances</span>()</div>
</section>
</li>
<li>
<section class="detail" id="IntegerFunctions()">
<h3>IntegerFunctions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="IntegerFunctionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">IntegerFunctionsLibrary</a></span> <span class="element-name">IntegerFunctions</span>()</div>
</section>
</li>
<li>
<section class="detail" id="KerML()">
<h3>KerML</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="KerMLLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary</a></span> <span class="element-name">KerML</span>()</div>
</section>
</li>
<li>
<section class="detail" id="Links()">
<h3>Links</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="LinksLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">LinksLibrary</a></span> <span class="element-name">Links</span>()</div>
</section>
</li>
<li>
<section class="detail" id="Metaobjects()">
<h3>Metaobjects</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="MetaobjectsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">MetaobjectsLibrary</a></span> <span class="element-name">Metaobjects</span>()</div>
</section>
</li>
<li>
<section class="detail" id="NaturalFunctions()">
<h3>NaturalFunctions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="NaturalFunctionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">NaturalFunctionsLibrary</a></span> <span class="element-name">NaturalFunctions</span>()</div>
</section>
</li>
<li>
<section class="detail" id="NumericalFunctions()">
<h3>NumericalFunctions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="NumericalFunctionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">NumericalFunctionsLibrary</a></span> <span class="element-name">NumericalFunctions</span>()</div>
</section>
</li>
<li>
<section class="detail" id="Objects()">
<h3>Objects</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ObjectsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ObjectsLibrary</a></span> <span class="element-name">Objects</span>()</div>
</section>
</li>
<li>
<section class="detail" id="Observation()">
<h3>Observation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ObservationLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ObservationLibrary</a></span> <span class="element-name">Observation</span>()</div>
</section>
</li>
<li>
<section class="detail" id="OccurrenceFunctions()">
<h3>OccurrenceFunctions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="OccurrenceFunctionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">OccurrenceFunctionsLibrary</a></span> <span class="element-name">OccurrenceFunctions</span>()</div>
</section>
</li>
<li>
<section class="detail" id="Occurrences()">
<h3>Occurrences</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="OccurrencesLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">OccurrencesLibrary</a></span> <span class="element-name">Occurrences</span>()</div>
</section>
</li>
<li>
<section class="detail" id="Performances()">
<h3>Performances</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="PerformancesLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">PerformancesLibrary</a></span> <span class="element-name">Performances</span>()</div>
</section>
</li>
<li>
<section class="detail" id="RationalFunctions()">
<h3>RationalFunctions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="RationalFunctionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">RationalFunctionsLibrary</a></span> <span class="element-name">RationalFunctions</span>()</div>
</section>
</li>
<li>
<section class="detail" id="RealFunctions()">
<h3>RealFunctions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="RealFunctionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">RealFunctionsLibrary</a></span> <span class="element-name">RealFunctions</span>()</div>
</section>
</li>
<li>
<section class="detail" id="ScalarFunctions()">
<h3>ScalarFunctions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ScalarFunctionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ScalarFunctionsLibrary</a></span> <span class="element-name">ScalarFunctions</span>()</div>
</section>
</li>
<li>
<section class="detail" id="ScalarValues()">
<h3>ScalarValues</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ScalarValuesLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ScalarValuesLibrary</a></span> <span class="element-name">ScalarValues</span>()</div>
</section>
</li>
<li>
<section class="detail" id="SequenceFunctions()">
<h3>SequenceFunctions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SequenceFunctionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">SequenceFunctionsLibrary</a></span> <span class="element-name">SequenceFunctions</span>()</div>
</section>
</li>
<li>
<section class="detail" id="SpatialFrames()">
<h3>SpatialFrames</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SpatialFramesLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">SpatialFramesLibrary</a></span> <span class="element-name">SpatialFrames</span>()</div>
</section>
</li>
<li>
<section class="detail" id="StatePerformances()">
<h3>StatePerformances</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="StatePerformancesLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">StatePerformancesLibrary</a></span> <span class="element-name">StatePerformances</span>()</div>
</section>
</li>
<li>
<section class="detail" id="StringFunctions()">
<h3>StringFunctions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="StringFunctionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">StringFunctionsLibrary</a></span> <span class="element-name">StringFunctions</span>()</div>
</section>
</li>
<li>
<section class="detail" id="Transfers()">
<h3>Transfers</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="TransfersLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">TransfersLibrary</a></span> <span class="element-name">Transfers</span>()</div>
</section>
</li>
<li>
<section class="detail" id="TransitionPerformances()">
<h3>TransitionPerformances</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="TransitionPerformancesLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">TransitionPerformancesLibrary</a></span> <span class="element-name">TransitionPerformances</span>()</div>
</section>
</li>
<li>
<section class="detail" id="TrigFunctions()">
<h3>TrigFunctions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="TrigFunctionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">TrigFunctionsLibrary</a></span> <span class="element-name">TrigFunctions</span>()</div>
</section>
</li>
<li>
<section class="detail" id="Triggers()">
<h3>Triggers</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="TriggersLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">TriggersLibrary</a></span> <span class="element-name">Triggers</span>()</div>
</section>
</li>
<li>
<section class="detail" id="VectorFunctions()">
<h3>VectorFunctions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="VectorFunctionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">VectorFunctionsLibrary</a></span> <span class="element-name">VectorFunctions</span>()</div>
</section>
</li>
<li>
<section class="detail" id="VectorValues()">
<h3>VectorValues</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="VectorValuesLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">VectorValuesLibrary</a></span> <span class="element-name">VectorValues</span>()</div>
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
