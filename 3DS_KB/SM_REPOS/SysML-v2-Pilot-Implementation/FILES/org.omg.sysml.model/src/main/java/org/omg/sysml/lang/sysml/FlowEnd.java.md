# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/FlowEnd.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/FlowEnd.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/FlowEnd.java
- source_bytes: 1065
- source_sha256: `4f0f8eec43f9d862c5323da48cb9a6a69711101bb4913307bb20ff180a95a3e1`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/**
 */
package org.omg.sysml.lang.sysml;


/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Flow End</b></em>'.
 * <!-- end-user-doc -->
 *
 * <!-- begin-model-doc -->
 * <p>A <code>FlowEnd</code> is a <code>Feature</code> that is one of the <code>connectorEnds</code> giving the <code><em>source</em></code> or <code><em>target</em></code> of a <code>Flow</code>. For <code>Flows</code> typed by <code><em>FlowTransfer</em></code> or its specializations, <code>FlowEnds</code> must have exactly one <code>ownedFeature</code>, which redefines <code><em>Transfer::source::sourceOutput</em></code> or <code><em>Transfer::target::targetInput</em></code> and redefines the corresponding feature of the <code>relatedElement</code> for its end.</p>
 * isEnd
 * ownedFeature->size() = 1
 * owningType <> null and owningType.oclIsKindOf(Flow)
 * <!-- end-model-doc -->
 *
 *
 * @see org.omg.sysml.lang.sysml.SysMLPackage#getFlowEnd()
 * @model
 * @generated
 */
public interface FlowEnd extends Feature {
} // FlowEnd

````
