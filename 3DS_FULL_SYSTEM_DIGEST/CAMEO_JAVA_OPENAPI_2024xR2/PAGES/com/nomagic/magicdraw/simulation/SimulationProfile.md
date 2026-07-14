# JAVA OPENAPI: SimulationProfile (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/simulation/SimulationProfile.html
- source_path: `com/nomagic/magicdraw/simulation/SimulationProfile.html`
- source_sha256: `0bbaaacc91e63e5e76f64477457a58fa9603ab2ae872aa6b38b814dce14ecae7`
- captured_utc: `2026-07-14T16:55:29.779171+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.simulation](package-summary.html)

## Class SimulationProfile

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.profiles.ProfileImplementation](../../profiles/ProfileImplementation.html)
com.nomagic.magicdraw.simulation.SimulationProfile

@OpenApiAllpublic classSimulationProfile
extends [ProfileImplementation](../../profiles/ProfileImplementation.html)

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`static class`
`[SimulationProfile._3DXSimulationTemplateStereotype](SimulationProfile._3DXSimulationTemplateStereotype.html)`

`static class`
`[SimulationProfile.ActivationStereotype](SimulationProfile.ActivationStereotype.html)`

`static class`
`[SimulationProfile.ActiveImageStereotype](SimulationProfile.ActiveImageStereotype.html)`

`static enum`
`[SimulationProfile.ActiveStateImagesEnum](SimulationProfile.ActiveStateImagesEnum.html)`

`static class`
`[SimulationProfile.BehaviorCallStereotype](SimulationProfile.BehaviorCallStereotype.html)`

`static class`
`[SimulationProfile.ConstraintFailureStereotype](SimulationProfile.ConstraintFailureStereotype.html)`

`static class`
`[SimulationProfile.CSVExportStereotype](SimulationProfile.CSVExportStereotype.html)`

`static enum`
`[SimulationProfile.DataRecordTypeEnum](SimulationProfile.DataRecordTypeEnum.html)`

`static class`
`[SimulationProfile.DeactivationStereotype](SimulationProfile.DeactivationStereotype.html)`

`static enum`
`[SimulationProfile.DurationSimulationModeEnum](SimulationProfile.DurationSimulationModeEnum.html)`

`static class`
`[SimulationProfile.ExecutionEventStereotype](SimulationProfile.ExecutionEventStereotype.html)`

`static class`
`[SimulationProfile.ExecutionListenerStereotype](SimulationProfile.ExecutionListenerStereotype.html)`

`static class`
`[SimulationProfile.ExecutionSessionStereotype](SimulationProfile.ExecutionSessionStereotype.html)`

`static class`
`[SimulationProfile.HistogramStereotype](SimulationProfile.HistogramStereotype.html)`

`static class`
`[SimulationProfile.ImageSwitcherStereotype](SimulationProfile.ImageSwitcherStereotype.html)`

`static class`
`[SimulationProfile.InvocationStereotype](SimulationProfile.InvocationStereotype.html)`

`static class`
`[SimulationProfile.NestedUIConfigStereotype](SimulationProfile.NestedUIConfigStereotype.html)`

`static class`
`[SimulationProfile.OperationCallStereotype](SimulationProfile.OperationCallStereotype.html)`

`static class`
`[SimulationProfile.RuntimeValueStereotype](SimulationProfile.RuntimeValueStereotype.html)`

`static class`
`[SimulationProfile.SelectPropertiesConfigStereotype](SimulationProfile.SelectPropertiesConfigStereotype.html)`

`static class`
`[SimulationProfile.SequenceDiagramGeneratorConfigStereotype](SimulationProfile.SequenceDiagramGeneratorConfigStereotype.html)`

`static class`
`[SimulationProfile.SignalInstanceStereotype](SimulationProfile.SignalInstanceStereotype.html)`

`static class`
`[SimulationProfile.SimulationConfigStereotype](SimulationProfile.SimulationConfigStereotype.html)`

`static class`
`[SimulationProfile.SimulationLogStereotype](SimulationProfile.SimulationLogStereotype.html)`

`static class`
`[SimulationProfile.TimeHandlerStereotype](SimulationProfile.TimeHandlerStereotype.html)`

`static class`
`[SimulationProfile.TimelineChartStereotype](SimulationProfile.TimelineChartStereotype.html)`

`static enum`
`[SimulationProfile.TimelineModeEnum](SimulationProfile.TimelineModeEnum.html)`

`static class`
`[SimulationProfile.TimeSeriesChartStereotype](SimulationProfile.TimeSeriesChartStereotype.html)`

`static enum`
`[SimulationProfile.TimeUnitKindEnum](SimulationProfile.TimeUnitKindEnum.html)`

`static class`
`[SimulationProfile.UIStereotype](SimulationProfile.UIStereotype.html)`

`static class`
`[SimulationProfile.WidgetStereotype](SimulationProfile.WidgetStereotype.html)`
Nested classes/interfaces inherited from class com.nomagic.profiles.[ProfileImplementation](../../profiles/ProfileImplementation.html)
`[ProfileImplementation.StereotypeWrapper](../../profiles/ProfileImplementation.StereotypeWrapper.html)`
 =========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ACTIVESTATEIMAGES_DATATYPE](#ACTIVESTATEIMAGES_DATATYPE)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[CALLBEHAVIORACTION_CUSTOMIZATION_BODY_PROPERTY](#CALLBEHAVIORACTION_CUSTOMIZATION_BODY_PROPERTY)`
