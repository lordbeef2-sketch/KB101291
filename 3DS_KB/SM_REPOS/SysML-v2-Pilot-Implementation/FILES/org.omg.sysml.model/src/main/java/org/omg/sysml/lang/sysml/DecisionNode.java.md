# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/DecisionNode.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/DecisionNode.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/DecisionNode.java
- source_bytes: 1009
- source_sha256: `eb8156025bf6a4cf04b0addf31807bc018ad717605b8dd98df9f6f70417320e2`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/**
 */
package org.omg.sysml.lang.sysml;


/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Decision Node</b></em>'.
 * <!-- end-user-doc -->
 *
 * <!-- begin-model-doc -->
 * <p>A <code>DecisionNode</code> is a <code>ControlNode</code> that makes a selection from its outgoing <code>Successions</code>.</p>
 * targetConnector->selectByKind(Succession)->size() <= 1
 * sourceConnector->selectAsKind(Succession)->
 *     collect(connectorEnd->at(2))->
 *     forAll(targetMult |
 *         multiplicityHasBounds(targetMult, 0, 1))
 * specializesFromLibrary('Actions::Action::decisions')
 * sourceConnector->selectByKind(Succession)->
 *     forAll(subsetsChain(self, 
 *         resolveGlobal('ControlPerformances::DecisionPerformance::outgoingHBLink')))
 * <!-- end-model-doc -->
 *
 *
 * @see org.omg.sysml.lang.sysml.SysMLPackage#getDecisionNode()
 * @model
 * @generated
 */
public interface DecisionNode extends ControlNode {
} // DecisionNode

````
