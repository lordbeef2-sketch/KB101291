# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/BindingConnector.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/BindingConnector.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/BindingConnector.java
- source_bytes: 692
- source_sha256: `0cc83d7f999e576c57babc1abd61115bd2d8d88b6c6dae83d41549c25411367a`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/**
 */
package org.omg.sysml.lang.sysml;


/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Binding Connector</b></em>'.
 * <!-- end-user-doc -->
 *
 * <!-- begin-model-doc -->
 * <p>A <code>BindingConnector</code> is a binary <code>Connector</code> that requires its <code>relatedFeatures</code> to identify the same things (have the same values).</p>
 * 
 * relatedFeature->size() = 2
 * specializesFromLibrary('Links::selfLinks')
 * <!-- end-model-doc -->
 *
 *
 * @see org.omg.sysml.lang.sysml.SysMLPackage#getBindingConnector()
 * @model
 * @generated
 */
public interface BindingConnector extends Connector {
} // BindingConnector

````