If Behavior is an OpaqueBehavior, represents it's body.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DATARECORDTYPE_DATATYPE](#DATARECORDTYPE_DATATYPE)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DURATIONSIMULATIONMODE_DATATYPE](#DURATIONSIMULATIONMODE_DATATYPE)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[PROFILE_NAME](#PROFILE_NAME)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[PROFILE_URI](#PROFILE_URI)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[STATE_CUSTOMIZATION_BODY_PROPERTY](#STATE_CUSTOMIZATION_BODY_PROPERTY)`
If Behavior is an OpaqueBehavior, represents it's body.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[TIMELINEMODE_DATATYPE](#TIMELINEMODE_DATATYPE)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[TIMEUNITKIND_DATATYPE](#TIMEUNITKIND_DATATYPE)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[SimulationProfile](#%3Cinit%3E(com.nomagic.profiles.ProfileCache))(com.nomagic.profiles.ProfileCache cache)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[SimulationProfile._3DXSimulationTemplateStereotype](SimulationProfile._3DXSimulationTemplateStereotype.html)`
`[_3DXSimulationTemplate](#_3DXSimulationTemplate())()`

`[SimulationProfile.ActivationStereotype](SimulationProfile.ActivationStereotype.html)`
`[activation](#activation())()`

`[SimulationProfile.ActiveImageStereotype](SimulationProfile.ActiveImageStereotype.html)`
`[activeImage](#activeImage())()`

`[SimulationProfile.BehaviorCallStereotype](SimulationProfile.BehaviorCallStereotype.html)`
`[behaviorCall](#behaviorCall())()`

`[SimulationProfile.ConstraintFailureStereotype](SimulationProfile.ConstraintFailureStereotype.html)`
`[constraintFailure](#constraintFailure())()`

`[SimulationProfile.CSVExportStereotype](SimulationProfile.CSVExportStereotype.html)`
`[csvExport](#csvExport())()`

`[SimulationProfile.DeactivationStereotype](SimulationProfile.DeactivationStereotype.html)`
`[deactivation](#deactivation())()`

`[SimulationProfile.ExecutionEventStereotype](SimulationProfile.ExecutionEventStereotype.html)`
`[executionEvent](#executionEvent())()`

`[SimulationProfile.ExecutionListenerStereotype](SimulationProfile.ExecutionListenerStereotype.html)`
`[executionListener](#executionListener())()`

`[SimulationProfile.ExecutionSessionStereotype](SimulationProfile.ExecutionSessionStereotype.html)`
`[executionSession](#executionSession())()`

`protected [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.nomagic.profiles.ProfileImplementation.ProfileElementWrapper>`
`[generatedGetAllElementWrappers](#generatedGetAllElementWrappers())()`

`protected [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html)>`
`[generatedGetAllStereotypes](#generatedGetAllStereotypes())()`

`[Enumeration](../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html)`
`[getActiveStateImages](#getActiveStateImages())()`

`[Enumeration](../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html)`
`[getDataRecordType](#getDataRecordType())()`

`[Enumeration](../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html)`
`[getDurationSimulationMode](#getDurationSimulationMode())()`

`static [SimulationProfile](SimulationProfile.html)`
`[getInstance](#getInstance(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../uml/BaseElement.html) baseElement)`

`static [SimulationProfile](SimulationProfile.html)`
`[getInstanceByProject](#getInstanceByProject(com.nomagic.uml2.project.ElementProject))(com.nomagic.uml2.project.ElementProject project)`

`[Enumeration](../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html)`
`[getTimelineMode](#getTimelineMode())()`

`[Enumeration](../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html)`
`[getTimeUnitKind](#getTimeUnitKind())()`

`[SimulationProfile.HistogramStereotype](SimulationProfile.HistogramStereotype.html)`
`[histogram](#histogram())()`

`[SimulationProfile.ImageSwitcherStereotype](SimulationProfile.ImageSwitcherStereotype.html)`
`[imageSwitcher](#imageSwitcher())()`

