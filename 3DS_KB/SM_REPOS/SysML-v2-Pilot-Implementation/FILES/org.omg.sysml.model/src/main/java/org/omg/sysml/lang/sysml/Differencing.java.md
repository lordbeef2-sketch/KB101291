# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/Differencing.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/Differencing.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/Differencing.java
- source_bytes: 4069
- source_sha256: `8922866b5aac92ee34ad6ee03c8c03bf18c41bdf75bfa13860c5505753bc48bb`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/**
 */
package org.omg.sysml.lang.sysml;


/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Differencing</b></em>'.
 * <!-- end-user-doc -->
 *
 * <!-- begin-model-doc -->
 * <p><code>Differencing</code> is a <code>Relationship</code> that makes its <code>differencingType</code> one of the <code>differencingTypes</code> of its <code>typeDifferenced</code>.</p>
 * 
 * <!-- end-model-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 *   <li>{@link org.omg.sysml.lang.sysml.Differencing#getDifferencingType <em>Differencing Type</em>}</li>
 *   <li>{@link org.omg.sysml.lang.sysml.Differencing#getTypeDifferenced <em>Type Differenced</em>}</li>
 * </ul>
 *
 * @see org.omg.sysml.lang.sysml.SysMLPackage#getDifferencing()
 * @model
 * @generated
 */
public interface Differencing extends Relationship {
	/**
	 * Returns the value of the '<em><b>Differencing Type</b></em>' reference.
	 * <p>
	 * This feature redefines the following features:
	 * </p>
	 * <ul>
	 *   <li>'{@link org.omg.sysml.lang.sysml.Relationship#getTarget() <em>Target</em>}'</li>
	 * </ul>
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * <!-- begin-model-doc -->
	 * <p><code>Type</code> that partly determines interpretations of <code>typeDifferenced</code>, as described in <code>Type::differencingType</code>.</p>
	 * 
	 * <!-- end-model-doc -->
	 * @return the value of the '<em>Differencing Type</em>' reference.
	 * @see #setDifferencingType(Type)
	 * @see org.omg.sysml.lang.sysml.SysMLPackage#getDifferencing_DifferencingType()
	 * @model required="true" ordered="false"
	 *        annotation="http://schema.omg.org/spec/MOF/2.0/emof.xml#Property.oppositeRoleName body='differencedDifferencing'"
	 *        annotation="redefines"
	 * @generated
	 */
	Type getDifferencingType();

	/**
	 * Sets the value of the '{@link org.omg.sysml.lang.sysml.Differencing#getDifferencingType <em>Differencing Type</em>}' reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Differencing Type</em>' reference.
	 * @see #getDifferencingType()
	 * @generated
	 */
	void setDifferencingType(Type value);

	/**
	 * Returns the value of the '<em><b>Type Differenced</b></em>' reference.
	 * It is bidirectional and its opposite is '{@link org.omg.sysml.lang.sysml.Type#getOwnedDifferencing <em>Owned Differencing</em>}'.
	 * <p>
	 * This feature subsets the following features:
	 * </p>
	 * <ul>
	 *   <li>'{@link org.omg.sysml.lang.sysml.Relationship#getOwningRelatedElement() <em>Owning Related Element</em>}'</li>
	 * </ul>
	 * <p>
	 * This feature redefines the following features:
	 * </p>
	 * <ul>
	 *   <li>'{@link org.omg.sysml.lang.sysml.Relationship#getSource() <em>Source</em>}'</li>
	 * </ul>
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * <!-- begin-model-doc -->
	 * <p><code>Type</code> with interpretations partly determined by <code>differencingType</code>, as described in <code>Type::differencingType</code>.</p>
	 * 
	 * <!-- end-model-doc -->
	 * @return the value of the '<em>Type Differenced</em>' reference.
	 * @see #setTypeDifferenced(Type)
	 * @see org.omg.sysml.lang.sysml.SysMLPackage#getDifferencing_TypeDifferenced()
	 * @see org.omg.sysml.lang.sysml.Type#getOwnedDifferencing
	 * @model opposite="ownedDifferencing" required="true" transient="true" volatile="true" derived="true" ordered="false"
	 *        annotation="redefines"
	 *        annotation="subsets"
	 *        annotation="http://www.omg.org/spec/SysML"
	 * @generated
	 */
	Type getTypeDifferenced();

	/**
	 * Sets the value of the '{@link org.omg.sysml.lang.sysml.Differencing#getTypeDifferenced <em>Type Differenced</em>}' reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Type Differenced</em>' reference.
	 * @see #getTypeDifferenced()
	 * @generated
	 */
	void setTypeDifferenced(Type value);

} // Differencing

````
