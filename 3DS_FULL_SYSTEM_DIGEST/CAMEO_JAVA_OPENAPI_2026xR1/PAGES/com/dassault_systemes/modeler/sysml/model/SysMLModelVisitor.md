# JAVA OPENAPI: SysMLModelVisitor (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/sysml/model/SysMLModelVisitor.html
- source_path: `com/dassault_systemes/modeler/sysml/model/SysMLModelVisitor.html`
- source_sha256: `e4288b862a7796e6f4c5c0260b92b8849d90a49f0d61064d801f9c7f59c78761`
- captured_utc: `2026-07-14T16:45:03.404048+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.sysml.model](package-summary.html)

## Interface SysMLModelVisitor<C extends [SysMLVisitorContext](SysMLVisitorContext.html)>

Type Parameters:
`C` - the type of the visitor context

All Superinterfaces:
`[AbstractVisitor](../../../../nomagic/magicdraw/uml/AbstractVisitor.html)`, `[KerMLModelVisitor](../../kerml/model/KerMLModelVisitor.html)<C>`

All Known Subinterfaces:
`[SysMLModelHierarchyVisitor](SysMLModelHierarchyVisitor.html)<C>`

@OpenApiAllpublic interfaceSysMLModelVisitor<C extends [SysMLVisitorContext](SysMLVisitorContext.html)>extends [KerMLModelVisitor](../../kerml/model/KerMLModelVisitor.html)<C>

This interface extends KerMLModelVisitor to provide a visitor pattern implementation
 for traversing SysML model elements.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsDefault Methods
Modifier and Type
Method
Description
`default [C](SysMLModelVisitor.html)`
`[createVisitorContext](#createVisitorContext())()`
Creates a new visitor context.
`void`
`[visitAcceptActionUsage](#visitAcceptActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.AcceptActionUsage,C))([AcceptActionUsage](sysml/AcceptActionUsage.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`AcceptActionUsage`](sysml/AcceptActionUsage.html).
`void`
`[visitActionDefinition](#visitActionDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ActionDefinition,C))([ActionDefinition](sysml/ActionDefinition.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`ActionDefinition`](sysml/ActionDefinition.html).
`void`
`[visitActionUsage](#visitActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.ActionUsage,C))([ActionUsage](sysml/ActionUsage.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`ActionUsage`](sysml/ActionUsage.html).
`void`
`[visitActorMembership](#visitActorMembership(com.dassault_systemes.modeler.sysml.model.sysml.ActorMembership,C))([ActorMembership](sysml/ActorMembership.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`ActorMembership`](sysml/ActorMembership.html).
`void`
`[visitAllocationDefinition](#visitAllocationDefinition(com.dassault_systemes.modeler.sysml.model.sysml.AllocationDefinition,C))([AllocationDefinition](sysml/AllocationDefinition.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`AllocationDefinition`](sysml/AllocationDefinition.html).
`void`
`[visitAllocationUsage](#visitAllocationUsage(com.dassault_systemes.modeler.sysml.model.sysml.AllocationUsage,C))([AllocationUsage](sysml/AllocationUsage.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`AllocationUsage`](sysml/AllocationUsage.html).
`void`
`[visitAnalysisCaseDefinition](#visitAnalysisCaseDefinition(com.dassault_systemes.modeler.sysml.model.sysml.AnalysisCaseDefinition,C))([AnalysisCaseDefinition](sysml/AnalysisCaseDefinition.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`AnalysisCaseDefinition`](sysml/AnalysisCaseDefinition.html).
`void`
`[visitAnalysisCaseUsage](#visitAnalysisCaseUsage(com.dassault_systemes.modeler.sysml.model.sysml.AnalysisCaseUsage,C))([AnalysisCaseUsage](sysml/AnalysisCaseUsage.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`AnalysisCaseUsage`](sysml/AnalysisCaseUsage.html).
`void`
`[visitAssertConstraintUsage](#visitAssertConstraintUsage(com.dassault_systemes.modeler.sysml.model.sysml.AssertConstraintUsage,C))([AssertConstraintUsage](sysml/AssertConstraintUsage.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`AssertConstraintUsage`](sysml/AssertConstraintUsage.html).
`void`
`[visitAssignmentActionUsage](#visitAssignmentActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.AssignmentActionUsage,C))([AssignmentActionUsage](sysml/AssignmentActionUsage.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`AssignmentActionUsage`](sysml/AssignmentActionUsage.html).
`void`
`[visitAttributeDefinition](#visitAttributeDefinition(com.dassault_systemes.modeler.sysml.model.sysml.AttributeDefinition,C))([AttributeDefinition](sysml/AttributeDefinition.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`AttributeDefinition`](sysml/AttributeDefinition.html).
`void`
`[visitAttributeUsage](#visitAttributeUsage(com.dassault_systemes.modeler.sysml.model.sysml.AttributeUsage,C))([AttributeUsage](sysml/AttributeUsage.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`AttributeUsage`](sysml/AttributeUsage.html).
`void`
`[visitBindingConnectorAsUsage](#visitBindingConnectorAsUsage(com.dassault_systemes.modeler.sysml.model.sysml.BindingConnectorAsUsage,C))([BindingConnectorAsUsage](sysml/BindingConnectorAsUsage.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`BindingConnectorAsUsage`](sysml/BindingConnectorAsUsage.html).
`void`
`[visitCalculationDefinition](#visitCalculationDefinition(com.dassault_systemes.modeler.sysml.model.sysml.CalculationDefinition,C))([CalculationDefinition](sysml/CalculationDefinition.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`CalculationDefinition`](sysml/CalculationDefinition.html).
`void`
`[visitCalculationUsage](#visitCalculationUsage(com.dassault_systemes.modeler.sysml.model.sysml.CalculationUsage,C))([CalculationUsage](sysml/CalculationUsage.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`CalculationUsage`](sysml/CalculationUsage.html).
`void`
`[visitCaseDefinition](#visitCaseDefinition(com.dassault_systemes.modeler.sysml.model.sysml.CaseDefinition,C))([CaseDefinition](sysml/CaseDefinition.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`CaseDefinition`](sysml/CaseDefinition.html).
`void`
`[visitCaseUsage](#visitCaseUsage(com.dassault_systemes.modeler.sysml.model.sysml.CaseUsage,C))([CaseUsage](sysml/CaseUsage.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`CaseUsage`](sysml/CaseUsage.html).
`void`
`[visitConcernDefinition](#visitConcernDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ConcernDefinition,C))([ConcernDefinition](sysml/ConcernDefinition.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`ConcernDefinition`](sysml/ConcernDefinition.html).
`void`
`[visitConcernUsage](#visitConcernUsage(com.dassault_systemes.modeler.sysml.model.sysml.ConcernUsage,C))([ConcernUsage](sysml/ConcernUsage.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`ConcernUsage`](sysml/ConcernUsage.html).
`void`
`[visitConjugatedPortDefinition](#visitConjugatedPortDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ConjugatedPortDefinition,C))([ConjugatedPortDefinition](sysml/ConjugatedPortDefinition.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`ConjugatedPortDefinition`](sysml/ConjugatedPortDefinition.html).
`void`
`[visitConjugatedPortTyping](#visitConjugatedPortTyping(com.dassault_systemes.modeler.sysml.model.sysml.ConjugatedPortTyping,C))([ConjugatedPortTyping](sysml/ConjugatedPortTyping.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`ConjugatedPortTyping`](sysml/ConjugatedPortTyping.html).
`void`
`[visitConnectionDefinition](#visitConnectionDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ConnectionDefinition,C))([ConnectionDefinition](sysml/ConnectionDefinition.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`ConnectionDefinition`](sysml/ConnectionDefinition.html).
`void`
`[visitConnectionUsage](#visitConnectionUsage(com.dassault_systemes.modeler.sysml.model.sysml.ConnectionUsage,C))([ConnectionUsage](sysml/ConnectionUsage.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`ConnectionUsage`](sysml/ConnectionUsage.html).
`void`
`[visitConnectorAsUsage](#visitConnectorAsUsage(com.dassault_systemes.modeler.sysml.model.sysml.ConnectorAsUsage,C))([ConnectorAsUsage](sysml/ConnectorAsUsage.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`ConnectorAsUsage`](sysml/ConnectorAsUsage.html).
`void`
`[visitConstraintDefinition](#visitConstraintDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ConstraintDefinition,C))([ConstraintDefinition](sysml/ConstraintDefinition.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`ConstraintDefinition`](sysml/ConstraintDefinition.html).
`void`
`[visitConstraintUsage](#visitConstraintUsage(com.dassault_systemes.modeler.sysml.model.sysml.ConstraintUsage,C))([ConstraintUsage](sysml/ConstraintUsage.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`ConstraintUsage`](sysml/ConstraintUsage.html).
`void`
`[visitControlNode](#visitControlNode(com.dassault_systemes.modeler.sysml.model.sysml.ControlNode,C))([ControlNode](sysml/ControlNode.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`ControlNode`](sysml/ControlNode.html).
`void`
`[visitDecisionNode](#visitDecisionNode(com.dassault_systemes.modeler.sysml.model.sysml.DecisionNode,C))([DecisionNode](sysml/DecisionNode.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`DecisionNode`](sysml/DecisionNode.html).
`void`
`[visitDefinition](#visitDefinition(com.dassault_systemes.modeler.sysml.model.sysml.Definition,C))([Definition](sysml/Definition.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`Definition`](sysml/Definition.html).
`void`
`[visitEnumerationDefinition](#visitEnumerationDefinition(com.dassault_systemes.modeler.sysml.model.sysml.EnumerationDefinition,C))([EnumerationDefinition](sysml/EnumerationDefinition.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`EnumerationDefinition`](sysml/EnumerationDefinition.html).
`void`
`[visitEnumerationUsage](#visitEnumerationUsage(com.dassault_systemes.modeler.sysml.model.sysml.EnumerationUsage,C))([EnumerationUsage](sysml/EnumerationUsage.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`EnumerationUsage`](sysml/EnumerationUsage.html).
`void`
`[visitEventOccurrenceUsage](#visitEventOccurrenceUsage(com.dassault_systemes.modeler.sysml.model.sysml.EventOccurrenceUsage,C))([EventOccurrenceUsage](sysml/EventOccurrenceUsage.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`EventOccurrenceUsage`](sysml/EventOccurrenceUsage.html).
`void`
`[visitExhibitStateUsage](#visitExhibitStateUsage(com.dassault_systemes.modeler.sysml.model.sysml.ExhibitStateUsage,C))([ExhibitStateUsage](sysml/ExhibitStateUsage.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`ExhibitStateUsage`](sysml/ExhibitStateUsage.html).
`void`
`[visitExpose](#visitExpose(com.dassault_systemes.modeler.sysml.model.sysml.Expose,C))([Expose](sysml/Expose.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`Expose`](sysml/Expose.html).
`void`
`[visitFlowDefinition](#visitFlowDefinition(com.dassault_systemes.modeler.sysml.model.sysml.FlowDefinition,C))([FlowDefinition](sysml/FlowDefinition.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`FlowDefinition`](sysml/FlowDefinition.html).
`void`
`[visitFlowUsage](#visitFlowUsage(com.dassault_systemes.modeler.sysml.model.sysml.FlowUsage,C))([FlowUsage](sysml/FlowUsage.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`FlowUsage`](sysml/FlowUsage.html).
`void`
`[visitForkNode](#visitForkNode(com.dassault_systemes.modeler.sysml.model.sysml.ForkNode,C))([ForkNode](sysml/ForkNode.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`ForkNode`](sysml/ForkNode.html).
`void`
`[visitForLoopActionUsage](#visitForLoopActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.ForLoopActionUsage,C))([ForLoopActionUsage](sysml/ForLoopActionUsage.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`ForLoopActionUsage`](sysml/ForLoopActionUsage.html).
`void`
`[visitFramedConcernMembership](#visitFramedConcernMembership(com.dassault_systemes.modeler.sysml.model.sysml.FramedConcernMembership,C))([FramedConcernMembership](sysml/FramedConcernMembership.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`FramedConcernMembership`](sysml/FramedConcernMembership.html).
`void`
`[visitIfActionUsage](#visitIfActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.IfActionUsage,C))([IfActionUsage](sysml/IfActionUsage.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`IfActionUsage`](sysml/IfActionUsage.html).
`void`
`[visitIncludeUseCaseUsage](#visitIncludeUseCaseUsage(com.dassault_systemes.modeler.sysml.model.sysml.IncludeUseCaseUsage,C))([IncludeUseCaseUsage](sysml/IncludeUseCaseUsage.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`IncludeUseCaseUsage`](sysml/IncludeUseCaseUsage.html).
`void`
`[visitInterfaceDefinition](#visitInterfaceDefinition(com.dassault_systemes.modeler.sysml.model.sysml.InterfaceDefinition,C))([InterfaceDefinition](sysml/InterfaceDefinition.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`InterfaceDefinition`](sysml/InterfaceDefinition.html).
`void`
`[visitInterfaceUsage](#visitInterfaceUsage(com.dassault_systemes.modeler.sysml.model.sysml.InterfaceUsage,C))([InterfaceUsage](sysml/InterfaceUsage.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`InterfaceUsage`](sysml/InterfaceUsage.html).
`void`
`[visitItemDefinition](#visitItemDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ItemDefinition,C))([ItemDefinition](sysml/ItemDefinition.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`ItemDefinition`](sysml/ItemDefinition.html).
`void`
`[visitItemUsage](#visitItemUsage(com.dassault_systemes.modeler.sysml.model.sysml.ItemUsage,C))([ItemUsage](sysml/ItemUsage.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`ItemUsage`](sysml/ItemUsage.html).
`void`
`[visitJoinNode](#visitJoinNode(com.dassault_systemes.modeler.sysml.model.sysml.JoinNode,C))([JoinNode](sysml/JoinNode.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`JoinNode`](sysml/JoinNode.html).
`void`
`[visitLoopActionUsage](#visitLoopActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.LoopActionUsage,C))([LoopActionUsage](sysml/LoopActionUsage.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`LoopActionUsage`](sysml/LoopActionUsage.html).
`void`
`[visitMembershipExpose](#visitMembershipExpose(com.dassault_systemes.modeler.sysml.model.sysml.MembershipExpose,C))([MembershipExpose](sysml/MembershipExpose.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`MembershipExpose`](sysml/MembershipExpose.html).
`void`
`[visitMergeNode](#visitMergeNode(com.dassault_systemes.modeler.sysml.model.sysml.MergeNode,C))([MergeNode](sysml/MergeNode.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`MergeNode`](sysml/MergeNode.html).
`void`
`[visitMetadataDefinition](#visitMetadataDefinition(com.dassault_systemes.modeler.sysml.model.sysml.MetadataDefinition,C))([MetadataDefinition](sysml/MetadataDefinition.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`MetadataDefinition`](sysml/MetadataDefinition.html).
`void`
`[visitMetadataUsage](#visitMetadataUsage(com.dassault_systemes.modeler.sysml.model.sysml.MetadataUsage,C))([MetadataUsage](sysml/MetadataUsage.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`MetadataUsage`](sysml/MetadataUsage.html).
`void`
`[visitNamespaceExpose](#visitNamespaceExpose(com.dassault_systemes.modeler.sysml.model.sysml.NamespaceExpose,C))([NamespaceExpose](sysml/NamespaceExpose.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`NamespaceExpose`](sysml/NamespaceExpose.html).
`void`
`[visitObjectiveMembership](#visitObjectiveMembership(com.dassault_systemes.modeler.sysml.model.sysml.ObjectiveMembership,C))([ObjectiveMembership](sysml/ObjectiveMembership.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`ObjectiveMembership`](sysml/ObjectiveMembership.html).
`void`
`[visitOccurrenceDefinition](#visitOccurrenceDefinition(com.dassault_systemes.modeler.sysml.model.sysml.OccurrenceDefinition,C))([OccurrenceDefinition](sysml/OccurrenceDefinition.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`OccurrenceDefinition`](sysml/OccurrenceDefinition.html).
`void`
`[visitOccurrenceUsage](#visitOccurrenceUsage(com.dassault_systemes.modeler.sysml.model.sysml.OccurrenceUsage,C))([OccurrenceUsage](sysml/OccurrenceUsage.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`OccurrenceUsage`](sysml/OccurrenceUsage.html).
`void`
`[visitPartDefinition](#visitPartDefinition(com.dassault_systemes.modeler.sysml.model.sysml.PartDefinition,C))([PartDefinition](sysml/PartDefinition.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`PartDefinition`](sysml/PartDefinition.html).
`void`
`[visitPartUsage](#visitPartUsage(com.dassault_systemes.modeler.sysml.model.sysml.PartUsage,C))([PartUsage](sysml/PartUsage.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`PartUsage`](sysml/PartUsage.html).
`void`
`[visitPerformActionUsage](#visitPerformActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.PerformActionUsage,C))([PerformActionUsage](sysml/PerformActionUsage.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`PerformActionUsage`](sysml/PerformActionUsage.html).
`void`
`[visitPortConjugation](#visitPortConjugation(com.dassault_systemes.modeler.sysml.model.sysml.PortConjugation,C))([PortConjugation](sysml/PortConjugation.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`PortConjugation`](sysml/PortConjugation.html).
`void`
`[visitPortDefinition](#visitPortDefinition(com.dassault_systemes.modeler.sysml.model.sysml.PortDefinition,C))([PortDefinition](sysml/PortDefinition.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`PortDefinition`](sysml/PortDefinition.html).
`void`
`[visitPortUsage](#visitPortUsage(com.dassault_systemes.modeler.sysml.model.sysml.PortUsage,C))([PortUsage](sysml/PortUsage.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`PortUsage`](sysml/PortUsage.html).
`void`
`[visitReferenceUsage](#visitReferenceUsage(com.dassault_systemes.modeler.sysml.model.sysml.ReferenceUsage,C))([ReferenceUsage](sysml/ReferenceUsage.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`ReferenceUsage`](sysml/ReferenceUsage.html).
`void`
`[visitRenderingDefinition](#visitRenderingDefinition(com.dassault_systemes.modeler.sysml.model.sysml.RenderingDefinition,C))([RenderingDefinition](sysml/RenderingDefinition.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`RenderingDefinition`](sysml/RenderingDefinition.html).
`void`
`[visitRenderingUsage](#visitRenderingUsage(com.dassault_systemes.modeler.sysml.model.sysml.RenderingUsage,C))([RenderingUsage](sysml/RenderingUsage.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`RenderingUsage`](sysml/RenderingUsage.html).
`void`
`[visitRequirementConstraintMembership](#visitRequirementConstraintMembership(com.dassault_systemes.modeler.sysml.model.sysml.RequirementConstraintMembership,C))([RequirementConstraintMembership](sysml/RequirementConstraintMembership.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`RequirementConstraintMembership`](sysml/RequirementConstraintMembership.html).
`void`
`[visitRequirementDefinition](#visitRequirementDefinition(com.dassault_systemes.modeler.sysml.model.sysml.RequirementDefinition,C))([RequirementDefinition](sysml/RequirementDefinition.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`RequirementDefinition`](sysml/RequirementDefinition.html).
`void`
`[visitRequirementUsage](#visitRequirementUsage(com.dassault_systemes.modeler.sysml.model.sysml.RequirementUsage,C))([RequirementUsage](sysml/RequirementUsage.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`RequirementUsage`](sysml/RequirementUsage.html).
`void`
`[visitRequirementVerificationMembership](#visitRequirementVerificationMembership(com.dassault_systemes.modeler.sysml.model.sysml.RequirementVerificationMembership,C))([RequirementVerificationMembership](sysml/RequirementVerificationMembership.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`RequirementVerificationMembership`](sysml/RequirementVerificationMembership.html).
`void`
`[visitSatisfyRequirementUsage](#visitSatisfyRequirementUsage(com.dassault_systemes.modeler.sysml.model.sysml.SatisfyRequirementUsage,C))([SatisfyRequirementUsage](sysml/SatisfyRequirementUsage.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`SatisfyRequirementUsage`](sysml/SatisfyRequirementUsage.html).
`void`
`[visitSendActionUsage](#visitSendActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.SendActionUsage,C))([SendActionUsage](sysml/SendActionUsage.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`SendActionUsage`](sysml/SendActionUsage.html).
`void`
`[visitStakeholderMembership](#visitStakeholderMembership(com.dassault_systemes.modeler.sysml.model.sysml.StakeholderMembership,C))([StakeholderMembership](sysml/StakeholderMembership.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`StakeholderMembership`](sysml/StakeholderMembership.html).
`void`
`[visitStateDefinition](#visitStateDefinition(com.dassault_systemes.modeler.sysml.model.sysml.StateDefinition,C))([StateDefinition](sysml/StateDefinition.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`StateDefinition`](sysml/StateDefinition.html).
`void`
`[visitStateSubactionMembership](#visitStateSubactionMembership(com.dassault_systemes.modeler.sysml.model.sysml.StateSubactionMembership,C))([StateSubactionMembership](sysml/StateSubactionMembership.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`StateSubactionMembership`](sysml/StateSubactionMembership.html).
`void`
`[visitStateUsage](#visitStateUsage(com.dassault_systemes.modeler.sysml.model.sysml.StateUsage,C))([StateUsage](sysml/StateUsage.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`StateUsage`](sysml/StateUsage.html).
`void`
`[visitSubjectMembership](#visitSubjectMembership(com.dassault_systemes.modeler.sysml.model.sysml.SubjectMembership,C))([SubjectMembership](sysml/SubjectMembership.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`SubjectMembership`](sysml/SubjectMembership.html).
`void`
`[visitSuccessionAsUsage](#visitSuccessionAsUsage(com.dassault_systemes.modeler.sysml.model.sysml.SuccessionAsUsage,C))([SuccessionAsUsage](sysml/SuccessionAsUsage.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`SuccessionAsUsage`](sysml/SuccessionAsUsage.html).
`void`
`[visitSuccessionFlowUsage](#visitSuccessionFlowUsage(com.dassault_systemes.modeler.sysml.model.sysml.SuccessionFlowUsage,C))([SuccessionFlowUsage](sysml/SuccessionFlowUsage.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`SuccessionFlowUsage`](sysml/SuccessionFlowUsage.html).
`void`
`[visitTerminateActionUsage](#visitTerminateActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.TerminateActionUsage,C))([TerminateActionUsage](sysml/TerminateActionUsage.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`TerminateActionUsage`](sysml/TerminateActionUsage.html).
`void`
`[visitTransitionFeatureMembership](#visitTransitionFeatureMembership(com.dassault_systemes.modeler.sysml.model.sysml.TransitionFeatureMembership,C))([TransitionFeatureMembership](sysml/TransitionFeatureMembership.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`TransitionFeatureMembership`](sysml/TransitionFeatureMembership.html).
`void`
`[visitTransitionUsage](#visitTransitionUsage(com.dassault_systemes.modeler.sysml.model.sysml.TransitionUsage,C))([TransitionUsage](sysml/TransitionUsage.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`TransitionUsage`](sysml/TransitionUsage.html).
`void`
`[visitTriggerInvocationExpression](#visitTriggerInvocationExpression(com.dassault_systemes.modeler.sysml.model.sysml.TriggerInvocationExpression,C))([TriggerInvocationExpression](sysml/TriggerInvocationExpression.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`TriggerInvocationExpression`](sysml/TriggerInvocationExpression.html).
`void`
`[visitUsage](#visitUsage(com.dassault_systemes.modeler.sysml.model.sysml.Usage,C))([Usage](sysml/Usage.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`Usage`](sysml/Usage.html).
`void`
`[visitUseCaseDefinition](#visitUseCaseDefinition(com.dassault_systemes.modeler.sysml.model.sysml.UseCaseDefinition,C))([UseCaseDefinition](sysml/UseCaseDefinition.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`UseCaseDefinition`](sysml/UseCaseDefinition.html).
`void`
`[visitUseCaseUsage](#visitUseCaseUsage(com.dassault_systemes.modeler.sysml.model.sysml.UseCaseUsage,C))([UseCaseUsage](sysml/UseCaseUsage.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`UseCaseUsage`](sysml/UseCaseUsage.html).
`void`
`[visitVariantMembership](#visitVariantMembership(com.dassault_systemes.modeler.sysml.model.sysml.VariantMembership,C))([VariantMembership](sysml/VariantMembership.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`VariantMembership`](sysml/VariantMembership.html).
`void`
`[visitVerificationCaseDefinition](#visitVerificationCaseDefinition(com.dassault_systemes.modeler.sysml.model.sysml.VerificationCaseDefinition,C))([VerificationCaseDefinition](sysml/VerificationCaseDefinition.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`VerificationCaseDefinition`](sysml/VerificationCaseDefinition.html).
`void`
`[visitVerificationCaseUsage](#visitVerificationCaseUsage(com.dassault_systemes.modeler.sysml.model.sysml.VerificationCaseUsage,C))([VerificationCaseUsage](sysml/VerificationCaseUsage.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`VerificationCaseUsage`](sysml/VerificationCaseUsage.html).
`void`
`[visitViewDefinition](#visitViewDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ViewDefinition,C))([ViewDefinition](sysml/ViewDefinition.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`ViewDefinition`](sysml/ViewDefinition.html).
`void`
`[visitViewpointDefinition](#visitViewpointDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ViewpointDefinition,C))([ViewpointDefinition](sysml/ViewpointDefinition.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`ViewpointDefinition`](sysml/ViewpointDefinition.html).
`void`
`[visitViewpointUsage](#visitViewpointUsage(com.dassault_systemes.modeler.sysml.model.sysml.ViewpointUsage,C))([ViewpointUsage](sysml/ViewpointUsage.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`ViewpointUsage`](sysml/ViewpointUsage.html).
`void`
`[visitViewRenderingMembership](#visitViewRenderingMembership(com.dassault_systemes.modeler.sysml.model.sysml.ViewRenderingMembership,C))([ViewRenderingMembership](sysml/ViewRenderingMembership.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`ViewRenderingMembership`](sysml/ViewRenderingMembership.html).
`void`
`[visitViewUsage](#visitViewUsage(com.dassault_systemes.modeler.sysml.model.sysml.ViewUsage,C))([ViewUsage](sysml/ViewUsage.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`ViewUsage`](sysml/ViewUsage.html).
`void`
`[visitWhileLoopActionUsage](#visitWhileLoopActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.WhileLoopActionUsage,C))([WhileLoopActionUsage](sysml/WhileLoopActionUsage.html) element,
 [C](SysMLModelVisitor.html) context)`
Visitor method for [`WhileLoopActionUsage`](sysml/WhileLoopActionUsage.html).
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.[KerMLModelVisitor](../../kerml/model/KerMLModelVisitor.html)
`[visitAnnotatingElement](../../kerml/model/KerMLModelVisitor.html#visitAnnotatingElement(com.dassault_systemes.modeler.kerml.model.kerml.AnnotatingElement,C)), [visitAnnotation](../../kerml/model/KerMLModelVisitor.html#visitAnnotation(com.dassault_systemes.modeler.kerml.model.kerml.Annotation,C)), [visitAssociation](../../kerml/model/KerMLModelVisitor.html#visitAssociation(com.dassault_systemes.modeler.kerml.model.kerml.Association,C)), [visitAssociationStructure](../../kerml/model/KerMLModelVisitor.html#visitAssociationStructure(com.dassault_systemes.modeler.kerml.model.kerml.AssociationStructure,C)), [visitBehavior](../../kerml/model/KerMLModelVisitor.html#visitBehavior(com.dassault_systemes.modeler.kerml.model.kerml.Behavior,C)), [visitBindingConnector](../../kerml/model/KerMLModelVisitor.html#visitBindingConnector(com.dassault_systemes.modeler.kerml.model.kerml.BindingConnector,C)), [visitBooleanExpression](../../kerml/model/KerMLModelVisitor.html#visitBooleanExpression(com.dassault_systemes.modeler.kerml.model.kerml.BooleanExpression,C)), [visitClass](../../kerml/model/KerMLModelVisitor.html#visitClass(com.dassault_systemes.modeler.kerml.model.kerml.Class,C)), [visitClassifier](../../kerml/model/KerMLModelVisitor.html#visitClassifier(com.dassault_systemes.modeler.kerml.model.kerml.Classifier,C)), [visitCollectExpression](../../kerml/model/KerMLModelVisitor.html#visitCollectExpression(com.dassault_systemes.modeler.kerml.model.kerml.CollectExpression,C)), [visitComment](../../kerml/model/KerMLModelVisitor.html#visitComment(com.dassault_systemes.modeler.kerml.model.kerml.Comment,C)), [visitConjugation](../../kerml/model/KerMLModelVisitor.html#visitConjugation(com.dassault_systemes.modeler.kerml.model.kerml.Conjugation,C)), [visitConnector](../../kerml/model/KerMLModelVisitor.html#visitConnector(com.dassault_systemes.modeler.kerml.model.kerml.Connector,C)), [visitConstructorExpression](../../kerml/model/KerMLModelVisitor.html#visitConstructorExpression(com.dassault_systemes.modeler.kerml.model.kerml.ConstructorExpression,C)), [visitCrossSubsetting](../../kerml/model/KerMLModelVisitor.html#visitCrossSubsetting(com.dassault_systemes.modeler.kerml.model.kerml.CrossSubsetting,C)), [visitDataType](../../kerml/model/KerMLModelVisitor.html#visitDataType(com.dassault_systemes.modeler.kerml.model.kerml.DataType,C)), [visitDependency](../../kerml/model/KerMLModelVisitor.html#visitDependency(com.dassault_systemes.modeler.kerml.model.kerml.Dependency,C)), [visitDifferencing](../../kerml/model/KerMLModelVisitor.html#visitDifferencing(com.dassault_systemes.modeler.kerml.model.kerml.Differencing,C)), [visitDisjoining](../../kerml/model/KerMLModelVisitor.html#visitDisjoining(com.dassault_systemes.modeler.kerml.model.kerml.Disjoining,C)), [visitDocumentation](../../kerml/model/KerMLModelVisitor.html#visitDocumentation(com.dassault_systemes.modeler.kerml.model.kerml.Documentation,C)), [visitElement](../../kerml/model/KerMLModelVisitor.html#visitElement(com.dassault_systemes.modeler.kerml.model.kerml.Element,C)), [visitElementFilterMembership](../../kerml/model/KerMLModelVisitor.html#visitElementFilterMembership(com.dassault_systemes.modeler.kerml.model.kerml.ElementFilterMembership,C)), [visitEndFeatureMembership](../../kerml/model/KerMLModelVisitor.html#visitEndFeatureMembership(com.dassault_systemes.modeler.kerml.model.kerml.EndFeatureMembership,C)), [visitExpression](../../kerml/model/KerMLModelVisitor.html#visitExpression(com.dassault_systemes.modeler.kerml.model.kerml.Expression,C)), [visitFeature](../../kerml/model/KerMLModelVisitor.html#visitFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature,C)), [visitFeatureChainExpression](../../kerml/model/KerMLModelVisitor.html#visitFeatureChainExpression(com.dassault_systemes.modeler.kerml.model.kerml.FeatureChainExpression,C)), [visitFeatureChaining](../../kerml/model/KerMLModelVisitor.html#visitFeatureChaining(com.dassault_systemes.modeler.kerml.model.kerml.FeatureChaining,C)), [visitFeatureInverting](../../kerml/model/KerMLModelVisitor.html#visitFeatureInverting(com.dassault_systemes.modeler.kerml.model.kerml.FeatureInverting,C)), [visitFeatureMembership](../../kerml/model/KerMLModelVisitor.html#visitFeatureMembership(com.dassault_systemes.modeler.kerml.model.kerml.FeatureMembership,C)), [visitFeatureReferenceExpression](../../kerml/model/KerMLModelVisitor.html#visitFeatureReferenceExpression(com.dassault_systemes.modeler.kerml.model.kerml.FeatureReferenceExpression,C)), [visitFeatureTyping](../../kerml/model/KerMLModelVisitor.html#visitFeatureTyping(com.dassault_systemes.modeler.kerml.model.kerml.FeatureTyping,C)), [visitFeatureValue](../../kerml/model/KerMLModelVisitor.html#visitFeatureValue(com.dassault_systemes.modeler.kerml.model.kerml.FeatureValue,C)), [visitFlow](../../kerml/model/KerMLModelVisitor.html#visitFlow(com.dassault_systemes.modeler.kerml.model.kerml.Flow,C)), [visitFlowEnd](../../kerml/model/KerMLModelVisitor.html#visitFlowEnd(com.dassault_systemes.modeler.kerml.model.kerml.FlowEnd,C)), [visitFunction](../../kerml/model/KerMLModelVisitor.html#visitFunction(com.dassault_systemes.modeler.kerml.model.kerml.Function,C)), [visitImport](../../kerml/model/KerMLModelVisitor.html#visitImport(com.dassault_systemes.modeler.kerml.model.kerml.Import,C)), [visitIndexExpression](../../kerml/model/KerMLModelVisitor.html#visitIndexExpression(com.dassault_systemes.modeler.kerml.model.kerml.IndexExpression,C)), [visitInstantiationExpression](../../kerml/model/KerMLModelVisitor.html#visitInstantiationExpression(com.dassault_systemes.modeler.kerml.model.kerml.InstantiationExpression,C)), [visitInteraction](../../kerml/model/KerMLModelVisitor.html#visitInteraction(com.dassault_systemes.modeler.kerml.model.kerml.Interaction,C)), [visitIntersecting](../../kerml/model/KerMLModelVisitor.html#visitIntersecting(com.dassault_systemes.modeler.kerml.model.kerml.Intersecting,C)), [visitInvariant](../../kerml/model/KerMLModelVisitor.html#visitInvariant(com.dassault_systemes.modeler.kerml.model.kerml.Invariant,C)), [visitInvocationExpression](../../kerml/model/KerMLModelVisitor.html#visitInvocationExpression(com.dassault_systemes.modeler.kerml.model.kerml.InvocationExpression,C)), [visitLibraryPackage](../../kerml/model/KerMLModelVisitor.html#visitLibraryPackage(com.dassault_systemes.modeler.kerml.model.kerml.LibraryPackage,C)), [visitLiteralBoolean](../../kerml/model/KerMLModelVisitor.html#visitLiteralBoolean(com.dassault_systemes.modeler.kerml.model.kerml.LiteralBoolean,C)), [visitLiteralExpression](../../kerml/model/KerMLModelVisitor.html#visitLiteralExpression(com.dassault_systemes.modeler.kerml.model.kerml.LiteralExpression,C)), [visitLiteralInfinity](../../kerml/model/KerMLModelVisitor.html#visitLiteralInfinity(com.dassault_systemes.modeler.kerml.model.kerml.LiteralInfinity,C)), [visitLiteralInteger](../../kerml/model/KerMLModelVisitor.html#visitLiteralInteger(com.dassault_systemes.modeler.kerml.model.kerml.LiteralInteger,C)), [visitLiteralRational](../../kerml/model/KerMLModelVisitor.html#visitLiteralRational(com.dassault_systemes.modeler.kerml.model.kerml.LiteralRational,C)), [visitLiteralString](../../kerml/model/KerMLModelVisitor.html#visitLiteralString(com.dassault_systemes.modeler.kerml.model.kerml.LiteralString,C)), [visitMembership](../../kerml/model/KerMLModelVisitor.html#visitMembership(com.dassault_systemes.modeler.kerml.model.kerml.Membership,C)), [visitMembershipImport](../../kerml/model/KerMLModelVisitor.html#visitMembershipImport(com.dassault_systemes.modeler.kerml.model.kerml.MembershipImport,C)), [visitMetaclass](../../kerml/model/KerMLModelVisitor.html#visitMetaclass(com.dassault_systemes.modeler.kerml.model.kerml.Metaclass,C)), [visitMetadataAccessExpression](../../kerml/model/KerMLModelVisitor.html#visitMetadataAccessExpression(com.dassault_systemes.modeler.kerml.model.kerml.MetadataAccessExpression,C)), [visitMetadataFeature](../../kerml/model/KerMLModelVisitor.html#visitMetadataFeature(com.dassault_systemes.modeler.kerml.model.kerml.MetadataFeature,C)), [visitMultiplicity](../../kerml/model/KerMLModelVisitor.html#visitMultiplicity(com.dassault_systemes.modeler.kerml.model.kerml.Multiplicity,C)), [visitMultiplicityRange](../../kerml/model/KerMLModelVisitor.html#visitMultiplicityRange(com.dassault_systemes.modeler.kerml.model.kerml.MultiplicityRange,C)), [visitNamespace](../../kerml/model/KerMLModelVisitor.html#visitNamespace(com.dassault_systemes.modeler.kerml.model.kerml.Namespace,C)), [visitNamespaceImport](../../kerml/model/KerMLModelVisitor.html#visitNamespaceImport(com.dassault_systemes.modeler.kerml.model.kerml.NamespaceImport,C)), [visitNullExpression](../../kerml/model/KerMLModelVisitor.html#visitNullExpression(com.dassault_systemes.modeler.kerml.model.kerml.NullExpression,C)), [visitOperatorExpression](../../kerml/model/KerMLModelVisitor.html#visitOperatorExpression(com.dassault_systemes.modeler.kerml.model.kerml.OperatorExpression,C)), [visitOwningMembership](../../kerml/model/KerMLModelVisitor.html#visitOwningMembership(com.dassault_systemes.modeler.kerml.model.kerml.OwningMembership,C)), [visitPackage](../../kerml/model/KerMLModelVisitor.html#visitPackage(com.dassault_systemes.modeler.kerml.model.kerml.Package,C)), [visitParameterMembership](../../kerml/model/KerMLModelVisitor.html#visitParameterMembership(com.dassault_systemes.modeler.kerml.model.kerml.ParameterMembership,C)), [visitPayloadFeature](../../kerml/model/KerMLModelVisitor.html#visitPayloadFeature(com.dassault_systemes.modeler.kerml.model.kerml.PayloadFeature,C)), [visitPredicate](../../kerml/model/KerMLModelVisitor.html#visitPredicate(com.dassault_systemes.modeler.kerml.model.kerml.Predicate,C)), [visitRedefinition](../../kerml/model/KerMLModelVisitor.html#visitRedefinition(com.dassault_systemes.modeler.kerml.model.kerml.Redefinition,C)), [visitReferenceSubsetting](../../kerml/model/KerMLModelVisitor.html#visitReferenceSubsetting(com.dassault_systemes.modeler.kerml.model.kerml.ReferenceSubsetting,C)), [visitRelationship](../../kerml/model/KerMLModelVisitor.html#visitRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Relationship,C)), [visitResultExpressionMembership](../../kerml/model/KerMLModelVisitor.html#visitResultExpressionMembership(com.dassault_systemes.modeler.kerml.model.kerml.ResultExpressionMembership,C)), [visitReturnParameterMembership](../../kerml/model/KerMLModelVisitor.html#visitReturnParameterMembership(com.dassault_systemes.modeler.kerml.model.kerml.ReturnParameterMembership,C)), [visitSelectExpression](../../kerml/model/KerMLModelVisitor.html#visitSelectExpression(com.dassault_systemes.modeler.kerml.model.kerml.SelectExpression,C)), [visitSpecialization](../../kerml/model/KerMLModelVisitor.html#visitSpecialization(com.dassault_systemes.modeler.kerml.model.kerml.Specialization,C)), [visitStep](../../kerml/model/KerMLModelVisitor.html#visitStep(com.dassault_systemes.modeler.kerml.model.kerml.Step,C)), [visitStructure](../../kerml/model/KerMLModelVisitor.html#visitStructure(com.dassault_systemes.modeler.kerml.model.kerml.Structure,C)), [visitSubclassification](../../kerml/model/KerMLModelVisitor.html#visitSubclassification(com.dassault_systemes.modeler.kerml.model.kerml.Subclassification,C)), [visitSubsetting](../../kerml/model/KerMLModelVisitor.html#visitSubsetting(com.dassault_systemes.modeler.kerml.model.kerml.Subsetting,C)), [visitSuccession](../../kerml/model/KerMLModelVisitor.html#visitSuccession(com.dassault_systemes.modeler.kerml.model.kerml.Succession,C)), [visitSuccessionFlow](../../kerml/model/KerMLModelVisitor.html#visitSuccessionFlow(com.dassault_systemes.modeler.kerml.model.kerml.SuccessionFlow,C)), [visitTextualRepresentation](../../kerml/model/KerMLModelVisitor.html#visitTextualRepresentation(com.dassault_systemes.modeler.kerml.model.kerml.TextualRepresentation,C)), [visitType](../../kerml/model/KerMLModelVisitor.html#visitType(com.dassault_systemes.modeler.kerml.model.kerml.Type,C)), [visitTypeFeaturing](../../kerml/model/KerMLModelVisitor.html#visitTypeFeaturing(com.dassault_systemes.modeler.kerml.model.kerml.TypeFeaturing,C)), [visitUnioning](../../kerml/model/KerMLModelVisitor.html#visitUnioning(com.dassault_systemes.modeler.kerml.model.kerml.Unioning,C))`

============ METHOD DETAIL ========== 
Method Details
visitAcceptActionUsage
void visitAcceptActionUsage([AcceptActionUsage](sysml/AcceptActionUsage.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`AcceptActionUsage`](sysml/AcceptActionUsage.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitActionDefinition
void visitActionDefinition([ActionDefinition](sysml/ActionDefinition.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`ActionDefinition`](sysml/ActionDefinition.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitActionUsage
void visitActionUsage([ActionUsage](sysml/ActionUsage.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`ActionUsage`](sysml/ActionUsage.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitActorMembership
void visitActorMembership([ActorMembership](sysml/ActorMembership.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`ActorMembership`](sysml/ActorMembership.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitAllocationDefinition
void visitAllocationDefinition([AllocationDefinition](sysml/AllocationDefinition.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`AllocationDefinition`](sysml/AllocationDefinition.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitAllocationUsage
void visitAllocationUsage([AllocationUsage](sysml/AllocationUsage.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`AllocationUsage`](sysml/AllocationUsage.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitAnalysisCaseDefinition
void visitAnalysisCaseDefinition([AnalysisCaseDefinition](sysml/AnalysisCaseDefinition.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`AnalysisCaseDefinition`](sysml/AnalysisCaseDefinition.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitAnalysisCaseUsage
void visitAnalysisCaseUsage([AnalysisCaseUsage](sysml/AnalysisCaseUsage.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`AnalysisCaseUsage`](sysml/AnalysisCaseUsage.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitAssertConstraintUsage
void visitAssertConstraintUsage([AssertConstraintUsage](sysml/AssertConstraintUsage.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`AssertConstraintUsage`](sysml/AssertConstraintUsage.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitAssignmentActionUsage
void visitAssignmentActionUsage([AssignmentActionUsage](sysml/AssignmentActionUsage.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`AssignmentActionUsage`](sysml/AssignmentActionUsage.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitAttributeDefinition
void visitAttributeDefinition([AttributeDefinition](sysml/AttributeDefinition.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`AttributeDefinition`](sysml/AttributeDefinition.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitAttributeUsage
void visitAttributeUsage([AttributeUsage](sysml/AttributeUsage.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`AttributeUsage`](sysml/AttributeUsage.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitBindingConnectorAsUsage
void visitBindingConnectorAsUsage([BindingConnectorAsUsage](sysml/BindingConnectorAsUsage.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`BindingConnectorAsUsage`](sysml/BindingConnectorAsUsage.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitCalculationDefinition
void visitCalculationDefinition([CalculationDefinition](sysml/CalculationDefinition.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`CalculationDefinition`](sysml/CalculationDefinition.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitCalculationUsage
void visitCalculationUsage([CalculationUsage](sysml/CalculationUsage.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`CalculationUsage`](sysml/CalculationUsage.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitCaseDefinition
void visitCaseDefinition([CaseDefinition](sysml/CaseDefinition.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`CaseDefinition`](sysml/CaseDefinition.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitCaseUsage
void visitCaseUsage([CaseUsage](sysml/CaseUsage.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`CaseUsage`](sysml/CaseUsage.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitConcernDefinition
void visitConcernDefinition([ConcernDefinition](sysml/ConcernDefinition.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`ConcernDefinition`](sysml/ConcernDefinition.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitConcernUsage
void visitConcernUsage([ConcernUsage](sysml/ConcernUsage.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`ConcernUsage`](sysml/ConcernUsage.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitConjugatedPortDefinition
void visitConjugatedPortDefinition([ConjugatedPortDefinition](sysml/ConjugatedPortDefinition.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`ConjugatedPortDefinition`](sysml/ConjugatedPortDefinition.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitConjugatedPortTyping
void visitConjugatedPortTyping([ConjugatedPortTyping](sysml/ConjugatedPortTyping.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`ConjugatedPortTyping`](sysml/ConjugatedPortTyping.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitConnectionDefinition
void visitConnectionDefinition([ConnectionDefinition](sysml/ConnectionDefinition.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`ConnectionDefinition`](sysml/ConnectionDefinition.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitConnectionUsage
void visitConnectionUsage([ConnectionUsage](sysml/ConnectionUsage.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`ConnectionUsage`](sysml/ConnectionUsage.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitConnectorAsUsage
void visitConnectorAsUsage([ConnectorAsUsage](sysml/ConnectorAsUsage.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`ConnectorAsUsage`](sysml/ConnectorAsUsage.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitConstraintDefinition
void visitConstraintDefinition([ConstraintDefinition](sysml/ConstraintDefinition.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`ConstraintDefinition`](sysml/ConstraintDefinition.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitConstraintUsage
void visitConstraintUsage([ConstraintUsage](sysml/ConstraintUsage.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`ConstraintUsage`](sysml/ConstraintUsage.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitControlNode
void visitControlNode([ControlNode](sysml/ControlNode.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`ControlNode`](sysml/ControlNode.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitDecisionNode
void visitDecisionNode([DecisionNode](sysml/DecisionNode.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`DecisionNode`](sysml/DecisionNode.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitDefinition
void visitDefinition([Definition](sysml/Definition.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`Definition`](sysml/Definition.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitEnumerationDefinition
void visitEnumerationDefinition([EnumerationDefinition](sysml/EnumerationDefinition.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`EnumerationDefinition`](sysml/EnumerationDefinition.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitEnumerationUsage
void visitEnumerationUsage([EnumerationUsage](sysml/EnumerationUsage.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`EnumerationUsage`](sysml/EnumerationUsage.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitEventOccurrenceUsage
void visitEventOccurrenceUsage([EventOccurrenceUsage](sysml/EventOccurrenceUsage.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`EventOccurrenceUsage`](sysml/EventOccurrenceUsage.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitExhibitStateUsage
void visitExhibitStateUsage([ExhibitStateUsage](sysml/ExhibitStateUsage.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`ExhibitStateUsage`](sysml/ExhibitStateUsage.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitExpose
void visitExpose([Expose](sysml/Expose.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`Expose`](sysml/Expose.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitFlowDefinition
void visitFlowDefinition([FlowDefinition](sysml/FlowDefinition.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`FlowDefinition`](sysml/FlowDefinition.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitFlowUsage
void visitFlowUsage([FlowUsage](sysml/FlowUsage.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`FlowUsage`](sysml/FlowUsage.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitForLoopActionUsage
void visitForLoopActionUsage([ForLoopActionUsage](sysml/ForLoopActionUsage.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`ForLoopActionUsage`](sysml/ForLoopActionUsage.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitForkNode
void visitForkNode([ForkNode](sysml/ForkNode.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`ForkNode`](sysml/ForkNode.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitFramedConcernMembership
void visitFramedConcernMembership([FramedConcernMembership](sysml/FramedConcernMembership.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`FramedConcernMembership`](sysml/FramedConcernMembership.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitIfActionUsage
void visitIfActionUsage([IfActionUsage](sysml/IfActionUsage.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`IfActionUsage`](sysml/IfActionUsage.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitIncludeUseCaseUsage
void visitIncludeUseCaseUsage([IncludeUseCaseUsage](sysml/IncludeUseCaseUsage.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`IncludeUseCaseUsage`](sysml/IncludeUseCaseUsage.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitInterfaceDefinition
void visitInterfaceDefinition([InterfaceDefinition](sysml/InterfaceDefinition.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`InterfaceDefinition`](sysml/InterfaceDefinition.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitInterfaceUsage
void visitInterfaceUsage([InterfaceUsage](sysml/InterfaceUsage.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`InterfaceUsage`](sysml/InterfaceUsage.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitItemDefinition
void visitItemDefinition([ItemDefinition](sysml/ItemDefinition.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`ItemDefinition`](sysml/ItemDefinition.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitItemUsage
void visitItemUsage([ItemUsage](sysml/ItemUsage.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`ItemUsage`](sysml/ItemUsage.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitJoinNode
void visitJoinNode([JoinNode](sysml/JoinNode.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`JoinNode`](sysml/JoinNode.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitLoopActionUsage
void visitLoopActionUsage([LoopActionUsage](sysml/LoopActionUsage.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`LoopActionUsage`](sysml/LoopActionUsage.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitMembershipExpose
void visitMembershipExpose([MembershipExpose](sysml/MembershipExpose.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`MembershipExpose`](sysml/MembershipExpose.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitMergeNode
void visitMergeNode([MergeNode](sysml/MergeNode.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`MergeNode`](sysml/MergeNode.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitMetadataDefinition
void visitMetadataDefinition([MetadataDefinition](sysml/MetadataDefinition.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`MetadataDefinition`](sysml/MetadataDefinition.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitMetadataUsage
void visitMetadataUsage([MetadataUsage](sysml/MetadataUsage.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`MetadataUsage`](sysml/MetadataUsage.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitNamespaceExpose
void visitNamespaceExpose([NamespaceExpose](sysml/NamespaceExpose.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`NamespaceExpose`](sysml/NamespaceExpose.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitObjectiveMembership
void visitObjectiveMembership([ObjectiveMembership](sysml/ObjectiveMembership.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`ObjectiveMembership`](sysml/ObjectiveMembership.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitOccurrenceDefinition
void visitOccurrenceDefinition([OccurrenceDefinition](sysml/OccurrenceDefinition.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`OccurrenceDefinition`](sysml/OccurrenceDefinition.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitOccurrenceUsage
void visitOccurrenceUsage([OccurrenceUsage](sysml/OccurrenceUsage.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`OccurrenceUsage`](sysml/OccurrenceUsage.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitPartDefinition
void visitPartDefinition([PartDefinition](sysml/PartDefinition.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`PartDefinition`](sysml/PartDefinition.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitPartUsage
void visitPartUsage([PartUsage](sysml/PartUsage.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`PartUsage`](sysml/PartUsage.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitPerformActionUsage
void visitPerformActionUsage([PerformActionUsage](sysml/PerformActionUsage.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`PerformActionUsage`](sysml/PerformActionUsage.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitPortConjugation
void visitPortConjugation([PortConjugation](sysml/PortConjugation.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`PortConjugation`](sysml/PortConjugation.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitPortDefinition
void visitPortDefinition([PortDefinition](sysml/PortDefinition.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`PortDefinition`](sysml/PortDefinition.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitPortUsage
void visitPortUsage([PortUsage](sysml/PortUsage.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`PortUsage`](sysml/PortUsage.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitReferenceUsage
void visitReferenceUsage([ReferenceUsage](sysml/ReferenceUsage.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`ReferenceUsage`](sysml/ReferenceUsage.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitRenderingDefinition
void visitRenderingDefinition([RenderingDefinition](sysml/RenderingDefinition.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`RenderingDefinition`](sysml/RenderingDefinition.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitRenderingUsage
void visitRenderingUsage([RenderingUsage](sysml/RenderingUsage.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`RenderingUsage`](sysml/RenderingUsage.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitRequirementConstraintMembership
void visitRequirementConstraintMembership([RequirementConstraintMembership](sysml/RequirementConstraintMembership.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`RequirementConstraintMembership`](sysml/RequirementConstraintMembership.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitRequirementDefinition
void visitRequirementDefinition([RequirementDefinition](sysml/RequirementDefinition.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`RequirementDefinition`](sysml/RequirementDefinition.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitRequirementUsage
void visitRequirementUsage([RequirementUsage](sysml/RequirementUsage.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`RequirementUsage`](sysml/RequirementUsage.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitRequirementVerificationMembership
void visitRequirementVerificationMembership([RequirementVerificationMembership](sysml/RequirementVerificationMembership.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`RequirementVerificationMembership`](sysml/RequirementVerificationMembership.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitSatisfyRequirementUsage
void visitSatisfyRequirementUsage([SatisfyRequirementUsage](sysml/SatisfyRequirementUsage.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`SatisfyRequirementUsage`](sysml/SatisfyRequirementUsage.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitSendActionUsage
void visitSendActionUsage([SendActionUsage](sysml/SendActionUsage.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`SendActionUsage`](sysml/SendActionUsage.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitStakeholderMembership
void visitStakeholderMembership([StakeholderMembership](sysml/StakeholderMembership.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`StakeholderMembership`](sysml/StakeholderMembership.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitStateDefinition
void visitStateDefinition([StateDefinition](sysml/StateDefinition.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`StateDefinition`](sysml/StateDefinition.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitStateSubactionMembership
void visitStateSubactionMembership([StateSubactionMembership](sysml/StateSubactionMembership.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`StateSubactionMembership`](sysml/StateSubactionMembership.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitStateUsage
void visitStateUsage([StateUsage](sysml/StateUsage.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`StateUsage`](sysml/StateUsage.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitSubjectMembership
void visitSubjectMembership([SubjectMembership](sysml/SubjectMembership.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`SubjectMembership`](sysml/SubjectMembership.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitSuccessionAsUsage
void visitSuccessionAsUsage([SuccessionAsUsage](sysml/SuccessionAsUsage.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`SuccessionAsUsage`](sysml/SuccessionAsUsage.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitSuccessionFlowUsage
void visitSuccessionFlowUsage([SuccessionFlowUsage](sysml/SuccessionFlowUsage.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`SuccessionFlowUsage`](sysml/SuccessionFlowUsage.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitTerminateActionUsage
void visitTerminateActionUsage([TerminateActionUsage](sysml/TerminateActionUsage.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`TerminateActionUsage`](sysml/TerminateActionUsage.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitTransitionFeatureMembership
void visitTransitionFeatureMembership([TransitionFeatureMembership](sysml/TransitionFeatureMembership.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`TransitionFeatureMembership`](sysml/TransitionFeatureMembership.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitTransitionUsage
void visitTransitionUsage([TransitionUsage](sysml/TransitionUsage.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`TransitionUsage`](sysml/TransitionUsage.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitTriggerInvocationExpression
void visitTriggerInvocationExpression([TriggerInvocationExpression](sysml/TriggerInvocationExpression.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`TriggerInvocationExpression`](sysml/TriggerInvocationExpression.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitUsage
void visitUsage([Usage](sysml/Usage.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`Usage`](sysml/Usage.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitUseCaseDefinition
void visitUseCaseDefinition([UseCaseDefinition](sysml/UseCaseDefinition.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`UseCaseDefinition`](sysml/UseCaseDefinition.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitUseCaseUsage
void visitUseCaseUsage([UseCaseUsage](sysml/UseCaseUsage.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`UseCaseUsage`](sysml/UseCaseUsage.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitVariantMembership
void visitVariantMembership([VariantMembership](sysml/VariantMembership.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`VariantMembership`](sysml/VariantMembership.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitVerificationCaseDefinition
void visitVerificationCaseDefinition([VerificationCaseDefinition](sysml/VerificationCaseDefinition.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`VerificationCaseDefinition`](sysml/VerificationCaseDefinition.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitVerificationCaseUsage
void visitVerificationCaseUsage([VerificationCaseUsage](sysml/VerificationCaseUsage.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`VerificationCaseUsage`](sysml/VerificationCaseUsage.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitViewDefinition
void visitViewDefinition([ViewDefinition](sysml/ViewDefinition.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`ViewDefinition`](sysml/ViewDefinition.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitViewRenderingMembership
void visitViewRenderingMembership([ViewRenderingMembership](sysml/ViewRenderingMembership.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`ViewRenderingMembership`](sysml/ViewRenderingMembership.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitViewUsage
void visitViewUsage([ViewUsage](sysml/ViewUsage.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`ViewUsage`](sysml/ViewUsage.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitViewpointDefinition
void visitViewpointDefinition([ViewpointDefinition](sysml/ViewpointDefinition.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`ViewpointDefinition`](sysml/ViewpointDefinition.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitViewpointUsage
void visitViewpointUsage([ViewpointUsage](sysml/ViewpointUsage.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`ViewpointUsage`](sysml/ViewpointUsage.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitWhileLoopActionUsage
void visitWhileLoopActionUsage([WhileLoopActionUsage](sysml/WhileLoopActionUsage.html) element,
 [C](SysMLModelVisitor.html) context)
Visitor method for [`WhileLoopActionUsage`](sysml/WhileLoopActionUsage.html).
Parameters:
`element` - element to visit
`context` - context of visitor
createVisitorContext
default [C](SysMLModelVisitor.html) createVisitorContext()
Description copied from interface: `[KerMLModelVisitor](../../kerml/model/KerMLModelVisitor.html#createVisitorContext())`
Creates a new visitor context.
Specified by:
`[createVisitorContext](../../kerml/model/KerMLModelVisitor.html#createVisitorContext())` in interface `[KerMLModelVisitor](../../kerml/model/KerMLModelVisitor.html)<[C](SysMLModelVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Returns:
A new instance of `KerMLVisitorContextImpl`.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.sysml.model</a></div>
<h1 class="title" title="Interface SysMLModelVisitor">Interface SysMLModelVisitor&lt;C extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><code>C</code> - the type of the visitor context</dd>
</dl>
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../nomagic/magicdraw/uml/AbstractVisitor.html" title="interface in com.nomagic.magicdraw.uml">AbstractVisitor</a></code>, <code><a href="../../kerml/model/KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;C&gt;</code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="SysMLModelHierarchyVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelHierarchyVisitor</a>&lt;C&gt;</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">SysMLModelVisitor&lt;C extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</span><span class="extends-implements">
extends <a href="../../kerml/model/KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;C&gt;</span></div>
<div class="block">This interface extends KerMLModelVisitor to provide a visitor pattern implementation
 for traversing SysML model elements.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab5" onclick="show('method-summary-table', 'method-summary-table-tab5', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Default Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createVisitorContext()">createVisitorContext</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Creates a new visitor context.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitAcceptActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.AcceptActionUsage,C)">visitAcceptActionUsage</a><wbr/>(<a href="sysml/AcceptActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AcceptActionUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/AcceptActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>AcceptActionUsage</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitActionDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ActionDefinition,C)">visitActionDefinition</a><wbr/>(<a href="sysml/ActionDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActionDefinition</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/ActionDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ActionDefinition</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.ActionUsage,C)">visitActionUsage</a><wbr/>(<a href="sysml/ActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActionUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/ActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ActionUsage</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitActorMembership(com.dassault_systemes.modeler.sysml.model.sysml.ActorMembership,C)">visitActorMembership</a><wbr/>(<a href="sysml/ActorMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActorMembership</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/ActorMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ActorMembership</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitAllocationDefinition(com.dassault_systemes.modeler.sysml.model.sysml.AllocationDefinition,C)">visitAllocationDefinition</a><wbr/>(<a href="sysml/AllocationDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AllocationDefinition</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/AllocationDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>AllocationDefinition</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitAllocationUsage(com.dassault_systemes.modeler.sysml.model.sysml.AllocationUsage,C)">visitAllocationUsage</a><wbr/>(<a href="sysml/AllocationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AllocationUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/AllocationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>AllocationUsage</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitAnalysisCaseDefinition(com.dassault_systemes.modeler.sysml.model.sysml.AnalysisCaseDefinition,C)">visitAnalysisCaseDefinition</a><wbr/>(<a href="sysml/AnalysisCaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AnalysisCaseDefinition</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/AnalysisCaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>AnalysisCaseDefinition</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitAnalysisCaseUsage(com.dassault_systemes.modeler.sysml.model.sysml.AnalysisCaseUsage,C)">visitAnalysisCaseUsage</a><wbr/>(<a href="sysml/AnalysisCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AnalysisCaseUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/AnalysisCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>AnalysisCaseUsage</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitAssertConstraintUsage(com.dassault_systemes.modeler.sysml.model.sysml.AssertConstraintUsage,C)">visitAssertConstraintUsage</a><wbr/>(<a href="sysml/AssertConstraintUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AssertConstraintUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/AssertConstraintUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>AssertConstraintUsage</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitAssignmentActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.AssignmentActionUsage,C)">visitAssignmentActionUsage</a><wbr/>(<a href="sysml/AssignmentActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AssignmentActionUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/AssignmentActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>AssignmentActionUsage</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitAttributeDefinition(com.dassault_systemes.modeler.sysml.model.sysml.AttributeDefinition,C)">visitAttributeDefinition</a><wbr/>(<a href="sysml/AttributeDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AttributeDefinition</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/AttributeDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>AttributeDefinition</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitAttributeUsage(com.dassault_systemes.modeler.sysml.model.sysml.AttributeUsage,C)">visitAttributeUsage</a><wbr/>(<a href="sysml/AttributeUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AttributeUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/AttributeUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>AttributeUsage</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitBindingConnectorAsUsage(com.dassault_systemes.modeler.sysml.model.sysml.BindingConnectorAsUsage,C)">visitBindingConnectorAsUsage</a><wbr/>(<a href="sysml/BindingConnectorAsUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">BindingConnectorAsUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/BindingConnectorAsUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>BindingConnectorAsUsage</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitCalculationDefinition(com.dassault_systemes.modeler.sysml.model.sysml.CalculationDefinition,C)">visitCalculationDefinition</a><wbr/>(<a href="sysml/CalculationDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">CalculationDefinition</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/CalculationDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>CalculationDefinition</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitCalculationUsage(com.dassault_systemes.modeler.sysml.model.sysml.CalculationUsage,C)">visitCalculationUsage</a><wbr/>(<a href="sysml/CalculationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">CalculationUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/CalculationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>CalculationUsage</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitCaseDefinition(com.dassault_systemes.modeler.sysml.model.sysml.CaseDefinition,C)">visitCaseDefinition</a><wbr/>(<a href="sysml/CaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">CaseDefinition</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/CaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>CaseDefinition</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitCaseUsage(com.dassault_systemes.modeler.sysml.model.sysml.CaseUsage,C)">visitCaseUsage</a><wbr/>(<a href="sysml/CaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">CaseUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/CaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>CaseUsage</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitConcernDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ConcernDefinition,C)">visitConcernDefinition</a><wbr/>(<a href="sysml/ConcernDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConcernDefinition</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/ConcernDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ConcernDefinition</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitConcernUsage(com.dassault_systemes.modeler.sysml.model.sysml.ConcernUsage,C)">visitConcernUsage</a><wbr/>(<a href="sysml/ConcernUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConcernUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/ConcernUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ConcernUsage</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitConjugatedPortDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ConjugatedPortDefinition,C)">visitConjugatedPortDefinition</a><wbr/>(<a href="sysml/ConjugatedPortDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConjugatedPortDefinition</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/ConjugatedPortDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ConjugatedPortDefinition</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitConjugatedPortTyping(com.dassault_systemes.modeler.sysml.model.sysml.ConjugatedPortTyping,C)">visitConjugatedPortTyping</a><wbr/>(<a href="sysml/ConjugatedPortTyping.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConjugatedPortTyping</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/ConjugatedPortTyping.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ConjugatedPortTyping</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitConnectionDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ConnectionDefinition,C)">visitConnectionDefinition</a><wbr/>(<a href="sysml/ConnectionDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConnectionDefinition</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/ConnectionDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ConnectionDefinition</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitConnectionUsage(com.dassault_systemes.modeler.sysml.model.sysml.ConnectionUsage,C)">visitConnectionUsage</a><wbr/>(<a href="sysml/ConnectionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConnectionUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/ConnectionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ConnectionUsage</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitConnectorAsUsage(com.dassault_systemes.modeler.sysml.model.sysml.ConnectorAsUsage,C)">visitConnectorAsUsage</a><wbr/>(<a href="sysml/ConnectorAsUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConnectorAsUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/ConnectorAsUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ConnectorAsUsage</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitConstraintDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ConstraintDefinition,C)">visitConstraintDefinition</a><wbr/>(<a href="sysml/ConstraintDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConstraintDefinition</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/ConstraintDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ConstraintDefinition</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitConstraintUsage(com.dassault_systemes.modeler.sysml.model.sysml.ConstraintUsage,C)">visitConstraintUsage</a><wbr/>(<a href="sysml/ConstraintUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConstraintUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/ConstraintUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ConstraintUsage</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitControlNode(com.dassault_systemes.modeler.sysml.model.sysml.ControlNode,C)">visitControlNode</a><wbr/>(<a href="sysml/ControlNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ControlNode</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/ControlNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ControlNode</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitDecisionNode(com.dassault_systemes.modeler.sysml.model.sysml.DecisionNode,C)">visitDecisionNode</a><wbr/>(<a href="sysml/DecisionNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">DecisionNode</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/DecisionNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>DecisionNode</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitDefinition(com.dassault_systemes.modeler.sysml.model.sysml.Definition,C)">visitDefinition</a><wbr/>(<a href="sysml/Definition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Definition</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/Definition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>Definition</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitEnumerationDefinition(com.dassault_systemes.modeler.sysml.model.sysml.EnumerationDefinition,C)">visitEnumerationDefinition</a><wbr/>(<a href="sysml/EnumerationDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">EnumerationDefinition</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/EnumerationDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>EnumerationDefinition</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitEnumerationUsage(com.dassault_systemes.modeler.sysml.model.sysml.EnumerationUsage,C)">visitEnumerationUsage</a><wbr/>(<a href="sysml/EnumerationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">EnumerationUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/EnumerationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>EnumerationUsage</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitEventOccurrenceUsage(com.dassault_systemes.modeler.sysml.model.sysml.EventOccurrenceUsage,C)">visitEventOccurrenceUsage</a><wbr/>(<a href="sysml/EventOccurrenceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">EventOccurrenceUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/EventOccurrenceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>EventOccurrenceUsage</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitExhibitStateUsage(com.dassault_systemes.modeler.sysml.model.sysml.ExhibitStateUsage,C)">visitExhibitStateUsage</a><wbr/>(<a href="sysml/ExhibitStateUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ExhibitStateUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/ExhibitStateUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ExhibitStateUsage</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitExpose(com.dassault_systemes.modeler.sysml.model.sysml.Expose,C)">visitExpose</a><wbr/>(<a href="sysml/Expose.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Expose</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/Expose.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>Expose</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitFlowDefinition(com.dassault_systemes.modeler.sysml.model.sysml.FlowDefinition,C)">visitFlowDefinition</a><wbr/>(<a href="sysml/FlowDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">FlowDefinition</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/FlowDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>FlowDefinition</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitFlowUsage(com.dassault_systemes.modeler.sysml.model.sysml.FlowUsage,C)">visitFlowUsage</a><wbr/>(<a href="sysml/FlowUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">FlowUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/FlowUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>FlowUsage</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitForkNode(com.dassault_systemes.modeler.sysml.model.sysml.ForkNode,C)">visitForkNode</a><wbr/>(<a href="sysml/ForkNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ForkNode</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/ForkNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ForkNode</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitForLoopActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.ForLoopActionUsage,C)">visitForLoopActionUsage</a><wbr/>(<a href="sysml/ForLoopActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ForLoopActionUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/ForLoopActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ForLoopActionUsage</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitFramedConcernMembership(com.dassault_systemes.modeler.sysml.model.sysml.FramedConcernMembership,C)">visitFramedConcernMembership</a><wbr/>(<a href="sysml/FramedConcernMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">FramedConcernMembership</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/FramedConcernMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>FramedConcernMembership</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitIfActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.IfActionUsage,C)">visitIfActionUsage</a><wbr/>(<a href="sysml/IfActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">IfActionUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/IfActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>IfActionUsage</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitIncludeUseCaseUsage(com.dassault_systemes.modeler.sysml.model.sysml.IncludeUseCaseUsage,C)">visitIncludeUseCaseUsage</a><wbr/>(<a href="sysml/IncludeUseCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">IncludeUseCaseUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/IncludeUseCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>IncludeUseCaseUsage</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitInterfaceDefinition(com.dassault_systemes.modeler.sysml.model.sysml.InterfaceDefinition,C)">visitInterfaceDefinition</a><wbr/>(<a href="sysml/InterfaceDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">InterfaceDefinition</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/InterfaceDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>InterfaceDefinition</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitInterfaceUsage(com.dassault_systemes.modeler.sysml.model.sysml.InterfaceUsage,C)">visitInterfaceUsage</a><wbr/>(<a href="sysml/InterfaceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">InterfaceUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/InterfaceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>InterfaceUsage</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitItemDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ItemDefinition,C)">visitItemDefinition</a><wbr/>(<a href="sysml/ItemDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ItemDefinition</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/ItemDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ItemDefinition</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitItemUsage(com.dassault_systemes.modeler.sysml.model.sysml.ItemUsage,C)">visitItemUsage</a><wbr/>(<a href="sysml/ItemUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ItemUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/ItemUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ItemUsage</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitJoinNode(com.dassault_systemes.modeler.sysml.model.sysml.JoinNode,C)">visitJoinNode</a><wbr/>(<a href="sysml/JoinNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">JoinNode</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/JoinNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>JoinNode</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitLoopActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.LoopActionUsage,C)">visitLoopActionUsage</a><wbr/>(<a href="sysml/LoopActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">LoopActionUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/LoopActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>LoopActionUsage</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitMembershipExpose(com.dassault_systemes.modeler.sysml.model.sysml.MembershipExpose,C)">visitMembershipExpose</a><wbr/>(<a href="sysml/MembershipExpose.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">MembershipExpose</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/MembershipExpose.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>MembershipExpose</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitMergeNode(com.dassault_systemes.modeler.sysml.model.sysml.MergeNode,C)">visitMergeNode</a><wbr/>(<a href="sysml/MergeNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">MergeNode</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/MergeNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>MergeNode</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitMetadataDefinition(com.dassault_systemes.modeler.sysml.model.sysml.MetadataDefinition,C)">visitMetadataDefinition</a><wbr/>(<a href="sysml/MetadataDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">MetadataDefinition</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/MetadataDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>MetadataDefinition</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitMetadataUsage(com.dassault_systemes.modeler.sysml.model.sysml.MetadataUsage,C)">visitMetadataUsage</a><wbr/>(<a href="sysml/MetadataUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">MetadataUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/MetadataUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>MetadataUsage</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitNamespaceExpose(com.dassault_systemes.modeler.sysml.model.sysml.NamespaceExpose,C)">visitNamespaceExpose</a><wbr/>(<a href="sysml/NamespaceExpose.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">NamespaceExpose</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/NamespaceExpose.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>NamespaceExpose</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitObjectiveMembership(com.dassault_systemes.modeler.sysml.model.sysml.ObjectiveMembership,C)">visitObjectiveMembership</a><wbr/>(<a href="sysml/ObjectiveMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ObjectiveMembership</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/ObjectiveMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ObjectiveMembership</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitOccurrenceDefinition(com.dassault_systemes.modeler.sysml.model.sysml.OccurrenceDefinition,C)">visitOccurrenceDefinition</a><wbr/>(<a href="sysml/OccurrenceDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">OccurrenceDefinition</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/OccurrenceDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>OccurrenceDefinition</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitOccurrenceUsage(com.dassault_systemes.modeler.sysml.model.sysml.OccurrenceUsage,C)">visitOccurrenceUsage</a><wbr/>(<a href="sysml/OccurrenceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">OccurrenceUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/OccurrenceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>OccurrenceUsage</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitPartDefinition(com.dassault_systemes.modeler.sysml.model.sysml.PartDefinition,C)">visitPartDefinition</a><wbr/>(<a href="sysml/PartDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PartDefinition</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/PartDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>PartDefinition</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitPartUsage(com.dassault_systemes.modeler.sysml.model.sysml.PartUsage,C)">visitPartUsage</a><wbr/>(<a href="sysml/PartUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PartUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/PartUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>PartUsage</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitPerformActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.PerformActionUsage,C)">visitPerformActionUsage</a><wbr/>(<a href="sysml/PerformActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PerformActionUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/PerformActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>PerformActionUsage</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitPortConjugation(com.dassault_systemes.modeler.sysml.model.sysml.PortConjugation,C)">visitPortConjugation</a><wbr/>(<a href="sysml/PortConjugation.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PortConjugation</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/PortConjugation.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>PortConjugation</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitPortDefinition(com.dassault_systemes.modeler.sysml.model.sysml.PortDefinition,C)">visitPortDefinition</a><wbr/>(<a href="sysml/PortDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PortDefinition</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/PortDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>PortDefinition</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitPortUsage(com.dassault_systemes.modeler.sysml.model.sysml.PortUsage,C)">visitPortUsage</a><wbr/>(<a href="sysml/PortUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PortUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/PortUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>PortUsage</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitReferenceUsage(com.dassault_systemes.modeler.sysml.model.sysml.ReferenceUsage,C)">visitReferenceUsage</a><wbr/>(<a href="sysml/ReferenceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ReferenceUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/ReferenceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ReferenceUsage</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitRenderingDefinition(com.dassault_systemes.modeler.sysml.model.sysml.RenderingDefinition,C)">visitRenderingDefinition</a><wbr/>(<a href="sysml/RenderingDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RenderingDefinition</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/RenderingDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>RenderingDefinition</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitRenderingUsage(com.dassault_systemes.modeler.sysml.model.sysml.RenderingUsage,C)">visitRenderingUsage</a><wbr/>(<a href="sysml/RenderingUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RenderingUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/RenderingUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>RenderingUsage</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitRequirementConstraintMembership(com.dassault_systemes.modeler.sysml.model.sysml.RequirementConstraintMembership,C)">visitRequirementConstraintMembership</a><wbr/>(<a href="sysml/RequirementConstraintMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementConstraintMembership</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/RequirementConstraintMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>RequirementConstraintMembership</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitRequirementDefinition(com.dassault_systemes.modeler.sysml.model.sysml.RequirementDefinition,C)">visitRequirementDefinition</a><wbr/>(<a href="sysml/RequirementDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementDefinition</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/RequirementDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>RequirementDefinition</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitRequirementUsage(com.dassault_systemes.modeler.sysml.model.sysml.RequirementUsage,C)">visitRequirementUsage</a><wbr/>(<a href="sysml/RequirementUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/RequirementUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>RequirementUsage</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitRequirementVerificationMembership(com.dassault_systemes.modeler.sysml.model.sysml.RequirementVerificationMembership,C)">visitRequirementVerificationMembership</a><wbr/>(<a href="sysml/RequirementVerificationMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementVerificationMembership</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/RequirementVerificationMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>RequirementVerificationMembership</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitSatisfyRequirementUsage(com.dassault_systemes.modeler.sysml.model.sysml.SatisfyRequirementUsage,C)">visitSatisfyRequirementUsage</a><wbr/>(<a href="sysml/SatisfyRequirementUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SatisfyRequirementUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/SatisfyRequirementUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>SatisfyRequirementUsage</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitSendActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.SendActionUsage,C)">visitSendActionUsage</a><wbr/>(<a href="sysml/SendActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SendActionUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/SendActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>SendActionUsage</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitStakeholderMembership(com.dassault_systemes.modeler.sysml.model.sysml.StakeholderMembership,C)">visitStakeholderMembership</a><wbr/>(<a href="sysml/StakeholderMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">StakeholderMembership</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/StakeholderMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>StakeholderMembership</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitStateDefinition(com.dassault_systemes.modeler.sysml.model.sysml.StateDefinition,C)">visitStateDefinition</a><wbr/>(<a href="sysml/StateDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">StateDefinition</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/StateDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>StateDefinition</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitStateSubactionMembership(com.dassault_systemes.modeler.sysml.model.sysml.StateSubactionMembership,C)">visitStateSubactionMembership</a><wbr/>(<a href="sysml/StateSubactionMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">StateSubactionMembership</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/StateSubactionMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>StateSubactionMembership</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitStateUsage(com.dassault_systemes.modeler.sysml.model.sysml.StateUsage,C)">visitStateUsage</a><wbr/>(<a href="sysml/StateUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">StateUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/StateUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>StateUsage</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitSubjectMembership(com.dassault_systemes.modeler.sysml.model.sysml.SubjectMembership,C)">visitSubjectMembership</a><wbr/>(<a href="sysml/SubjectMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SubjectMembership</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/SubjectMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>SubjectMembership</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitSuccessionAsUsage(com.dassault_systemes.modeler.sysml.model.sysml.SuccessionAsUsage,C)">visitSuccessionAsUsage</a><wbr/>(<a href="sysml/SuccessionAsUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SuccessionAsUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/SuccessionAsUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>SuccessionAsUsage</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitSuccessionFlowUsage(com.dassault_systemes.modeler.sysml.model.sysml.SuccessionFlowUsage,C)">visitSuccessionFlowUsage</a><wbr/>(<a href="sysml/SuccessionFlowUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SuccessionFlowUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/SuccessionFlowUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>SuccessionFlowUsage</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitTerminateActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.TerminateActionUsage,C)">visitTerminateActionUsage</a><wbr/>(<a href="sysml/TerminateActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TerminateActionUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/TerminateActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>TerminateActionUsage</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitTransitionFeatureMembership(com.dassault_systemes.modeler.sysml.model.sysml.TransitionFeatureMembership,C)">visitTransitionFeatureMembership</a><wbr/>(<a href="sysml/TransitionFeatureMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TransitionFeatureMembership</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/TransitionFeatureMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>TransitionFeatureMembership</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitTransitionUsage(com.dassault_systemes.modeler.sysml.model.sysml.TransitionUsage,C)">visitTransitionUsage</a><wbr/>(<a href="sysml/TransitionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TransitionUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/TransitionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>TransitionUsage</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitTriggerInvocationExpression(com.dassault_systemes.modeler.sysml.model.sysml.TriggerInvocationExpression,C)">visitTriggerInvocationExpression</a><wbr/>(<a href="sysml/TriggerInvocationExpression.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TriggerInvocationExpression</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/TriggerInvocationExpression.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>TriggerInvocationExpression</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitUsage(com.dassault_systemes.modeler.sysml.model.sysml.Usage,C)">visitUsage</a><wbr/>(<a href="sysml/Usage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Usage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/Usage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>Usage</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitUseCaseDefinition(com.dassault_systemes.modeler.sysml.model.sysml.UseCaseDefinition,C)">visitUseCaseDefinition</a><wbr/>(<a href="sysml/UseCaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">UseCaseDefinition</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/UseCaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>UseCaseDefinition</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitUseCaseUsage(com.dassault_systemes.modeler.sysml.model.sysml.UseCaseUsage,C)">visitUseCaseUsage</a><wbr/>(<a href="sysml/UseCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">UseCaseUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/UseCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>UseCaseUsage</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitVariantMembership(com.dassault_systemes.modeler.sysml.model.sysml.VariantMembership,C)">visitVariantMembership</a><wbr/>(<a href="sysml/VariantMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">VariantMembership</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/VariantMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>VariantMembership</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitVerificationCaseDefinition(com.dassault_systemes.modeler.sysml.model.sysml.VerificationCaseDefinition,C)">visitVerificationCaseDefinition</a><wbr/>(<a href="sysml/VerificationCaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">VerificationCaseDefinition</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/VerificationCaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>VerificationCaseDefinition</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitVerificationCaseUsage(com.dassault_systemes.modeler.sysml.model.sysml.VerificationCaseUsage,C)">visitVerificationCaseUsage</a><wbr/>(<a href="sysml/VerificationCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">VerificationCaseUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/VerificationCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>VerificationCaseUsage</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitViewDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ViewDefinition,C)">visitViewDefinition</a><wbr/>(<a href="sysml/ViewDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewDefinition</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/ViewDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ViewDefinition</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitViewpointDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ViewpointDefinition,C)">visitViewpointDefinition</a><wbr/>(<a href="sysml/ViewpointDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewpointDefinition</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/ViewpointDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ViewpointDefinition</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitViewpointUsage(com.dassault_systemes.modeler.sysml.model.sysml.ViewpointUsage,C)">visitViewpointUsage</a><wbr/>(<a href="sysml/ViewpointUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewpointUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/ViewpointUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ViewpointUsage</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitViewRenderingMembership(com.dassault_systemes.modeler.sysml.model.sysml.ViewRenderingMembership,C)">visitViewRenderingMembership</a><wbr/>(<a href="sysml/ViewRenderingMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewRenderingMembership</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/ViewRenderingMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ViewRenderingMembership</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitViewUsage(com.dassault_systemes.modeler.sysml.model.sysml.ViewUsage,C)">visitViewUsage</a><wbr/>(<a href="sysml/ViewUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/ViewUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ViewUsage</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitWhileLoopActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.WhileLoopActionUsage,C)">visitWhileLoopActionUsage</a><wbr/>(<a href="sysml/WhileLoopActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">WhileLoopActionUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="sysml/WhileLoopActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>WhileLoopActionUsage</code></a>.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.model.KerMLModelVisitor">Methods inherited from interface com.dassault_systemes.modeler.kerml.model.<a href="../../kerml/model/KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a></h3>
<code><a href="../../kerml/model/KerMLModelVisitor.html#visitAnnotatingElement(com.dassault_systemes.modeler.kerml.model.kerml.AnnotatingElement,C)">visitAnnotatingElement</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitAnnotation(com.dassault_systemes.modeler.kerml.model.kerml.Annotation,C)">visitAnnotation</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitAssociation(com.dassault_systemes.modeler.kerml.model.kerml.Association,C)">visitAssociation</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitAssociationStructure(com.dassault_systemes.modeler.kerml.model.kerml.AssociationStructure,C)">visitAssociationStructure</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitBehavior(com.dassault_systemes.modeler.kerml.model.kerml.Behavior,C)">visitBehavior</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitBindingConnector(com.dassault_systemes.modeler.kerml.model.kerml.BindingConnector,C)">visitBindingConnector</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitBooleanExpression(com.dassault_systemes.modeler.kerml.model.kerml.BooleanExpression,C)">visitBooleanExpression</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitClass(com.dassault_systemes.modeler.kerml.model.kerml.Class,C)">visitClass</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitClassifier(com.dassault_systemes.modeler.kerml.model.kerml.Classifier,C)">visitClassifier</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitCollectExpression(com.dassault_systemes.modeler.kerml.model.kerml.CollectExpression,C)">visitCollectExpression</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitComment(com.dassault_systemes.modeler.kerml.model.kerml.Comment,C)">visitComment</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitConjugation(com.dassault_systemes.modeler.kerml.model.kerml.Conjugation,C)">visitConjugation</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitConnector(com.dassault_systemes.modeler.kerml.model.kerml.Connector,C)">visitConnector</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitConstructorExpression(com.dassault_systemes.modeler.kerml.model.kerml.ConstructorExpression,C)">visitConstructorExpression</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitCrossSubsetting(com.dassault_systemes.modeler.kerml.model.kerml.CrossSubsetting,C)">visitCrossSubsetting</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitDataType(com.dassault_systemes.modeler.kerml.model.kerml.DataType,C)">visitDataType</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitDependency(com.dassault_systemes.modeler.kerml.model.kerml.Dependency,C)">visitDependency</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitDifferencing(com.dassault_systemes.modeler.kerml.model.kerml.Differencing,C)">visitDifferencing</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitDisjoining(com.dassault_systemes.modeler.kerml.model.kerml.Disjoining,C)">visitDisjoining</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitDocumentation(com.dassault_systemes.modeler.kerml.model.kerml.Documentation,C)">visitDocumentation</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitElement(com.dassault_systemes.modeler.kerml.model.kerml.Element,C)">visitElement</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitElementFilterMembership(com.dassault_systemes.modeler.kerml.model.kerml.ElementFilterMembership,C)">visitElementFilterMembership</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitEndFeatureMembership(com.dassault_systemes.modeler.kerml.model.kerml.EndFeatureMembership,C)">visitEndFeatureMembership</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitExpression(com.dassault_systemes.modeler.kerml.model.kerml.Expression,C)">visitExpression</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature,C)">visitFeature</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitFeatureChainExpression(com.dassault_systemes.modeler.kerml.model.kerml.FeatureChainExpression,C)">visitFeatureChainExpression</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitFeatureChaining(com.dassault_systemes.modeler.kerml.model.kerml.FeatureChaining,C)">visitFeatureChaining</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitFeatureInverting(com.dassault_systemes.modeler.kerml.model.kerml.FeatureInverting,C)">visitFeatureInverting</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitFeatureMembership(com.dassault_systemes.modeler.kerml.model.kerml.FeatureMembership,C)">visitFeatureMembership</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitFeatureReferenceExpression(com.dassault_systemes.modeler.kerml.model.kerml.FeatureReferenceExpression,C)">visitFeatureReferenceExpression</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitFeatureTyping(com.dassault_systemes.modeler.kerml.model.kerml.FeatureTyping,C)">visitFeatureTyping</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitFeatureValue(com.dassault_systemes.modeler.kerml.model.kerml.FeatureValue,C)">visitFeatureValue</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitFlow(com.dassault_systemes.modeler.kerml.model.kerml.Flow,C)">visitFlow</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitFlowEnd(com.dassault_systemes.modeler.kerml.model.kerml.FlowEnd,C)">visitFlowEnd</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitFunction(com.dassault_systemes.modeler.kerml.model.kerml.Function,C)">visitFunction</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitImport(com.dassault_systemes.modeler.kerml.model.kerml.Import,C)">visitImport</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitIndexExpression(com.dassault_systemes.modeler.kerml.model.kerml.IndexExpression,C)">visitIndexExpression</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitInstantiationExpression(com.dassault_systemes.modeler.kerml.model.kerml.InstantiationExpression,C)">visitInstantiationExpression</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitInteraction(com.dassault_systemes.modeler.kerml.model.kerml.Interaction,C)">visitInteraction</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitIntersecting(com.dassault_systemes.modeler.kerml.model.kerml.Intersecting,C)">visitIntersecting</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitInvariant(com.dassault_systemes.modeler.kerml.model.kerml.Invariant,C)">visitInvariant</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitInvocationExpression(com.dassault_systemes.modeler.kerml.model.kerml.InvocationExpression,C)">visitInvocationExpression</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitLibraryPackage(com.dassault_systemes.modeler.kerml.model.kerml.LibraryPackage,C)">visitLibraryPackage</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitLiteralBoolean(com.dassault_systemes.modeler.kerml.model.kerml.LiteralBoolean,C)">visitLiteralBoolean</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitLiteralExpression(com.dassault_systemes.modeler.kerml.model.kerml.LiteralExpression,C)">visitLiteralExpression</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitLiteralInfinity(com.dassault_systemes.modeler.kerml.model.kerml.LiteralInfinity,C)">visitLiteralInfinity</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitLiteralInteger(com.dassault_systemes.modeler.kerml.model.kerml.LiteralInteger,C)">visitLiteralInteger</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitLiteralRational(com.dassault_systemes.modeler.kerml.model.kerml.LiteralRational,C)">visitLiteralRational</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitLiteralString(com.dassault_systemes.modeler.kerml.model.kerml.LiteralString,C)">visitLiteralString</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitMembership(com.dassault_systemes.modeler.kerml.model.kerml.Membership,C)">visitMembership</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitMembershipImport(com.dassault_systemes.modeler.kerml.model.kerml.MembershipImport,C)">visitMembershipImport</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitMetaclass(com.dassault_systemes.modeler.kerml.model.kerml.Metaclass,C)">visitMetaclass</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitMetadataAccessExpression(com.dassault_systemes.modeler.kerml.model.kerml.MetadataAccessExpression,C)">visitMetadataAccessExpression</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitMetadataFeature(com.dassault_systemes.modeler.kerml.model.kerml.MetadataFeature,C)">visitMetadataFeature</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitMultiplicity(com.dassault_systemes.modeler.kerml.model.kerml.Multiplicity,C)">visitMultiplicity</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitMultiplicityRange(com.dassault_systemes.modeler.kerml.model.kerml.MultiplicityRange,C)">visitMultiplicityRange</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitNamespace(com.dassault_systemes.modeler.kerml.model.kerml.Namespace,C)">visitNamespace</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitNamespaceImport(com.dassault_systemes.modeler.kerml.model.kerml.NamespaceImport,C)">visitNamespaceImport</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitNullExpression(com.dassault_systemes.modeler.kerml.model.kerml.NullExpression,C)">visitNullExpression</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitOperatorExpression(com.dassault_systemes.modeler.kerml.model.kerml.OperatorExpression,C)">visitOperatorExpression</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitOwningMembership(com.dassault_systemes.modeler.kerml.model.kerml.OwningMembership,C)">visitOwningMembership</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitPackage(com.dassault_systemes.modeler.kerml.model.kerml.Package,C)">visitPackage</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitParameterMembership(com.dassault_systemes.modeler.kerml.model.kerml.ParameterMembership,C)">visitParameterMembership</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitPayloadFeature(com.dassault_systemes.modeler.kerml.model.kerml.PayloadFeature,C)">visitPayloadFeature</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitPredicate(com.dassault_systemes.modeler.kerml.model.kerml.Predicate,C)">visitPredicate</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitRedefinition(com.dassault_systemes.modeler.kerml.model.kerml.Redefinition,C)">visitRedefinition</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitReferenceSubsetting(com.dassault_systemes.modeler.kerml.model.kerml.ReferenceSubsetting,C)">visitReferenceSubsetting</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Relationship,C)">visitRelationship</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitResultExpressionMembership(com.dassault_systemes.modeler.kerml.model.kerml.ResultExpressionMembership,C)">visitResultExpressionMembership</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitReturnParameterMembership(com.dassault_systemes.modeler.kerml.model.kerml.ReturnParameterMembership,C)">visitReturnParameterMembership</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitSelectExpression(com.dassault_systemes.modeler.kerml.model.kerml.SelectExpression,C)">visitSelectExpression</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitSpecialization(com.dassault_systemes.modeler.kerml.model.kerml.Specialization,C)">visitSpecialization</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitStep(com.dassault_systemes.modeler.kerml.model.kerml.Step,C)">visitStep</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitStructure(com.dassault_systemes.modeler.kerml.model.kerml.Structure,C)">visitStructure</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitSubclassification(com.dassault_systemes.modeler.kerml.model.kerml.Subclassification,C)">visitSubclassification</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitSubsetting(com.dassault_systemes.modeler.kerml.model.kerml.Subsetting,C)">visitSubsetting</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitSuccession(com.dassault_systemes.modeler.kerml.model.kerml.Succession,C)">visitSuccession</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitSuccessionFlow(com.dassault_systemes.modeler.kerml.model.kerml.SuccessionFlow,C)">visitSuccessionFlow</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitTextualRepresentation(com.dassault_systemes.modeler.kerml.model.kerml.TextualRepresentation,C)">visitTextualRepresentation</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitType(com.dassault_systemes.modeler.kerml.model.kerml.Type,C)">visitType</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitTypeFeaturing(com.dassault_systemes.modeler.kerml.model.kerml.TypeFeaturing,C)">visitTypeFeaturing</a>, <a href="../../kerml/model/KerMLModelVisitor.html#visitUnioning(com.dassault_systemes.modeler.kerml.model.kerml.Unioning,C)">visitUnioning</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">
<h2>Method Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="visitAcceptActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.AcceptActionUsage,C)">
<h3 id="visitAcceptActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.AcceptActionUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitAcceptActionUsage</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitAcceptActionUsage</span><wbr/><span class="parameters">(<a href="sysml/AcceptActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AcceptActionUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/AcceptActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>AcceptActionUsage</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitActionDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ActionDefinition,C)">
<h3 id="visitActionDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ActionDefinition,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitActionDefinition</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitActionDefinition</span><wbr/><span class="parameters">(<a href="sysml/ActionDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActionDefinition</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/ActionDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ActionDefinition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.ActionUsage,C)">
<h3 id="visitActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.ActionUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitActionUsage</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitActionUsage</span><wbr/><span class="parameters">(<a href="sysml/ActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActionUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/ActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ActionUsage</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitActorMembership(com.dassault_systemes.modeler.sysml.model.sysml.ActorMembership,C)">
<h3 id="visitActorMembership(com.dassault_systemes.modeler.sysml.model.sysml.ActorMembership,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitActorMembership</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitActorMembership</span><wbr/><span class="parameters">(<a href="sysml/ActorMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActorMembership</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/ActorMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ActorMembership</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitAllocationDefinition(com.dassault_systemes.modeler.sysml.model.sysml.AllocationDefinition,C)">
<h3 id="visitAllocationDefinition(com.dassault_systemes.modeler.sysml.model.sysml.AllocationDefinition,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitAllocationDefinition</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitAllocationDefinition</span><wbr/><span class="parameters">(<a href="sysml/AllocationDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AllocationDefinition</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/AllocationDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>AllocationDefinition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitAllocationUsage(com.dassault_systemes.modeler.sysml.model.sysml.AllocationUsage,C)">
<h3 id="visitAllocationUsage(com.dassault_systemes.modeler.sysml.model.sysml.AllocationUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitAllocationUsage</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitAllocationUsage</span><wbr/><span class="parameters">(<a href="sysml/AllocationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AllocationUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/AllocationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>AllocationUsage</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitAnalysisCaseDefinition(com.dassault_systemes.modeler.sysml.model.sysml.AnalysisCaseDefinition,C)">
<h3 id="visitAnalysisCaseDefinition(com.dassault_systemes.modeler.sysml.model.sysml.AnalysisCaseDefinition,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitAnalysisCaseDefinition</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitAnalysisCaseDefinition</span><wbr/><span class="parameters">(<a href="sysml/AnalysisCaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AnalysisCaseDefinition</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/AnalysisCaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>AnalysisCaseDefinition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitAnalysisCaseUsage(com.dassault_systemes.modeler.sysml.model.sysml.AnalysisCaseUsage,C)">
<h3 id="visitAnalysisCaseUsage(com.dassault_systemes.modeler.sysml.model.sysml.AnalysisCaseUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitAnalysisCaseUsage</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitAnalysisCaseUsage</span><wbr/><span class="parameters">(<a href="sysml/AnalysisCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AnalysisCaseUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/AnalysisCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>AnalysisCaseUsage</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitAssertConstraintUsage(com.dassault_systemes.modeler.sysml.model.sysml.AssertConstraintUsage,C)">
<h3 id="visitAssertConstraintUsage(com.dassault_systemes.modeler.sysml.model.sysml.AssertConstraintUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitAssertConstraintUsage</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitAssertConstraintUsage</span><wbr/><span class="parameters">(<a href="sysml/AssertConstraintUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AssertConstraintUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/AssertConstraintUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>AssertConstraintUsage</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitAssignmentActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.AssignmentActionUsage,C)">
<h3 id="visitAssignmentActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.AssignmentActionUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitAssignmentActionUsage</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitAssignmentActionUsage</span><wbr/><span class="parameters">(<a href="sysml/AssignmentActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AssignmentActionUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/AssignmentActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>AssignmentActionUsage</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitAttributeDefinition(com.dassault_systemes.modeler.sysml.model.sysml.AttributeDefinition,C)">
<h3 id="visitAttributeDefinition(com.dassault_systemes.modeler.sysml.model.sysml.AttributeDefinition,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitAttributeDefinition</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitAttributeDefinition</span><wbr/><span class="parameters">(<a href="sysml/AttributeDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AttributeDefinition</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/AttributeDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>AttributeDefinition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitAttributeUsage(com.dassault_systemes.modeler.sysml.model.sysml.AttributeUsage,C)">
<h3 id="visitAttributeUsage(com.dassault_systemes.modeler.sysml.model.sysml.AttributeUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitAttributeUsage</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitAttributeUsage</span><wbr/><span class="parameters">(<a href="sysml/AttributeUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AttributeUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/AttributeUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>AttributeUsage</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitBindingConnectorAsUsage(com.dassault_systemes.modeler.sysml.model.sysml.BindingConnectorAsUsage,C)">
<h3 id="visitBindingConnectorAsUsage(com.dassault_systemes.modeler.sysml.model.sysml.BindingConnectorAsUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitBindingConnectorAsUsage</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitBindingConnectorAsUsage</span><wbr/><span class="parameters">(<a href="sysml/BindingConnectorAsUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">BindingConnectorAsUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/BindingConnectorAsUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>BindingConnectorAsUsage</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitCalculationDefinition(com.dassault_systemes.modeler.sysml.model.sysml.CalculationDefinition,C)">
<h3 id="visitCalculationDefinition(com.dassault_systemes.modeler.sysml.model.sysml.CalculationDefinition,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitCalculationDefinition</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitCalculationDefinition</span><wbr/><span class="parameters">(<a href="sysml/CalculationDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">CalculationDefinition</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/CalculationDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>CalculationDefinition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitCalculationUsage(com.dassault_systemes.modeler.sysml.model.sysml.CalculationUsage,C)">
<h3 id="visitCalculationUsage(com.dassault_systemes.modeler.sysml.model.sysml.CalculationUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitCalculationUsage</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitCalculationUsage</span><wbr/><span class="parameters">(<a href="sysml/CalculationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">CalculationUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/CalculationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>CalculationUsage</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitCaseDefinition(com.dassault_systemes.modeler.sysml.model.sysml.CaseDefinition,C)">
<h3 id="visitCaseDefinition(com.dassault_systemes.modeler.sysml.model.sysml.CaseDefinition,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitCaseDefinition</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitCaseDefinition</span><wbr/><span class="parameters">(<a href="sysml/CaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">CaseDefinition</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/CaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>CaseDefinition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitCaseUsage(com.dassault_systemes.modeler.sysml.model.sysml.CaseUsage,C)">
<h3 id="visitCaseUsage(com.dassault_systemes.modeler.sysml.model.sysml.CaseUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitCaseUsage</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitCaseUsage</span><wbr/><span class="parameters">(<a href="sysml/CaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">CaseUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/CaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>CaseUsage</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitConcernDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ConcernDefinition,C)">
<h3 id="visitConcernDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ConcernDefinition,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitConcernDefinition</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitConcernDefinition</span><wbr/><span class="parameters">(<a href="sysml/ConcernDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConcernDefinition</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/ConcernDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ConcernDefinition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitConcernUsage(com.dassault_systemes.modeler.sysml.model.sysml.ConcernUsage,C)">
<h3 id="visitConcernUsage(com.dassault_systemes.modeler.sysml.model.sysml.ConcernUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitConcernUsage</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitConcernUsage</span><wbr/><span class="parameters">(<a href="sysml/ConcernUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConcernUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/ConcernUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ConcernUsage</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitConjugatedPortDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ConjugatedPortDefinition,C)">
<h3 id="visitConjugatedPortDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ConjugatedPortDefinition,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitConjugatedPortDefinition</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitConjugatedPortDefinition</span><wbr/><span class="parameters">(<a href="sysml/ConjugatedPortDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConjugatedPortDefinition</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/ConjugatedPortDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ConjugatedPortDefinition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitConjugatedPortTyping(com.dassault_systemes.modeler.sysml.model.sysml.ConjugatedPortTyping,C)">
<h3 id="visitConjugatedPortTyping(com.dassault_systemes.modeler.sysml.model.sysml.ConjugatedPortTyping,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitConjugatedPortTyping</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitConjugatedPortTyping</span><wbr/><span class="parameters">(<a href="sysml/ConjugatedPortTyping.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConjugatedPortTyping</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/ConjugatedPortTyping.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ConjugatedPortTyping</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitConnectionDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ConnectionDefinition,C)">
<h3 id="visitConnectionDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ConnectionDefinition,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitConnectionDefinition</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitConnectionDefinition</span><wbr/><span class="parameters">(<a href="sysml/ConnectionDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConnectionDefinition</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/ConnectionDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ConnectionDefinition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitConnectionUsage(com.dassault_systemes.modeler.sysml.model.sysml.ConnectionUsage,C)">
<h3 id="visitConnectionUsage(com.dassault_systemes.modeler.sysml.model.sysml.ConnectionUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitConnectionUsage</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitConnectionUsage</span><wbr/><span class="parameters">(<a href="sysml/ConnectionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConnectionUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/ConnectionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ConnectionUsage</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitConnectorAsUsage(com.dassault_systemes.modeler.sysml.model.sysml.ConnectorAsUsage,C)">
<h3 id="visitConnectorAsUsage(com.dassault_systemes.modeler.sysml.model.sysml.ConnectorAsUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitConnectorAsUsage</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitConnectorAsUsage</span><wbr/><span class="parameters">(<a href="sysml/ConnectorAsUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConnectorAsUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/ConnectorAsUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ConnectorAsUsage</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitConstraintDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ConstraintDefinition,C)">
<h3 id="visitConstraintDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ConstraintDefinition,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitConstraintDefinition</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitConstraintDefinition</span><wbr/><span class="parameters">(<a href="sysml/ConstraintDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConstraintDefinition</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/ConstraintDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ConstraintDefinition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitConstraintUsage(com.dassault_systemes.modeler.sysml.model.sysml.ConstraintUsage,C)">
<h3 id="visitConstraintUsage(com.dassault_systemes.modeler.sysml.model.sysml.ConstraintUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitConstraintUsage</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitConstraintUsage</span><wbr/><span class="parameters">(<a href="sysml/ConstraintUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConstraintUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/ConstraintUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ConstraintUsage</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitControlNode(com.dassault_systemes.modeler.sysml.model.sysml.ControlNode,C)">
<h3 id="visitControlNode(com.dassault_systemes.modeler.sysml.model.sysml.ControlNode,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitControlNode</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitControlNode</span><wbr/><span class="parameters">(<a href="sysml/ControlNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ControlNode</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/ControlNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ControlNode</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDecisionNode(com.dassault_systemes.modeler.sysml.model.sysml.DecisionNode,C)">
<h3 id="visitDecisionNode(com.dassault_systemes.modeler.sysml.model.sysml.DecisionNode,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitDecisionNode</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitDecisionNode</span><wbr/><span class="parameters">(<a href="sysml/DecisionNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">DecisionNode</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/DecisionNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>DecisionNode</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDefinition(com.dassault_systemes.modeler.sysml.model.sysml.Definition,C)">
<h3 id="visitDefinition(com.dassault_systemes.modeler.sysml.model.sysml.Definition,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitDefinition</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitDefinition</span><wbr/><span class="parameters">(<a href="sysml/Definition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Definition</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/Definition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>Definition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitEnumerationDefinition(com.dassault_systemes.modeler.sysml.model.sysml.EnumerationDefinition,C)">
<h3 id="visitEnumerationDefinition(com.dassault_systemes.modeler.sysml.model.sysml.EnumerationDefinition,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitEnumerationDefinition</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitEnumerationDefinition</span><wbr/><span class="parameters">(<a href="sysml/EnumerationDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">EnumerationDefinition</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/EnumerationDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>EnumerationDefinition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitEnumerationUsage(com.dassault_systemes.modeler.sysml.model.sysml.EnumerationUsage,C)">
<h3 id="visitEnumerationUsage(com.dassault_systemes.modeler.sysml.model.sysml.EnumerationUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitEnumerationUsage</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitEnumerationUsage</span><wbr/><span class="parameters">(<a href="sysml/EnumerationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">EnumerationUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/EnumerationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>EnumerationUsage</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitEventOccurrenceUsage(com.dassault_systemes.modeler.sysml.model.sysml.EventOccurrenceUsage,C)">
<h3 id="visitEventOccurrenceUsage(com.dassault_systemes.modeler.sysml.model.sysml.EventOccurrenceUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitEventOccurrenceUsage</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitEventOccurrenceUsage</span><wbr/><span class="parameters">(<a href="sysml/EventOccurrenceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">EventOccurrenceUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/EventOccurrenceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>EventOccurrenceUsage</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitExhibitStateUsage(com.dassault_systemes.modeler.sysml.model.sysml.ExhibitStateUsage,C)">
<h3 id="visitExhibitStateUsage(com.dassault_systemes.modeler.sysml.model.sysml.ExhibitStateUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitExhibitStateUsage</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitExhibitStateUsage</span><wbr/><span class="parameters">(<a href="sysml/ExhibitStateUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ExhibitStateUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/ExhibitStateUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ExhibitStateUsage</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitExpose(com.dassault_systemes.modeler.sysml.model.sysml.Expose,C)">
<h3 id="visitExpose(com.dassault_systemes.modeler.sysml.model.sysml.Expose,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitExpose</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitExpose</span><wbr/><span class="parameters">(<a href="sysml/Expose.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Expose</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/Expose.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>Expose</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitFlowDefinition(com.dassault_systemes.modeler.sysml.model.sysml.FlowDefinition,C)">
<h3 id="visitFlowDefinition(com.dassault_systemes.modeler.sysml.model.sysml.FlowDefinition,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitFlowDefinition</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitFlowDefinition</span><wbr/><span class="parameters">(<a href="sysml/FlowDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">FlowDefinition</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/FlowDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>FlowDefinition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitFlowUsage(com.dassault_systemes.modeler.sysml.model.sysml.FlowUsage,C)">
<h3 id="visitFlowUsage(com.dassault_systemes.modeler.sysml.model.sysml.FlowUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitFlowUsage</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitFlowUsage</span><wbr/><span class="parameters">(<a href="sysml/FlowUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">FlowUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/FlowUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>FlowUsage</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitForLoopActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.ForLoopActionUsage,C)">
<h3 id="visitForLoopActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.ForLoopActionUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitForLoopActionUsage</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitForLoopActionUsage</span><wbr/><span class="parameters">(<a href="sysml/ForLoopActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ForLoopActionUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/ForLoopActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ForLoopActionUsage</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitForkNode(com.dassault_systemes.modeler.sysml.model.sysml.ForkNode,C)">
<h3 id="visitForkNode(com.dassault_systemes.modeler.sysml.model.sysml.ForkNode,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitForkNode</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitForkNode</span><wbr/><span class="parameters">(<a href="sysml/ForkNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ForkNode</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/ForkNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ForkNode</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitFramedConcernMembership(com.dassault_systemes.modeler.sysml.model.sysml.FramedConcernMembership,C)">
<h3 id="visitFramedConcernMembership(com.dassault_systemes.modeler.sysml.model.sysml.FramedConcernMembership,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitFramedConcernMembership</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitFramedConcernMembership</span><wbr/><span class="parameters">(<a href="sysml/FramedConcernMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">FramedConcernMembership</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/FramedConcernMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>FramedConcernMembership</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitIfActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.IfActionUsage,C)">
<h3 id="visitIfActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.IfActionUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitIfActionUsage</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitIfActionUsage</span><wbr/><span class="parameters">(<a href="sysml/IfActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">IfActionUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/IfActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>IfActionUsage</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitIncludeUseCaseUsage(com.dassault_systemes.modeler.sysml.model.sysml.IncludeUseCaseUsage,C)">
<h3 id="visitIncludeUseCaseUsage(com.dassault_systemes.modeler.sysml.model.sysml.IncludeUseCaseUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitIncludeUseCaseUsage</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitIncludeUseCaseUsage</span><wbr/><span class="parameters">(<a href="sysml/IncludeUseCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">IncludeUseCaseUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/IncludeUseCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>IncludeUseCaseUsage</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInterfaceDefinition(com.dassault_systemes.modeler.sysml.model.sysml.InterfaceDefinition,C)">
<h3 id="visitInterfaceDefinition(com.dassault_systemes.modeler.sysml.model.sysml.InterfaceDefinition,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitInterfaceDefinition</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitInterfaceDefinition</span><wbr/><span class="parameters">(<a href="sysml/InterfaceDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">InterfaceDefinition</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/InterfaceDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>InterfaceDefinition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInterfaceUsage(com.dassault_systemes.modeler.sysml.model.sysml.InterfaceUsage,C)">
<h3 id="visitInterfaceUsage(com.dassault_systemes.modeler.sysml.model.sysml.InterfaceUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitInterfaceUsage</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitInterfaceUsage</span><wbr/><span class="parameters">(<a href="sysml/InterfaceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">InterfaceUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/InterfaceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>InterfaceUsage</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitItemDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ItemDefinition,C)">
<h3 id="visitItemDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ItemDefinition,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitItemDefinition</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitItemDefinition</span><wbr/><span class="parameters">(<a href="sysml/ItemDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ItemDefinition</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/ItemDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ItemDefinition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitItemUsage(com.dassault_systemes.modeler.sysml.model.sysml.ItemUsage,C)">
<h3 id="visitItemUsage(com.dassault_systemes.modeler.sysml.model.sysml.ItemUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitItemUsage</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitItemUsage</span><wbr/><span class="parameters">(<a href="sysml/ItemUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ItemUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/ItemUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ItemUsage</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitJoinNode(com.dassault_systemes.modeler.sysml.model.sysml.JoinNode,C)">
<h3 id="visitJoinNode(com.dassault_systemes.modeler.sysml.model.sysml.JoinNode,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitJoinNode</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitJoinNode</span><wbr/><span class="parameters">(<a href="sysml/JoinNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">JoinNode</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/JoinNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>JoinNode</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitLoopActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.LoopActionUsage,C)">
<h3 id="visitLoopActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.LoopActionUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitLoopActionUsage</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitLoopActionUsage</span><wbr/><span class="parameters">(<a href="sysml/LoopActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">LoopActionUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/LoopActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>LoopActionUsage</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitMembershipExpose(com.dassault_systemes.modeler.sysml.model.sysml.MembershipExpose,C)">
<h3 id="visitMembershipExpose(com.dassault_systemes.modeler.sysml.model.sysml.MembershipExpose,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitMembershipExpose</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitMembershipExpose</span><wbr/><span class="parameters">(<a href="sysml/MembershipExpose.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">MembershipExpose</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/MembershipExpose.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>MembershipExpose</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitMergeNode(com.dassault_systemes.modeler.sysml.model.sysml.MergeNode,C)">
<h3 id="visitMergeNode(com.dassault_systemes.modeler.sysml.model.sysml.MergeNode,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitMergeNode</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitMergeNode</span><wbr/><span class="parameters">(<a href="sysml/MergeNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">MergeNode</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/MergeNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>MergeNode</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitMetadataDefinition(com.dassault_systemes.modeler.sysml.model.sysml.MetadataDefinition,C)">
<h3 id="visitMetadataDefinition(com.dassault_systemes.modeler.sysml.model.sysml.MetadataDefinition,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitMetadataDefinition</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitMetadataDefinition</span><wbr/><span class="parameters">(<a href="sysml/MetadataDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">MetadataDefinition</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/MetadataDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>MetadataDefinition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitMetadataUsage(com.dassault_systemes.modeler.sysml.model.sysml.MetadataUsage,C)">
<h3 id="visitMetadataUsage(com.dassault_systemes.modeler.sysml.model.sysml.MetadataUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitMetadataUsage</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitMetadataUsage</span><wbr/><span class="parameters">(<a href="sysml/MetadataUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">MetadataUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/MetadataUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>MetadataUsage</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitNamespaceExpose(com.dassault_systemes.modeler.sysml.model.sysml.NamespaceExpose,C)">
<h3 id="visitNamespaceExpose(com.dassault_systemes.modeler.sysml.model.sysml.NamespaceExpose,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitNamespaceExpose</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitNamespaceExpose</span><wbr/><span class="parameters">(<a href="sysml/NamespaceExpose.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">NamespaceExpose</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/NamespaceExpose.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>NamespaceExpose</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitObjectiveMembership(com.dassault_systemes.modeler.sysml.model.sysml.ObjectiveMembership,C)">
<h3 id="visitObjectiveMembership(com.dassault_systemes.modeler.sysml.model.sysml.ObjectiveMembership,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitObjectiveMembership</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitObjectiveMembership</span><wbr/><span class="parameters">(<a href="sysml/ObjectiveMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ObjectiveMembership</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/ObjectiveMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ObjectiveMembership</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitOccurrenceDefinition(com.dassault_systemes.modeler.sysml.model.sysml.OccurrenceDefinition,C)">
<h3 id="visitOccurrenceDefinition(com.dassault_systemes.modeler.sysml.model.sysml.OccurrenceDefinition,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitOccurrenceDefinition</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitOccurrenceDefinition</span><wbr/><span class="parameters">(<a href="sysml/OccurrenceDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">OccurrenceDefinition</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/OccurrenceDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>OccurrenceDefinition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitOccurrenceUsage(com.dassault_systemes.modeler.sysml.model.sysml.OccurrenceUsage,C)">
<h3 id="visitOccurrenceUsage(com.dassault_systemes.modeler.sysml.model.sysml.OccurrenceUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitOccurrenceUsage</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitOccurrenceUsage</span><wbr/><span class="parameters">(<a href="sysml/OccurrenceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">OccurrenceUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/OccurrenceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>OccurrenceUsage</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPartDefinition(com.dassault_systemes.modeler.sysml.model.sysml.PartDefinition,C)">
<h3 id="visitPartDefinition(com.dassault_systemes.modeler.sysml.model.sysml.PartDefinition,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitPartDefinition</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitPartDefinition</span><wbr/><span class="parameters">(<a href="sysml/PartDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PartDefinition</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/PartDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>PartDefinition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPartUsage(com.dassault_systemes.modeler.sysml.model.sysml.PartUsage,C)">
<h3 id="visitPartUsage(com.dassault_systemes.modeler.sysml.model.sysml.PartUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitPartUsage</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitPartUsage</span><wbr/><span class="parameters">(<a href="sysml/PartUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PartUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/PartUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>PartUsage</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPerformActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.PerformActionUsage,C)">
<h3 id="visitPerformActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.PerformActionUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitPerformActionUsage</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitPerformActionUsage</span><wbr/><span class="parameters">(<a href="sysml/PerformActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PerformActionUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/PerformActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>PerformActionUsage</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPortConjugation(com.dassault_systemes.modeler.sysml.model.sysml.PortConjugation,C)">
<h3 id="visitPortConjugation(com.dassault_systemes.modeler.sysml.model.sysml.PortConjugation,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitPortConjugation</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitPortConjugation</span><wbr/><span class="parameters">(<a href="sysml/PortConjugation.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PortConjugation</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/PortConjugation.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>PortConjugation</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPortDefinition(com.dassault_systemes.modeler.sysml.model.sysml.PortDefinition,C)">
<h3 id="visitPortDefinition(com.dassault_systemes.modeler.sysml.model.sysml.PortDefinition,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitPortDefinition</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitPortDefinition</span><wbr/><span class="parameters">(<a href="sysml/PortDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PortDefinition</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/PortDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>PortDefinition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPortUsage(com.dassault_systemes.modeler.sysml.model.sysml.PortUsage,C)">
<h3 id="visitPortUsage(com.dassault_systemes.modeler.sysml.model.sysml.PortUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitPortUsage</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitPortUsage</span><wbr/><span class="parameters">(<a href="sysml/PortUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PortUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/PortUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>PortUsage</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitReferenceUsage(com.dassault_systemes.modeler.sysml.model.sysml.ReferenceUsage,C)">
<h3 id="visitReferenceUsage(com.dassault_systemes.modeler.sysml.model.sysml.ReferenceUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitReferenceUsage</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitReferenceUsage</span><wbr/><span class="parameters">(<a href="sysml/ReferenceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ReferenceUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/ReferenceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ReferenceUsage</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitRenderingDefinition(com.dassault_systemes.modeler.sysml.model.sysml.RenderingDefinition,C)">
<h3 id="visitRenderingDefinition(com.dassault_systemes.modeler.sysml.model.sysml.RenderingDefinition,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitRenderingDefinition</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitRenderingDefinition</span><wbr/><span class="parameters">(<a href="sysml/RenderingDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RenderingDefinition</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/RenderingDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>RenderingDefinition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitRenderingUsage(com.dassault_systemes.modeler.sysml.model.sysml.RenderingUsage,C)">
<h3 id="visitRenderingUsage(com.dassault_systemes.modeler.sysml.model.sysml.RenderingUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitRenderingUsage</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitRenderingUsage</span><wbr/><span class="parameters">(<a href="sysml/RenderingUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RenderingUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/RenderingUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>RenderingUsage</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitRequirementConstraintMembership(com.dassault_systemes.modeler.sysml.model.sysml.RequirementConstraintMembership,C)">
<h3 id="visitRequirementConstraintMembership(com.dassault_systemes.modeler.sysml.model.sysml.RequirementConstraintMembership,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitRequirementConstraintMembership</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitRequirementConstraintMembership</span><wbr/><span class="parameters">(<a href="sysml/RequirementConstraintMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementConstraintMembership</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/RequirementConstraintMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>RequirementConstraintMembership</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitRequirementDefinition(com.dassault_systemes.modeler.sysml.model.sysml.RequirementDefinition,C)">
<h3 id="visitRequirementDefinition(com.dassault_systemes.modeler.sysml.model.sysml.RequirementDefinition,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitRequirementDefinition</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitRequirementDefinition</span><wbr/><span class="parameters">(<a href="sysml/RequirementDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementDefinition</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/RequirementDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>RequirementDefinition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitRequirementUsage(com.dassault_systemes.modeler.sysml.model.sysml.RequirementUsage,C)">
<h3 id="visitRequirementUsage(com.dassault_systemes.modeler.sysml.model.sysml.RequirementUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitRequirementUsage</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitRequirementUsage</span><wbr/><span class="parameters">(<a href="sysml/RequirementUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/RequirementUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>RequirementUsage</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitRequirementVerificationMembership(com.dassault_systemes.modeler.sysml.model.sysml.RequirementVerificationMembership,C)">
<h3 id="visitRequirementVerificationMembership(com.dassault_systemes.modeler.sysml.model.sysml.RequirementVerificationMembership,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitRequirementVerificationMembership</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitRequirementVerificationMembership</span><wbr/><span class="parameters">(<a href="sysml/RequirementVerificationMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementVerificationMembership</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/RequirementVerificationMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>RequirementVerificationMembership</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitSatisfyRequirementUsage(com.dassault_systemes.modeler.sysml.model.sysml.SatisfyRequirementUsage,C)">
<h3 id="visitSatisfyRequirementUsage(com.dassault_systemes.modeler.sysml.model.sysml.SatisfyRequirementUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitSatisfyRequirementUsage</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitSatisfyRequirementUsage</span><wbr/><span class="parameters">(<a href="sysml/SatisfyRequirementUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SatisfyRequirementUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/SatisfyRequirementUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>SatisfyRequirementUsage</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitSendActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.SendActionUsage,C)">
<h3 id="visitSendActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.SendActionUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitSendActionUsage</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitSendActionUsage</span><wbr/><span class="parameters">(<a href="sysml/SendActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SendActionUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/SendActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>SendActionUsage</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitStakeholderMembership(com.dassault_systemes.modeler.sysml.model.sysml.StakeholderMembership,C)">
<h3 id="visitStakeholderMembership(com.dassault_systemes.modeler.sysml.model.sysml.StakeholderMembership,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitStakeholderMembership</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitStakeholderMembership</span><wbr/><span class="parameters">(<a href="sysml/StakeholderMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">StakeholderMembership</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/StakeholderMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>StakeholderMembership</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitStateDefinition(com.dassault_systemes.modeler.sysml.model.sysml.StateDefinition,C)">
<h3 id="visitStateDefinition(com.dassault_systemes.modeler.sysml.model.sysml.StateDefinition,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitStateDefinition</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitStateDefinition</span><wbr/><span class="parameters">(<a href="sysml/StateDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">StateDefinition</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/StateDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>StateDefinition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitStateSubactionMembership(com.dassault_systemes.modeler.sysml.model.sysml.StateSubactionMembership,C)">
<h3 id="visitStateSubactionMembership(com.dassault_systemes.modeler.sysml.model.sysml.StateSubactionMembership,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitStateSubactionMembership</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitStateSubactionMembership</span><wbr/><span class="parameters">(<a href="sysml/StateSubactionMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">StateSubactionMembership</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/StateSubactionMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>StateSubactionMembership</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitStateUsage(com.dassault_systemes.modeler.sysml.model.sysml.StateUsage,C)">
<h3 id="visitStateUsage(com.dassault_systemes.modeler.sysml.model.sysml.StateUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitStateUsage</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitStateUsage</span><wbr/><span class="parameters">(<a href="sysml/StateUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">StateUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/StateUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>StateUsage</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitSubjectMembership(com.dassault_systemes.modeler.sysml.model.sysml.SubjectMembership,C)">
<h3 id="visitSubjectMembership(com.dassault_systemes.modeler.sysml.model.sysml.SubjectMembership,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitSubjectMembership</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitSubjectMembership</span><wbr/><span class="parameters">(<a href="sysml/SubjectMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SubjectMembership</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/SubjectMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>SubjectMembership</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitSuccessionAsUsage(com.dassault_systemes.modeler.sysml.model.sysml.SuccessionAsUsage,C)">
<h3 id="visitSuccessionAsUsage(com.dassault_systemes.modeler.sysml.model.sysml.SuccessionAsUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitSuccessionAsUsage</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitSuccessionAsUsage</span><wbr/><span class="parameters">(<a href="sysml/SuccessionAsUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SuccessionAsUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/SuccessionAsUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>SuccessionAsUsage</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitSuccessionFlowUsage(com.dassault_systemes.modeler.sysml.model.sysml.SuccessionFlowUsage,C)">
<h3 id="visitSuccessionFlowUsage(com.dassault_systemes.modeler.sysml.model.sysml.SuccessionFlowUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitSuccessionFlowUsage</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitSuccessionFlowUsage</span><wbr/><span class="parameters">(<a href="sysml/SuccessionFlowUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SuccessionFlowUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/SuccessionFlowUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>SuccessionFlowUsage</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTerminateActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.TerminateActionUsage,C)">
<h3 id="visitTerminateActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.TerminateActionUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitTerminateActionUsage</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitTerminateActionUsage</span><wbr/><span class="parameters">(<a href="sysml/TerminateActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TerminateActionUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/TerminateActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>TerminateActionUsage</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTransitionFeatureMembership(com.dassault_systemes.modeler.sysml.model.sysml.TransitionFeatureMembership,C)">
<h3 id="visitTransitionFeatureMembership(com.dassault_systemes.modeler.sysml.model.sysml.TransitionFeatureMembership,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitTransitionFeatureMembership</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitTransitionFeatureMembership</span><wbr/><span class="parameters">(<a href="sysml/TransitionFeatureMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TransitionFeatureMembership</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/TransitionFeatureMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>TransitionFeatureMembership</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTransitionUsage(com.dassault_systemes.modeler.sysml.model.sysml.TransitionUsage,C)">
<h3 id="visitTransitionUsage(com.dassault_systemes.modeler.sysml.model.sysml.TransitionUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitTransitionUsage</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitTransitionUsage</span><wbr/><span class="parameters">(<a href="sysml/TransitionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TransitionUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/TransitionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>TransitionUsage</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTriggerInvocationExpression(com.dassault_systemes.modeler.sysml.model.sysml.TriggerInvocationExpression,C)">
<h3 id="visitTriggerInvocationExpression(com.dassault_systemes.modeler.sysml.model.sysml.TriggerInvocationExpression,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitTriggerInvocationExpression</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitTriggerInvocationExpression</span><wbr/><span class="parameters">(<a href="sysml/TriggerInvocationExpression.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TriggerInvocationExpression</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/TriggerInvocationExpression.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>TriggerInvocationExpression</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitUsage(com.dassault_systemes.modeler.sysml.model.sysml.Usage,C)">
<h3 id="visitUsage(com.dassault_systemes.modeler.sysml.model.sysml.Usage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitUsage</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitUsage</span><wbr/><span class="parameters">(<a href="sysml/Usage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Usage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/Usage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>Usage</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitUseCaseDefinition(com.dassault_systemes.modeler.sysml.model.sysml.UseCaseDefinition,C)">
<h3 id="visitUseCaseDefinition(com.dassault_systemes.modeler.sysml.model.sysml.UseCaseDefinition,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitUseCaseDefinition</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitUseCaseDefinition</span><wbr/><span class="parameters">(<a href="sysml/UseCaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">UseCaseDefinition</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/UseCaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>UseCaseDefinition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitUseCaseUsage(com.dassault_systemes.modeler.sysml.model.sysml.UseCaseUsage,C)">
<h3 id="visitUseCaseUsage(com.dassault_systemes.modeler.sysml.model.sysml.UseCaseUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitUseCaseUsage</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitUseCaseUsage</span><wbr/><span class="parameters">(<a href="sysml/UseCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">UseCaseUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/UseCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>UseCaseUsage</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitVariantMembership(com.dassault_systemes.modeler.sysml.model.sysml.VariantMembership,C)">
<h3 id="visitVariantMembership(com.dassault_systemes.modeler.sysml.model.sysml.VariantMembership,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitVariantMembership</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitVariantMembership</span><wbr/><span class="parameters">(<a href="sysml/VariantMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">VariantMembership</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/VariantMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>VariantMembership</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitVerificationCaseDefinition(com.dassault_systemes.modeler.sysml.model.sysml.VerificationCaseDefinition,C)">
<h3 id="visitVerificationCaseDefinition(com.dassault_systemes.modeler.sysml.model.sysml.VerificationCaseDefinition,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitVerificationCaseDefinition</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitVerificationCaseDefinition</span><wbr/><span class="parameters">(<a href="sysml/VerificationCaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">VerificationCaseDefinition</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/VerificationCaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>VerificationCaseDefinition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitVerificationCaseUsage(com.dassault_systemes.modeler.sysml.model.sysml.VerificationCaseUsage,C)">
<h3 id="visitVerificationCaseUsage(com.dassault_systemes.modeler.sysml.model.sysml.VerificationCaseUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitVerificationCaseUsage</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitVerificationCaseUsage</span><wbr/><span class="parameters">(<a href="sysml/VerificationCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">VerificationCaseUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/VerificationCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>VerificationCaseUsage</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitViewDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ViewDefinition,C)">
<h3 id="visitViewDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ViewDefinition,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitViewDefinition</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitViewDefinition</span><wbr/><span class="parameters">(<a href="sysml/ViewDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewDefinition</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/ViewDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ViewDefinition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitViewRenderingMembership(com.dassault_systemes.modeler.sysml.model.sysml.ViewRenderingMembership,C)">
<h3 id="visitViewRenderingMembership(com.dassault_systemes.modeler.sysml.model.sysml.ViewRenderingMembership,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitViewRenderingMembership</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitViewRenderingMembership</span><wbr/><span class="parameters">(<a href="sysml/ViewRenderingMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewRenderingMembership</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/ViewRenderingMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ViewRenderingMembership</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitViewUsage(com.dassault_systemes.modeler.sysml.model.sysml.ViewUsage,C)">
<h3 id="visitViewUsage(com.dassault_systemes.modeler.sysml.model.sysml.ViewUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitViewUsage</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitViewUsage</span><wbr/><span class="parameters">(<a href="sysml/ViewUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/ViewUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ViewUsage</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitViewpointDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ViewpointDefinition,C)">
<h3 id="visitViewpointDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ViewpointDefinition,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitViewpointDefinition</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitViewpointDefinition</span><wbr/><span class="parameters">(<a href="sysml/ViewpointDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewpointDefinition</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/ViewpointDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ViewpointDefinition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitViewpointUsage(com.dassault_systemes.modeler.sysml.model.sysml.ViewpointUsage,C)">
<h3 id="visitViewpointUsage(com.dassault_systemes.modeler.sysml.model.sysml.ViewpointUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitViewpointUsage</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitViewpointUsage</span><wbr/><span class="parameters">(<a href="sysml/ViewpointUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewpointUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/ViewpointUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ViewpointUsage</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitWhileLoopActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.WhileLoopActionUsage,C)">
<h3 id="visitWhileLoopActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.WhileLoopActionUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitWhileLoopActionUsage</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitWhileLoopActionUsage</span><wbr/><span class="parameters">(<a href="sysml/WhileLoopActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">WhileLoopActionUsage</a> element,
 <a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="sysml/WhileLoopActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>WhileLoopActionUsage</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createVisitorContext()">
<h3>createVisitorContext</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a></span> <span class="element-name">createVisitorContext</span>()</div>
<div class="block"><span class="description-from-type-label">Description copied from interface: <code><a href="../../kerml/model/KerMLModelVisitor.html#createVisitorContext()">KerMLModelVisitor</a></code></span></div>
<div class="block">Creates a new visitor context.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../kerml/model/KerMLModelVisitor.html#createVisitorContext()">createVisitorContext</a></code> in interface <code><a href="../../kerml/model/KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="SysMLModelVisitor.html" title="type parameter in SysMLModelVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Returns:</dt>
<dd>A new instance of <code>KerMLVisitorContextImpl</code>.</dd>
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
