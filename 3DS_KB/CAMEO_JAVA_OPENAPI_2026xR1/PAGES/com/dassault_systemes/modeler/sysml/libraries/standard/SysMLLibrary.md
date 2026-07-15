# JAVA OPENAPI: SysMLLibrary (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/sysml/libraries/standard/SysMLLibrary.html
- source_path: `com/dassault_systemes/modeler/sysml/libraries/standard/SysMLLibrary.html`
- source_sha256: `72875552e5dee3b2a16ec28eed40e82f3366dfe1557c5e07e94b40798bba2288`
- captured_utc: `2026-07-14T16:45:01.744024+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.sysml.libraries.standard](package-summary.html)

## Class SysMLLibrary

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService<[ModelElementProject](../../../foundation/project/ModelElementProject.html)>
[com.dassault_systemes.modeler.kerml.libraries.AbstractLibrary](../../../kerml/libraries/AbstractLibrary.html)
com.dassault_systemes.modeler.sysml.libraries.standard.SysMLLibrary

All Implemented Interfaces:
`com.dassault_systemes.modeler.foundation.project.service.DisposableService`

@OpenApiAllpublic classSysMLLibrary
extends [AbstractLibrary](../../../kerml/libraries/AbstractLibrary.html)

Access helper for the sys ml standard library.

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`static class`
`[SysMLLibrary.AcceptActionUsageMetadataDefinition](SysMLLibrary.AcceptActionUsageMetadataDefinition.html)`
Wrapper for the accept action usage metadata definition library element.
`static class`
`[SysMLLibrary.ActionDefinitionMetadataDefinition](SysMLLibrary.ActionDefinitionMetadataDefinition.html)`
Wrapper for the action definition metadata definition library element.
`static class`
`[SysMLLibrary.ActionUsageMetadataDefinition](SysMLLibrary.ActionUsageMetadataDefinition.html)`
Wrapper for the action usage metadata definition library element.
`static class`
`[SysMLLibrary.ConnectionDefinitionMetadataDefinition](SysMLLibrary.ConnectionDefinitionMetadataDefinition.html)`
Wrapper for the connection definition metadata definition library element.
`static class`
`[SysMLLibrary.ConnectionUsageMetadataDefinition](SysMLLibrary.ConnectionUsageMetadataDefinition.html)`
Wrapper for the connection usage metadata definition library element.
`static class`
`[SysMLLibrary.ConstraintUsageMetadataDefinition](SysMLLibrary.ConstraintUsageMetadataDefinition.html)`
Wrapper for the constraint usage metadata definition library element.
`static class`
`[SysMLLibrary.ControlNodeMetadataDefinition](SysMLLibrary.ControlNodeMetadataDefinition.html)`
Wrapper for the control node metadata definition library element.
`static class`
`[SysMLLibrary.DecisionNodeMetadataDefinition](SysMLLibrary.DecisionNodeMetadataDefinition.html)`
Wrapper for the decision node metadata definition library element.
`static class`
`[SysMLLibrary.EnumerationDefinitionMetadataDefinition](SysMLLibrary.EnumerationDefinitionMetadataDefinition.html)`
Wrapper for the enumeration definition metadata definition library element.
`static class`
`[SysMLLibrary.EnumerationUsageMetadataDefinition](SysMLLibrary.EnumerationUsageMetadataDefinition.html)`
Wrapper for the enumeration usage metadata definition library element.
`static class`
`[SysMLLibrary.FlowUsageMetadataDefinition](SysMLLibrary.FlowUsageMetadataDefinition.html)`
Wrapper for the flow usage metadata definition library element.
`static class`
`[SysMLLibrary.ForkNodeMetadataDefinition](SysMLLibrary.ForkNodeMetadataDefinition.html)`
Wrapper for the fork node metadata definition library element.
`static class`
`[SysMLLibrary.IncludeUseCaseUsageMetadataDefinition](SysMLLibrary.IncludeUseCaseUsageMetadataDefinition.html)`
Wrapper for the include use case usage metadata definition library element.
`static class`
`[SysMLLibrary.ItemDefinitionMetadataDefinition](SysMLLibrary.ItemDefinitionMetadataDefinition.html)`
Wrapper for the item definition metadata definition library element.
`static class`
`[SysMLLibrary.JoinNodeMetadataDefinition](SysMLLibrary.JoinNodeMetadataDefinition.html)`
Wrapper for the join node metadata definition library element.
`static class`
`[SysMLLibrary.MergeNodeMetadataDefinition](SysMLLibrary.MergeNodeMetadataDefinition.html)`
Wrapper for the merge node metadata definition library element.
`static class`
`[SysMLLibrary.MetadataDefinitionMetadataDefinition](SysMLLibrary.MetadataDefinitionMetadataDefinition.html)`
Wrapper for the metadata definition metadata definition library element.
`static class`
`[SysMLLibrary.OccurrenceDefinitionMetadataDefinition](SysMLLibrary.OccurrenceDefinitionMetadataDefinition.html)`
Wrapper for the occurrence definition metadata definition library element.
`static class`
`[SysMLLibrary.PartDefinitionMetadataDefinition](SysMLLibrary.PartDefinitionMetadataDefinition.html)`
Wrapper for the part definition metadata definition library element.
`static class`
`[SysMLLibrary.PortDefinitionMetadataDefinition](SysMLLibrary.PortDefinitionMetadataDefinition.html)`
Wrapper for the port definition metadata definition library element.
`static class`
`[SysMLLibrary.PortUsageMetadataDefinition](SysMLLibrary.PortUsageMetadataDefinition.html)`
Wrapper for the port usage metadata definition library element.
`static class`
`[SysMLLibrary.ReferenceUsageMetadataDefinition](SysMLLibrary.ReferenceUsageMetadataDefinition.html)`
Wrapper for the reference usage metadata definition library element.
`static class`
`[SysMLLibrary.SendActionUsageMetadataDefinition](SysMLLibrary.SendActionUsageMetadataDefinition.html)`
Wrapper for the send action usage metadata definition library element.
`static class`
`[SysMLLibrary.StateDefinitionMetadataDefinition](SysMLLibrary.StateDefinitionMetadataDefinition.html)`
Wrapper for the state definition metadata definition library element.
`static class`
`[SysMLLibrary.StateUsageMetadataDefinition](SysMLLibrary.StateUsageMetadataDefinition.html)`
Wrapper for the state usage metadata definition library element.
`static class`
`[SysMLLibrary.TerminateActionUsageMetadataDefinition](SysMLLibrary.TerminateActionUsageMetadataDefinition.html)`
Wrapper for the terminate action usage metadata definition library element.
`static class`
`[SysMLLibrary.TransitionUsageMetadataDefinition](SysMLLibrary.TransitionUsageMetadataDefinition.html)`
Wrapper for the transition usage metadata definition library element.
`static class`
`[SysMLLibrary.UsageMetadataDefinition](SysMLLibrary.UsageMetadataDefinition.html)`
Wrapper for the usage metadata definition library element.
`static class`
`[SysMLLibrary.UseCaseDefinitionMetadataDefinition](SysMLLibrary.UseCaseDefinitionMetadataDefinition.html)`
Wrapper for the use case definition metadata definition library element.
`static class`
`[SysMLLibrary.ViewUsageMetadataDefinition](SysMLLibrary.ViewUsageMetadataDefinition.html)`
Wrapper for the view usage metadata definition library element.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[SysMLLibrary](#%3Cinit%3E(com.dassault_systemes.modeler.foundation.project.ModelElementProject))([ModelElementProject](../../../foundation/project/ModelElementProject.html) project)`
Creates a new sys mllibrary instance.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[SysMLLibrary.AcceptActionUsageMetadataDefinition](SysMLLibrary.AcceptActionUsageMetadataDefinition.html)`
`[AcceptActionUsage](#AcceptActionUsage())()`
Returns accept action usage.
`[SysMLLibrary.ActionDefinitionMetadataDefinition](SysMLLibrary.ActionDefinitionMetadataDefinition.html)`
`[ActionDefinition](#ActionDefinition())()`
Returns action definition.
`[SysMLLibrary.ActionUsageMetadataDefinition](SysMLLibrary.ActionUsageMetadataDefinition.html)`
`[ActionUsage](#ActionUsage())()`
Returns action usage.
`[SysMLLibrary.ConnectionDefinitionMetadataDefinition](SysMLLibrary.ConnectionDefinitionMetadataDefinition.html)`
`[ConnectionDefinition](#ConnectionDefinition())()`
Returns connection definition.
`[SysMLLibrary.ConnectionUsageMetadataDefinition](SysMLLibrary.ConnectionUsageMetadataDefinition.html)`
`[ConnectionUsage](#ConnectionUsage())()`
Returns connection usage.
`[SysMLLibrary.ConstraintUsageMetadataDefinition](SysMLLibrary.ConstraintUsageMetadataDefinition.html)`
`[ConstraintUsage](#ConstraintUsage())()`
Returns constraint usage.
`[SysMLLibrary.ControlNodeMetadataDefinition](SysMLLibrary.ControlNodeMetadataDefinition.html)`
`[ControlNode](#ControlNode())()`
Returns control node.
`[SysMLLibrary.DecisionNodeMetadataDefinition](SysMLLibrary.DecisionNodeMetadataDefinition.html)`
`[DecisionNode](#DecisionNode())()`
Returns decision node.
`[SysMLLibrary.EnumerationDefinitionMetadataDefinition](SysMLLibrary.EnumerationDefinitionMetadataDefinition.html)`
`[EnumerationDefinition](#EnumerationDefinition())()`
Returns enumeration definition.
`[SysMLLibrary.EnumerationUsageMetadataDefinition](SysMLLibrary.EnumerationUsageMetadataDefinition.html)`
`[EnumerationUsage](#EnumerationUsage())()`
Returns enumeration usage.
`[SysMLLibrary.FlowUsageMetadataDefinition](SysMLLibrary.FlowUsageMetadataDefinition.html)`
`[FlowUsage](#FlowUsage())()`
Returns flow usage.
`[SysMLLibrary.ForkNodeMetadataDefinition](SysMLLibrary.ForkNodeMetadataDefinition.html)`
`[ForkNode](#ForkNode())()`
Returns fork node.
`static [SysMLLibrary](SysMLLibrary.html)`
`[getInstance](#getInstance(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../../../../../nomagic/magicdraw/uml/BaseElement.html) element)`
Returns the library instance for the project that owns the given element.
`static [SysMLLibrary](SysMLLibrary.html)`
`[getInstanceByProject](#getInstanceByProject(com.dassault_systemes.modeler.foundation.project.ModelElementProject))([ModelElementProject](../../../foundation/project/ModelElementProject.html) project)`
Returns the library instance for the given project.
`protected final [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<com.dassault_systemes.modeler.kerml.libraries.TypeWrapper>`
`[getTypeWrappers](#getTypeWrappers())()`
Returns get type wrappers.
`[SysMLLibrary.IncludeUseCaseUsageMetadataDefinition](SysMLLibrary.IncludeUseCaseUsageMetadataDefinition.html)`
`[IncludeUseCaseUsage](#IncludeUseCaseUsage())()`
Returns include use case usage.
`boolean`
`[isSemantic](#isSemantic())()`
Returns whether this library is semantic.
`[SysMLLibrary.ItemDefinitionMetadataDefinition](SysMLLibrary.ItemDefinitionMetadataDefinition.html)`
`[ItemDefinition](#ItemDefinition())()`
Returns item definition.
`[SysMLLibrary.JoinNodeMetadataDefinition](SysMLLibrary.JoinNodeMetadataDefinition.html)`
`[JoinNode](#JoinNode())()`
Returns join node.
`[SysMLLibrary.MergeNodeMetadataDefinition](SysMLLibrary.MergeNodeMetadataDefinition.html)`
`[MergeNode](#MergeNode())()`
Returns merge node.
`[SysMLLibrary.MetadataDefinitionMetadataDefinition](SysMLLibrary.MetadataDefinitionMetadataDefinition.html)`
`[MetadataDefinition](#MetadataDefinition())()`
Returns metadata definition.
`[SysMLLibrary.OccurrenceDefinitionMetadataDefinition](SysMLLibrary.OccurrenceDefinitionMetadataDefinition.html)`
`[OccurrenceDefinition](#OccurrenceDefinition())()`
Returns occurrence definition.
`protected [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[packagesNames](#packagesNames())()`
Returns the names of the packages that belong to this library.
`[SysMLLibrary.PartDefinitionMetadataDefinition](SysMLLibrary.PartDefinitionMetadataDefinition.html)`
`[PartDefinition](#PartDefinition())()`
Returns part definition.
`[SysMLLibrary.PortDefinitionMetadataDefinition](SysMLLibrary.PortDefinitionMetadataDefinition.html)`
`[PortDefinition](#PortDefinition())()`
Returns port definition.
`[SysMLLibrary.PortUsageMetadataDefinition](SysMLLibrary.PortUsageMetadataDefinition.html)`
`[PortUsage](#PortUsage())()`
Returns port usage.
`[SysMLLibrary.ReferenceUsageMetadataDefinition](SysMLLibrary.ReferenceUsageMetadataDefinition.html)`
`[ReferenceUsage](#ReferenceUsage())()`
Returns reference usage.
`[SysMLLibrary.SendActionUsageMetadataDefinition](SysMLLibrary.SendActionUsageMetadataDefinition.html)`
`[SendActionUsage](#SendActionUsage())()`
Returns send action usage.
`[SysMLLibrary.StateDefinitionMetadataDefinition](SysMLLibrary.StateDefinitionMetadataDefinition.html)`
`[StateDefinition](#StateDefinition())()`
Returns state definition.
`[SysMLLibrary.StateUsageMetadataDefinition](SysMLLibrary.StateUsageMetadataDefinition.html)`
`[StateUsage](#StateUsage())()`
Returns state usage.
`[SysMLLibrary.TerminateActionUsageMetadataDefinition](SysMLLibrary.TerminateActionUsageMetadataDefinition.html)`
`[TerminateActionUsage](#TerminateActionUsage())()`
Returns terminate action usage.
`[SysMLLibrary.TransitionUsageMetadataDefinition](SysMLLibrary.TransitionUsageMetadataDefinition.html)`
`[TransitionUsage](#TransitionUsage())()`
Returns transition usage.
`[SysMLLibrary.UsageMetadataDefinition](SysMLLibrary.UsageMetadataDefinition.html)`
`[Usage](#Usage())()`
Returns usage.
`[SysMLLibrary.UseCaseDefinitionMetadataDefinition](SysMLLibrary.UseCaseDefinitionMetadataDefinition.html)`
`[UseCaseDefinition](#UseCaseDefinition())()`
Returns use case definition.
`[SysMLLibrary.ViewUsageMetadataDefinition](SysMLLibrary.ViewUsageMetadataDefinition.html)`
`[ViewUsage](#ViewUsage())()`
Returns view usage.
Methods inherited from class com.dassault_systemes.modeler.kerml.libraries.[AbstractLibrary](../../../kerml/libraries/AbstractLibrary.html)
`[findFunctionInLibrary](../../../kerml/libraries/AbstractLibrary.html#findFunctionInLibrary(java.lang.String)), [findLibraryPackage](../../../kerml/libraries/AbstractLibrary.html#findLibraryPackage(java.lang.String)), [findPackage](../../../kerml/libraries/AbstractLibrary.html#findPackage(java.lang.String,java.lang.String)), [getLibraryPackages](../../../kerml/libraries/AbstractLibrary.html#getLibraryPackages()), [getNamespace](../../../kerml/libraries/AbstractLibrary.html#getNamespace()), [initialized](../../../kerml/libraries/AbstractLibrary.html#initialized())`
Methods inherited from class com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService
`disposeService, getIfPresent, getOrCreateInstance, getOrCreateInstanceWithNullSupport, getReferencedProject`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
SysMLLibrary
public SysMLLibrary([ModelElementProject](../../../foundation/project/ModelElementProject.html) project)
Creates a new sys mllibrary instance.
Parameters:
`project` - the project
 ============ METHOD DETAIL ========== 
Method Details
getInstanceByProject
public static [SysMLLibrary](SysMLLibrary.html) getInstanceByProject([ModelElementProject](../../../foundation/project/ModelElementProject.html) project)
Returns the library instance for the given project.
Parameters:
`project` - the project
Returns:
get instance by project
getInstance
public static [SysMLLibrary](SysMLLibrary.html) getInstance([BaseElement](../../../../../nomagic/magicdraw/uml/BaseElement.html) element)
Returns the library instance for the project that owns the given element.
Parameters:
`element` - the element
Returns:
get instance
isSemantic
public boolean isSemantic()
Returns whether this library is semantic.
Specified by:
`[isSemantic](../../../kerml/libraries/AbstractLibrary.html#isSemantic())` in class `[AbstractLibrary](../../../kerml/libraries/AbstractLibrary.html)`
Returns:
`true` if semantic; `false` otherwise
packagesNames
protected [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> packagesNames()
Returns the names of the packages that belong to this library.
Specified by:
`[packagesNames](../../../kerml/libraries/AbstractLibrary.html#packagesNames())` in class `[AbstractLibrary](../../../kerml/libraries/AbstractLibrary.html)`
Returns:
packages names
AcceptActionUsage
public [SysMLLibrary.AcceptActionUsageMetadataDefinition](SysMLLibrary.AcceptActionUsageMetadataDefinition.html) AcceptActionUsage()
Returns accept action usage.
Returns:
accept action usage
ActionDefinition
public [SysMLLibrary.ActionDefinitionMetadataDefinition](SysMLLibrary.ActionDefinitionMetadataDefinition.html) ActionDefinition()
Returns action definition.
Returns:
action definition
ActionUsage
public [SysMLLibrary.ActionUsageMetadataDefinition](SysMLLibrary.ActionUsageMetadataDefinition.html) ActionUsage()
Returns action usage.
Returns:
action usage
ConnectionDefinition
public [SysMLLibrary.ConnectionDefinitionMetadataDefinition](SysMLLibrary.ConnectionDefinitionMetadataDefinition.html) ConnectionDefinition()
Returns connection definition.
Returns:
connection definition
ConnectionUsage
public [SysMLLibrary.ConnectionUsageMetadataDefinition](SysMLLibrary.ConnectionUsageMetadataDefinition.html) ConnectionUsage()
Returns connection usage.
Returns:
connection usage
ConstraintUsage
public [SysMLLibrary.ConstraintUsageMetadataDefinition](SysMLLibrary.ConstraintUsageMetadataDefinition.html) ConstraintUsage()
Returns constraint usage.
Returns:
constraint usage
ControlNode
public [SysMLLibrary.ControlNodeMetadataDefinition](SysMLLibrary.ControlNodeMetadataDefinition.html) ControlNode()
Returns control node.
Returns:
control node
DecisionNode
public [SysMLLibrary.DecisionNodeMetadataDefinition](SysMLLibrary.DecisionNodeMetadataDefinition.html) DecisionNode()
Returns decision node.
Returns:
decision node
EnumerationDefinition
public [SysMLLibrary.EnumerationDefinitionMetadataDefinition](SysMLLibrary.EnumerationDefinitionMetadataDefinition.html) EnumerationDefinition()
Returns enumeration definition.
Returns:
enumeration definition
EnumerationUsage
public [SysMLLibrary.EnumerationUsageMetadataDefinition](SysMLLibrary.EnumerationUsageMetadataDefinition.html) EnumerationUsage()
Returns enumeration usage.
Returns:
enumeration usage
FlowUsage
public [SysMLLibrary.FlowUsageMetadataDefinition](SysMLLibrary.FlowUsageMetadataDefinition.html) FlowUsage()
Returns flow usage.
Returns:
flow usage
ForkNode
public [SysMLLibrary.ForkNodeMetadataDefinition](SysMLLibrary.ForkNodeMetadataDefinition.html) ForkNode()
Returns fork node.
Returns:
fork node
IncludeUseCaseUsage
public [SysMLLibrary.IncludeUseCaseUsageMetadataDefinition](SysMLLibrary.IncludeUseCaseUsageMetadataDefinition.html) IncludeUseCaseUsage()
Returns include use case usage.
Returns:
include use case usage
ItemDefinition
public [SysMLLibrary.ItemDefinitionMetadataDefinition](SysMLLibrary.ItemDefinitionMetadataDefinition.html) ItemDefinition()
Returns item definition.
Returns:
item definition
JoinNode
public [SysMLLibrary.JoinNodeMetadataDefinition](SysMLLibrary.JoinNodeMetadataDefinition.html) JoinNode()
Returns join node.
Returns:
join node
MergeNode
public [SysMLLibrary.MergeNodeMetadataDefinition](SysMLLibrary.MergeNodeMetadataDefinition.html) MergeNode()
Returns merge node.
Returns:
merge node
MetadataDefinition
public [SysMLLibrary.MetadataDefinitionMetadataDefinition](SysMLLibrary.MetadataDefinitionMetadataDefinition.html) MetadataDefinition()
Returns metadata definition.
Returns:
metadata definition
OccurrenceDefinition
public [SysMLLibrary.OccurrenceDefinitionMetadataDefinition](SysMLLibrary.OccurrenceDefinitionMetadataDefinition.html) OccurrenceDefinition()
Returns occurrence definition.
Returns:
occurrence definition
PartDefinition
public [SysMLLibrary.PartDefinitionMetadataDefinition](SysMLLibrary.PartDefinitionMetadataDefinition.html) PartDefinition()
Returns part definition.
Returns:
part definition
PortDefinition
public [SysMLLibrary.PortDefinitionMetadataDefinition](SysMLLibrary.PortDefinitionMetadataDefinition.html) PortDefinition()
Returns port definition.
Returns:
port definition
PortUsage
public [SysMLLibrary.PortUsageMetadataDefinition](SysMLLibrary.PortUsageMetadataDefinition.html) PortUsage()
Returns port usage.
Returns:
port usage
ReferenceUsage
public [SysMLLibrary.ReferenceUsageMetadataDefinition](SysMLLibrary.ReferenceUsageMetadataDefinition.html) ReferenceUsage()
Returns reference usage.
Returns:
reference usage
SendActionUsage
public [SysMLLibrary.SendActionUsageMetadataDefinition](SysMLLibrary.SendActionUsageMetadataDefinition.html) SendActionUsage()
Returns send action usage.
Returns:
send action usage
StateDefinition
public [SysMLLibrary.StateDefinitionMetadataDefinition](SysMLLibrary.StateDefinitionMetadataDefinition.html) StateDefinition()
Returns state definition.
Returns:
state definition
StateUsage
public [SysMLLibrary.StateUsageMetadataDefinition](SysMLLibrary.StateUsageMetadataDefinition.html) StateUsage()
Returns state usage.
Returns:
state usage
TerminateActionUsage
public [SysMLLibrary.TerminateActionUsageMetadataDefinition](SysMLLibrary.TerminateActionUsageMetadataDefinition.html) TerminateActionUsage()
Returns terminate action usage.
Returns:
terminate action usage
TransitionUsage
public [SysMLLibrary.TransitionUsageMetadataDefinition](SysMLLibrary.TransitionUsageMetadataDefinition.html) TransitionUsage()
Returns transition usage.
Returns:
transition usage
Usage
public [SysMLLibrary.UsageMetadataDefinition](SysMLLibrary.UsageMetadataDefinition.html) Usage()
Returns usage.
Returns:
usage
UseCaseDefinition
public [SysMLLibrary.UseCaseDefinitionMetadataDefinition](SysMLLibrary.UseCaseDefinitionMetadataDefinition.html) UseCaseDefinition()
Returns use case definition.
Returns:
use case definition
ViewUsage
public [SysMLLibrary.ViewUsageMetadataDefinition](SysMLLibrary.ViewUsageMetadataDefinition.html) ViewUsage()
Returns view usage.
Returns:
view usage
getTypeWrappers
protected final [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<com.dassault_systemes.modeler.kerml.libraries.TypeWrapper> getTypeWrappers()
Returns get type wrappers.
Specified by:
`[getTypeWrappers](../../../kerml/libraries/AbstractLibrary.html#getTypeWrappers())` in class `[AbstractLibrary](../../../kerml/libraries/AbstractLibrary.html)`
Returns:
get type wrappers

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.sysml.libraries.standard</a></div>
<h1 class="title" title="Class SysMLLibrary">Class SysMLLibrary</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService&lt;<a href="../../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a>&gt;
<div class="inheritance"><a href="../../../kerml/libraries/AbstractLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries">com.dassault_systemes.modeler.kerml.libraries.AbstractLibrary</a>
<div class="inheritance">com.dassault_systemes.modeler.sysml.libraries.standard.SysMLLibrary</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.dassault_systemes.modeler.foundation.project.service.DisposableService</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">SysMLLibrary</span>
<span class="extends-implements">extends <a href="../../../kerml/libraries/AbstractLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries">AbstractLibrary</a></span></div>
<div class="block">Access helper for the sys ml standard library.</div>
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
<div class="col-second even-row-color"><code><a class="type-name-link" href="SysMLLibrary.AcceptActionUsageMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.AcceptActionUsageMetadataDefinition</a></code></div>
<div class="col-last even-row-color">
<div class="block">Wrapper for the accept action usage metadata definition library element.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="SysMLLibrary.ActionDefinitionMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.ActionDefinitionMetadataDefinition</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Wrapper for the action definition metadata definition library element.</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="SysMLLibrary.ActionUsageMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.ActionUsageMetadataDefinition</a></code></div>
<div class="col-last even-row-color">
<div class="block">Wrapper for the action usage metadata definition library element.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="SysMLLibrary.ConnectionDefinitionMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.ConnectionDefinitionMetadataDefinition</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Wrapper for the connection definition metadata definition library element.</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="SysMLLibrary.ConnectionUsageMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.ConnectionUsageMetadataDefinition</a></code></div>
<div class="col-last even-row-color">
<div class="block">Wrapper for the connection usage metadata definition library element.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="SysMLLibrary.ConstraintUsageMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.ConstraintUsageMetadataDefinition</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Wrapper for the constraint usage metadata definition library element.</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="SysMLLibrary.ControlNodeMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.ControlNodeMetadataDefinition</a></code></div>
<div class="col-last even-row-color">
<div class="block">Wrapper for the control node metadata definition library element.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="SysMLLibrary.DecisionNodeMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.DecisionNodeMetadataDefinition</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Wrapper for the decision node metadata definition library element.</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="SysMLLibrary.EnumerationDefinitionMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.EnumerationDefinitionMetadataDefinition</a></code></div>
<div class="col-last even-row-color">
<div class="block">Wrapper for the enumeration definition metadata definition library element.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="SysMLLibrary.EnumerationUsageMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.EnumerationUsageMetadataDefinition</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Wrapper for the enumeration usage metadata definition library element.</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="SysMLLibrary.FlowUsageMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.FlowUsageMetadataDefinition</a></code></div>
<div class="col-last even-row-color">
<div class="block">Wrapper for the flow usage metadata definition library element.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="SysMLLibrary.ForkNodeMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.ForkNodeMetadataDefinition</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Wrapper for the fork node metadata definition library element.</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="SysMLLibrary.IncludeUseCaseUsageMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.IncludeUseCaseUsageMetadataDefinition</a></code></div>
<div class="col-last even-row-color">
<div class="block">Wrapper for the include use case usage metadata definition library element.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="SysMLLibrary.ItemDefinitionMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.ItemDefinitionMetadataDefinition</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Wrapper for the item definition metadata definition library element.</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="SysMLLibrary.JoinNodeMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.JoinNodeMetadataDefinition</a></code></div>
<div class="col-last even-row-color">
<div class="block">Wrapper for the join node metadata definition library element.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="SysMLLibrary.MergeNodeMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.MergeNodeMetadataDefinition</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Wrapper for the merge node metadata definition library element.</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="SysMLLibrary.MetadataDefinitionMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.MetadataDefinitionMetadataDefinition</a></code></div>
<div class="col-last even-row-color">
<div class="block">Wrapper for the metadata definition metadata definition library element.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="SysMLLibrary.OccurrenceDefinitionMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.OccurrenceDefinitionMetadataDefinition</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Wrapper for the occurrence definition metadata definition library element.</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="SysMLLibrary.PartDefinitionMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.PartDefinitionMetadataDefinition</a></code></div>
<div class="col-last even-row-color">
<div class="block">Wrapper for the part definition metadata definition library element.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="SysMLLibrary.PortDefinitionMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.PortDefinitionMetadataDefinition</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Wrapper for the port definition metadata definition library element.</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="SysMLLibrary.PortUsageMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.PortUsageMetadataDefinition</a></code></div>
<div class="col-last even-row-color">
<div class="block">Wrapper for the port usage metadata definition library element.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="SysMLLibrary.ReferenceUsageMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.ReferenceUsageMetadataDefinition</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Wrapper for the reference usage metadata definition library element.</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="SysMLLibrary.SendActionUsageMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.SendActionUsageMetadataDefinition</a></code></div>
<div class="col-last even-row-color">
<div class="block">Wrapper for the send action usage metadata definition library element.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="SysMLLibrary.StateDefinitionMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.StateDefinitionMetadataDefinition</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Wrapper for the state definition metadata definition library element.</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="SysMLLibrary.StateUsageMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.StateUsageMetadataDefinition</a></code></div>
<div class="col-last even-row-color">
<div class="block">Wrapper for the state usage metadata definition library element.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="SysMLLibrary.TerminateActionUsageMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.TerminateActionUsageMetadataDefinition</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Wrapper for the terminate action usage metadata definition library element.</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="SysMLLibrary.TransitionUsageMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.TransitionUsageMetadataDefinition</a></code></div>
<div class="col-last even-row-color">
<div class="block">Wrapper for the transition usage metadata definition library element.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="SysMLLibrary.UsageMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.UsageMetadataDefinition</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Wrapper for the usage metadata definition library element.</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="SysMLLibrary.UseCaseDefinitionMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.UseCaseDefinitionMetadataDefinition</a></code></div>
<div class="col-last even-row-color">
<div class="block">Wrapper for the use case definition metadata definition library element.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="SysMLLibrary.ViewUsageMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.ViewUsageMetadataDefinition</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Wrapper for the view usage metadata definition library element.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.dassault_systemes.modeler.foundation.project.ModelElementProject)">SysMLLibrary</a><wbr/>(<a href="../../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new sys mllibrary instance.</div>
</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SysMLLibrary.AcceptActionUsageMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.AcceptActionUsageMetadataDefinition</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#AcceptActionUsage()">AcceptActionUsage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns accept action usage.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SysMLLibrary.ActionDefinitionMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.ActionDefinitionMetadataDefinition</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#ActionDefinition()">ActionDefinition</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns action definition.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SysMLLibrary.ActionUsageMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.ActionUsageMetadataDefinition</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#ActionUsage()">ActionUsage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns action usage.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SysMLLibrary.ConnectionDefinitionMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.ConnectionDefinitionMetadataDefinition</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#ConnectionDefinition()">ConnectionDefinition</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns connection definition.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SysMLLibrary.ConnectionUsageMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.ConnectionUsageMetadataDefinition</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#ConnectionUsage()">ConnectionUsage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns connection usage.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SysMLLibrary.ConstraintUsageMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.ConstraintUsageMetadataDefinition</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#ConstraintUsage()">ConstraintUsage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns constraint usage.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SysMLLibrary.ControlNodeMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.ControlNodeMetadataDefinition</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#ControlNode()">ControlNode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns control node.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SysMLLibrary.DecisionNodeMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.DecisionNodeMetadataDefinition</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#DecisionNode()">DecisionNode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns decision node.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SysMLLibrary.EnumerationDefinitionMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.EnumerationDefinitionMetadataDefinition</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#EnumerationDefinition()">EnumerationDefinition</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns enumeration definition.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SysMLLibrary.EnumerationUsageMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.EnumerationUsageMetadataDefinition</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#EnumerationUsage()">EnumerationUsage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns enumeration usage.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SysMLLibrary.FlowUsageMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.FlowUsageMetadataDefinition</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#FlowUsage()">FlowUsage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns flow usage.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SysMLLibrary.ForkNodeMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.ForkNodeMetadataDefinition</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#ForkNode()">ForkNode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns fork node.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="SysMLLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstance(com.nomagic.magicdraw.uml.BaseElement)">getInstance</a><wbr/>(<a href="../../../../../nomagic/magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the library instance for the project that owns the given element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="SysMLLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstanceByProject(com.dassault_systemes.modeler.foundation.project.ModelElementProject)">getInstanceByProject</a><wbr/>(<a href="../../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the library instance for the given project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a><wbr/>&lt;com.dassault_systemes.modeler.kerml.libraries.TypeWrapper&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTypeWrappers()">getTypeWrappers</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns get type wrappers.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SysMLLibrary.IncludeUseCaseUsageMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.IncludeUseCaseUsageMetadataDefinition</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#IncludeUseCaseUsage()">IncludeUseCaseUsage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns include use case usage.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isSemantic()">isSemantic</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns whether this library is semantic.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SysMLLibrary.ItemDefinitionMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.ItemDefinitionMetadataDefinition</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#ItemDefinition()">ItemDefinition</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns item definition.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SysMLLibrary.JoinNodeMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.JoinNodeMetadataDefinition</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#JoinNode()">JoinNode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns join node.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SysMLLibrary.MergeNodeMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.MergeNodeMetadataDefinition</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#MergeNode()">MergeNode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns merge node.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SysMLLibrary.MetadataDefinitionMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.MetadataDefinitionMetadataDefinition</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#MetadataDefinition()">MetadataDefinition</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns metadata definition.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SysMLLibrary.OccurrenceDefinitionMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.OccurrenceDefinitionMetadataDefinition</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#OccurrenceDefinition()">OccurrenceDefinition</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns occurrence definition.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#packagesNames()">packagesNames</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the names of the packages that belong to this library.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SysMLLibrary.PartDefinitionMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.PartDefinitionMetadataDefinition</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#PartDefinition()">PartDefinition</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns part definition.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SysMLLibrary.PortDefinitionMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.PortDefinitionMetadataDefinition</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#PortDefinition()">PortDefinition</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns port definition.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SysMLLibrary.PortUsageMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.PortUsageMetadataDefinition</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#PortUsage()">PortUsage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns port usage.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SysMLLibrary.ReferenceUsageMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.ReferenceUsageMetadataDefinition</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#ReferenceUsage()">ReferenceUsage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns reference usage.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SysMLLibrary.SendActionUsageMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.SendActionUsageMetadataDefinition</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#SendActionUsage()">SendActionUsage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns send action usage.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SysMLLibrary.StateDefinitionMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.StateDefinitionMetadataDefinition</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#StateDefinition()">StateDefinition</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns state definition.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SysMLLibrary.StateUsageMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.StateUsageMetadataDefinition</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#StateUsage()">StateUsage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns state usage.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SysMLLibrary.TerminateActionUsageMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.TerminateActionUsageMetadataDefinition</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#TerminateActionUsage()">TerminateActionUsage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns terminate action usage.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SysMLLibrary.TransitionUsageMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.TransitionUsageMetadataDefinition</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#TransitionUsage()">TransitionUsage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns transition usage.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SysMLLibrary.UsageMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.UsageMetadataDefinition</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#Usage()">Usage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns usage.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SysMLLibrary.UseCaseDefinitionMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.UseCaseDefinitionMetadataDefinition</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#UseCaseDefinition()">UseCaseDefinition</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns use case definition.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SysMLLibrary.ViewUsageMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.ViewUsageMetadataDefinition</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#ViewUsage()">ViewUsage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns view usage.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.libraries.AbstractLibrary">Methods inherited from class com.dassault_systemes.modeler.kerml.libraries.<a href="../../../kerml/libraries/AbstractLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries">AbstractLibrary</a></h3>
<code><a href="../../../kerml/libraries/AbstractLibrary.html#findFunctionInLibrary(java.lang.String)">findFunctionInLibrary</a>, <a href="../../../kerml/libraries/AbstractLibrary.html#findLibraryPackage(java.lang.String)">findLibraryPackage</a>, <a href="../../../kerml/libraries/AbstractLibrary.html#findPackage(java.lang.String,java.lang.String)">findPackage</a>, <a href="../../../kerml/libraries/AbstractLibrary.html#getLibraryPackages()">getLibraryPackages</a>, <a href="../../../kerml/libraries/AbstractLibrary.html#getNamespace()">getNamespace</a>, <a href="../../../kerml/libraries/AbstractLibrary.html#initialized()">initialized</a></code></div>
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
<h3>SysMLLibrary</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SysMLLibrary</span><wbr/><span class="parameters">(<a href="../../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project)</span></div>
<div class="block">Creates a new sys mllibrary instance.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - the project</dd>
</dl>
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="SysMLLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary</a></span> <span class="element-name">getInstanceByProject</span><wbr/><span class="parameters">(<a href="../../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project)</span></div>
<div class="block">Returns the library instance for the given project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - the project</dd>
<dt>Returns:</dt>
<dd>get instance by project</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInstance(com.nomagic.magicdraw.uml.BaseElement)">
<h3>getInstance</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="SysMLLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary</a></span> <span class="element-name">getInstance</span><wbr/><span class="parameters">(<a href="../../../../../nomagic/magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</span></div>
<div class="block">Returns the library instance for the project that owns the given element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element</dd>
<dt>Returns:</dt>
<dd>get instance</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSemantic()">
<h3>isSemantic</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isSemantic</span>()</div>
<div class="block">Returns whether this library is semantic.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../../kerml/libraries/AbstractLibrary.html#isSemantic()">isSemantic</a></code> in class <code><a href="../../../kerml/libraries/AbstractLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries">AbstractLibrary</a></code></dd>
<dt>Returns:</dt>
<dd><code>true</code> if semantic; <code>false</code> otherwise</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="packagesNames()">
<h3>packagesNames</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">packagesNames</span>()</div>
<div class="block">Returns the names of the packages that belong to this library.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../../kerml/libraries/AbstractLibrary.html#packagesNames()">packagesNames</a></code> in class <code><a href="../../../kerml/libraries/AbstractLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries">AbstractLibrary</a></code></dd>
<dt>Returns:</dt>
<dd>packages names</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="AcceptActionUsage()">
<h3>AcceptActionUsage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SysMLLibrary.AcceptActionUsageMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.AcceptActionUsageMetadataDefinition</a></span> <span class="element-name">AcceptActionUsage</span>()</div>
<div class="block">Returns accept action usage.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>accept action usage</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ActionDefinition()">
<h3>ActionDefinition</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SysMLLibrary.ActionDefinitionMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.ActionDefinitionMetadataDefinition</a></span> <span class="element-name">ActionDefinition</span>()</div>
<div class="block">Returns action definition.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>action definition</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ActionUsage()">
<h3>ActionUsage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SysMLLibrary.ActionUsageMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.ActionUsageMetadataDefinition</a></span> <span class="element-name">ActionUsage</span>()</div>
<div class="block">Returns action usage.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>action usage</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ConnectionDefinition()">
<h3>ConnectionDefinition</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SysMLLibrary.ConnectionDefinitionMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.ConnectionDefinitionMetadataDefinition</a></span> <span class="element-name">ConnectionDefinition</span>()</div>
<div class="block">Returns connection definition.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>connection definition</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ConnectionUsage()">
<h3>ConnectionUsage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SysMLLibrary.ConnectionUsageMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.ConnectionUsageMetadataDefinition</a></span> <span class="element-name">ConnectionUsage</span>()</div>
<div class="block">Returns connection usage.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>connection usage</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ConstraintUsage()">
<h3>ConstraintUsage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SysMLLibrary.ConstraintUsageMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.ConstraintUsageMetadataDefinition</a></span> <span class="element-name">ConstraintUsage</span>()</div>
<div class="block">Returns constraint usage.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>constraint usage</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ControlNode()">
<h3>ControlNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SysMLLibrary.ControlNodeMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.ControlNodeMetadataDefinition</a></span> <span class="element-name">ControlNode</span>()</div>
<div class="block">Returns control node.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>control node</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DecisionNode()">
<h3>DecisionNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SysMLLibrary.DecisionNodeMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.DecisionNodeMetadataDefinition</a></span> <span class="element-name">DecisionNode</span>()</div>
<div class="block">Returns decision node.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>decision node</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="EnumerationDefinition()">
<h3>EnumerationDefinition</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SysMLLibrary.EnumerationDefinitionMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.EnumerationDefinitionMetadataDefinition</a></span> <span class="element-name">EnumerationDefinition</span>()</div>
<div class="block">Returns enumeration definition.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>enumeration definition</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="EnumerationUsage()">
<h3>EnumerationUsage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SysMLLibrary.EnumerationUsageMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.EnumerationUsageMetadataDefinition</a></span> <span class="element-name">EnumerationUsage</span>()</div>
<div class="block">Returns enumeration usage.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>enumeration usage</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="FlowUsage()">
<h3>FlowUsage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SysMLLibrary.FlowUsageMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.FlowUsageMetadataDefinition</a></span> <span class="element-name">FlowUsage</span>()</div>
<div class="block">Returns flow usage.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>flow usage</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ForkNode()">
<h3>ForkNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SysMLLibrary.ForkNodeMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.ForkNodeMetadataDefinition</a></span> <span class="element-name">ForkNode</span>()</div>
<div class="block">Returns fork node.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>fork node</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="IncludeUseCaseUsage()">
<h3>IncludeUseCaseUsage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SysMLLibrary.IncludeUseCaseUsageMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.IncludeUseCaseUsageMetadataDefinition</a></span> <span class="element-name">IncludeUseCaseUsage</span>()</div>
<div class="block">Returns include use case usage.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>include use case usage</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ItemDefinition()">
<h3>ItemDefinition</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SysMLLibrary.ItemDefinitionMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.ItemDefinitionMetadataDefinition</a></span> <span class="element-name">ItemDefinition</span>()</div>
<div class="block">Returns item definition.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>item definition</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="JoinNode()">
<h3>JoinNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SysMLLibrary.JoinNodeMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.JoinNodeMetadataDefinition</a></span> <span class="element-name">JoinNode</span>()</div>
<div class="block">Returns join node.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>join node</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="MergeNode()">
<h3>MergeNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SysMLLibrary.MergeNodeMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.MergeNodeMetadataDefinition</a></span> <span class="element-name">MergeNode</span>()</div>
<div class="block">Returns merge node.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>merge node</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="MetadataDefinition()">
<h3>MetadataDefinition</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SysMLLibrary.MetadataDefinitionMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.MetadataDefinitionMetadataDefinition</a></span> <span class="element-name">MetadataDefinition</span>()</div>
<div class="block">Returns metadata definition.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>metadata definition</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="OccurrenceDefinition()">
<h3>OccurrenceDefinition</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SysMLLibrary.OccurrenceDefinitionMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.OccurrenceDefinitionMetadataDefinition</a></span> <span class="element-name">OccurrenceDefinition</span>()</div>
<div class="block">Returns occurrence definition.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>occurrence definition</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PartDefinition()">
<h3>PartDefinition</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SysMLLibrary.PartDefinitionMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.PartDefinitionMetadataDefinition</a></span> <span class="element-name">PartDefinition</span>()</div>
<div class="block">Returns part definition.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>part definition</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PortDefinition()">
<h3>PortDefinition</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SysMLLibrary.PortDefinitionMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.PortDefinitionMetadataDefinition</a></span> <span class="element-name">PortDefinition</span>()</div>
<div class="block">Returns port definition.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>port definition</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PortUsage()">
<h3>PortUsage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SysMLLibrary.PortUsageMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.PortUsageMetadataDefinition</a></span> <span class="element-name">PortUsage</span>()</div>
<div class="block">Returns port usage.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>port usage</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ReferenceUsage()">
<h3>ReferenceUsage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SysMLLibrary.ReferenceUsageMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.ReferenceUsageMetadataDefinition</a></span> <span class="element-name">ReferenceUsage</span>()</div>
<div class="block">Returns reference usage.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>reference usage</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SendActionUsage()">
<h3>SendActionUsage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SysMLLibrary.SendActionUsageMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.SendActionUsageMetadataDefinition</a></span> <span class="element-name">SendActionUsage</span>()</div>
<div class="block">Returns send action usage.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>send action usage</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="StateDefinition()">
<h3>StateDefinition</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SysMLLibrary.StateDefinitionMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.StateDefinitionMetadataDefinition</a></span> <span class="element-name">StateDefinition</span>()</div>
<div class="block">Returns state definition.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>state definition</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="StateUsage()">
<h3>StateUsage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SysMLLibrary.StateUsageMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.StateUsageMetadataDefinition</a></span> <span class="element-name">StateUsage</span>()</div>
<div class="block">Returns state usage.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>state usage</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TerminateActionUsage()">
<h3>TerminateActionUsage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SysMLLibrary.TerminateActionUsageMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.TerminateActionUsageMetadataDefinition</a></span> <span class="element-name">TerminateActionUsage</span>()</div>
<div class="block">Returns terminate action usage.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>terminate action usage</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TransitionUsage()">
<h3>TransitionUsage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SysMLLibrary.TransitionUsageMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.TransitionUsageMetadataDefinition</a></span> <span class="element-name">TransitionUsage</span>()</div>
<div class="block">Returns transition usage.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>transition usage</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="Usage()">
<h3>Usage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SysMLLibrary.UsageMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.UsageMetadataDefinition</a></span> <span class="element-name">Usage</span>()</div>
<div class="block">Returns usage.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>usage</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="UseCaseDefinition()">
<h3>UseCaseDefinition</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SysMLLibrary.UseCaseDefinitionMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.UseCaseDefinitionMetadataDefinition</a></span> <span class="element-name">UseCaseDefinition</span>()</div>
<div class="block">Returns use case definition.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>use case definition</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ViewUsage()">
<h3>ViewUsage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SysMLLibrary.ViewUsageMetadataDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">SysMLLibrary.ViewUsageMetadataDefinition</a></span> <span class="element-name">ViewUsage</span>()</div>
<div class="block">Returns view usage.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>view usage</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTypeWrappers()">
<h3>getTypeWrappers</h3>
<div class="member-signature"><span class="modifiers">protected final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;com.dassault_systemes.modeler.kerml.libraries.TypeWrapper&gt;</span> <span class="element-name">getTypeWrappers</span>()</div>
<div class="block">Returns get type wrappers.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../../kerml/libraries/AbstractLibrary.html#getTypeWrappers()">getTypeWrappers</a></code> in class <code><a href="../../../kerml/libraries/AbstractLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries">AbstractLibrary</a></code></dd>
<dt>Returns:</dt>
<dd>get type wrappers</dd>
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
