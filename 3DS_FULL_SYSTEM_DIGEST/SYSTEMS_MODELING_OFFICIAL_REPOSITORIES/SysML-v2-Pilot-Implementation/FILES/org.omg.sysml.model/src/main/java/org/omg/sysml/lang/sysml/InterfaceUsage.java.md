# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/InterfaceUsage.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/InterfaceUsage.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/InterfaceUsage.java
- source_bytes: 2128
- source_sha256: `3c17937f0d4e38f7f1c204d0188a5427f36b6d62768d7ad69291630df8fe0c24`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/**
 */
package org.omg.sysml.lang.sysml;

import org.eclipse.emf.common.util.EList;

/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Interface Usage</b></em>'.
 * <!-- end-user-doc -->
 *
 * <!-- begin-model-doc -->
 * <p>An <code>InterfaceUsage</code> is a Usage of an <code>InterfaceDefinition</code> to represent an interface connecting parts of a system through specific ports.</p>
 * ownedEndFeature->size() = 2 implies
 *     specializesFromLibrary('Interfaces::binaryInterfaces')
 * specializesFromLibrary('Interfaces::interfaces')
 * <!-- end-model-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 *   <li>{@link org.omg.sysml.lang.sysml.InterfaceUsage#getInterfaceDefinition <em>Interface Definition</em>}</li>
 * </ul>
 *
 * @see org.omg.sysml.lang.sysml.SysMLPackage#getInterfaceUsage()
 * @model
 * @generated
 */
public interface InterfaceUsage extends ConnectionUsage {
	/**
	 * Returns the value of the '<em><b>Interface Definition</b></em>' reference list.
	 * The list contents are of type {@link org.omg.sysml.lang.sysml.InterfaceDefinition}.
	 * <p>
	 * This feature redefines the following features:
	 * </p>
	 * <ul>
	 *   <li>'{@link org.omg.sysml.lang.sysml.ConnectionUsage#getConnectionDefinition() <em>Connection Definition</em>}'</li>
	 * </ul>
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * <!-- begin-model-doc -->
	 * <p>The <code>InterfaceDefinitions</code> that type this <code>InterfaceUsage</code>.</p>
	 * <!-- end-model-doc -->
	 * @return the value of the '<em>Interface Definition</em>' reference list.
	 * @see org.omg.sysml.lang.sysml.SysMLPackage#getInterfaceUsage_InterfaceDefinition()
	 * @model transient="true" volatile="true" derived="true" ordered="false"
	 *        annotation="http://schema.omg.org/spec/MOF/2.0/emof.xml#Property.oppositeRoleName body='definedInterface'"
	 *        annotation="redefines"
	 *        annotation="http://www.omg.org/spec/SysML"
	 * @generated
	 */
	EList<InterfaceDefinition> getInterfaceDefinition();

} // InterfaceUsage

````
