# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/SuccessionFlow.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/SuccessionFlow.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/SuccessionFlow.java
- source_bytes: 807
- source_sha256: `10dcc6a7e678678b9ff74acebf83979bd4b72061c450f355677d32171202c6e5`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/**
 */
package org.omg.sysml.lang.sysml;


/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Succession Flow</b></em>'.
 * <!-- end-user-doc -->
 *
 * <!-- begin-model-doc -->
 * <p>A <code>SuccessionFlow</code> is a <code>Flow</code> that also provides temporal ordering. It classifies <code><em>Transfers</em></code> that cannot start until the source <code><em>Occurrence</em></code> has completed and that must complete before the target <code><em>Occurrence</em></code> can start.</p>
 * specializesFromLibrary('Transfers::flowTransfersBefore')
 * <!-- end-model-doc -->
 *
 *
 * @see org.omg.sysml.lang.sysml.SysMLPackage#getSuccessionFlow()
 * @model
 * @generated
 */
public interface SuccessionFlow extends Flow, Succession {
} // SuccessionFlow

````
