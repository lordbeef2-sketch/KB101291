# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/Dependency.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/Dependency.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/Dependency.java
- source_bytes: 3197
- source_sha256: `f5078065e4652cfdbcee76398df27a1db8c6dfb7d1df181541441a97115c592c`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/**
 */
package org.omg.sysml.lang.sysml;

import org.eclipse.emf.common.util.EList;

/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Dependency</b></em>'.
 * <!-- end-user-doc -->
 *
 * <!-- begin-model-doc -->
 * <p>A <code>Dependency</code> is a <code>Relationship</code> that indicates that one or more <code>client</code> <code>Elements</code> require one more <code>supplier</code> <code>Elements</code> for their complete specification. In general, this means that a change to one of the <code>supplier</code> <code>Elements</code> may necessitate a change to, or re-specification of, the <code>client</code> <code>Elements</code>.</p>
 * 
 * <p>Note that a <code>Dependency</code> is entirely a model-level <code>Relationship</code>, without instance-level semantics.</p>
 * <!-- end-model-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 *   <li>{@link org.omg.sysml.lang.sysml.Dependency#getClient <em>Client</em>}</li>
 *   <li>{@link org.omg.sysml.lang.sysml.Dependency#getSupplier <em>Supplier</em>}</li>
 * </ul>
 *
 * @see org.omg.sysml.lang.sysml.SysMLPackage#getDependency()
 * @model
 * @generated
 */
public interface Dependency extends Relationship {
	/**
	 * Returns the value of the '<em><b>Client</b></em>' reference list.
	 * The list contents are of type {@link org.omg.sysml.lang.sysml.Element}.
	 * <p>
	 * This feature redefines the following features:
	 * </p>
	 * <ul>
	 *   <li>'{@link org.omg.sysml.lang.sysml.Relationship#getSource() <em>Source</em>}'</li>
	 * </ul>
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * <!-- begin-model-doc -->
	 * <p>The <code>Element</code> or <code>Elements</code> dependent on the <code>supplier</code> <code>Elements</code>.</p>
	 * <!-- end-model-doc -->
	 * @return the value of the '<em>Client</em>' reference list.
	 * @see org.omg.sysml.lang.sysml.SysMLPackage#getDependency_Client()
	 * @model required="true"
	 *        annotation="http://schema.omg.org/spec/MOF/2.0/emof.xml#Property.oppositeRoleName body='clientDependency'"
	 *        annotation="redefines"
	 * @generated
	 */
	EList<Element> getClient();

	/**
	 * Returns the value of the '<em><b>Supplier</b></em>' reference list.
	 * The list contents are of type {@link org.omg.sysml.lang.sysml.Element}.
	 * <p>
	 * This feature redefines the following features:
	 * </p>
	 * <ul>
	 *   <li>'{@link org.omg.sysml.lang.sysml.Relationship#getTarget() <em>Target</em>}'</li>
	 * </ul>
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * <!-- begin-model-doc -->
	 * <p>The <code>Element</code> or <code>Elements</code> on which the <code>client</code> <code>Elements</code> depend in some respect.</p>
	 * <!-- end-model-doc -->
	 * @return the value of the '<em>Supplier</em>' reference list.
	 * @see org.omg.sysml.lang.sysml.SysMLPackage#getDependency_Supplier()
	 * @model required="true"
	 *        annotation="http://schema.omg.org/spec/MOF/2.0/emof.xml#Property.oppositeRoleName body='supplierDependency'"
	 *        annotation="redefines"
	 * @generated
	 */
	EList<Element> getSupplier();

} // Dependency

````
