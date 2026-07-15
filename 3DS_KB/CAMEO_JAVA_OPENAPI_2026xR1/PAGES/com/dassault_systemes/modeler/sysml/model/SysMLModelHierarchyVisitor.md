# JAVA OPENAPI: SysMLModelHierarchyVisitor (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/sysml/model/SysMLModelHierarchyVisitor.html
- source_path: `com/dassault_systemes/modeler/sysml/model/SysMLModelHierarchyVisitor.html`
- source_sha256: `956dbf6d90ffc27498b07a99444eb7cb56b63700b69a423f675be51b445f9e03`
- captured_utc: `2026-07-14T16:45:03.673052+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.sysml.model](package-summary.html)

## Interface SysMLModelHierarchyVisitor<C extends [SysMLVisitorContext](SysMLVisitorContext.html)>

Type Parameters:
`C` - the type of the visitor context

All Superinterfaces:
`[AbstractVisitor](../../../../nomagic/magicdraw/uml/AbstractVisitor.html)`, `[KerMLModelHierarchyVisitor](../../kerml/model/KerMLModelHierarchyVisitor.html)<C>`, `[KerMLModelVisitor](../../kerml/model/KerMLModelVisitor.html)<C>`, `[SysMLModelVisitor](SysMLModelVisitor.html)<C>`

@OpenApiAllpublic interfaceSysMLModelHierarchyVisitor<C extends [SysMLVisitorContext](SysMLVisitorContext.html)>extends [KerMLModelHierarchyVisitor](../../kerml/model/KerMLModelHierarchyVisitor.html)<C>, [SysMLModelVisitor](SysMLModelVisitor.html)<C>

This interface extends KerMLModelHierarchyVisitor and SysMLModelVisitor to provide
 a visitor pattern implementation for traversing SysML model elements.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsDefault Methods
Modifier and Type
Method
Description
`default org.eclipse.emf.ecore.EPackage`
`[getEPackage](#getEPackage())()`
Returns the EPackage that this visitor is suited for.
`default boolean`
`[isAcceptable](#isAcceptable(org.eclipse.emf.ecore.EPackage))(org.eclipse.emf.ecore.EPackage ePackage)`
Checks if the given EPackage elements are acceptable by the visitor.
`default void`
`[visitAcceptActionUsage](#visitAcceptActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.AcceptActionUsage,C))([AcceptActionUsage](sysml/AcceptActionUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits an AcceptActionUsage element.
`default void`
`[visitActionDefinition](#visitActionDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ActionDefinition,C))([ActionDefinition](sysml/ActionDefinition.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits an ActionDefinition element.
`default void`
`[visitActionUsage](#visitActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.ActionUsage,C))([ActionUsage](sysml/ActionUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits an ActionUsage element.
`default void`
`[visitActorMembership](#visitActorMembership(com.dassault_systemes.modeler.sysml.model.sysml.ActorMembership,C))([ActorMembership](sysml/ActorMembership.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits an ActorMembership element.
`default void`
`[visitAllocationDefinition](#visitAllocationDefinition(com.dassault_systemes.modeler.sysml.model.sysml.AllocationDefinition,C))([AllocationDefinition](sysml/AllocationDefinition.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits an AllocationDefinition element.
`default void`
`[visitAllocationUsage](#visitAllocationUsage(com.dassault_systemes.modeler.sysml.model.sysml.AllocationUsage,C))([AllocationUsage](sysml/AllocationUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits an AllocationUsage element.
`default void`
`[visitAnalysisCaseDefinition](#visitAnalysisCaseDefinition(com.dassault_systemes.modeler.sysml.model.sysml.AnalysisCaseDefinition,C))([AnalysisCaseDefinition](sysml/AnalysisCaseDefinition.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits an AnalysisCaseDefinition element.
`default void`
`[visitAnalysisCaseUsage](#visitAnalysisCaseUsage(com.dassault_systemes.modeler.sysml.model.sysml.AnalysisCaseUsage,C))([AnalysisCaseUsage](sysml/AnalysisCaseUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits an AnalysisCaseUsage element.
`default void`
`[visitAssertConstraintUsage](#visitAssertConstraintUsage(com.dassault_systemes.modeler.sysml.model.sysml.AssertConstraintUsage,C))([AssertConstraintUsage](sysml/AssertConstraintUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits an AssertConstraintUsage element.
`default void`
`[visitAssignmentActionUsage](#visitAssignmentActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.AssignmentActionUsage,C))([AssignmentActionUsage](sysml/AssignmentActionUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits an AssignmentActionUsage element.
`default void`
`[visitAttributeDefinition](#visitAttributeDefinition(com.dassault_systemes.modeler.sysml.model.sysml.AttributeDefinition,C))([AttributeDefinition](sysml/AttributeDefinition.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits an AttributeDefinition element.
`default void`
`[visitAttributeUsage](#visitAttributeUsage(com.dassault_systemes.modeler.sysml.model.sysml.AttributeUsage,C))([AttributeUsage](sysml/AttributeUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits an AttributeUsage element.
`default void`
`[visitBindingConnectorAsUsage](#visitBindingConnectorAsUsage(com.dassault_systemes.modeler.sysml.model.sysml.BindingConnectorAsUsage,C))([BindingConnectorAsUsage](sysml/BindingConnectorAsUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a BindingConnectorAsUsage element.
`default void`
`[visitCalculationDefinition](#visitCalculationDefinition(com.dassault_systemes.modeler.sysml.model.sysml.CalculationDefinition,C))([CalculationDefinition](sysml/CalculationDefinition.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a CalculationDefinition element.
`default void`
`[visitCalculationUsage](#visitCalculationUsage(com.dassault_systemes.modeler.sysml.model.sysml.CalculationUsage,C))([CalculationUsage](sysml/CalculationUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a CalculationUsage element.
`default void`
`[visitCaseDefinition](#visitCaseDefinition(com.dassault_systemes.modeler.sysml.model.sysml.CaseDefinition,C))([CaseDefinition](sysml/CaseDefinition.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a CaseDefinition element.
`default void`
`[visitCaseUsage](#visitCaseUsage(com.dassault_systemes.modeler.sysml.model.sysml.CaseUsage,C))([CaseUsage](sysml/CaseUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a CaseUsage element.
`default void`
`[visitConcernDefinition](#visitConcernDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ConcernDefinition,C))([ConcernDefinition](sysml/ConcernDefinition.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a ConcernDefinition element.
`default void`
`[visitConcernUsage](#visitConcernUsage(com.dassault_systemes.modeler.sysml.model.sysml.ConcernUsage,C))([ConcernUsage](sysml/ConcernUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a ConcernUsage element.
`default void`
`[visitConjugatedPortDefinition](#visitConjugatedPortDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ConjugatedPortDefinition,C))([ConjugatedPortDefinition](sysml/ConjugatedPortDefinition.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a ConjugatedPortDefinition element.
`default void`
`[visitConjugatedPortTyping](#visitConjugatedPortTyping(com.dassault_systemes.modeler.sysml.model.sysml.ConjugatedPortTyping,C))([ConjugatedPortTyping](sysml/ConjugatedPortTyping.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a ConjugatedPortTyping element.
`default void`
`[visitConnectionDefinition](#visitConnectionDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ConnectionDefinition,C))([ConnectionDefinition](sysml/ConnectionDefinition.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a ConnectionDefinition element.
`default void`
`[visitConnectionUsage](#visitConnectionUsage(com.dassault_systemes.modeler.sysml.model.sysml.ConnectionUsage,C))([ConnectionUsage](sysml/ConnectionUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a ConnectionUsage element.
`default void`
`[visitConnectorAsUsage](#visitConnectorAsUsage(com.dassault_systemes.modeler.sysml.model.sysml.ConnectorAsUsage,C))([ConnectorAsUsage](sysml/ConnectorAsUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a ConnectorAsUsage element.
`default void`
`[visitConstraintDefinition](#visitConstraintDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ConstraintDefinition,C))([ConstraintDefinition](sysml/ConstraintDefinition.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a ConstraintDefinition element.
`default void`
`[visitConstraintUsage](#visitConstraintUsage(com.dassault_systemes.modeler.sysml.model.sysml.ConstraintUsage,C))([ConstraintUsage](sysml/ConstraintUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a ConstraintUsage element.
`default void`
`[visitControlNode](#visitControlNode(com.dassault_systemes.modeler.sysml.model.sysml.ControlNode,C))([ControlNode](sysml/ControlNode.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a ControlNode element.
`default void`
`[visitDecisionNode](#visitDecisionNode(com.dassault_systemes.modeler.sysml.model.sysml.DecisionNode,C))([DecisionNode](sysml/DecisionNode.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a DecisionNode element.
`default void`
`[visitDefinition](#visitDefinition(com.dassault_systemes.modeler.sysml.model.sysml.Definition,C))([Definition](sysml/Definition.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a Definition element.
`default void`
`[visitEnumerationDefinition](#visitEnumerationDefinition(com.dassault_systemes.modeler.sysml.model.sysml.EnumerationDefinition,C))([EnumerationDefinition](sysml/EnumerationDefinition.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits an EnumerationDefinition element.
`default void`
`[visitEnumerationUsage](#visitEnumerationUsage(com.dassault_systemes.modeler.sysml.model.sysml.EnumerationUsage,C))([EnumerationUsage](sysml/EnumerationUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits an EnumerationUsage element.
`default void`
`[visitEventOccurrenceUsage](#visitEventOccurrenceUsage(com.dassault_systemes.modeler.sysml.model.sysml.EventOccurrenceUsage,C))([EventOccurrenceUsage](sysml/EventOccurrenceUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits an EventOccurrenceUsage element.
`default void`
`[visitExhibitStateUsage](#visitExhibitStateUsage(com.dassault_systemes.modeler.sysml.model.sysml.ExhibitStateUsage,C))([ExhibitStateUsage](sysml/ExhibitStateUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits an ExhibitStateUsage element.
`default void`
`[visitExpose](#visitExpose(com.dassault_systemes.modeler.sysml.model.sysml.Expose,C))([Expose](sysml/Expose.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits an Expose element.
`default void`
`[visitFlowDefinition](#visitFlowDefinition(com.dassault_systemes.modeler.sysml.model.sysml.FlowDefinition,C))([FlowDefinition](sysml/FlowDefinition.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a FlowDefinition element.
`default void`
`[visitFlowUsage](#visitFlowUsage(com.dassault_systemes.modeler.sysml.model.sysml.FlowUsage,C))([FlowUsage](sysml/FlowUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a FlowUsage element.
`default void`
`[visitForkNode](#visitForkNode(com.dassault_systemes.modeler.sysml.model.sysml.ForkNode,C))([ForkNode](sysml/ForkNode.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a ForkNode element.
`default void`
`[visitForLoopActionUsage](#visitForLoopActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.ForLoopActionUsage,C))([ForLoopActionUsage](sysml/ForLoopActionUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a ForLoopActionUsage element.
`default void`
`[visitFramedConcernMembership](#visitFramedConcernMembership(com.dassault_systemes.modeler.sysml.model.sysml.FramedConcernMembership,C))([FramedConcernMembership](sysml/FramedConcernMembership.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a FramedConcernMembership element.
`default void`
`[visitIfActionUsage](#visitIfActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.IfActionUsage,C))([IfActionUsage](sysml/IfActionUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits an IfActionUsage element.
`default void`
`[visitIncludeUseCaseUsage](#visitIncludeUseCaseUsage(com.dassault_systemes.modeler.sysml.model.sysml.IncludeUseCaseUsage,C))([IncludeUseCaseUsage](sysml/IncludeUseCaseUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits an IncludeUseCaseUsage element.
`default void`
`[visitInterfaceDefinition](#visitInterfaceDefinition(com.dassault_systemes.modeler.sysml.model.sysml.InterfaceDefinition,C))([InterfaceDefinition](sysml/InterfaceDefinition.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits an InterfaceDefinition element.
`default void`
`[visitInterfaceUsage](#visitInterfaceUsage(com.dassault_systemes.modeler.sysml.model.sysml.InterfaceUsage,C))([InterfaceUsage](sysml/InterfaceUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits an InterfaceUsage element.
`default void`
`[visitItemDefinition](#visitItemDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ItemDefinition,C))([ItemDefinition](sysml/ItemDefinition.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits an ItemDefinition element.
`default void`
`[visitItemUsage](#visitItemUsage(com.dassault_systemes.modeler.sysml.model.sysml.ItemUsage,C))([ItemUsage](sysml/ItemUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits an ItemUsage element.
`default void`
`[visitJoinNode](#visitJoinNode(com.dassault_systemes.modeler.sysml.model.sysml.JoinNode,C))([JoinNode](sysml/JoinNode.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a JoinNode element.
`default void`
`[visitLoopActionUsage](#visitLoopActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.LoopActionUsage,C))([LoopActionUsage](sysml/LoopActionUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a LoopActionUsage element.
`default void`
`[visitMembershipExpose](#visitMembershipExpose(com.dassault_systemes.modeler.sysml.model.sysml.MembershipExpose,C))([MembershipExpose](sysml/MembershipExpose.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a MembershipExpose element.
`default void`
`[visitMergeNode](#visitMergeNode(com.dassault_systemes.modeler.sysml.model.sysml.MergeNode,C))([MergeNode](sysml/MergeNode.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a MergeNode element.
`default void`
`[visitMetadataDefinition](#visitMetadataDefinition(com.dassault_systemes.modeler.sysml.model.sysml.MetadataDefinition,C))([MetadataDefinition](sysml/MetadataDefinition.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a MetadataDefinition element.
`default void`
`[visitMetadataUsage](#visitMetadataUsage(com.dassault_systemes.modeler.sysml.model.sysml.MetadataUsage,C))([MetadataUsage](sysml/MetadataUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a MetadataUsage element.
`default void`
`[visitNamespaceExpose](#visitNamespaceExpose(com.dassault_systemes.modeler.sysml.model.sysml.NamespaceExpose,C))([NamespaceExpose](sysml/NamespaceExpose.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a NamespaceExpose element.
`default void`
`[visitObjectiveMembership](#visitObjectiveMembership(com.dassault_systemes.modeler.sysml.model.sysml.ObjectiveMembership,C))([ObjectiveMembership](sysml/ObjectiveMembership.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits an ObjectiveMembership element.
`default void`
`[visitOccurrenceDefinition](#visitOccurrenceDefinition(com.dassault_systemes.modeler.sysml.model.sysml.OccurrenceDefinition,C))([OccurrenceDefinition](sysml/OccurrenceDefinition.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits an OccurrenceDefinition element.
`default void`
`[visitOccurrenceUsage](#visitOccurrenceUsage(com.dassault_systemes.modeler.sysml.model.sysml.OccurrenceUsage,C))([OccurrenceUsage](sysml/OccurrenceUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits an OccurrenceUsage element.
`default void`
`[visitPartDefinition](#visitPartDefinition(com.dassault_systemes.modeler.sysml.model.sysml.PartDefinition,C))([PartDefinition](sysml/PartDefinition.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a PartDefinition element.
`default void`
`[visitPartUsage](#visitPartUsage(com.dassault_systemes.modeler.sysml.model.sysml.PartUsage,C))([PartUsage](sysml/PartUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a PartUsage element.
`default void`
`[visitPerformActionUsage](#visitPerformActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.PerformActionUsage,C))([PerformActionUsage](sysml/PerformActionUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a PerformActionUsage element.
`default void`
`[visitPortConjugation](#visitPortConjugation(com.dassault_systemes.modeler.sysml.model.sysml.PortConjugation,C))([PortConjugation](sysml/PortConjugation.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a PortConjugation element.
`default void`
`[visitPortDefinition](#visitPortDefinition(com.dassault_systemes.modeler.sysml.model.sysml.PortDefinition,C))([PortDefinition](sysml/PortDefinition.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a PortDefinition element.
`default void`
`[visitPortUsage](#visitPortUsage(com.dassault_systemes.modeler.sysml.model.sysml.PortUsage,C))([PortUsage](sysml/PortUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a PortUsage element.
`default void`
`[visitReferenceUsage](#visitReferenceUsage(com.dassault_systemes.modeler.sysml.model.sysml.ReferenceUsage,C))([ReferenceUsage](sysml/ReferenceUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a ReferenceUsage element.
`default void`
`[visitRenderingDefinition](#visitRenderingDefinition(com.dassault_systemes.modeler.sysml.model.sysml.RenderingDefinition,C))([RenderingDefinition](sysml/RenderingDefinition.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a RenderingDefinition element.
`default void`
`[visitRenderingUsage](#visitRenderingUsage(com.dassault_systemes.modeler.sysml.model.sysml.RenderingUsage,C))([RenderingUsage](sysml/RenderingUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a RenderingUsage element.
`default void`
`[visitRequirementConstraintMembership](#visitRequirementConstraintMembership(com.dassault_systemes.modeler.sysml.model.sysml.RequirementConstraintMembership,C))([RequirementConstraintMembership](sysml/RequirementConstraintMembership.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a RequirementConstraintMembership element.
`default void`
`[visitRequirementDefinition](#visitRequirementDefinition(com.dassault_systemes.modeler.sysml.model.sysml.RequirementDefinition,C))([RequirementDefinition](sysml/RequirementDefinition.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a RequirementDefinition element.
`default void`
`[visitRequirementUsage](#visitRequirementUsage(com.dassault_systemes.modeler.sysml.model.sysml.RequirementUsage,C))([RequirementUsage](sysml/RequirementUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a RequirementUsage element.
`default void`
`[visitRequirementVerificationMembership](#visitRequirementVerificationMembership(com.dassault_systemes.modeler.sysml.model.sysml.RequirementVerificationMembership,C))([RequirementVerificationMembership](sysml/RequirementVerificationMembership.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a RequirementVerificationMembership element.
`default void`
`[visitSatisfyRequirementUsage](#visitSatisfyRequirementUsage(com.dassault_systemes.modeler.sysml.model.sysml.SatisfyRequirementUsage,C))([SatisfyRequirementUsage](sysml/SatisfyRequirementUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a SatisfyRequirementUsage element.
`default void`
`[visitSendActionUsage](#visitSendActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.SendActionUsage,C))([SendActionUsage](sysml/SendActionUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a SendActionUsage element.
`default void`
`[visitStakeholderMembership](#visitStakeholderMembership(com.dassault_systemes.modeler.sysml.model.sysml.StakeholderMembership,C))([StakeholderMembership](sysml/StakeholderMembership.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a StakeholderMembership element.
`default void`
`[visitStateDefinition](#visitStateDefinition(com.dassault_systemes.modeler.sysml.model.sysml.StateDefinition,C))([StateDefinition](sysml/StateDefinition.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a StateDefinition element.
`default void`
`[visitStateSubactionMembership](#visitStateSubactionMembership(com.dassault_systemes.modeler.sysml.model.sysml.StateSubactionMembership,C))([StateSubactionMembership](sysml/StateSubactionMembership.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a StateSubactionMembership element.
`default void`
`[visitStateUsage](#visitStateUsage(com.dassault_systemes.modeler.sysml.model.sysml.StateUsage,C))([StateUsage](sysml/StateUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a StateUsage element.
`default void`
`[visitSubjectMembership](#visitSubjectMembership(com.dassault_systemes.modeler.sysml.model.sysml.SubjectMembership,C))([SubjectMembership](sysml/SubjectMembership.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a SubjectMembership element.
`default void`
`[visitSuccessionAsUsage](#visitSuccessionAsUsage(com.dassault_systemes.modeler.sysml.model.sysml.SuccessionAsUsage,C))([SuccessionAsUsage](sysml/SuccessionAsUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a SuccessionAsUsage element.
`default void`
`[visitSuccessionFlowUsage](#visitSuccessionFlowUsage(com.dassault_systemes.modeler.sysml.model.sysml.SuccessionFlowUsage,C))([SuccessionFlowUsage](sysml/SuccessionFlowUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a SuccessionFlowUsage element.
`default void`
`[visitTerminateActionUsage](#visitTerminateActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.TerminateActionUsage,C))([TerminateActionUsage](sysml/TerminateActionUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a TerminateActionUsage element.
`default void`
`[visitTransitionFeatureMembership](#visitTransitionFeatureMembership(com.dassault_systemes.modeler.sysml.model.sysml.TransitionFeatureMembership,C))([TransitionFeatureMembership](sysml/TransitionFeatureMembership.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a TransitionFeatureMembership element.
`default void`
`[visitTransitionUsage](#visitTransitionUsage(com.dassault_systemes.modeler.sysml.model.sysml.TransitionUsage,C))([TransitionUsage](sysml/TransitionUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a TransitionUsage element.
`default void`
`[visitTriggerInvocationExpression](#visitTriggerInvocationExpression(com.dassault_systemes.modeler.sysml.model.sysml.TriggerInvocationExpression,C))([TriggerInvocationExpression](sysml/TriggerInvocationExpression.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a TriggerInvocationExpression element.
`default void`
`[visitUsage](#visitUsage(com.dassault_systemes.modeler.sysml.model.sysml.Usage,C))([Usage](sysml/Usage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a Usage element.
`default void`
`[visitUseCaseDefinition](#visitUseCaseDefinition(com.dassault_systemes.modeler.sysml.model.sysml.UseCaseDefinition,C))([UseCaseDefinition](sysml/UseCaseDefinition.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a UseCaseDefinition element.
`default void`
`[visitUseCaseUsage](#visitUseCaseUsage(com.dassault_systemes.modeler.sysml.model.sysml.UseCaseUsage,C))([UseCaseUsage](sysml/UseCaseUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a UseCaseUsage element.
`default void`
`[visitVariantMembership](#visitVariantMembership(com.dassault_systemes.modeler.sysml.model.sysml.VariantMembership,C))([VariantMembership](sysml/VariantMembership.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a VariantMembership element.
`default void`
`[visitVerificationCaseDefinition](#visitVerificationCaseDefinition(com.dassault_systemes.modeler.sysml.model.sysml.VerificationCaseDefinition,C))([VerificationCaseDefinition](sysml/VerificationCaseDefinition.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a VerificationCaseDefinition element.
`default void`
`[visitVerificationCaseUsage](#visitVerificationCaseUsage(com.dassault_systemes.modeler.sysml.model.sysml.VerificationCaseUsage,C))([VerificationCaseUsage](sysml/VerificationCaseUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a VerificationCaseUsage element.
`default void`
`[visitViewDefinition](#visitViewDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ViewDefinition,C))([ViewDefinition](sysml/ViewDefinition.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a ViewDefinition element.
`default void`
`[visitViewpointDefinition](#visitViewpointDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ViewpointDefinition,C))([ViewpointDefinition](sysml/ViewpointDefinition.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a ViewpointDefinition element.
`default void`
`[visitViewpointUsage](#visitViewpointUsage(com.dassault_systemes.modeler.sysml.model.sysml.ViewpointUsage,C))([ViewpointUsage](sysml/ViewpointUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a ViewpointUsage element.
`default void`
`[visitViewRenderingMembership](#visitViewRenderingMembership(com.dassault_systemes.modeler.sysml.model.sysml.ViewRenderingMembership,C))([ViewRenderingMembership](sysml/ViewRenderingMembership.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a ViewRenderingMembership element.
`default void`
`[visitViewUsage](#visitViewUsage(com.dassault_systemes.modeler.sysml.model.sysml.ViewUsage,C))([ViewUsage](sysml/ViewUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a ViewUsage element.
`default void`
`[visitWhileLoopActionUsage](#visitWhileLoopActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.WhileLoopActionUsage,C))([WhileLoopActionUsage](sysml/WhileLoopActionUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)`
Visits a WhileLoopActionUsage element.
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.[KerMLModelHierarchyVisitor](../../kerml/model/KerMLModelHierarchyVisitor.html)
`[visitAnnotatingElement](../../kerml/model/KerMLModelHierarchyVisitor.html#visitAnnotatingElement(com.dassault_systemes.modeler.kerml.model.kerml.AnnotatingElement,C)), [visitAnnotation](../../kerml/model/KerMLModelHierarchyVisitor.html#visitAnnotation(com.dassault_systemes.modeler.kerml.model.kerml.Annotation,C)), [visitAssociation](../../kerml/model/KerMLModelHierarchyVisitor.html#visitAssociation(com.dassault_systemes.modeler.kerml.model.kerml.Association,C)), [visitAssociationStructure](../../kerml/model/KerMLModelHierarchyVisitor.html#visitAssociationStructure(com.dassault_systemes.modeler.kerml.model.kerml.AssociationStructure,C)), [visitBehavior](../../kerml/model/KerMLModelHierarchyVisitor.html#visitBehavior(com.dassault_systemes.modeler.kerml.model.kerml.Behavior,C)), [visitBindingConnector](../../kerml/model/KerMLModelHierarchyVisitor.html#visitBindingConnector(com.dassault_systemes.modeler.kerml.model.kerml.BindingConnector,C)), [visitBooleanExpression](../../kerml/model/KerMLModelHierarchyVisitor.html#visitBooleanExpression(com.dassault_systemes.modeler.kerml.model.kerml.BooleanExpression,C)), [visitClass](../../kerml/model/KerMLModelHierarchyVisitor.html#visitClass(com.dassault_systemes.modeler.kerml.model.kerml.Class,C)), [visitClassifier](../../kerml/model/KerMLModelHierarchyVisitor.html#visitClassifier(com.dassault_systemes.modeler.kerml.model.kerml.Classifier,C)), [visitCollectExpression](../../kerml/model/KerMLModelHierarchyVisitor.html#visitCollectExpression(com.dassault_systemes.modeler.kerml.model.kerml.CollectExpression,C)), [visitComment](../../kerml/model/KerMLModelHierarchyVisitor.html#visitComment(com.dassault_systemes.modeler.kerml.model.kerml.Comment,C)), [visitConjugation](../../kerml/model/KerMLModelHierarchyVisitor.html#visitConjugation(com.dassault_systemes.modeler.kerml.model.kerml.Conjugation,C)), [visitConnector](../../kerml/model/KerMLModelHierarchyVisitor.html#visitConnector(com.dassault_systemes.modeler.kerml.model.kerml.Connector,C)), [visitConstructorExpression](../../kerml/model/KerMLModelHierarchyVisitor.html#visitConstructorExpression(com.dassault_systemes.modeler.kerml.model.kerml.ConstructorExpression,C)), [visitCrossSubsetting](../../kerml/model/KerMLModelHierarchyVisitor.html#visitCrossSubsetting(com.dassault_systemes.modeler.kerml.model.kerml.CrossSubsetting,C)), [visitDataType](../../kerml/model/KerMLModelHierarchyVisitor.html#visitDataType(com.dassault_systemes.modeler.kerml.model.kerml.DataType,C)), [visitDependency](../../kerml/model/KerMLModelHierarchyVisitor.html#visitDependency(com.dassault_systemes.modeler.kerml.model.kerml.Dependency,C)), [visitDifferencing](../../kerml/model/KerMLModelHierarchyVisitor.html#visitDifferencing(com.dassault_systemes.modeler.kerml.model.kerml.Differencing,C)), [visitDisjoining](../../kerml/model/KerMLModelHierarchyVisitor.html#visitDisjoining(com.dassault_systemes.modeler.kerml.model.kerml.Disjoining,C)), [visitDocumentation](../../kerml/model/KerMLModelHierarchyVisitor.html#visitDocumentation(com.dassault_systemes.modeler.kerml.model.kerml.Documentation,C)), [visitElement](../../kerml/model/KerMLModelHierarchyVisitor.html#visitElement(com.dassault_systemes.modeler.kerml.model.kerml.Element,C)), [visitElementFilterMembership](../../kerml/model/KerMLModelHierarchyVisitor.html#visitElementFilterMembership(com.dassault_systemes.modeler.kerml.model.kerml.ElementFilterMembership,C)), [visitEndFeatureMembership](../../kerml/model/KerMLModelHierarchyVisitor.html#visitEndFeatureMembership(com.dassault_systemes.modeler.kerml.model.kerml.EndFeatureMembership,C)), [visitExpression](../../kerml/model/KerMLModelHierarchyVisitor.html#visitExpression(com.dassault_systemes.modeler.kerml.model.kerml.Expression,C)), [visitFeature](../../kerml/model/KerMLModelHierarchyVisitor.html#visitFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature,C)), [visitFeatureChainExpression](../../kerml/model/KerMLModelHierarchyVisitor.html#visitFeatureChainExpression(com.dassault_systemes.modeler.kerml.model.kerml.FeatureChainExpression,C)), [visitFeatureChaining](../../kerml/model/KerMLModelHierarchyVisitor.html#visitFeatureChaining(com.dassault_systemes.modeler.kerml.model.kerml.FeatureChaining,C)), [visitFeatureInverting](../../kerml/model/KerMLModelHierarchyVisitor.html#visitFeatureInverting(com.dassault_systemes.modeler.kerml.model.kerml.FeatureInverting,C)), [visitFeatureMembership](../../kerml/model/KerMLModelHierarchyVisitor.html#visitFeatureMembership(com.dassault_systemes.modeler.kerml.model.kerml.FeatureMembership,C)), [visitFeatureReferenceExpression](../../kerml/model/KerMLModelHierarchyVisitor.html#visitFeatureReferenceExpression(com.dassault_systemes.modeler.kerml.model.kerml.FeatureReferenceExpression,C)), [visitFeatureTyping](../../kerml/model/KerMLModelHierarchyVisitor.html#visitFeatureTyping(com.dassault_systemes.modeler.kerml.model.kerml.FeatureTyping,C)), [visitFeatureValue](../../kerml/model/KerMLModelHierarchyVisitor.html#visitFeatureValue(com.dassault_systemes.modeler.kerml.model.kerml.FeatureValue,C)), [visitFlow](../../kerml/model/KerMLModelHierarchyVisitor.html#visitFlow(com.dassault_systemes.modeler.kerml.model.kerml.Flow,C)), [visitFlowEnd](../../kerml/model/KerMLModelHierarchyVisitor.html#visitFlowEnd(com.dassault_systemes.modeler.kerml.model.kerml.FlowEnd,C)), [visitFunction](../../kerml/model/KerMLModelHierarchyVisitor.html#visitFunction(com.dassault_systemes.modeler.kerml.model.kerml.Function,C)), [visitImport](../../kerml/model/KerMLModelHierarchyVisitor.html#visitImport(com.dassault_systemes.modeler.kerml.model.kerml.Import,C)), [visitIndexExpression](../../kerml/model/KerMLModelHierarchyVisitor.html#visitIndexExpression(com.dassault_systemes.modeler.kerml.model.kerml.IndexExpression,C)), [visitInstantiationExpression](../../kerml/model/KerMLModelHierarchyVisitor.html#visitInstantiationExpression(com.dassault_systemes.modeler.kerml.model.kerml.InstantiationExpression,C)), [visitInteraction](../../kerml/model/KerMLModelHierarchyVisitor.html#visitInteraction(com.dassault_systemes.modeler.kerml.model.kerml.Interaction,C)), [visitIntersecting](../../kerml/model/KerMLModelHierarchyVisitor.html#visitIntersecting(com.dassault_systemes.modeler.kerml.model.kerml.Intersecting,C)), [visitInvariant](../../kerml/model/KerMLModelHierarchyVisitor.html#visitInvariant(com.dassault_systemes.modeler.kerml.model.kerml.Invariant,C)), [visitInvocationExpression](../../kerml/model/KerMLModelHierarchyVisitor.html#visitInvocationExpression(com.dassault_systemes.modeler.kerml.model.kerml.InvocationExpression,C)), [visitLibraryPackage](../../kerml/model/KerMLModelHierarchyVisitor.html#visitLibraryPackage(com.dassault_systemes.modeler.kerml.model.kerml.LibraryPackage,C)), [visitLiteralBoolean](../../kerml/model/KerMLModelHierarchyVisitor.html#visitLiteralBoolean(com.dassault_systemes.modeler.kerml.model.kerml.LiteralBoolean,C)), [visitLiteralExpression](../../kerml/model/KerMLModelHierarchyVisitor.html#visitLiteralExpression(com.dassault_systemes.modeler.kerml.model.kerml.LiteralExpression,C)), [visitLiteralInfinity](../../kerml/model/KerMLModelHierarchyVisitor.html#visitLiteralInfinity(com.dassault_systemes.modeler.kerml.model.kerml.LiteralInfinity,C)), [visitLiteralInteger](../../kerml/model/KerMLModelHierarchyVisitor.html#visitLiteralInteger(com.dassault_systemes.modeler.kerml.model.kerml.LiteralInteger,C)), [visitLiteralRational](../../kerml/model/KerMLModelHierarchyVisitor.html#visitLiteralRational(com.dassault_systemes.modeler.kerml.model.kerml.LiteralRational,C)), [visitLiteralString](../../kerml/model/KerMLModelHierarchyVisitor.html#visitLiteralString(com.dassault_systemes.modeler.kerml.model.kerml.LiteralString,C)), [visitMembership](../../kerml/model/KerMLModelHierarchyVisitor.html#visitMembership(com.dassault_systemes.modeler.kerml.model.kerml.Membership,C)), [visitMembershipImport](../../kerml/model/KerMLModelHierarchyVisitor.html#visitMembershipImport(com.dassault_systemes.modeler.kerml.model.kerml.MembershipImport,C)), [visitMetaclass](../../kerml/model/KerMLModelHierarchyVisitor.html#visitMetaclass(com.dassault_systemes.modeler.kerml.model.kerml.Metaclass,C)), [visitMetadataAccessExpression](../../kerml/model/KerMLModelHierarchyVisitor.html#visitMetadataAccessExpression(com.dassault_systemes.modeler.kerml.model.kerml.MetadataAccessExpression,C)), [visitMetadataFeature](../../kerml/model/KerMLModelHierarchyVisitor.html#visitMetadataFeature(com.dassault_systemes.modeler.kerml.model.kerml.MetadataFeature,C)), [visitMultiplicity](../../kerml/model/KerMLModelHierarchyVisitor.html#visitMultiplicity(com.dassault_systemes.modeler.kerml.model.kerml.Multiplicity,C)), [visitMultiplicityRange](../../kerml/model/KerMLModelHierarchyVisitor.html#visitMultiplicityRange(com.dassault_systemes.modeler.kerml.model.kerml.MultiplicityRange,C)), [visitNamespace](../../kerml/model/KerMLModelHierarchyVisitor.html#visitNamespace(com.dassault_systemes.modeler.kerml.model.kerml.Namespace,C)), [visitNamespaceImport](../../kerml/model/KerMLModelHierarchyVisitor.html#visitNamespaceImport(com.dassault_systemes.modeler.kerml.model.kerml.NamespaceImport,C)), [visitNullExpression](../../kerml/model/KerMLModelHierarchyVisitor.html#visitNullExpression(com.dassault_systemes.modeler.kerml.model.kerml.NullExpression,C)), [visitOperatorExpression](../../kerml/model/KerMLModelHierarchyVisitor.html#visitOperatorExpression(com.dassault_systemes.modeler.kerml.model.kerml.OperatorExpression,C)), [visitOwningMembership](../../kerml/model/KerMLModelHierarchyVisitor.html#visitOwningMembership(com.dassault_systemes.modeler.kerml.model.kerml.OwningMembership,C)), [visitPackage](../../kerml/model/KerMLModelHierarchyVisitor.html#visitPackage(com.dassault_systemes.modeler.kerml.model.kerml.Package,C)), [visitParameterMembership](../../kerml/model/KerMLModelHierarchyVisitor.html#visitParameterMembership(com.dassault_systemes.modeler.kerml.model.kerml.ParameterMembership,C)), [visitPayloadFeature](../../kerml/model/KerMLModelHierarchyVisitor.html#visitPayloadFeature(com.dassault_systemes.modeler.kerml.model.kerml.PayloadFeature,C)), [visitPredicate](../../kerml/model/KerMLModelHierarchyVisitor.html#visitPredicate(com.dassault_systemes.modeler.kerml.model.kerml.Predicate,C)), [visitRedefinition](../../kerml/model/KerMLModelHierarchyVisitor.html#visitRedefinition(com.dassault_systemes.modeler.kerml.model.kerml.Redefinition,C)), [visitReferenceSubsetting](../../kerml/model/KerMLModelHierarchyVisitor.html#visitReferenceSubsetting(com.dassault_systemes.modeler.kerml.model.kerml.ReferenceSubsetting,C)), [visitRelationship](../../kerml/model/KerMLModelHierarchyVisitor.html#visitRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Relationship,C)), [visitResultExpressionMembership](../../kerml/model/KerMLModelHierarchyVisitor.html#visitResultExpressionMembership(com.dassault_systemes.modeler.kerml.model.kerml.ResultExpressionMembership,C)), [visitReturnParameterMembership](../../kerml/model/KerMLModelHierarchyVisitor.html#visitReturnParameterMembership(com.dassault_systemes.modeler.kerml.model.kerml.ReturnParameterMembership,C)), [visitSelectExpression](../../kerml/model/KerMLModelHierarchyVisitor.html#visitSelectExpression(com.dassault_systemes.modeler.kerml.model.kerml.SelectExpression,C)), [visitSpecialization](../../kerml/model/KerMLModelHierarchyVisitor.html#visitSpecialization(com.dassault_systemes.modeler.kerml.model.kerml.Specialization,C)), [visitStep](../../kerml/model/KerMLModelHierarchyVisitor.html#visitStep(com.dassault_systemes.modeler.kerml.model.kerml.Step,C)), [visitStructure](../../kerml/model/KerMLModelHierarchyVisitor.html#visitStructure(com.dassault_systemes.modeler.kerml.model.kerml.Structure,C)), [visitSubclassification](../../kerml/model/KerMLModelHierarchyVisitor.html#visitSubclassification(com.dassault_systemes.modeler.kerml.model.kerml.Subclassification,C)), [visitSubsetting](../../kerml/model/KerMLModelHierarchyVisitor.html#visitSubsetting(com.dassault_systemes.modeler.kerml.model.kerml.Subsetting,C)), [visitSuccession](../../kerml/model/KerMLModelHierarchyVisitor.html#visitSuccession(com.dassault_systemes.modeler.kerml.model.kerml.Succession,C)), [visitSuccessionFlow](../../kerml/model/KerMLModelHierarchyVisitor.html#visitSuccessionFlow(com.dassault_systemes.modeler.kerml.model.kerml.SuccessionFlow,C)), [visitTextualRepresentation](../../kerml/model/KerMLModelHierarchyVisitor.html#visitTextualRepresentation(com.dassault_systemes.modeler.kerml.model.kerml.TextualRepresentation,C)), [visitType](../../kerml/model/KerMLModelHierarchyVisitor.html#visitType(com.dassault_systemes.modeler.kerml.model.kerml.Type,C)), [visitTypeFeaturing](../../kerml/model/KerMLModelHierarchyVisitor.html#visitTypeFeaturing(com.dassault_systemes.modeler.kerml.model.kerml.TypeFeaturing,C)), [visitUnioning](../../kerml/model/KerMLModelHierarchyVisitor.html#visitUnioning(com.dassault_systemes.modeler.kerml.model.kerml.Unioning,C))`
Methods inherited from interface com.dassault_systemes.modeler.sysml.model.[SysMLModelVisitor](SysMLModelVisitor.html)
`[createVisitorContext](SysMLModelVisitor.html#createVisitorContext())`

============ METHOD DETAIL ========== 
Method Details
getEPackage
default org.eclipse.emf.ecore.EPackage getEPackage()
Returns the EPackage that this visitor is suited for.
Specified by:
`[getEPackage](../../kerml/model/KerMLModelHierarchyVisitor.html#getEPackage())` in interface `[KerMLModelHierarchyVisitor](../../kerml/model/KerMLModelHierarchyVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Returns:
the EPackage instance
isAcceptable
default boolean isAcceptable(org.eclipse.emf.ecore.EPackage ePackage)
Checks if the given EPackage elements are acceptable by the visitor.
Specified by:
`[isAcceptable](../../kerml/model/KerMLModelHierarchyVisitor.html#isAcceptable(org.eclipse.emf.ecore.EPackage))` in interface `[KerMLModelHierarchyVisitor](../../kerml/model/KerMLModelHierarchyVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`ePackage` - the EPackage to check
Returns:
true if the EPackage is acceptable, false otherwise
visitAcceptActionUsage
default void visitAcceptActionUsage([AcceptActionUsage](sysml/AcceptActionUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits an AcceptActionUsage element.
Specified by:
`[visitAcceptActionUsage](SysMLModelVisitor.html#visitAcceptActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.AcceptActionUsage,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the AcceptActionUsage element to visit
`context` - the visitor context
visitActionDefinition
default void visitActionDefinition([ActionDefinition](sysml/ActionDefinition.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits an ActionDefinition element.
Specified by:
`[visitActionDefinition](SysMLModelVisitor.html#visitActionDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ActionDefinition,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the ActionDefinition element to visit
`context` - the visitor context
visitActionUsage
default void visitActionUsage([ActionUsage](sysml/ActionUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits an ActionUsage element.
Specified by:
`[visitActionUsage](SysMLModelVisitor.html#visitActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.ActionUsage,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the ActionUsage element to visit
`context` - the visitor context
visitActorMembership
default void visitActorMembership([ActorMembership](sysml/ActorMembership.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits an ActorMembership element.
Specified by:
`[visitActorMembership](SysMLModelVisitor.html#visitActorMembership(com.dassault_systemes.modeler.sysml.model.sysml.ActorMembership,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the ActorMembership element to visit
`context` - the visitor context
visitAllocationDefinition
default void visitAllocationDefinition([AllocationDefinition](sysml/AllocationDefinition.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits an AllocationDefinition element.
Specified by:
`[visitAllocationDefinition](SysMLModelVisitor.html#visitAllocationDefinition(com.dassault_systemes.modeler.sysml.model.sysml.AllocationDefinition,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the AllocationDefinition element to visit
`context` - the visitor context
visitAllocationUsage
default void visitAllocationUsage([AllocationUsage](sysml/AllocationUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits an AllocationUsage element.
Specified by:
`[visitAllocationUsage](SysMLModelVisitor.html#visitAllocationUsage(com.dassault_systemes.modeler.sysml.model.sysml.AllocationUsage,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the AllocationUsage element to visit
`context` - the visitor context
visitAnalysisCaseDefinition
default void visitAnalysisCaseDefinition([AnalysisCaseDefinition](sysml/AnalysisCaseDefinition.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits an AnalysisCaseDefinition element.
Specified by:
`[visitAnalysisCaseDefinition](SysMLModelVisitor.html#visitAnalysisCaseDefinition(com.dassault_systemes.modeler.sysml.model.sysml.AnalysisCaseDefinition,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the AnalysisCaseDefinition element to visit
`context` - the visitor context
visitAnalysisCaseUsage
default void visitAnalysisCaseUsage([AnalysisCaseUsage](sysml/AnalysisCaseUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits an AnalysisCaseUsage element.
Specified by:
`[visitAnalysisCaseUsage](SysMLModelVisitor.html#visitAnalysisCaseUsage(com.dassault_systemes.modeler.sysml.model.sysml.AnalysisCaseUsage,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the AnalysisCaseUsage element to visit
`context` - the visitor context
visitAssertConstraintUsage
default void visitAssertConstraintUsage([AssertConstraintUsage](sysml/AssertConstraintUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits an AssertConstraintUsage element.
Specified by:
`[visitAssertConstraintUsage](SysMLModelVisitor.html#visitAssertConstraintUsage(com.dassault_systemes.modeler.sysml.model.sysml.AssertConstraintUsage,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the AssertConstraintUsage element to visit
`context` - the visitor context
visitAssignmentActionUsage
default void visitAssignmentActionUsage([AssignmentActionUsage](sysml/AssignmentActionUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits an AssignmentActionUsage element.
Specified by:
`[visitAssignmentActionUsage](SysMLModelVisitor.html#visitAssignmentActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.AssignmentActionUsage,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the AssignmentActionUsage element to visit
`context` - the visitor context
visitAttributeDefinition
default void visitAttributeDefinition([AttributeDefinition](sysml/AttributeDefinition.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits an AttributeDefinition element.
Specified by:
`[visitAttributeDefinition](SysMLModelVisitor.html#visitAttributeDefinition(com.dassault_systemes.modeler.sysml.model.sysml.AttributeDefinition,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the AttributeDefinition element to visit
`context` - the visitor context
visitAttributeUsage
default void visitAttributeUsage([AttributeUsage](sysml/AttributeUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits an AttributeUsage element.
Specified by:
`[visitAttributeUsage](SysMLModelVisitor.html#visitAttributeUsage(com.dassault_systemes.modeler.sysml.model.sysml.AttributeUsage,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the AttributeUsage element to visit
`context` - the visitor context
visitBindingConnectorAsUsage
default void visitBindingConnectorAsUsage([BindingConnectorAsUsage](sysml/BindingConnectorAsUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a BindingConnectorAsUsage element.
Specified by:
`[visitBindingConnectorAsUsage](SysMLModelVisitor.html#visitBindingConnectorAsUsage(com.dassault_systemes.modeler.sysml.model.sysml.BindingConnectorAsUsage,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the BindingConnectorAsUsage element to visit
`context` - the visitor context
visitCalculationDefinition
default void visitCalculationDefinition([CalculationDefinition](sysml/CalculationDefinition.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a CalculationDefinition element.
Specified by:
`[visitCalculationDefinition](SysMLModelVisitor.html#visitCalculationDefinition(com.dassault_systemes.modeler.sysml.model.sysml.CalculationDefinition,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the CalculationDefinition element to visit
`context` - the visitor context
visitCalculationUsage
default void visitCalculationUsage([CalculationUsage](sysml/CalculationUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a CalculationUsage element.
Specified by:
`[visitCalculationUsage](SysMLModelVisitor.html#visitCalculationUsage(com.dassault_systemes.modeler.sysml.model.sysml.CalculationUsage,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the CalculationUsage element to visit
`context` - the visitor context
visitCaseDefinition
default void visitCaseDefinition([CaseDefinition](sysml/CaseDefinition.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a CaseDefinition element.
Specified by:
`[visitCaseDefinition](SysMLModelVisitor.html#visitCaseDefinition(com.dassault_systemes.modeler.sysml.model.sysml.CaseDefinition,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the CaseDefinition element to visit
`context` - the visitor context
visitCaseUsage
default void visitCaseUsage([CaseUsage](sysml/CaseUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a CaseUsage element.
Specified by:
`[visitCaseUsage](SysMLModelVisitor.html#visitCaseUsage(com.dassault_systemes.modeler.sysml.model.sysml.CaseUsage,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the CaseUsage element to visit
`context` - the visitor context
visitConcernDefinition
default void visitConcernDefinition([ConcernDefinition](sysml/ConcernDefinition.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a ConcernDefinition element.
Specified by:
`[visitConcernDefinition](SysMLModelVisitor.html#visitConcernDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ConcernDefinition,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the ConcernDefinition element to visit
`context` - the visitor context
visitConcernUsage
default void visitConcernUsage([ConcernUsage](sysml/ConcernUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a ConcernUsage element.
Specified by:
`[visitConcernUsage](SysMLModelVisitor.html#visitConcernUsage(com.dassault_systemes.modeler.sysml.model.sysml.ConcernUsage,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the ConcernUsage element to visit
`context` - the visitor context
visitConjugatedPortDefinition
default void visitConjugatedPortDefinition([ConjugatedPortDefinition](sysml/ConjugatedPortDefinition.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a ConjugatedPortDefinition element.
Specified by:
`[visitConjugatedPortDefinition](SysMLModelVisitor.html#visitConjugatedPortDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ConjugatedPortDefinition,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the ConjugatedPortDefinition element to visit
`context` - the visitor context
visitConjugatedPortTyping
default void visitConjugatedPortTyping([ConjugatedPortTyping](sysml/ConjugatedPortTyping.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a ConjugatedPortTyping element.
Specified by:
`[visitConjugatedPortTyping](SysMLModelVisitor.html#visitConjugatedPortTyping(com.dassault_systemes.modeler.sysml.model.sysml.ConjugatedPortTyping,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the ConjugatedPortTyping element to visit
`context` - the visitor context
visitConnectionDefinition
default void visitConnectionDefinition([ConnectionDefinition](sysml/ConnectionDefinition.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a ConnectionDefinition element.
Specified by:
`[visitConnectionDefinition](SysMLModelVisitor.html#visitConnectionDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ConnectionDefinition,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the ConnectionDefinition element to visit
`context` - the visitor context
visitConnectionUsage
default void visitConnectionUsage([ConnectionUsage](sysml/ConnectionUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a ConnectionUsage element.
Specified by:
`[visitConnectionUsage](SysMLModelVisitor.html#visitConnectionUsage(com.dassault_systemes.modeler.sysml.model.sysml.ConnectionUsage,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the ConnectionUsage element to visit
`context` - the visitor context
visitConnectorAsUsage
default void visitConnectorAsUsage([ConnectorAsUsage](sysml/ConnectorAsUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a ConnectorAsUsage element.
Specified by:
`[visitConnectorAsUsage](SysMLModelVisitor.html#visitConnectorAsUsage(com.dassault_systemes.modeler.sysml.model.sysml.ConnectorAsUsage,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the ConnectorAsUsage element to visit
`context` - the visitor context
visitConstraintDefinition
default void visitConstraintDefinition([ConstraintDefinition](sysml/ConstraintDefinition.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a ConstraintDefinition element.
Specified by:
`[visitConstraintDefinition](SysMLModelVisitor.html#visitConstraintDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ConstraintDefinition,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the ConstraintDefinition element to visit
`context` - the visitor context
visitConstraintUsage
default void visitConstraintUsage([ConstraintUsage](sysml/ConstraintUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a ConstraintUsage element.
Specified by:
`[visitConstraintUsage](SysMLModelVisitor.html#visitConstraintUsage(com.dassault_systemes.modeler.sysml.model.sysml.ConstraintUsage,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the ConstraintUsage element to visit
`context` - the visitor context
visitControlNode
default void visitControlNode([ControlNode](sysml/ControlNode.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a ControlNode element.
Specified by:
`[visitControlNode](SysMLModelVisitor.html#visitControlNode(com.dassault_systemes.modeler.sysml.model.sysml.ControlNode,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the ControlNode element to visit
`context` - the visitor context
visitDecisionNode
default void visitDecisionNode([DecisionNode](sysml/DecisionNode.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a DecisionNode element.
Specified by:
`[visitDecisionNode](SysMLModelVisitor.html#visitDecisionNode(com.dassault_systemes.modeler.sysml.model.sysml.DecisionNode,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the DecisionNode element to visit
`context` - the visitor context
visitDefinition
default void visitDefinition([Definition](sysml/Definition.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a Definition element.
Specified by:
`[visitDefinition](SysMLModelVisitor.html#visitDefinition(com.dassault_systemes.modeler.sysml.model.sysml.Definition,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the Definition element to visit
`context` - the visitor context
visitEnumerationDefinition
default void visitEnumerationDefinition([EnumerationDefinition](sysml/EnumerationDefinition.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits an EnumerationDefinition element.
Specified by:
`[visitEnumerationDefinition](SysMLModelVisitor.html#visitEnumerationDefinition(com.dassault_systemes.modeler.sysml.model.sysml.EnumerationDefinition,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the EnumerationDefinition element to visit
`context` - the visitor context
visitEnumerationUsage
default void visitEnumerationUsage([EnumerationUsage](sysml/EnumerationUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits an EnumerationUsage element.
Specified by:
`[visitEnumerationUsage](SysMLModelVisitor.html#visitEnumerationUsage(com.dassault_systemes.modeler.sysml.model.sysml.EnumerationUsage,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the EnumerationUsage element to visit
`context` - the visitor context
visitEventOccurrenceUsage
default void visitEventOccurrenceUsage([EventOccurrenceUsage](sysml/EventOccurrenceUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits an EventOccurrenceUsage element.
Specified by:
`[visitEventOccurrenceUsage](SysMLModelVisitor.html#visitEventOccurrenceUsage(com.dassault_systemes.modeler.sysml.model.sysml.EventOccurrenceUsage,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the EventOccurrenceUsage element to visit
`context` - the visitor context
visitExhibitStateUsage
default void visitExhibitStateUsage([ExhibitStateUsage](sysml/ExhibitStateUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits an ExhibitStateUsage element.
Specified by:
`[visitExhibitStateUsage](SysMLModelVisitor.html#visitExhibitStateUsage(com.dassault_systemes.modeler.sysml.model.sysml.ExhibitStateUsage,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the ExhibitStateUsage element to visit
`context` - the visitor context
visitExpose
default void visitExpose([Expose](sysml/Expose.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits an Expose element.
Specified by:
`[visitExpose](SysMLModelVisitor.html#visitExpose(com.dassault_systemes.modeler.sysml.model.sysml.Expose,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the Expose element to visit
`context` - the visitor context
visitFlowDefinition
default void visitFlowDefinition([FlowDefinition](sysml/FlowDefinition.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a FlowDefinition element.
Specified by:
`[visitFlowDefinition](SysMLModelVisitor.html#visitFlowDefinition(com.dassault_systemes.modeler.sysml.model.sysml.FlowDefinition,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the FlowDefinition element to visit
`context` - the visitor context
visitFlowUsage
default void visitFlowUsage([FlowUsage](sysml/FlowUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a FlowUsage element.
Specified by:
`[visitFlowUsage](SysMLModelVisitor.html#visitFlowUsage(com.dassault_systemes.modeler.sysml.model.sysml.FlowUsage,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the FlowUsage element to visit
`context` - the visitor context
visitForLoopActionUsage
default void visitForLoopActionUsage([ForLoopActionUsage](sysml/ForLoopActionUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a ForLoopActionUsage element.
Specified by:
`[visitForLoopActionUsage](SysMLModelVisitor.html#visitForLoopActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.ForLoopActionUsage,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the ForLoopActionUsage element to visit
`context` - the visitor context
visitForkNode
default void visitForkNode([ForkNode](sysml/ForkNode.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a ForkNode element.
Specified by:
`[visitForkNode](SysMLModelVisitor.html#visitForkNode(com.dassault_systemes.modeler.sysml.model.sysml.ForkNode,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the ForkNode element to visit
`context` - the visitor context
visitFramedConcernMembership
default void visitFramedConcernMembership([FramedConcernMembership](sysml/FramedConcernMembership.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a FramedConcernMembership element.
Specified by:
`[visitFramedConcernMembership](SysMLModelVisitor.html#visitFramedConcernMembership(com.dassault_systemes.modeler.sysml.model.sysml.FramedConcernMembership,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the FramedConcernMembership element to visit
`context` - the visitor context
visitIfActionUsage
default void visitIfActionUsage([IfActionUsage](sysml/IfActionUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits an IfActionUsage element.
Specified by:
`[visitIfActionUsage](SysMLModelVisitor.html#visitIfActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.IfActionUsage,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the IfActionUsage element to visit
`context` - the visitor context
visitIncludeUseCaseUsage
default void visitIncludeUseCaseUsage([IncludeUseCaseUsage](sysml/IncludeUseCaseUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits an IncludeUseCaseUsage element.
Specified by:
`[visitIncludeUseCaseUsage](SysMLModelVisitor.html#visitIncludeUseCaseUsage(com.dassault_systemes.modeler.sysml.model.sysml.IncludeUseCaseUsage,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the IncludeUseCaseUsage element to visit
`context` - the visitor context
visitInterfaceDefinition
default void visitInterfaceDefinition([InterfaceDefinition](sysml/InterfaceDefinition.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits an InterfaceDefinition element.
Specified by:
`[visitInterfaceDefinition](SysMLModelVisitor.html#visitInterfaceDefinition(com.dassault_systemes.modeler.sysml.model.sysml.InterfaceDefinition,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the InterfaceDefinition element to visit
`context` - the visitor context
visitInterfaceUsage
default void visitInterfaceUsage([InterfaceUsage](sysml/InterfaceUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits an InterfaceUsage element.
Specified by:
`[visitInterfaceUsage](SysMLModelVisitor.html#visitInterfaceUsage(com.dassault_systemes.modeler.sysml.model.sysml.InterfaceUsage,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the InterfaceUsage element to visit
`context` - the visitor context
visitItemDefinition
default void visitItemDefinition([ItemDefinition](sysml/ItemDefinition.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits an ItemDefinition element.
Specified by:
`[visitItemDefinition](SysMLModelVisitor.html#visitItemDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ItemDefinition,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the ItemDefinition element to visit
`context` - the visitor context
visitItemUsage
default void visitItemUsage([ItemUsage](sysml/ItemUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits an ItemUsage element.
Specified by:
`[visitItemUsage](SysMLModelVisitor.html#visitItemUsage(com.dassault_systemes.modeler.sysml.model.sysml.ItemUsage,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the ItemUsage element to visit
`context` - the visitor context
visitJoinNode
default void visitJoinNode([JoinNode](sysml/JoinNode.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a JoinNode element.
Specified by:
`[visitJoinNode](SysMLModelVisitor.html#visitJoinNode(com.dassault_systemes.modeler.sysml.model.sysml.JoinNode,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the JoinNode element to visit
`context` - the visitor context
visitLoopActionUsage
default void visitLoopActionUsage([LoopActionUsage](sysml/LoopActionUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a LoopActionUsage element.
Specified by:
`[visitLoopActionUsage](SysMLModelVisitor.html#visitLoopActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.LoopActionUsage,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the LoopActionUsage element to visit
`context` - the visitor context
visitMembershipExpose
default void visitMembershipExpose([MembershipExpose](sysml/MembershipExpose.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a MembershipExpose element.
Specified by:
`[visitMembershipExpose](SysMLModelVisitor.html#visitMembershipExpose(com.dassault_systemes.modeler.sysml.model.sysml.MembershipExpose,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the MembershipExpose element to visit
`context` - the visitor context
visitMergeNode
default void visitMergeNode([MergeNode](sysml/MergeNode.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a MergeNode element.
Specified by:
`[visitMergeNode](SysMLModelVisitor.html#visitMergeNode(com.dassault_systemes.modeler.sysml.model.sysml.MergeNode,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the MergeNode element to visit
`context` - the visitor context
visitMetadataDefinition
default void visitMetadataDefinition([MetadataDefinition](sysml/MetadataDefinition.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a MetadataDefinition element.
Specified by:
`[visitMetadataDefinition](SysMLModelVisitor.html#visitMetadataDefinition(com.dassault_systemes.modeler.sysml.model.sysml.MetadataDefinition,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the MetadataDefinition element to visit
`context` - the visitor context
visitMetadataUsage
default void visitMetadataUsage([MetadataUsage](sysml/MetadataUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a MetadataUsage element.
Specified by:
`[visitMetadataUsage](SysMLModelVisitor.html#visitMetadataUsage(com.dassault_systemes.modeler.sysml.model.sysml.MetadataUsage,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the MetadataUsage element to visit
`context` - the visitor context
visitNamespaceExpose
default void visitNamespaceExpose([NamespaceExpose](sysml/NamespaceExpose.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a NamespaceExpose element.
Specified by:
`[visitNamespaceExpose](SysMLModelVisitor.html#visitNamespaceExpose(com.dassault_systemes.modeler.sysml.model.sysml.NamespaceExpose,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the NamespaceExpose element to visit
`context` - the visitor context
visitObjectiveMembership
default void visitObjectiveMembership([ObjectiveMembership](sysml/ObjectiveMembership.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits an ObjectiveMembership element.
Specified by:
`[visitObjectiveMembership](SysMLModelVisitor.html#visitObjectiveMembership(com.dassault_systemes.modeler.sysml.model.sysml.ObjectiveMembership,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the ObjectiveMembership element to visit
`context` - the visitor context
visitOccurrenceDefinition
default void visitOccurrenceDefinition([OccurrenceDefinition](sysml/OccurrenceDefinition.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits an OccurrenceDefinition element.
Specified by:
`[visitOccurrenceDefinition](SysMLModelVisitor.html#visitOccurrenceDefinition(com.dassault_systemes.modeler.sysml.model.sysml.OccurrenceDefinition,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the OccurrenceDefinition element to visit
`context` - the visitor context
visitOccurrenceUsage
default void visitOccurrenceUsage([OccurrenceUsage](sysml/OccurrenceUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits an OccurrenceUsage element.
Specified by:
`[visitOccurrenceUsage](SysMLModelVisitor.html#visitOccurrenceUsage(com.dassault_systemes.modeler.sysml.model.sysml.OccurrenceUsage,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the OccurrenceUsage element to visit
`context` - the visitor context
visitPartDefinition
default void visitPartDefinition([PartDefinition](sysml/PartDefinition.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a PartDefinition element.
Specified by:
`[visitPartDefinition](SysMLModelVisitor.html#visitPartDefinition(com.dassault_systemes.modeler.sysml.model.sysml.PartDefinition,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the PartDefinition element to visit
`context` - the visitor context
visitPartUsage
default void visitPartUsage([PartUsage](sysml/PartUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a PartUsage element.
Specified by:
`[visitPartUsage](SysMLModelVisitor.html#visitPartUsage(com.dassault_systemes.modeler.sysml.model.sysml.PartUsage,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the PartUsage element to visit
`context` - the visitor context
visitPerformActionUsage
default void visitPerformActionUsage([PerformActionUsage](sysml/PerformActionUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a PerformActionUsage element.
Specified by:
`[visitPerformActionUsage](SysMLModelVisitor.html#visitPerformActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.PerformActionUsage,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the PerformActionUsage element to visit
`context` - the visitor context
visitPortConjugation
default void visitPortConjugation([PortConjugation](sysml/PortConjugation.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a PortConjugation element.
Specified by:
`[visitPortConjugation](SysMLModelVisitor.html#visitPortConjugation(com.dassault_systemes.modeler.sysml.model.sysml.PortConjugation,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the PortConjugation element to visit
`context` - the visitor context
visitPortDefinition
default void visitPortDefinition([PortDefinition](sysml/PortDefinition.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a PortDefinition element.
Specified by:
`[visitPortDefinition](SysMLModelVisitor.html#visitPortDefinition(com.dassault_systemes.modeler.sysml.model.sysml.PortDefinition,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the PortDefinition element to visit
`context` - the visitor context
visitPortUsage
default void visitPortUsage([PortUsage](sysml/PortUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a PortUsage element.
Specified by:
`[visitPortUsage](SysMLModelVisitor.html#visitPortUsage(com.dassault_systemes.modeler.sysml.model.sysml.PortUsage,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the PortUsage element to visit
`context` - the visitor context
visitReferenceUsage
default void visitReferenceUsage([ReferenceUsage](sysml/ReferenceUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a ReferenceUsage element.
Specified by:
`[visitReferenceUsage](SysMLModelVisitor.html#visitReferenceUsage(com.dassault_systemes.modeler.sysml.model.sysml.ReferenceUsage,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the ReferenceUsage element to visit
`context` - the visitor context
visitRenderingDefinition
default void visitRenderingDefinition([RenderingDefinition](sysml/RenderingDefinition.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a RenderingDefinition element.
Specified by:
`[visitRenderingDefinition](SysMLModelVisitor.html#visitRenderingDefinition(com.dassault_systemes.modeler.sysml.model.sysml.RenderingDefinition,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the RenderingDefinition element to visit
`context` - the visitor context
visitRenderingUsage
default void visitRenderingUsage([RenderingUsage](sysml/RenderingUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a RenderingUsage element.
Specified by:
`[visitRenderingUsage](SysMLModelVisitor.html#visitRenderingUsage(com.dassault_systemes.modeler.sysml.model.sysml.RenderingUsage,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the RenderingUsage element to visit
`context` - the visitor context
visitRequirementConstraintMembership
default void visitRequirementConstraintMembership([RequirementConstraintMembership](sysml/RequirementConstraintMembership.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a RequirementConstraintMembership element.
Specified by:
`[visitRequirementConstraintMembership](SysMLModelVisitor.html#visitRequirementConstraintMembership(com.dassault_systemes.modeler.sysml.model.sysml.RequirementConstraintMembership,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the RequirementConstraintMembership element to visit
`context` - the visitor context
visitRequirementDefinition
default void visitRequirementDefinition([RequirementDefinition](sysml/RequirementDefinition.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a RequirementDefinition element.
Specified by:
`[visitRequirementDefinition](SysMLModelVisitor.html#visitRequirementDefinition(com.dassault_systemes.modeler.sysml.model.sysml.RequirementDefinition,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the RequirementDefinition element to visit
`context` - the visitor context
visitRequirementUsage
default void visitRequirementUsage([RequirementUsage](sysml/RequirementUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a RequirementUsage element.
Specified by:
`[visitRequirementUsage](SysMLModelVisitor.html#visitRequirementUsage(com.dassault_systemes.modeler.sysml.model.sysml.RequirementUsage,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the RequirementUsage element to visit
`context` - the visitor context
visitRequirementVerificationMembership
default void visitRequirementVerificationMembership([RequirementVerificationMembership](sysml/RequirementVerificationMembership.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a RequirementVerificationMembership element.
Specified by:
`[visitRequirementVerificationMembership](SysMLModelVisitor.html#visitRequirementVerificationMembership(com.dassault_systemes.modeler.sysml.model.sysml.RequirementVerificationMembership,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the RequirementVerificationMembership element to visit
`context` - the visitor context
visitSatisfyRequirementUsage
default void visitSatisfyRequirementUsage([SatisfyRequirementUsage](sysml/SatisfyRequirementUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a SatisfyRequirementUsage element.
Specified by:
`[visitSatisfyRequirementUsage](SysMLModelVisitor.html#visitSatisfyRequirementUsage(com.dassault_systemes.modeler.sysml.model.sysml.SatisfyRequirementUsage,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the SatisfyRequirementUsage element to visit
`context` - the visitor context
visitSendActionUsage
default void visitSendActionUsage([SendActionUsage](sysml/SendActionUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a SendActionUsage element.
Specified by:
`[visitSendActionUsage](SysMLModelVisitor.html#visitSendActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.SendActionUsage,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the SendActionUsage element to visit
`context` - the visitor context
visitStakeholderMembership
default void visitStakeholderMembership([StakeholderMembership](sysml/StakeholderMembership.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a StakeholderMembership element.
Specified by:
`[visitStakeholderMembership](SysMLModelVisitor.html#visitStakeholderMembership(com.dassault_systemes.modeler.sysml.model.sysml.StakeholderMembership,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the StakeholderMembership element to visit
`context` - the visitor context
visitStateDefinition
default void visitStateDefinition([StateDefinition](sysml/StateDefinition.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a StateDefinition element.
Specified by:
`[visitStateDefinition](SysMLModelVisitor.html#visitStateDefinition(com.dassault_systemes.modeler.sysml.model.sysml.StateDefinition,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the StateDefinition element to visit
`context` - the visitor context
visitStateSubactionMembership
default void visitStateSubactionMembership([StateSubactionMembership](sysml/StateSubactionMembership.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a StateSubactionMembership element.
Specified by:
`[visitStateSubactionMembership](SysMLModelVisitor.html#visitStateSubactionMembership(com.dassault_systemes.modeler.sysml.model.sysml.StateSubactionMembership,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the StateSubactionMembership element to visit
`context` - the visitor context
visitStateUsage
default void visitStateUsage([StateUsage](sysml/StateUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a StateUsage element.
Specified by:
`[visitStateUsage](SysMLModelVisitor.html#visitStateUsage(com.dassault_systemes.modeler.sysml.model.sysml.StateUsage,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the StateUsage element to visit
`context` - the visitor context
visitSubjectMembership
default void visitSubjectMembership([SubjectMembership](sysml/SubjectMembership.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a SubjectMembership element.
Specified by:
`[visitSubjectMembership](SysMLModelVisitor.html#visitSubjectMembership(com.dassault_systemes.modeler.sysml.model.sysml.SubjectMembership,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the SubjectMembership element to visit
`context` - the visitor context
visitSuccessionAsUsage
default void visitSuccessionAsUsage([SuccessionAsUsage](sysml/SuccessionAsUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a SuccessionAsUsage element.
Specified by:
`[visitSuccessionAsUsage](SysMLModelVisitor.html#visitSuccessionAsUsage(com.dassault_systemes.modeler.sysml.model.sysml.SuccessionAsUsage,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the SuccessionAsUsage element to visit
`context` - the visitor context
visitSuccessionFlowUsage
default void visitSuccessionFlowUsage([SuccessionFlowUsage](sysml/SuccessionFlowUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a SuccessionFlowUsage element.
Specified by:
`[visitSuccessionFlowUsage](SysMLModelVisitor.html#visitSuccessionFlowUsage(com.dassault_systemes.modeler.sysml.model.sysml.SuccessionFlowUsage,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the SuccessionFlowUsage element to visit
`context` - the visitor context
visitTerminateActionUsage
default void visitTerminateActionUsage([TerminateActionUsage](sysml/TerminateActionUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a TerminateActionUsage element.
Specified by:
`[visitTerminateActionUsage](SysMLModelVisitor.html#visitTerminateActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.TerminateActionUsage,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the TerminateActionUsage element to visit
`context` - the visitor context
visitTransitionFeatureMembership
default void visitTransitionFeatureMembership([TransitionFeatureMembership](sysml/TransitionFeatureMembership.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a TransitionFeatureMembership element.
Specified by:
`[visitTransitionFeatureMembership](SysMLModelVisitor.html#visitTransitionFeatureMembership(com.dassault_systemes.modeler.sysml.model.sysml.TransitionFeatureMembership,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the TransitionFeatureMembership element to visit
`context` - the visitor context
visitTransitionUsage
default void visitTransitionUsage([TransitionUsage](sysml/TransitionUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a TransitionUsage element.
Specified by:
`[visitTransitionUsage](SysMLModelVisitor.html#visitTransitionUsage(com.dassault_systemes.modeler.sysml.model.sysml.TransitionUsage,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the TransitionUsage element to visit
`context` - the visitor context
visitTriggerInvocationExpression
default void visitTriggerInvocationExpression([TriggerInvocationExpression](sysml/TriggerInvocationExpression.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a TriggerInvocationExpression element.
Specified by:
`[visitTriggerInvocationExpression](SysMLModelVisitor.html#visitTriggerInvocationExpression(com.dassault_systemes.modeler.sysml.model.sysml.TriggerInvocationExpression,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the TriggerInvocationExpression element to visit
`context` - the visitor context
visitUsage
default void visitUsage([Usage](sysml/Usage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a Usage element.
Specified by:
`[visitUsage](SysMLModelVisitor.html#visitUsage(com.dassault_systemes.modeler.sysml.model.sysml.Usage,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the Usage element to visit
`context` - the visitor context
visitUseCaseDefinition
default void visitUseCaseDefinition([UseCaseDefinition](sysml/UseCaseDefinition.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a UseCaseDefinition element.
Specified by:
`[visitUseCaseDefinition](SysMLModelVisitor.html#visitUseCaseDefinition(com.dassault_systemes.modeler.sysml.model.sysml.UseCaseDefinition,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the UseCaseDefinition element to visit
`context` - the visitor context
visitUseCaseUsage
default void visitUseCaseUsage([UseCaseUsage](sysml/UseCaseUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a UseCaseUsage element.
Specified by:
`[visitUseCaseUsage](SysMLModelVisitor.html#visitUseCaseUsage(com.dassault_systemes.modeler.sysml.model.sysml.UseCaseUsage,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the UseCaseUsage element to visit
`context` - the visitor context
visitVariantMembership
default void visitVariantMembership([VariantMembership](sysml/VariantMembership.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a VariantMembership element.
Specified by:
`[visitVariantMembership](SysMLModelVisitor.html#visitVariantMembership(com.dassault_systemes.modeler.sysml.model.sysml.VariantMembership,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the VariantMembership element to visit
`context` - the visitor context
visitVerificationCaseDefinition
default void visitVerificationCaseDefinition([VerificationCaseDefinition](sysml/VerificationCaseDefinition.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a VerificationCaseDefinition element.
Specified by:
`[visitVerificationCaseDefinition](SysMLModelVisitor.html#visitVerificationCaseDefinition(com.dassault_systemes.modeler.sysml.model.sysml.VerificationCaseDefinition,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the VerificationCaseDefinition element to visit
`context` - the visitor context
visitVerificationCaseUsage
default void visitVerificationCaseUsage([VerificationCaseUsage](sysml/VerificationCaseUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a VerificationCaseUsage element.
Specified by:
`[visitVerificationCaseUsage](SysMLModelVisitor.html#visitVerificationCaseUsage(com.dassault_systemes.modeler.sysml.model.sysml.VerificationCaseUsage,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the VerificationCaseUsage element to visit
`context` - the visitor context
visitViewDefinition
default void visitViewDefinition([ViewDefinition](sysml/ViewDefinition.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a ViewDefinition element.
Specified by:
`[visitViewDefinition](SysMLModelVisitor.html#visitViewDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ViewDefinition,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the ViewDefinition element to visit
`context` - the visitor context
visitViewRenderingMembership
default void visitViewRenderingMembership([ViewRenderingMembership](sysml/ViewRenderingMembership.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a ViewRenderingMembership element.
Specified by:
`[visitViewRenderingMembership](SysMLModelVisitor.html#visitViewRenderingMembership(com.dassault_systemes.modeler.sysml.model.sysml.ViewRenderingMembership,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the ViewRenderingMembership element to visit
`context` - the visitor context
visitViewUsage
default void visitViewUsage([ViewUsage](sysml/ViewUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a ViewUsage element.
Specified by:
`[visitViewUsage](SysMLModelVisitor.html#visitViewUsage(com.dassault_systemes.modeler.sysml.model.sysml.ViewUsage,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the ViewUsage element to visit
`context` - the visitor context
visitViewpointDefinition
default void visitViewpointDefinition([ViewpointDefinition](sysml/ViewpointDefinition.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a ViewpointDefinition element.
Specified by:
`[visitViewpointDefinition](SysMLModelVisitor.html#visitViewpointDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ViewpointDefinition,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the ViewpointDefinition element to visit
`context` - the visitor context
visitViewpointUsage
default void visitViewpointUsage([ViewpointUsage](sysml/ViewpointUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a ViewpointUsage element.
Specified by:
`[visitViewpointUsage](SysMLModelVisitor.html#visitViewpointUsage(com.dassault_systemes.modeler.sysml.model.sysml.ViewpointUsage,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the ViewpointUsage element to visit
`context` - the visitor context
visitWhileLoopActionUsage
default void visitWhileLoopActionUsage([WhileLoopActionUsage](sysml/WhileLoopActionUsage.html) element,
 [C](SysMLModelHierarchyVisitor.html) context)
Visits a WhileLoopActionUsage element.
Specified by:
`[visitWhileLoopActionUsage](SysMLModelVisitor.html#visitWhileLoopActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.WhileLoopActionUsage,C))` in interface `[SysMLModelVisitor](SysMLModelVisitor.html)<[C](SysMLModelHierarchyVisitor.html) extends [SysMLVisitorContext](SysMLVisitorContext.html)>`
Parameters:
`element` - the WhileLoopActionUsage element to visit
`context` - the visitor context

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.sysml.model</a></div>
<h1 class="title" title="Interface SysMLModelHierarchyVisitor">Interface SysMLModelHierarchyVisitor&lt;C extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><code>C</code> - the type of the visitor context</dd>
</dl>
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../nomagic/magicdraw/uml/AbstractVisitor.html" title="interface in com.nomagic.magicdraw.uml">AbstractVisitor</a></code>, <code><a href="../../kerml/model/KerMLModelHierarchyVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelHierarchyVisitor</a>&lt;C&gt;</code>, <code><a href="../../kerml/model/KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;C&gt;</code>, <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;C&gt;</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">SysMLModelHierarchyVisitor&lt;C extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</span><span class="extends-implements">
extends <a href="../../kerml/model/KerMLModelHierarchyVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelHierarchyVisitor</a>&lt;C&gt;, <a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;C&gt;</span></div>
<div class="block">This interface extends KerMLModelHierarchyVisitor and SysMLModelVisitor to provide
 a visitor pattern implementation for traversing SysML model elements.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab5" onclick="show('method-summary-table', 'method-summary-table-tab5', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Default Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default org.eclipse.emf.ecore.EPackage</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#getEPackage()">getEPackage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns the EPackage that this visitor is suited for.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#isAcceptable(org.eclipse.emf.ecore.EPackage)">isAcceptable</a><wbr/>(org.eclipse.emf.ecore.EPackage ePackage)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Checks if the given EPackage elements are acceptable by the visitor.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitAcceptActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.AcceptActionUsage,C)">visitAcceptActionUsage</a><wbr/>(<a href="sysml/AcceptActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AcceptActionUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits an AcceptActionUsage element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitActionDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ActionDefinition,C)">visitActionDefinition</a><wbr/>(<a href="sysml/ActionDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActionDefinition</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits an ActionDefinition element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.ActionUsage,C)">visitActionUsage</a><wbr/>(<a href="sysml/ActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActionUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits an ActionUsage element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitActorMembership(com.dassault_systemes.modeler.sysml.model.sysml.ActorMembership,C)">visitActorMembership</a><wbr/>(<a href="sysml/ActorMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActorMembership</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits an ActorMembership element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitAllocationDefinition(com.dassault_systemes.modeler.sysml.model.sysml.AllocationDefinition,C)">visitAllocationDefinition</a><wbr/>(<a href="sysml/AllocationDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AllocationDefinition</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits an AllocationDefinition element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitAllocationUsage(com.dassault_systemes.modeler.sysml.model.sysml.AllocationUsage,C)">visitAllocationUsage</a><wbr/>(<a href="sysml/AllocationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AllocationUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits an AllocationUsage element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitAnalysisCaseDefinition(com.dassault_systemes.modeler.sysml.model.sysml.AnalysisCaseDefinition,C)">visitAnalysisCaseDefinition</a><wbr/>(<a href="sysml/AnalysisCaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AnalysisCaseDefinition</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits an AnalysisCaseDefinition element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitAnalysisCaseUsage(com.dassault_systemes.modeler.sysml.model.sysml.AnalysisCaseUsage,C)">visitAnalysisCaseUsage</a><wbr/>(<a href="sysml/AnalysisCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AnalysisCaseUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits an AnalysisCaseUsage element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitAssertConstraintUsage(com.dassault_systemes.modeler.sysml.model.sysml.AssertConstraintUsage,C)">visitAssertConstraintUsage</a><wbr/>(<a href="sysml/AssertConstraintUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AssertConstraintUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits an AssertConstraintUsage element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitAssignmentActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.AssignmentActionUsage,C)">visitAssignmentActionUsage</a><wbr/>(<a href="sysml/AssignmentActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AssignmentActionUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits an AssignmentActionUsage element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitAttributeDefinition(com.dassault_systemes.modeler.sysml.model.sysml.AttributeDefinition,C)">visitAttributeDefinition</a><wbr/>(<a href="sysml/AttributeDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AttributeDefinition</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits an AttributeDefinition element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitAttributeUsage(com.dassault_systemes.modeler.sysml.model.sysml.AttributeUsage,C)">visitAttributeUsage</a><wbr/>(<a href="sysml/AttributeUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AttributeUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits an AttributeUsage element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitBindingConnectorAsUsage(com.dassault_systemes.modeler.sysml.model.sysml.BindingConnectorAsUsage,C)">visitBindingConnectorAsUsage</a><wbr/>(<a href="sysml/BindingConnectorAsUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">BindingConnectorAsUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a BindingConnectorAsUsage element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitCalculationDefinition(com.dassault_systemes.modeler.sysml.model.sysml.CalculationDefinition,C)">visitCalculationDefinition</a><wbr/>(<a href="sysml/CalculationDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">CalculationDefinition</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a CalculationDefinition element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitCalculationUsage(com.dassault_systemes.modeler.sysml.model.sysml.CalculationUsage,C)">visitCalculationUsage</a><wbr/>(<a href="sysml/CalculationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">CalculationUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a CalculationUsage element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitCaseDefinition(com.dassault_systemes.modeler.sysml.model.sysml.CaseDefinition,C)">visitCaseDefinition</a><wbr/>(<a href="sysml/CaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">CaseDefinition</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a CaseDefinition element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitCaseUsage(com.dassault_systemes.modeler.sysml.model.sysml.CaseUsage,C)">visitCaseUsage</a><wbr/>(<a href="sysml/CaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">CaseUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a CaseUsage element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitConcernDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ConcernDefinition,C)">visitConcernDefinition</a><wbr/>(<a href="sysml/ConcernDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConcernDefinition</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a ConcernDefinition element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitConcernUsage(com.dassault_systemes.modeler.sysml.model.sysml.ConcernUsage,C)">visitConcernUsage</a><wbr/>(<a href="sysml/ConcernUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConcernUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a ConcernUsage element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitConjugatedPortDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ConjugatedPortDefinition,C)">visitConjugatedPortDefinition</a><wbr/>(<a href="sysml/ConjugatedPortDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConjugatedPortDefinition</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a ConjugatedPortDefinition element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitConjugatedPortTyping(com.dassault_systemes.modeler.sysml.model.sysml.ConjugatedPortTyping,C)">visitConjugatedPortTyping</a><wbr/>(<a href="sysml/ConjugatedPortTyping.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConjugatedPortTyping</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a ConjugatedPortTyping element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitConnectionDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ConnectionDefinition,C)">visitConnectionDefinition</a><wbr/>(<a href="sysml/ConnectionDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConnectionDefinition</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a ConnectionDefinition element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitConnectionUsage(com.dassault_systemes.modeler.sysml.model.sysml.ConnectionUsage,C)">visitConnectionUsage</a><wbr/>(<a href="sysml/ConnectionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConnectionUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a ConnectionUsage element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitConnectorAsUsage(com.dassault_systemes.modeler.sysml.model.sysml.ConnectorAsUsage,C)">visitConnectorAsUsage</a><wbr/>(<a href="sysml/ConnectorAsUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConnectorAsUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a ConnectorAsUsage element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitConstraintDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ConstraintDefinition,C)">visitConstraintDefinition</a><wbr/>(<a href="sysml/ConstraintDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConstraintDefinition</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a ConstraintDefinition element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitConstraintUsage(com.dassault_systemes.modeler.sysml.model.sysml.ConstraintUsage,C)">visitConstraintUsage</a><wbr/>(<a href="sysml/ConstraintUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConstraintUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a ConstraintUsage element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitControlNode(com.dassault_systemes.modeler.sysml.model.sysml.ControlNode,C)">visitControlNode</a><wbr/>(<a href="sysml/ControlNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ControlNode</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a ControlNode element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitDecisionNode(com.dassault_systemes.modeler.sysml.model.sysml.DecisionNode,C)">visitDecisionNode</a><wbr/>(<a href="sysml/DecisionNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">DecisionNode</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a DecisionNode element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitDefinition(com.dassault_systemes.modeler.sysml.model.sysml.Definition,C)">visitDefinition</a><wbr/>(<a href="sysml/Definition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Definition</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a Definition element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitEnumerationDefinition(com.dassault_systemes.modeler.sysml.model.sysml.EnumerationDefinition,C)">visitEnumerationDefinition</a><wbr/>(<a href="sysml/EnumerationDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">EnumerationDefinition</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits an EnumerationDefinition element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitEnumerationUsage(com.dassault_systemes.modeler.sysml.model.sysml.EnumerationUsage,C)">visitEnumerationUsage</a><wbr/>(<a href="sysml/EnumerationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">EnumerationUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits an EnumerationUsage element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitEventOccurrenceUsage(com.dassault_systemes.modeler.sysml.model.sysml.EventOccurrenceUsage,C)">visitEventOccurrenceUsage</a><wbr/>(<a href="sysml/EventOccurrenceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">EventOccurrenceUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits an EventOccurrenceUsage element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitExhibitStateUsage(com.dassault_systemes.modeler.sysml.model.sysml.ExhibitStateUsage,C)">visitExhibitStateUsage</a><wbr/>(<a href="sysml/ExhibitStateUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ExhibitStateUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits an ExhibitStateUsage element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitExpose(com.dassault_systemes.modeler.sysml.model.sysml.Expose,C)">visitExpose</a><wbr/>(<a href="sysml/Expose.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Expose</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits an Expose element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitFlowDefinition(com.dassault_systemes.modeler.sysml.model.sysml.FlowDefinition,C)">visitFlowDefinition</a><wbr/>(<a href="sysml/FlowDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">FlowDefinition</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a FlowDefinition element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitFlowUsage(com.dassault_systemes.modeler.sysml.model.sysml.FlowUsage,C)">visitFlowUsage</a><wbr/>(<a href="sysml/FlowUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">FlowUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a FlowUsage element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitForkNode(com.dassault_systemes.modeler.sysml.model.sysml.ForkNode,C)">visitForkNode</a><wbr/>(<a href="sysml/ForkNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ForkNode</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a ForkNode element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitForLoopActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.ForLoopActionUsage,C)">visitForLoopActionUsage</a><wbr/>(<a href="sysml/ForLoopActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ForLoopActionUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a ForLoopActionUsage element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitFramedConcernMembership(com.dassault_systemes.modeler.sysml.model.sysml.FramedConcernMembership,C)">visitFramedConcernMembership</a><wbr/>(<a href="sysml/FramedConcernMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">FramedConcernMembership</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a FramedConcernMembership element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitIfActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.IfActionUsage,C)">visitIfActionUsage</a><wbr/>(<a href="sysml/IfActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">IfActionUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits an IfActionUsage element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitIncludeUseCaseUsage(com.dassault_systemes.modeler.sysml.model.sysml.IncludeUseCaseUsage,C)">visitIncludeUseCaseUsage</a><wbr/>(<a href="sysml/IncludeUseCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">IncludeUseCaseUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits an IncludeUseCaseUsage element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitInterfaceDefinition(com.dassault_systemes.modeler.sysml.model.sysml.InterfaceDefinition,C)">visitInterfaceDefinition</a><wbr/>(<a href="sysml/InterfaceDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">InterfaceDefinition</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits an InterfaceDefinition element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitInterfaceUsage(com.dassault_systemes.modeler.sysml.model.sysml.InterfaceUsage,C)">visitInterfaceUsage</a><wbr/>(<a href="sysml/InterfaceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">InterfaceUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits an InterfaceUsage element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitItemDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ItemDefinition,C)">visitItemDefinition</a><wbr/>(<a href="sysml/ItemDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ItemDefinition</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits an ItemDefinition element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitItemUsage(com.dassault_systemes.modeler.sysml.model.sysml.ItemUsage,C)">visitItemUsage</a><wbr/>(<a href="sysml/ItemUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ItemUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits an ItemUsage element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitJoinNode(com.dassault_systemes.modeler.sysml.model.sysml.JoinNode,C)">visitJoinNode</a><wbr/>(<a href="sysml/JoinNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">JoinNode</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a JoinNode element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitLoopActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.LoopActionUsage,C)">visitLoopActionUsage</a><wbr/>(<a href="sysml/LoopActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">LoopActionUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a LoopActionUsage element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitMembershipExpose(com.dassault_systemes.modeler.sysml.model.sysml.MembershipExpose,C)">visitMembershipExpose</a><wbr/>(<a href="sysml/MembershipExpose.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">MembershipExpose</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a MembershipExpose element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitMergeNode(com.dassault_systemes.modeler.sysml.model.sysml.MergeNode,C)">visitMergeNode</a><wbr/>(<a href="sysml/MergeNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">MergeNode</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a MergeNode element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitMetadataDefinition(com.dassault_systemes.modeler.sysml.model.sysml.MetadataDefinition,C)">visitMetadataDefinition</a><wbr/>(<a href="sysml/MetadataDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">MetadataDefinition</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a MetadataDefinition element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitMetadataUsage(com.dassault_systemes.modeler.sysml.model.sysml.MetadataUsage,C)">visitMetadataUsage</a><wbr/>(<a href="sysml/MetadataUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">MetadataUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a MetadataUsage element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitNamespaceExpose(com.dassault_systemes.modeler.sysml.model.sysml.NamespaceExpose,C)">visitNamespaceExpose</a><wbr/>(<a href="sysml/NamespaceExpose.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">NamespaceExpose</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a NamespaceExpose element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitObjectiveMembership(com.dassault_systemes.modeler.sysml.model.sysml.ObjectiveMembership,C)">visitObjectiveMembership</a><wbr/>(<a href="sysml/ObjectiveMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ObjectiveMembership</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits an ObjectiveMembership element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitOccurrenceDefinition(com.dassault_systemes.modeler.sysml.model.sysml.OccurrenceDefinition,C)">visitOccurrenceDefinition</a><wbr/>(<a href="sysml/OccurrenceDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">OccurrenceDefinition</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits an OccurrenceDefinition element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitOccurrenceUsage(com.dassault_systemes.modeler.sysml.model.sysml.OccurrenceUsage,C)">visitOccurrenceUsage</a><wbr/>(<a href="sysml/OccurrenceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">OccurrenceUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits an OccurrenceUsage element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitPartDefinition(com.dassault_systemes.modeler.sysml.model.sysml.PartDefinition,C)">visitPartDefinition</a><wbr/>(<a href="sysml/PartDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PartDefinition</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a PartDefinition element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitPartUsage(com.dassault_systemes.modeler.sysml.model.sysml.PartUsage,C)">visitPartUsage</a><wbr/>(<a href="sysml/PartUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PartUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a PartUsage element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitPerformActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.PerformActionUsage,C)">visitPerformActionUsage</a><wbr/>(<a href="sysml/PerformActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PerformActionUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a PerformActionUsage element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitPortConjugation(com.dassault_systemes.modeler.sysml.model.sysml.PortConjugation,C)">visitPortConjugation</a><wbr/>(<a href="sysml/PortConjugation.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PortConjugation</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a PortConjugation element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitPortDefinition(com.dassault_systemes.modeler.sysml.model.sysml.PortDefinition,C)">visitPortDefinition</a><wbr/>(<a href="sysml/PortDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PortDefinition</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a PortDefinition element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitPortUsage(com.dassault_systemes.modeler.sysml.model.sysml.PortUsage,C)">visitPortUsage</a><wbr/>(<a href="sysml/PortUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PortUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a PortUsage element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitReferenceUsage(com.dassault_systemes.modeler.sysml.model.sysml.ReferenceUsage,C)">visitReferenceUsage</a><wbr/>(<a href="sysml/ReferenceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ReferenceUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a ReferenceUsage element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitRenderingDefinition(com.dassault_systemes.modeler.sysml.model.sysml.RenderingDefinition,C)">visitRenderingDefinition</a><wbr/>(<a href="sysml/RenderingDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RenderingDefinition</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a RenderingDefinition element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitRenderingUsage(com.dassault_systemes.modeler.sysml.model.sysml.RenderingUsage,C)">visitRenderingUsage</a><wbr/>(<a href="sysml/RenderingUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RenderingUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a RenderingUsage element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitRequirementConstraintMembership(com.dassault_systemes.modeler.sysml.model.sysml.RequirementConstraintMembership,C)">visitRequirementConstraintMembership</a><wbr/>(<a href="sysml/RequirementConstraintMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementConstraintMembership</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a RequirementConstraintMembership element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitRequirementDefinition(com.dassault_systemes.modeler.sysml.model.sysml.RequirementDefinition,C)">visitRequirementDefinition</a><wbr/>(<a href="sysml/RequirementDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementDefinition</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a RequirementDefinition element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitRequirementUsage(com.dassault_systemes.modeler.sysml.model.sysml.RequirementUsage,C)">visitRequirementUsage</a><wbr/>(<a href="sysml/RequirementUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a RequirementUsage element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitRequirementVerificationMembership(com.dassault_systemes.modeler.sysml.model.sysml.RequirementVerificationMembership,C)">visitRequirementVerificationMembership</a><wbr/>(<a href="sysml/RequirementVerificationMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementVerificationMembership</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a RequirementVerificationMembership element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitSatisfyRequirementUsage(com.dassault_systemes.modeler.sysml.model.sysml.SatisfyRequirementUsage,C)">visitSatisfyRequirementUsage</a><wbr/>(<a href="sysml/SatisfyRequirementUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SatisfyRequirementUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a SatisfyRequirementUsage element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitSendActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.SendActionUsage,C)">visitSendActionUsage</a><wbr/>(<a href="sysml/SendActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SendActionUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a SendActionUsage element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitStakeholderMembership(com.dassault_systemes.modeler.sysml.model.sysml.StakeholderMembership,C)">visitStakeholderMembership</a><wbr/>(<a href="sysml/StakeholderMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">StakeholderMembership</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a StakeholderMembership element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitStateDefinition(com.dassault_systemes.modeler.sysml.model.sysml.StateDefinition,C)">visitStateDefinition</a><wbr/>(<a href="sysml/StateDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">StateDefinition</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a StateDefinition element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitStateSubactionMembership(com.dassault_systemes.modeler.sysml.model.sysml.StateSubactionMembership,C)">visitStateSubactionMembership</a><wbr/>(<a href="sysml/StateSubactionMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">StateSubactionMembership</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a StateSubactionMembership element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitStateUsage(com.dassault_systemes.modeler.sysml.model.sysml.StateUsage,C)">visitStateUsage</a><wbr/>(<a href="sysml/StateUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">StateUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a StateUsage element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitSubjectMembership(com.dassault_systemes.modeler.sysml.model.sysml.SubjectMembership,C)">visitSubjectMembership</a><wbr/>(<a href="sysml/SubjectMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SubjectMembership</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a SubjectMembership element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitSuccessionAsUsage(com.dassault_systemes.modeler.sysml.model.sysml.SuccessionAsUsage,C)">visitSuccessionAsUsage</a><wbr/>(<a href="sysml/SuccessionAsUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SuccessionAsUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a SuccessionAsUsage element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitSuccessionFlowUsage(com.dassault_systemes.modeler.sysml.model.sysml.SuccessionFlowUsage,C)">visitSuccessionFlowUsage</a><wbr/>(<a href="sysml/SuccessionFlowUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SuccessionFlowUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a SuccessionFlowUsage element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitTerminateActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.TerminateActionUsage,C)">visitTerminateActionUsage</a><wbr/>(<a href="sysml/TerminateActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TerminateActionUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a TerminateActionUsage element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitTransitionFeatureMembership(com.dassault_systemes.modeler.sysml.model.sysml.TransitionFeatureMembership,C)">visitTransitionFeatureMembership</a><wbr/>(<a href="sysml/TransitionFeatureMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TransitionFeatureMembership</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a TransitionFeatureMembership element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitTransitionUsage(com.dassault_systemes.modeler.sysml.model.sysml.TransitionUsage,C)">visitTransitionUsage</a><wbr/>(<a href="sysml/TransitionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TransitionUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a TransitionUsage element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitTriggerInvocationExpression(com.dassault_systemes.modeler.sysml.model.sysml.TriggerInvocationExpression,C)">visitTriggerInvocationExpression</a><wbr/>(<a href="sysml/TriggerInvocationExpression.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TriggerInvocationExpression</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a TriggerInvocationExpression element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitUsage(com.dassault_systemes.modeler.sysml.model.sysml.Usage,C)">visitUsage</a><wbr/>(<a href="sysml/Usage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Usage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a Usage element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitUseCaseDefinition(com.dassault_systemes.modeler.sysml.model.sysml.UseCaseDefinition,C)">visitUseCaseDefinition</a><wbr/>(<a href="sysml/UseCaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">UseCaseDefinition</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a UseCaseDefinition element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitUseCaseUsage(com.dassault_systemes.modeler.sysml.model.sysml.UseCaseUsage,C)">visitUseCaseUsage</a><wbr/>(<a href="sysml/UseCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">UseCaseUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a UseCaseUsage element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitVariantMembership(com.dassault_systemes.modeler.sysml.model.sysml.VariantMembership,C)">visitVariantMembership</a><wbr/>(<a href="sysml/VariantMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">VariantMembership</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a VariantMembership element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitVerificationCaseDefinition(com.dassault_systemes.modeler.sysml.model.sysml.VerificationCaseDefinition,C)">visitVerificationCaseDefinition</a><wbr/>(<a href="sysml/VerificationCaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">VerificationCaseDefinition</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a VerificationCaseDefinition element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitVerificationCaseUsage(com.dassault_systemes.modeler.sysml.model.sysml.VerificationCaseUsage,C)">visitVerificationCaseUsage</a><wbr/>(<a href="sysml/VerificationCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">VerificationCaseUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a VerificationCaseUsage element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitViewDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ViewDefinition,C)">visitViewDefinition</a><wbr/>(<a href="sysml/ViewDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewDefinition</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a ViewDefinition element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitViewpointDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ViewpointDefinition,C)">visitViewpointDefinition</a><wbr/>(<a href="sysml/ViewpointDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewpointDefinition</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a ViewpointDefinition element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitViewpointUsage(com.dassault_systemes.modeler.sysml.model.sysml.ViewpointUsage,C)">visitViewpointUsage</a><wbr/>(<a href="sysml/ViewpointUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewpointUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a ViewpointUsage element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitViewRenderingMembership(com.dassault_systemes.modeler.sysml.model.sysml.ViewRenderingMembership,C)">visitViewRenderingMembership</a><wbr/>(<a href="sysml/ViewRenderingMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewRenderingMembership</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a ViewRenderingMembership element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitViewUsage(com.dassault_systemes.modeler.sysml.model.sysml.ViewUsage,C)">visitViewUsage</a><wbr/>(<a href="sysml/ViewUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a ViewUsage element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitWhileLoopActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.WhileLoopActionUsage,C)">visitWhileLoopActionUsage</a><wbr/>(<a href="sysml/WhileLoopActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">WhileLoopActionUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a WhileLoopActionUsage element.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.model.KerMLModelHierarchyVisitor">Methods inherited from interface com.dassault_systemes.modeler.kerml.model.<a href="../../kerml/model/KerMLModelHierarchyVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelHierarchyVisitor</a></h3>
<code><a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitAnnotatingElement(com.dassault_systemes.modeler.kerml.model.kerml.AnnotatingElement,C)">visitAnnotatingElement</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitAnnotation(com.dassault_systemes.modeler.kerml.model.kerml.Annotation,C)">visitAnnotation</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitAssociation(com.dassault_systemes.modeler.kerml.model.kerml.Association,C)">visitAssociation</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitAssociationStructure(com.dassault_systemes.modeler.kerml.model.kerml.AssociationStructure,C)">visitAssociationStructure</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitBehavior(com.dassault_systemes.modeler.kerml.model.kerml.Behavior,C)">visitBehavior</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitBindingConnector(com.dassault_systemes.modeler.kerml.model.kerml.BindingConnector,C)">visitBindingConnector</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitBooleanExpression(com.dassault_systemes.modeler.kerml.model.kerml.BooleanExpression,C)">visitBooleanExpression</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitClass(com.dassault_systemes.modeler.kerml.model.kerml.Class,C)">visitClass</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitClassifier(com.dassault_systemes.modeler.kerml.model.kerml.Classifier,C)">visitClassifier</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitCollectExpression(com.dassault_systemes.modeler.kerml.model.kerml.CollectExpression,C)">visitCollectExpression</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitComment(com.dassault_systemes.modeler.kerml.model.kerml.Comment,C)">visitComment</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitConjugation(com.dassault_systemes.modeler.kerml.model.kerml.Conjugation,C)">visitConjugation</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitConnector(com.dassault_systemes.modeler.kerml.model.kerml.Connector,C)">visitConnector</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitConstructorExpression(com.dassault_systemes.modeler.kerml.model.kerml.ConstructorExpression,C)">visitConstructorExpression</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitCrossSubsetting(com.dassault_systemes.modeler.kerml.model.kerml.CrossSubsetting,C)">visitCrossSubsetting</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitDataType(com.dassault_systemes.modeler.kerml.model.kerml.DataType,C)">visitDataType</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitDependency(com.dassault_systemes.modeler.kerml.model.kerml.Dependency,C)">visitDependency</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitDifferencing(com.dassault_systemes.modeler.kerml.model.kerml.Differencing,C)">visitDifferencing</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitDisjoining(com.dassault_systemes.modeler.kerml.model.kerml.Disjoining,C)">visitDisjoining</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitDocumentation(com.dassault_systemes.modeler.kerml.model.kerml.Documentation,C)">visitDocumentation</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitElement(com.dassault_systemes.modeler.kerml.model.kerml.Element,C)">visitElement</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitElementFilterMembership(com.dassault_systemes.modeler.kerml.model.kerml.ElementFilterMembership,C)">visitElementFilterMembership</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitEndFeatureMembership(com.dassault_systemes.modeler.kerml.model.kerml.EndFeatureMembership,C)">visitEndFeatureMembership</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitExpression(com.dassault_systemes.modeler.kerml.model.kerml.Expression,C)">visitExpression</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature,C)">visitFeature</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitFeatureChainExpression(com.dassault_systemes.modeler.kerml.model.kerml.FeatureChainExpression,C)">visitFeatureChainExpression</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitFeatureChaining(com.dassault_systemes.modeler.kerml.model.kerml.FeatureChaining,C)">visitFeatureChaining</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitFeatureInverting(com.dassault_systemes.modeler.kerml.model.kerml.FeatureInverting,C)">visitFeatureInverting</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitFeatureMembership(com.dassault_systemes.modeler.kerml.model.kerml.FeatureMembership,C)">visitFeatureMembership</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitFeatureReferenceExpression(com.dassault_systemes.modeler.kerml.model.kerml.FeatureReferenceExpression,C)">visitFeatureReferenceExpression</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitFeatureTyping(com.dassault_systemes.modeler.kerml.model.kerml.FeatureTyping,C)">visitFeatureTyping</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitFeatureValue(com.dassault_systemes.modeler.kerml.model.kerml.FeatureValue,C)">visitFeatureValue</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitFlow(com.dassault_systemes.modeler.kerml.model.kerml.Flow,C)">visitFlow</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitFlowEnd(com.dassault_systemes.modeler.kerml.model.kerml.FlowEnd,C)">visitFlowEnd</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitFunction(com.dassault_systemes.modeler.kerml.model.kerml.Function,C)">visitFunction</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitImport(com.dassault_systemes.modeler.kerml.model.kerml.Import,C)">visitImport</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitIndexExpression(com.dassault_systemes.modeler.kerml.model.kerml.IndexExpression,C)">visitIndexExpression</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitInstantiationExpression(com.dassault_systemes.modeler.kerml.model.kerml.InstantiationExpression,C)">visitInstantiationExpression</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitInteraction(com.dassault_systemes.modeler.kerml.model.kerml.Interaction,C)">visitInteraction</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitIntersecting(com.dassault_systemes.modeler.kerml.model.kerml.Intersecting,C)">visitIntersecting</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitInvariant(com.dassault_systemes.modeler.kerml.model.kerml.Invariant,C)">visitInvariant</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitInvocationExpression(com.dassault_systemes.modeler.kerml.model.kerml.InvocationExpression,C)">visitInvocationExpression</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitLibraryPackage(com.dassault_systemes.modeler.kerml.model.kerml.LibraryPackage,C)">visitLibraryPackage</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitLiteralBoolean(com.dassault_systemes.modeler.kerml.model.kerml.LiteralBoolean,C)">visitLiteralBoolean</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitLiteralExpression(com.dassault_systemes.modeler.kerml.model.kerml.LiteralExpression,C)">visitLiteralExpression</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitLiteralInfinity(com.dassault_systemes.modeler.kerml.model.kerml.LiteralInfinity,C)">visitLiteralInfinity</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitLiteralInteger(com.dassault_systemes.modeler.kerml.model.kerml.LiteralInteger,C)">visitLiteralInteger</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitLiteralRational(com.dassault_systemes.modeler.kerml.model.kerml.LiteralRational,C)">visitLiteralRational</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitLiteralString(com.dassault_systemes.modeler.kerml.model.kerml.LiteralString,C)">visitLiteralString</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitMembership(com.dassault_systemes.modeler.kerml.model.kerml.Membership,C)">visitMembership</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitMembershipImport(com.dassault_systemes.modeler.kerml.model.kerml.MembershipImport,C)">visitMembershipImport</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitMetaclass(com.dassault_systemes.modeler.kerml.model.kerml.Metaclass,C)">visitMetaclass</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitMetadataAccessExpression(com.dassault_systemes.modeler.kerml.model.kerml.MetadataAccessExpression,C)">visitMetadataAccessExpression</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitMetadataFeature(com.dassault_systemes.modeler.kerml.model.kerml.MetadataFeature,C)">visitMetadataFeature</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitMultiplicity(com.dassault_systemes.modeler.kerml.model.kerml.Multiplicity,C)">visitMultiplicity</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitMultiplicityRange(com.dassault_systemes.modeler.kerml.model.kerml.MultiplicityRange,C)">visitMultiplicityRange</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitNamespace(com.dassault_systemes.modeler.kerml.model.kerml.Namespace,C)">visitNamespace</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitNamespaceImport(com.dassault_systemes.modeler.kerml.model.kerml.NamespaceImport,C)">visitNamespaceImport</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitNullExpression(com.dassault_systemes.modeler.kerml.model.kerml.NullExpression,C)">visitNullExpression</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitOperatorExpression(com.dassault_systemes.modeler.kerml.model.kerml.OperatorExpression,C)">visitOperatorExpression</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitOwningMembership(com.dassault_systemes.modeler.kerml.model.kerml.OwningMembership,C)">visitOwningMembership</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitPackage(com.dassault_systemes.modeler.kerml.model.kerml.Package,C)">visitPackage</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitParameterMembership(com.dassault_systemes.modeler.kerml.model.kerml.ParameterMembership,C)">visitParameterMembership</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitPayloadFeature(com.dassault_systemes.modeler.kerml.model.kerml.PayloadFeature,C)">visitPayloadFeature</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitPredicate(com.dassault_systemes.modeler.kerml.model.kerml.Predicate,C)">visitPredicate</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitRedefinition(com.dassault_systemes.modeler.kerml.model.kerml.Redefinition,C)">visitRedefinition</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitReferenceSubsetting(com.dassault_systemes.modeler.kerml.model.kerml.ReferenceSubsetting,C)">visitReferenceSubsetting</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Relationship,C)">visitRelationship</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitResultExpressionMembership(com.dassault_systemes.modeler.kerml.model.kerml.ResultExpressionMembership,C)">visitResultExpressionMembership</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitReturnParameterMembership(com.dassault_systemes.modeler.kerml.model.kerml.ReturnParameterMembership,C)">visitReturnParameterMembership</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitSelectExpression(com.dassault_systemes.modeler.kerml.model.kerml.SelectExpression,C)">visitSelectExpression</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitSpecialization(com.dassault_systemes.modeler.kerml.model.kerml.Specialization,C)">visitSpecialization</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitStep(com.dassault_systemes.modeler.kerml.model.kerml.Step,C)">visitStep</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitStructure(com.dassault_systemes.modeler.kerml.model.kerml.Structure,C)">visitStructure</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitSubclassification(com.dassault_systemes.modeler.kerml.model.kerml.Subclassification,C)">visitSubclassification</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitSubsetting(com.dassault_systemes.modeler.kerml.model.kerml.Subsetting,C)">visitSubsetting</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitSuccession(com.dassault_systemes.modeler.kerml.model.kerml.Succession,C)">visitSuccession</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitSuccessionFlow(com.dassault_systemes.modeler.kerml.model.kerml.SuccessionFlow,C)">visitSuccessionFlow</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitTextualRepresentation(com.dassault_systemes.modeler.kerml.model.kerml.TextualRepresentation,C)">visitTextualRepresentation</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitType(com.dassault_systemes.modeler.kerml.model.kerml.Type,C)">visitType</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitTypeFeaturing(com.dassault_systemes.modeler.kerml.model.kerml.TypeFeaturing,C)">visitTypeFeaturing</a>, <a href="../../kerml/model/KerMLModelHierarchyVisitor.html#visitUnioning(com.dassault_systemes.modeler.kerml.model.kerml.Unioning,C)">visitUnioning</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.sysml.model.SysMLModelVisitor">Methods inherited from interface com.dassault_systemes.modeler.sysml.model.<a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a></h3>
<code><a href="SysMLModelVisitor.html#createVisitorContext()">createVisitorContext</a></code></div>
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
<section class="detail" id="getEPackage()">
<h3>getEPackage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">org.eclipse.emf.ecore.EPackage</span> <span class="element-name">getEPackage</span>()</div>
<div class="block">Returns the EPackage that this visitor is suited for.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../kerml/model/KerMLModelHierarchyVisitor.html#getEPackage()">getEPackage</a></code> in interface <code><a href="../../kerml/model/KerMLModelHierarchyVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelHierarchyVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Returns:</dt>
<dd>the EPackage instance</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isAcceptable(org.eclipse.emf.ecore.EPackage)">
<h3>isAcceptable</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">boolean</span> <span class="element-name">isAcceptable</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EPackage ePackage)</span></div>
<div class="block">Checks if the given EPackage elements are acceptable by the visitor.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../kerml/model/KerMLModelHierarchyVisitor.html#isAcceptable(org.eclipse.emf.ecore.EPackage)">isAcceptable</a></code> in interface <code><a href="../../kerml/model/KerMLModelHierarchyVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelHierarchyVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>ePackage</code> - the EPackage to check</dd>
<dt>Returns:</dt>
<dd>true if the EPackage is acceptable, false otherwise</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitAcceptActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.AcceptActionUsage,C)">
<h3 id="visitAcceptActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.AcceptActionUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitAcceptActionUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitAcceptActionUsage</span><wbr/><span class="parameters">(<a href="sysml/AcceptActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AcceptActionUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits an AcceptActionUsage element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitAcceptActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.AcceptActionUsage,C)">visitAcceptActionUsage</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the AcceptActionUsage element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitActionDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ActionDefinition,C)">
<h3 id="visitActionDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ActionDefinition,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitActionDefinition</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitActionDefinition</span><wbr/><span class="parameters">(<a href="sysml/ActionDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActionDefinition</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits an ActionDefinition element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitActionDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ActionDefinition,C)">visitActionDefinition</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the ActionDefinition element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.ActionUsage,C)">
<h3 id="visitActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.ActionUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitActionUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitActionUsage</span><wbr/><span class="parameters">(<a href="sysml/ActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActionUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits an ActionUsage element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.ActionUsage,C)">visitActionUsage</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the ActionUsage element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitActorMembership(com.dassault_systemes.modeler.sysml.model.sysml.ActorMembership,C)">
<h3 id="visitActorMembership(com.dassault_systemes.modeler.sysml.model.sysml.ActorMembership,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitActorMembership</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitActorMembership</span><wbr/><span class="parameters">(<a href="sysml/ActorMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActorMembership</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits an ActorMembership element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitActorMembership(com.dassault_systemes.modeler.sysml.model.sysml.ActorMembership,C)">visitActorMembership</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the ActorMembership element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitAllocationDefinition(com.dassault_systemes.modeler.sysml.model.sysml.AllocationDefinition,C)">
<h3 id="visitAllocationDefinition(com.dassault_systemes.modeler.sysml.model.sysml.AllocationDefinition,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitAllocationDefinition</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitAllocationDefinition</span><wbr/><span class="parameters">(<a href="sysml/AllocationDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AllocationDefinition</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits an AllocationDefinition element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitAllocationDefinition(com.dassault_systemes.modeler.sysml.model.sysml.AllocationDefinition,C)">visitAllocationDefinition</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the AllocationDefinition element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitAllocationUsage(com.dassault_systemes.modeler.sysml.model.sysml.AllocationUsage,C)">
<h3 id="visitAllocationUsage(com.dassault_systemes.modeler.sysml.model.sysml.AllocationUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitAllocationUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitAllocationUsage</span><wbr/><span class="parameters">(<a href="sysml/AllocationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AllocationUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits an AllocationUsage element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitAllocationUsage(com.dassault_systemes.modeler.sysml.model.sysml.AllocationUsage,C)">visitAllocationUsage</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the AllocationUsage element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitAnalysisCaseDefinition(com.dassault_systemes.modeler.sysml.model.sysml.AnalysisCaseDefinition,C)">
<h3 id="visitAnalysisCaseDefinition(com.dassault_systemes.modeler.sysml.model.sysml.AnalysisCaseDefinition,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitAnalysisCaseDefinition</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitAnalysisCaseDefinition</span><wbr/><span class="parameters">(<a href="sysml/AnalysisCaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AnalysisCaseDefinition</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits an AnalysisCaseDefinition element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitAnalysisCaseDefinition(com.dassault_systemes.modeler.sysml.model.sysml.AnalysisCaseDefinition,C)">visitAnalysisCaseDefinition</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the AnalysisCaseDefinition element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitAnalysisCaseUsage(com.dassault_systemes.modeler.sysml.model.sysml.AnalysisCaseUsage,C)">
<h3 id="visitAnalysisCaseUsage(com.dassault_systemes.modeler.sysml.model.sysml.AnalysisCaseUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitAnalysisCaseUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitAnalysisCaseUsage</span><wbr/><span class="parameters">(<a href="sysml/AnalysisCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AnalysisCaseUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits an AnalysisCaseUsage element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitAnalysisCaseUsage(com.dassault_systemes.modeler.sysml.model.sysml.AnalysisCaseUsage,C)">visitAnalysisCaseUsage</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the AnalysisCaseUsage element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitAssertConstraintUsage(com.dassault_systemes.modeler.sysml.model.sysml.AssertConstraintUsage,C)">
<h3 id="visitAssertConstraintUsage(com.dassault_systemes.modeler.sysml.model.sysml.AssertConstraintUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitAssertConstraintUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitAssertConstraintUsage</span><wbr/><span class="parameters">(<a href="sysml/AssertConstraintUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AssertConstraintUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits an AssertConstraintUsage element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitAssertConstraintUsage(com.dassault_systemes.modeler.sysml.model.sysml.AssertConstraintUsage,C)">visitAssertConstraintUsage</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the AssertConstraintUsage element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitAssignmentActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.AssignmentActionUsage,C)">
<h3 id="visitAssignmentActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.AssignmentActionUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitAssignmentActionUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitAssignmentActionUsage</span><wbr/><span class="parameters">(<a href="sysml/AssignmentActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AssignmentActionUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits an AssignmentActionUsage element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitAssignmentActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.AssignmentActionUsage,C)">visitAssignmentActionUsage</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the AssignmentActionUsage element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitAttributeDefinition(com.dassault_systemes.modeler.sysml.model.sysml.AttributeDefinition,C)">
<h3 id="visitAttributeDefinition(com.dassault_systemes.modeler.sysml.model.sysml.AttributeDefinition,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitAttributeDefinition</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitAttributeDefinition</span><wbr/><span class="parameters">(<a href="sysml/AttributeDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AttributeDefinition</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits an AttributeDefinition element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitAttributeDefinition(com.dassault_systemes.modeler.sysml.model.sysml.AttributeDefinition,C)">visitAttributeDefinition</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the AttributeDefinition element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitAttributeUsage(com.dassault_systemes.modeler.sysml.model.sysml.AttributeUsage,C)">
<h3 id="visitAttributeUsage(com.dassault_systemes.modeler.sysml.model.sysml.AttributeUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitAttributeUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitAttributeUsage</span><wbr/><span class="parameters">(<a href="sysml/AttributeUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AttributeUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits an AttributeUsage element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitAttributeUsage(com.dassault_systemes.modeler.sysml.model.sysml.AttributeUsage,C)">visitAttributeUsage</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the AttributeUsage element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitBindingConnectorAsUsage(com.dassault_systemes.modeler.sysml.model.sysml.BindingConnectorAsUsage,C)">
<h3 id="visitBindingConnectorAsUsage(com.dassault_systemes.modeler.sysml.model.sysml.BindingConnectorAsUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitBindingConnectorAsUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitBindingConnectorAsUsage</span><wbr/><span class="parameters">(<a href="sysml/BindingConnectorAsUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">BindingConnectorAsUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a BindingConnectorAsUsage element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitBindingConnectorAsUsage(com.dassault_systemes.modeler.sysml.model.sysml.BindingConnectorAsUsage,C)">visitBindingConnectorAsUsage</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the BindingConnectorAsUsage element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitCalculationDefinition(com.dassault_systemes.modeler.sysml.model.sysml.CalculationDefinition,C)">
<h3 id="visitCalculationDefinition(com.dassault_systemes.modeler.sysml.model.sysml.CalculationDefinition,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitCalculationDefinition</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitCalculationDefinition</span><wbr/><span class="parameters">(<a href="sysml/CalculationDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">CalculationDefinition</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a CalculationDefinition element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitCalculationDefinition(com.dassault_systemes.modeler.sysml.model.sysml.CalculationDefinition,C)">visitCalculationDefinition</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the CalculationDefinition element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitCalculationUsage(com.dassault_systemes.modeler.sysml.model.sysml.CalculationUsage,C)">
<h3 id="visitCalculationUsage(com.dassault_systemes.modeler.sysml.model.sysml.CalculationUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitCalculationUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitCalculationUsage</span><wbr/><span class="parameters">(<a href="sysml/CalculationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">CalculationUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a CalculationUsage element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitCalculationUsage(com.dassault_systemes.modeler.sysml.model.sysml.CalculationUsage,C)">visitCalculationUsage</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the CalculationUsage element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitCaseDefinition(com.dassault_systemes.modeler.sysml.model.sysml.CaseDefinition,C)">
<h3 id="visitCaseDefinition(com.dassault_systemes.modeler.sysml.model.sysml.CaseDefinition,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitCaseDefinition</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitCaseDefinition</span><wbr/><span class="parameters">(<a href="sysml/CaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">CaseDefinition</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a CaseDefinition element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitCaseDefinition(com.dassault_systemes.modeler.sysml.model.sysml.CaseDefinition,C)">visitCaseDefinition</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the CaseDefinition element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitCaseUsage(com.dassault_systemes.modeler.sysml.model.sysml.CaseUsage,C)">
<h3 id="visitCaseUsage(com.dassault_systemes.modeler.sysml.model.sysml.CaseUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitCaseUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitCaseUsage</span><wbr/><span class="parameters">(<a href="sysml/CaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">CaseUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a CaseUsage element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitCaseUsage(com.dassault_systemes.modeler.sysml.model.sysml.CaseUsage,C)">visitCaseUsage</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the CaseUsage element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitConcernDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ConcernDefinition,C)">
<h3 id="visitConcernDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ConcernDefinition,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitConcernDefinition</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitConcernDefinition</span><wbr/><span class="parameters">(<a href="sysml/ConcernDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConcernDefinition</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a ConcernDefinition element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitConcernDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ConcernDefinition,C)">visitConcernDefinition</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the ConcernDefinition element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitConcernUsage(com.dassault_systemes.modeler.sysml.model.sysml.ConcernUsage,C)">
<h3 id="visitConcernUsage(com.dassault_systemes.modeler.sysml.model.sysml.ConcernUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitConcernUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitConcernUsage</span><wbr/><span class="parameters">(<a href="sysml/ConcernUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConcernUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a ConcernUsage element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitConcernUsage(com.dassault_systemes.modeler.sysml.model.sysml.ConcernUsage,C)">visitConcernUsage</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the ConcernUsage element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitConjugatedPortDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ConjugatedPortDefinition,C)">
<h3 id="visitConjugatedPortDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ConjugatedPortDefinition,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitConjugatedPortDefinition</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitConjugatedPortDefinition</span><wbr/><span class="parameters">(<a href="sysml/ConjugatedPortDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConjugatedPortDefinition</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a ConjugatedPortDefinition element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitConjugatedPortDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ConjugatedPortDefinition,C)">visitConjugatedPortDefinition</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the ConjugatedPortDefinition element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitConjugatedPortTyping(com.dassault_systemes.modeler.sysml.model.sysml.ConjugatedPortTyping,C)">
<h3 id="visitConjugatedPortTyping(com.dassault_systemes.modeler.sysml.model.sysml.ConjugatedPortTyping,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitConjugatedPortTyping</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitConjugatedPortTyping</span><wbr/><span class="parameters">(<a href="sysml/ConjugatedPortTyping.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConjugatedPortTyping</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a ConjugatedPortTyping element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitConjugatedPortTyping(com.dassault_systemes.modeler.sysml.model.sysml.ConjugatedPortTyping,C)">visitConjugatedPortTyping</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the ConjugatedPortTyping element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitConnectionDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ConnectionDefinition,C)">
<h3 id="visitConnectionDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ConnectionDefinition,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitConnectionDefinition</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitConnectionDefinition</span><wbr/><span class="parameters">(<a href="sysml/ConnectionDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConnectionDefinition</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a ConnectionDefinition element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitConnectionDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ConnectionDefinition,C)">visitConnectionDefinition</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the ConnectionDefinition element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitConnectionUsage(com.dassault_systemes.modeler.sysml.model.sysml.ConnectionUsage,C)">
<h3 id="visitConnectionUsage(com.dassault_systemes.modeler.sysml.model.sysml.ConnectionUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitConnectionUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitConnectionUsage</span><wbr/><span class="parameters">(<a href="sysml/ConnectionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConnectionUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a ConnectionUsage element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitConnectionUsage(com.dassault_systemes.modeler.sysml.model.sysml.ConnectionUsage,C)">visitConnectionUsage</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the ConnectionUsage element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitConnectorAsUsage(com.dassault_systemes.modeler.sysml.model.sysml.ConnectorAsUsage,C)">
<h3 id="visitConnectorAsUsage(com.dassault_systemes.modeler.sysml.model.sysml.ConnectorAsUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitConnectorAsUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitConnectorAsUsage</span><wbr/><span class="parameters">(<a href="sysml/ConnectorAsUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConnectorAsUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a ConnectorAsUsage element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitConnectorAsUsage(com.dassault_systemes.modeler.sysml.model.sysml.ConnectorAsUsage,C)">visitConnectorAsUsage</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the ConnectorAsUsage element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitConstraintDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ConstraintDefinition,C)">
<h3 id="visitConstraintDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ConstraintDefinition,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitConstraintDefinition</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitConstraintDefinition</span><wbr/><span class="parameters">(<a href="sysml/ConstraintDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConstraintDefinition</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a ConstraintDefinition element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitConstraintDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ConstraintDefinition,C)">visitConstraintDefinition</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the ConstraintDefinition element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitConstraintUsage(com.dassault_systemes.modeler.sysml.model.sysml.ConstraintUsage,C)">
<h3 id="visitConstraintUsage(com.dassault_systemes.modeler.sysml.model.sysml.ConstraintUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitConstraintUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitConstraintUsage</span><wbr/><span class="parameters">(<a href="sysml/ConstraintUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConstraintUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a ConstraintUsage element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitConstraintUsage(com.dassault_systemes.modeler.sysml.model.sysml.ConstraintUsage,C)">visitConstraintUsage</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the ConstraintUsage element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitControlNode(com.dassault_systemes.modeler.sysml.model.sysml.ControlNode,C)">
<h3 id="visitControlNode(com.dassault_systemes.modeler.sysml.model.sysml.ControlNode,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitControlNode</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitControlNode</span><wbr/><span class="parameters">(<a href="sysml/ControlNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ControlNode</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a ControlNode element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitControlNode(com.dassault_systemes.modeler.sysml.model.sysml.ControlNode,C)">visitControlNode</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the ControlNode element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDecisionNode(com.dassault_systemes.modeler.sysml.model.sysml.DecisionNode,C)">
<h3 id="visitDecisionNode(com.dassault_systemes.modeler.sysml.model.sysml.DecisionNode,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitDecisionNode</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitDecisionNode</span><wbr/><span class="parameters">(<a href="sysml/DecisionNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">DecisionNode</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a DecisionNode element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitDecisionNode(com.dassault_systemes.modeler.sysml.model.sysml.DecisionNode,C)">visitDecisionNode</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the DecisionNode element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDefinition(com.dassault_systemes.modeler.sysml.model.sysml.Definition,C)">
<h3 id="visitDefinition(com.dassault_systemes.modeler.sysml.model.sysml.Definition,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitDefinition</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitDefinition</span><wbr/><span class="parameters">(<a href="sysml/Definition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Definition</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a Definition element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitDefinition(com.dassault_systemes.modeler.sysml.model.sysml.Definition,C)">visitDefinition</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the Definition element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitEnumerationDefinition(com.dassault_systemes.modeler.sysml.model.sysml.EnumerationDefinition,C)">
<h3 id="visitEnumerationDefinition(com.dassault_systemes.modeler.sysml.model.sysml.EnumerationDefinition,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitEnumerationDefinition</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitEnumerationDefinition</span><wbr/><span class="parameters">(<a href="sysml/EnumerationDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">EnumerationDefinition</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits an EnumerationDefinition element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitEnumerationDefinition(com.dassault_systemes.modeler.sysml.model.sysml.EnumerationDefinition,C)">visitEnumerationDefinition</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the EnumerationDefinition element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitEnumerationUsage(com.dassault_systemes.modeler.sysml.model.sysml.EnumerationUsage,C)">
<h3 id="visitEnumerationUsage(com.dassault_systemes.modeler.sysml.model.sysml.EnumerationUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitEnumerationUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitEnumerationUsage</span><wbr/><span class="parameters">(<a href="sysml/EnumerationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">EnumerationUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits an EnumerationUsage element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitEnumerationUsage(com.dassault_systemes.modeler.sysml.model.sysml.EnumerationUsage,C)">visitEnumerationUsage</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the EnumerationUsage element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitEventOccurrenceUsage(com.dassault_systemes.modeler.sysml.model.sysml.EventOccurrenceUsage,C)">
<h3 id="visitEventOccurrenceUsage(com.dassault_systemes.modeler.sysml.model.sysml.EventOccurrenceUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitEventOccurrenceUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitEventOccurrenceUsage</span><wbr/><span class="parameters">(<a href="sysml/EventOccurrenceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">EventOccurrenceUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits an EventOccurrenceUsage element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitEventOccurrenceUsage(com.dassault_systemes.modeler.sysml.model.sysml.EventOccurrenceUsage,C)">visitEventOccurrenceUsage</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the EventOccurrenceUsage element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitExhibitStateUsage(com.dassault_systemes.modeler.sysml.model.sysml.ExhibitStateUsage,C)">
<h3 id="visitExhibitStateUsage(com.dassault_systemes.modeler.sysml.model.sysml.ExhibitStateUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitExhibitStateUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitExhibitStateUsage</span><wbr/><span class="parameters">(<a href="sysml/ExhibitStateUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ExhibitStateUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits an ExhibitStateUsage element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitExhibitStateUsage(com.dassault_systemes.modeler.sysml.model.sysml.ExhibitStateUsage,C)">visitExhibitStateUsage</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the ExhibitStateUsage element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitExpose(com.dassault_systemes.modeler.sysml.model.sysml.Expose,C)">
<h3 id="visitExpose(com.dassault_systemes.modeler.sysml.model.sysml.Expose,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitExpose</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitExpose</span><wbr/><span class="parameters">(<a href="sysml/Expose.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Expose</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits an Expose element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitExpose(com.dassault_systemes.modeler.sysml.model.sysml.Expose,C)">visitExpose</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the Expose element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitFlowDefinition(com.dassault_systemes.modeler.sysml.model.sysml.FlowDefinition,C)">
<h3 id="visitFlowDefinition(com.dassault_systemes.modeler.sysml.model.sysml.FlowDefinition,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitFlowDefinition</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitFlowDefinition</span><wbr/><span class="parameters">(<a href="sysml/FlowDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">FlowDefinition</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a FlowDefinition element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitFlowDefinition(com.dassault_systemes.modeler.sysml.model.sysml.FlowDefinition,C)">visitFlowDefinition</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the FlowDefinition element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitFlowUsage(com.dassault_systemes.modeler.sysml.model.sysml.FlowUsage,C)">
<h3 id="visitFlowUsage(com.dassault_systemes.modeler.sysml.model.sysml.FlowUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitFlowUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitFlowUsage</span><wbr/><span class="parameters">(<a href="sysml/FlowUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">FlowUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a FlowUsage element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitFlowUsage(com.dassault_systemes.modeler.sysml.model.sysml.FlowUsage,C)">visitFlowUsage</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the FlowUsage element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitForLoopActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.ForLoopActionUsage,C)">
<h3 id="visitForLoopActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.ForLoopActionUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitForLoopActionUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitForLoopActionUsage</span><wbr/><span class="parameters">(<a href="sysml/ForLoopActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ForLoopActionUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a ForLoopActionUsage element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitForLoopActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.ForLoopActionUsage,C)">visitForLoopActionUsage</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the ForLoopActionUsage element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitForkNode(com.dassault_systemes.modeler.sysml.model.sysml.ForkNode,C)">
<h3 id="visitForkNode(com.dassault_systemes.modeler.sysml.model.sysml.ForkNode,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitForkNode</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitForkNode</span><wbr/><span class="parameters">(<a href="sysml/ForkNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ForkNode</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a ForkNode element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitForkNode(com.dassault_systemes.modeler.sysml.model.sysml.ForkNode,C)">visitForkNode</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the ForkNode element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitFramedConcernMembership(com.dassault_systemes.modeler.sysml.model.sysml.FramedConcernMembership,C)">
<h3 id="visitFramedConcernMembership(com.dassault_systemes.modeler.sysml.model.sysml.FramedConcernMembership,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitFramedConcernMembership</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitFramedConcernMembership</span><wbr/><span class="parameters">(<a href="sysml/FramedConcernMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">FramedConcernMembership</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a FramedConcernMembership element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitFramedConcernMembership(com.dassault_systemes.modeler.sysml.model.sysml.FramedConcernMembership,C)">visitFramedConcernMembership</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the FramedConcernMembership element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitIfActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.IfActionUsage,C)">
<h3 id="visitIfActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.IfActionUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitIfActionUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitIfActionUsage</span><wbr/><span class="parameters">(<a href="sysml/IfActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">IfActionUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits an IfActionUsage element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitIfActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.IfActionUsage,C)">visitIfActionUsage</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the IfActionUsage element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitIncludeUseCaseUsage(com.dassault_systemes.modeler.sysml.model.sysml.IncludeUseCaseUsage,C)">
<h3 id="visitIncludeUseCaseUsage(com.dassault_systemes.modeler.sysml.model.sysml.IncludeUseCaseUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitIncludeUseCaseUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitIncludeUseCaseUsage</span><wbr/><span class="parameters">(<a href="sysml/IncludeUseCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">IncludeUseCaseUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits an IncludeUseCaseUsage element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitIncludeUseCaseUsage(com.dassault_systemes.modeler.sysml.model.sysml.IncludeUseCaseUsage,C)">visitIncludeUseCaseUsage</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the IncludeUseCaseUsage element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInterfaceDefinition(com.dassault_systemes.modeler.sysml.model.sysml.InterfaceDefinition,C)">
<h3 id="visitInterfaceDefinition(com.dassault_systemes.modeler.sysml.model.sysml.InterfaceDefinition,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitInterfaceDefinition</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitInterfaceDefinition</span><wbr/><span class="parameters">(<a href="sysml/InterfaceDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">InterfaceDefinition</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits an InterfaceDefinition element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitInterfaceDefinition(com.dassault_systemes.modeler.sysml.model.sysml.InterfaceDefinition,C)">visitInterfaceDefinition</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the InterfaceDefinition element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInterfaceUsage(com.dassault_systemes.modeler.sysml.model.sysml.InterfaceUsage,C)">
<h3 id="visitInterfaceUsage(com.dassault_systemes.modeler.sysml.model.sysml.InterfaceUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitInterfaceUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitInterfaceUsage</span><wbr/><span class="parameters">(<a href="sysml/InterfaceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">InterfaceUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits an InterfaceUsage element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitInterfaceUsage(com.dassault_systemes.modeler.sysml.model.sysml.InterfaceUsage,C)">visitInterfaceUsage</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the InterfaceUsage element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitItemDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ItemDefinition,C)">
<h3 id="visitItemDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ItemDefinition,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitItemDefinition</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitItemDefinition</span><wbr/><span class="parameters">(<a href="sysml/ItemDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ItemDefinition</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits an ItemDefinition element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitItemDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ItemDefinition,C)">visitItemDefinition</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the ItemDefinition element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitItemUsage(com.dassault_systemes.modeler.sysml.model.sysml.ItemUsage,C)">
<h3 id="visitItemUsage(com.dassault_systemes.modeler.sysml.model.sysml.ItemUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitItemUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitItemUsage</span><wbr/><span class="parameters">(<a href="sysml/ItemUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ItemUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits an ItemUsage element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitItemUsage(com.dassault_systemes.modeler.sysml.model.sysml.ItemUsage,C)">visitItemUsage</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the ItemUsage element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitJoinNode(com.dassault_systemes.modeler.sysml.model.sysml.JoinNode,C)">
<h3 id="visitJoinNode(com.dassault_systemes.modeler.sysml.model.sysml.JoinNode,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitJoinNode</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitJoinNode</span><wbr/><span class="parameters">(<a href="sysml/JoinNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">JoinNode</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a JoinNode element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitJoinNode(com.dassault_systemes.modeler.sysml.model.sysml.JoinNode,C)">visitJoinNode</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the JoinNode element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitLoopActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.LoopActionUsage,C)">
<h3 id="visitLoopActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.LoopActionUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitLoopActionUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitLoopActionUsage</span><wbr/><span class="parameters">(<a href="sysml/LoopActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">LoopActionUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a LoopActionUsage element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitLoopActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.LoopActionUsage,C)">visitLoopActionUsage</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the LoopActionUsage element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitMembershipExpose(com.dassault_systemes.modeler.sysml.model.sysml.MembershipExpose,C)">
<h3 id="visitMembershipExpose(com.dassault_systemes.modeler.sysml.model.sysml.MembershipExpose,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitMembershipExpose</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitMembershipExpose</span><wbr/><span class="parameters">(<a href="sysml/MembershipExpose.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">MembershipExpose</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a MembershipExpose element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitMembershipExpose(com.dassault_systemes.modeler.sysml.model.sysml.MembershipExpose,C)">visitMembershipExpose</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the MembershipExpose element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitMergeNode(com.dassault_systemes.modeler.sysml.model.sysml.MergeNode,C)">
<h3 id="visitMergeNode(com.dassault_systemes.modeler.sysml.model.sysml.MergeNode,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitMergeNode</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitMergeNode</span><wbr/><span class="parameters">(<a href="sysml/MergeNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">MergeNode</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a MergeNode element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitMergeNode(com.dassault_systemes.modeler.sysml.model.sysml.MergeNode,C)">visitMergeNode</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the MergeNode element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitMetadataDefinition(com.dassault_systemes.modeler.sysml.model.sysml.MetadataDefinition,C)">
<h3 id="visitMetadataDefinition(com.dassault_systemes.modeler.sysml.model.sysml.MetadataDefinition,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitMetadataDefinition</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitMetadataDefinition</span><wbr/><span class="parameters">(<a href="sysml/MetadataDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">MetadataDefinition</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a MetadataDefinition element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitMetadataDefinition(com.dassault_systemes.modeler.sysml.model.sysml.MetadataDefinition,C)">visitMetadataDefinition</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the MetadataDefinition element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitMetadataUsage(com.dassault_systemes.modeler.sysml.model.sysml.MetadataUsage,C)">
<h3 id="visitMetadataUsage(com.dassault_systemes.modeler.sysml.model.sysml.MetadataUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitMetadataUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitMetadataUsage</span><wbr/><span class="parameters">(<a href="sysml/MetadataUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">MetadataUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a MetadataUsage element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitMetadataUsage(com.dassault_systemes.modeler.sysml.model.sysml.MetadataUsage,C)">visitMetadataUsage</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the MetadataUsage element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitNamespaceExpose(com.dassault_systemes.modeler.sysml.model.sysml.NamespaceExpose,C)">
<h3 id="visitNamespaceExpose(com.dassault_systemes.modeler.sysml.model.sysml.NamespaceExpose,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitNamespaceExpose</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitNamespaceExpose</span><wbr/><span class="parameters">(<a href="sysml/NamespaceExpose.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">NamespaceExpose</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a NamespaceExpose element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitNamespaceExpose(com.dassault_systemes.modeler.sysml.model.sysml.NamespaceExpose,C)">visitNamespaceExpose</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the NamespaceExpose element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitObjectiveMembership(com.dassault_systemes.modeler.sysml.model.sysml.ObjectiveMembership,C)">
<h3 id="visitObjectiveMembership(com.dassault_systemes.modeler.sysml.model.sysml.ObjectiveMembership,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitObjectiveMembership</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitObjectiveMembership</span><wbr/><span class="parameters">(<a href="sysml/ObjectiveMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ObjectiveMembership</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits an ObjectiveMembership element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitObjectiveMembership(com.dassault_systemes.modeler.sysml.model.sysml.ObjectiveMembership,C)">visitObjectiveMembership</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the ObjectiveMembership element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitOccurrenceDefinition(com.dassault_systemes.modeler.sysml.model.sysml.OccurrenceDefinition,C)">
<h3 id="visitOccurrenceDefinition(com.dassault_systemes.modeler.sysml.model.sysml.OccurrenceDefinition,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitOccurrenceDefinition</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitOccurrenceDefinition</span><wbr/><span class="parameters">(<a href="sysml/OccurrenceDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">OccurrenceDefinition</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits an OccurrenceDefinition element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitOccurrenceDefinition(com.dassault_systemes.modeler.sysml.model.sysml.OccurrenceDefinition,C)">visitOccurrenceDefinition</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the OccurrenceDefinition element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitOccurrenceUsage(com.dassault_systemes.modeler.sysml.model.sysml.OccurrenceUsage,C)">
<h3 id="visitOccurrenceUsage(com.dassault_systemes.modeler.sysml.model.sysml.OccurrenceUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitOccurrenceUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitOccurrenceUsage</span><wbr/><span class="parameters">(<a href="sysml/OccurrenceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">OccurrenceUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits an OccurrenceUsage element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitOccurrenceUsage(com.dassault_systemes.modeler.sysml.model.sysml.OccurrenceUsage,C)">visitOccurrenceUsage</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the OccurrenceUsage element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPartDefinition(com.dassault_systemes.modeler.sysml.model.sysml.PartDefinition,C)">
<h3 id="visitPartDefinition(com.dassault_systemes.modeler.sysml.model.sysml.PartDefinition,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitPartDefinition</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitPartDefinition</span><wbr/><span class="parameters">(<a href="sysml/PartDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PartDefinition</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a PartDefinition element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitPartDefinition(com.dassault_systemes.modeler.sysml.model.sysml.PartDefinition,C)">visitPartDefinition</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the PartDefinition element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPartUsage(com.dassault_systemes.modeler.sysml.model.sysml.PartUsage,C)">
<h3 id="visitPartUsage(com.dassault_systemes.modeler.sysml.model.sysml.PartUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitPartUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitPartUsage</span><wbr/><span class="parameters">(<a href="sysml/PartUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PartUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a PartUsage element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitPartUsage(com.dassault_systemes.modeler.sysml.model.sysml.PartUsage,C)">visitPartUsage</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the PartUsage element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPerformActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.PerformActionUsage,C)">
<h3 id="visitPerformActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.PerformActionUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitPerformActionUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitPerformActionUsage</span><wbr/><span class="parameters">(<a href="sysml/PerformActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PerformActionUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a PerformActionUsage element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitPerformActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.PerformActionUsage,C)">visitPerformActionUsage</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the PerformActionUsage element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPortConjugation(com.dassault_systemes.modeler.sysml.model.sysml.PortConjugation,C)">
<h3 id="visitPortConjugation(com.dassault_systemes.modeler.sysml.model.sysml.PortConjugation,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitPortConjugation</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitPortConjugation</span><wbr/><span class="parameters">(<a href="sysml/PortConjugation.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PortConjugation</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a PortConjugation element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitPortConjugation(com.dassault_systemes.modeler.sysml.model.sysml.PortConjugation,C)">visitPortConjugation</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the PortConjugation element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPortDefinition(com.dassault_systemes.modeler.sysml.model.sysml.PortDefinition,C)">
<h3 id="visitPortDefinition(com.dassault_systemes.modeler.sysml.model.sysml.PortDefinition,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitPortDefinition</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitPortDefinition</span><wbr/><span class="parameters">(<a href="sysml/PortDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PortDefinition</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a PortDefinition element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitPortDefinition(com.dassault_systemes.modeler.sysml.model.sysml.PortDefinition,C)">visitPortDefinition</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the PortDefinition element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPortUsage(com.dassault_systemes.modeler.sysml.model.sysml.PortUsage,C)">
<h3 id="visitPortUsage(com.dassault_systemes.modeler.sysml.model.sysml.PortUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitPortUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitPortUsage</span><wbr/><span class="parameters">(<a href="sysml/PortUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PortUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a PortUsage element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitPortUsage(com.dassault_systemes.modeler.sysml.model.sysml.PortUsage,C)">visitPortUsage</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the PortUsage element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitReferenceUsage(com.dassault_systemes.modeler.sysml.model.sysml.ReferenceUsage,C)">
<h3 id="visitReferenceUsage(com.dassault_systemes.modeler.sysml.model.sysml.ReferenceUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitReferenceUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitReferenceUsage</span><wbr/><span class="parameters">(<a href="sysml/ReferenceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ReferenceUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a ReferenceUsage element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitReferenceUsage(com.dassault_systemes.modeler.sysml.model.sysml.ReferenceUsage,C)">visitReferenceUsage</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the ReferenceUsage element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitRenderingDefinition(com.dassault_systemes.modeler.sysml.model.sysml.RenderingDefinition,C)">
<h3 id="visitRenderingDefinition(com.dassault_systemes.modeler.sysml.model.sysml.RenderingDefinition,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitRenderingDefinition</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitRenderingDefinition</span><wbr/><span class="parameters">(<a href="sysml/RenderingDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RenderingDefinition</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a RenderingDefinition element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitRenderingDefinition(com.dassault_systemes.modeler.sysml.model.sysml.RenderingDefinition,C)">visitRenderingDefinition</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the RenderingDefinition element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitRenderingUsage(com.dassault_systemes.modeler.sysml.model.sysml.RenderingUsage,C)">
<h3 id="visitRenderingUsage(com.dassault_systemes.modeler.sysml.model.sysml.RenderingUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitRenderingUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitRenderingUsage</span><wbr/><span class="parameters">(<a href="sysml/RenderingUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RenderingUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a RenderingUsage element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitRenderingUsage(com.dassault_systemes.modeler.sysml.model.sysml.RenderingUsage,C)">visitRenderingUsage</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the RenderingUsage element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitRequirementConstraintMembership(com.dassault_systemes.modeler.sysml.model.sysml.RequirementConstraintMembership,C)">
<h3 id="visitRequirementConstraintMembership(com.dassault_systemes.modeler.sysml.model.sysml.RequirementConstraintMembership,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitRequirementConstraintMembership</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitRequirementConstraintMembership</span><wbr/><span class="parameters">(<a href="sysml/RequirementConstraintMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementConstraintMembership</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a RequirementConstraintMembership element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitRequirementConstraintMembership(com.dassault_systemes.modeler.sysml.model.sysml.RequirementConstraintMembership,C)">visitRequirementConstraintMembership</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the RequirementConstraintMembership element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitRequirementDefinition(com.dassault_systemes.modeler.sysml.model.sysml.RequirementDefinition,C)">
<h3 id="visitRequirementDefinition(com.dassault_systemes.modeler.sysml.model.sysml.RequirementDefinition,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitRequirementDefinition</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitRequirementDefinition</span><wbr/><span class="parameters">(<a href="sysml/RequirementDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementDefinition</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a RequirementDefinition element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitRequirementDefinition(com.dassault_systemes.modeler.sysml.model.sysml.RequirementDefinition,C)">visitRequirementDefinition</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the RequirementDefinition element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitRequirementUsage(com.dassault_systemes.modeler.sysml.model.sysml.RequirementUsage,C)">
<h3 id="visitRequirementUsage(com.dassault_systemes.modeler.sysml.model.sysml.RequirementUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitRequirementUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitRequirementUsage</span><wbr/><span class="parameters">(<a href="sysml/RequirementUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a RequirementUsage element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitRequirementUsage(com.dassault_systemes.modeler.sysml.model.sysml.RequirementUsage,C)">visitRequirementUsage</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the RequirementUsage element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitRequirementVerificationMembership(com.dassault_systemes.modeler.sysml.model.sysml.RequirementVerificationMembership,C)">
<h3 id="visitRequirementVerificationMembership(com.dassault_systemes.modeler.sysml.model.sysml.RequirementVerificationMembership,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitRequirementVerificationMembership</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitRequirementVerificationMembership</span><wbr/><span class="parameters">(<a href="sysml/RequirementVerificationMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementVerificationMembership</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a RequirementVerificationMembership element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitRequirementVerificationMembership(com.dassault_systemes.modeler.sysml.model.sysml.RequirementVerificationMembership,C)">visitRequirementVerificationMembership</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the RequirementVerificationMembership element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitSatisfyRequirementUsage(com.dassault_systemes.modeler.sysml.model.sysml.SatisfyRequirementUsage,C)">
<h3 id="visitSatisfyRequirementUsage(com.dassault_systemes.modeler.sysml.model.sysml.SatisfyRequirementUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitSatisfyRequirementUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitSatisfyRequirementUsage</span><wbr/><span class="parameters">(<a href="sysml/SatisfyRequirementUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SatisfyRequirementUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a SatisfyRequirementUsage element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitSatisfyRequirementUsage(com.dassault_systemes.modeler.sysml.model.sysml.SatisfyRequirementUsage,C)">visitSatisfyRequirementUsage</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the SatisfyRequirementUsage element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitSendActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.SendActionUsage,C)">
<h3 id="visitSendActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.SendActionUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitSendActionUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitSendActionUsage</span><wbr/><span class="parameters">(<a href="sysml/SendActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SendActionUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a SendActionUsage element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitSendActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.SendActionUsage,C)">visitSendActionUsage</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the SendActionUsage element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitStakeholderMembership(com.dassault_systemes.modeler.sysml.model.sysml.StakeholderMembership,C)">
<h3 id="visitStakeholderMembership(com.dassault_systemes.modeler.sysml.model.sysml.StakeholderMembership,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitStakeholderMembership</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitStakeholderMembership</span><wbr/><span class="parameters">(<a href="sysml/StakeholderMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">StakeholderMembership</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a StakeholderMembership element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitStakeholderMembership(com.dassault_systemes.modeler.sysml.model.sysml.StakeholderMembership,C)">visitStakeholderMembership</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the StakeholderMembership element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitStateDefinition(com.dassault_systemes.modeler.sysml.model.sysml.StateDefinition,C)">
<h3 id="visitStateDefinition(com.dassault_systemes.modeler.sysml.model.sysml.StateDefinition,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitStateDefinition</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitStateDefinition</span><wbr/><span class="parameters">(<a href="sysml/StateDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">StateDefinition</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a StateDefinition element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitStateDefinition(com.dassault_systemes.modeler.sysml.model.sysml.StateDefinition,C)">visitStateDefinition</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the StateDefinition element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitStateSubactionMembership(com.dassault_systemes.modeler.sysml.model.sysml.StateSubactionMembership,C)">
<h3 id="visitStateSubactionMembership(com.dassault_systemes.modeler.sysml.model.sysml.StateSubactionMembership,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitStateSubactionMembership</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitStateSubactionMembership</span><wbr/><span class="parameters">(<a href="sysml/StateSubactionMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">StateSubactionMembership</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a StateSubactionMembership element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitStateSubactionMembership(com.dassault_systemes.modeler.sysml.model.sysml.StateSubactionMembership,C)">visitStateSubactionMembership</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the StateSubactionMembership element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitStateUsage(com.dassault_systemes.modeler.sysml.model.sysml.StateUsage,C)">
<h3 id="visitStateUsage(com.dassault_systemes.modeler.sysml.model.sysml.StateUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitStateUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitStateUsage</span><wbr/><span class="parameters">(<a href="sysml/StateUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">StateUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a StateUsage element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitStateUsage(com.dassault_systemes.modeler.sysml.model.sysml.StateUsage,C)">visitStateUsage</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the StateUsage element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitSubjectMembership(com.dassault_systemes.modeler.sysml.model.sysml.SubjectMembership,C)">
<h3 id="visitSubjectMembership(com.dassault_systemes.modeler.sysml.model.sysml.SubjectMembership,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitSubjectMembership</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitSubjectMembership</span><wbr/><span class="parameters">(<a href="sysml/SubjectMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SubjectMembership</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a SubjectMembership element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitSubjectMembership(com.dassault_systemes.modeler.sysml.model.sysml.SubjectMembership,C)">visitSubjectMembership</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the SubjectMembership element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitSuccessionAsUsage(com.dassault_systemes.modeler.sysml.model.sysml.SuccessionAsUsage,C)">
<h3 id="visitSuccessionAsUsage(com.dassault_systemes.modeler.sysml.model.sysml.SuccessionAsUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitSuccessionAsUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitSuccessionAsUsage</span><wbr/><span class="parameters">(<a href="sysml/SuccessionAsUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SuccessionAsUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a SuccessionAsUsage element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitSuccessionAsUsage(com.dassault_systemes.modeler.sysml.model.sysml.SuccessionAsUsage,C)">visitSuccessionAsUsage</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the SuccessionAsUsage element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitSuccessionFlowUsage(com.dassault_systemes.modeler.sysml.model.sysml.SuccessionFlowUsage,C)">
<h3 id="visitSuccessionFlowUsage(com.dassault_systemes.modeler.sysml.model.sysml.SuccessionFlowUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitSuccessionFlowUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitSuccessionFlowUsage</span><wbr/><span class="parameters">(<a href="sysml/SuccessionFlowUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SuccessionFlowUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a SuccessionFlowUsage element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitSuccessionFlowUsage(com.dassault_systemes.modeler.sysml.model.sysml.SuccessionFlowUsage,C)">visitSuccessionFlowUsage</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the SuccessionFlowUsage element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTerminateActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.TerminateActionUsage,C)">
<h3 id="visitTerminateActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.TerminateActionUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitTerminateActionUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitTerminateActionUsage</span><wbr/><span class="parameters">(<a href="sysml/TerminateActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TerminateActionUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a TerminateActionUsage element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitTerminateActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.TerminateActionUsage,C)">visitTerminateActionUsage</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the TerminateActionUsage element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTransitionFeatureMembership(com.dassault_systemes.modeler.sysml.model.sysml.TransitionFeatureMembership,C)">
<h3 id="visitTransitionFeatureMembership(com.dassault_systemes.modeler.sysml.model.sysml.TransitionFeatureMembership,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitTransitionFeatureMembership</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitTransitionFeatureMembership</span><wbr/><span class="parameters">(<a href="sysml/TransitionFeatureMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TransitionFeatureMembership</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a TransitionFeatureMembership element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitTransitionFeatureMembership(com.dassault_systemes.modeler.sysml.model.sysml.TransitionFeatureMembership,C)">visitTransitionFeatureMembership</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the TransitionFeatureMembership element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTransitionUsage(com.dassault_systemes.modeler.sysml.model.sysml.TransitionUsage,C)">
<h3 id="visitTransitionUsage(com.dassault_systemes.modeler.sysml.model.sysml.TransitionUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitTransitionUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitTransitionUsage</span><wbr/><span class="parameters">(<a href="sysml/TransitionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TransitionUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a TransitionUsage element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitTransitionUsage(com.dassault_systemes.modeler.sysml.model.sysml.TransitionUsage,C)">visitTransitionUsage</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the TransitionUsage element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTriggerInvocationExpression(com.dassault_systemes.modeler.sysml.model.sysml.TriggerInvocationExpression,C)">
<h3 id="visitTriggerInvocationExpression(com.dassault_systemes.modeler.sysml.model.sysml.TriggerInvocationExpression,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitTriggerInvocationExpression</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitTriggerInvocationExpression</span><wbr/><span class="parameters">(<a href="sysml/TriggerInvocationExpression.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TriggerInvocationExpression</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a TriggerInvocationExpression element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitTriggerInvocationExpression(com.dassault_systemes.modeler.sysml.model.sysml.TriggerInvocationExpression,C)">visitTriggerInvocationExpression</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the TriggerInvocationExpression element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitUsage(com.dassault_systemes.modeler.sysml.model.sysml.Usage,C)">
<h3 id="visitUsage(com.dassault_systemes.modeler.sysml.model.sysml.Usage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitUsage</span><wbr/><span class="parameters">(<a href="sysml/Usage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Usage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a Usage element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitUsage(com.dassault_systemes.modeler.sysml.model.sysml.Usage,C)">visitUsage</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the Usage element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitUseCaseDefinition(com.dassault_systemes.modeler.sysml.model.sysml.UseCaseDefinition,C)">
<h3 id="visitUseCaseDefinition(com.dassault_systemes.modeler.sysml.model.sysml.UseCaseDefinition,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitUseCaseDefinition</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitUseCaseDefinition</span><wbr/><span class="parameters">(<a href="sysml/UseCaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">UseCaseDefinition</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a UseCaseDefinition element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitUseCaseDefinition(com.dassault_systemes.modeler.sysml.model.sysml.UseCaseDefinition,C)">visitUseCaseDefinition</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the UseCaseDefinition element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitUseCaseUsage(com.dassault_systemes.modeler.sysml.model.sysml.UseCaseUsage,C)">
<h3 id="visitUseCaseUsage(com.dassault_systemes.modeler.sysml.model.sysml.UseCaseUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitUseCaseUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitUseCaseUsage</span><wbr/><span class="parameters">(<a href="sysml/UseCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">UseCaseUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a UseCaseUsage element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitUseCaseUsage(com.dassault_systemes.modeler.sysml.model.sysml.UseCaseUsage,C)">visitUseCaseUsage</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the UseCaseUsage element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitVariantMembership(com.dassault_systemes.modeler.sysml.model.sysml.VariantMembership,C)">
<h3 id="visitVariantMembership(com.dassault_systemes.modeler.sysml.model.sysml.VariantMembership,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitVariantMembership</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitVariantMembership</span><wbr/><span class="parameters">(<a href="sysml/VariantMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">VariantMembership</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a VariantMembership element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitVariantMembership(com.dassault_systemes.modeler.sysml.model.sysml.VariantMembership,C)">visitVariantMembership</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the VariantMembership element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitVerificationCaseDefinition(com.dassault_systemes.modeler.sysml.model.sysml.VerificationCaseDefinition,C)">
<h3 id="visitVerificationCaseDefinition(com.dassault_systemes.modeler.sysml.model.sysml.VerificationCaseDefinition,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitVerificationCaseDefinition</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitVerificationCaseDefinition</span><wbr/><span class="parameters">(<a href="sysml/VerificationCaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">VerificationCaseDefinition</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a VerificationCaseDefinition element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitVerificationCaseDefinition(com.dassault_systemes.modeler.sysml.model.sysml.VerificationCaseDefinition,C)">visitVerificationCaseDefinition</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the VerificationCaseDefinition element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitVerificationCaseUsage(com.dassault_systemes.modeler.sysml.model.sysml.VerificationCaseUsage,C)">
<h3 id="visitVerificationCaseUsage(com.dassault_systemes.modeler.sysml.model.sysml.VerificationCaseUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitVerificationCaseUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitVerificationCaseUsage</span><wbr/><span class="parameters">(<a href="sysml/VerificationCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">VerificationCaseUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a VerificationCaseUsage element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitVerificationCaseUsage(com.dassault_systemes.modeler.sysml.model.sysml.VerificationCaseUsage,C)">visitVerificationCaseUsage</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the VerificationCaseUsage element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitViewDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ViewDefinition,C)">
<h3 id="visitViewDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ViewDefinition,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitViewDefinition</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitViewDefinition</span><wbr/><span class="parameters">(<a href="sysml/ViewDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewDefinition</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a ViewDefinition element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitViewDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ViewDefinition,C)">visitViewDefinition</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the ViewDefinition element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitViewRenderingMembership(com.dassault_systemes.modeler.sysml.model.sysml.ViewRenderingMembership,C)">
<h3 id="visitViewRenderingMembership(com.dassault_systemes.modeler.sysml.model.sysml.ViewRenderingMembership,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitViewRenderingMembership</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitViewRenderingMembership</span><wbr/><span class="parameters">(<a href="sysml/ViewRenderingMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewRenderingMembership</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a ViewRenderingMembership element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitViewRenderingMembership(com.dassault_systemes.modeler.sysml.model.sysml.ViewRenderingMembership,C)">visitViewRenderingMembership</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the ViewRenderingMembership element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitViewUsage(com.dassault_systemes.modeler.sysml.model.sysml.ViewUsage,C)">
<h3 id="visitViewUsage(com.dassault_systemes.modeler.sysml.model.sysml.ViewUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitViewUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitViewUsage</span><wbr/><span class="parameters">(<a href="sysml/ViewUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a ViewUsage element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitViewUsage(com.dassault_systemes.modeler.sysml.model.sysml.ViewUsage,C)">visitViewUsage</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the ViewUsage element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitViewpointDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ViewpointDefinition,C)">
<h3 id="visitViewpointDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ViewpointDefinition,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitViewpointDefinition</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitViewpointDefinition</span><wbr/><span class="parameters">(<a href="sysml/ViewpointDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewpointDefinition</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a ViewpointDefinition element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitViewpointDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ViewpointDefinition,C)">visitViewpointDefinition</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the ViewpointDefinition element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitViewpointUsage(com.dassault_systemes.modeler.sysml.model.sysml.ViewpointUsage,C)">
<h3 id="visitViewpointUsage(com.dassault_systemes.modeler.sysml.model.sysml.ViewpointUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitViewpointUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitViewpointUsage</span><wbr/><span class="parameters">(<a href="sysml/ViewpointUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewpointUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a ViewpointUsage element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitViewpointUsage(com.dassault_systemes.modeler.sysml.model.sysml.ViewpointUsage,C)">visitViewpointUsage</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the ViewpointUsage element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitWhileLoopActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.WhileLoopActionUsage,C)">
<h3 id="visitWhileLoopActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.WhileLoopActionUsage,com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext)">visitWhileLoopActionUsage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitWhileLoopActionUsage</span><wbr/><span class="parameters">(<a href="sysml/WhileLoopActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">WhileLoopActionUsage</a> element,
 <a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a WhileLoopActionUsage element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="SysMLModelVisitor.html#visitWhileLoopActionUsage(com.dassault_systemes.modeler.sysml.model.sysml.WhileLoopActionUsage,C)">visitWhileLoopActionUsage</a></code> in interface <code><a href="SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;<a href="SysMLModelHierarchyVisitor.html" title="type parameter in SysMLModelHierarchyVisitor">C</a> extends <a href="SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the WhileLoopActionUsage element to visit</dd>
<dd><code>context</code> - the visitor context</dd>
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
