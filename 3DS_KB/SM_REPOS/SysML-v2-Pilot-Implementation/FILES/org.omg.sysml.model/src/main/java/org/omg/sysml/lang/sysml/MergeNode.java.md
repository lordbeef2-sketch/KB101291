# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/MergeNode.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/MergeNode.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/MergeNode.java
- source_bytes: 1069
- source_sha256: `a25f22dd142d5ae62f4e48e0a4e0338cf09917e49fd37c534166b15833d0e0b9`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/**
 */
package org.omg.sysml.lang.sysml;


/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Merge Node</b></em>'.
 * <!-- end-user-doc -->
 *
 * <!-- begin-model-doc -->
 * <p>A <code>MergeNode</code> is a <code>ControlNode</code> that asserts the merging of its incoming <code>Successions</code>. A <code>MergeNode</code> may have at most one outgoing <code>Successions</code>.</p>
 * sourceConnector->selectAsKind(Succession)->size() <= 1
 * targetConnector->selectByKind(Succession)->
 *     collect(connectorEnd->at(1))->
 *     forAll(sourceMult |
 *         multiplicityHasBounds(sourceMult, 0, 1))
 * targetConnector->selectByKind(Succession)->
 *     forAll(subsetsChain(self, 
 *         resolveGlobal('ControlPerformances::MergePerformance::incomingHBLink')))
 * specializesFromLibrary('Actions::Action::merges')
 * <!-- end-model-doc -->
 *
 *
 * @see org.omg.sysml.lang.sysml.SysMLPackage#getMergeNode()
 * @model
 * @generated
 */
public interface MergeNode extends ControlNode {
} // MergeNode

````
