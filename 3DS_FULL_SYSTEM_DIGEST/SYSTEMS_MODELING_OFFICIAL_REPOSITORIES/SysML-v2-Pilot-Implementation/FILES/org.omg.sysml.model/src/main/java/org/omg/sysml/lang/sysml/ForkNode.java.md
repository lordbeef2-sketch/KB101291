# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/ForkNode.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/ForkNode.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/ForkNode.java
- source_bytes: 690
- source_sha256: `390f0c283e89ed5dfe9b3d741c48cac0e5b3af621fac4ba74da57e7eed470548`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/**
 */
package org.omg.sysml.lang.sysml;


/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Fork Node</b></em>'.
 * <!-- end-user-doc -->
 *
 * <!-- begin-model-doc -->
 * <p>A <code>ForkNode</code> is a <code>ControlNode</code> that must be followed by successor <code>Actions</code> as given by all its outgoing <code>Successions</code>.</p>
 * targetConnector->selectByKind(Succession)->size() <= 1
 * specializesFromLibrary('Actions::Action::forks')
 * <!-- end-model-doc -->
 *
 *
 * @see org.omg.sysml.lang.sysml.SysMLPackage#getForkNode()
 * @model
 * @generated
 */
public interface ForkNode extends ControlNode {
} // ForkNode

````
