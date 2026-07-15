# JAVA OPENAPI: PresentationElementVisitor (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/uml/PresentationElementVisitor.html
- source_path: `com/nomagic/magicdraw/uml/PresentationElementVisitor.html`
- source_sha256: `83dadae8b9b73aafe0b078454f9891a3865dd5b95dc8b3a7d25ab3682d2e4c8e`
- captured_utc: `2026-07-14T16:55:58.464492+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml](package-summary.html)

## Interface PresentationElementVisitor

All Known Implementing Classes:
`[InheritanceVisitor](InheritanceVisitor.html)`, `[Visitor](Visitor.html)`

@OpenApipublic interfacePresentationElementVisitor

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsDefault Methods
Modifier and Type
Method
Description
`default void`
`[visitAbstractBaseCompartmentView](#visitAbstractBaseCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.AbstractCompartmentView))(com.nomagic.magicdraw.uml.symbols.shapes.AbstractCompartmentView o)`

`default void`
`[visitAbstractDiagramPresentationElement](#visitAbstractDiagramPresentationElement(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement))([AbstractDiagramPresentationElement](symbols/AbstractDiagramPresentationElement.html) o)`
Method visits given object.
`default void`
`[visitAbstractDiagramPresentationElementContainer](#visitAbstractDiagramPresentationElementContainer(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElementContainer))(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElementContainer o)`

`default void`
`[visitAbstractHeaderShapeView](#visitAbstractHeaderShapeView(com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView))(com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView o)`

`default void`
`[visitAbstractImageShapeView](#visitAbstractImageShapeView(com.nomagic.magicdraw.uml.symbols.shapes.AbstractImageShapeView))(com.nomagic.magicdraw.uml.symbols.shapes.AbstractImageShapeView imageShapeView)`

`default void`
`[visitAbstractPathEndShape](#visitAbstractPathEndShape(com.nomagic.magicdraw.uml.symbols.shapes.AbstractPathEndShape))(com.nomagic.magicdraw.uml.symbols.shapes.AbstractPathEndShape o)`

`default void`
`[visitAbstractSeparatorView](#visitAbstractSeparatorView(com.nomagic.magicdraw.uml.symbols.shapes.AbstractSeparatorView))(com.nomagic.magicdraw.uml.symbols.shapes.AbstractSeparatorView o)`

`default void`
`[visitAbstractShapeWithLabels](#visitAbstractShapeWithLabels(com.nomagic.magicdraw.uml.symbols.shapes.AbstractShapeWithLabels))(com.nomagic.magicdraw.uml.symbols.shapes.AbstractShapeWithLabels o)`

`default void`
`[visitAbstractShapeWithLabelsInside](#visitAbstractShapeWithLabelsInside(com.nomagic.magicdraw.uml.symbols.shapes.AbstractShapeWithLabelsInside))(com.nomagic.magicdraw.uml.symbols.shapes.AbstractShapeWithLabelsInside o)`

`default void`
`[visitAbstractTextBoxView](#visitAbstractTextBoxView(com.nomagic.magicdraw.uml.symbols.shapes.AbstractTextBoxView))(com.nomagic.magicdraw.uml.symbols.shapes.AbstractTextBoxView o)`

`default void`
`[visitActionHeaderView](#visitActionHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.ActionHeaderView))(com.nomagic.magicdraw.uml.symbols.shapes.ActionHeaderView o)`

`default void`
`[visitActionView](#visitActionView(com.nomagic.magicdraw.uml.symbols.shapes.ActionView))([ActionView](symbols/shapes/ActionView.html) o)`

`default void`
`[visitActivationView](#visitActivationView(com.nomagic.magicdraw.uml.symbols.shapes.ActivationView))([ActivationView](symbols/shapes/ActivationView.html) o)`

`default void`
`[visitActivityGroupView](#visitActivityGroupView(com.nomagic.magicdraw.uml.symbols.shapes.ActivityGroupView))(com.nomagic.magicdraw.uml.symbols.shapes.ActivityGroupView o)`

`default void`
`[visitActivityObjectViewContainer](#visitActivityObjectViewContainer(com.nomagic.magicdraw.uml.symbols.ActivityObjectViewContainer))(com.nomagic.magicdraw.uml.symbols.ActivityObjectViewContainer o)`

`default void`
`[visitActorView](#visitActorView(com.nomagic.magicdraw.uml.symbols.shapes.ActorView))([ActorView](symbols/shapes/ActorView.html) o)`

`default void`
`[visitArtifactsCompartmentView](#visitArtifactsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.ArtifactsCompartmentView))(com.nomagic.magicdraw.uml.symbols.shapes.ArtifactsCompartmentView o)`

`default void`
`[visitArtifactView](#visitArtifactView(com.nomagic.magicdraw.uml.symbols.shapes.ArtifactView))([ArtifactView](symbols/shapes/ArtifactView.html) o)`

`default void`
`[visitAssociationClassView](#visitAssociationClassView(com.nomagic.magicdraw.uml.symbols.paths.AssociationClassView))([AssociationClassView](symbols/paths/AssociationClassView.html) o)`

`default void`
`[visitAssociationTextBoxView](#visitAssociationTextBoxView(com.nomagic.magicdraw.uml.symbols.shapes.AssociationTextBoxView))(com.nomagic.magicdraw.uml.symbols.shapes.AssociationTextBoxView o)`

`default void`
`[visitAssociationView](#visitAssociationView(com.nomagic.magicdraw.uml.symbols.paths.AssociationView))([AssociationView](symbols/paths/AssociationView.html) o)`

`default void`
`[visitAttributesCompartmentView](#visitAttributesCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.AttributesCompartmentView))(com.nomagic.magicdraw.uml.symbols.shapes.AttributesCompartmentView o)`

`default void`
`[visitAttributeView](#visitAttributeView(com.nomagic.magicdraw.uml.symbols.shapes.AttributeView))(com.nomagic.magicdraw.uml.symbols.shapes.AttributeView o)`

`default void`
`[visitBarView](#visitBarView(com.nomagic.magicdraw.uml.symbols.shapes.BarView))([BarView](symbols/shapes/BarView.html) o)`

`default void`
`[visitBaseCompartmentView](#visitBaseCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.BaseCompartmentView))(com.nomagic.magicdraw.uml.symbols.shapes.BaseCompartmentView o)`

`default void`
`[visitBaseElementTextArea](#visitBaseElementTextArea(com.nomagic.magicdraw.uml.symbols.shapes.BaseElementTextArea))(com.nomagic.magicdraw.uml.symbols.shapes.BaseElementTextArea o)`

`default void`
`[visitBaseElementTextField](#visitBaseElementTextField(com.nomagic.magicdraw.uml.symbols.shapes.BaseElementTextField))(com.nomagic.magicdraw.uml.symbols.shapes.BaseElementTextField o)`

`default void`
`[visitBaseFlowView](#visitBaseFlowView(com.nomagic.magicdraw.uml.symbols.paths.BaseFlowView))(com.nomagic.magicdraw.uml.symbols.paths.BaseFlowView o)`

`default void`
`[visitBaseHeaderShapeView](#visitBaseHeaderShapeView(com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView))(com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView o)`

`default void`
`[visitBaseHeaderView](#visitBaseHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderView))(com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderView o)`

`default void`
`[visitBaseLifelineHeaderView](#visitBaseLifelineHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.BaseLifelineHeaderView))(com.nomagic.magicdraw.uml.symbols.shapes.BaseLifelineHeaderView o)`

`default void`
`[visitBaseLifelineView](#visitBaseLifelineView(com.nomagic.magicdraw.uml.symbols.shapes.BaseLifelineView))(com.nomagic.magicdraw.uml.symbols.shapes.BaseLifelineView o)`

`default void`
`[visitBaseMembersCompartmentView](#visitBaseMembersCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.BaseMembersCompartmentView))(com.nomagic.magicdraw.uml.symbols.shapes.BaseMembersCompartmentView o)`

`default void`
`[visitBaseNameHeaderView](#visitBaseNameHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.BaseNameHeaderView))(com.nomagic.magicdraw.uml.symbols.shapes.BaseNameHeaderView o)`

`default void`
`[visitBasePropertiesCompartmentView](#visitBasePropertiesCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.BasePropertiesCompartmentView))(com.nomagic.magicdraw.uml.symbols.shapes.BasePropertiesCompartmentView o)`

`default void`
`[visitBaseRealizationView](#visitBaseRealizationView(com.nomagic.magicdraw.uml.symbols.paths.BaseRealizationView))(com.nomagic.magicdraw.uml.symbols.paths.BaseRealizationView o)`

`default void`
`[visitBaseSplitCompartmentView](#visitBaseSplitCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.BaseSplitCompartmentView))(com.nomagic.magicdraw.uml.symbols.shapes.BaseSplitCompartmentView o)`

`default void`
`[visitBaseTreeShape](#visitBaseTreeShape(com.nomagic.magicdraw.uml.symbols.shapes.BaseTreeShape))(com.nomagic.magicdraw.uml.symbols.shapes.BaseTreeShape o)`

`default void`
`[visitBehavioralFeatureView](#visitBehavioralFeatureView(com.nomagic.magicdraw.uml.symbols.shapes.BehavioralFeatureView))(com.nomagic.magicdraw.uml.symbols.shapes.BehavioralFeatureView o)`

`default void`
`[visitBehaviorLabelView](#visitBehaviorLabelView(com.nomagic.magicdraw.uml.symbols.shapes.BehaviorLabelView))(com.nomagic.magicdraw.uml.symbols.shapes.BehaviorLabelView behaviorLabelView)`

`default void`
`[visitBehaviorsCompartmentView](#visitBehaviorsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.BehaviorsCompartmentView))(com.nomagic.magicdraw.uml.symbols.shapes.BehaviorsCompartmentView o)`

`default void`
`[visitBehaviorView](#visitBehaviorView(com.nomagic.magicdraw.uml.symbols.shapes.BehaviorView))(com.nomagic.magicdraw.uml.symbols.shapes.BehaviorView o)`

`default void`
`[visitBodyRegionView](#visitBodyRegionView(com.nomagic.magicdraw.uml.symbols.shapes.ClauseView.BodyRegionView))(com.nomagic.magicdraw.uml.symbols.shapes.ClauseView.BodyRegionView o)`

`default void`
`[visitBodyRegionView](#visitBodyRegionView(com.nomagic.magicdraw.uml.symbols.shapes.LoopNodeView.BodyRegionView))(com.nomagic.magicdraw.uml.symbols.shapes.LoopNodeView.BodyRegionView o)`

`default void`
`[visitCallBehaviorActionHeaderView](#visitCallBehaviorActionHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.CallBehaviorActionHeaderView))(com.nomagic.magicdraw.uml.symbols.shapes.CallBehaviorActionHeaderView callBehaviorActionHeaderView)`

`default void`
`[visitCallBehaviorActionView](#visitCallBehaviorActionView(com.nomagic.magicdraw.uml.symbols.shapes.CallBehaviorActionView))([CallBehaviorActionView](symbols/shapes/CallBehaviorActionView.html) o)`

`default void`
`[visitCallOperationActionView](#visitCallOperationActionView(com.nomagic.magicdraw.uml.symbols.shapes.CallOperationActionView))([CallOperationActionView](symbols/shapes/CallOperationActionView.html) o)`

`default void`
`[visitClassHeaderView](#visitClassHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.ClassHeaderView))(com.nomagic.magicdraw.uml.symbols.shapes.ClassHeaderView o)`

`default void`
`[visitClassifierHeaderView](#visitClassifierHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.ClassifierHeaderView))(com.nomagic.magicdraw.uml.symbols.shapes.ClassifierHeaderView o)`

`default void`
`[visitClassifierView](#visitClassifierView(com.nomagic.magicdraw.uml.symbols.shapes.ClassifierView))([ClassifierView](symbols/shapes/ClassifierView.html) o)`

`default void`
`[visitClassView](#visitClassView(com.nomagic.magicdraw.uml.symbols.shapes.ClassView))([ClassView](symbols/shapes/ClassView.html) o)`

`default void`
`[visitClauseCompartmentView](#visitClauseCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.ClauseCompartmentView))(com.nomagic.magicdraw.uml.symbols.shapes.ClauseCompartmentView o)`

`default void`
`[visitClauseView](#visitClauseView(com.nomagic.magicdraw.uml.symbols.shapes.ClauseView))(com.nomagic.magicdraw.uml.symbols.shapes.ClauseView o)`

`default void`
`[visitCollaborationHeaderView](#visitCollaborationHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.CollaborationHeaderView))(com.nomagic.magicdraw.uml.symbols.shapes.CollaborationHeaderView o)`

`default void`
`[visitCollaborationUseView](#visitCollaborationUseView(com.nomagic.magicdraw.uml.symbols.shapes.CollaborationUseView))([CollaborationUseView](symbols/shapes/CollaborationUseView.html) o)`

`default void`
`[visitCollaborationView](#visitCollaborationView(com.nomagic.magicdraw.uml.symbols.shapes.CollaborationView))([CollaborationView](symbols/shapes/CollaborationView.html) o)`

`default void`
`[visitCombinedFragmentHeaderView](#visitCombinedFragmentHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.CombinedFragmentHeaderView))(com.nomagic.magicdraw.uml.symbols.shapes.CombinedFragmentHeaderView o)`

`default void`
`[visitCombinedFragmentView](#visitCombinedFragmentView(com.nomagic.magicdraw.uml.symbols.shapes.CombinedFragmentView))([CombinedFragmentView](symbols/shapes/CombinedFragmentView.html) o)`

`default void`
`[visitCommentView](#visitCommentView(com.nomagic.magicdraw.uml.symbols.shapes.CommentView))([CommentView](symbols/shapes/CommentView.html) o)`

`default void`
`[visitCommunicationPathView](#visitCommunicationPathView(com.nomagic.magicdraw.uml.symbols.paths.CommunicationPathView))([CommunicationPathView](symbols/paths/CommunicationPathView.html) o)`

`default void`
`[visitCompartmentElement](#visitCompartmentElement(com.nomagic.magicdraw.uml.CompartmentElement))([CompartmentElement](CompartmentElement.html) o)`
Method visitCompartmentElement.
`default void`
`[visitComponentHeaderView](#visitComponentHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.ComponentHeaderView))(com.nomagic.magicdraw.uml.symbols.shapes.ComponentHeaderView o)`

`default void`
`[visitComponentView](#visitComponentView(com.nomagic.magicdraw.uml.symbols.shapes.ComponentView))([ComponentView](symbols/shapes/ComponentView.html) o)`

`default void`
`[visitConditionalNodeView](#visitConditionalNodeView(com.nomagic.magicdraw.uml.symbols.shapes.ConditionalNodeView))([ConditionalNodeView](symbols/shapes/ConditionalNodeView.html) o)`

`default void`
`[visitConnectorEndView](#visitConnectorEndView(com.nomagic.magicdraw.uml.symbols.shapes.ConnectorEndView))(com.nomagic.magicdraw.uml.symbols.shapes.ConnectorEndView o)`

`default void`
`[visitConnectorToSelfView](#visitConnectorToSelfView(com.nomagic.magicdraw.uml.symbols.paths.ConnectorToSelfView))([ConnectorToSelfView](symbols/paths/ConnectorToSelfView.html) o)`

`default void`
`[visitConnectorView](#visitConnectorView(com.nomagic.magicdraw.uml.symbols.paths.ConnectorView))([ConnectorView](symbols/paths/ConnectorView.html) o)`

`default void`
`[visitConstraintCompartmentView](#visitConstraintCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.ConstraintCompartmentView))(com.nomagic.magicdraw.uml.symbols.shapes.ConstraintCompartmentView o)`

`default void`
`[visitConstraintLinkView](#visitConstraintLinkView(com.nomagic.magicdraw.uml.symbols.paths.ConstraintLinkView))([ConstraintLinkView](symbols/paths/ConstraintLinkView.html) o)`

`default void`
`[visitConstraintsCompartmentView](#visitConstraintsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.ConstraintsCompartmentView))(com.nomagic.magicdraw.uml.symbols.shapes.ConstraintsCompartmentView o)`

`default void`
`[visitConstraintsView](#visitConstraintsView(com.nomagic.magicdraw.uml.symbols.shapes.ConstraintsView))(com.nomagic.magicdraw.uml.symbols.shapes.ConstraintsView o)`

`default void`
`[visitContainerLinkView](#visitContainerLinkView(com.nomagic.magicdraw.uml.symbols.paths.ContainerLinkView))(com.nomagic.magicdraw.uml.symbols.paths.ContainerLinkView o)`

`default void`
`[visitContainerShapeView](#visitContainerShapeView(com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView))(com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView o)`

`default void`
`[visitContainmentLinkView](#visitContainmentLinkView(com.nomagic.magicdraw.uml.symbols.paths.ContainmentLinkView))([ContainmentLinkView](symbols/paths/ContainmentLinkView.html) o)`

`default void`
`[visitContentShape](#visitContentShape(com.nomagic.magicdraw.uml.symbols.shapes.ContentShape))([ContentShape](symbols/shapes/ContentShape.html) o)`

`default void`
`[visitControlFlowView](#visitControlFlowView(com.nomagic.magicdraw.uml.symbols.paths.ControlFlowView))([ControlFlowView](symbols/paths/ControlFlowView.html) o)`

`default void`
`[visitConveyedInformationView](#visitConveyedInformationView(com.nomagic.magicdraw.uml.symbols.shapes.ConveyedInformationView))(com.nomagic.magicdraw.uml.symbols.shapes.ConveyedInformationView o)`

`default void`
`[visitCustomCompartmentView](#visitCustomCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.CustomCompartmentView))(com.nomagic.magicdraw.uml.symbols.shapes.CustomCompartmentView o)`

`default void`
`[visitCustomElementCompartmentView](#visitCustomElementCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.CustomElementCompartmentView))(com.nomagic.magicdraw.uml.symbols.shapes.CustomElementCompartmentView o)`

`default void`
`[visitDataTypeView](#visitDataTypeView(com.nomagic.magicdraw.uml.symbols.shapes.DataTypeView))([DataTypeView](symbols/shapes/DataTypeView.html) o)`

`default void`
`[visitDecisionView](#visitDecisionView(com.nomagic.magicdraw.uml.symbols.shapes.DecisionView))([DecisionView](symbols/shapes/DecisionView.html) o)`

`default void`
`[visitDependencyView](#visitDependencyView(com.nomagic.magicdraw.uml.symbols.paths.DependencyView))([DependencyView](symbols/paths/DependencyView.html) o)`

`default void`
`[visitDeployedElementsCompartmentView](#visitDeployedElementsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.DeployedElementsCompartmentView))(com.nomagic.magicdraw.uml.symbols.shapes.DeployedElementsCompartmentView o)`

`default void`
`[visitDeploymentView](#visitDeploymentView(com.nomagic.magicdraw.uml.symbols.paths.DeploymentView))([DeploymentView](symbols/paths/DeploymentView.html) o)`

`default void`
`[visitDiagramFrameHeaderView](#visitDiagramFrameHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.DiagramFrameHeaderView))(com.nomagic.magicdraw.uml.symbols.shapes.DiagramFrameHeaderView diagramFrameHeaderView)`

`default void`
`[visitDiagramFrameLabelView](#visitDiagramFrameLabelView(com.nomagic.magicdraw.uml.symbols.shapes.DiagramFrameLabelView))(com.nomagic.magicdraw.uml.symbols.shapes.DiagramFrameLabelView diagramFrameLabelView)`

`default void`
`[visitDiagramFrameView](#visitDiagramFrameView(com.nomagic.magicdraw.uml.symbols.shapes.DiagramFrameView))([DiagramFrameView](symbols/shapes/DiagramFrameView.html) diagramFrameView)`

`default void`
`[visitDiagramLegendShape](#visitDiagramLegendShape(com.nomagic.magicdraw.uml.symbols.shapes.DiagramLegendShape))([DiagramLegendShape](symbols/shapes/DiagramLegendShape.html) o)`

`default void`
`[visitDiagramObjectViewContainer](#visitDiagramObjectViewContainer(com.nomagic.magicdraw.uml.symbols.DiagramObjectViewContainer))(com.nomagic.magicdraw.uml.symbols.DiagramObjectViewContainer o)`

`default void`
`[visitDiagramOverviewCompartmentView](#visitDiagramOverviewCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.DiagramOverviewCompartmentView))(com.nomagic.magicdraw.uml.symbols.shapes.DiagramOverviewCompartmentView o)`

`default void`
`[visitDiagramPresentationElement](#visitDiagramPresentationElement(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement))([DiagramPresentationElement](symbols/DiagramPresentationElement.html) o)`
Method visits given object.
`default void`
`[visitDiagramPropertiesShape](#visitDiagramPropertiesShape(com.nomagic.magicdraw.uml.symbols.shapes.DiagramPropertiesShape))([DiagramPropertiesShape](symbols/shapes/DiagramPropertiesShape.html) o)`

`default void`
`[visitDiagramShape](#visitDiagramShape(com.nomagic.magicdraw.uml.symbols.shapes.DiagramShape))([DiagramShape](symbols/shapes/DiagramShape.html) o)`

`default void`
`[visitDirectionIconView](#visitDirectionIconView(com.nomagic.magicdraw.uml.symbols.shapes.DirectionIconView))(com.nomagic.magicdraw.uml.symbols.shapes.DirectionIconView o)`

`default void`
`[visitDummyDiagramObjectViewContainer](#visitDummyDiagramObjectViewContainer(com.nomagic.magicdraw.uml.symbols.DummyDiagramObjectViewContainer))(com.nomagic.magicdraw.uml.symbols.DummyDiagramObjectViewContainer o)`

`default void`
`[visitDurationConstraintView](#visitDurationConstraintView(com.nomagic.magicdraw.uml.symbols.paths.DurationConstraintView))([DurationConstraintView](symbols/paths/DurationConstraintView.html) o)`

`default void`
`[visitElementCompartmentView](#visitElementCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.ElementCompartmentView))(com.nomagic.magicdraw.uml.symbols.shapes.ElementCompartmentView o)`

`default void`
`[visitElementImportView](#visitElementImportView(com.nomagic.magicdraw.uml.symbols.paths.ElementImportView))([ElementImportView](symbols/paths/ElementImportView.html) o)`

`default void`
`[visitElementPropertiesCompartmentView](#visitElementPropertiesCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.ElementPropertiesCompartmentView))(com.nomagic.magicdraw.uml.symbols.shapes.ElementPropertiesCompartmentView o)`

`default void`
`[visitElementTaggedValueView](#visitElementTaggedValueView(com.nomagic.magicdraw.uml.symbols.shapes.ElementTaggedValueView))(com.nomagic.magicdraw.uml.symbols.shapes.ElementTaggedValueView o)`

`default void`
`[visitElementWithIconView](#visitElementWithIconView(com.nomagic.magicdraw.uml.symbols.shapes.ElementWithIconView))(com.nomagic.magicdraw.uml.symbols.shapes.ElementWithIconView o)`

`default void`
`[visitElseRegionView](#visitElseRegionView(com.nomagic.magicdraw.uml.symbols.shapes.ClauseView.ElseRegionView))(com.nomagic.magicdraw.uml.symbols.shapes.ClauseView.ElseRegionView o)`

`default void`
`[visitEmbeddedImageShapeView](#visitEmbeddedImageShapeView(com.nomagic.magicdraw.uml.symbols.shapes.EmbeddedImageShapeView))(com.nomagic.magicdraw.uml.symbols.shapes.EmbeddedImageShapeView imageShapeView)`

`default void`
`[visitEnumerationHeaderView](#visitEnumerationHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.EnumerationHeaderView))(com.nomagic.magicdraw.uml.symbols.shapes.EnumerationHeaderView o)`

`default void`
`[visitEnumerationLiteralsCompartmentView](#visitEnumerationLiteralsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.EnumerationLiteralsCompartmentView))(com.nomagic.magicdraw.uml.symbols.shapes.EnumerationLiteralsCompartmentView o)`

`default void`
`[visitEnumerationLiteralView](#visitEnumerationLiteralView(com.nomagic.magicdraw.uml.symbols.shapes.EnumerationLiteralView))(com.nomagic.magicdraw.uml.symbols.shapes.EnumerationLiteralView o)`

`default void`
`[visitEnumerationView](#visitEnumerationView(com.nomagic.magicdraw.uml.symbols.shapes.EnumerationView))([EnumerationView](symbols/shapes/EnumerationView.html) o)`

`default void`
`[visitExceptionHandlerView](#visitExceptionHandlerView(com.nomagic.magicdraw.uml.symbols.paths.ExceptionHandlerView))([ExceptionHandlerView](symbols/paths/ExceptionHandlerView.html) o)`

`default void`
`[visitExpansionNodeView](#visitExpansionNodeView(com.nomagic.magicdraw.uml.symbols.shapes.ExpansionNodeView))([ExpansionNodeView](symbols/shapes/ExpansionNodeView.html) o)`

`default void`
`[visitExpansionRegionView](#visitExpansionRegionView(com.nomagic.magicdraw.uml.symbols.shapes.ExpansionRegionView))([ExpansionRegionView](symbols/shapes/ExpansionRegionView.html) o)`

`default void`
`[visitExtendView](#visitExtendView(com.nomagic.magicdraw.uml.symbols.paths.ExtendView))([ExtendView](symbols/paths/ExtendView.html) o)`

`default void`
`[visitExtensionPointsCompartmentView](#visitExtensionPointsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.ExtensionPointsCompartmentView))(com.nomagic.magicdraw.uml.symbols.shapes.ExtensionPointsCompartmentView o)`

`default void`
`[visitExtensionPointView](#visitExtensionPointView(com.nomagic.magicdraw.uml.symbols.shapes.ExtensionPointView))(com.nomagic.magicdraw.uml.symbols.shapes.ExtensionPointView o)`

`default void`
`[visitExtensionView](#visitExtensionView(com.nomagic.magicdraw.uml.symbols.paths.ExtensionView))([ExtensionView](symbols/paths/ExtensionView.html) o)`

`default void`
`[visitFlowConnectorView](#visitFlowConnectorView(com.nomagic.magicdraw.uml.symbols.shapes.FlowConnectorView))([FlowConnectorView](symbols/shapes/FlowConnectorView.html) o)`

`default void`
`[visitFoundMessageView](#visitFoundMessageView(com.nomagic.magicdraw.uml.symbols.paths.FoundMessageView))([FoundMessageView](symbols/paths/FoundMessageView.html) foundMessageView)`
Visits found message view.
`default void`
`[visitFragmentView](#visitFragmentView(com.nomagic.magicdraw.uml.symbols.shapes.FragmentView))(com.nomagic.magicdraw.uml.symbols.shapes.FragmentView o)`

`default void`
`[visitFrameHeaderView](#visitFrameHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.FrameHeaderView))(com.nomagic.magicdraw.uml.symbols.shapes.FrameHeaderView o)`

`default void`
`[visitFrameView](#visitFrameView(com.nomagic.magicdraw.uml.symbols.shapes.FrameView))(com.nomagic.magicdraw.uml.symbols.shapes.FrameView o)`

`default void`
`[visitGeneralizationSetHeaderView](#visitGeneralizationSetHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.GeneralizationSetHeaderView))(com.nomagic.magicdraw.uml.symbols.shapes.GeneralizationSetHeaderView o)`

`default void`
`[visitGeneralizationSetView](#visitGeneralizationSetView(com.nomagic.magicdraw.uml.symbols.shapes.GeneralizationSetView))([GeneralizationSetView](symbols/shapes/GeneralizationSetView.html) o)`

`default void`
`[visitGeneralizationView](#visitGeneralizationView(com.nomagic.magicdraw.uml.symbols.paths.GeneralizationView))([GeneralizationView](symbols/paths/GeneralizationView.html) o)`

`default void`
`[visitGenericView](#visitGenericView(com.nomagic.magicdraw.uml.symbols.shapes.GenericView))([GenericView](symbols/shapes/GenericView.html) o)`

`default void`
`[visitHeaderOfBaseHeaderShapeView](#visitHeaderOfBaseHeaderShapeView(com.nomagic.magicdraw.uml.symbols.shapes.HeaderOfBaseHeaderShapeView))(com.nomagic.magicdraw.uml.symbols.shapes.HeaderOfBaseHeaderShapeView o)`

`default void`
`[visitHeaderShapeView](#visitHeaderShapeView(com.nomagic.magicdraw.uml.symbols.shapes.HeaderShapeView))(com.nomagic.magicdraw.uml.symbols.shapes.HeaderShapeView o)`

`default void`
`[visitHeaderView](#visitHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.HeaderView))(com.nomagic.magicdraw.uml.symbols.shapes.HeaderView o)`

`default void`
`[visitImageShapeFromElementView](#visitImageShapeFromElementView(com.nomagic.magicdraw.uml.symbols.shapes.ImageShapeFromElementView))(com.nomagic.magicdraw.uml.symbols.shapes.ImageShapeFromElementView imageShapeView)`

`default void`
`[visitImageShapeView](#visitImageShapeView(com.nomagic.magicdraw.uml.symbols.shapes.ImageShapeView))([ImageShapeView](symbols/shapes/ImageShapeView.html) imageShapeView)`
Visits image shape view.
`default void`
`[visitImageView](#visitImageView(com.nomagic.magicdraw.uml.symbols.shapes.ImageView))(com.nomagic.magicdraw.uml.symbols.shapes.ImageView o)`

`default void`
`[visitIncludeView](#visitIncludeView(com.nomagic.magicdraw.uml.symbols.paths.IncludeView))([IncludeView](symbols/paths/IncludeView.html) o)`

`default void`
`[visitInformationFlowView](#visitInformationFlowView(com.nomagic.magicdraw.uml.symbols.paths.InformationFlowView))([InformationFlowView](symbols/paths/InformationFlowView.html) informationFlowView)`

`default void`
`[visitInformationItemHeaderView](#visitInformationItemHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.InformationItemHeaderView))(com.nomagic.magicdraw.uml.symbols.shapes.InformationItemHeaderView o)`

`default void`
`[visitInformationItemView](#visitInformationItemView(com.nomagic.magicdraw.uml.symbols.shapes.InformationItemView))([InformationItemView](symbols/shapes/InformationItemView.html) informationItemView)`

`default void`
`[visitInnerElementsCompartmentView](#visitInnerElementsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.InnerElementsCompartmentView))(com.nomagic.magicdraw.uml.symbols.shapes.InnerElementsCompartmentView o)`

`default void`
`[visitInstanceSlotsCompartmentView](#visitInstanceSlotsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.InstanceSlotsCompartmentView))(com.nomagic.magicdraw.uml.symbols.shapes.InstanceSlotsCompartmentView o)`

`default void`
`[visitInstanceSpecificationHeaderView](#visitInstanceSpecificationHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.InstanceSpecificationHeaderView))(com.nomagic.magicdraw.uml.symbols.shapes.InstanceSpecificationHeaderView o)`

`default void`
`[visitInstanceSpecificationView](#visitInstanceSpecificationView(com.nomagic.magicdraw.uml.symbols.shapes.InstanceSpecificationView))([InstanceSpecificationView](symbols/shapes/InstanceSpecificationView.html) o)`

`default void`
`[visitInteractionOperandsCompartmentView](#visitInteractionOperandsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.InteractionOperandsCompartmentView))(com.nomagic.magicdraw.uml.symbols.shapes.InteractionOperandsCompartmentView o)`

`default void`
`[visitInteractionOperandView](#visitInteractionOperandView(com.nomagic.magicdraw.uml.symbols.shapes.InteractionOperandView))(com.nomagic.magicdraw.uml.symbols.shapes.InteractionOperandView o)`

`default void`
`[visitInteractionUseOverviewView](#visitInteractionUseOverviewView(com.nomagic.magicdraw.uml.symbols.shapes.InteractionUseOverviewView))([InteractionUseOverviewView](symbols/shapes/InteractionUseOverviewView.html) o)`

`default void`
`[visitInteractionUseView](#visitInteractionUseView(com.nomagic.magicdraw.uml.symbols.shapes.InteractionUseView))([InteractionUseView](symbols/shapes/InteractionUseView.html) o)`

`default void`
`[visitInterfaceHeaderView](#visitInterfaceHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.InterfaceHeaderView))(com.nomagic.magicdraw.uml.symbols.shapes.InterfaceHeaderView o)`

`default void`
`[visitInterfaceRealizationView](#visitInterfaceRealizationView(com.nomagic.magicdraw.uml.symbols.paths.InterfaceRealizationView))([InterfaceRealizationView](symbols/paths/InterfaceRealizationView.html) o)`

`default void`
`[visitInterfacesCompartmentView](#visitInterfacesCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.InterfacesCompartmentView))(com.nomagic.magicdraw.uml.symbols.shapes.InterfacesCompartmentView o)`

`default void`
`[visitInterfaceView](#visitInterfaceView(com.nomagic.magicdraw.uml.symbols.shapes.InterfaceView))([InterfaceView](symbols/shapes/InterfaceView.html) o)`

`default void`
`[visitInternalStateCompartmentView](#visitInternalStateCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.InternalStateCompartmentView))(com.nomagic.magicdraw.uml.symbols.shapes.InternalStateCompartmentView o)`

`default void`
`[visitInterruptibleActivityRegionView](#visitInterruptibleActivityRegionView(com.nomagic.magicdraw.uml.symbols.shapes.InterruptibleActivityRegionView))([InterruptibleActivityRegionView](symbols/shapes/InterruptibleActivityRegionView.html) o)`

`default void`
`[visitLegendItemsCompartmentView](#visitLegendItemsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.LegendItemsCompartmentView))(com.nomagic.magicdraw.uml.symbols.shapes.LegendItemsCompartmentView o)`

`default void`
`[visitLegendItemView](#visitLegendItemView(com.nomagic.magicdraw.uml.symbols.shapes.LegendItemView))(com.nomagic.magicdraw.uml.symbols.shapes.LegendItemView o)`

`default void`
`[visitLifeLineLineView](#visitLifeLineLineView(com.nomagic.magicdraw.uml.symbols.shapes.LifeLineLineView))([LifeLineLineView](symbols/shapes/LifeLineLineView.html) o)`

`default void`
`[visitLifelineView](#visitLifelineView(com.nomagic.magicdraw.uml.symbols.shapes.LifelineView))([LifelineView](symbols/shapes/LifelineView.html) o)`

`default void`
`[visitLinkAttributeView](#visitLinkAttributeView(com.nomagic.magicdraw.uml.symbols.paths.LinkAttributeView))([LinkAttributeView](symbols/paths/LinkAttributeView.html) o)`

`default void`
`[visitLinkEndView](#visitLinkEndView(com.nomagic.magicdraw.uml.symbols.shapes.LinkEndView))(com.nomagic.magicdraw.uml.symbols.shapes.LinkEndView o)`

`default void`
`[visitLinkView](#visitLinkView(com.nomagic.magicdraw.uml.symbols.paths.LinkView))([LinkView](symbols/paths/LinkView.html) o)`

`default void`
`[visitLinkWithEndsView](#visitLinkWithEndsView(com.nomagic.magicdraw.uml.symbols.paths.LinkWithEndsView))(com.nomagic.magicdraw.uml.symbols.paths.LinkWithEndsView o)`

`default void`
`[visitLinkWithRolesView](#visitLinkWithRolesView(com.nomagic.magicdraw.uml.symbols.paths.LinkWithRolesView))(com.nomagic.magicdraw.uml.symbols.paths.LinkWithRolesView o)`

`default void`
`[visitLinkWithStereotype](#visitLinkWithStereotype(com.nomagic.magicdraw.uml.symbols.paths.LinkWithStereotype))(com.nomagic.magicdraw.uml.symbols.paths.LinkWithStereotype o)`

`default void`
`[visitListElementView](#visitListElementView(com.nomagic.magicdraw.uml.symbols.shapes.ListElementView))(com.nomagic.magicdraw.uml.symbols.shapes.ListElementView o)`

`default void`
`[visitLoopNodeView](#visitLoopNodeView(com.nomagic.magicdraw.uml.symbols.shapes.LoopNodeView))([LoopNodeView](symbols/shapes/LoopNodeView.html) o)`

`default void`
`[visitLostFoundMessageView](#visitLostFoundMessageView(com.nomagic.magicdraw.uml.symbols.paths.LostFoundMessageView))(com.nomagic.magicdraw.uml.symbols.paths.LostFoundMessageView lostFoundMessageView)`
Visits lost/found message view.
`default void`
`[visitLostMessageView](#visitLostMessageView(com.nomagic.magicdraw.uml.symbols.paths.LostMessageView))([LostMessageView](symbols/paths/LostMessageView.html) lostMessageView)`
Visits lost message view.
`default void`
`[visitMemberView](#visitMemberView(com.nomagic.magicdraw.uml.symbols.shapes.MemberView))(com.nomagic.magicdraw.uml.symbols.shapes.MemberView o)`

`default void`
`[visitMessageSignatureView](#visitMessageSignatureView(com.nomagic.magicdraw.uml.symbols.shapes.MessageSignatureView))(com.nomagic.magicdraw.uml.symbols.shapes.MessageSignatureView o)`

`default void`
`[visitMessageView](#visitMessageView(com.nomagic.magicdraw.uml.symbols.shapes.MessageView))([MessageView](symbols/shapes/MessageView.html) o)`

`default void`
`[visitNNaryAssociationView](#visitNNaryAssociationView(com.nomagic.magicdraw.uml.symbols.shapes.NNaryAssociationView))([NNaryAssociationView](symbols/shapes/NNaryAssociationView.html) o)`

`default void`
`[visitNodeHeaderView](#visitNodeHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.NodeHeaderView))(com.nomagic.magicdraw.uml.symbols.shapes.NodeHeaderView o)`

`default void`
`[visitNodeInstanceSpecificationHeaderView](#visitNodeInstanceSpecificationHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.NodeInstanceSpecificationHeaderView))(com.nomagic.magicdraw.uml.symbols.shapes.NodeInstanceSpecificationHeaderView o)`

`default void`
`[visitNodeInstanceSpecificationView](#visitNodeInstanceSpecificationView(com.nomagic.magicdraw.uml.symbols.shapes.NodeInstanceSpecificationView))([NodeInstanceSpecificationView](symbols/shapes/NodeInstanceSpecificationView.html) o)`

`default void`
`[visitNodeView](#visitNodeView(com.nomagic.magicdraw.uml.symbols.shapes.NodeView))([NodeView](symbols/shapes/NodeView.html) o)`

`default void`
`[visitNoteAnchorView](#visitNoteAnchorView(com.nomagic.magicdraw.uml.symbols.paths.NoteAnchorView))([NoteAnchorView](symbols/paths/NoteAnchorView.html) o)`

`default void`
`[visitNoteHeaderView](#visitNoteHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.NoteHeaderView))(com.nomagic.magicdraw.uml.symbols.shapes.NoteHeaderView o)`

`default void`
`[visitNoteView](#visitNoteView(com.nomagic.magicdraw.uml.symbols.shapes.NoteView))([NoteView](symbols/shapes/NoteView.html) o)`

`default void`
`[visitObjectFlowView](#visitObjectFlowView(com.nomagic.magicdraw.uml.symbols.paths.ObjectFlowView))([ObjectFlowView](symbols/paths/ObjectFlowView.html) o)`

`default void`
`[visitObjectNodeView](#visitObjectNodeView(com.nomagic.magicdraw.uml.symbols.shapes.ObjectNodeView))([ObjectNodeView](symbols/shapes/ObjectNodeView.html) o)`

`default void`
`[visitObjectNodeViewHeaderView](#visitObjectNodeViewHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.ObjectNodeViewHeaderView))(com.nomagic.magicdraw.uml.symbols.shapes.ObjectNodeViewHeaderView objectNodeViewHeaderView)`

`default void`
`[visitOpaqueActionView](#visitOpaqueActionView(com.nomagic.magicdraw.uml.symbols.shapes.OpaqueActionView))([OpaqueActionView](symbols/shapes/OpaqueActionView.html) o)`

`default void`
`[visitOperationsCompartmentView](#visitOperationsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.OperationsCompartmentView))(com.nomagic.magicdraw.uml.symbols.shapes.OperationsCompartmentView o)`

`default void`
`[visitOperationTextArea](#visitOperationTextArea(com.nomagic.magicdraw.uml.symbols.shapes.OperationTextArea))(com.nomagic.magicdraw.uml.symbols.shapes.OperationTextArea operationTextArea)`

`default void`
`[visitOperationView](#visitOperationView(com.nomagic.magicdraw.uml.symbols.shapes.OperationView))(com.nomagic.magicdraw.uml.symbols.shapes.OperationView o)`

`default void`
`[visitPackageHeaderView](#visitPackageHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.PackageHeaderView))(com.nomagic.magicdraw.uml.symbols.shapes.PackageHeaderView o)`

`default void`
`[visitPackageImportView](#visitPackageImportView(com.nomagic.magicdraw.uml.symbols.paths.PackageImportView))([PackageImportView](symbols/paths/PackageImportView.html) o)`

`default void`
`[visitPackageMergeView](#visitPackageMergeView(com.nomagic.magicdraw.uml.symbols.paths.PackageMergeView))([PackageMergeView](symbols/paths/PackageMergeView.html) o)`

`default void`
`[visitPackageView](#visitPackageView(com.nomagic.magicdraw.uml.symbols.shapes.PackageView))([PackageView](symbols/shapes/PackageView.html) o)`

`default void`
`[visitPartHeaderView](#visitPartHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.PartHeaderView))(com.nomagic.magicdraw.uml.symbols.shapes.PartHeaderView o)`

`default void`
`[visitPartView](#visitPartView(com.nomagic.magicdraw.uml.symbols.shapes.PartView))([PartView](symbols/shapes/PartView.html) o)`

`default void`
`[visitPathConnector](#visitPathConnector(com.nomagic.magicdraw.uml.symbols.paths.PathConnector))([PathConnector](symbols/paths/PathConnector.html) o)`
Method visits given object.
`default void`
`[visitPathElement](#visitPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement))([PathElement](symbols/paths/PathElement.html) o)`
Method visits given object.
`default void`
`[visitPathToSelfShape](#visitPathToSelfShape(com.nomagic.magicdraw.uml.symbols.shapes.PathToSelfShape))(com.nomagic.magicdraw.uml.symbols.shapes.PathToSelfShape o)`

`default void`
`[visitPinView](#visitPinView(com.nomagic.magicdraw.uml.symbols.shapes.PinView))([PinView](symbols/shapes/PinView.html) o)`

`default void`
`[visitPortAttributeView](#visitPortAttributeView(com.nomagic.magicdraw.uml.symbols.shapes.PortAttributeView))(com.nomagic.magicdraw.uml.symbols.shapes.PortAttributeView o)`

`default void`
`[visitPortsCompartmentView](#visitPortsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.PortsCompartmentView))(com.nomagic.magicdraw.uml.symbols.shapes.PortsCompartmentView o)`

`default void`
`[visitPortView](#visitPortView(com.nomagic.magicdraw.uml.symbols.shapes.PortView))([PortView](symbols/shapes/PortView.html) o)`

`default void`
`[visitPresentationElement](#visitPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](symbols/PresentationElement.html) o)`
Method visits given object.
`default void`
`[visitPresentationElementContainer](#visitPresentationElementContainer(com.nomagic.magicdraw.uml.symbols.PresentationElementContainer))(com.nomagic.magicdraw.uml.symbols.PresentationElementContainer o)`

`default void`
`[visitPrimitiveTaggedValueView](#visitPrimitiveTaggedValueView(com.nomagic.magicdraw.uml.symbols.shapes.PrimitiveTaggedValueView))(com.nomagic.magicdraw.uml.symbols.shapes.PrimitiveTaggedValueView primitiveTaggedValueView)`

`default void`
`[visitPrimitiveTypeView](#visitPrimitiveTypeView(com.nomagic.magicdraw.uml.symbols.shapes.PrimitiveTypeView))([PrimitiveTypeView](symbols/shapes/PrimitiveTypeView.html) o)`

`default void`
`[visitPrimitiveValueView](#visitPrimitiveValueView(com.nomagic.magicdraw.uml.symbols.shapes.PrimitiveValueView))(com.nomagic.magicdraw.uml.symbols.shapes.PrimitiveValueView view)`

`default void`
`[visitProfileApplicationView](#visitProfileApplicationView(com.nomagic.magicdraw.uml.symbols.paths.ProfileApplicationView))([ProfileApplicationView](symbols/paths/ProfileApplicationView.html) o)`

`default void`
`[visitProjectOptions](#visitProjectOptions(com.nomagic.magicdraw.core.options.ProjectOptions))([ProjectOptions](../core/options/ProjectOptions.html) o)`

`default void`
`[visitPseudoNodeView](#visitPseudoNodeView(com.nomagic.magicdraw.uml.symbols.shapes.PseudoNodeView))([PseudoNodeView](symbols/shapes/PseudoNodeView.html) o)`

`default void`
`[visitPseudoStateView](#visitPseudoStateView(com.nomagic.magicdraw.uml.symbols.shapes.PseudoStateView))([PseudoStateView](symbols/shapes/PseudoStateView.html) o)`

`default void`
`[visitQualifiersView](#visitQualifiersView(com.nomagic.magicdraw.uml.symbols.shapes.QualifiersView))(com.nomagic.magicdraw.uml.symbols.shapes.QualifiersView o)`

`default void`
`[visitRealizationsCompartmentView](#visitRealizationsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.RealizationsCompartmentView))(com.nomagic.magicdraw.uml.symbols.shapes.RealizationsCompartmentView o)`

`default void`
`[visitRealizationView](#visitRealizationView(com.nomagic.magicdraw.uml.symbols.paths.RealizationView))([RealizationView](symbols/paths/RealizationView.html) o)`

`default void`
`[visitReceptionsCompartmentView](#visitReceptionsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.ReceptionsCompartmentView))(com.nomagic.magicdraw.uml.symbols.shapes.ReceptionsCompartmentView o)`

`default void`
`[visitReceptionView](#visitReceptionView(com.nomagic.magicdraw.uml.symbols.shapes.ReceptionView))(com.nomagic.magicdraw.uml.symbols.shapes.ReceptionView o)`

`default void`
`[visitRectangularShape](#visitRectangularShape(com.nomagic.magicdraw.uml.symbols.shapes.RectangularShape))([RectangularShape](symbols/shapes/RectangularShape.html) o)`

`default void`
`[visitRegionsCompartmentView](#visitRegionsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.RegionsCompartmentView))(com.nomagic.magicdraw.uml.symbols.shapes.RegionsCompartmentView o)`

`default void`
`[visitRegionView](#visitRegionView(com.nomagic.magicdraw.uml.symbols.shapes.RegionView))(com.nomagic.magicdraw.uml.symbols.shapes.RegionView o)`

`default void`
`[visitRequiredProvidedCompartmentView](#visitRequiredProvidedCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.RequiredProvidedInterfacesCompartmentView))(com.nomagic.magicdraw.uml.symbols.shapes.RequiredProvidedInterfacesCompartmentView o)`

`default void`
`[visitRoleBindingView](#visitRoleBindingView(com.nomagic.magicdraw.uml.symbols.paths.RoleBindingView))([RoleBindingView](symbols/paths/RoleBindingView.html) o)`

`default void`
`[visitRoleView](#visitRoleView(com.nomagic.magicdraw.uml.symbols.shapes.RoleView))(com.nomagic.magicdraw.uml.symbols.shapes.RoleView o)`

`default void`
`[visitSeparatorView](#visitSeparatorView(com.nomagic.magicdraw.uml.symbols.shapes.SeparatorView))([SeparatorView](symbols/shapes/SeparatorView.html) o)`

`default void`
`[visitSeqBaseMessageView](#visitSeqBaseMessageView(com.nomagic.magicdraw.uml.symbols.paths.SeqBaseMessageView))(com.nomagic.magicdraw.uml.symbols.paths.SeqBaseMessageView o)`

`default void`
`[visitSeqMessageView](#visitSeqMessageView(com.nomagic.magicdraw.uml.symbols.paths.SeqMessageView))([SeqMessageView](symbols/paths/SeqMessageView.html) o)`

`default void`
`[visitSeqSelfMessageView](#visitSeqSelfMessageView(com.nomagic.magicdraw.uml.symbols.paths.SeqSelfMessageView))([SeqSelfMessageView](symbols/paths/SeqSelfMessageView.html) o)`

`default void`
`[visitSequenceLifelineView](#visitSequenceLifelineView(com.nomagic.magicdraw.uml.symbols.shapes.SequenceLifelineView))([SequenceLifelineView](symbols/shapes/SequenceLifelineView.html) o)`

`default void`
`[visitSequenceNodeView](#visitSequenceNodeView(com.nomagic.magicdraw.uml.symbols.shapes.SequenceNodeView))([SequenceNodeView](symbols/shapes/SequenceNodeView.html) o)`

`default void`
`[visitSequenceObjectViewContainer](#visitSequenceObjectViewContainer(com.nomagic.magicdraw.uml.symbols.SequenceObjectViewContainer))(com.nomagic.magicdraw.uml.symbols.SequenceObjectViewContainer o)`

`default void`
`[visitSetupRegionView](#visitSetupRegionView(com.nomagic.magicdraw.uml.symbols.shapes.LoopNodeView.SetupRegionView))(com.nomagic.magicdraw.uml.symbols.shapes.LoopNodeView.SetupRegionView o)`

`default void`
`[visitShapeElement](#visitShapeElement(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement))([ShapeElement](symbols/shapes/ShapeElement.html) o)`
Method visits given object.
`default void`
`[visitShapeWithLabels](#visitShapeWithLabels(com.nomagic.magicdraw.uml.symbols.shapes.ShapeWithLabels))(com.nomagic.magicdraw.uml.symbols.shapes.ShapeWithLabels o)`

`default void`
`[visitSignalActionView](#visitSignalActionView(com.nomagic.magicdraw.uml.symbols.shapes.SignalActionView))([SignalActionView](symbols/shapes/SignalActionView.html) o)`

`default void`
`[visitSignalView](#visitSignalView(com.nomagic.magicdraw.uml.symbols.shapes.SignalView))([SignalView](symbols/shapes/SignalView.html) o)`

`default void`
`[visitSimpleActivityRegionView](#visitSimpleActivityRegionView(com.nomagic.magicdraw.uml.symbols.shapes.SimpleActivityRegionView))(com.nomagic.magicdraw.uml.symbols.shapes.SimpleActivityRegionView o)`

`default void`
`[visitSlotView](#visitSlotView(com.nomagic.magicdraw.uml.symbols.shapes.SlotView))(com.nomagic.magicdraw.uml.symbols.shapes.SlotView o)`

`default void`
`[visitSplitView](#visitSplitView(com.nomagic.magicdraw.uml.symbols.shapes.SplitView))(com.nomagic.magicdraw.uml.symbols.shapes.SplitView o)`

`default void`
`[visitStateHeaderView](#visitStateHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.StateHeaderView))(com.nomagic.magicdraw.uml.symbols.shapes.StateHeaderView o)`

`default void`
`[visitStateInvariantHeaderView](#visitStateInvariantHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.StateInvariantHeaderView))(com.nomagic.magicdraw.uml.symbols.shapes.StateInvariantHeaderView o)`

`default void`
`[visitStateInvariantView](#visitStateInvariantView(com.nomagic.magicdraw.uml.symbols.shapes.StateInvariantView))([StateInvariantView](symbols/shapes/StateInvariantView.html) o)`

`default void`
`[visitStateObjectViewContainer](#visitStateObjectViewContainer(com.nomagic.magicdraw.uml.symbols.StateObjectViewContainer))(com.nomagic.magicdraw.uml.symbols.StateObjectViewContainer o)`

`default void`
`[visitStateView](#visitStateView(com.nomagic.magicdraw.uml.symbols.shapes.StateView))([StateView](symbols/shapes/StateView.html) o)`

`default void`
`[visitStereotypeHeaderView](#visitStereotypeHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.StereotypeHeaderView))(com.nomagic.magicdraw.uml.symbols.shapes.StereotypeHeaderView o)`

`default void`
`[visitStereotypeIconView](#visitStereotypeIconView(com.nomagic.magicdraw.uml.symbols.shapes.StereotypeIconView))(com.nomagic.magicdraw.uml.symbols.shapes.StereotypeIconView o)`

`default void`
`[visitStereotypesView](#visitStereotypesView(com.nomagic.magicdraw.uml.symbols.shapes.StereotypesView))(com.nomagic.magicdraw.uml.symbols.shapes.StereotypesView o)`

`default void`
`[visitStereotypeView](#visitStereotypeView(com.nomagic.magicdraw.uml.symbols.shapes.StereotypeView))([StereotypeView](symbols/shapes/StereotypeView.html) o)`

`default void`
`[visitStructureCompartmentView](#visitStructureCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.StructureCompartmentView))(com.nomagic.magicdraw.uml.symbols.shapes.StructureCompartmentView o)`

`default void`
`[visitStructuredActivityNodeView](#visitStructuredActivityNodeView(com.nomagic.magicdraw.uml.symbols.shapes.StructuredActivityNodeView))([StructuredActivityNodeView](symbols/shapes/StructuredActivityNodeView.html) o)`

`default void`
`[visitSwimlaneCellView](#visitSwimlaneCellView(com.nomagic.magicdraw.uml.symbols.shapes.SwimlaneCellView))([SwimlaneCellView](symbols/shapes/SwimlaneCellView.html) o)`

`default void`
`[visitSwimlaneHeaderView](#visitSwimlaneHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.SwimlaneHeaderView))(com.nomagic.magicdraw.uml.symbols.shapes.SwimlaneHeaderView o)`

`default void`
`[visitSwimlaneView](#visitSwimlaneView(com.nomagic.magicdraw.uml.symbols.shapes.SwimlaneView))([SwimlaneView](symbols/shapes/SwimlaneView.html) o)`

`default void`
`[visitTableCellView](#visitTableCellView(com.nomagic.magicdraw.uml.symbols.shapes.TableCellView))(com.nomagic.magicdraw.uml.symbols.shapes.TableCellView o)`

`default void`
`[visitTableShapeView](#visitTableShapeView(com.nomagic.magicdraw.uml.symbols.shapes.TableShapeView))(com.nomagic.magicdraw.uml.symbols.shapes.TableShapeView o)`

`default void`
`[visitTaggedValuesCompartmentView](#visitTaggedValuesCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.TaggedValuesCompartmentView))(com.nomagic.magicdraw.uml.symbols.shapes.TaggedValuesCompartmentView o)`

`default void`
`[visitTaggedValuesView](#visitTaggedValuesView(com.nomagic.magicdraw.uml.symbols.shapes.TaggedValuesView))(com.nomagic.magicdraw.uml.symbols.shapes.TaggedValuesView o)`

`default void`
`[visitTemplateBindingView](#visitTemplateBindingView(com.nomagic.magicdraw.uml.symbols.paths.TemplateBindingView))([TemplateBindingView](symbols/paths/TemplateBindingView.html) o)`

`default void`
`[visitTemplateSignatureView](#visitTemplateSignatureView(com.nomagic.magicdraw.uml.symbols.shapes.TemplateSignatureView))(com.nomagic.magicdraw.uml.symbols.shapes.TemplateSignatureView o)`

`default void`
`[visitTestRegionView](#visitTestRegionView(com.nomagic.magicdraw.uml.symbols.shapes.ClauseView.TestRegionView))(com.nomagic.magicdraw.uml.symbols.shapes.ClauseView.TestRegionView o)`

`default void`
`[visitTestRegionView](#visitTestRegionView(com.nomagic.magicdraw.uml.symbols.shapes.LoopNodeView.TestRegionView))(com.nomagic.magicdraw.uml.symbols.shapes.LoopNodeView.TestRegionView o)`

`default void`
`[visitTextAreaCompartmentView](#visitTextAreaCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.TextAreaCompartmentView))(com.nomagic.magicdraw.uml.symbols.shapes.TextAreaCompartmentView o)`

`default void`
`[visitTextAreaView](#visitTextAreaView(com.nomagic.magicdraw.uml.symbols.shapes.TextAreaView))(com.nomagic.magicdraw.uml.symbols.shapes.TextAreaView o)`

`default void`
`[visitTextBoxView](#visitTextBoxView(com.nomagic.magicdraw.uml.symbols.shapes.TextBoxView))([TextBoxView](symbols/shapes/TextBoxView.html) o)`

`default void`
`[visitTextBoxWithIconView](#visitTextBoxWithIconView(com.nomagic.magicdraw.uml.symbols.shapes.TextBoxWithIconView))(com.nomagic.magicdraw.uml.symbols.shapes.TextBoxWithIconView o)`

`default void`
`[visitTextObject](#visitTextObject(com.nomagic.magicdraw.uml.symbols.shapes.TextObject))(com.nomagic.magicdraw.uml.symbols.shapes.TextObject o)`

`default void`
`[visitTextShapeView](#visitTextShapeView(com.nomagic.magicdraw.uml.symbols.shapes.TextShapeView))(com.nomagic.magicdraw.uml.symbols.shapes.TextShapeView o)`

`default void`
`[visitTextView](#visitTextView(com.nomagic.magicdraw.uml.symbols.shapes.TextView))(com.nomagic.magicdraw.uml.symbols.shapes.TextView o)`

`default void`
`[visitTimeConstraintView](#visitTimeConstraintView(com.nomagic.magicdraw.uml.symbols.paths.TimeConstraintView))([TimeConstraintView](symbols/paths/TimeConstraintView.html) o)`

`default void`
`[visitTransitionLabelView](#visitTransitionLabelView(com.nomagic.magicdraw.uml.symbols.shapes.TransitionLabelView))(com.nomagic.magicdraw.uml.symbols.shapes.TransitionLabelView transitionLabelView)`

`default void`
`[visitTransitionToSelfView](#visitTransitionToSelfView(com.nomagic.magicdraw.uml.symbols.shapes.TransitionToSelfView))([TransitionToSelfView](symbols/shapes/TransitionToSelfView.html) o)`

`default void`
`[visitTransitionView](#visitTransitionView(com.nomagic.magicdraw.uml.symbols.paths.TransitionView))([TransitionView](symbols/paths/TransitionView.html) o)`

`default void`
`[visitTreeView](#visitTreeView(com.nomagic.magicdraw.uml.symbols.shapes.TreeView))([TreeView](symbols/shapes/TreeView.html) o)`

`default void`
`[visitTriggerLabelView](#visitTriggerLabelView(com.nomagic.magicdraw.uml.symbols.shapes.TriggerLabelView))(com.nomagic.magicdraw.uml.symbols.shapes.TriggerLabelView triggerLabelView)`

`default void`
`[visitTypedElementHeaderView](#visitTypedElementHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.TypedElementHeaderView))(com.nomagic.magicdraw.uml.symbols.shapes.TypedElementHeaderView o)`

`default void`
`[visitTypedElementView](#visitTypedElementView(com.nomagic.magicdraw.uml.symbols.shapes.TypedElementView))(com.nomagic.magicdraw.uml.symbols.shapes.TypedElementView o)`

`default void`
`[visitTypedElementWithLabels](#visitTypedElementWithLabels(com.nomagic.magicdraw.uml.symbols.shapes.TypedElementWithLabels))(com.nomagic.magicdraw.uml.symbols.shapes.TypedElementWithLabels o)`

`default void`
`[visitUsageView](#visitUsageView(com.nomagic.magicdraw.uml.symbols.paths.UsageView))([UsageView](symbols/paths/UsageView.html) o)`

`default void`
`[visitUseCaseView](#visitUseCaseView(com.nomagic.magicdraw.uml.symbols.shapes.UseCaseView))([UseCaseView](symbols/shapes/UseCaseView.html) o)`

`default void`
`[visitVirtualRelation](#visitVirtualRelation(com.nomagic.magicdraw.uml.symbols.paths.VirtualRelationView))([VirtualRelationView](symbols/paths/VirtualRelationView.html) o)`

============ METHOD DETAIL ========== 
Method Details
visitDiagramPresentationElement
@OpenApidefault void visitDiagramPresentationElement([DiagramPresentationElement](symbols/DiagramPresentationElement.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Method visits given object.
Parameters:
`o` - object to visit.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitAbstractDiagramPresentationElement
@OpenApidefault void visitAbstractDiagramPresentationElement([AbstractDiagramPresentationElement](symbols/AbstractDiagramPresentationElement.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Method visits given object.
Parameters:
`o` - object to visit.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitPresentationElement
@OpenApidefault void visitPresentationElement([PresentationElement](symbols/PresentationElement.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Method visits given object.
Parameters:
`o` - object to visit.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitCollaborationView
default void visitCollaborationView([CollaborationView](symbols/shapes/CollaborationView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitObjectNodeView
default void visitObjectNodeView([ObjectNodeView](symbols/shapes/ObjectNodeView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitAbstractHeaderShapeView
default void visitAbstractHeaderShapeView(com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitBaseHeaderShapeView
default void visitBaseHeaderShapeView(com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitHeaderShapeView
default void visitHeaderShapeView(com.nomagic.magicdraw.uml.symbols.shapes.HeaderShapeView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitBaseHeaderView
default void visitBaseHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitNodeInstanceSpecificationView
default void visitNodeInstanceSpecificationView([NodeInstanceSpecificationView](symbols/shapes/NodeInstanceSpecificationView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitLinkWithStereotype
default void visitLinkWithStereotype(com.nomagic.magicdraw.uml.symbols.paths.LinkWithStereotype o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitSplitView
default void visitSplitView(com.nomagic.magicdraw.uml.symbols.shapes.SplitView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitLifelineView
default void visitLifelineView([LifelineView](symbols/shapes/LifelineView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitTypedElementView
default void visitTypedElementView(com.nomagic.magicdraw.uml.symbols.shapes.TypedElementView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitRegionView
default void visitRegionView(com.nomagic.magicdraw.uml.symbols.shapes.RegionView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitSimpleActivityRegionView
default void visitSimpleActivityRegionView(com.nomagic.magicdraw.uml.symbols.shapes.SimpleActivityRegionView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitTestRegionView
default void visitTestRegionView(com.nomagic.magicdraw.uml.symbols.shapes.LoopNodeView.TestRegionView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitBodyRegionView
default void visitBodyRegionView(com.nomagic.magicdraw.uml.symbols.shapes.LoopNodeView.BodyRegionView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitSetupRegionView
default void visitSetupRegionView(com.nomagic.magicdraw.uml.symbols.shapes.LoopNodeView.SetupRegionView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitTestRegionView
default void visitTestRegionView(com.nomagic.magicdraw.uml.symbols.shapes.ClauseView.TestRegionView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitBodyRegionView
default void visitBodyRegionView(com.nomagic.magicdraw.uml.symbols.shapes.ClauseView.BodyRegionView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitElseRegionView
default void visitElseRegionView(com.nomagic.magicdraw.uml.symbols.shapes.ClauseView.ElseRegionView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitClauseView
default void visitClauseView(com.nomagic.magicdraw.uml.symbols.shapes.ClauseView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitTemplateBindingView
default void visitTemplateBindingView([TemplateBindingView](symbols/paths/TemplateBindingView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitBaseMembersCompartmentView
default void visitBaseMembersCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.BaseMembersCompartmentView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitBaseCompartmentView
default void visitBaseCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.BaseCompartmentView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitAbstractBaseCompartmentView
default void visitAbstractBaseCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.AbstractCompartmentView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitAbstractSeparatorView
default void visitAbstractSeparatorView(com.nomagic.magicdraw.uml.symbols.shapes.AbstractSeparatorView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitSeparatorView
default void visitSeparatorView([SeparatorView](symbols/shapes/SeparatorView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitRectangularShape
default void visitRectangularShape([RectangularShape](symbols/shapes/RectangularShape.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitListElementView
default void visitListElementView(com.nomagic.magicdraw.uml.symbols.shapes.ListElementView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitLegendItemView
default void visitLegendItemView(com.nomagic.magicdraw.uml.symbols.shapes.LegendItemView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitElementWithIconView
default void visitElementWithIconView(com.nomagic.magicdraw.uml.symbols.shapes.ElementWithIconView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitImageView
default void visitImageView(com.nomagic.magicdraw.uml.symbols.shapes.ImageView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitInnerElementsCompartmentView
default void visitInnerElementsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.InnerElementsCompartmentView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitConstraintsView
default void visitConstraintsView(com.nomagic.magicdraw.uml.symbols.shapes.ConstraintsView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitStereotypesView
default void visitStereotypesView(com.nomagic.magicdraw.uml.symbols.shapes.StereotypesView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitElementPropertiesCompartmentView
default void visitElementPropertiesCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.ElementPropertiesCompartmentView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitConveyedInformationView
default void visitConveyedInformationView(com.nomagic.magicdraw.uml.symbols.shapes.ConveyedInformationView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitTaggedValuesView
default void visitTaggedValuesView(com.nomagic.magicdraw.uml.symbols.shapes.TaggedValuesView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitExtensionPointView
default void visitExtensionPointView(com.nomagic.magicdraw.uml.symbols.shapes.ExtensionPointView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitTextAreaCompartmentView
default void visitTextAreaCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.TextAreaCompartmentView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitRequiredProvidedCompartmentView
default void visitRequiredProvidedCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.RequiredProvidedInterfacesCompartmentView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitProjectOptions
default void visitProjectOptions([ProjectOptions](../core/options/ProjectOptions.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitPresentationElementContainer
default void visitPresentationElementContainer(com.nomagic.magicdraw.uml.symbols.PresentationElementContainer o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitAbstractDiagramPresentationElementContainer
default void visitAbstractDiagramPresentationElementContainer(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElementContainer o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitDiagramObjectViewContainer
default void visitDiagramObjectViewContainer(com.nomagic.magicdraw.uml.symbols.DiagramObjectViewContainer o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitDummyDiagramObjectViewContainer
default void visitDummyDiagramObjectViewContainer(com.nomagic.magicdraw.uml.symbols.DummyDiagramObjectViewContainer o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitAssociationView
default void visitAssociationView([AssociationView](symbols/paths/AssociationView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitCommunicationPathView
default void visitCommunicationPathView([CommunicationPathView](symbols/paths/CommunicationPathView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitAssociationClassView
default void visitAssociationClassView([AssociationClassView](symbols/paths/AssociationClassView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitConstraintLinkView
default void visitConstraintLinkView([ConstraintLinkView](symbols/paths/ConstraintLinkView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitConnectorToSelfView
default void visitConnectorToSelfView([ConnectorToSelfView](symbols/paths/ConnectorToSelfView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitLinkView
default void visitLinkView([LinkView](symbols/paths/LinkView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitContainerLinkView
default void visitContainerLinkView(com.nomagic.magicdraw.uml.symbols.paths.ContainerLinkView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitDependencyView
default void visitDependencyView([DependencyView](symbols/paths/DependencyView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitRoleBindingView
default void visitRoleBindingView([RoleBindingView](symbols/paths/RoleBindingView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitUsageView
default void visitUsageView([UsageView](symbols/paths/UsageView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitDeploymentView
default void visitDeploymentView([DeploymentView](symbols/paths/DeploymentView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitConnectorView
default void visitConnectorView([ConnectorView](symbols/paths/ConnectorView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitPackageImportView
default void visitPackageImportView([PackageImportView](symbols/paths/PackageImportView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitProfileApplicationView
default void visitProfileApplicationView([ProfileApplicationView](symbols/paths/ProfileApplicationView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitElementImportView
default void visitElementImportView([ElementImportView](symbols/paths/ElementImportView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitPackageMergeView
default void visitPackageMergeView([PackageMergeView](symbols/paths/PackageMergeView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitExtendView
default void visitExtendView([ExtendView](symbols/paths/ExtendView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitIncludeView
default void visitIncludeView([IncludeView](symbols/paths/IncludeView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitGeneralizationView
default void visitGeneralizationView([GeneralizationView](symbols/paths/GeneralizationView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitLinkAttributeView
default void visitLinkAttributeView([LinkAttributeView](symbols/paths/LinkAttributeView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitPathConnector
@OpenApidefault void visitPathConnector([PathConnector](symbols/paths/PathConnector.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Method visits given object.
Parameters:
`o` - object to visit.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitPathElement
@OpenApidefault void visitPathElement([PathElement](symbols/paths/PathElement.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Method visits given object.
Parameters:
`o` - object to visit.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitNoteAnchorView
default void visitNoteAnchorView([NoteAnchorView](symbols/paths/NoteAnchorView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitContainmentLinkView
default void visitContainmentLinkView([ContainmentLinkView](symbols/paths/ContainmentLinkView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitVirtualRelation
default void visitVirtualRelation([VirtualRelationView](symbols/paths/VirtualRelationView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitGenericView
default void visitGenericView([GenericView](symbols/shapes/GenericView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitBaseRealizationView
default void visitBaseRealizationView(com.nomagic.magicdraw.uml.symbols.paths.BaseRealizationView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitInterfaceRealizationView
default void visitInterfaceRealizationView([InterfaceRealizationView](symbols/paths/InterfaceRealizationView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitSeqMessageView
default void visitSeqMessageView([SeqMessageView](symbols/paths/SeqMessageView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitSeqSelfMessageView
default void visitSeqSelfMessageView([SeqSelfMessageView](symbols/paths/SeqSelfMessageView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitTransitionView
default void visitTransitionView([TransitionView](symbols/paths/TransitionView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitExceptionHandlerView
default void visitExceptionHandlerView([ExceptionHandlerView](symbols/paths/ExceptionHandlerView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitTransitionToSelfView
default void visitTransitionToSelfView([TransitionToSelfView](symbols/shapes/TransitionToSelfView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitTimeConstraintView
default void visitTimeConstraintView([TimeConstraintView](symbols/paths/TimeConstraintView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitDurationConstraintView
default void visitDurationConstraintView([DurationConstraintView](symbols/paths/DurationConstraintView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitPathToSelfShape
default void visitPathToSelfShape(com.nomagic.magicdraw.uml.symbols.shapes.PathToSelfShape o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitActivationView
default void visitActivationView([ActivationView](symbols/shapes/ActivationView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitBarView
default void visitBarView([BarView](symbols/shapes/BarView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitAttributeView
default void visitAttributeView(com.nomagic.magicdraw.uml.symbols.shapes.AttributeView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitPortAttributeView
default void visitPortAttributeView(com.nomagic.magicdraw.uml.symbols.shapes.PortAttributeView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitMemberView
default void visitMemberView(com.nomagic.magicdraw.uml.symbols.shapes.MemberView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitBehavioralFeatureView
default void visitBehavioralFeatureView(com.nomagic.magicdraw.uml.symbols.shapes.BehavioralFeatureView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitClassView
default void visitClassView([ClassView](symbols/shapes/ClassView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitInterfaceView
default void visitInterfaceView([InterfaceView](symbols/shapes/InterfaceView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitSignalView
default void visitSignalView([SignalView](symbols/shapes/SignalView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitActorView
default void visitActorView([ActorView](symbols/shapes/ActorView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitDataTypeView
default void visitDataTypeView([DataTypeView](symbols/shapes/DataTypeView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitPrimitiveTypeView
default void visitPrimitiveTypeView([PrimitiveTypeView](symbols/shapes/PrimitiveTypeView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitStereotypeView
default void visitStereotypeView([StereotypeView](symbols/shapes/StereotypeView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitClassifierView
default void visitClassifierView([ClassifierView](symbols/shapes/ClassifierView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitClassifierHeaderView
default void visitClassifierHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.ClassifierHeaderView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitEnumerationView
default void visitEnumerationView([EnumerationView](symbols/shapes/EnumerationView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitArtifactView
default void visitArtifactView([ArtifactView](symbols/shapes/ArtifactView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitInstanceSpecificationView
default void visitInstanceSpecificationView([InstanceSpecificationView](symbols/shapes/InstanceSpecificationView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitContainerShapeView
default void visitContainerShapeView(com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitDecisionView
default void visitDecisionView([DecisionView](symbols/shapes/DecisionView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitBaseTreeShape
default void visitBaseTreeShape(com.nomagic.magicdraw.uml.symbols.shapes.BaseTreeShape o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitTreeView
default void visitTreeView([TreeView](symbols/shapes/TreeView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitLifeLineLineView
default void visitLifeLineLineView([LifeLineLineView](symbols/shapes/LifeLineLineView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitMessageView
default void visitMessageView([MessageView](symbols/shapes/MessageView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitOperationView
default void visitOperationView(com.nomagic.magicdraw.uml.symbols.shapes.OperationView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitReceptionView
default void visitReceptionView(com.nomagic.magicdraw.uml.symbols.shapes.ReceptionView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitReceptionsCompartmentView
default void visitReceptionsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.ReceptionsCompartmentView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitNoteView
default void visitNoteView([NoteView](symbols/shapes/NoteView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitMessageSignatureView
default void visitMessageSignatureView(com.nomagic.magicdraw.uml.symbols.shapes.MessageSignatureView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitPackageView
default void visitPackageView([PackageView](symbols/shapes/PackageView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitRoleView
default void visitRoleView(com.nomagic.magicdraw.uml.symbols.shapes.RoleView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitAbstractPathEndShape
default void visitAbstractPathEndShape(com.nomagic.magicdraw.uml.symbols.shapes.AbstractPathEndShape o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitLinkEndView
default void visitLinkEndView(com.nomagic.magicdraw.uml.symbols.shapes.LinkEndView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitConnectorEndView
default void visitConnectorEndView(com.nomagic.magicdraw.uml.symbols.shapes.ConnectorEndView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitNNaryAssociationView
default void visitNNaryAssociationView([NNaryAssociationView](symbols/shapes/NNaryAssociationView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitSequenceLifelineView
default void visitSequenceLifelineView([SequenceLifelineView](symbols/shapes/SequenceLifelineView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitShapeElement
@OpenApidefault void visitShapeElement([ShapeElement](symbols/shapes/ShapeElement.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Method visits given object.
Parameters:
`o` - object to visit.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitQualifiersView
default void visitQualifiersView(com.nomagic.magicdraw.uml.symbols.shapes.QualifiersView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitTextAreaView
default void visitTextAreaView(com.nomagic.magicdraw.uml.symbols.shapes.TextAreaView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitAbstractTextBoxView
default void visitAbstractTextBoxView(com.nomagic.magicdraw.uml.symbols.shapes.AbstractTextBoxView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitTextBoxView
default void visitTextBoxView([TextBoxView](symbols/shapes/TextBoxView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitTextBoxWithIconView
default void visitTextBoxWithIconView(com.nomagic.magicdraw.uml.symbols.shapes.TextBoxWithIconView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitTextObject
default void visitTextObject(com.nomagic.magicdraw.uml.symbols.shapes.TextObject o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitTextShapeView
default void visitTextShapeView(com.nomagic.magicdraw.uml.symbols.shapes.TextShapeView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitTextView
default void visitTextView(com.nomagic.magicdraw.uml.symbols.shapes.TextView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitUseCaseView
default void visitUseCaseView([UseCaseView](symbols/shapes/UseCaseView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitSeqBaseMessageView
default void visitSeqBaseMessageView(com.nomagic.magicdraw.uml.symbols.paths.SeqBaseMessageView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitSequenceObjectViewContainer
default void visitSequenceObjectViewContainer(com.nomagic.magicdraw.uml.symbols.SequenceObjectViewContainer o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitPseudoStateView
default void visitPseudoStateView([PseudoStateView](symbols/shapes/PseudoStateView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitPseudoNodeView
default void visitPseudoNodeView([PseudoNodeView](symbols/shapes/PseudoNodeView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitStateView
default void visitStateView([StateView](symbols/shapes/StateView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitStateObjectViewContainer
default void visitStateObjectViewContainer(com.nomagic.magicdraw.uml.symbols.StateObjectViewContainer o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitActivityObjectViewContainer
default void visitActivityObjectViewContainer(com.nomagic.magicdraw.uml.symbols.ActivityObjectViewContainer o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitComponentView
default void visitComponentView([ComponentView](symbols/shapes/ComponentView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitNodeView
default void visitNodeView([NodeView](symbols/shapes/NodeView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitRealizationView
default void visitRealizationView([RealizationView](symbols/paths/RealizationView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitStereotypeIconView
default void visitStereotypeIconView(com.nomagic.magicdraw.uml.symbols.shapes.StereotypeIconView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitTemplateSignatureView
default void visitTemplateSignatureView(com.nomagic.magicdraw.uml.symbols.shapes.TemplateSignatureView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitHeaderOfBaseHeaderShapeView
default void visitHeaderOfBaseHeaderShapeView(com.nomagic.magicdraw.uml.symbols.shapes.HeaderOfBaseHeaderShapeView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitHeaderView
default void visitHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.HeaderView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitEnumerationHeaderView
default void visitEnumerationHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.EnumerationHeaderView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitComponentHeaderView
default void visitComponentHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.ComponentHeaderView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitNodeHeaderView
default void visitNodeHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.NodeHeaderView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitEnumerationLiteralView
default void visitEnumerationLiteralView(com.nomagic.magicdraw.uml.symbols.shapes.EnumerationLiteralView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitBehaviorView
default void visitBehaviorView(com.nomagic.magicdraw.uml.symbols.shapes.BehaviorView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitEnumerationLiteralsCompartmentView
default void visitEnumerationLiteralsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.EnumerationLiteralsCompartmentView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitBehaviorsCompartmentView
default void visitBehaviorsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.BehaviorsCompartmentView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitAttributesCompartmentView
default void visitAttributesCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.AttributesCompartmentView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitPortsCompartmentView
default void visitPortsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.PortsCompartmentView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitBasePropertiesCompartmentView
default void visitBasePropertiesCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.BasePropertiesCompartmentView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitStructureCompartmentView
default void visitStructureCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.StructureCompartmentView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitDiagramOverviewCompartmentView
default void visitDiagramOverviewCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.DiagramOverviewCompartmentView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitOperationsCompartmentView
default void visitOperationsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.OperationsCompartmentView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitAssociationTextBoxView
default void visitAssociationTextBoxView(com.nomagic.magicdraw.uml.symbols.shapes.AssociationTextBoxView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitSignalActionView
default void visitSignalActionView([SignalActionView](symbols/shapes/SignalActionView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitSlotView
default void visitSlotView(com.nomagic.magicdraw.uml.symbols.shapes.SlotView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitPrimitiveValueView
default void visitPrimitiveValueView(com.nomagic.magicdraw.uml.symbols.shapes.PrimitiveValueView view)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitCommentView
default void visitCommentView([CommentView](symbols/shapes/CommentView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitCompartmentElement
default void visitCompartmentElement([CompartmentElement](CompartmentElement.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Method visitCompartmentElement.
Parameters:
`o` -
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitContentShape
default void visitContentShape([ContentShape](symbols/shapes/ContentShape.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitDiagramShape
default void visitDiagramShape([DiagramShape](symbols/shapes/DiagramShape.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitDiagramPropertiesShape
default void visitDiagramPropertiesShape([DiagramPropertiesShape](symbols/shapes/DiagramPropertiesShape.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitDiagramLegendShape
default void visitDiagramLegendShape([DiagramLegendShape](symbols/shapes/DiagramLegendShape.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitAbstractShapeWithLabelsInside
default void visitAbstractShapeWithLabelsInside(com.nomagic.magicdraw.uml.symbols.shapes.AbstractShapeWithLabelsInside o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitTypedElementWithLabels
default void visitTypedElementWithLabels(com.nomagic.magicdraw.uml.symbols.shapes.TypedElementWithLabels o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitPortView
default void visitPortView([PortView](symbols/shapes/PortView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitPinView
default void visitPinView([PinView](symbols/shapes/PinView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitExpansionNodeView
default void visitExpansionNodeView([ExpansionNodeView](symbols/shapes/ExpansionNodeView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitAbstractShapeWithLabels
default void visitAbstractShapeWithLabels(com.nomagic.magicdraw.uml.symbols.shapes.AbstractShapeWithLabels o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitShapeWithLabels
default void visitShapeWithLabels(com.nomagic.magicdraw.uml.symbols.shapes.ShapeWithLabels o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitFlowConnectorView
default void visitFlowConnectorView([FlowConnectorView](symbols/shapes/FlowConnectorView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitSwimlaneCellView
default void visitSwimlaneCellView([SwimlaneCellView](symbols/shapes/SwimlaneCellView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitSwimlaneView
default void visitSwimlaneView([SwimlaneView](symbols/shapes/SwimlaneView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitTableShapeView
default void visitTableShapeView(com.nomagic.magicdraw.uml.symbols.shapes.TableShapeView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitTableCellView
default void visitTableCellView(com.nomagic.magicdraw.uml.symbols.shapes.TableCellView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitSwimlaneHeaderView
default void visitSwimlaneHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.SwimlaneHeaderView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitInteractionUseView
default void visitInteractionUseView([InteractionUseView](symbols/shapes/InteractionUseView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitFragmentView
default void visitFragmentView(com.nomagic.magicdraw.uml.symbols.shapes.FragmentView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitStateInvariantView
default void visitStateInvariantView([StateInvariantView](symbols/shapes/StateInvariantView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitStateInvariantHeaderView
default void visitStateInvariantHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.StateInvariantHeaderView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitFrameView
default void visitFrameView(com.nomagic.magicdraw.uml.symbols.shapes.FrameView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitCombinedFragmentView
default void visitCombinedFragmentView([CombinedFragmentView](symbols/shapes/CombinedFragmentView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitInteractionOperandView
default void visitInteractionOperandView(com.nomagic.magicdraw.uml.symbols.shapes.InteractionOperandView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitActionView
default void visitActionView([ActionView](symbols/shapes/ActionView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitStructuredActivityNodeView
default void visitStructuredActivityNodeView([StructuredActivityNodeView](symbols/shapes/StructuredActivityNodeView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitActivityGroupView
default void visitActivityGroupView(com.nomagic.magicdraw.uml.symbols.shapes.ActivityGroupView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitInterruptibleActivityRegionView
default void visitInterruptibleActivityRegionView([InterruptibleActivityRegionView](symbols/shapes/InterruptibleActivityRegionView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitSequenceNodeView
default void visitSequenceNodeView([SequenceNodeView](symbols/shapes/SequenceNodeView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitConditionalNodeView
default void visitConditionalNodeView([ConditionalNodeView](symbols/shapes/ConditionalNodeView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitLoopNodeView
default void visitLoopNodeView([LoopNodeView](symbols/shapes/LoopNodeView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitExpansionRegionView
default void visitExpansionRegionView([ExpansionRegionView](symbols/shapes/ExpansionRegionView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitCallBehaviorActionView
default void visitCallBehaviorActionView([CallBehaviorActionView](symbols/shapes/CallBehaviorActionView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitInteractionUseOverviewView
default void visitInteractionUseOverviewView([InteractionUseOverviewView](symbols/shapes/InteractionUseOverviewView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitOpaqueActionView
default void visitOpaqueActionView([OpaqueActionView](symbols/shapes/OpaqueActionView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitCallOperationActionView
default void visitCallOperationActionView([CallOperationActionView](symbols/shapes/CallOperationActionView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitObjectFlowView
default void visitObjectFlowView([ObjectFlowView](symbols/paths/ObjectFlowView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitControlFlowView
default void visitControlFlowView([ControlFlowView](symbols/paths/ControlFlowView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitBaseFlowView
default void visitBaseFlowView(com.nomagic.magicdraw.uml.symbols.paths.BaseFlowView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitExtensionView
default void visitExtensionView([ExtensionView](symbols/paths/ExtensionView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitBaseLifelineView
default void visitBaseLifelineView(com.nomagic.magicdraw.uml.symbols.shapes.BaseLifelineView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitLinkWithRolesView
default void visitLinkWithRolesView(com.nomagic.magicdraw.uml.symbols.paths.LinkWithRolesView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitLinkWithEndsView
default void visitLinkWithEndsView(com.nomagic.magicdraw.uml.symbols.paths.LinkWithEndsView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitPartView
default void visitPartView([PartView](symbols/shapes/PartView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitCollaborationUseView
default void visitCollaborationUseView([CollaborationUseView](symbols/shapes/CollaborationUseView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitInteractionOperandsCompartmentView
default void visitInteractionOperandsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.InteractionOperandsCompartmentView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitRegionsCompartmentView
default void visitRegionsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.RegionsCompartmentView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitClauseCompartmentView
default void visitClauseCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.ClauseCompartmentView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitBaseSplitCompartmentView
default void visitBaseSplitCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.BaseSplitCompartmentView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitClassHeaderView
default void visitClassHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.ClassHeaderView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitInterfaceHeaderView
default void visitInterfaceHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.InterfaceHeaderView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitInformationItemHeaderView
default void visitInformationItemHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.InformationItemHeaderView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitExtensionPointsCompartmentView
default void visitExtensionPointsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.ExtensionPointsCompartmentView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitInterfacesCompartmentView
default void visitInterfacesCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.InterfacesCompartmentView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitRealizationsCompartmentView
default void visitRealizationsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.RealizationsCompartmentView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitInternalStateCompartmentView
default void visitInternalStateCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.InternalStateCompartmentView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitInstanceSlotsCompartmentView
default void visitInstanceSlotsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.InstanceSlotsCompartmentView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitDeployedElementsCompartmentView
default void visitDeployedElementsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.DeployedElementsCompartmentView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitCustomCompartmentView
default void visitCustomCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.CustomCompartmentView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitArtifactsCompartmentView
default void visitArtifactsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.ArtifactsCompartmentView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitConstraintsCompartmentView
default void visitConstraintsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.ConstraintsCompartmentView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitLegendItemsCompartmentView
default void visitLegendItemsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.LegendItemsCompartmentView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitTaggedValuesCompartmentView
default void visitTaggedValuesCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.TaggedValuesCompartmentView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitCombinedFragmentHeaderView
default void visitCombinedFragmentHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.CombinedFragmentHeaderView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitFrameHeaderView
default void visitFrameHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.FrameHeaderView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitActionHeaderView
default void visitActionHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.ActionHeaderView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitStateHeaderView
default void visitStateHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.StateHeaderView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitBaseElementTextField
default void visitBaseElementTextField(com.nomagic.magicdraw.uml.symbols.shapes.BaseElementTextField o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitBaseElementTextArea
default void visitBaseElementTextArea(com.nomagic.magicdraw.uml.symbols.shapes.BaseElementTextArea o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitElementCompartmentView
default void visitElementCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.ElementCompartmentView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitCustomElementCompartmentView
default void visitCustomElementCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.CustomElementCompartmentView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitConstraintCompartmentView
default void visitConstraintCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.ConstraintCompartmentView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitDirectionIconView
default void visitDirectionIconView(com.nomagic.magicdraw.uml.symbols.shapes.DirectionIconView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitCollaborationHeaderView
default void visitCollaborationHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.CollaborationHeaderView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitStereotypeHeaderView
default void visitStereotypeHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.StereotypeHeaderView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitPackageHeaderView
default void visitPackageHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.PackageHeaderView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitNoteHeaderView
default void visitNoteHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.NoteHeaderView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitBaseNameHeaderView
default void visitBaseNameHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.BaseNameHeaderView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitInstanceSpecificationHeaderView
default void visitInstanceSpecificationHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.InstanceSpecificationHeaderView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitNodeInstanceSpecificationHeaderView
default void visitNodeInstanceSpecificationHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.NodeInstanceSpecificationHeaderView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitTypedElementHeaderView
default void visitTypedElementHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.TypedElementHeaderView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitPartHeaderView
default void visitPartHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.PartHeaderView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitBaseLifelineHeaderView
default void visitBaseLifelineHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.BaseLifelineHeaderView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitGeneralizationSetView
default void visitGeneralizationSetView([GeneralizationSetView](symbols/shapes/GeneralizationSetView.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitGeneralizationSetHeaderView
default void visitGeneralizationSetHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.GeneralizationSetHeaderView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitElementTaggedValueView
default void visitElementTaggedValueView(com.nomagic.magicdraw.uml.symbols.shapes.ElementTaggedValueView o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitInformationFlowView
default void visitInformationFlowView([InformationFlowView](symbols/paths/InformationFlowView.html) informationFlowView)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitInformationItemView
default void visitInformationItemView([InformationItemView](symbols/shapes/InformationItemView.html) informationItemView)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitDiagramFrameView
default void visitDiagramFrameView([DiagramFrameView](symbols/shapes/DiagramFrameView.html) diagramFrameView)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitDiagramFrameHeaderView
default void visitDiagramFrameHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.DiagramFrameHeaderView diagramFrameHeaderView)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitDiagramFrameLabelView
default void visitDiagramFrameLabelView(com.nomagic.magicdraw.uml.symbols.shapes.DiagramFrameLabelView diagramFrameLabelView)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitCallBehaviorActionHeaderView
default void visitCallBehaviorActionHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.CallBehaviorActionHeaderView callBehaviorActionHeaderView)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitBehaviorLabelView
default void visitBehaviorLabelView(com.nomagic.magicdraw.uml.symbols.shapes.BehaviorLabelView behaviorLabelView)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitObjectNodeViewHeaderView
default void visitObjectNodeViewHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.ObjectNodeViewHeaderView objectNodeViewHeaderView)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitOperationTextArea
default void visitOperationTextArea(com.nomagic.magicdraw.uml.symbols.shapes.OperationTextArea operationTextArea)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitTriggerLabelView
default void visitTriggerLabelView(com.nomagic.magicdraw.uml.symbols.shapes.TriggerLabelView triggerLabelView)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitTransitionLabelView
default void visitTransitionLabelView(com.nomagic.magicdraw.uml.symbols.shapes.TransitionLabelView transitionLabelView)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitAbstractImageShapeView
default void visitAbstractImageShapeView(com.nomagic.magicdraw.uml.symbols.shapes.AbstractImageShapeView imageShapeView)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitEmbeddedImageShapeView
default void visitEmbeddedImageShapeView(com.nomagic.magicdraw.uml.symbols.shapes.EmbeddedImageShapeView imageShapeView)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitImageShapeView
default void visitImageShapeView([ImageShapeView](symbols/shapes/ImageShapeView.html) imageShapeView)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Visits image shape view.
Parameters:
`imageShapeView` - - image shape view.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitImageShapeFromElementView
default void visitImageShapeFromElementView(com.nomagic.magicdraw.uml.symbols.shapes.ImageShapeFromElementView imageShapeView)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitLostFoundMessageView
default void visitLostFoundMessageView(com.nomagic.magicdraw.uml.symbols.paths.LostFoundMessageView lostFoundMessageView)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Visits lost/found message view.
Parameters:
`lostFoundMessageView` - - lost/found message view.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitFoundMessageView
default void visitFoundMessageView([FoundMessageView](symbols/paths/FoundMessageView.html) foundMessageView)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Visits found message view.
Parameters:
`foundMessageView` - - found message view.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitLostMessageView
default void visitLostMessageView([LostMessageView](symbols/paths/LostMessageView.html) lostMessageView)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Visits lost message view.
Parameters:
`lostMessageView` - - lost message view.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitPrimitiveTaggedValueView
default void visitPrimitiveTaggedValueView(com.nomagic.magicdraw.uml.symbols.shapes.PrimitiveTaggedValueView primitiveTaggedValueView)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml</a></div>
<h1 class="title" title="Interface PresentationElementVisitor">Interface PresentationElementVisitor</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="InheritanceVisitor.html" title="class in com.nomagic.magicdraw.uml">InheritanceVisitor</a></code>, <code><a href="Visitor.html" title="class in com.nomagic.magicdraw.uml">Visitor</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">PresentationElementVisitor</span></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitAbstractBaseCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.AbstractCompartmentView)">visitAbstractBaseCompartmentView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.AbstractCompartmentView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitAbstractDiagramPresentationElement(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">visitAbstractDiagramPresentationElement</a><wbr/>(<a href="symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Method visits given object.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitAbstractDiagramPresentationElementContainer(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElementContainer)">visitAbstractDiagramPresentationElementContainer</a><wbr/>(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElementContainer o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitAbstractHeaderShapeView(com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView)">visitAbstractHeaderShapeView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitAbstractImageShapeView(com.nomagic.magicdraw.uml.symbols.shapes.AbstractImageShapeView)">visitAbstractImageShapeView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.AbstractImageShapeView imageShapeView)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitAbstractPathEndShape(com.nomagic.magicdraw.uml.symbols.shapes.AbstractPathEndShape)">visitAbstractPathEndShape</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.AbstractPathEndShape o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitAbstractSeparatorView(com.nomagic.magicdraw.uml.symbols.shapes.AbstractSeparatorView)">visitAbstractSeparatorView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.AbstractSeparatorView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitAbstractShapeWithLabels(com.nomagic.magicdraw.uml.symbols.shapes.AbstractShapeWithLabels)">visitAbstractShapeWithLabels</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.AbstractShapeWithLabels o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitAbstractShapeWithLabelsInside(com.nomagic.magicdraw.uml.symbols.shapes.AbstractShapeWithLabelsInside)">visitAbstractShapeWithLabelsInside</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.AbstractShapeWithLabelsInside o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitAbstractTextBoxView(com.nomagic.magicdraw.uml.symbols.shapes.AbstractTextBoxView)">visitAbstractTextBoxView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.AbstractTextBoxView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitActionHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.ActionHeaderView)">visitActionHeaderView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.ActionHeaderView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitActionView(com.nomagic.magicdraw.uml.symbols.shapes.ActionView)">visitActionView</a><wbr/>(<a href="symbols/shapes/ActionView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ActionView</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitActivationView(com.nomagic.magicdraw.uml.symbols.shapes.ActivationView)">visitActivationView</a><wbr/>(<a href="symbols/shapes/ActivationView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ActivationView</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitActivityGroupView(com.nomagic.magicdraw.uml.symbols.shapes.ActivityGroupView)">visitActivityGroupView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.ActivityGroupView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitActivityObjectViewContainer(com.nomagic.magicdraw.uml.symbols.ActivityObjectViewContainer)">visitActivityObjectViewContainer</a><wbr/>(com.nomagic.magicdraw.uml.symbols.ActivityObjectViewContainer o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitActorView(com.nomagic.magicdraw.uml.symbols.shapes.ActorView)">visitActorView</a><wbr/>(<a href="symbols/shapes/ActorView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ActorView</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitArtifactsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.ArtifactsCompartmentView)">visitArtifactsCompartmentView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.ArtifactsCompartmentView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitArtifactView(com.nomagic.magicdraw.uml.symbols.shapes.ArtifactView)">visitArtifactView</a><wbr/>(<a href="symbols/shapes/ArtifactView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ArtifactView</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitAssociationClassView(com.nomagic.magicdraw.uml.symbols.paths.AssociationClassView)">visitAssociationClassView</a><wbr/>(<a href="symbols/paths/AssociationClassView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">AssociationClassView</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitAssociationTextBoxView(com.nomagic.magicdraw.uml.symbols.shapes.AssociationTextBoxView)">visitAssociationTextBoxView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.AssociationTextBoxView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitAssociationView(com.nomagic.magicdraw.uml.symbols.paths.AssociationView)">visitAssociationView</a><wbr/>(<a href="symbols/paths/AssociationView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">AssociationView</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitAttributesCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.AttributesCompartmentView)">visitAttributesCompartmentView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.AttributesCompartmentView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitAttributeView(com.nomagic.magicdraw.uml.symbols.shapes.AttributeView)">visitAttributeView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.AttributeView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitBarView(com.nomagic.magicdraw.uml.symbols.shapes.BarView)">visitBarView</a><wbr/>(<a href="symbols/shapes/BarView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">BarView</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitBaseCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.BaseCompartmentView)">visitBaseCompartmentView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.BaseCompartmentView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitBaseElementTextArea(com.nomagic.magicdraw.uml.symbols.shapes.BaseElementTextArea)">visitBaseElementTextArea</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.BaseElementTextArea o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitBaseElementTextField(com.nomagic.magicdraw.uml.symbols.shapes.BaseElementTextField)">visitBaseElementTextField</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.BaseElementTextField o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitBaseFlowView(com.nomagic.magicdraw.uml.symbols.paths.BaseFlowView)">visitBaseFlowView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.paths.BaseFlowView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitBaseHeaderShapeView(com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView)">visitBaseHeaderShapeView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitBaseHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderView)">visitBaseHeaderView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitBaseLifelineHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.BaseLifelineHeaderView)">visitBaseLifelineHeaderView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.BaseLifelineHeaderView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitBaseLifelineView(com.nomagic.magicdraw.uml.symbols.shapes.BaseLifelineView)">visitBaseLifelineView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.BaseLifelineView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitBaseMembersCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.BaseMembersCompartmentView)">visitBaseMembersCompartmentView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.BaseMembersCompartmentView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitBaseNameHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.BaseNameHeaderView)">visitBaseNameHeaderView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.BaseNameHeaderView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitBasePropertiesCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.BasePropertiesCompartmentView)">visitBasePropertiesCompartmentView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.BasePropertiesCompartmentView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitBaseRealizationView(com.nomagic.magicdraw.uml.symbols.paths.BaseRealizationView)">visitBaseRealizationView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.paths.BaseRealizationView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitBaseSplitCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.BaseSplitCompartmentView)">visitBaseSplitCompartmentView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.BaseSplitCompartmentView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitBaseTreeShape(com.nomagic.magicdraw.uml.symbols.shapes.BaseTreeShape)">visitBaseTreeShape</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.BaseTreeShape o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitBehavioralFeatureView(com.nomagic.magicdraw.uml.symbols.shapes.BehavioralFeatureView)">visitBehavioralFeatureView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.BehavioralFeatureView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitBehaviorLabelView(com.nomagic.magicdraw.uml.symbols.shapes.BehaviorLabelView)">visitBehaviorLabelView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.BehaviorLabelView behaviorLabelView)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitBehaviorsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.BehaviorsCompartmentView)">visitBehaviorsCompartmentView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.BehaviorsCompartmentView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitBehaviorView(com.nomagic.magicdraw.uml.symbols.shapes.BehaviorView)">visitBehaviorView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.BehaviorView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitBodyRegionView(com.nomagic.magicdraw.uml.symbols.shapes.ClauseView.BodyRegionView)">visitBodyRegionView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.ClauseView.BodyRegionView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitBodyRegionView(com.nomagic.magicdraw.uml.symbols.shapes.LoopNodeView.BodyRegionView)">visitBodyRegionView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.LoopNodeView.BodyRegionView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitCallBehaviorActionHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.CallBehaviorActionHeaderView)">visitCallBehaviorActionHeaderView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.CallBehaviorActionHeaderView callBehaviorActionHeaderView)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitCallBehaviorActionView(com.nomagic.magicdraw.uml.symbols.shapes.CallBehaviorActionView)">visitCallBehaviorActionView</a><wbr/>(<a href="symbols/shapes/CallBehaviorActionView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">CallBehaviorActionView</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitCallOperationActionView(com.nomagic.magicdraw.uml.symbols.shapes.CallOperationActionView)">visitCallOperationActionView</a><wbr/>(<a href="symbols/shapes/CallOperationActionView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">CallOperationActionView</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitClassHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.ClassHeaderView)">visitClassHeaderView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.ClassHeaderView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitClassifierHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.ClassifierHeaderView)">visitClassifierHeaderView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.ClassifierHeaderView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitClassifierView(com.nomagic.magicdraw.uml.symbols.shapes.ClassifierView)">visitClassifierView</a><wbr/>(<a href="symbols/shapes/ClassifierView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ClassifierView</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitClassView(com.nomagic.magicdraw.uml.symbols.shapes.ClassView)">visitClassView</a><wbr/>(<a href="symbols/shapes/ClassView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ClassView</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitClauseCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.ClauseCompartmentView)">visitClauseCompartmentView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.ClauseCompartmentView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitClauseView(com.nomagic.magicdraw.uml.symbols.shapes.ClauseView)">visitClauseView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.ClauseView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitCollaborationHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.CollaborationHeaderView)">visitCollaborationHeaderView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.CollaborationHeaderView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitCollaborationUseView(com.nomagic.magicdraw.uml.symbols.shapes.CollaborationUseView)">visitCollaborationUseView</a><wbr/>(<a href="symbols/shapes/CollaborationUseView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">CollaborationUseView</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitCollaborationView(com.nomagic.magicdraw.uml.symbols.shapes.CollaborationView)">visitCollaborationView</a><wbr/>(<a href="symbols/shapes/CollaborationView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">CollaborationView</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitCombinedFragmentHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.CombinedFragmentHeaderView)">visitCombinedFragmentHeaderView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.CombinedFragmentHeaderView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitCombinedFragmentView(com.nomagic.magicdraw.uml.symbols.shapes.CombinedFragmentView)">visitCombinedFragmentView</a><wbr/>(<a href="symbols/shapes/CombinedFragmentView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">CombinedFragmentView</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitCommentView(com.nomagic.magicdraw.uml.symbols.shapes.CommentView)">visitCommentView</a><wbr/>(<a href="symbols/shapes/CommentView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">CommentView</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitCommunicationPathView(com.nomagic.magicdraw.uml.symbols.paths.CommunicationPathView)">visitCommunicationPathView</a><wbr/>(<a href="symbols/paths/CommunicationPathView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">CommunicationPathView</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitCompartmentElement(com.nomagic.magicdraw.uml.CompartmentElement)">visitCompartmentElement</a><wbr/>(<a href="CompartmentElement.html" title="interface in com.nomagic.magicdraw.uml">CompartmentElement</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Method visitCompartmentElement.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitComponentHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.ComponentHeaderView)">visitComponentHeaderView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.ComponentHeaderView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitComponentView(com.nomagic.magicdraw.uml.symbols.shapes.ComponentView)">visitComponentView</a><wbr/>(<a href="symbols/shapes/ComponentView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ComponentView</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitConditionalNodeView(com.nomagic.magicdraw.uml.symbols.shapes.ConditionalNodeView)">visitConditionalNodeView</a><wbr/>(<a href="symbols/shapes/ConditionalNodeView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ConditionalNodeView</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitConnectorEndView(com.nomagic.magicdraw.uml.symbols.shapes.ConnectorEndView)">visitConnectorEndView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.ConnectorEndView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitConnectorToSelfView(com.nomagic.magicdraw.uml.symbols.paths.ConnectorToSelfView)">visitConnectorToSelfView</a><wbr/>(<a href="symbols/paths/ConnectorToSelfView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">ConnectorToSelfView</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitConnectorView(com.nomagic.magicdraw.uml.symbols.paths.ConnectorView)">visitConnectorView</a><wbr/>(<a href="symbols/paths/ConnectorView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">ConnectorView</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitConstraintCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.ConstraintCompartmentView)">visitConstraintCompartmentView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.ConstraintCompartmentView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitConstraintLinkView(com.nomagic.magicdraw.uml.symbols.paths.ConstraintLinkView)">visitConstraintLinkView</a><wbr/>(<a href="symbols/paths/ConstraintLinkView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">ConstraintLinkView</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitConstraintsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.ConstraintsCompartmentView)">visitConstraintsCompartmentView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.ConstraintsCompartmentView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitConstraintsView(com.nomagic.magicdraw.uml.symbols.shapes.ConstraintsView)">visitConstraintsView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.ConstraintsView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitContainerLinkView(com.nomagic.magicdraw.uml.symbols.paths.ContainerLinkView)">visitContainerLinkView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.paths.ContainerLinkView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitContainerShapeView(com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView)">visitContainerShapeView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitContainmentLinkView(com.nomagic.magicdraw.uml.symbols.paths.ContainmentLinkView)">visitContainmentLinkView</a><wbr/>(<a href="symbols/paths/ContainmentLinkView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">ContainmentLinkView</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitContentShape(com.nomagic.magicdraw.uml.symbols.shapes.ContentShape)">visitContentShape</a><wbr/>(<a href="symbols/shapes/ContentShape.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ContentShape</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitControlFlowView(com.nomagic.magicdraw.uml.symbols.paths.ControlFlowView)">visitControlFlowView</a><wbr/>(<a href="symbols/paths/ControlFlowView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">ControlFlowView</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitConveyedInformationView(com.nomagic.magicdraw.uml.symbols.shapes.ConveyedInformationView)">visitConveyedInformationView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.ConveyedInformationView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitCustomCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.CustomCompartmentView)">visitCustomCompartmentView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.CustomCompartmentView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitCustomElementCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.CustomElementCompartmentView)">visitCustomElementCompartmentView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.CustomElementCompartmentView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitDataTypeView(com.nomagic.magicdraw.uml.symbols.shapes.DataTypeView)">visitDataTypeView</a><wbr/>(<a href="symbols/shapes/DataTypeView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">DataTypeView</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitDecisionView(com.nomagic.magicdraw.uml.symbols.shapes.DecisionView)">visitDecisionView</a><wbr/>(<a href="symbols/shapes/DecisionView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">DecisionView</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitDependencyView(com.nomagic.magicdraw.uml.symbols.paths.DependencyView)">visitDependencyView</a><wbr/>(<a href="symbols/paths/DependencyView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">DependencyView</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitDeployedElementsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.DeployedElementsCompartmentView)">visitDeployedElementsCompartmentView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.DeployedElementsCompartmentView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitDeploymentView(com.nomagic.magicdraw.uml.symbols.paths.DeploymentView)">visitDeploymentView</a><wbr/>(<a href="symbols/paths/DeploymentView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">DeploymentView</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitDiagramFrameHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.DiagramFrameHeaderView)">visitDiagramFrameHeaderView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.DiagramFrameHeaderView diagramFrameHeaderView)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitDiagramFrameLabelView(com.nomagic.magicdraw.uml.symbols.shapes.DiagramFrameLabelView)">visitDiagramFrameLabelView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.DiagramFrameLabelView diagramFrameLabelView)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitDiagramFrameView(com.nomagic.magicdraw.uml.symbols.shapes.DiagramFrameView)">visitDiagramFrameView</a><wbr/>(<a href="symbols/shapes/DiagramFrameView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">DiagramFrameView</a> diagramFrameView)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitDiagramLegendShape(com.nomagic.magicdraw.uml.symbols.shapes.DiagramLegendShape)">visitDiagramLegendShape</a><wbr/>(<a href="symbols/shapes/DiagramLegendShape.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">DiagramLegendShape</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitDiagramObjectViewContainer(com.nomagic.magicdraw.uml.symbols.DiagramObjectViewContainer)">visitDiagramObjectViewContainer</a><wbr/>(com.nomagic.magicdraw.uml.symbols.DiagramObjectViewContainer o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitDiagramOverviewCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.DiagramOverviewCompartmentView)">visitDiagramOverviewCompartmentView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.DiagramOverviewCompartmentView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitDiagramPresentationElement(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement)">visitDiagramPresentationElement</a><wbr/>(<a href="symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Method visits given object.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitDiagramPropertiesShape(com.nomagic.magicdraw.uml.symbols.shapes.DiagramPropertiesShape)">visitDiagramPropertiesShape</a><wbr/>(<a href="symbols/shapes/DiagramPropertiesShape.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">DiagramPropertiesShape</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitDiagramShape(com.nomagic.magicdraw.uml.symbols.shapes.DiagramShape)">visitDiagramShape</a><wbr/>(<a href="symbols/shapes/DiagramShape.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">DiagramShape</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitDirectionIconView(com.nomagic.magicdraw.uml.symbols.shapes.DirectionIconView)">visitDirectionIconView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.DirectionIconView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitDummyDiagramObjectViewContainer(com.nomagic.magicdraw.uml.symbols.DummyDiagramObjectViewContainer)">visitDummyDiagramObjectViewContainer</a><wbr/>(com.nomagic.magicdraw.uml.symbols.DummyDiagramObjectViewContainer o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitDurationConstraintView(com.nomagic.magicdraw.uml.symbols.paths.DurationConstraintView)">visitDurationConstraintView</a><wbr/>(<a href="symbols/paths/DurationConstraintView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">DurationConstraintView</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitElementCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.ElementCompartmentView)">visitElementCompartmentView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.ElementCompartmentView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitElementImportView(com.nomagic.magicdraw.uml.symbols.paths.ElementImportView)">visitElementImportView</a><wbr/>(<a href="symbols/paths/ElementImportView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">ElementImportView</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitElementPropertiesCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.ElementPropertiesCompartmentView)">visitElementPropertiesCompartmentView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.ElementPropertiesCompartmentView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitElementTaggedValueView(com.nomagic.magicdraw.uml.symbols.shapes.ElementTaggedValueView)">visitElementTaggedValueView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.ElementTaggedValueView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitElementWithIconView(com.nomagic.magicdraw.uml.symbols.shapes.ElementWithIconView)">visitElementWithIconView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.ElementWithIconView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitElseRegionView(com.nomagic.magicdraw.uml.symbols.shapes.ClauseView.ElseRegionView)">visitElseRegionView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.ClauseView.ElseRegionView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitEmbeddedImageShapeView(com.nomagic.magicdraw.uml.symbols.shapes.EmbeddedImageShapeView)">visitEmbeddedImageShapeView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.EmbeddedImageShapeView imageShapeView)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitEnumerationHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.EnumerationHeaderView)">visitEnumerationHeaderView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.EnumerationHeaderView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitEnumerationLiteralsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.EnumerationLiteralsCompartmentView)">visitEnumerationLiteralsCompartmentView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.EnumerationLiteralsCompartmentView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitEnumerationLiteralView(com.nomagic.magicdraw.uml.symbols.shapes.EnumerationLiteralView)">visitEnumerationLiteralView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.EnumerationLiteralView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitEnumerationView(com.nomagic.magicdraw.uml.symbols.shapes.EnumerationView)">visitEnumerationView</a><wbr/>(<a href="symbols/shapes/EnumerationView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">EnumerationView</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitExceptionHandlerView(com.nomagic.magicdraw.uml.symbols.paths.ExceptionHandlerView)">visitExceptionHandlerView</a><wbr/>(<a href="symbols/paths/ExceptionHandlerView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">ExceptionHandlerView</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitExpansionNodeView(com.nomagic.magicdraw.uml.symbols.shapes.ExpansionNodeView)">visitExpansionNodeView</a><wbr/>(<a href="symbols/shapes/ExpansionNodeView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ExpansionNodeView</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitExpansionRegionView(com.nomagic.magicdraw.uml.symbols.shapes.ExpansionRegionView)">visitExpansionRegionView</a><wbr/>(<a href="symbols/shapes/ExpansionRegionView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ExpansionRegionView</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitExtendView(com.nomagic.magicdraw.uml.symbols.paths.ExtendView)">visitExtendView</a><wbr/>(<a href="symbols/paths/ExtendView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">ExtendView</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitExtensionPointsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.ExtensionPointsCompartmentView)">visitExtensionPointsCompartmentView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.ExtensionPointsCompartmentView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitExtensionPointView(com.nomagic.magicdraw.uml.symbols.shapes.ExtensionPointView)">visitExtensionPointView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.ExtensionPointView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitExtensionView(com.nomagic.magicdraw.uml.symbols.paths.ExtensionView)">visitExtensionView</a><wbr/>(<a href="symbols/paths/ExtensionView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">ExtensionView</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitFlowConnectorView(com.nomagic.magicdraw.uml.symbols.shapes.FlowConnectorView)">visitFlowConnectorView</a><wbr/>(<a href="symbols/shapes/FlowConnectorView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">FlowConnectorView</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitFoundMessageView(com.nomagic.magicdraw.uml.symbols.paths.FoundMessageView)">visitFoundMessageView</a><wbr/>(<a href="symbols/paths/FoundMessageView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">FoundMessageView</a> foundMessageView)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits found message view.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitFragmentView(com.nomagic.magicdraw.uml.symbols.shapes.FragmentView)">visitFragmentView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.FragmentView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitFrameHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.FrameHeaderView)">visitFrameHeaderView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.FrameHeaderView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitFrameView(com.nomagic.magicdraw.uml.symbols.shapes.FrameView)">visitFrameView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.FrameView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitGeneralizationSetHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.GeneralizationSetHeaderView)">visitGeneralizationSetHeaderView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.GeneralizationSetHeaderView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitGeneralizationSetView(com.nomagic.magicdraw.uml.symbols.shapes.GeneralizationSetView)">visitGeneralizationSetView</a><wbr/>(<a href="symbols/shapes/GeneralizationSetView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">GeneralizationSetView</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitGeneralizationView(com.nomagic.magicdraw.uml.symbols.paths.GeneralizationView)">visitGeneralizationView</a><wbr/>(<a href="symbols/paths/GeneralizationView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">GeneralizationView</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitGenericView(com.nomagic.magicdraw.uml.symbols.shapes.GenericView)">visitGenericView</a><wbr/>(<a href="symbols/shapes/GenericView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">GenericView</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitHeaderOfBaseHeaderShapeView(com.nomagic.magicdraw.uml.symbols.shapes.HeaderOfBaseHeaderShapeView)">visitHeaderOfBaseHeaderShapeView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.HeaderOfBaseHeaderShapeView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitHeaderShapeView(com.nomagic.magicdraw.uml.symbols.shapes.HeaderShapeView)">visitHeaderShapeView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.HeaderShapeView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.HeaderView)">visitHeaderView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.HeaderView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitImageShapeFromElementView(com.nomagic.magicdraw.uml.symbols.shapes.ImageShapeFromElementView)">visitImageShapeFromElementView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.ImageShapeFromElementView imageShapeView)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitImageShapeView(com.nomagic.magicdraw.uml.symbols.shapes.ImageShapeView)">visitImageShapeView</a><wbr/>(<a href="symbols/shapes/ImageShapeView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ImageShapeView</a> imageShapeView)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits image shape view.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitImageView(com.nomagic.magicdraw.uml.symbols.shapes.ImageView)">visitImageView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.ImageView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitIncludeView(com.nomagic.magicdraw.uml.symbols.paths.IncludeView)">visitIncludeView</a><wbr/>(<a href="symbols/paths/IncludeView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">IncludeView</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitInformationFlowView(com.nomagic.magicdraw.uml.symbols.paths.InformationFlowView)">visitInformationFlowView</a><wbr/>(<a href="symbols/paths/InformationFlowView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">InformationFlowView</a> informationFlowView)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitInformationItemHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.InformationItemHeaderView)">visitInformationItemHeaderView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.InformationItemHeaderView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitInformationItemView(com.nomagic.magicdraw.uml.symbols.shapes.InformationItemView)">visitInformationItemView</a><wbr/>(<a href="symbols/shapes/InformationItemView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">InformationItemView</a> informationItemView)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitInnerElementsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.InnerElementsCompartmentView)">visitInnerElementsCompartmentView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.InnerElementsCompartmentView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitInstanceSlotsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.InstanceSlotsCompartmentView)">visitInstanceSlotsCompartmentView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.InstanceSlotsCompartmentView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitInstanceSpecificationHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.InstanceSpecificationHeaderView)">visitInstanceSpecificationHeaderView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.InstanceSpecificationHeaderView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitInstanceSpecificationView(com.nomagic.magicdraw.uml.symbols.shapes.InstanceSpecificationView)">visitInstanceSpecificationView</a><wbr/>(<a href="symbols/shapes/InstanceSpecificationView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">InstanceSpecificationView</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitInteractionOperandsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.InteractionOperandsCompartmentView)">visitInteractionOperandsCompartmentView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.InteractionOperandsCompartmentView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitInteractionOperandView(com.nomagic.magicdraw.uml.symbols.shapes.InteractionOperandView)">visitInteractionOperandView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.InteractionOperandView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitInteractionUseOverviewView(com.nomagic.magicdraw.uml.symbols.shapes.InteractionUseOverviewView)">visitInteractionUseOverviewView</a><wbr/>(<a href="symbols/shapes/InteractionUseOverviewView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">InteractionUseOverviewView</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitInteractionUseView(com.nomagic.magicdraw.uml.symbols.shapes.InteractionUseView)">visitInteractionUseView</a><wbr/>(<a href="symbols/shapes/InteractionUseView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">InteractionUseView</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitInterfaceHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.InterfaceHeaderView)">visitInterfaceHeaderView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.InterfaceHeaderView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitInterfaceRealizationView(com.nomagic.magicdraw.uml.symbols.paths.InterfaceRealizationView)">visitInterfaceRealizationView</a><wbr/>(<a href="symbols/paths/InterfaceRealizationView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">InterfaceRealizationView</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitInterfacesCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.InterfacesCompartmentView)">visitInterfacesCompartmentView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.InterfacesCompartmentView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitInterfaceView(com.nomagic.magicdraw.uml.symbols.shapes.InterfaceView)">visitInterfaceView</a><wbr/>(<a href="symbols/shapes/InterfaceView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">InterfaceView</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitInternalStateCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.InternalStateCompartmentView)">visitInternalStateCompartmentView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.InternalStateCompartmentView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitInterruptibleActivityRegionView(com.nomagic.magicdraw.uml.symbols.shapes.InterruptibleActivityRegionView)">visitInterruptibleActivityRegionView</a><wbr/>(<a href="symbols/shapes/InterruptibleActivityRegionView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">InterruptibleActivityRegionView</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitLegendItemsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.LegendItemsCompartmentView)">visitLegendItemsCompartmentView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.LegendItemsCompartmentView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitLegendItemView(com.nomagic.magicdraw.uml.symbols.shapes.LegendItemView)">visitLegendItemView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.LegendItemView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitLifeLineLineView(com.nomagic.magicdraw.uml.symbols.shapes.LifeLineLineView)">visitLifeLineLineView</a><wbr/>(<a href="symbols/shapes/LifeLineLineView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">LifeLineLineView</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitLifelineView(com.nomagic.magicdraw.uml.symbols.shapes.LifelineView)">visitLifelineView</a><wbr/>(<a href="symbols/shapes/LifelineView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">LifelineView</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitLinkAttributeView(com.nomagic.magicdraw.uml.symbols.paths.LinkAttributeView)">visitLinkAttributeView</a><wbr/>(<a href="symbols/paths/LinkAttributeView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">LinkAttributeView</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitLinkEndView(com.nomagic.magicdraw.uml.symbols.shapes.LinkEndView)">visitLinkEndView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.LinkEndView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitLinkView(com.nomagic.magicdraw.uml.symbols.paths.LinkView)">visitLinkView</a><wbr/>(<a href="symbols/paths/LinkView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">LinkView</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitLinkWithEndsView(com.nomagic.magicdraw.uml.symbols.paths.LinkWithEndsView)">visitLinkWithEndsView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.paths.LinkWithEndsView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitLinkWithRolesView(com.nomagic.magicdraw.uml.symbols.paths.LinkWithRolesView)">visitLinkWithRolesView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.paths.LinkWithRolesView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitLinkWithStereotype(com.nomagic.magicdraw.uml.symbols.paths.LinkWithStereotype)">visitLinkWithStereotype</a><wbr/>(com.nomagic.magicdraw.uml.symbols.paths.LinkWithStereotype o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitListElementView(com.nomagic.magicdraw.uml.symbols.shapes.ListElementView)">visitListElementView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.ListElementView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitLoopNodeView(com.nomagic.magicdraw.uml.symbols.shapes.LoopNodeView)">visitLoopNodeView</a><wbr/>(<a href="symbols/shapes/LoopNodeView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">LoopNodeView</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitLostFoundMessageView(com.nomagic.magicdraw.uml.symbols.paths.LostFoundMessageView)">visitLostFoundMessageView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.paths.LostFoundMessageView lostFoundMessageView)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits lost/found message view.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitLostMessageView(com.nomagic.magicdraw.uml.symbols.paths.LostMessageView)">visitLostMessageView</a><wbr/>(<a href="symbols/paths/LostMessageView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">LostMessageView</a> lostMessageView)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits lost message view.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitMemberView(com.nomagic.magicdraw.uml.symbols.shapes.MemberView)">visitMemberView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.MemberView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitMessageSignatureView(com.nomagic.magicdraw.uml.symbols.shapes.MessageSignatureView)">visitMessageSignatureView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.MessageSignatureView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitMessageView(com.nomagic.magicdraw.uml.symbols.shapes.MessageView)">visitMessageView</a><wbr/>(<a href="symbols/shapes/MessageView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">MessageView</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitNNaryAssociationView(com.nomagic.magicdraw.uml.symbols.shapes.NNaryAssociationView)">visitNNaryAssociationView</a><wbr/>(<a href="symbols/shapes/NNaryAssociationView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">NNaryAssociationView</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitNodeHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.NodeHeaderView)">visitNodeHeaderView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.NodeHeaderView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitNodeInstanceSpecificationHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.NodeInstanceSpecificationHeaderView)">visitNodeInstanceSpecificationHeaderView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.NodeInstanceSpecificationHeaderView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitNodeInstanceSpecificationView(com.nomagic.magicdraw.uml.symbols.shapes.NodeInstanceSpecificationView)">visitNodeInstanceSpecificationView</a><wbr/>(<a href="symbols/shapes/NodeInstanceSpecificationView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">NodeInstanceSpecificationView</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitNodeView(com.nomagic.magicdraw.uml.symbols.shapes.NodeView)">visitNodeView</a><wbr/>(<a href="symbols/shapes/NodeView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">NodeView</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitNoteAnchorView(com.nomagic.magicdraw.uml.symbols.paths.NoteAnchorView)">visitNoteAnchorView</a><wbr/>(<a href="symbols/paths/NoteAnchorView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">NoteAnchorView</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitNoteHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.NoteHeaderView)">visitNoteHeaderView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.NoteHeaderView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitNoteView(com.nomagic.magicdraw.uml.symbols.shapes.NoteView)">visitNoteView</a><wbr/>(<a href="symbols/shapes/NoteView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">NoteView</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitObjectFlowView(com.nomagic.magicdraw.uml.symbols.paths.ObjectFlowView)">visitObjectFlowView</a><wbr/>(<a href="symbols/paths/ObjectFlowView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">ObjectFlowView</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitObjectNodeView(com.nomagic.magicdraw.uml.symbols.shapes.ObjectNodeView)">visitObjectNodeView</a><wbr/>(<a href="symbols/shapes/ObjectNodeView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ObjectNodeView</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitObjectNodeViewHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.ObjectNodeViewHeaderView)">visitObjectNodeViewHeaderView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.ObjectNodeViewHeaderView objectNodeViewHeaderView)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitOpaqueActionView(com.nomagic.magicdraw.uml.symbols.shapes.OpaqueActionView)">visitOpaqueActionView</a><wbr/>(<a href="symbols/shapes/OpaqueActionView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">OpaqueActionView</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitOperationsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.OperationsCompartmentView)">visitOperationsCompartmentView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.OperationsCompartmentView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitOperationTextArea(com.nomagic.magicdraw.uml.symbols.shapes.OperationTextArea)">visitOperationTextArea</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.OperationTextArea operationTextArea)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitOperationView(com.nomagic.magicdraw.uml.symbols.shapes.OperationView)">visitOperationView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.OperationView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitPackageHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.PackageHeaderView)">visitPackageHeaderView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.PackageHeaderView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitPackageImportView(com.nomagic.magicdraw.uml.symbols.paths.PackageImportView)">visitPackageImportView</a><wbr/>(<a href="symbols/paths/PackageImportView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PackageImportView</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitPackageMergeView(com.nomagic.magicdraw.uml.symbols.paths.PackageMergeView)">visitPackageMergeView</a><wbr/>(<a href="symbols/paths/PackageMergeView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PackageMergeView</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitPackageView(com.nomagic.magicdraw.uml.symbols.shapes.PackageView)">visitPackageView</a><wbr/>(<a href="symbols/shapes/PackageView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">PackageView</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitPartHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.PartHeaderView)">visitPartHeaderView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.PartHeaderView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitPartView(com.nomagic.magicdraw.uml.symbols.shapes.PartView)">visitPartView</a><wbr/>(<a href="symbols/shapes/PartView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">PartView</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitPathConnector(com.nomagic.magicdraw.uml.symbols.paths.PathConnector)">visitPathConnector</a><wbr/>(<a href="symbols/paths/PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathConnector</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Method visits given object.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">visitPathElement</a><wbr/>(<a href="symbols/paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Method visits given object.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitPathToSelfShape(com.nomagic.magicdraw.uml.symbols.shapes.PathToSelfShape)">visitPathToSelfShape</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.PathToSelfShape o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitPinView(com.nomagic.magicdraw.uml.symbols.shapes.PinView)">visitPinView</a><wbr/>(<a href="symbols/shapes/PinView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">PinView</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitPortAttributeView(com.nomagic.magicdraw.uml.symbols.shapes.PortAttributeView)">visitPortAttributeView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.PortAttributeView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitPortsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.PortsCompartmentView)">visitPortsCompartmentView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.PortsCompartmentView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitPortView(com.nomagic.magicdraw.uml.symbols.shapes.PortView)">visitPortView</a><wbr/>(<a href="symbols/shapes/PortView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">PortView</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">visitPresentationElement</a><wbr/>(<a href="symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Method visits given object.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitPresentationElementContainer(com.nomagic.magicdraw.uml.symbols.PresentationElementContainer)">visitPresentationElementContainer</a><wbr/>(com.nomagic.magicdraw.uml.symbols.PresentationElementContainer o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitPrimitiveTaggedValueView(com.nomagic.magicdraw.uml.symbols.shapes.PrimitiveTaggedValueView)">visitPrimitiveTaggedValueView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.PrimitiveTaggedValueView primitiveTaggedValueView)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitPrimitiveTypeView(com.nomagic.magicdraw.uml.symbols.shapes.PrimitiveTypeView)">visitPrimitiveTypeView</a><wbr/>(<a href="symbols/shapes/PrimitiveTypeView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">PrimitiveTypeView</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitPrimitiveValueView(com.nomagic.magicdraw.uml.symbols.shapes.PrimitiveValueView)">visitPrimitiveValueView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.PrimitiveValueView view)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitProfileApplicationView(com.nomagic.magicdraw.uml.symbols.paths.ProfileApplicationView)">visitProfileApplicationView</a><wbr/>(<a href="symbols/paths/ProfileApplicationView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">ProfileApplicationView</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitProjectOptions(com.nomagic.magicdraw.core.options.ProjectOptions)">visitProjectOptions</a><wbr/>(<a href="../core/options/ProjectOptions.html" title="class in com.nomagic.magicdraw.core.options">ProjectOptions</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitPseudoNodeView(com.nomagic.magicdraw.uml.symbols.shapes.PseudoNodeView)">visitPseudoNodeView</a><wbr/>(<a href="symbols/shapes/PseudoNodeView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">PseudoNodeView</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitPseudoStateView(com.nomagic.magicdraw.uml.symbols.shapes.PseudoStateView)">visitPseudoStateView</a><wbr/>(<a href="symbols/shapes/PseudoStateView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">PseudoStateView</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitQualifiersView(com.nomagic.magicdraw.uml.symbols.shapes.QualifiersView)">visitQualifiersView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.QualifiersView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitRealizationsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.RealizationsCompartmentView)">visitRealizationsCompartmentView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.RealizationsCompartmentView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitRealizationView(com.nomagic.magicdraw.uml.symbols.paths.RealizationView)">visitRealizationView</a><wbr/>(<a href="symbols/paths/RealizationView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">RealizationView</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitReceptionsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.ReceptionsCompartmentView)">visitReceptionsCompartmentView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.ReceptionsCompartmentView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitReceptionView(com.nomagic.magicdraw.uml.symbols.shapes.ReceptionView)">visitReceptionView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.ReceptionView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitRectangularShape(com.nomagic.magicdraw.uml.symbols.shapes.RectangularShape)">visitRectangularShape</a><wbr/>(<a href="symbols/shapes/RectangularShape.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">RectangularShape</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitRegionsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.RegionsCompartmentView)">visitRegionsCompartmentView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.RegionsCompartmentView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitRegionView(com.nomagic.magicdraw.uml.symbols.shapes.RegionView)">visitRegionView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.RegionView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitRequiredProvidedCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.RequiredProvidedInterfacesCompartmentView)">visitRequiredProvidedCompartmentView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.RequiredProvidedInterfacesCompartmentView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitRoleBindingView(com.nomagic.magicdraw.uml.symbols.paths.RoleBindingView)">visitRoleBindingView</a><wbr/>(<a href="symbols/paths/RoleBindingView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">RoleBindingView</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitRoleView(com.nomagic.magicdraw.uml.symbols.shapes.RoleView)">visitRoleView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.RoleView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitSeparatorView(com.nomagic.magicdraw.uml.symbols.shapes.SeparatorView)">visitSeparatorView</a><wbr/>(<a href="symbols/shapes/SeparatorView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">SeparatorView</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitSeqBaseMessageView(com.nomagic.magicdraw.uml.symbols.paths.SeqBaseMessageView)">visitSeqBaseMessageView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.paths.SeqBaseMessageView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitSeqMessageView(com.nomagic.magicdraw.uml.symbols.paths.SeqMessageView)">visitSeqMessageView</a><wbr/>(<a href="symbols/paths/SeqMessageView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">SeqMessageView</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitSeqSelfMessageView(com.nomagic.magicdraw.uml.symbols.paths.SeqSelfMessageView)">visitSeqSelfMessageView</a><wbr/>(<a href="symbols/paths/SeqSelfMessageView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">SeqSelfMessageView</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitSequenceLifelineView(com.nomagic.magicdraw.uml.symbols.shapes.SequenceLifelineView)">visitSequenceLifelineView</a><wbr/>(<a href="symbols/shapes/SequenceLifelineView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">SequenceLifelineView</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitSequenceNodeView(com.nomagic.magicdraw.uml.symbols.shapes.SequenceNodeView)">visitSequenceNodeView</a><wbr/>(<a href="symbols/shapes/SequenceNodeView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">SequenceNodeView</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitSequenceObjectViewContainer(com.nomagic.magicdraw.uml.symbols.SequenceObjectViewContainer)">visitSequenceObjectViewContainer</a><wbr/>(com.nomagic.magicdraw.uml.symbols.SequenceObjectViewContainer o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitSetupRegionView(com.nomagic.magicdraw.uml.symbols.shapes.LoopNodeView.SetupRegionView)">visitSetupRegionView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.LoopNodeView.SetupRegionView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitShapeElement(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement)">visitShapeElement</a><wbr/>(<a href="symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Method visits given object.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitShapeWithLabels(com.nomagic.magicdraw.uml.symbols.shapes.ShapeWithLabels)">visitShapeWithLabels</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.ShapeWithLabels o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitSignalActionView(com.nomagic.magicdraw.uml.symbols.shapes.SignalActionView)">visitSignalActionView</a><wbr/>(<a href="symbols/shapes/SignalActionView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">SignalActionView</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitSignalView(com.nomagic.magicdraw.uml.symbols.shapes.SignalView)">visitSignalView</a><wbr/>(<a href="symbols/shapes/SignalView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">SignalView</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitSimpleActivityRegionView(com.nomagic.magicdraw.uml.symbols.shapes.SimpleActivityRegionView)">visitSimpleActivityRegionView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.SimpleActivityRegionView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitSlotView(com.nomagic.magicdraw.uml.symbols.shapes.SlotView)">visitSlotView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.SlotView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitSplitView(com.nomagic.magicdraw.uml.symbols.shapes.SplitView)">visitSplitView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.SplitView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitStateHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.StateHeaderView)">visitStateHeaderView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.StateHeaderView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitStateInvariantHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.StateInvariantHeaderView)">visitStateInvariantHeaderView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.StateInvariantHeaderView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitStateInvariantView(com.nomagic.magicdraw.uml.symbols.shapes.StateInvariantView)">visitStateInvariantView</a><wbr/>(<a href="symbols/shapes/StateInvariantView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">StateInvariantView</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitStateObjectViewContainer(com.nomagic.magicdraw.uml.symbols.StateObjectViewContainer)">visitStateObjectViewContainer</a><wbr/>(com.nomagic.magicdraw.uml.symbols.StateObjectViewContainer o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitStateView(com.nomagic.magicdraw.uml.symbols.shapes.StateView)">visitStateView</a><wbr/>(<a href="symbols/shapes/StateView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">StateView</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitStereotypeHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.StereotypeHeaderView)">visitStereotypeHeaderView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.StereotypeHeaderView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitStereotypeIconView(com.nomagic.magicdraw.uml.symbols.shapes.StereotypeIconView)">visitStereotypeIconView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.StereotypeIconView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitStereotypesView(com.nomagic.magicdraw.uml.symbols.shapes.StereotypesView)">visitStereotypesView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.StereotypesView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitStereotypeView(com.nomagic.magicdraw.uml.symbols.shapes.StereotypeView)">visitStereotypeView</a><wbr/>(<a href="symbols/shapes/StereotypeView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">StereotypeView</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitStructureCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.StructureCompartmentView)">visitStructureCompartmentView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.StructureCompartmentView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitStructuredActivityNodeView(com.nomagic.magicdraw.uml.symbols.shapes.StructuredActivityNodeView)">visitStructuredActivityNodeView</a><wbr/>(<a href="symbols/shapes/StructuredActivityNodeView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">StructuredActivityNodeView</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitSwimlaneCellView(com.nomagic.magicdraw.uml.symbols.shapes.SwimlaneCellView)">visitSwimlaneCellView</a><wbr/>(<a href="symbols/shapes/SwimlaneCellView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">SwimlaneCellView</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitSwimlaneHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.SwimlaneHeaderView)">visitSwimlaneHeaderView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.SwimlaneHeaderView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitSwimlaneView(com.nomagic.magicdraw.uml.symbols.shapes.SwimlaneView)">visitSwimlaneView</a><wbr/>(<a href="symbols/shapes/SwimlaneView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">SwimlaneView</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitTableCellView(com.nomagic.magicdraw.uml.symbols.shapes.TableCellView)">visitTableCellView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.TableCellView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitTableShapeView(com.nomagic.magicdraw.uml.symbols.shapes.TableShapeView)">visitTableShapeView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.TableShapeView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitTaggedValuesCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.TaggedValuesCompartmentView)">visitTaggedValuesCompartmentView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.TaggedValuesCompartmentView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitTaggedValuesView(com.nomagic.magicdraw.uml.symbols.shapes.TaggedValuesView)">visitTaggedValuesView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.TaggedValuesView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitTemplateBindingView(com.nomagic.magicdraw.uml.symbols.paths.TemplateBindingView)">visitTemplateBindingView</a><wbr/>(<a href="symbols/paths/TemplateBindingView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">TemplateBindingView</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitTemplateSignatureView(com.nomagic.magicdraw.uml.symbols.shapes.TemplateSignatureView)">visitTemplateSignatureView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.TemplateSignatureView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitTestRegionView(com.nomagic.magicdraw.uml.symbols.shapes.ClauseView.TestRegionView)">visitTestRegionView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.ClauseView.TestRegionView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitTestRegionView(com.nomagic.magicdraw.uml.symbols.shapes.LoopNodeView.TestRegionView)">visitTestRegionView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.LoopNodeView.TestRegionView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitTextAreaCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.TextAreaCompartmentView)">visitTextAreaCompartmentView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.TextAreaCompartmentView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitTextAreaView(com.nomagic.magicdraw.uml.symbols.shapes.TextAreaView)">visitTextAreaView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.TextAreaView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitTextBoxView(com.nomagic.magicdraw.uml.symbols.shapes.TextBoxView)">visitTextBoxView</a><wbr/>(<a href="symbols/shapes/TextBoxView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">TextBoxView</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitTextBoxWithIconView(com.nomagic.magicdraw.uml.symbols.shapes.TextBoxWithIconView)">visitTextBoxWithIconView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.TextBoxWithIconView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitTextObject(com.nomagic.magicdraw.uml.symbols.shapes.TextObject)">visitTextObject</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.TextObject o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitTextShapeView(com.nomagic.magicdraw.uml.symbols.shapes.TextShapeView)">visitTextShapeView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.TextShapeView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitTextView(com.nomagic.magicdraw.uml.symbols.shapes.TextView)">visitTextView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.TextView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitTimeConstraintView(com.nomagic.magicdraw.uml.symbols.paths.TimeConstraintView)">visitTimeConstraintView</a><wbr/>(<a href="symbols/paths/TimeConstraintView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">TimeConstraintView</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitTransitionLabelView(com.nomagic.magicdraw.uml.symbols.shapes.TransitionLabelView)">visitTransitionLabelView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.TransitionLabelView transitionLabelView)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitTransitionToSelfView(com.nomagic.magicdraw.uml.symbols.shapes.TransitionToSelfView)">visitTransitionToSelfView</a><wbr/>(<a href="symbols/shapes/TransitionToSelfView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">TransitionToSelfView</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitTransitionView(com.nomagic.magicdraw.uml.symbols.paths.TransitionView)">visitTransitionView</a><wbr/>(<a href="symbols/paths/TransitionView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">TransitionView</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitTreeView(com.nomagic.magicdraw.uml.symbols.shapes.TreeView)">visitTreeView</a><wbr/>(<a href="symbols/shapes/TreeView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">TreeView</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitTriggerLabelView(com.nomagic.magicdraw.uml.symbols.shapes.TriggerLabelView)">visitTriggerLabelView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.TriggerLabelView triggerLabelView)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitTypedElementHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.TypedElementHeaderView)">visitTypedElementHeaderView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.TypedElementHeaderView o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitTypedElementView(com.nomagic.magicdraw.uml.symbols.shapes.TypedElementView)">visitTypedElementView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.TypedElementView o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitTypedElementWithLabels(com.nomagic.magicdraw.uml.symbols.shapes.TypedElementWithLabels)">visitTypedElementWithLabels</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.TypedElementWithLabels o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitUsageView(com.nomagic.magicdraw.uml.symbols.paths.UsageView)">visitUsageView</a><wbr/>(<a href="symbols/paths/UsageView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">UsageView</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitUseCaseView(com.nomagic.magicdraw.uml.symbols.shapes.UseCaseView)">visitUseCaseView</a><wbr/>(<a href="symbols/shapes/UseCaseView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">UseCaseView</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitVirtualRelation(com.nomagic.magicdraw.uml.symbols.paths.VirtualRelationView)">visitVirtualRelation</a><wbr/>(<a href="symbols/paths/VirtualRelationView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">VirtualRelationView</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
</div>
</div>
</div>
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
<section class="detail" id="visitDiagramPresentationElement(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement)">
<h3>visitDiagramPresentationElement</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitDiagramPresentationElement</span><wbr/><span class="parameters">(<a href="symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a> o)</span>
                                      throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Method visits given object.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>o</code> - object to visit.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitAbstractDiagramPresentationElement(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">
<h3>visitAbstractDiagramPresentationElement</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitAbstractDiagramPresentationElement</span><wbr/><span class="parameters">(<a href="symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> o)</span>
                                              throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Method visits given object.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>o</code> - object to visit.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>visitPresentationElement</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitPresentationElement</span><wbr/><span class="parameters">(<a href="symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> o)</span>
                               throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Method visits given object.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>o</code> - object to visit.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitCollaborationView(com.nomagic.magicdraw.uml.symbols.shapes.CollaborationView)">
<h3>visitCollaborationView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitCollaborationView</span><wbr/><span class="parameters">(<a href="symbols/shapes/CollaborationView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">CollaborationView</a> o)</span>
                             throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitObjectNodeView(com.nomagic.magicdraw.uml.symbols.shapes.ObjectNodeView)">
<h3>visitObjectNodeView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitObjectNodeView</span><wbr/><span class="parameters">(<a href="symbols/shapes/ObjectNodeView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ObjectNodeView</a> o)</span>
                          throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitAbstractHeaderShapeView(com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView)">
<h3>visitAbstractHeaderShapeView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitAbstractHeaderShapeView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView o)</span>
                                   throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitBaseHeaderShapeView(com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView)">
<h3>visitBaseHeaderShapeView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitBaseHeaderShapeView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView o)</span>
                               throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitHeaderShapeView(com.nomagic.magicdraw.uml.symbols.shapes.HeaderShapeView)">
<h3>visitHeaderShapeView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitHeaderShapeView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.HeaderShapeView o)</span>
                           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitBaseHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderView)">
<h3>visitBaseHeaderView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitBaseHeaderView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderView o)</span>
                          throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitNodeInstanceSpecificationView(com.nomagic.magicdraw.uml.symbols.shapes.NodeInstanceSpecificationView)">
<h3>visitNodeInstanceSpecificationView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitNodeInstanceSpecificationView</span><wbr/><span class="parameters">(<a href="symbols/shapes/NodeInstanceSpecificationView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">NodeInstanceSpecificationView</a> o)</span>
                                         throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitLinkWithStereotype(com.nomagic.magicdraw.uml.symbols.paths.LinkWithStereotype)">
<h3>visitLinkWithStereotype</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitLinkWithStereotype</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.paths.LinkWithStereotype o)</span>
                              throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitSplitView(com.nomagic.magicdraw.uml.symbols.shapes.SplitView)">
<h3>visitSplitView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitSplitView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.SplitView o)</span>
                     throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitLifelineView(com.nomagic.magicdraw.uml.symbols.shapes.LifelineView)">
<h3>visitLifelineView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitLifelineView</span><wbr/><span class="parameters">(<a href="symbols/shapes/LifelineView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">LifelineView</a> o)</span>
                        throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTypedElementView(com.nomagic.magicdraw.uml.symbols.shapes.TypedElementView)">
<h3>visitTypedElementView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitTypedElementView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.TypedElementView o)</span>
                            throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitRegionView(com.nomagic.magicdraw.uml.symbols.shapes.RegionView)">
<h3>visitRegionView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitRegionView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.RegionView o)</span>
                      throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitSimpleActivityRegionView(com.nomagic.magicdraw.uml.symbols.shapes.SimpleActivityRegionView)">
<h3>visitSimpleActivityRegionView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitSimpleActivityRegionView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.SimpleActivityRegionView o)</span>
                                    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTestRegionView(com.nomagic.magicdraw.uml.symbols.shapes.LoopNodeView.TestRegionView)">
<h3>visitTestRegionView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitTestRegionView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.LoopNodeView.TestRegionView o)</span>
                          throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitBodyRegionView(com.nomagic.magicdraw.uml.symbols.shapes.LoopNodeView.BodyRegionView)">
<h3>visitBodyRegionView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitBodyRegionView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.LoopNodeView.BodyRegionView o)</span>
                          throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitSetupRegionView(com.nomagic.magicdraw.uml.symbols.shapes.LoopNodeView.SetupRegionView)">
<h3>visitSetupRegionView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitSetupRegionView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.LoopNodeView.SetupRegionView o)</span>
                           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTestRegionView(com.nomagic.magicdraw.uml.symbols.shapes.ClauseView.TestRegionView)">
<h3>visitTestRegionView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitTestRegionView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.ClauseView.TestRegionView o)</span>
                          throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitBodyRegionView(com.nomagic.magicdraw.uml.symbols.shapes.ClauseView.BodyRegionView)">
<h3>visitBodyRegionView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitBodyRegionView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.ClauseView.BodyRegionView o)</span>
                          throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitElseRegionView(com.nomagic.magicdraw.uml.symbols.shapes.ClauseView.ElseRegionView)">
<h3>visitElseRegionView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitElseRegionView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.ClauseView.ElseRegionView o)</span>
                          throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitClauseView(com.nomagic.magicdraw.uml.symbols.shapes.ClauseView)">
<h3>visitClauseView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitClauseView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.ClauseView o)</span>
                      throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTemplateBindingView(com.nomagic.magicdraw.uml.symbols.paths.TemplateBindingView)">
<h3>visitTemplateBindingView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitTemplateBindingView</span><wbr/><span class="parameters">(<a href="symbols/paths/TemplateBindingView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">TemplateBindingView</a> o)</span>
                               throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitBaseMembersCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.BaseMembersCompartmentView)">
<h3>visitBaseMembersCompartmentView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitBaseMembersCompartmentView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.BaseMembersCompartmentView o)</span>
                                      throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitBaseCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.BaseCompartmentView)">
<h3>visitBaseCompartmentView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitBaseCompartmentView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.BaseCompartmentView o)</span>
                               throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitAbstractBaseCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.AbstractCompartmentView)">
<h3>visitAbstractBaseCompartmentView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitAbstractBaseCompartmentView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.AbstractCompartmentView o)</span>
                                       throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitAbstractSeparatorView(com.nomagic.magicdraw.uml.symbols.shapes.AbstractSeparatorView)">
<h3>visitAbstractSeparatorView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitAbstractSeparatorView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.AbstractSeparatorView o)</span>
                                 throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitSeparatorView(com.nomagic.magicdraw.uml.symbols.shapes.SeparatorView)">
<h3>visitSeparatorView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitSeparatorView</span><wbr/><span class="parameters">(<a href="symbols/shapes/SeparatorView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">SeparatorView</a> o)</span>
                         throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitRectangularShape(com.nomagic.magicdraw.uml.symbols.shapes.RectangularShape)">
<h3>visitRectangularShape</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitRectangularShape</span><wbr/><span class="parameters">(<a href="symbols/shapes/RectangularShape.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">RectangularShape</a> o)</span>
                            throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitListElementView(com.nomagic.magicdraw.uml.symbols.shapes.ListElementView)">
<h3>visitListElementView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitListElementView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.ListElementView o)</span>
                           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitLegendItemView(com.nomagic.magicdraw.uml.symbols.shapes.LegendItemView)">
<h3>visitLegendItemView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitLegendItemView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.LegendItemView o)</span>
                          throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitElementWithIconView(com.nomagic.magicdraw.uml.symbols.shapes.ElementWithIconView)">
<h3>visitElementWithIconView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitElementWithIconView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.ElementWithIconView o)</span>
                               throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitImageView(com.nomagic.magicdraw.uml.symbols.shapes.ImageView)">
<h3>visitImageView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitImageView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.ImageView o)</span>
                     throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInnerElementsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.InnerElementsCompartmentView)">
<h3>visitInnerElementsCompartmentView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitInnerElementsCompartmentView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.InnerElementsCompartmentView o)</span>
                                        throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitConstraintsView(com.nomagic.magicdraw.uml.symbols.shapes.ConstraintsView)">
<h3>visitConstraintsView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitConstraintsView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.ConstraintsView o)</span>
                           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitStereotypesView(com.nomagic.magicdraw.uml.symbols.shapes.StereotypesView)">
<h3>visitStereotypesView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitStereotypesView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.StereotypesView o)</span>
                           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitElementPropertiesCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.ElementPropertiesCompartmentView)">
<h3>visitElementPropertiesCompartmentView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitElementPropertiesCompartmentView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.ElementPropertiesCompartmentView o)</span>
                                            throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitConveyedInformationView(com.nomagic.magicdraw.uml.symbols.shapes.ConveyedInformationView)">
<h3>visitConveyedInformationView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitConveyedInformationView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.ConveyedInformationView o)</span>
                                   throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTaggedValuesView(com.nomagic.magicdraw.uml.symbols.shapes.TaggedValuesView)">
<h3>visitTaggedValuesView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitTaggedValuesView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.TaggedValuesView o)</span>
                            throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitExtensionPointView(com.nomagic.magicdraw.uml.symbols.shapes.ExtensionPointView)">
<h3>visitExtensionPointView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitExtensionPointView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.ExtensionPointView o)</span>
                              throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTextAreaCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.TextAreaCompartmentView)">
<h3>visitTextAreaCompartmentView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitTextAreaCompartmentView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.TextAreaCompartmentView o)</span>
                                   throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitRequiredProvidedCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.RequiredProvidedInterfacesCompartmentView)">
<h3>visitRequiredProvidedCompartmentView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitRequiredProvidedCompartmentView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.RequiredProvidedInterfacesCompartmentView o)</span>
                                           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitProjectOptions(com.nomagic.magicdraw.core.options.ProjectOptions)">
<h3>visitProjectOptions</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitProjectOptions</span><wbr/><span class="parameters">(<a href="../core/options/ProjectOptions.html" title="class in com.nomagic.magicdraw.core.options">ProjectOptions</a> o)</span>
                          throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPresentationElementContainer(com.nomagic.magicdraw.uml.symbols.PresentationElementContainer)">
<h3>visitPresentationElementContainer</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitPresentationElementContainer</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.PresentationElementContainer o)</span>
                                        throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitAbstractDiagramPresentationElementContainer(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElementContainer)">
<h3>visitAbstractDiagramPresentationElementContainer</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitAbstractDiagramPresentationElementContainer</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElementContainer o)</span>
                                                       throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDiagramObjectViewContainer(com.nomagic.magicdraw.uml.symbols.DiagramObjectViewContainer)">
<h3>visitDiagramObjectViewContainer</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitDiagramObjectViewContainer</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.DiagramObjectViewContainer o)</span>
                                      throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDummyDiagramObjectViewContainer(com.nomagic.magicdraw.uml.symbols.DummyDiagramObjectViewContainer)">
<h3>visitDummyDiagramObjectViewContainer</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitDummyDiagramObjectViewContainer</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.DummyDiagramObjectViewContainer o)</span>
                                           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitAssociationView(com.nomagic.magicdraw.uml.symbols.paths.AssociationView)">
<h3>visitAssociationView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitAssociationView</span><wbr/><span class="parameters">(<a href="symbols/paths/AssociationView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">AssociationView</a> o)</span>
                           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitCommunicationPathView(com.nomagic.magicdraw.uml.symbols.paths.CommunicationPathView)">
<h3>visitCommunicationPathView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitCommunicationPathView</span><wbr/><span class="parameters">(<a href="symbols/paths/CommunicationPathView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">CommunicationPathView</a> o)</span>
                                 throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitAssociationClassView(com.nomagic.magicdraw.uml.symbols.paths.AssociationClassView)">
<h3>visitAssociationClassView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitAssociationClassView</span><wbr/><span class="parameters">(<a href="symbols/paths/AssociationClassView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">AssociationClassView</a> o)</span>
                                throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitConstraintLinkView(com.nomagic.magicdraw.uml.symbols.paths.ConstraintLinkView)">
<h3>visitConstraintLinkView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitConstraintLinkView</span><wbr/><span class="parameters">(<a href="symbols/paths/ConstraintLinkView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">ConstraintLinkView</a> o)</span>
                              throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitConnectorToSelfView(com.nomagic.magicdraw.uml.symbols.paths.ConnectorToSelfView)">
<h3>visitConnectorToSelfView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitConnectorToSelfView</span><wbr/><span class="parameters">(<a href="symbols/paths/ConnectorToSelfView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">ConnectorToSelfView</a> o)</span>
                               throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitLinkView(com.nomagic.magicdraw.uml.symbols.paths.LinkView)">
<h3>visitLinkView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitLinkView</span><wbr/><span class="parameters">(<a href="symbols/paths/LinkView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">LinkView</a> o)</span>
                    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitContainerLinkView(com.nomagic.magicdraw.uml.symbols.paths.ContainerLinkView)">
<h3>visitContainerLinkView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitContainerLinkView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.paths.ContainerLinkView o)</span>
                             throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDependencyView(com.nomagic.magicdraw.uml.symbols.paths.DependencyView)">
<h3>visitDependencyView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitDependencyView</span><wbr/><span class="parameters">(<a href="symbols/paths/DependencyView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">DependencyView</a> o)</span>
                          throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitRoleBindingView(com.nomagic.magicdraw.uml.symbols.paths.RoleBindingView)">
<h3>visitRoleBindingView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitRoleBindingView</span><wbr/><span class="parameters">(<a href="symbols/paths/RoleBindingView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">RoleBindingView</a> o)</span>
                           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitUsageView(com.nomagic.magicdraw.uml.symbols.paths.UsageView)">
<h3>visitUsageView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitUsageView</span><wbr/><span class="parameters">(<a href="symbols/paths/UsageView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">UsageView</a> o)</span>
                     throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDeploymentView(com.nomagic.magicdraw.uml.symbols.paths.DeploymentView)">
<h3>visitDeploymentView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitDeploymentView</span><wbr/><span class="parameters">(<a href="symbols/paths/DeploymentView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">DeploymentView</a> o)</span>
                          throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitConnectorView(com.nomagic.magicdraw.uml.symbols.paths.ConnectorView)">
<h3>visitConnectorView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitConnectorView</span><wbr/><span class="parameters">(<a href="symbols/paths/ConnectorView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">ConnectorView</a> o)</span>
                         throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPackageImportView(com.nomagic.magicdraw.uml.symbols.paths.PackageImportView)">
<h3>visitPackageImportView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitPackageImportView</span><wbr/><span class="parameters">(<a href="symbols/paths/PackageImportView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PackageImportView</a> o)</span>
                             throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitProfileApplicationView(com.nomagic.magicdraw.uml.symbols.paths.ProfileApplicationView)">
<h3>visitProfileApplicationView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitProfileApplicationView</span><wbr/><span class="parameters">(<a href="symbols/paths/ProfileApplicationView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">ProfileApplicationView</a> o)</span>
                                  throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitElementImportView(com.nomagic.magicdraw.uml.symbols.paths.ElementImportView)">
<h3>visitElementImportView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitElementImportView</span><wbr/><span class="parameters">(<a href="symbols/paths/ElementImportView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">ElementImportView</a> o)</span>
                             throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPackageMergeView(com.nomagic.magicdraw.uml.symbols.paths.PackageMergeView)">
<h3>visitPackageMergeView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitPackageMergeView</span><wbr/><span class="parameters">(<a href="symbols/paths/PackageMergeView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PackageMergeView</a> o)</span>
                            throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitExtendView(com.nomagic.magicdraw.uml.symbols.paths.ExtendView)">
<h3>visitExtendView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitExtendView</span><wbr/><span class="parameters">(<a href="symbols/paths/ExtendView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">ExtendView</a> o)</span>
                      throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitIncludeView(com.nomagic.magicdraw.uml.symbols.paths.IncludeView)">
<h3>visitIncludeView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitIncludeView</span><wbr/><span class="parameters">(<a href="symbols/paths/IncludeView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">IncludeView</a> o)</span>
                       throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitGeneralizationView(com.nomagic.magicdraw.uml.symbols.paths.GeneralizationView)">
<h3>visitGeneralizationView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitGeneralizationView</span><wbr/><span class="parameters">(<a href="symbols/paths/GeneralizationView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">GeneralizationView</a> o)</span>
                              throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitLinkAttributeView(com.nomagic.magicdraw.uml.symbols.paths.LinkAttributeView)">
<h3>visitLinkAttributeView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitLinkAttributeView</span><wbr/><span class="parameters">(<a href="symbols/paths/LinkAttributeView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">LinkAttributeView</a> o)</span>
                             throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPathConnector(com.nomagic.magicdraw.uml.symbols.paths.PathConnector)">
<h3>visitPathConnector</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitPathConnector</span><wbr/><span class="parameters">(<a href="symbols/paths/PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathConnector</a> o)</span>
                         throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Method visits given object.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>o</code> - object to visit.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">
<h3>visitPathElement</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitPathElement</span><wbr/><span class="parameters">(<a href="symbols/paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> o)</span>
                       throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Method visits given object.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>o</code> - object to visit.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitNoteAnchorView(com.nomagic.magicdraw.uml.symbols.paths.NoteAnchorView)">
<h3>visitNoteAnchorView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitNoteAnchorView</span><wbr/><span class="parameters">(<a href="symbols/paths/NoteAnchorView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">NoteAnchorView</a> o)</span>
                          throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitContainmentLinkView(com.nomagic.magicdraw.uml.symbols.paths.ContainmentLinkView)">
<h3>visitContainmentLinkView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitContainmentLinkView</span><wbr/><span class="parameters">(<a href="symbols/paths/ContainmentLinkView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">ContainmentLinkView</a> o)</span>
                               throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitVirtualRelation(com.nomagic.magicdraw.uml.symbols.paths.VirtualRelationView)">
<h3>visitVirtualRelation</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitVirtualRelation</span><wbr/><span class="parameters">(<a href="symbols/paths/VirtualRelationView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">VirtualRelationView</a> o)</span>
                           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitGenericView(com.nomagic.magicdraw.uml.symbols.shapes.GenericView)">
<h3>visitGenericView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitGenericView</span><wbr/><span class="parameters">(<a href="symbols/shapes/GenericView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">GenericView</a> o)</span>
                       throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitBaseRealizationView(com.nomagic.magicdraw.uml.symbols.paths.BaseRealizationView)">
<h3>visitBaseRealizationView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitBaseRealizationView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.paths.BaseRealizationView o)</span>
                               throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInterfaceRealizationView(com.nomagic.magicdraw.uml.symbols.paths.InterfaceRealizationView)">
<h3>visitInterfaceRealizationView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitInterfaceRealizationView</span><wbr/><span class="parameters">(<a href="symbols/paths/InterfaceRealizationView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">InterfaceRealizationView</a> o)</span>
                                    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitSeqMessageView(com.nomagic.magicdraw.uml.symbols.paths.SeqMessageView)">
<h3>visitSeqMessageView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitSeqMessageView</span><wbr/><span class="parameters">(<a href="symbols/paths/SeqMessageView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">SeqMessageView</a> o)</span>
                          throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitSeqSelfMessageView(com.nomagic.magicdraw.uml.symbols.paths.SeqSelfMessageView)">
<h3>visitSeqSelfMessageView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitSeqSelfMessageView</span><wbr/><span class="parameters">(<a href="symbols/paths/SeqSelfMessageView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">SeqSelfMessageView</a> o)</span>
                              throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTransitionView(com.nomagic.magicdraw.uml.symbols.paths.TransitionView)">
<h3>visitTransitionView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitTransitionView</span><wbr/><span class="parameters">(<a href="symbols/paths/TransitionView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">TransitionView</a> o)</span>
                          throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitExceptionHandlerView(com.nomagic.magicdraw.uml.symbols.paths.ExceptionHandlerView)">
<h3>visitExceptionHandlerView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitExceptionHandlerView</span><wbr/><span class="parameters">(<a href="symbols/paths/ExceptionHandlerView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">ExceptionHandlerView</a> o)</span>
                                throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTransitionToSelfView(com.nomagic.magicdraw.uml.symbols.shapes.TransitionToSelfView)">
<h3>visitTransitionToSelfView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitTransitionToSelfView</span><wbr/><span class="parameters">(<a href="symbols/shapes/TransitionToSelfView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">TransitionToSelfView</a> o)</span>
                                throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTimeConstraintView(com.nomagic.magicdraw.uml.symbols.paths.TimeConstraintView)">
<h3>visitTimeConstraintView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitTimeConstraintView</span><wbr/><span class="parameters">(<a href="symbols/paths/TimeConstraintView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">TimeConstraintView</a> o)</span>
                              throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDurationConstraintView(com.nomagic.magicdraw.uml.symbols.paths.DurationConstraintView)">
<h3>visitDurationConstraintView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitDurationConstraintView</span><wbr/><span class="parameters">(<a href="symbols/paths/DurationConstraintView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">DurationConstraintView</a> o)</span>
                                  throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPathToSelfShape(com.nomagic.magicdraw.uml.symbols.shapes.PathToSelfShape)">
<h3>visitPathToSelfShape</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitPathToSelfShape</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.PathToSelfShape o)</span>
                           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitActivationView(com.nomagic.magicdraw.uml.symbols.shapes.ActivationView)">
<h3>visitActivationView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitActivationView</span><wbr/><span class="parameters">(<a href="symbols/shapes/ActivationView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ActivationView</a> o)</span>
                          throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitBarView(com.nomagic.magicdraw.uml.symbols.shapes.BarView)">
<h3>visitBarView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitBarView</span><wbr/><span class="parameters">(<a href="symbols/shapes/BarView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">BarView</a> o)</span>
                   throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitAttributeView(com.nomagic.magicdraw.uml.symbols.shapes.AttributeView)">
<h3>visitAttributeView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitAttributeView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.AttributeView o)</span>
                         throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPortAttributeView(com.nomagic.magicdraw.uml.symbols.shapes.PortAttributeView)">
<h3>visitPortAttributeView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitPortAttributeView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.PortAttributeView o)</span>
                             throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitMemberView(com.nomagic.magicdraw.uml.symbols.shapes.MemberView)">
<h3>visitMemberView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitMemberView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.MemberView o)</span>
                      throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitBehavioralFeatureView(com.nomagic.magicdraw.uml.symbols.shapes.BehavioralFeatureView)">
<h3>visitBehavioralFeatureView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitBehavioralFeatureView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.BehavioralFeatureView o)</span>
                                 throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitClassView(com.nomagic.magicdraw.uml.symbols.shapes.ClassView)">
<h3>visitClassView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitClassView</span><wbr/><span class="parameters">(<a href="symbols/shapes/ClassView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ClassView</a> o)</span>
                     throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInterfaceView(com.nomagic.magicdraw.uml.symbols.shapes.InterfaceView)">
<h3>visitInterfaceView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitInterfaceView</span><wbr/><span class="parameters">(<a href="symbols/shapes/InterfaceView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">InterfaceView</a> o)</span>
                         throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitSignalView(com.nomagic.magicdraw.uml.symbols.shapes.SignalView)">
<h3>visitSignalView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitSignalView</span><wbr/><span class="parameters">(<a href="symbols/shapes/SignalView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">SignalView</a> o)</span>
                      throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitActorView(com.nomagic.magicdraw.uml.symbols.shapes.ActorView)">
<h3>visitActorView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitActorView</span><wbr/><span class="parameters">(<a href="symbols/shapes/ActorView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ActorView</a> o)</span>
                     throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDataTypeView(com.nomagic.magicdraw.uml.symbols.shapes.DataTypeView)">
<h3>visitDataTypeView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitDataTypeView</span><wbr/><span class="parameters">(<a href="symbols/shapes/DataTypeView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">DataTypeView</a> o)</span>
                        throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPrimitiveTypeView(com.nomagic.magicdraw.uml.symbols.shapes.PrimitiveTypeView)">
<h3>visitPrimitiveTypeView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitPrimitiveTypeView</span><wbr/><span class="parameters">(<a href="symbols/shapes/PrimitiveTypeView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">PrimitiveTypeView</a> o)</span>
                             throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitStereotypeView(com.nomagic.magicdraw.uml.symbols.shapes.StereotypeView)">
<h3>visitStereotypeView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitStereotypeView</span><wbr/><span class="parameters">(<a href="symbols/shapes/StereotypeView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">StereotypeView</a> o)</span>
                          throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitClassifierView(com.nomagic.magicdraw.uml.symbols.shapes.ClassifierView)">
<h3>visitClassifierView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitClassifierView</span><wbr/><span class="parameters">(<a href="symbols/shapes/ClassifierView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ClassifierView</a> o)</span>
                          throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitClassifierHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.ClassifierHeaderView)">
<h3>visitClassifierHeaderView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitClassifierHeaderView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.ClassifierHeaderView o)</span>
                                throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitEnumerationView(com.nomagic.magicdraw.uml.symbols.shapes.EnumerationView)">
<h3>visitEnumerationView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitEnumerationView</span><wbr/><span class="parameters">(<a href="symbols/shapes/EnumerationView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">EnumerationView</a> o)</span>
                           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitArtifactView(com.nomagic.magicdraw.uml.symbols.shapes.ArtifactView)">
<h3>visitArtifactView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitArtifactView</span><wbr/><span class="parameters">(<a href="symbols/shapes/ArtifactView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ArtifactView</a> o)</span>
                        throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInstanceSpecificationView(com.nomagic.magicdraw.uml.symbols.shapes.InstanceSpecificationView)">
<h3>visitInstanceSpecificationView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitInstanceSpecificationView</span><wbr/><span class="parameters">(<a href="symbols/shapes/InstanceSpecificationView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">InstanceSpecificationView</a> o)</span>
                                     throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitContainerShapeView(com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView)">
<h3>visitContainerShapeView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitContainerShapeView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView o)</span>
                              throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDecisionView(com.nomagic.magicdraw.uml.symbols.shapes.DecisionView)">
<h3>visitDecisionView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitDecisionView</span><wbr/><span class="parameters">(<a href="symbols/shapes/DecisionView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">DecisionView</a> o)</span>
                        throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitBaseTreeShape(com.nomagic.magicdraw.uml.symbols.shapes.BaseTreeShape)">
<h3>visitBaseTreeShape</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitBaseTreeShape</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.BaseTreeShape o)</span>
                         throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTreeView(com.nomagic.magicdraw.uml.symbols.shapes.TreeView)">
<h3>visitTreeView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitTreeView</span><wbr/><span class="parameters">(<a href="symbols/shapes/TreeView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">TreeView</a> o)</span>
                    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitLifeLineLineView(com.nomagic.magicdraw.uml.symbols.shapes.LifeLineLineView)">
<h3>visitLifeLineLineView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitLifeLineLineView</span><wbr/><span class="parameters">(<a href="symbols/shapes/LifeLineLineView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">LifeLineLineView</a> o)</span>
                            throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitMessageView(com.nomagic.magicdraw.uml.symbols.shapes.MessageView)">
<h3>visitMessageView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitMessageView</span><wbr/><span class="parameters">(<a href="symbols/shapes/MessageView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">MessageView</a> o)</span>
                       throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitOperationView(com.nomagic.magicdraw.uml.symbols.shapes.OperationView)">
<h3>visitOperationView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitOperationView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.OperationView o)</span>
                         throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitReceptionView(com.nomagic.magicdraw.uml.symbols.shapes.ReceptionView)">
<h3>visitReceptionView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitReceptionView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.ReceptionView o)</span>
                         throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitReceptionsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.ReceptionsCompartmentView)">
<h3>visitReceptionsCompartmentView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitReceptionsCompartmentView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.ReceptionsCompartmentView o)</span>
                                     throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitNoteView(com.nomagic.magicdraw.uml.symbols.shapes.NoteView)">
<h3>visitNoteView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitNoteView</span><wbr/><span class="parameters">(<a href="symbols/shapes/NoteView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">NoteView</a> o)</span>
                    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitMessageSignatureView(com.nomagic.magicdraw.uml.symbols.shapes.MessageSignatureView)">
<h3>visitMessageSignatureView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitMessageSignatureView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.MessageSignatureView o)</span>
                                throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPackageView(com.nomagic.magicdraw.uml.symbols.shapes.PackageView)">
<h3>visitPackageView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitPackageView</span><wbr/><span class="parameters">(<a href="symbols/shapes/PackageView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">PackageView</a> o)</span>
                       throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitRoleView(com.nomagic.magicdraw.uml.symbols.shapes.RoleView)">
<h3>visitRoleView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitRoleView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.RoleView o)</span>
                    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitAbstractPathEndShape(com.nomagic.magicdraw.uml.symbols.shapes.AbstractPathEndShape)">
<h3>visitAbstractPathEndShape</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitAbstractPathEndShape</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.AbstractPathEndShape o)</span>
                                throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitLinkEndView(com.nomagic.magicdraw.uml.symbols.shapes.LinkEndView)">
<h3>visitLinkEndView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitLinkEndView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.LinkEndView o)</span>
                       throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitConnectorEndView(com.nomagic.magicdraw.uml.symbols.shapes.ConnectorEndView)">
<h3>visitConnectorEndView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitConnectorEndView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.ConnectorEndView o)</span>
                            throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitNNaryAssociationView(com.nomagic.magicdraw.uml.symbols.shapes.NNaryAssociationView)">
<h3>visitNNaryAssociationView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitNNaryAssociationView</span><wbr/><span class="parameters">(<a href="symbols/shapes/NNaryAssociationView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">NNaryAssociationView</a> o)</span>
                                throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitSequenceLifelineView(com.nomagic.magicdraw.uml.symbols.shapes.SequenceLifelineView)">
<h3>visitSequenceLifelineView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitSequenceLifelineView</span><wbr/><span class="parameters">(<a href="symbols/shapes/SequenceLifelineView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">SequenceLifelineView</a> o)</span>
                                throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitShapeElement(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement)">
<h3>visitShapeElement</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitShapeElement</span><wbr/><span class="parameters">(<a href="symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> o)</span>
                        throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Method visits given object.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>o</code> - object to visit.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitQualifiersView(com.nomagic.magicdraw.uml.symbols.shapes.QualifiersView)">
<h3>visitQualifiersView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitQualifiersView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.QualifiersView o)</span>
                          throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTextAreaView(com.nomagic.magicdraw.uml.symbols.shapes.TextAreaView)">
<h3>visitTextAreaView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitTextAreaView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.TextAreaView o)</span>
                        throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitAbstractTextBoxView(com.nomagic.magicdraw.uml.symbols.shapes.AbstractTextBoxView)">
<h3>visitAbstractTextBoxView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitAbstractTextBoxView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.AbstractTextBoxView o)</span>
                               throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTextBoxView(com.nomagic.magicdraw.uml.symbols.shapes.TextBoxView)">
<h3>visitTextBoxView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitTextBoxView</span><wbr/><span class="parameters">(<a href="symbols/shapes/TextBoxView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">TextBoxView</a> o)</span>
                       throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTextBoxWithIconView(com.nomagic.magicdraw.uml.symbols.shapes.TextBoxWithIconView)">
<h3>visitTextBoxWithIconView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitTextBoxWithIconView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.TextBoxWithIconView o)</span>
                               throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTextObject(com.nomagic.magicdraw.uml.symbols.shapes.TextObject)">
<h3>visitTextObject</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitTextObject</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.TextObject o)</span>
                      throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTextShapeView(com.nomagic.magicdraw.uml.symbols.shapes.TextShapeView)">
<h3>visitTextShapeView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitTextShapeView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.TextShapeView o)</span>
                         throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTextView(com.nomagic.magicdraw.uml.symbols.shapes.TextView)">
<h3>visitTextView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitTextView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.TextView o)</span>
                    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitUseCaseView(com.nomagic.magicdraw.uml.symbols.shapes.UseCaseView)">
<h3>visitUseCaseView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitUseCaseView</span><wbr/><span class="parameters">(<a href="symbols/shapes/UseCaseView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">UseCaseView</a> o)</span>
                       throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitSeqBaseMessageView(com.nomagic.magicdraw.uml.symbols.paths.SeqBaseMessageView)">
<h3>visitSeqBaseMessageView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitSeqBaseMessageView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.paths.SeqBaseMessageView o)</span>
                              throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitSequenceObjectViewContainer(com.nomagic.magicdraw.uml.symbols.SequenceObjectViewContainer)">
<h3>visitSequenceObjectViewContainer</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitSequenceObjectViewContainer</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.SequenceObjectViewContainer o)</span>
                                       throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPseudoStateView(com.nomagic.magicdraw.uml.symbols.shapes.PseudoStateView)">
<h3>visitPseudoStateView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitPseudoStateView</span><wbr/><span class="parameters">(<a href="symbols/shapes/PseudoStateView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">PseudoStateView</a> o)</span>
                           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPseudoNodeView(com.nomagic.magicdraw.uml.symbols.shapes.PseudoNodeView)">
<h3>visitPseudoNodeView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitPseudoNodeView</span><wbr/><span class="parameters">(<a href="symbols/shapes/PseudoNodeView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">PseudoNodeView</a> o)</span>
                          throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitStateView(com.nomagic.magicdraw.uml.symbols.shapes.StateView)">
<h3>visitStateView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitStateView</span><wbr/><span class="parameters">(<a href="symbols/shapes/StateView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">StateView</a> o)</span>
                     throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitStateObjectViewContainer(com.nomagic.magicdraw.uml.symbols.StateObjectViewContainer)">
<h3>visitStateObjectViewContainer</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitStateObjectViewContainer</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.StateObjectViewContainer o)</span>
                                    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitActivityObjectViewContainer(com.nomagic.magicdraw.uml.symbols.ActivityObjectViewContainer)">
<h3>visitActivityObjectViewContainer</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitActivityObjectViewContainer</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.ActivityObjectViewContainer o)</span>
                                       throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitComponentView(com.nomagic.magicdraw.uml.symbols.shapes.ComponentView)">
<h3>visitComponentView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitComponentView</span><wbr/><span class="parameters">(<a href="symbols/shapes/ComponentView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ComponentView</a> o)</span>
                         throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitNodeView(com.nomagic.magicdraw.uml.symbols.shapes.NodeView)">
<h3>visitNodeView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitNodeView</span><wbr/><span class="parameters">(<a href="symbols/shapes/NodeView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">NodeView</a> o)</span>
                    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitRealizationView(com.nomagic.magicdraw.uml.symbols.paths.RealizationView)">
<h3>visitRealizationView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitRealizationView</span><wbr/><span class="parameters">(<a href="symbols/paths/RealizationView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">RealizationView</a> o)</span>
                           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitStereotypeIconView(com.nomagic.magicdraw.uml.symbols.shapes.StereotypeIconView)">
<h3>visitStereotypeIconView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitStereotypeIconView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.StereotypeIconView o)</span>
                              throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTemplateSignatureView(com.nomagic.magicdraw.uml.symbols.shapes.TemplateSignatureView)">
<h3>visitTemplateSignatureView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitTemplateSignatureView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.TemplateSignatureView o)</span>
                                 throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitHeaderOfBaseHeaderShapeView(com.nomagic.magicdraw.uml.symbols.shapes.HeaderOfBaseHeaderShapeView)">
<h3>visitHeaderOfBaseHeaderShapeView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitHeaderOfBaseHeaderShapeView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.HeaderOfBaseHeaderShapeView o)</span>
                                       throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.HeaderView)">
<h3>visitHeaderView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitHeaderView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.HeaderView o)</span>
                      throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitEnumerationHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.EnumerationHeaderView)">
<h3>visitEnumerationHeaderView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitEnumerationHeaderView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.EnumerationHeaderView o)</span>
                                 throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitComponentHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.ComponentHeaderView)">
<h3>visitComponentHeaderView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitComponentHeaderView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.ComponentHeaderView o)</span>
                               throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitNodeHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.NodeHeaderView)">
<h3>visitNodeHeaderView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitNodeHeaderView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.NodeHeaderView o)</span>
                          throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitEnumerationLiteralView(com.nomagic.magicdraw.uml.symbols.shapes.EnumerationLiteralView)">
<h3>visitEnumerationLiteralView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitEnumerationLiteralView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.EnumerationLiteralView o)</span>
                                  throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitBehaviorView(com.nomagic.magicdraw.uml.symbols.shapes.BehaviorView)">
<h3>visitBehaviorView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitBehaviorView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.BehaviorView o)</span>
                        throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitEnumerationLiteralsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.EnumerationLiteralsCompartmentView)">
<h3>visitEnumerationLiteralsCompartmentView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitEnumerationLiteralsCompartmentView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.EnumerationLiteralsCompartmentView o)</span>
                                              throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitBehaviorsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.BehaviorsCompartmentView)">
<h3>visitBehaviorsCompartmentView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitBehaviorsCompartmentView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.BehaviorsCompartmentView o)</span>
                                    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitAttributesCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.AttributesCompartmentView)">
<h3>visitAttributesCompartmentView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitAttributesCompartmentView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.AttributesCompartmentView o)</span>
                                     throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPortsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.PortsCompartmentView)">
<h3>visitPortsCompartmentView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitPortsCompartmentView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.PortsCompartmentView o)</span>
                                throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitBasePropertiesCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.BasePropertiesCompartmentView)">
<h3>visitBasePropertiesCompartmentView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitBasePropertiesCompartmentView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.BasePropertiesCompartmentView o)</span>
                                         throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitStructureCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.StructureCompartmentView)">
<h3>visitStructureCompartmentView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitStructureCompartmentView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.StructureCompartmentView o)</span>
                                    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDiagramOverviewCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.DiagramOverviewCompartmentView)">
<h3>visitDiagramOverviewCompartmentView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitDiagramOverviewCompartmentView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.DiagramOverviewCompartmentView o)</span>
                                          throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitOperationsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.OperationsCompartmentView)">
<h3>visitOperationsCompartmentView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitOperationsCompartmentView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.OperationsCompartmentView o)</span>
                                     throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitAssociationTextBoxView(com.nomagic.magicdraw.uml.symbols.shapes.AssociationTextBoxView)">
<h3>visitAssociationTextBoxView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitAssociationTextBoxView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.AssociationTextBoxView o)</span>
                                  throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitSignalActionView(com.nomagic.magicdraw.uml.symbols.shapes.SignalActionView)">
<h3>visitSignalActionView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitSignalActionView</span><wbr/><span class="parameters">(<a href="symbols/shapes/SignalActionView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">SignalActionView</a> o)</span>
                            throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitSlotView(com.nomagic.magicdraw.uml.symbols.shapes.SlotView)">
<h3>visitSlotView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitSlotView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.SlotView o)</span>
                    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPrimitiveValueView(com.nomagic.magicdraw.uml.symbols.shapes.PrimitiveValueView)">
<h3>visitPrimitiveValueView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitPrimitiveValueView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.PrimitiveValueView view)</span>
                              throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitCommentView(com.nomagic.magicdraw.uml.symbols.shapes.CommentView)">
<h3>visitCommentView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitCommentView</span><wbr/><span class="parameters">(<a href="symbols/shapes/CommentView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">CommentView</a> o)</span>
                       throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitCompartmentElement(com.nomagic.magicdraw.uml.CompartmentElement)">
<h3>visitCompartmentElement</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitCompartmentElement</span><wbr/><span class="parameters">(<a href="CompartmentElement.html" title="interface in com.nomagic.magicdraw.uml">CompartmentElement</a> o)</span>
                              throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Method visitCompartmentElement.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>o</code> - </dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitContentShape(com.nomagic.magicdraw.uml.symbols.shapes.ContentShape)">
<h3>visitContentShape</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitContentShape</span><wbr/><span class="parameters">(<a href="symbols/shapes/ContentShape.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ContentShape</a> o)</span>
                        throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDiagramShape(com.nomagic.magicdraw.uml.symbols.shapes.DiagramShape)">
<h3>visitDiagramShape</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitDiagramShape</span><wbr/><span class="parameters">(<a href="symbols/shapes/DiagramShape.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">DiagramShape</a> o)</span>
                        throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDiagramPropertiesShape(com.nomagic.magicdraw.uml.symbols.shapes.DiagramPropertiesShape)">
<h3>visitDiagramPropertiesShape</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitDiagramPropertiesShape</span><wbr/><span class="parameters">(<a href="symbols/shapes/DiagramPropertiesShape.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">DiagramPropertiesShape</a> o)</span>
                                  throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDiagramLegendShape(com.nomagic.magicdraw.uml.symbols.shapes.DiagramLegendShape)">
<h3>visitDiagramLegendShape</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitDiagramLegendShape</span><wbr/><span class="parameters">(<a href="symbols/shapes/DiagramLegendShape.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">DiagramLegendShape</a> o)</span>
                              throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitAbstractShapeWithLabelsInside(com.nomagic.magicdraw.uml.symbols.shapes.AbstractShapeWithLabelsInside)">
<h3>visitAbstractShapeWithLabelsInside</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitAbstractShapeWithLabelsInside</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.AbstractShapeWithLabelsInside o)</span>
                                         throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTypedElementWithLabels(com.nomagic.magicdraw.uml.symbols.shapes.TypedElementWithLabels)">
<h3>visitTypedElementWithLabels</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitTypedElementWithLabels</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.TypedElementWithLabels o)</span>
                                  throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPortView(com.nomagic.magicdraw.uml.symbols.shapes.PortView)">
<h3>visitPortView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitPortView</span><wbr/><span class="parameters">(<a href="symbols/shapes/PortView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">PortView</a> o)</span>
                    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPinView(com.nomagic.magicdraw.uml.symbols.shapes.PinView)">
<h3>visitPinView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitPinView</span><wbr/><span class="parameters">(<a href="symbols/shapes/PinView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">PinView</a> o)</span>
                   throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitExpansionNodeView(com.nomagic.magicdraw.uml.symbols.shapes.ExpansionNodeView)">
<h3>visitExpansionNodeView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitExpansionNodeView</span><wbr/><span class="parameters">(<a href="symbols/shapes/ExpansionNodeView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ExpansionNodeView</a> o)</span>
                             throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitAbstractShapeWithLabels(com.nomagic.magicdraw.uml.symbols.shapes.AbstractShapeWithLabels)">
<h3>visitAbstractShapeWithLabels</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitAbstractShapeWithLabels</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.AbstractShapeWithLabels o)</span>
                                   throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitShapeWithLabels(com.nomagic.magicdraw.uml.symbols.shapes.ShapeWithLabels)">
<h3>visitShapeWithLabels</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitShapeWithLabels</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.ShapeWithLabels o)</span>
                           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitFlowConnectorView(com.nomagic.magicdraw.uml.symbols.shapes.FlowConnectorView)">
<h3>visitFlowConnectorView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitFlowConnectorView</span><wbr/><span class="parameters">(<a href="symbols/shapes/FlowConnectorView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">FlowConnectorView</a> o)</span>
                             throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitSwimlaneCellView(com.nomagic.magicdraw.uml.symbols.shapes.SwimlaneCellView)">
<h3>visitSwimlaneCellView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitSwimlaneCellView</span><wbr/><span class="parameters">(<a href="symbols/shapes/SwimlaneCellView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">SwimlaneCellView</a> o)</span>
                            throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitSwimlaneView(com.nomagic.magicdraw.uml.symbols.shapes.SwimlaneView)">
<h3>visitSwimlaneView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitSwimlaneView</span><wbr/><span class="parameters">(<a href="symbols/shapes/SwimlaneView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">SwimlaneView</a> o)</span>
                        throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTableShapeView(com.nomagic.magicdraw.uml.symbols.shapes.TableShapeView)">
<h3>visitTableShapeView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitTableShapeView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.TableShapeView o)</span>
                          throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTableCellView(com.nomagic.magicdraw.uml.symbols.shapes.TableCellView)">
<h3>visitTableCellView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitTableCellView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.TableCellView o)</span>
                         throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitSwimlaneHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.SwimlaneHeaderView)">
<h3>visitSwimlaneHeaderView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitSwimlaneHeaderView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.SwimlaneHeaderView o)</span>
                              throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInteractionUseView(com.nomagic.magicdraw.uml.symbols.shapes.InteractionUseView)">
<h3>visitInteractionUseView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitInteractionUseView</span><wbr/><span class="parameters">(<a href="symbols/shapes/InteractionUseView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">InteractionUseView</a> o)</span>
                              throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitFragmentView(com.nomagic.magicdraw.uml.symbols.shapes.FragmentView)">
<h3>visitFragmentView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitFragmentView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.FragmentView o)</span>
                        throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitStateInvariantView(com.nomagic.magicdraw.uml.symbols.shapes.StateInvariantView)">
<h3>visitStateInvariantView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitStateInvariantView</span><wbr/><span class="parameters">(<a href="symbols/shapes/StateInvariantView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">StateInvariantView</a> o)</span>
                              throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitStateInvariantHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.StateInvariantHeaderView)">
<h3>visitStateInvariantHeaderView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitStateInvariantHeaderView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.StateInvariantHeaderView o)</span>
                                    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitFrameView(com.nomagic.magicdraw.uml.symbols.shapes.FrameView)">
<h3>visitFrameView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitFrameView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.FrameView o)</span>
                     throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitCombinedFragmentView(com.nomagic.magicdraw.uml.symbols.shapes.CombinedFragmentView)">
<h3>visitCombinedFragmentView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitCombinedFragmentView</span><wbr/><span class="parameters">(<a href="symbols/shapes/CombinedFragmentView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">CombinedFragmentView</a> o)</span>
                                throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInteractionOperandView(com.nomagic.magicdraw.uml.symbols.shapes.InteractionOperandView)">
<h3>visitInteractionOperandView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitInteractionOperandView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.InteractionOperandView o)</span>
                                  throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitActionView(com.nomagic.magicdraw.uml.symbols.shapes.ActionView)">
<h3>visitActionView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitActionView</span><wbr/><span class="parameters">(<a href="symbols/shapes/ActionView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ActionView</a> o)</span>
                      throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitStructuredActivityNodeView(com.nomagic.magicdraw.uml.symbols.shapes.StructuredActivityNodeView)">
<h3>visitStructuredActivityNodeView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitStructuredActivityNodeView</span><wbr/><span class="parameters">(<a href="symbols/shapes/StructuredActivityNodeView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">StructuredActivityNodeView</a> o)</span>
                                      throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitActivityGroupView(com.nomagic.magicdraw.uml.symbols.shapes.ActivityGroupView)">
<h3>visitActivityGroupView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitActivityGroupView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.ActivityGroupView o)</span>
                             throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInterruptibleActivityRegionView(com.nomagic.magicdraw.uml.symbols.shapes.InterruptibleActivityRegionView)">
<h3>visitInterruptibleActivityRegionView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitInterruptibleActivityRegionView</span><wbr/><span class="parameters">(<a href="symbols/shapes/InterruptibleActivityRegionView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">InterruptibleActivityRegionView</a> o)</span>
                                           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitSequenceNodeView(com.nomagic.magicdraw.uml.symbols.shapes.SequenceNodeView)">
<h3>visitSequenceNodeView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitSequenceNodeView</span><wbr/><span class="parameters">(<a href="symbols/shapes/SequenceNodeView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">SequenceNodeView</a> o)</span>
                            throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitConditionalNodeView(com.nomagic.magicdraw.uml.symbols.shapes.ConditionalNodeView)">
<h3>visitConditionalNodeView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitConditionalNodeView</span><wbr/><span class="parameters">(<a href="symbols/shapes/ConditionalNodeView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ConditionalNodeView</a> o)</span>
                               throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitLoopNodeView(com.nomagic.magicdraw.uml.symbols.shapes.LoopNodeView)">
<h3>visitLoopNodeView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitLoopNodeView</span><wbr/><span class="parameters">(<a href="symbols/shapes/LoopNodeView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">LoopNodeView</a> o)</span>
                        throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitExpansionRegionView(com.nomagic.magicdraw.uml.symbols.shapes.ExpansionRegionView)">
<h3>visitExpansionRegionView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitExpansionRegionView</span><wbr/><span class="parameters">(<a href="symbols/shapes/ExpansionRegionView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ExpansionRegionView</a> o)</span>
                               throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitCallBehaviorActionView(com.nomagic.magicdraw.uml.symbols.shapes.CallBehaviorActionView)">
<h3>visitCallBehaviorActionView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitCallBehaviorActionView</span><wbr/><span class="parameters">(<a href="symbols/shapes/CallBehaviorActionView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">CallBehaviorActionView</a> o)</span>
                                  throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInteractionUseOverviewView(com.nomagic.magicdraw.uml.symbols.shapes.InteractionUseOverviewView)">
<h3>visitInteractionUseOverviewView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitInteractionUseOverviewView</span><wbr/><span class="parameters">(<a href="symbols/shapes/InteractionUseOverviewView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">InteractionUseOverviewView</a> o)</span>
                                      throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitOpaqueActionView(com.nomagic.magicdraw.uml.symbols.shapes.OpaqueActionView)">
<h3>visitOpaqueActionView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitOpaqueActionView</span><wbr/><span class="parameters">(<a href="symbols/shapes/OpaqueActionView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">OpaqueActionView</a> o)</span>
                            throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitCallOperationActionView(com.nomagic.magicdraw.uml.symbols.shapes.CallOperationActionView)">
<h3>visitCallOperationActionView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitCallOperationActionView</span><wbr/><span class="parameters">(<a href="symbols/shapes/CallOperationActionView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">CallOperationActionView</a> o)</span>
                                   throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitObjectFlowView(com.nomagic.magicdraw.uml.symbols.paths.ObjectFlowView)">
<h3>visitObjectFlowView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitObjectFlowView</span><wbr/><span class="parameters">(<a href="symbols/paths/ObjectFlowView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">ObjectFlowView</a> o)</span>
                          throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitControlFlowView(com.nomagic.magicdraw.uml.symbols.paths.ControlFlowView)">
<h3>visitControlFlowView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitControlFlowView</span><wbr/><span class="parameters">(<a href="symbols/paths/ControlFlowView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">ControlFlowView</a> o)</span>
                           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitBaseFlowView(com.nomagic.magicdraw.uml.symbols.paths.BaseFlowView)">
<h3>visitBaseFlowView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitBaseFlowView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.paths.BaseFlowView o)</span>
                        throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitExtensionView(com.nomagic.magicdraw.uml.symbols.paths.ExtensionView)">
<h3>visitExtensionView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitExtensionView</span><wbr/><span class="parameters">(<a href="symbols/paths/ExtensionView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">ExtensionView</a> o)</span>
                         throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitBaseLifelineView(com.nomagic.magicdraw.uml.symbols.shapes.BaseLifelineView)">
<h3>visitBaseLifelineView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitBaseLifelineView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.BaseLifelineView o)</span>
                            throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitLinkWithRolesView(com.nomagic.magicdraw.uml.symbols.paths.LinkWithRolesView)">
<h3>visitLinkWithRolesView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitLinkWithRolesView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.paths.LinkWithRolesView o)</span>
                             throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitLinkWithEndsView(com.nomagic.magicdraw.uml.symbols.paths.LinkWithEndsView)">
<h3>visitLinkWithEndsView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitLinkWithEndsView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.paths.LinkWithEndsView o)</span>
                            throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPartView(com.nomagic.magicdraw.uml.symbols.shapes.PartView)">
<h3>visitPartView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitPartView</span><wbr/><span class="parameters">(<a href="symbols/shapes/PartView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">PartView</a> o)</span>
                    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitCollaborationUseView(com.nomagic.magicdraw.uml.symbols.shapes.CollaborationUseView)">
<h3>visitCollaborationUseView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitCollaborationUseView</span><wbr/><span class="parameters">(<a href="symbols/shapes/CollaborationUseView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">CollaborationUseView</a> o)</span>
                                throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInteractionOperandsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.InteractionOperandsCompartmentView)">
<h3>visitInteractionOperandsCompartmentView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitInteractionOperandsCompartmentView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.InteractionOperandsCompartmentView o)</span>
                                              throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitRegionsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.RegionsCompartmentView)">
<h3>visitRegionsCompartmentView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitRegionsCompartmentView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.RegionsCompartmentView o)</span>
                                  throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitClauseCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.ClauseCompartmentView)">
<h3>visitClauseCompartmentView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitClauseCompartmentView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.ClauseCompartmentView o)</span>
                                 throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitBaseSplitCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.BaseSplitCompartmentView)">
<h3>visitBaseSplitCompartmentView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitBaseSplitCompartmentView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.BaseSplitCompartmentView o)</span>
                                    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitClassHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.ClassHeaderView)">
<h3>visitClassHeaderView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitClassHeaderView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.ClassHeaderView o)</span>
                           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInterfaceHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.InterfaceHeaderView)">
<h3>visitInterfaceHeaderView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitInterfaceHeaderView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.InterfaceHeaderView o)</span>
                               throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInformationItemHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.InformationItemHeaderView)">
<h3>visitInformationItemHeaderView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitInformationItemHeaderView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.InformationItemHeaderView o)</span>
                                     throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitExtensionPointsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.ExtensionPointsCompartmentView)">
<h3>visitExtensionPointsCompartmentView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitExtensionPointsCompartmentView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.ExtensionPointsCompartmentView o)</span>
                                          throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInterfacesCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.InterfacesCompartmentView)">
<h3>visitInterfacesCompartmentView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitInterfacesCompartmentView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.InterfacesCompartmentView o)</span>
                                     throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitRealizationsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.RealizationsCompartmentView)">
<h3>visitRealizationsCompartmentView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitRealizationsCompartmentView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.RealizationsCompartmentView o)</span>
                                       throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInternalStateCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.InternalStateCompartmentView)">
<h3>visitInternalStateCompartmentView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitInternalStateCompartmentView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.InternalStateCompartmentView o)</span>
                                        throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInstanceSlotsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.InstanceSlotsCompartmentView)">
<h3>visitInstanceSlotsCompartmentView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitInstanceSlotsCompartmentView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.InstanceSlotsCompartmentView o)</span>
                                        throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDeployedElementsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.DeployedElementsCompartmentView)">
<h3>visitDeployedElementsCompartmentView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitDeployedElementsCompartmentView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.DeployedElementsCompartmentView o)</span>
                                           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitCustomCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.CustomCompartmentView)">
<h3>visitCustomCompartmentView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitCustomCompartmentView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.CustomCompartmentView o)</span>
                                 throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitArtifactsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.ArtifactsCompartmentView)">
<h3>visitArtifactsCompartmentView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitArtifactsCompartmentView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.ArtifactsCompartmentView o)</span>
                                    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitConstraintsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.ConstraintsCompartmentView)">
<h3>visitConstraintsCompartmentView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitConstraintsCompartmentView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.ConstraintsCompartmentView o)</span>
                                      throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitLegendItemsCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.LegendItemsCompartmentView)">
<h3>visitLegendItemsCompartmentView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitLegendItemsCompartmentView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.LegendItemsCompartmentView o)</span>
                                      throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTaggedValuesCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.TaggedValuesCompartmentView)">
<h3>visitTaggedValuesCompartmentView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitTaggedValuesCompartmentView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.TaggedValuesCompartmentView o)</span>
                                       throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitCombinedFragmentHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.CombinedFragmentHeaderView)">
<h3>visitCombinedFragmentHeaderView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitCombinedFragmentHeaderView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.CombinedFragmentHeaderView o)</span>
                                      throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitFrameHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.FrameHeaderView)">
<h3>visitFrameHeaderView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitFrameHeaderView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.FrameHeaderView o)</span>
                           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitActionHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.ActionHeaderView)">
<h3>visitActionHeaderView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitActionHeaderView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.ActionHeaderView o)</span>
                            throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitStateHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.StateHeaderView)">
<h3>visitStateHeaderView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitStateHeaderView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.StateHeaderView o)</span>
                           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitBaseElementTextField(com.nomagic.magicdraw.uml.symbols.shapes.BaseElementTextField)">
<h3>visitBaseElementTextField</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitBaseElementTextField</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.BaseElementTextField o)</span>
                                throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitBaseElementTextArea(com.nomagic.magicdraw.uml.symbols.shapes.BaseElementTextArea)">
<h3>visitBaseElementTextArea</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitBaseElementTextArea</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.BaseElementTextArea o)</span>
                               throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitElementCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.ElementCompartmentView)">
<h3>visitElementCompartmentView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitElementCompartmentView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.ElementCompartmentView o)</span>
                                  throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitCustomElementCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.CustomElementCompartmentView)">
<h3>visitCustomElementCompartmentView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitCustomElementCompartmentView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.CustomElementCompartmentView o)</span>
                                        throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitConstraintCompartmentView(com.nomagic.magicdraw.uml.symbols.shapes.ConstraintCompartmentView)">
<h3>visitConstraintCompartmentView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitConstraintCompartmentView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.ConstraintCompartmentView o)</span>
                                     throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDirectionIconView(com.nomagic.magicdraw.uml.symbols.shapes.DirectionIconView)">
<h3>visitDirectionIconView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitDirectionIconView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.DirectionIconView o)</span>
                             throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitCollaborationHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.CollaborationHeaderView)">
<h3>visitCollaborationHeaderView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitCollaborationHeaderView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.CollaborationHeaderView o)</span>
                                   throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitStereotypeHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.StereotypeHeaderView)">
<h3>visitStereotypeHeaderView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitStereotypeHeaderView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.StereotypeHeaderView o)</span>
                                throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPackageHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.PackageHeaderView)">
<h3>visitPackageHeaderView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitPackageHeaderView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.PackageHeaderView o)</span>
                             throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitNoteHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.NoteHeaderView)">
<h3>visitNoteHeaderView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitNoteHeaderView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.NoteHeaderView o)</span>
                          throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitBaseNameHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.BaseNameHeaderView)">
<h3>visitBaseNameHeaderView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitBaseNameHeaderView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.BaseNameHeaderView o)</span>
                              throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInstanceSpecificationHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.InstanceSpecificationHeaderView)">
<h3>visitInstanceSpecificationHeaderView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitInstanceSpecificationHeaderView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.InstanceSpecificationHeaderView o)</span>
                                           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitNodeInstanceSpecificationHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.NodeInstanceSpecificationHeaderView)">
<h3>visitNodeInstanceSpecificationHeaderView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitNodeInstanceSpecificationHeaderView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.NodeInstanceSpecificationHeaderView o)</span>
                                               throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTypedElementHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.TypedElementHeaderView)">
<h3>visitTypedElementHeaderView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitTypedElementHeaderView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.TypedElementHeaderView o)</span>
                                  throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPartHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.PartHeaderView)">
<h3>visitPartHeaderView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitPartHeaderView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.PartHeaderView o)</span>
                          throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitBaseLifelineHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.BaseLifelineHeaderView)">
<h3>visitBaseLifelineHeaderView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitBaseLifelineHeaderView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.BaseLifelineHeaderView o)</span>
                                  throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitGeneralizationSetView(com.nomagic.magicdraw.uml.symbols.shapes.GeneralizationSetView)">
<h3>visitGeneralizationSetView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitGeneralizationSetView</span><wbr/><span class="parameters">(<a href="symbols/shapes/GeneralizationSetView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">GeneralizationSetView</a> o)</span>
                                 throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitGeneralizationSetHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.GeneralizationSetHeaderView)">
<h3>visitGeneralizationSetHeaderView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitGeneralizationSetHeaderView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.GeneralizationSetHeaderView o)</span>
                                       throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitElementTaggedValueView(com.nomagic.magicdraw.uml.symbols.shapes.ElementTaggedValueView)">
<h3>visitElementTaggedValueView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitElementTaggedValueView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.ElementTaggedValueView o)</span>
                                  throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInformationFlowView(com.nomagic.magicdraw.uml.symbols.paths.InformationFlowView)">
<h3>visitInformationFlowView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitInformationFlowView</span><wbr/><span class="parameters">(<a href="symbols/paths/InformationFlowView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">InformationFlowView</a> informationFlowView)</span>
                               throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInformationItemView(com.nomagic.magicdraw.uml.symbols.shapes.InformationItemView)">
<h3>visitInformationItemView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitInformationItemView</span><wbr/><span class="parameters">(<a href="symbols/shapes/InformationItemView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">InformationItemView</a> informationItemView)</span>
                               throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDiagramFrameView(com.nomagic.magicdraw.uml.symbols.shapes.DiagramFrameView)">
<h3>visitDiagramFrameView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitDiagramFrameView</span><wbr/><span class="parameters">(<a href="symbols/shapes/DiagramFrameView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">DiagramFrameView</a> diagramFrameView)</span>
                            throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDiagramFrameHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.DiagramFrameHeaderView)">
<h3>visitDiagramFrameHeaderView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitDiagramFrameHeaderView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.DiagramFrameHeaderView diagramFrameHeaderView)</span>
                                  throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDiagramFrameLabelView(com.nomagic.magicdraw.uml.symbols.shapes.DiagramFrameLabelView)">
<h3>visitDiagramFrameLabelView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitDiagramFrameLabelView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.DiagramFrameLabelView diagramFrameLabelView)</span>
                                 throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitCallBehaviorActionHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.CallBehaviorActionHeaderView)">
<h3>visitCallBehaviorActionHeaderView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitCallBehaviorActionHeaderView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.CallBehaviorActionHeaderView callBehaviorActionHeaderView)</span>
                                        throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitBehaviorLabelView(com.nomagic.magicdraw.uml.symbols.shapes.BehaviorLabelView)">
<h3>visitBehaviorLabelView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitBehaviorLabelView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.BehaviorLabelView behaviorLabelView)</span>
                             throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitObjectNodeViewHeaderView(com.nomagic.magicdraw.uml.symbols.shapes.ObjectNodeViewHeaderView)">
<h3>visitObjectNodeViewHeaderView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitObjectNodeViewHeaderView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.ObjectNodeViewHeaderView objectNodeViewHeaderView)</span>
                                    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitOperationTextArea(com.nomagic.magicdraw.uml.symbols.shapes.OperationTextArea)">
<h3>visitOperationTextArea</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitOperationTextArea</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.OperationTextArea operationTextArea)</span>
                             throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTriggerLabelView(com.nomagic.magicdraw.uml.symbols.shapes.TriggerLabelView)">
<h3>visitTriggerLabelView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitTriggerLabelView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.TriggerLabelView triggerLabelView)</span>
                            throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTransitionLabelView(com.nomagic.magicdraw.uml.symbols.shapes.TransitionLabelView)">
<h3>visitTransitionLabelView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitTransitionLabelView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.TransitionLabelView transitionLabelView)</span>
                               throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitAbstractImageShapeView(com.nomagic.magicdraw.uml.symbols.shapes.AbstractImageShapeView)">
<h3>visitAbstractImageShapeView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitAbstractImageShapeView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.AbstractImageShapeView imageShapeView)</span>
                                  throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitEmbeddedImageShapeView(com.nomagic.magicdraw.uml.symbols.shapes.EmbeddedImageShapeView)">
<h3>visitEmbeddedImageShapeView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitEmbeddedImageShapeView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.EmbeddedImageShapeView imageShapeView)</span>
                                  throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitImageShapeView(com.nomagic.magicdraw.uml.symbols.shapes.ImageShapeView)">
<h3>visitImageShapeView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitImageShapeView</span><wbr/><span class="parameters">(<a href="symbols/shapes/ImageShapeView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ImageShapeView</a> imageShapeView)</span>
                          throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Visits image shape view.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>imageShapeView</code> - - image shape view.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitImageShapeFromElementView(com.nomagic.magicdraw.uml.symbols.shapes.ImageShapeFromElementView)">
<h3>visitImageShapeFromElementView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitImageShapeFromElementView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.ImageShapeFromElementView imageShapeView)</span>
                                     throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitLostFoundMessageView(com.nomagic.magicdraw.uml.symbols.paths.LostFoundMessageView)">
<h3>visitLostFoundMessageView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitLostFoundMessageView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.paths.LostFoundMessageView lostFoundMessageView)</span>
                                throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Visits lost/found message view.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>lostFoundMessageView</code> - - lost/found message view.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitFoundMessageView(com.nomagic.magicdraw.uml.symbols.paths.FoundMessageView)">
<h3>visitFoundMessageView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitFoundMessageView</span><wbr/><span class="parameters">(<a href="symbols/paths/FoundMessageView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">FoundMessageView</a> foundMessageView)</span>
                            throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Visits found message view.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>foundMessageView</code> - - found message view.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitLostMessageView(com.nomagic.magicdraw.uml.symbols.paths.LostMessageView)">
<h3>visitLostMessageView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitLostMessageView</span><wbr/><span class="parameters">(<a href="symbols/paths/LostMessageView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">LostMessageView</a> lostMessageView)</span>
                           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Visits lost message view.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>lostMessageView</code> - - lost message view.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPrimitiveTaggedValueView(com.nomagic.magicdraw.uml.symbols.shapes.PrimitiveTaggedValueView)">
<h3>visitPrimitiveTaggedValueView</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitPrimitiveTaggedValueView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.PrimitiveTaggedValueView primitiveTaggedValueView)</span>
                                    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
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
