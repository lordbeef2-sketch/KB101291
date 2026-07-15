# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/Succession.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/Succession.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/Succession.java
- source_bytes: 623
- source_sha256: `dbdcb499dd0955a251a6e8388f4390a640131b86c6de0069e2b8ab4bc42f7220`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/**
 */
package org.omg.sysml.lang.sysml;


/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Succession</b></em>'.
 * <!-- end-user-doc -->
 *
 * <!-- begin-model-doc -->
 * <p>A <code>Succession</code> is a binary <code>Connector</code> that requires its <code>relatedFeatures</code> to happen separately in time.</p>
 * 
 * specializesFromLibrary('Occurrences::happensBeforeLinks')
 * <!-- end-model-doc -->
 *
 *
 * @see org.omg.sysml.lang.sysml.SysMLPackage#getSuccession()
 * @model
 * @generated
 */
public interface Succession extends Connector {
} // Succession

````
