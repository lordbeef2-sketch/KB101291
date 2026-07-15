# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/LibraryPackage.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/LibraryPackage.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/LibraryPackage.java
- source_bytes: 2007
- source_sha256: `011fe6dd3fe45f3962bfdc5d8ea35b99d1332ae5fbba97daddc01683db269633`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/**
 */
package org.omg.sysml.lang.sysml;


/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Library Package</b></em>'.
 * <!-- end-user-doc -->
 *
 * <!-- begin-model-doc -->
 * <p>A <code>LibraryPackage</code> is a <code>Package</code> that is the container for a model library. A <code>LibraryPackage</code> is itself a library <code>Element</code> as are all <code>Elements</code> that are directly or indirectly contained in it.</p>
 * 
 * <!-- end-model-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 *   <li>{@link org.omg.sysml.lang.sysml.LibraryPackage#isStandard <em>Is Standard</em>}</li>
 * </ul>
 *
 * @see org.omg.sysml.lang.sysml.SysMLPackage#getLibraryPackage()
 * @model
 * @generated
 */
public interface LibraryPackage extends org.omg.sysml.lang.sysml.Package {
	/**
	 * Returns the value of the '<em><b>Is Standard</b></em>' attribute.
	 * The default value is <code>"false"</code>.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * <!-- begin-model-doc -->
	 * <p>Whether this <code>LibraryPackage</code> contains a standard library model. This should only be set to true for <code>LibraryPackages</code> in the standard Kernel Model Libraries or in normative model libraries for a language built on KerML.</p>
	 * <!-- end-model-doc -->
	 * @return the value of the '<em>Is Standard</em>' attribute.
	 * @see #setIsStandard(boolean)
	 * @see org.omg.sysml.lang.sysml.SysMLPackage#getLibraryPackage_IsStandard()
	 * @model default="false" required="true" ordered="false"
	 * @generated
	 */
	boolean isStandard();

	/**
	 * Sets the value of the '{@link org.omg.sysml.lang.sysml.LibraryPackage#isStandard <em>Is Standard</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Is Standard</em>' attribute.
	 * @see #isStandard()
	 * @generated
	 */
	void setIsStandard(boolean value);

} // LibraryPackage

````