`[SimulationProfile.InvocationStereotype](SimulationProfile.InvocationStereotype.html)`
`[invocation](#invocation())()`

`[SimulationProfile.NestedUIConfigStereotype](SimulationProfile.NestedUIConfigStereotype.html)`
`[nestedUIConfig](#nestedUIConfig())()`

`[SimulationProfile.OperationCallStereotype](SimulationProfile.OperationCallStereotype.html)`
`[operationCall](#operationCall())()`

`[SimulationProfile.RuntimeValueStereotype](SimulationProfile.RuntimeValueStereotype.html)`
`[runtimeValue](#runtimeValue())()`

`[SimulationProfile.SelectPropertiesConfigStereotype](SimulationProfile.SelectPropertiesConfigStereotype.html)`
`[selectPropertiesConfig](#selectPropertiesConfig())()`

`[SimulationProfile.SequenceDiagramGeneratorConfigStereotype](SimulationProfile.SequenceDiagramGeneratorConfigStereotype.html)`
`[sequenceDiagramGeneratorConfig](#sequenceDiagramGeneratorConfig())()`

`[SimulationProfile.SignalInstanceStereotype](SimulationProfile.SignalInstanceStereotype.html)`
`[signalInstance](#signalInstance())()`

`[SimulationProfile.SimulationConfigStereotype](SimulationProfile.SimulationConfigStereotype.html)`
`[simulationConfig](#simulationConfig())()`

`[SimulationProfile.SimulationLogStereotype](SimulationProfile.SimulationLogStereotype.html)`
`[simulationLog](#simulationLog())()`

`[SimulationProfile.TimeHandlerStereotype](SimulationProfile.TimeHandlerStereotype.html)`
`[timeHandler](#timeHandler())()`

`[SimulationProfile.TimelineChartStereotype](SimulationProfile.TimelineChartStereotype.html)`
`[timelineChart](#timelineChart())()`

`[SimulationProfile.TimeSeriesChartStereotype](SimulationProfile.TimeSeriesChartStereotype.html)`
`[timeSeriesChart](#timeSeriesChart())()`

`[SimulationProfile.UIStereotype](SimulationProfile.UIStereotype.html)`
`[ui](#ui())()`

`[SimulationProfile.WidgetStereotype](SimulationProfile.WidgetStereotype.html)`
`[widget](#widget())()`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
PROFILE_URI
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) PROFILE_URI
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.PROFILE_URI)
PROFILE_NAME
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) PROFILE_NAME
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.PROFILE_NAME)
ACTIVESTATEIMAGES_DATATYPE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ACTIVESTATEIMAGES_DATATYPE
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.ACTIVESTATEIMAGES_DATATYPE)
DATARECORDTYPE_DATATYPE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DATARECORDTYPE_DATATYPE
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.DATARECORDTYPE_DATATYPE)
DURATIONSIMULATIONMODE_DATATYPE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DURATIONSIMULATIONMODE_DATATYPE
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.DURATIONSIMULATIONMODE_DATATYPE)
TIMEUNITKIND_DATATYPE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TIMEUNITKIND_DATATYPE
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.TIMEUNITKIND_DATATYPE)
TIMELINEMODE_DATATYPE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TIMELINEMODE_DATATYPE
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.TIMELINEMODE_DATATYPE)
CALLBEHAVIORACTION_CUSTOMIZATION_BODY_PROPERTY
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) CALLBEHAVIORACTION_CUSTOMIZATION_BODY_PROPERTY
If Behavior is an OpaqueBehavior, represents it's body.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.CALLBEHAVIORACTION_CUSTOMIZATION_BODY_PROPERTY)
STATE_CUSTOMIZATION_BODY_PROPERTY
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) STATE_CUSTOMIZATION_BODY_PROPERTY
If Behavior is an OpaqueBehavior, represents it's body.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.STATE_CUSTOMIZATION_BODY_PROPERTY)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
SimulationProfile
public SimulationProfile(com.nomagic.profiles.ProfileCache cache)
 ============ METHOD DETAIL ========== 
