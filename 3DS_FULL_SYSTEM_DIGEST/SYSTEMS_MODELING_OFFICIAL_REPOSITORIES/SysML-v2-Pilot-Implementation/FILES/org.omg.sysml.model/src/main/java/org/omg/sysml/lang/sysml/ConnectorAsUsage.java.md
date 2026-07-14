# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/ConnectorAsUsage.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/ConnectorAsUsage.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/ConnectorAsUsage.java
- source_bytes: 811
- source_sha256: `a7c176ce91c4abdf702711084ecab2354409c5a32311fd8d372254303d352ae9`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/**
 */
package org.omg.sysml.lang.sysml;


/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Connector As Usage</b></em>'.
 * <!-- end-user-doc -->
 *
 * <!-- begin-model-doc -->
 * <p>A <code>ConnectorAsUsage</code> is both a <code>Connector</code> and a <code>Usage</code>. <code>ConnectorAsUsage</code> cannot itself be instantiated in a SysML model, but it is a base class for the concrete classes <code>BindingConnectorAsUsage</code>, <code>SuccessionAsUsage</code>, <code>ConnectionUsage</code> and <code>FlowUsage</code>.</p>
 * <!-- end-model-doc -->
 *
 *
 * @see org.omg.sysml.lang.sysml.SysMLPackage#getConnectorAsUsage()
 * @model abstract="true"
 * @generated
 */
public interface ConnectorAsUsage extends Usage, Connector {
} // ConnectorAsUsage

````
