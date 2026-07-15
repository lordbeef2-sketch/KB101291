# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/InterfaceDefinition.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/InterfaceDefinition.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/InterfaceDefinition.java
- source_bytes: 2156
- source_sha256: `8a2dcd052b2b41c2692b7bea5a81a69f1079bbe42c3c250f9dff9e385b094b8a`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/**
 */
package org.omg.sysml.lang.sysml;

import org.eclipse.emf.common.util.EList;

/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Interface Definition</b></em>'.
 * <!-- end-user-doc -->
 *
 * <!-- begin-model-doc -->
 * <p>An <code>InterfaceDefinition</code> is a <code>ConnectionDefinition</code> all of whose ends are <code>PortUsages</code>, defining an interface between elements that interact through such ports.</p>
 * specializesFromLibrary('Interfaces::Interface')
 * ownedEndFeature->size() = 2 implies
 *     specializesFromLibrary('Interfaces::BinaryInterface')
 * <!-- end-model-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 *   <li>{@link org.omg.sysml.lang.sysml.InterfaceDefinition#getInterfaceEnd <em>Interface End</em>}</li>
 * </ul>
 *
 * @see org.omg.sysml.lang.sysml.SysMLPackage#getInterfaceDefinition()
 * @model
 * @generated
 */
public interface InterfaceDefinition extends ConnectionDefinition {
	/**
	 * Returns the value of the '<em><b>Interface End</b></em>' reference list.
	 * The list contents are of type {@link org.omg.sysml.lang.sysml.PortUsage}.
	 * <p>
	 * This feature redefines the following features:
	 * </p>
	 * <ul>
	 *   <li>'{@link org.omg.sysml.lang.sysml.ConnectionDefinition#getConnectionEnd() <em>Connection End</em>}'</li>
	 * </ul>
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * <!-- begin-model-doc -->
	 * <p>The <code>PortUsages</code> that are the <code>connectionEnds</code> of this <code>InterfaceDefinition</code>.
	 * 
	 * 
	 * <!-- end-model-doc -->
	 * @return the value of the '<em>Interface End</em>' reference list.
	 * @see org.omg.sysml.lang.sysml.SysMLPackage#getInterfaceDefinition_InterfaceEnd()
	 * @model transient="true" volatile="true" derived="true"
	 *        annotation="http://schema.omg.org/spec/MOF/2.0/emof.xml#Property.oppositeRoleName body='interfaceDefinitionWithEnd'"
	 *        annotation="redefines"
	 *        annotation="http://www.omg.org/spec/SysML"
	 * @generated
	 */
	EList<PortUsage> getInterfaceEnd();

} // InterfaceDefinition

````