Method Details
getInstance
public static [SimulationProfile](SimulationProfile.html) getInstance([BaseElement](../uml/BaseElement.html) baseElement)
getInstanceByProject
public static [SimulationProfile](SimulationProfile.html) getInstanceByProject(com.nomagic.uml2.project.ElementProject project)
_3DXSimulationTemplate
public [SimulationProfile._3DXSimulationTemplateStereotype](SimulationProfile._3DXSimulationTemplateStereotype.html) _3DXSimulationTemplate()
activation
public [SimulationProfile.ActivationStereotype](SimulationProfile.ActivationStereotype.html) activation()
activeImage
public [SimulationProfile.ActiveImageStereotype](SimulationProfile.ActiveImageStereotype.html) activeImage()
behaviorCall
public [SimulationProfile.BehaviorCallStereotype](SimulationProfile.BehaviorCallStereotype.html) behaviorCall()
csvExport
public [SimulationProfile.CSVExportStereotype](SimulationProfile.CSVExportStereotype.html) csvExport()
constraintFailure
public [SimulationProfile.ConstraintFailureStereotype](SimulationProfile.ConstraintFailureStereotype.html) constraintFailure()
deactivation
public [SimulationProfile.DeactivationStereotype](SimulationProfile.DeactivationStereotype.html) deactivation()
executionEvent
public [SimulationProfile.ExecutionEventStereotype](SimulationProfile.ExecutionEventStereotype.html) executionEvent()
executionListener
public [SimulationProfile.ExecutionListenerStereotype](SimulationProfile.ExecutionListenerStereotype.html) executionListener()
executionSession
public [SimulationProfile.ExecutionSessionStereotype](SimulationProfile.ExecutionSessionStereotype.html) executionSession()
histogram
public [SimulationProfile.HistogramStereotype](SimulationProfile.HistogramStereotype.html) histogram()
imageSwitcher
public [SimulationProfile.ImageSwitcherStereotype](SimulationProfile.ImageSwitcherStereotype.html) imageSwitcher()
invocation
public [SimulationProfile.InvocationStereotype](SimulationProfile.InvocationStereotype.html) invocation()
nestedUIConfig
public [SimulationProfile.NestedUIConfigStereotype](SimulationProfile.NestedUIConfigStereotype.html) nestedUIConfig()
operationCall
public [SimulationProfile.OperationCallStereotype](SimulationProfile.OperationCallStereotype.html) operationCall()
runtimeValue
public [SimulationProfile.RuntimeValueStereotype](SimulationProfile.RuntimeValueStereotype.html) runtimeValue()
selectPropertiesConfig
public [SimulationProfile.SelectPropertiesConfigStereotype](SimulationProfile.SelectPropertiesConfigStereotype.html) selectPropertiesConfig()
sequenceDiagramGeneratorConfig
public [SimulationProfile.SequenceDiagramGeneratorConfigStereotype](SimulationProfile.SequenceDiagramGeneratorConfigStereotype.html) sequenceDiagramGeneratorConfig()
signalInstance
public [SimulationProfile.SignalInstanceStereotype](SimulationProfile.SignalInstanceStereotype.html) signalInstance()
simulationConfig
public [SimulationProfile.SimulationConfigStereotype](SimulationProfile.SimulationConfigStereotype.html) simulationConfig()
simulationLog
public [SimulationProfile.SimulationLogStereotype](SimulationProfile.SimulationLogStereotype.html) simulationLog()
timeHandler
public [SimulationProfile.TimeHandlerStereotype](SimulationProfile.TimeHandlerStereotype.html) timeHandler()
timeSeriesChart
public [SimulationProfile.TimeSeriesChartStereotype](SimulationProfile.TimeSeriesChartStereotype.html) timeSeriesChart()
timelineChart
public [SimulationProfile.TimelineChartStereotype](SimulationProfile.TimelineChartStereotype.html) timelineChart()
ui
public [SimulationProfile.UIStereotype](SimulationProfile.UIStereotype.html) ui()
widget
public [SimulationProfile.WidgetStereotype](SimulationProfile.WidgetStereotype.html) widget()
getActiveStateImages
public [Enumeration](../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html) getActiveStateImages()
getDataRecordType
public [Enumeration](../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html) getDataRecordType()
getDurationSimulationMode
public [Enumeration](../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html) getDurationSimulationMode()
getTimeUnitKind
public [Enumeration](../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html) getTimeUnitKind()
getTimelineMode
public [Enumeration](../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html) getTimelineMode()
generatedGetAllElementWrappers
protected [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.nomagic.profiles.ProfileImplementation.ProfileElementWrapper> generatedGetAllElementWrappers()
generatedGetAllStereotypes
protected [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html)> generatedGetAllStereotypes()

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.simulation</a></div>
<h1 class="title" title="Class SimulationProfile">Class SimulationProfile</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="../../profiles/ProfileImplementation.html" title="class in com.nomagic.profiles">com.nomagic.profiles.ProfileImplementation</a>
<div class="inheritance">com.nomagic.magicdraw.simulation.SimulationProfile</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">SimulationProfile</span>
<span class="extends-implements">extends <a href="../../profiles/ProfileImplementation.html" title="class in com.nomagic.profiles">ProfileImplementation</a></span></div>
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
<div class="col-second even-row-color"><code><a class="type-name-link" href="SimulationProfile._3DXSimulationTemplateStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile._3DXSimulationTemplateStereotype</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="SimulationProfile.ActivationStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.ActivationStereotype</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="SimulationProfile.ActiveImageStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.ActiveImageStereotype</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static enum </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="SimulationProfile.ActiveStateImagesEnum.html" title="enum class in com.nomagic.magicdraw.simulation">SimulationProfile.ActiveStateImagesEnum</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="SimulationProfile.BehaviorCallStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.BehaviorCallStereotype</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="SimulationProfile.ConstraintFailureStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.ConstraintFailureStereotype</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="SimulationProfile.CSVExportStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.CSVExportStereotype</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static enum </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="SimulationProfile.DataRecordTypeEnum.html" title="enum class in com.nomagic.magicdraw.simulation">SimulationProfile.DataRecordTypeEnum</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="SimulationProfile.DeactivationStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.DeactivationStereotype</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static enum </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="SimulationProfile.DurationSimulationModeEnum.html" title="enum class in com.nomagic.magicdraw.simulation">SimulationProfile.DurationSimulationModeEnum</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="SimulationProfile.ExecutionEventStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.ExecutionEventStereotype</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="SimulationProfile.ExecutionListenerStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.ExecutionListenerStereotype</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="SimulationProfile.ExecutionSessionStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.ExecutionSessionStereotype</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="SimulationProfile.HistogramStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.HistogramStereotype</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="SimulationProfile.ImageSwitcherStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.ImageSwitcherStereotype</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="SimulationProfile.InvocationStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.InvocationStereotype</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="SimulationProfile.NestedUIConfigStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.NestedUIConfigStereotype</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="SimulationProfile.OperationCallStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.OperationCallStereotype</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="SimulationProfile.RuntimeValueStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.RuntimeValueStereotype</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="SimulationProfile.SelectPropertiesConfigStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.SelectPropertiesConfigStereotype</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="SimulationProfile.SequenceDiagramGeneratorConfigStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.SequenceDiagramGeneratorConfigStereotype</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="SimulationProfile.SignalInstanceStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.SignalInstanceStereotype</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="SimulationProfile.SimulationConfigStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.SimulationConfigStereotype</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="SimulationProfile.SimulationLogStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.SimulationLogStereotype</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="SimulationProfile.TimeHandlerStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.TimeHandlerStereotype</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="SimulationProfile.TimelineChartStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.TimelineChartStereotype</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static enum </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="SimulationProfile.TimelineModeEnum.html" title="enum class in com.nomagic.magicdraw.simulation">SimulationProfile.TimelineModeEnum</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="SimulationProfile.TimeSeriesChartStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.TimeSeriesChartStereotype</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static enum </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="SimulationProfile.TimeUnitKindEnum.html" title="enum class in com.nomagic.magicdraw.simulation">SimulationProfile.TimeUnitKindEnum</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="SimulationProfile.UIStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.UIStereotype</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="SimulationProfile.WidgetStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.WidgetStereotype</a></code></div>
<div class="col-last even-row-color"> </div>
</div>
<div class="inherited-list">
<h2 id="nested-classes-inherited-from-class-com.nomagic.profiles.ProfileImplementation">Nested classes/interfaces inherited from class com.nomagic.profiles.<a href="../../profiles/ProfileImplementation.html" title="class in com.nomagic.profiles">ProfileImplementation</a></h2>
<code><a href="../../profiles/ProfileImplementation.StereotypeWrapper.html" title="class in com.nomagic.profiles">ProfileImplementation.StereotypeWrapper</a></code></div>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ACTIVESTATEIMAGES_DATATYPE">ACTIVESTATEIMAGES_DATATYPE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#CALLBEHAVIORACTION_CUSTOMIZATION_BODY_PROPERTY">CALLBEHAVIORACTION_CUSTOMIZATION_BODY_PROPERTY</a></code></div>
<div class="col-last odd-row-color">
<div class="block">If Behavior is an OpaqueBehavior, represents it's body.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DATARECORDTYPE_DATATYPE">DATARECORDTYPE_DATATYPE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DURATIONSIMULATIONMODE_DATATYPE">DURATIONSIMULATIONMODE_DATATYPE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#PROFILE_NAME">PROFILE_NAME</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#PROFILE_URI">PROFILE_URI</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#STATE_CUSTOMIZATION_BODY_PROPERTY">STATE_CUSTOMIZATION_BODY_PROPERTY</a></code></div>
<div class="col-last even-row-color">
<div class="block">If Behavior is an OpaqueBehavior, represents it's body.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TIMELINEMODE_DATATYPE">TIMELINEMODE_DATATYPE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TIMEUNITKIND_DATATYPE">TIMEUNITKIND_DATATYPE</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.profiles.ProfileCache)">SimulationProfile</a><wbr/>(com.nomagic.profiles.ProfileCache cache)</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SimulationProfile._3DXSimulationTemplateStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile._3DXSimulationTemplateStereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#_3DXSimulationTemplate()">_3DXSimulationTemplate</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SimulationProfile.ActivationStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.ActivationStereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#activation()">activation</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SimulationProfile.ActiveImageStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.ActiveImageStereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#activeImage()">activeImage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SimulationProfile.BehaviorCallStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.BehaviorCallStereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#behaviorCall()">behaviorCall</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SimulationProfile.ConstraintFailureStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.ConstraintFailureStereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#constraintFailure()">constraintFailure</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SimulationProfile.CSVExportStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.CSVExportStereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#csvExport()">csvExport</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SimulationProfile.DeactivationStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.DeactivationStereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#deactivation()">deactivation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SimulationProfile.ExecutionEventStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.ExecutionEventStereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#executionEvent()">executionEvent</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SimulationProfile.ExecutionListenerStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.ExecutionListenerStereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#executionListener()">executionListener</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SimulationProfile.ExecutionSessionStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.ExecutionSessionStereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#executionSession()">executionSession</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.nomagic.profiles.ProfileImplementation.ProfileElementWrapper&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#generatedGetAllElementWrappers()">generatedGetAllElementWrappers</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#generatedGetAllStereotypes()">generatedGetAllStereotypes</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Enumeration</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getActiveStateImages()">getActiveStateImages</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Enumeration</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDataRecordType()">getDataRecordType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Enumeration</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDurationSimulationMode()">getDurationSimulationMode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="SimulationProfile.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstance(com.nomagic.magicdraw.uml.BaseElement)">getInstance</a><wbr/>(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> baseElement)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="SimulationProfile.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstanceByProject(com.nomagic.uml2.project.ElementProject)">getInstanceByProject</a><wbr/>(com.nomagic.uml2.project.ElementProject project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Enumeration</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTimelineMode()">getTimelineMode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Enumeration</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTimeUnitKind()">getTimeUnitKind</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SimulationProfile.HistogramStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.HistogramStereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#histogram()">histogram</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SimulationProfile.ImageSwitcherStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.ImageSwitcherStereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#imageSwitcher()">imageSwitcher</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SimulationProfile.InvocationStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.InvocationStereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#invocation()">invocation</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SimulationProfile.NestedUIConfigStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.NestedUIConfigStereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#nestedUIConfig()">nestedUIConfig</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SimulationProfile.OperationCallStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.OperationCallStereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#operationCall()">operationCall</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SimulationProfile.RuntimeValueStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.RuntimeValueStereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#runtimeValue()">runtimeValue</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SimulationProfile.SelectPropertiesConfigStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.SelectPropertiesConfigStereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#selectPropertiesConfig()">selectPropertiesConfig</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SimulationProfile.SequenceDiagramGeneratorConfigStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.SequenceDiagramGeneratorConfigStereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sequenceDiagramGeneratorConfig()">sequenceDiagramGeneratorConfig</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SimulationProfile.SignalInstanceStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.SignalInstanceStereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#signalInstance()">signalInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SimulationProfile.SimulationConfigStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.SimulationConfigStereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#simulationConfig()">simulationConfig</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SimulationProfile.SimulationLogStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.SimulationLogStereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#simulationLog()">simulationLog</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SimulationProfile.TimeHandlerStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.TimeHandlerStereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#timeHandler()">timeHandler</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SimulationProfile.TimelineChartStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.TimelineChartStereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#timelineChart()">timelineChart</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SimulationProfile.TimeSeriesChartStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.TimeSeriesChartStereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#timeSeriesChart()">timeSeriesChart</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SimulationProfile.UIStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.UIStereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#ui()">ui</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SimulationProfile.WidgetStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.WidgetStereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#widget()">widget</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">PROFILE_URI</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.PROFILE_URI">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PROFILE_NAME">
<h3>PROFILE_NAME</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">PROFILE_NAME</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.PROFILE_NAME">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ACTIVESTATEIMAGES_DATATYPE">
<h3>ACTIVESTATEIMAGES_DATATYPE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ACTIVESTATEIMAGES_DATATYPE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.ACTIVESTATEIMAGES_DATATYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DATARECORDTYPE_DATATYPE">
<h3>DATARECORDTYPE_DATATYPE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DATARECORDTYPE_DATATYPE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.DATARECORDTYPE_DATATYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DURATIONSIMULATIONMODE_DATATYPE">
<h3>DURATIONSIMULATIONMODE_DATATYPE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DURATIONSIMULATIONMODE_DATATYPE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.DURATIONSIMULATIONMODE_DATATYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TIMEUNITKIND_DATATYPE">
<h3>TIMEUNITKIND_DATATYPE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TIMEUNITKIND_DATATYPE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.TIMEUNITKIND_DATATYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TIMELINEMODE_DATATYPE">
<h3>TIMELINEMODE_DATATYPE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TIMELINEMODE_DATATYPE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.TIMELINEMODE_DATATYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CALLBEHAVIORACTION_CUSTOMIZATION_BODY_PROPERTY">
<h3>CALLBEHAVIORACTION_CUSTOMIZATION_BODY_PROPERTY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">CALLBEHAVIORACTION_CUSTOMIZATION_BODY_PROPERTY</span></div>
<div class="block">If Behavior is an OpaqueBehavior, represents it's body.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.CALLBEHAVIORACTION_CUSTOMIZATION_BODY_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="STATE_CUSTOMIZATION_BODY_PROPERTY">
<h3>STATE_CUSTOMIZATION_BODY_PROPERTY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">STATE_CUSTOMIZATION_BODY_PROPERTY</span></div>
<div class="block">If Behavior is an OpaqueBehavior, represents it's body.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.STATE_CUSTOMIZATION_BODY_PROPERTY">Constant Field Values</a></li>
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
<h3>SimulationProfile</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SimulationProfile</span><wbr/><span class="parameters">(com.nomagic.profiles.ProfileCache cache)</span></div>
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="SimulationProfile.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile</a></span> <span class="element-name">getInstance</span><wbr/><span class="parameters">(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> baseElement)</span></div>
</section>
</li>
<li>
<section class="detail" id="getInstanceByProject(com.nomagic.uml2.project.ElementProject)">
<h3>getInstanceByProject</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="SimulationProfile.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile</a></span> <span class="element-name">getInstanceByProject</span><wbr/><span class="parameters">(com.nomagic.uml2.project.ElementProject project)</span></div>
</section>
</li>
<li>
<section class="detail" id="_3DXSimulationTemplate()">
<h3>_3DXSimulationTemplate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SimulationProfile._3DXSimulationTemplateStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile._3DXSimulationTemplateStereotype</a></span> <span class="element-name">_3DXSimulationTemplate</span>()</div>
</section>
</li>
<li>
<section class="detail" id="activation()">
<h3>activation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SimulationProfile.ActivationStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.ActivationStereotype</a></span> <span class="element-name">activation</span>()</div>
</section>
</li>
<li>
<section class="detail" id="activeImage()">
<h3>activeImage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SimulationProfile.ActiveImageStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.ActiveImageStereotype</a></span> <span class="element-name">activeImage</span>()</div>
</section>
</li>
<li>
<section class="detail" id="behaviorCall()">
<h3>behaviorCall</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SimulationProfile.BehaviorCallStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.BehaviorCallStereotype</a></span> <span class="element-name">behaviorCall</span>()</div>
</section>
</li>
<li>
<section class="detail" id="csvExport()">
<h3>csvExport</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SimulationProfile.CSVExportStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.CSVExportStereotype</a></span> <span class="element-name">csvExport</span>()</div>
</section>
</li>
<li>
<section class="detail" id="constraintFailure()">
<h3>constraintFailure</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SimulationProfile.ConstraintFailureStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.ConstraintFailureStereotype</a></span> <span class="element-name">constraintFailure</span>()</div>
</section>
</li>
<li>
<section class="detail" id="deactivation()">
<h3>deactivation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SimulationProfile.DeactivationStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.DeactivationStereotype</a></span> <span class="element-name">deactivation</span>()</div>
</section>
</li>
<li>
<section class="detail" id="executionEvent()">
<h3>executionEvent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SimulationProfile.ExecutionEventStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.ExecutionEventStereotype</a></span> <span class="element-name">executionEvent</span>()</div>
</section>
</li>
<li>
<section class="detail" id="executionListener()">
<h3>executionListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SimulationProfile.ExecutionListenerStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.ExecutionListenerStereotype</a></span> <span class="element-name">executionListener</span>()</div>
</section>
</li>
<li>
<section class="detail" id="executionSession()">
<h3>executionSession</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SimulationProfile.ExecutionSessionStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.ExecutionSessionStereotype</a></span> <span class="element-name">executionSession</span>()</div>
</section>
</li>
<li>
<section class="detail" id="histogram()">
<h3>histogram</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SimulationProfile.HistogramStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.HistogramStereotype</a></span> <span class="element-name">histogram</span>()</div>
</section>
</li>
<li>
<section class="detail" id="imageSwitcher()">
<h3>imageSwitcher</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SimulationProfile.ImageSwitcherStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.ImageSwitcherStereotype</a></span> <span class="element-name">imageSwitcher</span>()</div>
</section>
</li>
<li>
<section class="detail" id="invocation()">
<h3>invocation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SimulationProfile.InvocationStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.InvocationStereotype</a></span> <span class="element-name">invocation</span>()</div>
</section>
</li>
<li>
<section class="detail" id="nestedUIConfig()">
<h3>nestedUIConfig</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SimulationProfile.NestedUIConfigStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.NestedUIConfigStereotype</a></span> <span class="element-name">nestedUIConfig</span>()</div>
</section>
</li>
<li>
<section class="detail" id="operationCall()">
<h3>operationCall</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SimulationProfile.OperationCallStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.OperationCallStereotype</a></span> <span class="element-name">operationCall</span>()</div>
</section>
</li>
<li>
<section class="detail" id="runtimeValue()">
<h3>runtimeValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SimulationProfile.RuntimeValueStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.RuntimeValueStereotype</a></span> <span class="element-name">runtimeValue</span>()</div>
</section>
</li>
<li>
<section class="detail" id="selectPropertiesConfig()">
<h3>selectPropertiesConfig</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SimulationProfile.SelectPropertiesConfigStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.SelectPropertiesConfigStereotype</a></span> <span class="element-name">selectPropertiesConfig</span>()</div>
</section>
</li>
<li>
<section class="detail" id="sequenceDiagramGeneratorConfig()">
<h3>sequenceDiagramGeneratorConfig</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SimulationProfile.SequenceDiagramGeneratorConfigStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.SequenceDiagramGeneratorConfigStereotype</a></span> <span class="element-name">sequenceDiagramGeneratorConfig</span>()</div>
</section>
</li>
<li>
<section class="detail" id="signalInstance()">
<h3>signalInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SimulationProfile.SignalInstanceStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.SignalInstanceStereotype</a></span> <span class="element-name">signalInstance</span>()</div>
</section>
</li>
<li>
<section class="detail" id="simulationConfig()">
<h3>simulationConfig</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SimulationProfile.SimulationConfigStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.SimulationConfigStereotype</a></span> <span class="element-name">simulationConfig</span>()</div>
</section>
</li>
<li>
<section class="detail" id="simulationLog()">
<h3>simulationLog</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SimulationProfile.SimulationLogStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.SimulationLogStereotype</a></span> <span class="element-name">simulationLog</span>()</div>
</section>
</li>
<li>
<section class="detail" id="timeHandler()">
<h3>timeHandler</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SimulationProfile.TimeHandlerStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.TimeHandlerStereotype</a></span> <span class="element-name">timeHandler</span>()</div>
</section>
</li>
<li>
<section class="detail" id="timeSeriesChart()">
<h3>timeSeriesChart</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SimulationProfile.TimeSeriesChartStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.TimeSeriesChartStereotype</a></span> <span class="element-name">timeSeriesChart</span>()</div>
</section>
</li>
<li>
<section class="detail" id="timelineChart()">
<h3>timelineChart</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SimulationProfile.TimelineChartStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.TimelineChartStereotype</a></span> <span class="element-name">timelineChart</span>()</div>
</section>
</li>
<li>
<section class="detail" id="ui()">
<h3>ui</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SimulationProfile.UIStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.UIStereotype</a></span> <span class="element-name">ui</span>()</div>
</section>
</li>
<li>
<section class="detail" id="widget()">
<h3>widget</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SimulationProfile.WidgetStereotype.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile.WidgetStereotype</a></span> <span class="element-name">widget</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getActiveStateImages()">
<h3>getActiveStateImages</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Enumeration</a></span> <span class="element-name">getActiveStateImages</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getDataRecordType()">
<h3>getDataRecordType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Enumeration</a></span> <span class="element-name">getDataRecordType</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getDurationSimulationMode()">
<h3>getDurationSimulationMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Enumeration</a></span> <span class="element-name">getDurationSimulationMode</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getTimeUnitKind()">
<h3>getTimeUnitKind</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Enumeration</a></span> <span class="element-name">getTimeUnitKind</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getTimelineMode()">
<h3>getTimelineMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Enumeration</a></span> <span class="element-name">getTimelineMode</span>()</div>
</section>
</li>
<li>
<section class="detail" id="generatedGetAllElementWrappers()">
<h3>generatedGetAllElementWrappers</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.nomagic.profiles.ProfileImplementation.ProfileElementWrapper&gt;</span> <span class="element-name">generatedGetAllElementWrappers</span>()</div>
</section>
</li>
<li>
<section class="detail" id="generatedGetAllStereotypes()">
<h3>generatedGetAllStereotypes</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt;</span> <span class="element-name">generatedGetAllStereotypes</span>()</div>
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
